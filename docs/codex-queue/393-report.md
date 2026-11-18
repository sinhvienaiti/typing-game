# Phiếu 393 — Hoạt ảnh nhân vật khi gõ chữ và tung chiêu

## Tóm tắt cho chủ dự án

Nên dựng một bộ chuyển động theo **hành động và vũ khí**, rồi ghép thủ ấn, nhịp cơ thể và chất liệu của từng hệ. Không làm một bộ clip riêng cho mọi tổ hợp vũ khí × hệ. Khi gõ, nhân vật dần tụ lực; mỗi chữ đúng nối một cử động nhỏ; chữ cuối phát chiêu trong ≤ 50 ms. Phi kiếm tự đánh chỉ cần cử chỉ dẫn kiếm nhẹ, không liên tục giành toàn thân với chiêu người chơi.

Kiểm trực tiếp GLB: Lam mặc định của lab có **31 xương, 13 clip, không có xương ngón**; không thể diễn thủ ấn thật. Người thử nghiệm `human` có **66 khớp, đủ ba đốt mỗi ngón**, phù hợp thử trước. Chưa tìm thấy GLB nữ kiếm tu hoàn chỉnh trong cây game đã khảo sát. Model thật cần giữ một skeleton cho mọi trang phục theo D63, đúng bốn xương phụ; dải lụa và hào quang thuộc VFX.

Báo cáo có bản đồ trạng thái, **10 thủ ấn**, nhịp chân–hông–tay cho các họ chiêu và kế hoạch từng đợt. Đợt đầu chỉ thử một chiêu kiếm, hai thủ thế và lỗi/đổi đích trên rig `human`; chưa mở rộng tám hệ. Mục tiêu là chứng minh thân có diễn xuất, nhìn rõ ở camera chơi và không trễ phím.

Lối chơi Gemini là phương án đang xét, chưa thay canon: phần chuỗi từ và Space khai ấn được tách riêng. Các số thời gian dưới đây là đề xuất cần đo, không phải kết quả chạy. Chưa dựng, chưa chấm hình; mức nhận cuối vẫn là hai giám khảo độc lập cùng ≥ 9, từng mục ≥ 8,5 và chủ dự án xem cuối.

## 1. Phạm vi, căn cứ và điểm chưa chốt

Ngày đọc: **16/11/2026**. Phiếu đã có phản biện PASS của Sonnet; đây là nghiên cứu theo phiếu, không mở thêm làn hay gửi thêm trợ lý. Chỉ ghi file báo cáo này. Không chạy build/test/game, không sửa model, rig, mã hoặc tài liệu Tu Tiên, không tạo media, không tải gói tài sản. Hạn mức đọc đầu lượt: đã dùng 21%, còn 79%; không gặp giới hạn công cụ.

| Căn cứ đã đọc | Điều dùng trong báo cáo |
|---|---|
| [Skill hoạt ảnh](../../.agents/skills/game-character-animation/SKILL.md) và bốn tài liệu `references/` | Rig profile, chuyển xương, thứ tự lớp, thời điểm phát, probe và chấm chuyển động |
| [Hợp đồng hoạt ảnh](../games/CHARACTER_ANIMATION.md) §5.3–5.11; [chuẩn dùng chung](../games/SHARED_SYSTEMS_BAR.md) §2–5 | Một clip hành động chứa gồng–nhả–thu; sự kiện nhìn không quyết sát thương; chuẩn 9 |
| [Kế hoạch chuyển động](../games/tu-tien/MOTION_PLAN.md), gồm kết quả vòng 1–4 | Không lặp lại cách chỉ làm mượt mà thiếu diễn xuất; dáng khóa đọc rõ chưa đồng nghĩa đẹp |
| [Canon](../games/tu-tien/00-canon.md), D55–D59, D61, D63, §6, §9, §12 | Vũ khí và hệ độc lập; phát ≤ 50 ms; cử chỉ khớp chiêu; trang phục dùng chung skeleton |
| [Phân tích Gemini 16/11](../games/tu-tien/source/gemini-typing-gameplay-ui-2026-11-16.md) | Các khoảnh khắc cần hỗ trợ: tự đánh, từ trên quái, năm kỹ năng, chuỗi từ, vòng tụ linh, Space |
| [392](392-report.md), [392b](392b-report.md) | Hai báo cáo vẫn phân biệt phương án mới với canon/source; không lấy đề xuất giao diện làm luật đã triển khai |
| `src/lab/hero-select.ts`, `caster.ts`, `anim/`, `motion-probe.ts`, `pose-probe.ts`, `skills-main.ts`; `src/view/player-view.ts`, `walker-rig.ts`; `src/content/model-contracts.ts` trong game | Kiểm kê dưới đây là từ mã và dữ liệu thật, không chỉ từ kế hoạch cũ |

**Hai tuyến phải giữ riêng:** canon/source hiện có một từ → một Cast, quái thường không mang từ; tuyệt kỹ ở ô 5 chưa có chuỗi + Space theo phương án Gemini. Bản đồ bên dưới mô tả cả tuyến hiện tại và tuyến thử, nhưng Animator chỉ cần nhận ý định, tiến độ gõ và sự kiện hành động đã được tầng luật chấp nhận. Không tự quyết tokenizer, xử lý IME, hồi chiêu, sát thương hay loại từ.

Gemini nêu năm ô Kim/Mộc/Thủy/Hỏa/Lôi, trong khi D59 cho chọn vũ khí và hệ độc lập, gồm tám hệ. Vì vậy bảng hệ ở §5 là **từ vựng diễn xuất**, không tự chốt năm ô là năm hệ. Cùng một chiêu kiếm vẫn giữ đường chém khi đổi Kim sang Hỏa; chỉ thay thủ thế phụ và phẩm chất chuyển động trong giới hạn đã duyệt.

Một điểm cần chuyển cho người chốt gameplay: 15 WPM tương đương 1,25 ký tự/giây theo quy ước 5 ký tự/từ. Chuỗi ba từ 5 chữ, có hai Space, cần khoảng **13,6 giây** thuần gõ. Không được cắt chuỗi vì vòng slow-motion 3,5 giây hết, hay bắt thân giữ một dáng cứng suốt khoảng đó. Báo cáo này không nhận con số 3,5 giây là thời hạn bắt buộc.

## 2. Kiểm kê rig, clip và phần đang chạy

### 2.1 Dữ liệu GLB đọc trực tiếp

Phương pháp: Python chuẩn đọc header GLB, JSON chunk, `skins[].joints`, `nodes`, `animations[].channels` và `accessors[input].max`. Không nạp renderer, không ghi lại GLB. Thời lượng là giây theo dữ liệu sampler; số xương là khớp trong skin, không cộng socket. Đây chưa phải kiểm chất lượng skin hay xem chuyển động bằng mắt.

| File trong `games/immortality-cultivation/` | Dữ liệu tìm được | Vai trò thực tế |
|---|---|---|
| `art-src/lab/models/lam.glb` | 31 khớp, 13 clip; 7.009.232 byte | Lab mặc định, Lam mượn từ Wordwoven; quay mặt −Z |
| `art-src/lab/anim/human-base-animations.glb` | 66 khớp, **87 clip**; 5.656.648 byte | Rig người thử nghiệm của Mesh2Motion; profile cao 1,65 m, mặt +Z; vật liệu phẳng chỉ phục vụ lab |
| `art-src/lab/anim/human-addon-animations.glb` | 66 khớp, **75 clip**; 5.292.804 byte | Nguồn đi ngang/lùi và nhiều hành động phụ; không có nghĩa 75 clip đều đang được nạp hoặc đã đạt chất lượng |

Trong các GLB được liệt kê ở cây game, ngoài hai rig trên là quái, vũ khí, rồng năng lượng và đạo cụ. **Chưa tìm thấy model nữ kiếm tu đã rig**. `src/view/player-view.ts` vẫn tạo capsule cho người chơi; `walker-rig.ts` có đường phát bằng `AnimationMixer`, không phải toàn bộ Animator của lab đã vào bản chơi. Không gọi Lam hoặc `human` là nhân vật chính đã được nghiệm thu.

**Đủ 31 xương Lam**, nhóm theo chức năng:

| Nhóm | Tên |
|---|---|
| Gốc và thân (7) | `root`, `pelvis`, `spine_01`, `spine_02`, `spine_03`, `neck_01`, `head` |
| Tay (8) | `clavicle_l/r`, `upperarm_l/r`, `lowerarm_l/r`, `hand_l/r` |
| Chân (8) | `thigh_l/r`, `calf_l/r`, `foot_l/r`, `ball_l/r` |
| Phụ (8) | `tail_01`–`tail_05`, `ear_l`, `ear_r`, `bag_r` |

