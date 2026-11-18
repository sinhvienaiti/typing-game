# Phiếu 212 · Last Line · danh sách âm Firefly Map 1

Ngày 30/10/2026. Nhánh repo cha `feat/space-typing-admin-uiux`; mã game chỉ đọc ở `games/typing-survival`, nhánh `main`, HEAD `79db62851e00eadeca7bfd44c10c0c682a9cec8d`.

## Kết quả giao

Đã viết đủ bốn file [README](../games/audio/firefly/README.md), [schema.json](../games/audio/firefly/schema.json), [typing-survival.md](../games/audio/firefly/typing-survival.md), [typing-survival.json](../games/audio/firefly/typing-survival.json). Danh sách chép cho chủ dự án có **37 hàng, 66 lượt dự kiến**: P0 **50**, P1 **11**, P2 **5**. Đây là file kết quả cần tạo theo giả định hao hụt 25%, không phải số thao tác, credit hay bảo đảm chất lượng.

Script [212/check.mjs](212/check.mjs) đọc các mảng SOUND_IDS và spread từ mã, tên thẻ từ đĩa; export validator cùng hàm tính lượt/tổng cho 213. [check.txt](212/check.txt), [check.json](212/check.json), [check-selftest.txt](212/check-selftest.txt), [check-selftest.json](212/check-selftest.json) lưu đầu ra. [source-evidence.json](212/source-evidence.json) lưu bảng căn cứ máy đọc được; `make-data.py` và `make-evidence.py` giữ cách dựng tài liệu trong phạm vi phiếu. Muốn dựng lại hoàn toàn: chạy `python3 docs/codex-queue/212/make-evidence.py`, rồi `python3 docs/codex-queue/212/make-data.py`, sau đó hai lệnh kiểm. Hai script dựng không chạy game hoặc gọi model.

## Điều kiện trước và phạm vi

`grep -n "docs/games/audio/firefly" docs/HANDOFF_CURRENT.md` có kết quả tại **dòng 153**, trỏ đúng phiếu 212/213 và bước nhận 217. Không sửa HANDOFF. Theo xác nhận làn FF đã dừng trong đề bài, tiếp tục một danh sách duy nhất ở đường dẫn mới; không viết `FIREFLY_SOUND_LIST.md` cũ.

Đã lưu `git status --short -uall` và `git diff --stat` trước vào [status-before.txt](212/status-before.txt), HEAD/status game vào [game-before.txt](212/game-before.txt). Không gọi mạng, không tạo/tổng hợp âm hay ảnh, không tạo thư mục inbox ngoài repo; chỉ đọc tên WAV trong Downloads để biết mẫu. Không chạy build/test suite game; không gọi lệnh Git có ghi; không chạm worktree khác hoặc Tu Tiên.

Dùng `game-vfx-layered` để đối chiếu pha và mốc A/R/T/I/F với VFX_STANDARD §3.1. Phiếu chỉ lập danh sách âm; không sửa VFX, không có capture hay tuyên bố nghiệm thu hình/nghe. Tài liệu hướng B thắng chất liệu thời tàu; thẻ YAML quyết định độ dài/biến thể khi có số.

## Số kiểm

| Mục | Số và kết quả |
|---|---|
| 1. `node docs/codex-queue/212/check.mjs` | **Thoát 0**. SOUND_IDS **46**, thẻ **46**, hợp **50 id**; rows **37**, excluded **12**, retired **1**. Thiếu **0**, trùng **0**, lạ **0**, lỗi lược đồ **0**, prompt lỗi **0**, tên Việt **0**, Markdown lệch JSON **0**, sai phép tính **0**, lệch thẻ **0**. Tổng **66 lượt**. |
| 2. `node docs/codex-queue/212/check.mjs --selftest` | **Thoát 0, bắt 3/3**: bỏ hàng, thêm từ cấm vào prompt, thêm id lạ. Mọi lỗi chỉ cài trong bộ nhớ. |
| 3. Game không đổi | **Đạt**: HEAD và status sau giống từng byte `game-before.txt`; bản sau ở `game-after.txt`. Game sạch trước và sau. |
| 4. Repo cha | Thao tác ghi của phiếu chỉ ở đường dẫn cho phép. **So trạng thái toàn repo chưa đạt nguyên xi** vì có thay đổi đồng thời ngoài phạm vi; xem mục cuối và `state-check.json`. Không sửa/dọn chúng để ép kết quả đạt. |
| 5. Báo cáo | Có bảng đầy đủ **46/46** SOUND_IDS, xử lý **4/4** id chỉ thẻ và **4/4** id chỉ mã, các hàng đổi nghĩa/dừng, số kiểm và câu hỏi Firefly. |

