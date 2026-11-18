# Phiếu 132 · Bảng duyệt cũ → mới

**306 chuỗi nguồn/trang và 52 chuỗi hoặc dòng kỳ vọng test**. `file:dòng` là vị trí hiện tại; mảnh template giữ phần chữ tĩnh, không đổi nội suy. Bảng gồm cả nhãn không dấu và lời khuyên từng đọc động từ kit.

Độ dài đếm Unicode đã hiển thị (bỏ thẻ HTML hoàn chỉnh, chưa đo pixel); mỗi mảnh nội suy được đếm riêng. ⚑ là mảnh còn dài quá 20%, chưa coi đạt cổng độ dài. Đã rút `Typing stats` thành `Profile`, `Break Shield` thành `Shatter`, và nhiều nhãn/toast; các từ ngắn như Build, Learn, Good, Sound cần Claude chốt cách viết trong ô thật. Tên Wordwoven là tên bắt buộc. Không có kiểm tràn chữ bằng trình duyệt trong phiếu này.

| file:dòng | chuỗi cũ | chuỗi mới | ghi chú |
|---|---|---|---|
| `index.html:2` | `vi` | `en` | 2→2 ký tự (≤120%). |
| `index.html:10` | `Lời Gọi · Wordwoven` | `Wordwoven` | 19→9 ký tự (≤120%). Tên game bắt buộc. |
| `index.html:13` | `Bản đồ` | `Map` | 6→3 ký tự (≤120%). |
| `index.html:14` | `Lời Gọi · đang tải từ vựng…` | `Wordwoven · loading words…` | 27→26 ký tự (≤120%). Tên game bắt buộc. |
| `src/app/prefs.ts:17` | `Âm lượng chung` | `Master volume` | 14→13 ký tự (≤120%). |
| `src/app/prefs.ts:17` | `Nhạc` | `Music` | ⚑ 4→5 ký tự, +25%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/app/prefs.ts:17` | `Tiếng trận và gõ` | `Combat and keys` | 16→15 ký tự (≤120%). |
| `src/app/sandbox.ts:13` | `<b>Hộp cát</b><kbd>F9</kbd>` | `<b>Sandbox</b><kbd>F9</kbd>` | 9→9 ký tự (≤120%). |
| `src/app/sandbox.ts:15` | `<div class="td-row td-wide"><small>Kho</small>` | `<div class="td-row td-wide"><small>Add</small>` | 3→3 ký tự (≤120%). |
| `src/app/sandbox.ts:16` | `<div class="td-row"><small>Tốc E</small>` | `<div class="td-row"><small>WPM</small>` | 5→3 ký tự (≤120%). |
| `src/app/sandbox.ts:17` | `Chế độ` | `Mode` | 6→4 ký tự (≤120%). |
| `src/app/sandbox.ts:17` | `Thư giãn` | `Relaxed` | 8→7 ký tự (≤120%). |
| `src/app/sandbox.ts:17` | `Cân bằng` | `Balanced` | 8→8 ký tự (≤120%). |
| `src/app/sandbox.ts:17` | `Thử thách` | `Challenge` | 9→9 ký tự (≤120%). |
| `src/app/sandbox.ts:17` | `Học` | `Learn` | ⚑ 3→5 ký tự, +67%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/app/sandbox.ts:18` | `Từ vựng` | `Words` | 7→5 ký tự (≤120%). |
| `src/app/sandbox.ts:18` | `Cấp 1` | `Lv. 1` | 5→5 ký tự (≤120%). |
| `src/app/sandbox.ts:19` | `Tốc game` | `Speed` | 8→5 ký tự (≤120%). |
| `src/app/sandbox.ts:20` | `Đặt sẵn` | `Preset` | 7→6 ký tự (≤120%). |
| `src/app/sandbox.ts:20` | `Sinh đêm` | `New night` | 8→9 ký tự (≤120%). |
| `src/app/sandbox.ts:20` | `Đầy Tối Thượng` | `Fill Ultimate` | 14→13 ký tự (≤120%). |
| `src/app/sandbox.ts:21` | `<div class="td-row"><small>Ngày</small>` | `<div class="td-row"><small>Day</small>` | 4→3 ký tự (≤120%). |
| `src/app/sandbox.ts:21` | ` title="Nhảy tới Ngày ` | ` title="Skip to Day ` | 20→18 ký tự (≤120%). |
| `src/app/sandbox.ts:21` | ` title="Gọi Mộc Tinh"` | ` title="Summon Mộc Tinh"` | 20→23 ký tự (≤120%). Giữ tên riêng theo NAMES_EN.md. |
| `src/app/sandbox.ts:22` | `<div class="td-row"><small>Gọi</small>` | `<div class="td-row"><small>Add</small>` | 3→3 ký tự (≤120%). |
| `src/app/sandbox.ts:22` | ` title="+1 Raccoon Dog, 8 Hopping Zombie sau 6 s (Ngắt)"` | ` title="+1 Raccoon Dog, 8 Hopping Zombies after 6 s (Stop)"` | 55→58 ký tự (≤120%). |
| `src/app/sandbox.ts:23` | `<div class="td-row"><small>Gọi</small>` | `<div class="td-row"><small>Add</small>` | 3→3 ký tự (≤120%). |
| `src/app/sandbox.ts:23` | ` title="+1 Zombie Leader và 5 Hopping Zombie (Neo)"` | ` title="+1 Zombie Leader and 5 Hopping Zombies (Pin)"` | 50→52 ký tự (≤120%). |
| `src/app/sandbox.ts:23` | ` title="+1 Troll (Phá Khiên)"` | ` title="+1 Troll (Shatter)"` | 28→26 ký tự (≤120%). |
| `src/app/sandbox.ts:24` | `<div class="td-row"><small>Nhịp</small><span>k ×` | `<div class="td-row"><small>Pace</small><span>k ×` | 7→7 ký tự (≤120%). |
| `src/app/sandbox.ts:24` | ` · tự điều ` | ` · adaptive ` | 9→10 ký tự (≤120%). |
| `src/app/sandbox.ts:24` | `Bật` | `On` | 3→2 ký tự (≤120%). |
| `src/app/sandbox.ts:24` | `Tắt` | `Off` | 3→3 ký tự (≤120%). |
| `src/content/slice-1a.ts:76` | `L` | `B` | 1→1 ký tự (≤120%). Nhãn view; không đổi id hay dữ liệu sim. |
| `src/content/slice-1a.ts:81` | `M` | `G` | 1→1 ký tự (≤120%). Nhãn view; không đổi id hay dữ liệu sim. |
| `src/content/slice-1a.ts:89` | `CT` | `HZ` | 2→2 ký tự (≤120%). Nhãn view; không đổi id hay dữ liệu sim. |
| `src/content/slice-1a.ts:94` | `MT` | `GF` | 2→2 ký tự (≤120%). Nhãn view; không đổi id hay dữ liệu sim. |
| `src/content/slice-1a.ts:99` | `TL` | `RS` | 2→2 ký tự (≤120%). Nhãn view; không đổi id hay dữ liệu sim. |
| `src/content/slice-1a.ts:110` | `MG` | `S` | 2→1 ký tự (≤120%). Nhãn view; không đổi id hay dữ liệu sim. |
| `src/content/slice-1a.ts:119` | `TN` | `RD` | 2→2 ký tự (≤120%). Nhãn view; không đổi id hay dữ liệu sim. |
| `src/content/slice-1a.ts:124` | `NP` | `SB` | 2→2 ký tự (≤120%). Nhãn view; không đổi id hay dữ liệu sim. |
| `src/content/slice-1a.ts:129` | `np` | `lb` | 2→2 ký tự (≤120%). Nhãn view; không đổi id hay dữ liệu sim. |
| `src/content/slice-1a.ts:137` | `ĐĐ` | `ZL` | 2→2 ký tự (≤120%). Nhãn view; không đổi id hay dữ liệu sim. |
| `src/ui/build-menu.ts:22` | `Mở ở Ngày ` | `Day ` | 9→3 ký tự (≤120%). |
| `src/ui/build-menu.ts:34` | `<p><small>Fort cao nhất ở bản đồ này</small></p>` | `<p><small>Fort at this map's max level</small></p>` | 26→28 ký tự (≤120%). |
| `src/ui/build-menu.ts:36` | `Nâng Fort · ` | `Boost Fort · ` | 11→12 ký tự (≤120%). |
| `src/ui/build-menu.ts:36` | `Nâng Fort · ` | `Boost Fort · ` | 11→12 ký tự (≤120%). |
| `src/ui/build-menu.ts:37` | `<p><small>Mở: ` | `<p><small>New ` | 3→3 ký tự (≤120%). |
| `src/ui/build-menu.ts:44` | `Trống` | `Empty` | 5→5 ký tự (≤120%). |
| `src/ui/build-menu.ts:44` | `Lớn` | `Grow` | ⚑ 3→4 ký tự, +33%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/ui/build-menu.ts:44` | `Chín` | `Ripe` | 4→4 ký tự (≤120%). |
| `src/ui/build-menu.ts:52` | `<p>Đang xây ` | `<p>Building ` | 8→8 ký tự (≤120%). |
| `src/ui/build-menu.ts:52` | ` · chờ Builder` | ` · need Builder` | 13→14 ký tự (≤120%). |
| `src/ui/build-menu.ts:55` | `Bấm lần nữa: bán` | `Tap again: sell` | 16→15 ký tự (≤120%). |
| `src/ui/build-menu.ts:55` | `Bán · +` | `Sell · +` | 7→8 ký tự (≤120%). |
| `src/ui/build-menu.ts:57` | `</b> · tự mua ` | `</b> · auto-buy ` | ⚑ 8→10 ký tự, +25%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/ui/build-menu.ts:58` | `Mua ` | `Buy ` | 3→3 ký tự (≤120%). |
| `src/ui/build-menu.ts:58` | `Tự mua Seeds` | `Auto Seeds` | 12→10 ký tự (≤120%). |
| `src/ui/build-menu.ts:60` | `Thuê Villager · ` | `Hire Villager · ` | 15→15 ký tự (≤120%). |
| `src/ui/build-menu.ts:60` | `Bán ` | `Sell ` | ⚑ 3→4 ký tự, +33%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/ui/build-menu.ts:60` | `Bán ` | `Sell ` | ⚑ 3→4 ký tự, +33%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/ui/build-menu.ts:61` | `<p>Lượt mạnh <b>` | `<p>Charges <b>` | 9→7 ký tự (≤120%). |
| `src/ui/build-menu.ts:61` | `</b> · ban đêm gõ lời gọi Bắn mạnh để nạp</p>` | `</b> · type Power calls at night to charge</p>` | 36→37 ký tự (≤120%). |
| `src/ui/build-menu.ts:64` | `Cấp ` | `Lv. ` | 3→3 ký tự (≤120%). |
| `src/ui/build-menu.ts:64` | ` · nền chắc` | ` · sturdy` | 10→8 ký tự (≤120%). |
| `src/ui/build-menu.ts:66` | `Gửi ` | `Send ` | ⚑ 3→4 ký tự, +33%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/ui/build-menu.ts:67` | `Hoàn tác · ` | `Undo · ` | 10→6 ký tự (≤120%). |
| `src/ui/build-menu.ts:69` | `Nâng cấp · ` | `Upgrade · ` | 10→9 ký tự (≤120%). |
| `src/ui/build-menu.ts:69` | `Nâng cấp · ` | `Upgrade · ` | 10→9 ký tự (≤120%). |
| `src/ui/build-menu.ts:70` | `Cấp` | `Lv.` | 3→3 ký tự (≤120%). |
| `src/ui/build-menu.ts:80` | `Trong vòng giúp: sáng khi bớt lời gọi đang sáng.` | `In range: lights up when a call slot is free.` | 48→45 ký tự (≤120%). |
| `src/ui/build-menu.ts:80` | `Ngoài vòng giúp: đưa người tới gần để thẻ sáng và gõ được.` | `Out of range: send someone near to light this card and type.` | 58→60 ký tự (≤120%). |
| `src/ui/build-menu.ts:82` | ` từ · đang mờ` | ` words · dim` | 12→11 ký tự (≤120%). |
| `src/ui/build-menu.ts:83` | `Gửi ` | `Send ` | ⚑ 3→4 ký tự, +33%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/ui/build-menu.ts:96` | `Chỉ đặt trên quặng` | `Ore sites only` | 18→14 ký tự (≤120%). |
| `src/ui/build-menu.ts:97` | `Xây nhà` | `Build` | 7→5 ký tự (≤120%). |
| `src/ui/build-menu.ts:97` | `<p><small>Tab: chỗ kế · Enter: xây · Esc: hủy</small></p>` | `<p><small>Tab next · Enter build · Esc cancel</small></p>` | 35→35 ký tự (≤120%). |
| `src/ui/hud.ts:20` | `Tên ta ở đâu?` | `What's my name?` | 13→15 ký tự (≤120%). |
| `src/ui/hud.ts:20` | `Rễ ơi, mọc lên!` | `Roots, rise!` | 15→12 ký tự (≤120%). |
| `src/ui/hud.ts:20` | `Sinh khí làng này... ngọt quá.` | `This village's life... so sweet.` | 30→32 ký tự (≤120%). |
| `src/ui/hud.ts:20` | `Cái tên đó... quen quá...` | `That name... I know it...` | 25→25 ký tự (≤120%). |
| `src/ui/hud.ts:20` | `À... ta nhớ rồi.` | `Ah... I remember.` | 16→17 ký tự (≤120%). |
| `src/ui/hud.ts:26` | `Ván đã kết thúc` | `Run ended` | 15→9 ký tự (≤120%). |
| `src/ui/hud.ts:26` | `Đã đủ 16 nhà` | `16 at cap` | 12→9 ký tự (≤120%). |
| `src/ui/hud.ts:26` | `Đã đủ nhà loại này` | `Building type at cap` | 18→20 ký tự (≤120%). |
| `src/ui/hud.ts:26` | `Ngoài sân` | `Off map` | 9→7 ký tự (≤120%). |
| `src/ui/hud.ts:26` | `Gold Mine chỉ đặt trên quặng trống` | `Gold Mine needs a free ore site` | 34→31 ký tự (≤120%). |
| `src/ui/hud.ts:27` | `Không xây trên nước` | `Cannot build on water` | 19→21 ký tự (≤120%). |
| `src/ui/hud.ts:27` | `Sát đường quá` | `Near road` | 13→9 ký tự (≤120%). |
| `src/ui/hud.ts:27` | `Trong vòng 11 m quanh Fort` | `Within 11 m of Fort` | 26→19 ký tự (≤120%). |
| `src/ui/hud.ts:27` | `Chạm nhà khác` | `Overlaps` | 13→8 ký tự (≤120%). |
| `src/ui/hud.ts:27` | `Vướng cây` | `Tree here` | 9→9 ký tự (≤120%). |
| `src/ui/hud.ts:27` | `Barracks phải gần đường` | `Barracks needs a road` | 23→21 ký tự (≤120%). |
| `src/ui/hud.ts:28` | `Chặn lối đi` | `Path blocked` | 11→12 ký tự (≤120%). |
| `src/ui/hud.ts:28` | `Thiếu Gold` | `Need Gold` | 10→9 ký tự (≤120%). |
| `src/ui/hud.ts:28` | `Thiếu Wood` | `Need Wood` | 10→9 ký tự (≤120%). |
| `src/ui/hud.ts:28` | `Thiếu Rice` | `Need Rice` | 10→9 ký tự (≤120%). |
| `src/ui/hud.ts:28` | `Ô này còn khóa` | `Slot locked` | 14→11 ký tự (≤120%). |
| `src/ui/hud.ts:28` | `Chỉ gọi đêm được ban ngày` | `Call night during the day` | 25→25 ký tự (≤120%). |
| `src/ui/hud.ts:29` | `Hết 5 s hoàn tác` | `Undo expired (5 s)` | 16→18 ký tự (≤120%). |
| `src/ui/hud.ts:29` | `Xây xong rồi, không hoàn tác` | `Already built; cannot undo` | 28→26 ký tự (≤120%). |
| `src/ui/hud.ts:29` | `Không đứng được ở đó` | `Cannot stand there` | 20→18 ký tự (≤120%). |
| `src/ui/hud.ts:29` | `Xa Barracks quá` | `Barracks too far` | 15→16 ký tự (≤120%). |
| `src/ui/hud.ts:29` | `Điểm tập kết phải ở đường` | `Rally point needs a road` | 25→24 ký tự (≤120%). |
| `src/ui/hud.ts:30` | `Không có nhà đó` | `Building missing` | 15→16 ký tự (≤120%). |
| `src/ui/hud.ts:30` | `Không phải Barracks` | `Requires Barracks` | 19→17 ký tự (≤120%). |
| `src/ui/hud.ts:30` | `Giá trị không hợp lệ` | `Invalid value` | 20→13 ký tự (≤120%). |
| `src/ui/hud.ts:30` | `Chỉ có trong hộp cát` | `Sandbox only` | 20→12 ký tự (≤120%). |
| `src/ui/hud.ts:30` | `Phím không hợp lệ` | `Invalid key` | 17→11 ký tự (≤120%). |
| `src/ui/hud.ts:31` | `Không nâng cấp được` | `Cannot upgrade` | 19→14 ký tự (≤120%). |
| `src/ui/hud.ts:31` | `Nhà chưa xây xong` | `Still building` | 17→14 ký tự (≤120%). |
| `src/ui/hud.ts:31` | `Không có cây đó` | `Tree missing` | 15→12 ký tự (≤120%). |
| `src/ui/hud.ts:31` | `Đủ Villager rồi` | `Villager limit` | 15→14 ký tự (≤120%). |
| `src/ui/hud.ts:31` | `Ô này chưa chín` | `Plot unripe` | 15→11 ký tự (≤120%). |
| `src/ui/hud.ts:32` | `Chưa mở tới ngày này` | `Not unlocked yet` | 20→16 ký tự (≤120%). |
| `src/ui/hud.ts:32` | `Fort đã cao nhất ở bản đồ này` | `Fort at this map's max level` | 29→28 ký tự (≤120%). |
| `src/ui/hud.ts:32` | `Mộc Tinh đã thức` | `Mộc Tinh is awake` | 16→17 ký tự (≤120%). Giữ tên riêng theo NAMES_EN.md. |
| `src/ui/hud.ts:33` | `Tối Thượng chưa đầy` | `Ultimate not ready` | 19→18 ký tự (≤120%). |
| `src/ui/hud.ts:33` | `Fire Feather Rain đang rơi` | `Fire Feather Rain is active` | 26→27 ký tự (≤120%). |
| `src/ui/hud.ts:33` | `Xa Draconis quá (20 m)` | `Beyond Draconis (20 m)` | 22→22 ký tự (≤120%). |
| `src/ui/hud.ts:33` | `Chưa có quái gần Draconis (14 m)` | `No foes near Draconis (14 m)` | 32→28 ký tự (≤120%). |
| `src/ui/hud.ts:52` | `Ngày ` | `Day ` | 4→3 ký tự (≤120%). |
| `src/ui/hud.ts:52` | `Đêm ` | `Night ` | ⚑ 3→5 ký tự, +67%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/ui/hud.ts:52` | ` · còn ` | ` · ` | 5→1 ký tự (≤120%). |
| `src/ui/hud.ts:52` | ` quái` | ` foes left` | ⚑ 4→9 ký tự, +125%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/ui/hud.ts:52` | `Bình minh ` | `Dawn ` | 9→4 ký tự (≤120%). |
| `src/ui/hud.ts:52` | `Giữ được làng` | `Village saved` | 13→13 ký tự (≤120%). |
| `src/ui/hud.ts:52` | `Thua` | `Defeat` | ⚑ 4→6 ký tự, +50%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/ui/hud.ts:55` | `<div class="td-row"><span class="td-title"><b>Lời Gọi</b><small>` | `<div class="td-row"><span class="td-title"><b>Wordwoven</b><small>` | ⚑ 7→9 ký tự, +29%; còn vượt 20%, Claude duyệt/rút tiếp. Tên game bắt buộc. |
| `src/ui/hud.ts:55` | `Hộp cát · bản thử 1B` | `Sandbox · 1B demo` | 20→17 ký tự (≤120%). |
| `src/ui/hud.ts:55` | `Bản đồ 1 · Đồng Cỏ Thác Bạc` | `Map 1 · Silverfall Meadow` | 27→25 ký tự (≤120%). |
| `src/ui/hud.ts:56` | ` class="td-x" title="Tạm dừng (Pause)"` | ` class="td-x" title="Pause"` | 37→26 ký tự (≤120%). |
| `src/ui/hud.ts:56` | `<s>Âm</s>` | `<s>Sound</s>` | ⚑ 2→5 ký tự, +150%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/ui/hud.ts:56` | `Âm` | `Sound` | ⚑ 2→5 ký tự, +150%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/ui/hud.ts:56` | ` class="td-x" title="Hộp cát"` | ` class="td-x" title="Sandbox"` | 28→28 ký tự (≤120%). |
| `src/ui/hud.ts:57` | `Mạng` | `Lives` | ⚑ 4→5 ký tự, +25%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/ui/hud.ts:59` | `</b> · Sổ ôn <b>` | `</b> · Review <b>` | 7→8 ký tự (≤120%). |
| `src/ui/hud.ts:60` | `<p class="td-warn">Fort đã mất hết mạng</p>` | `<p class="td-warn">Fort has no lives left</p>` | 20→22 ký tự (≤120%). |
| `src/ui/hud.ts:70` | `<b>Gọi đêm sớm · +` | `<b>Early night · +` | 15→15 ký tự (≤120%). |
| `src/ui/hud.ts:70` | `Đã dừng` | `Paused` | 7→6 ký tự (≤120%). |
| `src/ui/hud.ts:87` | `<em>Gõ chữ đầu của một thẻ để khóa từ</em>` | `<em>Type a card's first letter to lock on</em>` | 33→37 ký tự (≤120%). |
| `src/ui/hud.ts:88` | `<em class="td-warn td-halt">Tạm dừng · Space</em>` | `<em class="td-warn td-halt">Paused · Space</em>` | 16→14 ký tự (≤120%). |
| `src/ui/hud.ts:93` | `<span class="td-chain" title="Bậc Chuỗi ` | `<span class="td-chain" title="Chain tier ` | 39→40 ký tự (≤120%). |
| `src/ui/hud.ts:93` | `">Chuỗi <b>` | `">Chain <b>` | 7→7 ký tự (≤120%). |
| `src/ui/hud.ts:100` | `Tối Thượng · Mở ở Đêm ` | `Ultimate · Night ` | 21→16 ký tự (≤120%). |
| `src/ui/hud.ts:100` | `Tối Thượng` | `Ultimate` | 10→8 ký tự (≤120%). |
| `src/ui/hud.ts:100` | `Tối Thượng ` | `Ultimate ` | 10→8 ký tự (≤120%). |
| `src/ui/hud.ts:101` | `Xây` | `Build` | ⚑ 3→5 ký tự, +67%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/ui/hud.ts:101` | `Thuê Villager` | `Hire Villager` | 13→13 ký tự (≤120%). |
| `src/ui/hud.ts:102` | `Chạy tiếp` | `Resume` | 9→6 ký tự (≤120%). |
| `src/ui/hud.ts:102` | `Tạm dừng` | `Pause` | 8→5 ký tự (≤120%). |
| `src/ui/hud.ts:158` | `Rễ hút ` | `Roots drain ` | ⚑ 6→11 ký tự, +83%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/ui/hud.ts:158` | ` mạng mỗi ` | ` life every ` | ⚑ 8→10 ký tự, +25%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/ui/hud.ts:158` | ` s: hạ nó nhanh!` | ` s: defeat him fast!` | ⚑ 15→19 ký tự, +27%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/ui/hud.ts:161` | `Mộc Tinh choáng! Gõ Bắn mạnh!` | `Mộc Tinh stunned! Type Power!` | 29→29 ký tự (≤120%). Giữ tên riêng theo NAMES_EN.md. |
| `src/ui/hud.ts:191` | `<div class="td-tip-chip"><small>Mẹo</small> <b>` | `<div class="td-tip-chip"><small>Tip</small> <b>` | 3→3 ký tự (≤120%). |
| `src/ui/hud.ts:199` | ` · Mẹo: ` | ` · Tip: ` | 6→6 ký tự (≤120%). |
| `src/ui/hud.ts:203` | `<b>Mộc Tinh</b> <small>đang ngủ` | `<b>Mộc Tinh</b> <small>asleep` | 17→15 ký tự (≤120%). Giữ tên riêng theo NAMES_EN.md. |
| `src/ui/hud.ts:203` | `<b>Đêm ` | `<b>Night ` | ⚑ 3→5 ký tự, +67%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/ui/hud.ts:203` | ` · Boss</b> <small>Mộc Tinh thức dậy` | ` · Boss</b> <small>Mộc Tinh awakens` | 24→23 ký tự (≤120%). Giữ tên riêng theo NAMES_EN.md. |
| `src/ui/hud.ts:204` | `<b>Mộc Tinh tới sau ` | `<b>Mộc Tinh in ` | 16→11 ký tự (≤120%). Giữ tên riêng theo NAMES_EN.md. |
| `src/ui/hud.ts:204` | ` · chờ quái gần Fort` | ` · waiting: foes near Fort` | ⚑ 19→25 ký tự, +32%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/ui/hud.ts:205` | `<b>Mộc Tinh đang trồi lên</b>` | `<b>Mộc Tinh is rising</b>` | 22→18 ký tự (≤120%). Giữ tên riêng theo NAMES_EN.md. |
| `src/ui/hud.ts:206` | `<b>Mộc Tinh rút lui</b> <small>+` | `<b>Mộc Tinh retreats</b> <small>+` | 18→19 ký tự (≤120%). Giữ tên riêng theo NAMES_EN.md. |
| `src/ui/hud.ts:210` | `rút lui` | `retreat` | 7→7 ký tự (≤120%). |
| `src/ui/hud.ts:210` | `choáng · Dễ Tổn Thương ` | `stunned · Vulnerable ` | 22→20 ký tự (≤120%). |
| `src/ui/hud.ts:210` | `pha ` | `phase ` | ⚑ 3→5 ký tự, +67%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/ui/hud.ts:213` | ` · còn ` | ` · ` | 5→1 ký tự (≤120%). |
| `src/ui/hud.ts:213` | ` m tới Fort</small></div>` | ` m to Fort</small></div>` | 10→9 ký tự (≤120%). |
| `src/ui/hud.ts:215` | `%"><small>rút lui</small></s></div>` | `%"><small>retreat</small></s></div>` | 10→10 ký tự (≤120%). |
| `src/ui/profile.ts:10` | `Tay bạn đang chậm dần: nghỉ vài phút rồi chơi tiếp nhé.` | `Your hands are slowing down. Take a short break.` | Lời khuyên cũ lấy từ src/kit/balance/pace.ts:110; bảng EN tại UI, không sửa kit. 55→48 ký tự (≤120%). |
| `src/ui/profile.ts:11` | `Bạn gõ nhanh nhưng hay sai: chậm lại một nhịp sẽ được Hoàn hảo nhiều hơn.` | `Ease your pace for fewer errors and more Perfect calls.` | Lời khuyên cũ lấy từ src/kit/balance/pace.ts:111; bảng EN tại UI, không sửa kit. 73→55 ký tự (≤120%). |
| `src/ui/profile.ts:12` | `Gõ chắc từng chữ trước, tốc độ sẽ tự lên.` | `Focus on each letter. Speed will follow.` | Lời khuyên cũ lấy từ src/kit/balance/pace.ts:112; bảng EN tại UI, không sửa kit. 41→40 ký tự (≤120%). |
| `src/ui/profile.ts:13` | `Nhịp gõ chưa đều: giữ một tốc độ vừa phải cho mọi từ.` | `Keep an even pace across every word.` | Lời khuyên cũ lấy từ src/kit/balance/pace.ts:113; bảng EN tại UI, không sửa kit. 53→36 ký tự (≤120%). |
| `src/ui/profile.ts:14` | `Từ mới còn lạ: đọc nghĩa và nghe phát âm trước khi gõ.` | `Read meanings and listen before typing unfamiliar words.` | Lời khuyên cũ lấy từ src/kit/balance/pace.ts:114; bảng EN tại UI, không sửa kit. 54→56 ký tự (≤120%). |
| `src/ui/profile.ts:15` | `Khi đông quái, chọn một từ và gõ dứt điểm rồi mới sang từ khác.` | `When foes crowd in, finish one word before picking another.` | Lời khuyên cũ lấy từ src/kit/balance/pace.ts:115; bảng EN tại UI, không sửa kit. 63→59 ký tự (≤120%). |
| `src/ui/profile.ts:16` | `Bạn đang tiến bộ đều. Giữ phong độ!` | `You're improving steadily. Keep it up!` | Lời khuyên cũ lấy từ src/kit/balance/pace.ts:116; bảng EN tại UI, không sửa kit. 35→38 ký tự (≤120%). |
| `src/ui/profile.ts:41` | `<h3>Hồ sơ gõ</h3><dl>` | `<h3>Profile</h3><dl>` | 8→7 ký tự (≤120%). |
| `src/ui/profile.ts:42` | `Tốc độ` | `Speed` | 6→5 ký tự (≤120%). |
| `src/ui/profile.ts:43` | `Độ chính xác` | `Accuracy` | 12→8 ký tự (≤120%). |
| `src/ui/profile.ts:44` | `Nhận từ mới` | `New words` | 11→9 ký tự (≤120%). |
| `src/ui/profile.ts:45` | `Độ đều` | `Rhythm` | 6→6 ký tự (≤120%). |
| `src/ui/profile.ts:46` | `Nhịp ván tới` | `Next pace` | 12→9 ký tự (≤120%). |
| `src/ui/profile.ts:46` | `Tắt` | `Off` | 3→3 ký tự (≤120%). |
| `src/ui/profile.ts:46` | `tự điều đang tắt` | `adaptive off` | 16→12 ký tự (≤120%). |
| `src/ui/profile.ts:46` | `nhanh hơn chuẩn` | `above normal` | 15→12 ký tự (≤120%). |
| `src/ui/profile.ts:46` | `chậm hơn chuẩn` | `below normal` | 14→12 ký tự (≤120%). |
| `src/ui/profile.ts:46` | `chuẩn` | `normal` | 5→6 ký tự (≤120%). |
| `src/ui/profile.ts:47` | `Chơi một ngày đêm để game hiểu cách bạn gõ.` | `Play a day and night to measure your typing.` | 43→44 ký tự (≤120%). |
| `src/ui/profile.ts:48` | `Đã đo ` | `From ` | 5→4 ký tự (≤120%). |
| `src/ui/profile.ts:48` | ` ngày đêm.` | ` days/nights.` | ⚑ 9→12 ký tự, +33%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/ui/profile.ts:48` | `Chưa đo: số trên là mức mặc định, sẽ đúng dần sau mỗi ngày đêm.` | `No data yet: these are defaults, refined after each day and night.` | 63→66 ký tự (≤120%). |
| `src/ui/profile.ts:48` | `Đã đo ` | `From ` | 5→4 ký tự (≤120%). |
| `src/ui/profile.ts:48` | ` ngày đêm: còn trộn với mức mặc định.` | ` days/nights: blended with defaults.` | 36→35 ký tự (≤120%). |
| `src/ui/profile.ts:49` | `<button class="vd-seal" type="button">Xong <kbd>Esc</kbd></button>` | `<button class="vd-seal" type="button">Done <kbd>Esc</kbd></button>` | 8→8 ký tự (≤120%). |
| `src/ui/settings.ts:11` | `Nhịp tự điều theo cách bạn gõ` | `Pace adapts to your typing` | 29→26 ký tự (≤120%). |
| `src/ui/settings.ts:15` | `Thư giãn` | `Relaxed` | 8→7 ký tự (≤120%). |
| `src/ui/settings.ts:15` | `Cân bằng` | `Balanced` | 8→8 ký tự (≤120%). |
| `src/ui/settings.ts:15` | `Thử thách` | `Challenge` | 9→9 ký tự (≤120%). |
| `src/ui/settings.ts:15` | `Học` | `Learn` | ⚑ 3→5 ký tự, +67%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/ui/settings.ts:17` | `Theo hồ sơ` | `By profile` | 10→10 ký tự (≤120%). |
| `src/ui/settings.ts:96` | `<small>Áp dụng khi bắt đầu ván</small></span>` | `<small>Applies to new runs</small></span>` | 23→19 ký tự (≤120%). |
| `src/ui/settings.ts:97` | `Bật` | `On` | 3→2 ký tự (≤120%). |
| `src/ui/settings.ts:97` | `Tắt` | `Off` | 3→3 ký tự (≤120%). |
| `src/ui/settings.ts:98` | `" data-key="mode"><span>Chế độ (truyện)<small>Áp dụng khi bắt đầu ván</small></span>` | `" data-key="mode"><span>Story mode<small>Applies to new runs</small></span>` | 56→47 ký tự (≤120%). |
| `src/ui/settings.ts:100` | `<p class="td-set-hint">↑ ↓ chọn · ← → chỉnh · Enter xong</p><button class="vd-seal" type="button">Xong <kbd>Esc</kbd></button>` | `<p class="td-set-hint">↑ ↓ select · ← → adjust · Enter done</p><button class="vd-seal" type="button">Done <kbd>Esc</kbd></button>` | 41→44 ký tự (≤120%). |
| `src/ui/sheets.ts:25` | `Chơi tiếp` | `Resume` | 9→6 ký tự (≤120%). |
| `src/ui/sheets.ts:25` | `Cài đặt` | `Settings` | 7→8 ký tự (≤120%). |
| `src/ui/sheets.ts:25` | `Về màn đầu` | `Title` | 10→5 ký tự (≤120%). |
| `src/ui/sheets.ts:29` | `<p class="td-best">Kỷ lục` | `<p class="td-best">Best` | 6→4 ký tự (≤120%). |
| `src/ui/sheets.ts:29` | ` mới` | ` new` | 3→3 ký tự (≤120%). |
| `src/ui/sheets.ts:42` | `Xây Archer Tower cạnh đường: Fort một mình không giữ nổi.` | `Build Archer Towers by roads: Fort needs help.` | 57→46 ký tự (≤120%). |
| `src/ui/sheets.ts:42` | `Gõ chữ trên thẻ tháp (Bắn mạnh) khi quái tới gần.` | `Type tower card words (Power) as foes approach.` | 49→47 ký tự (≤120%). |
| `src/ui/sheets.ts:42` | `Gõ Bắn mạnh khi quái tới gần tháp` | `Type Power as foes approach towers` | 33→34 ký tự (≤120%). |
| `src/ui/sheets.ts:42` | `; xây thêm tháp cạnh đường.` | `; add towers by roads.` | 27→22 ký tự (≤120%). |
| `src/ui/sheets.ts:42` | `; Word Shot của Cannon Tower cạnh Draconis làm quái cháy.` | `; Cannon Tower's Word Shot near Draconis burns foes.` | 57→52 ký tự (≤120%). |
| `src/ui/sheets.ts:43` | `Quái lọt vào Fort lúc Mộc Tinh tới: gõ Bắn mạnh ở tháp gần Fort.` | `Foes reached Fort as Mộc Tinh arrived: type Power at nearby towers.` | 64→67 ký tự (≤120%). Giữ tên riêng theo NAMES_EN.md. |
| `src/ui/sheets.ts:44` | `Thêm tháp trên nhánh rễ sáng.` | `Add towers along the glowing root.` | 29→34 ký tự (≤120%). |
| `src/ui/sheets.ts:45` | `Lúc nó choáng, gõ Bắn mạnh ngay.` | `When he's stunned, type Power at once.` | 32→38 ký tự (≤120%). |
| `src/ui/sheets.ts:46` | `Đặt Archer Tower xa đường hơn: rễ không với tới.` | `Move Archer Towers off-road, out of root range.` | 48→47 ký tự (≤120%). |
| `src/ui/sheets.ts:47` | `Dồn tháp và Draconis lên nhánh rễ sáng, gõ Bắn mạnh khi nó tới gần.` | `Group towers and Draconis on the glowing root; type Power as he nears.` | 67→70 ký tự (≤120%). |
| `src/ui/sheets.ts:81` | `Chơi lại Ngày ` | `Retry Day ` | 13→9 ký tự (≤120%). |
| `src/ui/sheets.ts:82` | `Chơi lại từ đầu` | `Restart` | 15→7 ký tự (≤120%). |
| `src/ui/sheets.ts:82` | `Chơi lại` | `Retry` | 8→5 ký tự (≤120%). |
| `src/ui/sheets.ts:82` | `Chép số chơi thử` | `Save playtest` | 16→13 ký tự (≤120%). |
| `src/ui/sheets.ts:82` | `Xem bản đồ` | `View map` | 10→8 ký tự (≤120%). |
| `src/ui/sheets.ts:82` | `Về màn đầu` | `Title` | 10→5 ký tự (≤120%). |
| `src/ui/sheets.ts:93` | `<h2>Tạm dừng</h2><p>Làng đứng yên chờ bạn. Chữ trên thẻ vẫn ở đó.</p>` | `<h2>Paused</h2><p>Your village waits. Card words stay in place.</p>` | 53→51 ký tự (≤120%). |
| `src/ui/sheets.ts:94` | `<h2>Giữ được làng</h2><div class="td-stars">` | `<h2>Village saved</h2><div class="td-stars">` | 13→13 ký tự (≤120%). |
| `src/ui/sheets.ts:94` | `<p>Mộc Tinh đã nhớ ra tên mình và lui về rừng.` | `<p>Mộc Tinh remembers his name and leaves.` | 43→39 ký tự (≤120%). Giữ tên riêng theo NAMES_EN.md. |
| `src/ui/sheets.ts:94` | ` (chơi lại Ngày ` | ` (retry Day ` | 14→10 ký tự (≤120%). |
| `src/ui/sheets.ts:95` | `<h2>Fort đã vỡ</h2><p class="td-hint-line">` | `<h2>Fort fallen</h2><p class="td-hint-line">` | 10→11 ký tự (≤120%). |
| `src/ui/sheets.ts:96` | `Mạng còn` | `Lives` | 8→5 ký tự (≤120%). |
| `src/ui/sheets.ts:96` | `Đêm đã giữ` | `Nights held` | 10→11 ký tự (≤120%). |
| `src/ui/sheets.ts:96` | `Quái đã hạ` | `Foes slain` | 10→10 ký tự (≤120%). |
| `src/ui/sheets.ts:96` | `Từ đã gõ` | `Words` | 8→5 ký tự (≤120%). |
| `src/ui/sheets.ts:96` | `Lời gọi Hoàn hảo` | `Perfect calls` | 16→13 ký tự (≤120%). |
| `src/ui/sheets.ts:97` | `<div class="td-review"><small>Từ cần ôn</small><ul>` | `<div class="td-review"><small>To review</small><ul>` | 9→9 ký tự (≤120%). |
| `src/ui/td.css:168` | `Ôn` | `R` | 2→1 ký tự (≤120%). |
| `src/ui/team-bar.ts:20` | `<button class="td-agent is-locked" disabled title="Mở ở Fort cấp ` | `<button class="td-agent is-locked" disabled title="Fort level ` | 64→61 ký tự (≤120%). |
| `src/ui/team-bar.ts:25` | `%" title="Tối Thượng ` | `%" title="Ultimate ` | 20→18 ký tự (≤120%). |
| `src/ui/team-bar.ts:29` | `</b></span><span class="td-load" title="Lời gọi đang sáng / tối đa">Đang gọi ` | `</b></span><span class="td-load" title="Lit calls / limit">Calling ` | 8→7 ký tự (≤120%). |
| `src/ui/tips.ts:16` | `Rice chín, bác Farmer gọi. Đưa Draconis tới, gõ chữ trên bong bóng.` | `Rice is ripe: Farmer calls. Send Draconis; type the bubble's words.` | 67→67 ký tự (≤120%). |
| `src/ui/tips.ts:16` | `Gõ chữ đầu để chọn · Esc để thôi` | `First letter selects · Esc exits` | 32→32 ký tự (≤120%). |
| `src/ui/tips.ts:17` | `Đêm xuống, tháp gọi khi quái tới gần. Gõ là bắn Word Shot.` | `At night, towers call for help. Type to fire a Word Shot.` | 58→57 ký tự (≤120%). |
| `src/ui/tips.ts:17` | `Bỏ qua lời gọi không mất gì` | `Skipped calls cost nothing` | 27→26 ký tự (≤120%). |
| `src/ui/tips.ts:18` | `Wood để xây nhà; cây mọc lại mỗi sáng. Bấm cây để chặt.` | `Build with Wood; trees regrow each dawn. Click a tree to chop.` | 55→62 ký tự (≤120%). |
| `src/ui/tips.ts:18` | `Shift + \ thuê Villager` | `Shift + \ hires Villager` | 23→24 ký tự (≤120%). |
| `src/ui/tips.ts:19` | `Ghost Flame bay qua đầu Soldier. Archer Tower và Draconis bắn được.` | `Ghost Flame flies over Soldiers. Archer Tower and Draconis can hit it.` | 67→70 ký tự (≤120%). |
| `src/ui/tips.ts:20` | `Nâng Fort thì Chấm ra giúp. Helper làm việc nhanh hơn.` | `Upgrade Fort to free Chấm. Helpers speed up work.` | 54→49 ký tự (≤120%). Giữ tên riêng theo NAMES_EN.md. |
| `src/ui/tips.ts:20` | `1–4 chọn người · Enter gửi đi` | `1–4 select · Enter send` | 29→23 ký tự (≤120%). |
| `src/ui/tips.ts:21` | `Lông lửa đầy thì bấm = khi quái tới gần. Gõ chữ, mưa to hơn.` | `Charge full: press = near foes. Type for more fire feathers.` | 60→60 ký tự (≤120%). |
| `src/ui/tips.ts:21` | `= Tối Thượng khi quái gần` | `= Ultimate near foes` | 25→20 ký tự (≤120%). |
| `src/ui/tips.ts:22` | `Nhà cấp 2 mạnh hơn. Bán lại được sáu phần mười.` | `Level 2 buildings are stronger. Sell for a 60% refund.` | 47→54 ký tự (≤120%). |
| `src/ui/tips.ts:22` | `Bán: bấm hai lần` | `Sell: click twice` | 16→17 ký tự (≤120%). |
| `src/ui/tips.ts:23` | `Raccoon Dog đánh trống hồi máu. Gõ chữ trên đầu nó để Ngắt.` | `Raccoon Dog drums to heal. Type its word to Stop it.` | 59→52 ký tự (≤120%). |
| `src/ui/tips.ts:23` | `Chữ trên quái: gõ để phá chiêu` | `Type foe words to break skills` | 30→30 ký tự (≤120%). |
| `src/ui/tips.ts:24` | `Đêm nay Mộc Tinh thức dậy. Dồn tháp lên nhánh rễ sáng.` | `Tonight Mộc Tinh awakens. Line the glowing root with towers.` | 54→60 ký tự (≤120%). Giữ tên riêng theo NAMES_EN.md. |
| `src/ui/tips.ts:24` | `Boss rút ở 50 % máu` | `Boss flees at 50% HP` | 19→20 ký tự (≤120%). |
| `src/ui/tips.ts:25` | `Rễ trồi làm nhà tê. Lửa của chữ mới làm nó cháy.` | `Rising roots stun buildings. Fresh words set him ablaze.` | 48→56 ký tự (≤120%). |
| `src/ui/tips.ts:25` | `Choáng: gõ Bắn mạnh ngay` | `Stunned: type Power now` | 24→23 ký tự (≤120%). |
| `src/ui/tips.ts:30` | `(Ruộng) Gieo Seeds; Rice chín thì gọi Gặt.` | `(Rice Field) Sow Seeds; ripe Rice calls for Reap.` | 42→49 ký tự (≤120%). |
| `src/ui/tips.ts:31` | `(Tháp Cung) Bắn quái gần, cả quái bay.` | `(Archer Tower) Hits nearby foes, even flyers.` | 38→45 ký tự (≤120%). |
| `src/ui/tips.ts:32` | `(Trại Lính) Soldier chặn quái trên đường cho tháp bắn.` | `(Barracks) Soldiers block foes on roads for towers to shoot.` | 54→60 ký tự (≤120%). |
| `src/ui/tips.ts:33` | `(Mỏ Vàng) Đặt trên quặng; Gold đầy nửa thì gọi Đào.` | `(Gold Mine) Needs ore; half-full Gold calls for Dig.` | 51→52 ký tự (≤120%). |
| `src/ui/tips.ts:34` | `(Tháp Pháo) Đạn nổ trúng cả bầy dưới đất.` | `(Cannon Tower) Blasts hit groups of ground foes.` | 41→48 ký tự (≤120%). |
| `src/ui/title.ts:21` | `Bắt đầu` | `Start` | 7→5 ký tự (≤120%). |
| `src/ui/title.ts:21` | `Bản đồ 1 · Đồng Cỏ Thác Bạc` | `Map 1 · Silverfall Meadow` | 27→25 ký tự (≤120%). |
| `src/ui/title.ts:22` | `Chơi tiếp` | `Resume` | 9→6 ký tự (≤120%). |
| `src/ui/title.ts:22` | `Về lại ván đang dở · Esc` | `Resume your run · Esc` | 24→21 ký tự (≤120%). |
| `src/ui/title.ts:23` | `Cài đặt` | `Settings` | 7→8 ký tự (≤120%). |
| `src/ui/title.ts:23` | `Âm lượng nhạc và tiếng` | `Music and sound volume` | 22→22 ký tự (≤120%). |
| `src/ui/title.ts:24` | `Học` | `Learn` | ⚑ 3→5 ký tự, +67%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/ui/title.ts:24` | `Chế độ Học: hiện nghĩa, Space để dừng` | `Learn: meanings shown, Space pauses` | 37→35 ký tự (≤120%). |
| `src/ui/title.ts:25` | `Hồ sơ gõ` | `Profile` | 8→7 ký tự (≤120%). Đã rút gọn thành Profile. |
| `src/ui/title.ts:25` | `Tốc độ, độ chính xác, một lời khuyên` | `Speed, accuracy, a typing tip` | 36→29 ký tự (≤120%). Đã rút gọn thành Profile. |
| `src/ui/title.ts:29` | ` · <span class="tt-stars" aria-label="Kỷ lục ` | ` · <span class="tt-stars" aria-label="Best ` | 43→41 ký tự (≤120%). |
| `src/ui/title.ts:29` | ` sao">` | ` stars">` | ⚑ 5→7 ký tự, +40%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/ui/title.ts:161` | `<header class="tt-head"><h1 class="tt-name">Lời Gọi</h1><span class="tt-seal" aria-hidden="true">Văn<br>Điền</span>` | `<header class="tt-head"><h1 class="tt-name">Wordwoven</h1><span class="tt-seal" aria-hidden="true">Word<br>Ward</span>` | ⚑ 14→17 ký tự, +21%; còn vượt 20%, Claude duyệt/rút tiếp. Tên game bắt buộc. |
| `src/ui/title.ts:162` | `<p class="tt-sub">Giữ làng tre bằng những lời gọi · <i>Wordwoven</i></p></header>` | `<p class="tt-sub">Defend your village, one word at a time.</p></header>` | 43→40 ký tự (≤120%). |
| `src/ui/title.ts:163` | `<nav class="tt-menu vd-sheet" aria-label="Màn đầu">` | `<nav class="tt-menu vd-sheet" aria-label="Title">` |  |
| `src/ui/title.ts:164` | `<p class="tt-keys">↑ ↓ chọn · Enter vào · 1–5 chọn nhanh</p>` | `<p class="tt-keys">↑ ↓ select · Enter play · 1–5 quick pick</p>` | 37→40 ký tự (≤120%). |
| `src/ui/title.ts:240` | `Chưa tải được · F5 để thử lại` | `Load failed · F5 to retry` | 29→25 ký tự (≤120%). |
| `src/view/boss-2d.ts:295` | ` mạng` | ` lives` | ⚑ 4→5 ký tự, +25%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/view/boss-2d.ts:390` | `Cháy ×1,25` | `Burn ×1.25` | 10→10 ký tự (≤120%). |
| `src/view/boss-2d.ts:426` | `Tê ` | `Stun ` | ⚑ 2→4 ký tự, +100%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/view/fx-pipe.ts:140` | `Đứng sững!` | `Pinned!` | 10→7 ký tự (≤120%). |
| `src/view/fx-pipe.ts:140` | `Vỡ vòm!` | `Broken!` | 7→7 ký tự (≤120%). |
| `src/view/fx-pipe.ts:187` | `Tối Thượng!` | `Ultimate!` | 11→9 ký tự (≤120%). |
| `src/view/words/cards.ts:24` | `Chớp` | `Flash` | ⚑ 4→5 ký tự, +25%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/view/words/cards.ts:24` | `Hoàn hảo` | `Perfect` | 8→7 ký tự (≤120%). |
| `src/view/words/cards.ts:24` | `Tốt` | `Good` | ⚑ 3→4 ký tự, +33%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/view/words/cards.ts:24` | `Vừa` | `OK` | 3→2 ký tự (≤120%). |
| `src/view/words/cards.ts:24` | `Ẩu` | `Poor` | ⚑ 2→4 ký tự, +100%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/view/words/cards.ts:28` | `Bắn mạnh` | `Power` | 8→5 ký tự (≤120%). |
| `src/view/words/cards.ts:28` | `Xây` | `Build` | ⚑ 3→5 ký tự, +67%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/view/words/cards.ts:28` | `Gặt` | `Reap` | ⚑ 3→4 ký tự, +33%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `src/view/words/cards.ts:28` | `Chặt` | `Chop` | 4→4 ký tự (≤120%). |
| `src/view/words/cards.ts:28` | `Đào` | `Dig` | 3→3 ký tự (≤120%). |
| `src/view/words/cards.ts:28` | `Hỏi bài` | `Quiz` | 7→4 ký tự (≤120%). |
| `src/view/words/cards.ts:28` | `Chữ Chiêu` | `Spell` | 9→5 ký tự (≤120%). |
| `src/view/words/cards.ts:28` | `Ngắt` | `Stop` | 4→4 ký tự (≤120%). |
| `src/view/words/cards.ts:33` | `Neo` | `Pin` | 3→3 ký tự (≤120%). |
| `src/view/words/cards.ts:33` | `Phá Khiên` | `Shatter` | 9→7 ký tự (≤120%). Rút gọn Break Shield để vừa thẻ. |
| `src/view/words/cards.ts:118` | `Chuộc lại` | `Redeemed` | 9→8 ký tự (≤120%). |
| `src/view/words/cards.ts:151` | `Hỏi bài` | `Quiz` | 7→4 ký tự (≤120%). |