Lam không có xương ngón, tóc, tay áo hoặc áo choàng. Tên `fingers` trong dữ liệu cử chỉ không tạo thêm khớp cho model này.

**Đủ 66 khớp người thử nghiệm:** 23 xương gốc/thân/tay/chân như ba dòng đầu của Lam; thêm 30 xương ngón và 13 khớp lá:

| Nhóm | Tên và ý nghĩa |
|---|---|
| Ngón điều khiển (30) | Mỗi bên `_l`, `_r`: `thumb_01`–`03`, `index_01`–`03`, `middle_01`–`03`, `ring_01`–`03`, `pinky_01`–`03` |
| Đầu ngón (10) | Mỗi bên: `thumb_04_leaf`, `index_04_leaf`, `middle_04_leaf`, `ring_04_leaf`, `pinky_04_leaf` |
| Lá còn lại (3) | `head_leaf`, `ball_leaf_l`, `ball_leaf_r` |

Rig này **đủ bậc tự do để thử** kiếm chỉ, nắm, mở, chạm hai đầu ngón và áp hai bàn tay. Chưa thể kết luận mọi ấn đẹp: còn phải xem trọng số ngón cái, khe ngón, độ vặn cổ tay và tiếp xúc hai tay. Có track ngón không chứng minh ngón đang chuyển động phong phú hoặc đúng ấn.

### 2.2 Clip Lam: có trong file khác với có trong Animator

| Clip trong GLB | Giây | Profile lab sử dụng |
|---|---:|---|
| `Hero_Idle` | 3,125 | `idle` |
| `Hero_Idle_Fidget` | 2,500 | `fidget` |
| `Hero_Run` | 0,833 | `run` |
| `Hero_Attack` | 0,833 | `attack`; sao chép thành `thrust`, chưa phải clip mới |
| `Hero_Skill1` | 1,667 | `skill1` |
| `Hero_Skill2` | 1,917 | `skill2` |
| `Hero_Ult` | 1,667 | `ult` |
| `Hero_Dash` | 0,708 | `dash` |
| `Hero_Hit` | 0,417 | `hit` |
| `Hero_Assist` | 2,667 | Chưa ánh xạ |
| `Hero_Death` | 2,167 | Chưa ánh xạ |
| `Hero_Respawn` | 1,417 | Chưa ánh xạ |
| `Hero_Victory` | 2,208 | Chưa ánh xạ |

Profile Lam bổ sung bốn clip từ Mesh2Motion: `Walk`, `Strafe_left`, `Strafe_right`, `Walk_Backwards`; chuyển xương lúc nạp. Mốc nhả khai báo hiện tại: Attack/Thrust/Skill1 **0,267 s**, Skill2 **0,708 s**, Ult **1,083 s**. Đó là thời điểm trong clip, **không phải thời gian người chơi phải chờ sau chữ cuối**.

Profile `human` dùng `Idle_A`, `Walk`, `Jog`, `Sprint`, `Sword_Regular_A/B`, `Sword_Attack`, `Sword_Block`, `Spell_Simple_Shoot`, `Hit_Chest`; bổ sung đi ngang/lùi và `Run_Anime` từ addon, không cần retarget giữa hai file cùng rig. Nguồn còn có thể khảo sát: `Spell_Simple_Enter/Idle/Exit`, `Two-hand Blast`, `Attack_Ground_Pound`, `Meditate`, `Bow`, `Death_A/B/C/D`, `Victory`, `Hit_Knockback`. Tên có thật trong GLB, **chưa chọn làm cử chỉ cuối**; tên động tác không bảo đảm hợp tiên hiệp.

### 2.3 Đã có gì, còn thiếu gì?

| Phần | Bằng chứng hiện tại | Phần còn thiếu cho yêu cầu 393 |
|---|---|---|
| Nền chuyển động | `animator.ts`: trạng thái `loco`, `fidget`, `charge`, `strike`, `dash`, `pose`; có quán tính, lấy mẫu 60 Hz, IK, lớp thở/nhìn/nghiêng và lò xo | Trạng thái gục, hồi phục, chết, thắng/thua chưa thuộc `ClipKey` của Animator lab; cần nối sự kiện ở phiếu triển khai |
| Cử chỉ theo chiêu | `gestures.ts`: `swordSeal`, `skyLift`, `fanSweep`, `bowThrust`, `overheadRaise`, `guardStance`, `dashCrouch`; slot → cử chỉ và clip | Các nhãn `sword/palm/spread/seal/fist` chưa là thư viện thủ ấn tổng quát; `acting.ts:applyArms` điều khiển tay/cổ tay, không giải từng ngón |
| Ngón trên `human` | `key-pose.ts` có ghi tư thế ngón; `fan-sweep-spec.ts` có `fist`, `seal`, `open`; profile chỉ định k4 → `fanSweep` | Mở rộng thành dữ liệu ngón dùng lại được, tư thế hai tay tiếp xúc, nhịp chữ đúng/sai; không coi toàn bộ chiêu đã có hand-seal controller |
| Marker | Ba GLB có `animations[].extras` rỗng; profile tự khai báo hoặc đo nhả bằng đỉnh tốc tay | Chưa có đầy đủ metadata `events`, tiếp đất, `recover`, biến thể, mask theo hợp đồng; đỉnh tốc tay chỉ là gợi ý, phải đặt marker theo động tác thật |
| Di chuyển | Walk/strafe/back có nguồn và đường nạp; xoay/dừng dùng lớp thủ tục | Clip Start/Stop, Turn có chủ ý; di chuyển khi đang kết ấn; không nhầm “chưa có clip” với “chưa có hành vi” |
| Bộ hành động | Clip nền một số chiêu và một fan sweep có dáng khóa riêng | Chưởng, nâng trụ, đóng trận, duy trì, tuyệt kỹ chuỗi/Space; hit theo hướng, hai kiểu ngã; tư thế nghỉ mang khí chất nhân vật thật |

**Bài học chưa được xóa bằng số đo:** `MOTION_PLAN` ghi vòng 1 chấm 5,4/5,4, vòng 2 là 6,1/6,5, vòng 3 bản làm lại 5,3/5,7; vòng 4 một chiêu đạt nhận diện pha 97–100% nhưng điểm cảm nhận vẫn **4,6**. Các bộ chấm khác nhau, không coi là đường điểm tương đương. Kỹ thuật mượt, dáng rộng hoặc nhận diện đúng đều chưa đủ khối lượng, diễn xuất và sức hút thương mại.

## 3. Bản đồ khoảnh khắc → hoạt ảnh

Các khoảng khung dưới đây là **đề xuất dựng ở 60 Hz**, 1 khung ≈ 16,67 ms. “Phản hồi ngay” là bắt đầu đổi dáng ở khung đầu có thể vẽ; không bắt hoàn tất cả động tác ngay. Gõ là tiến độ do tầng nhập xác nhận, không phải đếm mọi `keydown` vật lý.