Prompt dài nhất: **289 ký tự ASCII**, `gun.phao.launch`. Giới hạn Firefly **chưa biết**, chưa kết luận prompt có vừa giao diện hay không. Validator là tập từ khóa 2020-12 dùng trong schema, không tuyên bố hỗ trợ toàn bộ chuẩn.

Loại trừ theo nhóm lý do: tiếng phím **2** (189–191); nhạc **2** (stem 96 BPM La thứ); Pack Leader ngoài ải **2** (c1-s2); Rift **2** (c1-s3); Shield Guard **2** (c1-s4); Splitter chưa có ải cấu hình **1**; hit.t4 chưa có đường đạt T4 **1**. Tổng **12**. Mỗi id có lý do riêng trong JSON, cùng `firstStage`; null ghi rõ chưa có thay vì đoán ải tương lai.

## Bằng chứng từng SOUND_IDS

Trong bảng, các đường dẫn ở cột gọi được viết đầy đủ. Đường rút gọn trong cột điều kiện đều tính từ `games/typing-survival/src/`. “Trong” gồm menu/chọn súng/cài đặt/kết quả gắn với vòng chơi First Shift; không có nghĩa mọi âm đều tự phát trong mọi ván. 34 id trong mã có đường phát thuộc phạm vi; cộng ba lớp dự kiến tách file thành 37 hàng sản xuất.

First Shift: `content/chapter-1.ts:39–53` giữ 150 s, hazard null, Scout từ 12 s, brute pack từ 80 s, hai surge 50/115 s và PACE_HOLD. `content/stage-rules.ts:103` cho phép support; `app/journey.ts:142,162,194–205` cho chọn 2 trong 5 súng nên không loại súng theo mặc định. `sim/spawn.ts:180–184` không mở loại pack thiếu trong cấu hình. `audio/theme-audio.ts:29–36,76–90` quyết định bus.