## Kỳ vọng test

| file:dòng | chuỗi cũ | chuỗi mới | ghi chú |
|---|---|---|---|
| `tests/td-hud.test.ts:34` | `Mạng` | `Lives` | Chỉ đổi kỳ vọng chuỗi. ⚑ 4→5 ký tự, +25%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `tests/td-hud.test.ts:35` | `<b>Ngày 1 · 1:15</b>` | `<b>Day 1 · 1:15</b>` | Chỉ đổi kỳ vọng chuỗi. 13→12 ký tự (≤120%). |
| `tests/td-hud.test.ts:37` | `<b>Ngày 1 · 1:14</b>` | `<b>Day 1 · 1:14</b>` | Chỉ đổi kỳ vọng chuỗi. 13→12 ký tự (≤120%). |
| `tests/td-hud.test.ts:40` | `Gọi đêm sớm` | `Early night` | Chỉ đổi kỳ vọng chuỗi. 11→11 ký tự (≤120%). |
| `tests/td-hud.test.ts:58` | `<b>Gọi đêm sớm · +30 Gold</b>` | `<b>Early night · +30 Gold</b>` | Chỉ đổi kỳ vọng chuỗi. 22→22 ký tự (≤120%). |
| `tests/td-hud.test.ts:65` | `<b>Đã dừng</b>` | `<b>Paused</b>` | Chỉ đổi kỳ vọng chuỗi. 7→6 ký tự (≤120%). |
| `tests/td-hud.test.ts:68` | `names every reason the sim may refuse a command for, in Vietnamese` | `names every reason the sim may refuse a command for, in English` | Chỉ đổi kỳ vọng chuỗi. 66→63 ký tự (≤120%). |
| `tests/td-hud.test.ts:98` | `Knowledge <b>0</b> · Sổ ôn <b>1</b>` | `Knowledge <b>0</b> · Review <b>1</b>` | Chỉ đổi kỳ vọng chuỗi. 21→22 ký tự (≤120%). |
| `tests/td-hud.test.ts:127` | `Chín <b>1</b> · Lớn <b>2</b> · Trống <b>1</b>` | `Ripe <b>1</b> · Grow <b>2</b> · Empty <b>1</b>` | Chỉ đổi kỳ vọng chuỗi. 24→25 ký tự (≤120%). |
| `tests/td-hud.test.ts:127` | `Mua 4 Seeds · 30 Gold` | `Buy 4 Seeds · 30 Gold` | Chỉ đổi kỳ vọng chuỗi. 21→21 ký tự (≤120%). |
| `tests/td-hud.test.ts:127` | `class="is-on">Tự mua Seeds` | `class="is-on">Auto Seeds` | Chỉ đổi kỳ vọng chuỗi. 26→24 ký tự (≤120%). |
| `tests/td-hud.test.ts:128` | `Thuê Villager · 25 Gold, 5 Rice` | `Hire Villager · 25 Gold, 5 Rice` | Chỉ đổi kỳ vọng chuỗi. 31→31 ký tự (≤120%). |
| `tests/td-hud.test.ts:128` | `Bán 10 Rice · +10 Gold` | `Sell 10 Rice · +10 Gold` | Chỉ đổi kỳ vọng chuỗi. 22→23 ký tự (≤120%). |
| `tests/td-hud.test.ts:129` | `Lượt mạnh <b>0/5</b>` | `Charges <b>0/5</b>` | Chỉ đổi kỳ vọng chuỗi. 13→11 ký tự (≤120%). |
| `tests/td-hud.test.ts:145` | `Tạm dừng` | `Pause` | Chỉ đổi kỳ vọng chuỗi. 8→5 ký tự (≤120%). |
| `tests/td-hud.test.ts:145` | `Chạy tiếp` | `Resume` | Chỉ đổi kỳ vọng chuỗi. 9→6 ký tự (≤120%). |
| `tests/td-hud.test.ts:156` | `<b class="td-word"><span>g</span>ood</b><em class="td-warn td-halt">Tạm dừng` | `<b class="td-word"><span>g</span>ood</b><em class="td-warn td-halt">Paused` | Chỉ đổi kỳ vọng chuỗi. 12→10 ký tự (≤120%). |
| `tests/td-hud.test.ts:157` | `Tạm dừng` | `Paused` | Chỉ đổi kỳ vọng chuỗi. 8→6 ký tự (≤120%). |
| `tests/td-hud.test.ts:180` | `Bà Cú Mực: Đêm nay Mộc Tinh thức dậy.` | `Bà Cú Mực: Tonight Mộc Tinh awakens.` | Chỉ đổi kỳ vọng chuỗi. 37→36 ký tự (≤120%). Giữ tên riêng theo NAMES_EN.md. |
| `tests/td-hud.test.ts:181` | `Dồn tháp` | `Line the glowing root` | Chỉ đổi kỳ vọng chuỗi. ⚑ 8→21 ký tự, +162%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `tests/td-hud.test.ts:183` | `Bà Cú Mực: Dồn tháp lên nhánh rễ sáng.` | `Bà Cú Mực: Line the glowing root with towers.` | Chỉ đổi kỳ vọng chuỗi. 38→45 ký tự (≤120%). Giữ tên riêng theo NAMES_EN.md. |
| `tests/td-hud.test.ts:195` | `choáng` | `stunned` | Chỉ đổi kỳ vọng chuỗi. 6→7 ký tự (≤120%). |
| `tests/td-hud.test.ts:197` | `Lúc nó choáng` | `When he's stunned` | Chỉ đổi kỳ vọng chuỗi. ⚑ 13→17 ký tự, +31%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `tests/td-input.test.ts:253` | `Trong vòng 11 m quanh Fort` | `Within 11 m of Fort` | Chỉ đổi kỳ vọng chuỗi. 26→19 ký tự (≤120%). |
| `tests/td-r2.test.ts:264` | `data-act="ult" disabled>Tối Thượng · Mở ở Đêm 3` | `data-act="ult" disabled>Ultimate · Night 3` | Chỉ đổi kỳ vọng chuỗi. 47→42 ký tự (≤120%). |
| `tests/td-r2.test.ts:266` | `data-act="ult" disabled>Tối Thượng 45 %<kbd>=</kbd>` | `data-act="ult" disabled>Ultimate 45 %<kbd>=</kbd>` | Chỉ đổi kỳ vọng chuỗi. 40→38 ký tự (≤120%). |
| `tests/td-r2.test.ts:269` | `data-act="ult">Tối Thượng<kbd>=</kbd>` | `data-act="ult">Ultimate<kbd>=</kbd>` | Chỉ đổi kỳ vọng chuỗi. 26→24 ký tự (≤120%). |
| `tests/td-settings.test.ts:35` | `Theo hồ sơ` | `By profile` | Chỉ đổi kỳ vọng chuỗi. 10→10 ký tự (≤120%). |
| `tests/td-settings.test.ts:35` | `Thư giãn` | `Relaxed` | Chỉ đổi kỳ vọng chuỗi. 8→7 ký tự (≤120%). |
| `tests/td-settings.test.ts:35` | `Cân bằng` | `Balanced` | Chỉ đổi kỳ vọng chuỗi. 8→8 ký tự (≤120%). |
| `tests/td-settings.test.ts:35` | `Thử thách` | `Challenge` | Chỉ đổi kỳ vọng chuỗi. 9→9 ký tự (≤120%). |
| `tests/td-settings.test.ts:35` | `Học` | `Learn` | Chỉ đổi kỳ vọng chuỗi. ⚑ 3→5 ký tự, +67%; còn vượt 20%, Claude duyệt/rút tiếp. |
| `tests/td-settings.test.ts:59` | `<p class="td-best">Kỷ lục <b>★★</b></p>` | `<p class="td-best">Best <b>★★</b></p>` | Chỉ đổi kỳ vọng chuỗi. 9→7 ký tự (≤120%). |
| `tests/td-settings.test.ts:60` | `Kỷ lục mới` | `Best new` | Chỉ đổi kỳ vọng chuỗi. 10→8 ký tự (≤120%). |
| `tests/td-test-pass.test.ts:20` | `Xây Archer Tower` | `Build Archer Tower` | Chỉ đổi kỳ vọng chuỗi. 16→18 ký tự (≤120%). |
| `tests/td-test-pass.test.ts:22` | `Gõ chữ trên thẻ tháp` | `Type tower card words` | Chỉ đổi kỳ vọng chuỗi. 20→21 ký tự (≤120%). |
| `tests/td-test-pass.test.ts:26` | `Word Shot của Cannon Tower` | `Cannon Tower's Word Shot` | Chỉ đổi kỳ vọng chuỗi. 26→24 ký tự (≤120%). |
| `tests/td-test-pass.test.ts:29` | `Quái lọt vào Fort` | `Foes reached Fort` | Chỉ đổi kỳ vọng chuỗi. 17→17 ký tự (≤120%). |
| `tests/td-test-pass.test.ts:30` | `Quái lọt vào Fort` | `Foes reached Fort` | Chỉ đổi kỳ vọng chuỗi. 17→17 ký tự (≤120%). |
| `tests/td-test-pass.test.ts:55` | `Tối Thượng · Mở ở Đêm 3` | `Ultimate · Night 3` | Chỉ đổi kỳ vọng chuỗi. 23→18 ký tự (≤120%). |
| `tests/td-test-pass.test.ts:122` | `Sinh khí làng này` | `This village's life` | Chỉ đổi kỳ vọng chuỗi. 17→19 ký tự (≤120%). |
| `tests/td-test-pass.test.ts:124` | `Rễ ơi, mọc lên!` | `Roots, rise!` | Chỉ đổi kỳ vọng chuỗi. 15→12 ký tự (≤120%). |
| `tests/td-hud.test.ts:39` | `expect(status(w)).toMatch(/<b>Đêm 1 · còn \d+ quái<\/b>/);` | `expect(status(w)).toMatch(/<b>Night 1 · \d+ foes left<\/b>/);` | Kỳ vọng regex theo chữ hiển thị; số và luật giữ nguyên. Chỉ đổi kỳ vọng chuỗi. 50→53 ký tự (≤120%). |
| `tests/td-hud.test.ts:48` | `const promised = Number(/Gọi đêm sớm · \+(\d+) Gold/.exec(html)?.[1]);` | `const promised = Number(/Early night · \+(\d+) Gold/.exec(html)?.[1]);` | Kỳ vọng regex theo chữ hiển thị; số và luật giữ nguyên. Chỉ đổi kỳ vọng chuỗi. 70→70 ký tự (≤120%). |
| `tests/td-hud.test.ts:81` | `const chip = () => /Đang gọi (\d+)\/(\d+)/.exec(teamHtml(w, 0))?.slice(1).map(Number);` | `const chip = () => /Calling (\d+)\/(\d+)/.exec(teamHtml(w, 0))?.slice(1).map(Number);` | Kỳ vọng regex theo chữ hiển thị; số và luật giữ nguyên. Chỉ đổi kỳ vọng chuỗi. 86→85 ký tự (≤120%). |
| `tests/td-hud.test.ts:139` | `expect(dockHtml(w, sel)).toMatch(/⛏️ Đào.*2 từ · đang mờ.*Ngoài vòng giúp.*Gửi Draconis/s);` | `expect(dockHtml(w, sel)).toMatch(/⛏️ Dig.*2 words · dim.*Out of range.*Send Draconis/s);` | Kỳ vọng regex theo chữ hiển thị; số và luật giữ nguyên. Chỉ đổi kỳ vọng chuỗi. 91→88 ký tự (≤120%). |
| `tests/td-hud.test.ts:142` | `expect(dockHtml(w, sel)).toMatch(/Trong vòng giúp: sáng khi bớt lời gọi đang sáng/);` | `expect(dockHtml(w, sel)).toMatch(/In range: lights up when a call slot is free/);` | Kỳ vọng regex theo chữ hiển thị; số và luật giữ nguyên. Chỉ đổi kỳ vọng chuỗi. 84→81 ký tự (≤120%). |
| `tests/td-hud.test.ts:145` | `expect([actionsHtml(w, false), actionsHtml(w, true)].map((html) => /data-act="space">([^<]+)/.exec(html)?.[1])).toEqual(["Tạm dừng", "Chạy tiếp"]);` | `expect([actionsHtml(w, false), actionsHtml(w, true)].map((html) => /data-act="space">([^<]+)/.exec(html)?.[1])).toEqual(["Pause", "Resume"]);` | Kỳ vọng regex theo chữ hiển thị; số và luật giữ nguyên. Chỉ đổi kỳ vọng chuỗi. 147→141 ký tự (≤120%). |
| `tests/td-hud.test.ts:153` | `expect(stripHtml(w, "", true)).toMatch(/^<em class="td-warn td-halt">Tạm dừng · Space<\/em><span class="td-chain"/);` | `expect(stripHtml(w, "", true)).toMatch(/^<em class="td-warn td-halt">Paused · Space<\/em><span class="td-chain"/);` | Kỳ vọng regex theo chữ hiển thị; số và luật giữ nguyên. Chỉ đổi kỳ vọng chuỗi. 82→80 ký tự (≤120%). |
| `tests/td-hud.test.ts:192` | `expect(new BossBanner().html(w, 0)).toMatch(/choáng · Dễ Tổn Thương 5 s/);` | `expect(new BossBanner().html(w, 0)).toMatch(/stunned · Vulnerable 5 s/);` | Kỳ vọng regex theo chữ hiển thị; số và luật giữ nguyên. Chỉ đổi kỳ vọng chuỗi. 74→72 ký tự (≤120%). |
| `tests/td-test-pass.test.ts:24` | `expect(lossHint(w)).toMatch(/Bắn mạnh.*xây thêm tháp/); // day 1: Tháp Pháo is still shut` | `expect(lossHint(w)).toMatch(/Power.*add towers/); // day 1: Tháp Pháo is still shut` | Kỳ vọng regex theo chữ hiển thị; số và luật giữ nguyên. Chỉ đổi kỳ vọng chuỗi. 89→83 ký tự (≤120%). |
| `tests/td-test-pass.test.ts:123` | `expect(lineAt(2600)).toMatch(/Rễ hút 1 mạng mỗi 30 s/);` | `expect(lineAt(2600)).toMatch(/Roots drain 1 life every 30 s/);` | Kỳ vọng regex theo chữ hiển thị; số và luật giữ nguyên. Chỉ đổi kỳ vọng chuỗi. 55→62 ký tự (≤120%). |

Test mới `tests/english-ui.test.ts` dùng TypeScript AST để quét literal và mọi mảnh template, thêm chuỗi CSS và chữ/nhãn HTML. Không có test mới cho luật chơi.