| Khoảnh khắc / trạng thái | Cơ thể và tay | Nhịp, ưu tiên, ngắt |
|---|---|---|
| Chờ / sẵn sàng | Trụ vững, gối mềm; lồng ngực thở nhẹ, mắt theo tiền tuyến; tay kiếm thấp bên hông, tay dẫn thả cong; áo/tua theo gió và vận tốc thân | Thở khoảng 0,25 Hz; hai idle đổi rất chậm; fidget sau 4–9 s yên, ngắt ngay khi gõ, không vung kiếm qua chữ |
| Phi kiếm tự đánh | Kiếm bay tự vận hành; chỉ mắt hoặc cổ tay dẫn hướng nhỏ, vai ổn định | Một cử chỉ dẫn cho cả loạt, không full-body mỗi viên; đang kết ấn thì bỏ lớp dẫn tự động. Việc bắn vẫn theo sim |
| Chữ đầu đúng / bắt đầu gõ | Mắt khóa đích, hông hạ nhẹ, tay phụ lên ấn; vai/hông chuẩn bị hướng lực trước khi nhả | Bắt đầu trong 0–1 khung; vào gồng half-life 0,06 s; tiến độ từ quyết định đoạn clip, không chạy hết một animation mở đầu rồi mới nhận phím |
| Mỗi chữ đúng giữa từ | Cổ tay hoặc khuỷu nối một cung nhỏ 1–3°; thân thêm chút cuộn, đổi trọng lượng; ngón giữ cấu trúc ấn | Xung 3–6 khung chồng lên gồng; luân phiên cổ tay/khuỷu/lồng ngực, không đập cả người. Phím dồn được gộp biên độ, không xếp hàng xung |
| Gõ chậm / ngừng nghĩ | Giữ “sống”: thở, chuyển áp lực hai chân rất nhẹ, cổ tay lượn biên độ thấp quanh ấn | Không loop gồng–nhả; không tăng lực vô hạn theo thời gian. Vòng giữ không tự chạm marker phát |
| Phím sai | Cổ tay hơi lùi, ngón siết rồi mềm, mắt vẫn giữ đích; không diễn như bị quái đánh | Xung nhỏ 4–6 khung rồi tan 6–10 khung; lỗi dồn gộp, không rung liên tục; không tự hủy từ, trừ khi tầng luật báo hủy |
| Backspace / sửa / đổi đích / hủy | Tiến độ ấn lùi mượt; đổi đích cho mắt dẫn trước ngực; hủy thì hạ tay về thủ | Không tua clip qua `release`; không phát whoosh/đạn vì tua lùi. Gõ từ mới trong lúc thu thì chuyển trực tiếp vào gồng mới |
| Xong từ trên quái, nếu chọn phương án Gemini | Một nhát dẫn kiếm gọn, tay phụ chốt kiếm chỉ, hông chuyển lực vừa đủ | Lệnh phát ở F0, biểu hiện phát trong F0–F2; trần ≤ 50 ms. Không thêm Space hay một nghi thức dài cho đòn nhỏ |
| Xong từ ô kỹ năng | Họ clip đúng hành động, biến thể ấn theo hệ; gồng đã diễn trong lúc gõ | F0–F2 phát; sau đó tiếp tục vung và thu. Đây cũng là tuyến dùng được với Bàn Quyết hiện tại |
| Cast chưa có đích, nếu vẫn giữ luật `held` | Dáng đã sẵn, tay hạ thấp hơn dáng nhả; không bắn giả | Lõi luật quyết đích/hết hạn; ghi riêng thời gian chờ đích và thời gian sau sự kiện phát hợp lệ. Không dùng `held` để giấu trễ do animation |
| Kim | Kiếm chỉ S1, cổ tay thẳng theo mũi kiếm, cắt gọn, đối lực hông rõ | Dùng họ kiếm/chưởng tương ứng; đuôi động tác ngắn, dứt rồi mềm |
| Mộc | S2 nụ mở, hai khuỷu mở ra trước thân, trọng tâm nâng theo đường rễ/trụ | Phát không chờ trụ lớn lên; thân theo đà dâng sau F0 |
| Thủy | S3 ôm dòng, tay nọ dẫn tay kia, hông chuyển ngang mượt | Giữ dòng liên tục, đổi vận tốc có đỉnh; không dùng cùng đường vòng đều cho mọi chiêu |
| Hỏa | S4 nén–mở, vai gom trong lúc gõ rồi chưởng/tay kiếm mở dứt | Nén đã xong trước chữ cuối; phát ngay, ngực và áo theo đà 6–12 khung |
| Thổ | S5 trấn, chân rộng hơn, hông thấp vừa đủ, lực từ chân lên lòng bàn tay | Chân đã trụ khi gõ; hiệu ứng phát trước khi hoàn tất cú ấn xuống |
| Lôi | S6 nắm lôi → chỉ lệnh, mắt và khuỷu có nhịp dứt rõ | Chỉ một gia tốc mạnh khi phát, sau đó lắng; không giật từng khung giả điện giật |
| Băng | S7 khép tinh, hai tay đối nhau rồi tách theo mặt phẳng | Giữ tĩnh có chủ ý giữa chuyển động mềm, không khóa cứng toàn thân |
| Phong | S8 dẫn phong, vai/hông xoắn nhẹ, bàn tay vạch cung lệch nhau | Dòng lực xoắn rồi mở; chân chống xoay, không xoay vòng tại chỗ cho mọi đòn |
| Tuyệt kỹ: gõ chuỗi (đề xuất) | S0 → ấn hệ → S9; mỗi từ thêm một bậc lấy đà, khuỷu và hông đổi thế; phi kiếm tự đánh không giành tay | Tiến độ theo toàn chuỗi, có vòng giữ sống ở mỗi bậc; Space phân cách từ không phải lệnh khai ấn |
| Vòng tụ linh đã sẵn (đề xuất) | Giữ S9 trước ngực/trán lệch sang bên để nhìn thấy; mắt hướng đích, vai thả, hai chân neo | Vòng thu của UI không bắt nhân vật co giật theo từng tick; vẫn nhận hit và thay đổi đích hợp lệ |
| Space khai ấn: Phàm / Linh / Tiên (đề xuất) | Chung động tác phát S9; Phàm gọn và chắc, Linh mở tay/theo đà rộng hơn, Tiên thêm đường tay cao và động tác hồi trang trọng | Cùng F0–F2 phát, không kéo dài tụ lực theo cấp. Chỉ khuếch đại phần theo đà/diễn sau lệnh; thưởng sát thương thuộc luật, không nằm trong clip |
| Bị đánh nhẹ | Hông/ngực giật theo hướng, đầu trễ, tay đang kết ấn còn giữ được cấu trúc | Lên 2–3 khung, khựng 2–3 khung, tan 12–18 khung; lớp cộng, không tự cắt chiêu đã được sim chấp nhận |
| Choáng / gục | Trọng lượng đổ đúng hướng, bước cứu nếu còn đứng, gối chạm rồi thân theo; ngón thả dần | Toàn thân chỉ khi tầng luật báo; chạm đất có marker. Không cắt sang bind; hồi phục theo sự kiện riêng |
| Thắng | Thu kiếm → hạ vai → nhìn sân → chào gọn; tua còn lắng sau thân | Một clip 90–150 khung đề xuất; vẫn thở sau khi kết; không reo/vung vũ khí trẻ con trái khí chất D47/D63 |
| Thua / chết | Nếu cổng thua mà người sống: hạ tay, khuỵu/nhìn cổng. Nếu nhân vật chết: ngã theo hướng và lực đòn | Tách thua trận với chết; giữ tư thế cuối, marker chạm đất, không đứng lên trước bảng kết quả; có hai biến thể chết |

**Ưu tiên lớp:** chết/gục theo luật → choáng toàn thân theo luật → hành động được chấp nhận → gồng đang nhập → di chuyển/idle; hit nhẹ là lớp phủ. Thao tác mới hợp lệ có thể cắt **thu thế**, không cần chờ clip cũ hết. Nếu sim từ chối vì choáng/chết thì không diễn phát giả. Tầng nhập vẫn xử lý phím độc lập với việc nhân vật đang bận diễn.

## 4. Bộ 10 thủ ấn đề xuất

Tên dưới đây là tên làm việc trong tài liệu, không phải chữ UI. Mỗi ấn có một bóng dáng khuỷu–cổ tay để đọc ở camera chơi và chi tiết ngón khi zoom; không dùng cỡ ngón làm thông tin bắt buộc để chơi. Tay không cầm kiếm mới thực hiện đầy đủ ấn; động tác hai tay cần kiếm đã bay/rời tay qua sự kiện trang bị, không biến mất trong một khung. Có vũ khí cầm tay thì dùng biến thể một tay, tay còn lại giữ grip thật.

**Nguồn văn hóa đã kiểm tra bằng web, chỉ đọc văn bản:**