| Id | Trong/ngoài `c1-s1`; xử lý | Nơi gọi / chọn id | Điều kiện ải |
|---|---|---|---|
| `key.ok` | Trong; excluded (bộ khác) | `games/typing-survival/src/view/typing-feel.ts:120; games/typing-survival/src/audio/theme-audio.ts:222` | Gõ trong bất kỳ bến súng nào; content/chapter-1.ts:39–53 |
| `key.bad` | Trong; excluded (bộ khác) | `games/typing-survival/src/view/typing-feel.ts:129; games/typing-survival/src/audio/theme-audio.ts:228` | Gõ trong bất kỳ bến súng nào; content/chapter-1.ts:39–53 |
| `word.load` | Trong; rows | `games/typing-survival/src/view/typing-feel.ts:140–146; games/typing-survival/src/audio/theme-audio.ts:234–238` | Gõ trong bất kỳ bến súng nào; content/chapter-1.ts:39–53 |
| `word.perfect` | Trong; rows | `games/typing-survival/src/view/typing-feel.ts:140–146; games/typing-survival/src/audio/theme-audio.ts:234–238` | Gõ trong bất kỳ bến súng nào; content/chapter-1.ts:39–53 |
| `word.full` | Trong; rows | `games/typing-survival/src/view/typing-feel.ts:140–146; games/typing-survival/src/audio/type-audio.ts:72–77` | Từ vẫn hoàn tất khi bến đã đầy: view/typing-feel.ts:140–146; content/chapter-1.ts:39–53 |
| `streak.up` | Trong; rows | `games/typing-survival/src/view/typing-feel.ts:160–162; games/typing-survival/src/audio/type-audio.ts:81–86` | Gõ trong bất kỳ bến súng nào; content/chapter-1.ts:39–53 |
| `gun.xung` | Trong; rows | `games/typing-survival/src/view/shots.ts:178; games/typing-survival/src/audio/theme-audio.ts:248–250` | Chọn súng tương ứng trong 2/5; app/journey.ts:142,162,194–205; content/chapter-1.ts:39–53 |
| `gun.xung.tail` | Trong; rows | `games/typing-survival/src/view/shots.ts:181,431; games/typing-survival/src/audio/theme-audio.ts:254–256` | Chọn súng tương ứng trong 2/5; app/journey.ts:142,162,194–205; content/chapter-1.ts:39–53 |
| `gun.tia.start` | Trong; rows | `games/typing-survival/src/view/combat.ts:261–266; games/typing-survival/src/audio/theme-audio.ts:260–267` | Chọn súng tương ứng trong 2/5; app/journey.ts:142,162,194–205; content/chapter-1.ts:39–53 |
| `gun.tia.end` | Trong; rows | `games/typing-survival/src/view/combat.ts:269–271; games/typing-survival/src/audio/theme-audio.ts:270–271` | Chọn súng tương ứng trong 2/5; app/journey.ts:142,162,194–205; content/chapter-1.ts:39–53 |
| `gun.tia.loop` | Trong; rows | `games/typing-survival/src/view/beams.ts:172–184; games/typing-survival/src/audio/theme-audio.ts:206–214` | Chọn súng tương ứng trong 2/5; app/journey.ts:142,162,194–205; content/chapter-1.ts:39–53 |
| `gun.tia.pulse` | Trong; rows | `games/typing-survival/src/view/combat.ts:193,294; games/typing-survival/src/audio/theme-audio.ts:275–280` | Chọn súng tương ứng trong 2/5; app/journey.ts:142,162,194–205; content/chapter-1.ts:39–53 |
| `gun.tan.fire` | Trong; rows | `games/typing-survival/src/view/gunfx.ts:71–72` | Chọn súng tương ứng trong 2/5; app/journey.ts:142,162,194–205; content/chapter-1.ts:39–53 |
| `gun.ray.armed` | Trong; rows | `games/typing-survival/src/view/beams.ts:163–165; games/typing-survival/src/audio/gun-audio.ts:76` | Chọn súng tương ứng trong 2/5; app/journey.ts:142,162,194–205; content/chapter-1.ts:39–53 |
| `gun.ray.charge` | Trong; rows | `games/typing-survival/src/view/gunfx.ts:73–74` | Chọn súng tương ứng trong 2/5; app/journey.ts:142,162,194–205; content/chapter-1.ts:39–53 |
| `gun.ray.fire` | Trong; rows | `games/typing-survival/src/view/gunfx.ts:75–76` | Chọn súng tương ứng trong 2/5; app/journey.ts:142,162,194–205; content/chapter-1.ts:39–53 |
| `gun.phao.launch` | Trong; rows | `games/typing-survival/src/view/gunfx.ts:77–78` | Chọn súng tương ứng trong 2/5; app/journey.ts:142,162,194–205; content/chapter-1.ts:39–53 |
| `gun.phao.burst` | Trong; rows | `games/typing-survival/src/view/gunfx.ts:79–82; games/typing-survival/src/view/combat.ts:197–198` | Chọn súng tương ứng trong 2/5; app/journey.ts:142,162,194–205; content/chapter-1.ts:39–53 |
| `hit.t1` | Trong; rows | `games/typing-survival/src/view/combat.ts:185–198; games/typing-survival/src/audio/theme-audio.ts:294–303` | Đòn thường/crit/perfect có T1–T3; content/chapter-1.ts:39–53 |
| `hit.t2` | Trong; rows | `games/typing-survival/src/view/combat.ts:185–198; games/typing-survival/src/audio/theme-audio.ts:294–303` | Đòn thường/crit/perfect có T1–T3; content/chapter-1.ts:39–53 |
| `hit.t4` | Ngoài; excluded | `games/typing-survival/src/view/combat.ts:186,198; games/typing-survival/src/audio/theme-audio.ts:298; games/typing-survival/src/kit/feedback/tiers.ts:38–39` | Ngoài mọi ải hiện tại: chỉ một nơi gọi audio.hit, view/combat.ts:186,198, t tối đa 3; tail cần T4, kit/feedback/tiers.ts:38–39; quái lớn chết không gọi audio.hit |
| `hit.armour` | Trong; rows | `games/typing-survival/src/view/combat.ts:185–190; games/typing-survival/src/audio/theme-audio.ts:82` | Brute Armor 4 từ 80 s; content/foes.ts:46; content/chapter-1.ts:49; affix giáp còn có ở sim/pace.ts:244–250 |
| `kill.swarm` | Trong; rows | `games/typing-survival/src/view/combat.ts:351–366; games/typing-survival/src/audio/theme-audio.ts:319` | Swarm và Brute không mang cờ Scout; content/foes.ts:44,46; content/chapter-1.ts:39–53 |
| `kill.elite` | Trong; rows | `games/typing-survival/src/view/combat.ts:351–366; games/typing-survival/src/audio/theme-audio.ts:319` | Cụm có Scout từ 12 s, không lấy kích cỡ làm cờ; content/chapter-1.ts:48; view/combat.ts:337,351,366 |
| `foe.shot` | Trong; rows | `games/typing-survival/src/view/combat.ts:233–235; games/typing-survival/src/audio/theme-audio.ts:336` | Scout từ 12 s; content/chapter-1.ts:48; foe.shot.down cần Pulse Gun trong lựa chọn 2/5 |
| `foe.shot.down` | Trong; rows | `games/typing-survival/src/view/combat.ts:237–240; games/typing-survival/src/audio/theme-audio.ts:344` | Scout từ 12 s; content/chapter-1.ts:48; foe.shot.down cần Pulse Gun trong lựa chọn 2/5 |
| `hurt.hull` | Trong; rows | `games/typing-survival/src/view/combat.ts:223–228; games/typing-survival/src/audio/theme-audio.ts:352–365` | Scout từ 12 s; content/chapter-1.ts:48; foe.shot.down cần Pulse Gun trong lựa chọn 2/5 |
| `hurt.breach` | Trong; rows | `games/typing-survival/src/view/combat.ts:213–218; games/typing-survival/src/audio/theme-audio.ts:352–360` | Để quái áp sát/vượt tuyến hoặc Armor cạn; content/chapter-1.ts:24,42–53; sim/pace.ts:119–145 |
| `hurt.drain` | Trong; rows | `games/typing-survival/src/view/combat.ts:245–250; games/typing-survival/src/audio/theme-audio.ts:372–378` | Để quái áp sát/vượt tuyến hoặc Armor cạn; content/chapter-1.ts:24,42–53; sim/pace.ts:119–145 |
| `support.repair` | Trong; rows | `games/typing-survival/src/view/combat.ts:253–258; games/typing-survival/src/sim/pace.ts:229–233` | Director bật và chọn support khi nguy; content/chapter-1.ts:52; content/stage-rules.ts:103; sim/pace.ts:97–98,229–233 |
| `alarm.surge` | Trong; rows | `games/typing-survival/src/app/main.ts:649; games/typing-survival/src/audio/theme-audio.ts:392–399` | Hai surge gốc 50/115 s; content/chapter-1.ts:47; pace có thể dời, sim/pace.ts:223–225 |
| `end.win` | Trong; rows | `games/typing-survival/src/view/combat.ts:283–285; games/typing-survival/src/audio/theme-audio.ts:403–409` | Giữ đủ 150 s; content/chapter-1.ts:42 |
| `end.lose` | Trong; rows | `games/typing-survival/src/view/combat.ts:283–285; games/typing-survival/src/audio/theme-audio.ts:403–415` | Để quái áp sát/vượt tuyến hoặc Armor cạn; content/chapter-1.ts:24,42–53; sim/pace.ts:119–145 |
| `ui.move` | Trong; rows | `games/typing-survival/src/app/main.ts:393,472,502; games/typing-survival/src/app/journey.ts:222,235` | Menu, cài đặt và chọn súng quanh First Shift; app/journey.ts:142,194–205; app/main.ts:390–416 |
| `ui.select` | Trong; rows | `games/typing-survival/src/app/main.ts:416,579; games/typing-survival/src/app/journey.ts:205,261` | Menu, cài đặt và chọn súng quanh First Shift; app/journey.ts:142,194–205; app/main.ts:390–416 |
| `ui.back` | Trong; rows | `games/typing-survival/src/app/main.ts:398,483; games/typing-survival/src/app/journey.ts:200,267` | Menu, cài đặt và chọn súng quanh First Shift; app/journey.ts:142,194–205; app/main.ts:390–416 |
| `star.get` | Trong; rows | `games/typing-survival/src/app/main.ts:182–186` | Ải khác s0 và stars.some(Boolean); app/main.ts:182–186; content/chapter-1.ts:39–42 |
| `music.calm` | Trong; excluded (bộ khác) | `games/typing-survival/src/audio/theme-audio.ts:131–151` | Có thể phát trong/ngoài trận nhưng loại khỏi SFX; app/main.ts:651; content/chapter-1.ts:39–53 |
| `music.surge` | Trong; excluded (bộ khác) | `games/typing-survival/src/app/main.ts:651; games/typing-survival/src/audio/theme-audio.ts:434–443` | Có thể phát trong/ngoài trận nhưng loại khỏi SFX; app/main.ts:651; content/chapter-1.ts:39–53 |
| `leader.horn` | Ngoài; excluded | `games/typing-survival/src/view/gunfx.ts:90–91` | Ngoài ải; đầu tiên c1-s2, objective hunt; content/chapter-1.ts:57–60; c1-s1 chỉ hold, :42 |
| `leader.down` | Ngoài; excluded | `games/typing-survival/src/view/gunfx.ts:92–96` | Ngoài ải; đầu tiên c1-s2, objective hunt; content/chapter-1.ts:57–60; c1-s1 chỉ hold, :42 |
| `rift.warn` | Ngoài; excluded | `games/typing-survival/src/view/gunfx.ts:101–104` | Ngoài ải; đầu tiên c1-s3; content/chapter-1.ts:74–78; c1-s1 hazard null, :43 |
| `rift.open` | Ngoài; excluded | `games/typing-survival/src/view/gunfx.ts:105–107` | Ngoài ải; đầu tiên c1-s3; content/chapter-1.ts:74–78; c1-s1 hazard null, :43 |
| `shield.hit` | Ngoài; excluded | `games/typing-survival/src/view/gunfx.ts:83–84` | Ngoài ải; đầu tiên c1-s4; content/chapter-1.ts:91–101; c1-s1 chỉ brute, :49 |
| `shield.break` | Ngoài; excluded | `games/typing-survival/src/view/gunfx.ts:85–87` | Ngoài ải; đầu tiên c1-s4; content/chapter-1.ts:91–101; c1-s1 chỉ brute, :49 |
| `foe.split` | Ngoài; excluded | `games/typing-survival/src/view/gunfx.ts:88–89; games/typing-survival/src/sim/projectiles.ts:51` | Ngoài ải; chưa có ải đầu tiên trong mã; content/chapter-1.ts:36–107 và content/stage-s0.ts:67 không có splitter pack; sim/spawn.ts:180–184 bỏ loại thiếu cấu hình |

## Id chỉ ở thẻ và chỉ ở mã

| Id chỉ ở thẻ | Xử lý | Lý do và căn cứ |
|---|---|---|
| `hit.sub` | rows, P0; 80–120 ms, 1 biến thể | Bắt buộc theo phiếu; lớp sub của bậc trúng theo AUDIO_PIPELINE §6.3 mục 3. Chưa có id phát riêng: `theme-audio.ts:294–303` còn nhúng tone 160 ms. Thẻ duration trống; trần 120 ms lấy AUDIO_PIPELINE §8.3, khoảng 80–120 ms là mục tiêu biên tập, chưa đo từ Firefly. |
| `hit.tail` | rows, P0; 500–700 ms, 2 biến thể | Bắt buộc theo phiếu; lớp đuôi dùng chung. Thẻ trống, THEME_SOUND_LIST §2/§5 nói lớp đề xuất; `theme-audio.ts:294–307` có nhiễu 500 ms và thép 700 ms làm mốc. Chưa có id riêng; điều kiện tail từ T4 hiện không đạt trong First Shift. |
| `kill.chime` | rows, P0; 240 ms, 1 biến thể | **Giữ** vì sự kiện nốt hạ vẫn còn theo AUDIO_PIPELINE §6.4/§8.3 và THEME_SOUND_LIST §5. `theme-audio.ts:315–328` đang nhúng nốt 240 ms và đổi cao độ theo chuỗi. Thẻ duration trống; mốc 240 ms lấy hàm phát, biến thể 1 lấy thẻ. Đây là hàng chuẩn bị tách lớp, chưa phải id độc lập đang phát. |
| `gun.xung.loop` | retired; không prompt | **Dừng** nền cơ khí liên thanh của đề xuất cũ: hướng B có Pulse Gun phát từng viên và đuôi riêng (`shots.ts:178–181,431`); danh sách LOOP_SOUND_IDS hiện chỉ có hai vòng khác (`gun-audio.ts:37`). Không còn sự kiện âm cơ khí riêng để tạo. |