- **[VH1 — Shen Yun, “Blossoms and Blades…”](https://www.shenyun.org/blog/view/article/e/MzVgkILI6Kg/classical-chinese-dance-basics-hand-gestures-blossoms-blades.html)** mô tả kiếm chỉ trong múa: trỏ và giữa đi cùng nhau, cái giữ áp út và út. Đây là nguồn thực hành biểu diễn, không chứng minh mọi chi tiết đạo thuật hoặc một trường phái võ thuật.
- **[VH2 — FYSK Daoist Culture Centre, “Finger Gestures”](https://en.daoinfo.org/wiki/Finger_Gestures)** xác nhận Đạo giáo có hệ thủ quyết và tên kiếm quyết, quyết chế lôi. Trang không đủ hình hướng dẫn để xác nhận cấu hình từng đốt; không lấy nó làm chứng cứ rằng S6 là ấn lôi lịch sử.
- **[VH3 — Buddhist Society of Australia, “What is a mudra?”](https://buddhistsocietiesofaustralia.org/topics/mudra/)** mô tả thiền ấn: hai bàn tay ngửa, phải trên trái; mô tả vô úy: tay nâng, lòng hướng ra. **[Asia Society, tượng Abhaya-mudra](https://asiasociety.qi-cms.com/web/museum/collection/explore/1979-008-the-buddha-shakyamuni-in-abhaya-mudra)** xác nhận ý trấn an của tay phải nâng. Việc chuyển thành tư thế đứng chiến đấu là diễn giải của game.

Các ấn nguyên tố còn lại là **sáng tác tiên hiệp cho game**; không gán thành nghi lễ cổ hoặc khẳng định ngũ hành có đúng bộ ấn này. Không tải ảnh của những nguồn trên, không gửi ảnh bên thứ ba tới công cụ ảnh.

| Mã / vai trò | Tay phải: từng ngón, lòng tay | Tay trái: từng ngón, lòng tay | Vị trí, nhịp chuyển ở 60 Hz | Nguồn và mức xác thực |
|---|---|---|---|---|
| **S0 Quy nguyên** — nghỉ tụ khí, mở chuỗi | Bốn ngón duỗi mềm sát nhau, cái cong nhẹ; lòng ngửa, đặt trên tay trái | Bốn ngón duỗi mềm, cái cong lên gần đầu cái phải; lòng ngửa đỡ dưới | Trước bụng dưới, cách thân khoảng một bàn tay; nâng 12–18 khung trong lúc gõ, không khóa vai; thở làm hai tay dịch rất ít | Cảm hứng thiền ấn VH3; vị trí đứng và chuyển nhịp do game dựng, không gọi là nghi thức thiền chuẩn |
| **S1 Kiếm chỉ** — kiếm quyết, Kim | Trỏ + giữa duỗi song song; áp út + út gập; cái phủ giữ hai ngón gập, không ép xuyên; lòng chếch vào trái | Trỏ + giữa duỗi, áp út + út gập, cái giữ; lòng hướng vào thân; hoặc grip kiếm đủ năm ngón nếu kiếm ở tay trái | Tay dẫn ngang ngực rồi chỉ tới đích; tay còn lại gần sườn; chuyển vào 6–10 khung khi gõ, nhả chỉ một đoạn cổ tay ngắn | Dáng ngón có nguồn VH1; VH2 xác nhận tên kiếm quyết. Cặp tay, vị trí và hệ Kim là sáng tác |
| **S2 Sinh nha** — Mộc | Trỏ + giữa duỗi hơi cong; áp út + út cuộn nửa; cái mở nhẹ; lòng ngửa chéo | Trỏ + giữa duỗi hơi cong, áp út + út cuộn nửa, cái mở; lòng hướng vào tay phải | Hai cổ tay gần nhau trước ngực, đầu ngón vươn thành hai nhánh không đan; mở khuỷu 8–14 khung trong gồng; phát thì nhấc và tách | Sáng tác; tránh gọi là ấn Mộc Đạo giáo có thật |
| **S3 Dẫn lưu** — Thủy | Bốn ngón cong mềm liền nhau, cái mở tạo chén; lòng hướng vào trái, ngửa nhẹ | Bốn ngón cong mềm, cái mở; lòng hướng vào phải, úp nhẹ, không đặt phẳng đè tay kia | Hai tay ôm khoảng rỗng trước rốn, tay phải trên/ngoài, trái dưới/trong; dẫn một cung 12–18 khung, đổi vai trò khi thu | Sáng tác; dùng hình dòng chảy, không gán tên mudra lịch sử |
| **S4 Tàng diệm** — Hỏa | Trỏ/giữa/áp út/út co nửa trong gồng, cái mở khỏi trỏ; khi phát bốn ngón mở xòe có kiểm soát, cái dang vừa; lòng tới đích | Bốn ngón co nửa, cái ôm bên ngoài; lòng ngửa giữ “lõi” trước bụng; khi phát mở bốn ngón mềm, cái còn cong | Gồng gom tại sườn 8–12 khung đã diễn khi gõ; chữ cuối mở chưởng ngay, tay trái đối lực; ngón không bật từ nắm sang xòe trong một khung | Sáng tác; không xem ngọn lửa là hình ngón bắt buộc |
| **S5 Trấn nhạc** — Thổ, hộ thân | Bốn ngón duỗi gần nhau, cái mở mềm; lòng hướng ra trước khi hộ thân, xoay xuống khi trấn đất | Bốn ngón gập thành nắm vừa, cái nằm ngoài nắm; lòng nắm hướng lên tại eo trái | Tay phải trước ngực lệch phải, khuỷu hạ; trái tại đai; vào 8–12 khung; khi phát đẩy/ấn theo họ chiêu, không khóa thẳng khuỷu | Tay mở trấn an lấy cảm hứng vô úy VH3; tay trái, chuyển xuống đất và gắn Thổ đều sáng tác |
| **S6 Dẫn lôi** — Lôi | Bốn ngón nắm, cái đặt ngoài trên trỏ; lúc lệnh phát duỗi trỏ + giữa, giữ áp út + út gập dưới cái | Bốn ngón cuộn nửa quanh khoảng rỗng, cái đặt cạnh đốt trỏ; lòng ôm bên cổ tay phải nhưng không xuyên | Trước xương ức rồi nâng chéo tới thái dương, khuỷu tách khỏi bóng thân; chuẩn bị mở ngón ở cuối tiến độ, chỉ đường ngay khi phát; chuyển đầy đủ 8–12 khung nằm trong gõ | Sáng tác. VH2 chỉ xác nhận có quyết chế lôi, **không xác nhận cấu hình S6** |
| **S7 Ngưng tinh** — Băng | Bốn ngón duỗi mềm sát nhau, cái cong; lòng hướng trái | Bốn ngón duỗi mềm sát nhau, cái cong; lòng hướng phải | Hai lòng đối diện cách 4–8 cm trước ngực, đầu ngón hướng lên hơi chéo; khép khoảng hở 10–14 khung lúc gõ, khi phát trượt tách ngang thành hai mặt phẳng | Sáng tác; không khóa băng bằng dáng cầu nguyện chung cho mọi hệ |
| **S8 Dẫn phong** — Phong | Trỏ + giữa duỗi tách hẹp; áp út + út cong nửa; cái mở; lòng chéo xuống | Bốn ngón duỗi mềm theo cung, cái mở thấp; lòng chéo lên | Tay phải ngang vai ngoài bóng thân, trái gần eo; hai cung đối chiều 10–16 khung trong gõ, phát theo đường chiêu, không xoắn cổ tay quá tầm | Sáng tác; gợi chuyển động gió bằng đường khuỷu và hông |
| **S9 Khai thiên** — tuyệt kỹ | Trỏ + giữa duỗi cùng nhau lên chéo; áp út + út gập, cái giữ; lòng chếch trái | Bốn ngón duỗi mềm hơi khum, cái tách; lòng đỡ dưới gốc tay phải, không bóp cổ tay | Gồng trước ngực, nâng gần trán trong phần cuối chuỗi, giữ mặt thoáng; Space thì phải chỉ ra, trái mở đối lực. Phàm/Linh/Tiên cùng mốc phát, khác biên độ theo đà | Dùng kiếm chỉ VH1 làm bộ phận; toàn bộ cặp tay, tên và nghi thức ba cấp là sáng tác |

**Quy tắc chuyển ấn:** không nội suy thẳng mọi ngón xuyên nhau. Đường chuyển gồm mở khoảng tiếp xúc → xoay cổ tay → đóng ấn mới; nằm trong gõ/thu, thường 6–14 khung. Nếu người chơi gõ quá nhanh để xong đường này, ưu tiên cử chỉ phát có sẵn từ tư thế hiện tại; hoàn thiện ấn trong phần theo đà. Không kéo dài điều kiện phát chỉ để đủ ngón. Chỉ giữ các tiếp xúc quan trọng (đầu ngón cái, chỗ hai lòng gần nhau); không thêm finger IK tổng quát trước khi thấy dáng khóa không đáp ứng.

## 5. Chân–hông–tay theo họ kỹ năng

### 5.1 Trục thời gian chung và giới hạn 50 ms

**F0** là lần tầng luật nhận lệnh phát hợp lệ: chữ cuối của chiêu thường; Space khai ấn nếu phương án mới được duyệt. Tiến độ gõ trước F0 điều khiển đoạn gồng; với tuyệt kỹ hiện tại, chữ cuối vẫn là lệnh, không tự thêm Space.

- Trong lúc gõ: thời gian clip hướng tới `p × (release − lead)` từ đầu đoạn gồng; giữ dưới marker nhả. `p` là phần tiến độ hợp lệ. Giảm tiến độ/hủy không được quét qua marker phát.
- Tại F0: nhận sự kiện, bắt đầu mở thế và phát lớp release ngay trên khung vẽ đầu có thể; **mục tiêu F0–F2**, trần thực đo từ dấu thời gian đầu vào đến thân/VFX phát là **≤ 50 ms**. Không chờ toàn thân đạt đỉnh vung.
- Tiếp tục vung F3–F8, giữ ngắn và thu dài hơn. Clip có thể cần 30–70 khung để diễn hết; chiêu đã rời tay trước đó.
- Không cộng thêm “ba khung clip” sau một hàng đợi input/sim/render. 50 ms là ngân sách tổng, không phải mỗi tầng được 50 ms. Đo cả 60/120 Hz, không chỉ đổi số khung.
- Hit-stop còn giữ phải nhả cho lệnh mới; lớp thở/lò xo không chạy sang marker thay tầng luật. Đường cấp tốc khi từ cực ngắn/gõ dồn: chuyển quán tính từ dáng đang có sang tư thế phát gần, đo xem có giật; nếu giật thì sửa dáng cầu nối, không trì hoãn đòn.

### 5.2 Năm họ chiêu chính và biến thể vũ khí

Góc/độ dài sau là điểm bắt đầu cho **rig người**, cần điều chỉnh theo chân và áo thực tế; không bê biên độ Lam sang nữ kiếm tu. Bước là dịch chuyển phần nhìn có kiểm soát; không tự đổi hitbox, điểm đặt trụ, vị trí sim hoặc tầm sát thương.

| Họ chiêu | Thế đứng và tụ lực khi gõ | F0–F2 phát; F3–F8 theo đà | Giữ → thu đề xuất |
|---|---|---|---|
| **Kiếm chém / kiếm khí** | Chân trái trước khoảng 0,15–0,25 m, chân sau neo; hông cuộn 10–20°, ngực ngược thêm chút; kiếm kéo sau/chéo vai nhưng mũi còn đọc được về đích; tay phụ S1 ngoài bóng thân | Chân trụ đẩy → hông → ngực → khuỷu/cổ tay nối nhau; điểm phát trên cung kiếm trong F0–F2; mũi tiếp tục đi qua đường chém F3–F8 | Giữ 4–6 khung, vượt cung 5–10° rồi thu 16–24 khung; không đóng băng thành chữ V |
| **Chưởng / luồng phóng** | Cung bộ ngắn, gối sau mềm, hông lùi; tay phát ở sườn, tay kia giữ ấn trước đai; vai không nhún lên tai | Chuyển áp lực về chân trước và mở lòng hướng đích; phát lúc bắt đầu đẩy, khuỷu còn cong; ngực theo tiếp đến F6 | Giữ 4–8 khung, cổ tay hãm trước khuỷu, thân lắng; thu 18–26 khung. Luồng duy trì dùng giữ sống, không spam clip chưởng |
| **Triệu hồi trụ** | Chân rộng ngang vai, gối khuỵu nhẹ, hai tay thấp lòng ngửa; ánh nhìn chọn vị trí đã có từ tầng nhắm | F0–F2 xoay lòng/nhấc tay làm lệnh; trụ bắt đầu theo sự kiện đó. Hai khuỷu nâng qua F3–F8, thân đứng lên dần; không đợi tay qua đầu mới sinh trụ | Giữ 8–12 khung, hai tay hạ lệch nhau và hông ổn định 20–30 khung; trụ còn đánh không buộc caster đứng giơ tay hết vòng đời |
| **Kết trận dưới đất** | Bước mở một chân 0,10–0,20 m trong lúc gõ, chân còn lại neo; hông xoay 10–15°, hai tay gom trước bụng rồi tay dẫn hướng xuống vùng | Phát trên động tác ấn/điểm đầu tiên F0–F2; trọng tâm tiếp tục hạ F3–F8. Điểm trận lấy từ sự kiện nhắm, không lấy chỗ ngón chạm sàn | Giữ 6–10 khung, kéo tay theo đường vòng về ngực 20–30 khung; không bắt quỳ sát đất cho mọi chiêu |
| **Tuyệt kỹ toàn sân** | Chuỗi đổi S0 → ấn hệ → S9; chân mở, hông hạ 4–7% chiều cao, đầu vẫn rõ. Đoạn vòng tụ linh giữ cân bằng hai chân và các lớp sống | F0 là Space được chấp nhận: S9 mở, sự kiện phát ngay; F3–F8 mở tay/ngực và chuyển lực lớn hơn. Tiên Ấn không có đoạn chờ riêng | Giữ 8–14 khung, lắng/theo đà 18–24, thu 24–36 khung; cho phép hành động mới ngắt thu. Mưa đòn về sau do recipe VFX, không khóa tay tới đòn cuối |

Với Kiếm/Đao/Thương theo D59: dùng cùng phân pha nhưng cần **grip và đường lực riêng**. Kiếm dùng dẫn mũi/cổ tay tinh; Đao dùng hông và vai rộng hơn, tay phụ đối trọng; Thương cần hai điểm cầm và trượt bàn tay dọc cán, thế cung bộ sâu hơn. Không chuyển một tay kiếm chỉ thành tay đang giữ thương rồi xuyên cán; không nhân bản cả tám hệ để giải khác biệt vũ khí.

**Áp tám hệ lên họ hành động:** Kim dứt ở đường thẳng/cạnh; Mộc mở và vươn; Thủy chuyển lực qua hai tay; Hỏa gom rồi bùng; Thổ bám chân và nặng; Lôi một cú tăng tốc rõ; Băng khép–tách mặt phẳng; Phong xoắn–mở. Những đặc tính này điều chỉnh vai, khuỷu, cổ tay và thu thế; không đổi marker nhả, không đổi action class của chiêu. Nhịp chất liệu chỉ thuyết phục khi thân và recipe cùng trả lời một sự kiện.

### 5.3 Tuyệt kỹ và cut-in: không che một khoảng trễ

D58 đồng thời yêu cầu phát ≤ 50 ms và cho cut-in khoảng 1 giây dừng game/giờ gõ. Hiện `skills-main.ts:startUltimate` mở cut-in, `fireUltimate` mới gọi `probe.lastKey`, rồi `caster.release`; nhánh gõ k5 gọi `startUltimate` ở chữ cuối. **Nếu chỉ đo từ `probe.lastKey` ở cuối cut-in thì bỏ mất thời gian chờ thật**; báo cáo không xác nhận tuyệt kỹ hiện tại đạt 50 ms đầu vào → phát.

Đề xuất cần người chốt lựa chọn trước khi dựng: đặt cut-in ở giai đoạn vào nghi thức, trước khi nhận chuỗi/cửa Space; hoặc mở cut-in đồng thời với lệnh phát và biểu hiện release đầu tiên. Không chen cut-in khóa giữa chữ/Space cam kết và lần phát đầu rồi gọi là phản hồi tức thì. Ghi dấu đầu vào bằng đồng hồ thật ngay khi nhận; báo cáo riêng thời gian cinematic và thời gian mô phỏng. Camera/cut-in mới chỉ là phương án, phiếu này không thay D58.

## 6. Rig và kỹ thuật để mềm, có lực, đa dạng

### 6.1 Rig đích và hợp đồng trang phục

Giữ tên xương chuẩn, profile khai báo trục trước, rest pose, chiều cao, độ dài chân, socket và mặt nạ xương. Xương không có thì đánh dấu không hỗ trợ, không giả đã kết ấn. Với model nữ kiếm tu theo D63:

- Giữ 23 xương gốc/thân/tay/chân và **30 xương điều khiển ngón**; khớp lá là tùy chọn theo exporter. Chưa thêm twist bones riêng khi chưa thấy lỗi skin; ưu tiên chỉnh trọng số/roll trên rig chung.
- **Đúng bốn xương phụ lò xo:** hai đuôi lưng, hai tua theo bổ sung D63. Không tự mở một bộ tóc/áo 20–40 xương. Vạt váy lễ xẻ tấm gán theo đùi như canon; tóc chính theo đầu. Chỉ phần tóc có xương đã được duyệt mới chạy lò xo.
- Dải lụa dài và hào quang là VFX bám socket, không biến thành cloth mesh hoặc xương phụ ngoài hợp đồng. Áo vải có mesh theo xương chịu quán tính nhẹ; thử đủ hai bộ đồ đầu để tránh giấu lỗi bằng trang phục ngắn.
- Socket logic dùng lại: tay trái/phải, bàn chân, core, lưng, vũ khí. Profile ánh xạ `FX_HAND_R` của lab với `FX_CAST_R` của hợp đồng game; không đoán hai tên tự tương đương. Tách socket grip thật và điểm phát ở lòng/mũi vũ khí.
- Giữ một rest pose A và tỷ lệ chung cho mọi outfit. Weight ngón phải độc lập, vai không kéo cổ Nhật Bình; D63 giới hạn tấm cổ nhận ≤ 20% trọng số tay. Kiểm nách, háng, gối, cổ tay, ngón cái và vùng kiếm ngang xương cùng.

Thêm 30 xương chỉ có ích nếu mesh có khe ngón, topology và trọng số đúng. Lam không thể được “sửa thủ ấn” bằng vài quaternion; muốn dùng Lam cho việc đó cần sửa mesh/rig, không đáng làm thay cho hero thật. `human` chỉ kiểm cơ chế và diễn xuất, không phải mẫu mỹ thuật để nghiệm thu nhân vật.

### 6.2 Một nguồn tư thế chính, các lớp có mặt nạ

Ưu tiên thư viện chính thức cho thao tác clip, rồi giữ phần cục bộ đã có bằng chứng cần thiết. [AnimationMixer](https://threejs.org/docs/pages/AnimationMixer.html) quản lý phát clip; [AnimationAction](https://threejs.org/docs/pages/AnimationAction.html) có crossfade và giữ cuối clip. `clampWhenFinished` chỉ có tác dụng khi clip thực sự hết, không chữa mọi chuyển trạng thái bị ngắt. [AnimationUtils.makeClipAdditive](https://threejs.org/docs/pages/AnimationUtils.html) nhận clip/frame tham chiếu; dùng đúng pose tham chiếu cho hit/thở, không cộng hai tư thế tuyệt đối. Game khóa three **0.170.0**; tài liệu web hiện hành chỉ kiểm nguyên lý/API, khi dựng phải đối chiếu bản đã cài, không nâng dependency theo trang mới.

Lab hiện lấy mẫu pose riêng vì lớp IK/thủ tục có thể để dư giá trị nếu mixer bỏ qua track hằng; `rig.ts` và skill ghi lý do. Vì thế không viết lại Animator hoặc ghép thêm một mixer cùng ghi các xương đó. Đường clip mới thử [SkeletonUtils.retargetClip](https://threejs.org/docs/pages/module-SkeletonUtils) trước; chỉ giữ retarget riêng khi ma trận kiểm cho thấy khác rest/roll mà đường chuẩn chưa xử lý đạt.

Thứ tự đề xuất tiếp tục từ `animator.ts:update` đang có:

1. Nhận sự kiện sim/đầu vào đã định tuyến; cập nhật hướng, di chuyển và tiến độ hành động.
2. Chọn clip/dáng khóa chính và thời gian; lấy mẫu sang pose sạch. Xương thiếu track lấy pose tham chiếu có chủ đích, không lấy phần dư khung trước.
3. Chuyển tiếp quán tính: giữ chênh vị trí/góc **và vận tốc** từ dáng đang vẽ, tắt dần vào clip mới; không đi qua bind. Khi đang ngắt giữa hai lần ngắt, lấy dáng đã tổng hợp thực tế làm đầu vào.
4. Hit nhẹ theo hướng, nghiêng/thở/nhìn/giật lùi có mask; lớp tay theo hành động. Chiêu có dáng khóa toàn thân phải giảm lớp diễn cũ để không cộng hai lần hạ hông hoặc vặn ngực.
5. Áp dữ liệu ngón/tiếp xúc của thủ ấn sau clip tay; giữ grip của tay cầm vũ khí, kiểm khoảng cách hai tay. Sửa vị trí cổ tay bằng ràng buộc nhẹ khi thực sự cần chạm, không kéo vai xuyên thân.
6. IK chân hai đốt; khóa chân trụ theo world, xoay gót/mũi có nhấc đặt chân; hông hạ mềm trong tầm với, không duỗi gối ngược. Đi/ngang/lùi dùng tốc độ bước đo từ clip.
7. Lò xo phụ trên bốn xương được phép, collider thân/đùi; cập nhật world matrix; đọc socket, phát VFX/âm/camera rồi render.

Các half-life **trong mã hiện tại**: nhả 0,04 s; gồng 0,06; về idle 0,09; **thu 0,10**; dash vào/ra 0,04/0,08; hit 0,03. Tài liệu skill runtime còn nêu thu 0,065 s, nhưng mã mới ghi đã tăng vì tay vung 95° lúc chuyển; lấy mã làm mốc, không khôi phục số cũ. Các giá trị này làm mượt, không phải quyền lùi thời điểm phát.

Lò xo phụ bước cố định 60 Hz, hiển thị nội suy; sau pause/reset/teleport phải đặt lại trạng thái và vận tốc hợp lý. Chống xuyên bằng capsule/sphere, giới hạn góc nón và tốc quay; không “đẹp” bằng tăng biên độ vô hạn. Tua trễ khoảng 2–6 khung là mục tiêu nhìn, phải đo từng outfit. [Daniel Holden, “Spring-It-On”](https://www.theorangeduck.com/page/spring-roll-call) là nguồn tác giả về spring và inertialization; thông số chọn ở đây là đề xuất dự án, không phải số bắt buộc từ bài đó.

### 6.3 Đa dạng mà không mất nhịp

| Lớp | Cách tạo khác biệt | Giới hạn |
|---|---|---|
| Idle | Hai loop khác áp lực chân, một fidget; pha thở và lúc nhìn đổi bằng seed | Fidget chỉ khi rảnh, không quay lưng/che đường ngắm |
| Gõ đúng | Ba xung cổ tay/khuỷu/thân luân phiên có trọng số, tránh lặp biến thể vừa dùng; biên độ ±10% đề xuất | Cửa xung tối thiểu khoảng 80 ms; phím dồn cộng năng lượng có trần thay vì queue. Không random mỗi frame |
| Chiêu lặp | Hai đường kiếm tương thích cùng action class; đổi tay phụ, hướng thu và trọng tâm nhẹ | Giữ marker, socket, mục tiêu, grip và chân trụ. Không mirror mù cả người cầm kiếm/thương |
| Hệ | Chọn ấn S1–S8, độ dứt/mềm và nhịp thu | Không thay cả clip theo màu; không đổi thời gian phát ngẫu nhiên |
| Bị đánh | Hướng lực và cường độ từ event, ba pose nền trước/sau/bên | Lỗi gõ không gọi hit; hit nhẹ không phá ấn hoặc trì hoãn phát |
| Nhiều nhân vật | Seed theo nhân vật và số hành động, lệch idle/thở | Chỉ biến thiên presentation; replay và phép đo phải tái hiện được. Không bốc lại seed sau mỗi frame |

Để đạt vẻ quý phái, vai phải thả, cổ tay có cung và khoảng lặng; sức mạnh đến từ chân–hông–ngực nối lực, không lắc tay liên tục. Áo/tua đi sau điểm dừng; mắt nhìn nơi sắp tác động; thu thế có chủ ý thay vì ngắt xong trả thẳng về idle. Đó là phần cần tác giả clip/dáng khóa làm, spring không tự sinh diễn xuất.

### 6.4 Sự kiện: thân, hình, âm và camera cùng khung

Mỗi hành động có ID, biến thể đã chọn, clip, mask, contacts và marker `windup_end`, `release`, `recover`; bước chân `foot_l/r`, ngã `fall_impact`, gục `kneel_impact` nếu dùng. Lưu thời gian bằng giây hoặc tick 60 Hz rõ đơn vị. Không tách gồng và nhả thành hai clip phải nối lại lúc gõ.

**Sim quyết phát/trúng/sát thương.** View cập nhật thân → đọc socket mới → phát các thành phần release → âm release → camera → render trên cùng khung. VFX impact, phản ứng quái và âm trúng lấy sự kiện impact của sim, không chạy ngay ở release của đòn còn bay. Hành động nâng trụ/đóng trận vẫn có pha release ở người; điểm sinh ngoài xa thuộc event nhắm. Marker clip chỉ quyết bước chân, whoosh, va đất và diễn phụ, không phát damage lần hai.

Qua marker được xét trên khoảng thời gian, xử lý loop/đổi tốc/seek; tua gồng và sửa chữ chỉ tạo phản hồi gõ, **không tái phát `release`**. Đánh dấu event đã dùng theo action ID; không dựa vào bằng đúng một mốc thời gian. Toàn bộ nhịp dùng cùng clock, không `setTimeout` để hẹn hình/tiếng. AudioContext có đồng hồ riêng nên khi dựng cần ánh xạ thời điểm event tới lịch phát, đo onset; “cùng frame gọi hàm” chưa chứng minh loa phát trùng frame.

Âm chỉ ghép nguyên liệu audio đã được duyệt theo Q6, theo động tác: lấy lực, lướt vũ khí, thân năng lượng và đuôi; không sinh tiếng puff/pop/thump cho mỗi chữ. Xung tay nhỏ không cần một tiếng phép mới lấn tiếng phím. Nhãn từ luôn đọc được, chớp/rung không che dáng nhả; giảm chuyển động chỉ giảm biên độ phụ và camera, giữ dấu thời gian phát.

## 7. Nguồn clip, khối lượng cần làm và cổng hợp đồng

| Nguồn | Dùng cho gì | Điều kiện và kết luận |
|---|---|---|
| File Mesh2Motion đã có trong repo | Idle, locomotion, hit, ngã, đứng dậy; các cast làm nguyên liệu block | [Repo chính thức](https://github.com/Mesh2Motion/mesh2motion-app) và [LICENSE-CC0](https://github.com/Mesh2Motion/mesh2motion-app/blob/main/LICENSE-CC0.MD) xác nhận art/rig/animation CC0, mã MIT. Kiểm provenance từng gói đã nhập, không suy ra mọi clip tương lai cùng giấy phép |
| Blender trên rig chuẩn của ta | Các cung tay, thủ ấn, bước và nhịp thân đặc thù tiên hiệp; chỉnh clip nguồn cho đúng nhân vật | Nguồn ưu tiên cho phần không có sẵn; thao tác trên máy và tài sản của ta, không cloud auto-rig Tripo. Chuyển động cần người làm chọn key pose, trọng lượng và graph curves |
| Quaternius UAL1/2 | Bổ sung locomotion/đòn/biểu cảm nếu kho hiện có thực sự thiếu | [Trang UAL1](https://quaternius.com/packs/universalanimationlibrary.html) còn ghi CC0 nhưng [trang giấy phép](https://quaternius.com/license.html) ghi QAL v1.0, cập nhật 28/8/2026. Theo skill, xử lý thận trọng bằng QAL; ghi đúng gói/ngày tải/nguyên văn điều khoản vào sổ nguồn ở phiếu được phép ghi. Phiếu này không tải |
| KayKit | Chỉ khảo sát sau nếu thiếu clip đám đông | Skill cho làm phương án dự phòng, cần kiểm lại giấy phép gói tại nguồn trước khi dùng. Không cần cho lát cắt nhân vật chính này |
| Mixamo; Tripo auto-rig; kho CMU chưa kiểm | Không chọn | Theo luật repo: không đưa Mixamo vào luồng AI đám mây hoặc bản web này; không dùng auto-rig Tripo. Bỏ `human-mocap-animations.glb`/`CarnegieMellonAnimations` khi giấy phép nguồn chưa kiểm; không suy từ chữ “free” |

Không cần AI sinh hoạt ảnh mới ở đợt đầu. Không upload model/clip bên thứ ba sang công cụ AI, không cần ảnh tham chiếu thương mại làm đầu vào. Nếu sau này thêm nguồn/đổi retarget thì chạy ma trận **3 nhân vật × 10 clip** theo skill, kiểm cổ tay, vai, twist, hip drift cùng các cổng probe; phiếu 393 chỉ đề nghị, chưa thực hiện.

**Ước lượng cho một bộ người dùng chung: 28 đơn vị chuyển động**, không phải 28 file GLB hay 28 clip đều làm mới:

| Nhóm | Số | Danh mục mục tiêu |
|---|---:|---|
| Đứng và kết quả | 6 | Idle A/B, Fidget, Victory, Down, Rise |
| Di chuyển | 8 | Walk, Run, Strafe L/R, Back, Dash, Turn L/R |
| Hành động | 8 | Dẫn phi kiếm tự đánh, Kiếm A/B, Chưởng, Nâng trụ, Đóng trận, Tuyệt kỹ, Duy trì |
| Phản ứng | 6 | Hit trước/sau/bên, Stagger, Death A/B |
| **Tổng** | **28** | Thêm **10 pose thủ ấn** dạng dữ liệu; thở/nhìn/lò xo/xung chữ không tính thành clip |

Ước lượng thực hiện: khoảng **10–14 đơn vị cần dựng hoặc sửa đáng kể**, còn **14–18** có thể chọn và retarget/chỉnh từ kho đã có. Đây là dự toán phạm vi, không hứa số clip đạt sau một lần nhập. Chưa nhân lên cho 24 tổ hợp; Đao/Thương thêm grip và 2–3 động tác chủ lực mỗi loại khi đến lượt, còn chân/idle/hit dùng lại nếu kiểm qua.

**Cổng cần giữ:** D63 đang đặt mốc **8 clip đầu**; `IC_MODEL_CONTRACTS.cultivators` hiện bắt buộc `Idle`, `Run`, `Cast_Short`, `Hit`, tùy chọn `Cast_Heavy`, `Dash`, `Down`, `Victory`, và trần **12 clip**. Vì vậy gói model đầu đề xuất đúng tám tên đó; `Cast_Short` là kiếm A, `Cast_Heavy` là tuyệt kỹ mẫu. Bộ 28 là đích thư viện theo đợt, không nhét 28 clip vào GLB rồi bỏ qua validator. Cách nạp bundle hành động riêng hoặc sửa hợp đồng phải có phiếu và quyết định rõ trước khi mở rộng. Chưa xác nhận đường bundle đó tồn tại trong runtime.

## 8. Kế hoạch dựng theo đợt — đề xuất, chưa triển khai

| Đợt | Phạm vi nhỏ, đầu ra mong muốn | Điều kiện qua đợt |
|---|---|---|
| **1 — một chiêu để thử** | Dùng `human` đã có, camera chơi thật; chỉ Idle hiện có + một clip Kiếm A đủ gồng/nhả/thu, S0 và S1, ba xung chữ, lỗi/hủy/đổi đích. Hit sẵn có để thử ngắt. Dùng thành phần VFX/âm đã có để đối nhịp; không tạo look mới | Chứng minh ≤ 50 ms, không bind/trượt/bật; tay/hông có lực và đọc được ở xa. Hai người chấm thử độc lập; đạt ≥ 7 mọi mục áp dụng mới gửi demo theo skill, ghi rõ chưa đạt chuẩn 9. Không gọi lát cắt này là nghiệm thu hệ dùng chung |
| **2 — nhân vật và tám clip lõi** | Sau khi model thật được duyệt: rig theo D63, tám clip đúng hợp đồng §7; ngón và đúng bốn xương phụ. Chạy bộ đồ C và bộ lễ A bằng cùng skeleton, kiểm đổi đồ sớm | Không đổi tỷ lệ/retarget riêng từng bộ đồ; không xuyên vai/kiếm/vạt, đi và cast được. Lab `human` chỉ là đối chứng kỹ thuật; chấm nhân vật thật mới có ý nghĩa mỹ thuật |
| **3 — họ hành động và tám hệ** | Thêm chưởng, nâng trụ, đóng trận, duy trì; hoàn tất S2–S8 và biến thể kiếm; nạp action bundle chỉ sau khi hợp đồng được quyết | Hai chiêu khác action class nhìn khác từ thân ngay cả khi tắt VFX. Bật VFX phải cùng frame/đúng socket; không sinh thêm một bộ clip mỗi hệ |
| **4 — tuyệt kỹ và phản ứng đầy đủ** | Chỉ nếu gameplay chuỗi/Space được chốt: S9, vòng giữ sống, Phàm/Linh/Tiên; cut-in không làm trễ cam kết. Hoàn thiện hướng hit, gục/đứng dậy, chết A/B, thắng/thua | Gõ chậm, Space sớm/muộn/lặp, hit-stop, mất đích, thua giữa chuỗi đều có kết quả xác định; lớp nhìn không đổi luật |
| **5 — chấp nhận và dùng chung** | Bản chơi tích hợp thật với model/outfit/player settings; tái hiện cùng sự kiện như lab; kiểm ngân sách M4 và các rig khác rồi mới đưa lên kit theo quy trình riêng | Hai giám khảo mù độc lập cùng ≥ 9, không mục dưới 8,5, owner xem cuối; đủ chứng cứ runtime và ma trận chuyển xương nếu thay nguồn. Không coi kết quả chỉ trên URL lab là pass bản chơi |

Không định thời lượng theo ngày khi chưa có rig hero đích và số clip nguồn đạt. Chi phí lớn nhất nằm ở key pose, skin, đường chuyển và review, không ở việc xuất thêm nhiều biến thể. Sau ba lần sửa không tăng rõ, gom video/nhận xét để người chốt đổi cách làm theo skill, không tiếp tục tăng spring và phóng đại biên độ vô hướng.

## 9. Bài kiểm tra lab đề xuất

**Một kịch bản “gõ–đổi thế–khai ấn”, chưa chạy.** Bắt đầu với lát cắt đợt 1, sau đó mở các nhánh có thật ở đợt sau. Dùng camera chơi hiện tại theo thiết kế 12 m đang được chốt, không dùng riêng camera cận để che lỗi; có thêm góc tay cận để kiểm ngón. Tránh tự thay camera chỉ để điểm nhận diện cao.

| Đoạn | Thao tác và tình huống |
|---|---|
| A. Sống và định hướng | Idle 8 s → đi cung → dừng → xoay 90° và 180° → đi ngang/lùi → bắt đầu gõ. Fidget bị ngắt giữa chừng vẫn mềm |
| B. Tiến độ nhập | Gõ từ 3/5/8 chữ ở 15, 45, 90 WPM; chèn ngừng 2 s, sai lặp, Backspace và hủy/đổi đích. Thử paste/composition chỉ qua sự kiện mà tầng nhập chấp nhận, không giả một key vật lý là một chữ đúng |
| C. Phát dồn | Kết thúc từ khi đang thu chiêu, trong hit-stop và ngay sau bước xoay; thử hoàn thành tức thì để có trường hợp không kịp gồng. Phi kiếm tự đánh đồng thời không giành tay |
| D. Cùng hình khác hệ | Khi đợt 3 có: cùng một kiếm khí Kim → Hỏa → Thủy, sau đó chưởng/trụ/trận; xem riêng thân và bản ghép đầy đủ. Kiểm cả tám hướng đích |
| E. Cao trào | Khi gameplay được duyệt: chuỗi 2–3 từ, dừng giữa chuỗi, Space phân cách rồi Space khai ấn sớm/giữa/muộn và giữ phím. Mỗi lần tối đa một phát; thử vòng hết giờ, hit/choáng/gục, không có đích, cut-in và chuyển ra màn kết quả |
| F. Ngoại hình và kết quả | Hai outfit, một cảnh thắng, một cảnh thua cổng và hai kiểu chết; xem ngón/kiếm/cổ áo khi cận, chân/vai khi camera chơi |

Mỗi ca chạy ở **60 Hz và 120 Hz**, 1280×720 và 1920×1080 theo preset người chơi; đo riêng đồng hồ thật và clock world. Đợt 1 không buộc làm xong D–F để owner thử một chiêu; danh sách ca chưa có phải hiện là chưa thực hiện, không ghi PASS.

| Cổng | Ngưỡng và cách đọc |
|---|---|
| Trễ đầu vào → thân/VFX release đầu | Mọi ca phát hợp lệ ≤ 50 ms; ghi cả p95 và max. Dấu đầu vào lấy trước cut-in/hit-stop. Ca held/không được sim cho phát ghi trạng thái riêng, không tính như cast thành công |
| Đồng bộ | Thân, VFX, âm/camera theo cùng event; sai lệch marker ≤ 1 khung tại 60 Hz, kiểm lại bằng thời gian ở 120 Hz. Onset âm cần kiểm nghe/đo riêng nếu pipeline thu được |
| Chuyển tư thế | Không khung gần bind, không reset clip tạo giật; vận tốc góc chuyển ≤ 1,5 × đỉnh tham chiếu. Động tác mới cần đỉnh tham chiếu riêng, không so mọi cú bước với clip Idle rồi miễn lỗi bằng lời giải thích |
| Chân và vòng lặp | Chân trụ ≤ 0,05 m/s; seam ≤ 1 cm; xuyên đất ≤ 2% chiều cao. Đo trên hình đã tổng hợp cả root/IK, không chỉ trên clip sạch |
| Đọc động tác | Mục tiêu lab: nhận diện pha ≥ 80%, hướng ≥ 90% trong 8 hướng và cỡ 30/50/70 px như bài cũ; kiểm độ tách dáng gồng/nhả theo probe ≥ 15% chiều cao. Không thay chuẩn thẩm mỹ bằng các tỷ lệ này |
| Ngón và tiếp xúc | Không ngón xuyên lòng/kiếm, không vặn cổ tay hay vai bật; tiếp xúc ổn định khi dừng gõ và đổi outfit. Chưa có ngưỡng sai số ngón được duyệt: ghi khoảng cách/ảnh lỗi, chấm mù, không tự nhận một số mm là chuẩn repo |
| Tay và lớp phụ | Không dang cả hai tay > 70° quá ba khung ngoài pose chủ ý; không tua/áo xuyên thân, không lỗi nổ spring sau resume. Ngoài flash đã khai báo, alpha/cỡ lớp không đổi > 30% toàn mức trong một khung |
| Hiệu năng | Mốc tài liệu cho tổng animation High p95 ≤ 0,8 ms CPU, Ultra ≤ 1,2 ms; ngân sách frame game High là 12 ms. Đo lại trên M4 trong cảnh nặng, không lấy cỡ file hoặc số xương thay đo thời gian; hạ tần suất lớp phụ trước khi giảm chất lượng model |
| Chấm nhận | Hai giám khảo ngoài làn làm, chấm trước số liệu theo tám mục shared bar; phần đám đông chỉ xét khi tích hợp hệ dùng chung, không tự cho điểm từ một hero. Hai điểm tổng ≥ 9, không mục áp dụng < 8,5; owner chốt cuối |

Chứng cứ ở phiếu dựng sau: real-time 60 fps và nửa tốc độ, dải sáu khung quanh chuyển trạng thái, một bảng frame đầu vào/release/impact và metrics tách khỏi tài liệu chấm mù. Lưu tại `/Volumes/SS990TPRO/htdocs/typing-game-review/captures/tu-tien/393-animation/`, file gửi owner ở `owner-review/<ngày>/tu-tien/393-animation/`; thêm `ABOUT.md`, rebuild index, prune đúng khung thô do làn đó tạo. **Phiếu này không tạo các thư mục/capture đó.** Lab có thể dùng cờ dev để đo, còn chấm nhận cuối ở built play host, player settings, không URL flags.

## 10. Rủi ro và những gì owner cần xem

| Rủi ro | Cách xử lý đề xuất |
|---|---|
| Chốt animation theo lối chơi Gemini rồi 392 chọn khác | Tách `progress`, `ready`, `commit`, `cancel`; thử chuỗi/Space ở lab riêng sau khi luật được duyệt, bộ kiếm thường vẫn dùng được với Bàn Quyết |
| Thủ ấn rất đẹp khi cận nhưng mất ở camera sau 55° | Nhìn bóng khuỷu–tay–vũ khí trước, chi tiết ngón sau; không dùng zoom bắt buộc cho mọi từ, không để ánh chớp che dáng mạnh nhất |
| Ngón đủ xương nhưng topology/skin kém | Kiểm từng ngón, ngón cái và tiếp xúc trên model thật; không trả clip thiếu chất bằng một lớp glow |
| Áo/tóc đẹp nhưng vi phạm bốn xương hoặc che tay | Theo D63, hai outfit thử sớm, phần lụa VFX phối riêng; không mở cloth simulation hoặc thêm xương ngoài phiếu |
| Full-body auto-attack phá ấn đang gõ | Tự đánh chỉ dẫn nhẹ/không dùng tay khi đang cast; ưu tiên hành động người chơi; mọi viên kiếm vẫn theo sim |
| Phát nhanh bị giật, phát mềm bị trễ | Gồng theo chữ, chuẩn bị hướng sớm; đường phát ngắn từ nhiều pose, ngắt thu; đo trường hợp không đủ gồng và chỉnh clip, không nới 50 ms |
| Bộ 28 vượt hợp đồng 12 và mốc tám clip | Gói đầu đúng tám, chỉ mở thư viện bổ sung khi có thiết kế nạp và cổng rõ; không bỏ validator hoặc nạp toàn bộ 162 clip nguồn |
| Quá tin điểm nhận diện/spring | So chuyển động thực với thương mại và chấm diễn xuất; vòng 4 đã cho thấy 97–100% nhận diện vẫn chỉ 4,6 cảm nhận |

Owner cần xem ở đợt dựng: **một kiếm khí với lực chạy từ chân lên tay, ấn có ngón thật, thu thế mềm**, tại camera chơi và cận tay; sau đó mới xem ba cấp khai ấn và đổi trang phục. Trước phiếu dựng, người chốt cần xác nhận lệnh tuyệt kỹ/cutin, phạm vi tám clip đầu và cách mở thư viện ngoài trần 12. Không cần chốt lại màu/hệ hay thiết kế nhân vật trong phiếu báo cáo này.

**Tự kiểm phạm vi:** đã đọc hợp đồng, canon, MOTION_PLAN và phân tích Gemini; kiểm trực tiếp ba GLB và code nạp/diễn; có bảng khoảnh khắc, 10 thủ ấn có mức xác thực, chân–tay với nhịp 60 Hz, giải pháp rig/lớp/sự kiện, nguồn clip, ước lượng và kế hoạch/lab. Chưa dựng/chạy/chấm nhận; không tạo ảnh, video, âm hay clip; không sửa code hoặc tài liệu game. Đầu ra duy nhất: `docs/codex-queue/393-report.md`.