| Id chỉ ở mã | Xử lý và mốc bổ sung khi không có thẻ |
|---|---|
| `gun.tia.loop` | rows, P0. THEME_SOUND_LIST §4 có prompt vòng 2 s; `gun-audio.ts:75`, `beams.ts:172–184`. Mục tiêu đoạn vòng 2000 ms, 1 biến thể theo mặc định biên tập của §2; không suy ra file Firefly chỉ dài 2 s. |
| `gun.ray.armed` | rows, P0. THEME_SOUND_LIST §9 có vòng 2 s; `gun-audio.ts:76`, `beams.ts:163–165`. Đoạn vòng 2000 ms, 1 biến thể theo mặc định biên tập §2. |
| `word.full` | rows, P0. THEME_SOUND_LIST dòng 48/57 có 100 ms; `type-audio.ts:72–77`. 1 biến thể là mặc định biên tập §2, không nằm nhóm cần 4–6. |
| `streak.up` | rows, P0. THEME_SOUND_LIST dòng 49/58 mô tả hai cú cách 60 ms và đuôi 200 ms; `type-audio.ts:81–86` xác nhận tổng 260 ms. 1 biến thể là mặc định biên tập §2. |

**Khác với kiểm sơ:** 35 id SOUND_IDS dự kiến sau khi loại 11 id ban đầu giảm còn **34** do `hit.t4` không thể tới nhánh `row.tail`. `combat.ts:186` chỉ tính t tối đa 3, `:198` là chỗ duy nhất gọi `audio.hit`; `theme-audio.ts:298` cần cờ tail của T4/T5 để chọn hit.t4. VFX chết lớn không nâng bậc pending. Chưa biết ải đầu tiên phát được, vì mã hiện tại không có. Cộng hai lớp bắt buộc và `kill.chime` được chọn giữ = **37**, không phải đưa hit.t4 vào chỉ để khớp số dự kiến.

Hai sai khác khác cần giữ khi gắn: `kill.elite` được chọn bằng cờ Scout, không bằng kích thước; Brute vẫn đi `kill.swarm` dù có VFX chết lớn (`combat.ts:351–366`). `star.get` hiện gọi một lần khi có bất kỳ sao nào, không phát riêng từng sao bay (`main.ts:182–186`). Không sửa hành vi trong phiếu này.

THEME_SOUND_LIST dòng 31 còn nói mỗi file tự ghép sẵn và gun.xung.tail chỉ là đề xuất; mã đã có đuôi, AUDIO_PIPELINE §6.3 mục 3 yêu cầu tách tầng khi gắn file. Danh sách này giữ đầu+thân của từng bậc, tách hit.sub/hit.tail, không nướng thêm sub dài vào hit.t2 rồi ghép chồng. Thẻ gun.xung cũng còn mô tả một nửa số viên, trong khi mã/Theme mới phát mỗi viên; giữ số duration thẻ theo phiếu và yêu cầu nghe lặp dày ở bước ingest. Độ dài mới cần chủ dự án nghe, không tự sửa thẻ.

## Các hàng đổi nghĩa và id cũ

Mọi id mã súng giữ nguyên; tên người chơi đọc lấy từ `content/guns.ts:130–134`: Pulse Gun, Heat Beam, Scatter Gun, Rail Gun, Star Mortar. Tên quái lấy `content/foes.ts:44–50`. Prompt dùng mô tả nguồn chung, không chứa tên game, phe, nhân vật hay thương hiệu.

| Hàng `reworded` | Vì sao |
|---|---|
| `word.load` | Băng đạn đóng đổi thành vòng ký hiệu khóa quanh súng canh. |
| `word.perfect` | Nạp băng kèm điện đổi thành vòng ký hiệu vàng trắng khóa và chuông cao, cùng điều kiện perfect. |
| `word.full` | Chốt băng đạn hụt đổi thành phản hồi vòng năng lượng đã đầy; vẫn không nhận thêm đạn. |
| `gun.xung` | Súng cơ khí thời tàu đổi thành Pulse Gun canh bay: đầu tinh thể, thân plasma, vẫn phát mỗi viên. |
| `gun.xung.tail` | Vang hành lang thép đổi thành dư âm plasma trên đường đắp thép than chì và đá cổ, giữ lịch gọi đuôi. |
| `gun.tia.start` | Máy phát công nghiệp bật đổi thành súng canh gom năng lượng rồi mồi plasma, giữ EV.beamStart. |
| `gun.tan.fire` | Khóa bơm và vỏ đạn cơ khí đổi thành nổ chùm plasma từ súng canh, giữ một âm mỗi volley. |
| `gun.ray.fire` | Nổ súng ray cơ khí đổi thành nhát xả năng lượng xuyên có đuôi ion, giữ EV.rail. |
| `gun.phao.launch` | Đạn trượt vào ống thép đổi thành quả sáng khóa năng lượng và phóng theo cung từ súng canh. |
| `gun.phao.burst` | Nổ mảnh trên sàn thép đổi thành quả plasma phá kính đen trên đường đắp đá cổ, giữ tiếng nổ vùng riêng. |
| `hit.t1` | Keng nhẹ trên vỏ thép đổi thành nứt kính đen nhỏ, vẫn là đầu và thân của bậc T1. |
| `hit.t2` | Keng trên thép dày đổi thành va chạm kính đen dày, vẫn là đầu và thân T2–T3 để ghép sub sau. |
| `hit.armour` | Đòn bị vỏ máy chặn đổi thành đạn năng lượng bật khỏi Armor; vai trò báo bị chặn giữ nguyên. |
| `hit.tail` | Đuôi kim loại trong hành lang đổi thành ngân thấp của thép than chì và đá cổ trên đường đắp rộng. |
| `kill.swarm` | Kim loại vỡ đổi thành kính đen vỡ; Brute vẫn dùng cùng nhánh âm hiện tại. |
| `kill.elite` | Máy thép nổ đổi thành Scout kính đen tan cùng phóng điện. |
| `kill.chime` | Thanh thép leo nốt đổi chất âm tinh thể; sự kiện nốt thưởng vẫn còn. |
| `foe.shot` | Cầu plasma của lính máy đổi bối cảnh thành phát bắn của Scout kính đen, giữ nạp ngắn và tiếng lao tới. |
| `foe.shot.down` | Đạn kim loại vỡ đổi thành cầu plasma bị chặn với tia lửa và mảnh tinh thể, giữ EV.shotDown. |
| `hurt.hull` | Thân tàu bị đập đổi thành giáp Lightbearer lóe khiên lam và áo choàng giật. |
| `hurt.breach` | Thủng thân trạm đổi thành tuyến phòng thủ bị phá và mất Armor của nhân vật, giữ va chạm kèm báo động. |
| `hurt.drain` | Điện hút trên tấm thép đổi thành hồ quang hút trường bảo vệ quanh giáp nhân vật, vẫn giới hạn mỗi 420 ms. |
| `end.win` | Hợp âm máy kèm xả hơi đổi thành hợp âm năng lượng và âm bội tinh thể vàng trắng, cùng sự kiện thắng. |
| `end.lose` | Máy hạ điện và thép sụp đổi thành trường năng lượng tắt, kính đen lắng trên đá cổ, cùng sự kiện thua. |
| `support.repair` | Khoang sửa cập đổi thành vòng xanh từ trên xuống, vẫn tăng Armor. |
| `ui.move` | Rơ-le chọn mục đổi thành chạm kính khói rất ngắn, giữ hành động đổi focus. |
| `ui.select` | Công tắc nặng đổi thành chạm kính khói và cộng hưởng xác nhận thấp, giữ hành động chọn. |
| `ui.back` | Công tắc hạ đổi thành kính khói khép và ngân thấp đi xuống, giữ hành động quay lại. |

| `retired` | Vì sao |
|---|---|
| `gun.xung.loop` | Nền cơ khí liên thanh thời tàu không còn sự kiện âm riêng trong hướng B: Pulse Gun phát từng viên và có đuôi riêng, không có lệnh loop này. |

`kept` không có nghĩa giữ prompt cũ nguyên văn: cùng sự kiện/cùng nghĩa nhưng viết lại tiếng Anh khẳng định, nhường giọng đọc và đổi không gian vang. Các fallback duration có ghi rõ trong basis. Không tự suy thêm id cho quái đi, quái ra, bước Brute hay nền hố đen vì chưa có registry/thẻ tương ứng; đây là khoảng trống trong bible để làn game cân nhắc sau, không lẫn vào lô tạo này.

## Việc bỏ qua và việc chủ dự án cần xem

Không làm danh sách Dragonhold/Wordwoven; 213 đợi Claude commit schema và import hàm chung. Không tạo âm, chuẩn hóa, nghe duyệt, gắn file, sửa bus, sửa thẻ hay luật game. Không nhận xét chất lượng âm đã đạt vì chưa có file của lô này. Lược đồ có sẵn `sourceCommits`, `branchOnly`, `clips`, `clipsWhy`; Last Line không tự ghép clip VFX Firefly ngoài phạm vi.

Claude cần xem trước khi gửi: quyết định loại `hit.t4`; giữ `kill.chime` như lớp chuẩn bị; dừng `gun.xung.loop`; các mốc duration khi thẻ trống; giả định dùng được 75% và tổng 66 lượt. 37 hàng gồm 34 id có đường phát, 3 lớp chuẩn bị; không ghi rằng cả 37 id đều đang được mã gọi.

Câu hỏi cho chủ dự án sau lượt thử đầu (hiện đều **chưa biết**, không chặn soạn danh sách):

1. Giao diện Firefly chấp nhận tối đa bao nhiêu ký tự prompt? Prompt dài nhất danh sách là 289 ký tự.
2. Có chọn/chỉnh độ dài được không, và các giá trị nào hiện có? File khoảng 12 s của lô 189 chỉ là quan sát.
3. Một thao tác cho bao nhiêu file, tính credit theo thao tác/file/thời lượng thế nào; có giới hạn tốc độ nào?
4. Gợi ý bằng giọng có được công cụ hỗ trợ và giúp bám nhịp không? Có thể diễn để chia cú sạch như lô phím không?
5. Sau lượt đầu, có bao nhiêu cú tách dùng được trong mỗi file; vòng đều có cắt liền được không? Dùng số thực đó để Claude sửa usableFraction và fileSeconds, rồi kiểm lại JSON/Markdown.

## Đối chiếu trạng thái sau

Bản ghi cuối nằm ở [status-after.txt](212/status-after.txt), [game-after.txt](212/game-after.txt), [state-check.json](212/state-check.json). Phần trạng thái repo cha có thay đổi từ các làn đồng thời, nên không thể khẳng định cả năm mục đều đạt nguyên xi. Tôi không thay đổi các file đó. Các thay đổi ngoài phạm vi được ghi dưới dạng chênh trạng thái, không quy kết nội dung hay tác giả từ `git status`.

Lần chụp cuối: **19** dòng trạng thái mới trong phạm vi phiếu; **27** dòng mới ngoài phạm vi và **76** dòng trước đó không còn xuất hiện. Dòng biến mất có thể do làn khác đã xử lý Git; không suy ra file bị xóa. Game giống trước: **có**. Đối chiếu repo cha vì vậy ghi ngoại lệ, không ghi đạt toàn cục.
