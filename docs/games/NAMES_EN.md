# Bảng đề xuất tên tiếng Anh trong ba game

Ngày 27/10/2026 · Phiếu 026 · **Bản đề xuất để Claude duyệt, chưa đổi chuỗi trong game.**

Áp dụng mục “In-game names” trong `AGENTS.md` của repo cha: tên danh từ của thực thể, đồ, súng và tài nguyên dùng tiếng Anh; câu, hướng dẫn và menu giữ tiếng Việt. Nhân vật độc nhất giữ tên riêng. Cột nghĩa Việt dùng cho lần ra mắt/chú thích đầu, không phải hậu tố thường trực.

## Cách đọc và phạm vi đếm

- Mỗi dòng là một tên đang có chuỗi trong mã; không suy tên từ model chưa được gắn vào nội dung. id có sẵn được giữ; nơi không có id dữ liệu riêng ghi trường/hằng/hàm để tra cứu.
- **Chỗ = một dòng mã có literal tên**, kể cả tên trong câu hoặc phép so sánh phụ thuộc tên. Một dòng nhắc cùng tên hai lần vẫn tính một chỗ. `file:12,18` là hai chỗ. Đây là thống kê tĩnh, không phải số lần vẽ hay số màn.
- Quét chuỗi trong `src/content/**`, `src/ui/**`, `src/app/**` (thêm `src/main.ts` của Lời Gọi), các file vẽ chữ `view/banners.ts` của Rồng Giữ Ải, `view/words/cards.ts` của Lời Gọi và `view/{hud,screens,screens-journey}.ts` của Tuyến Cuối. Bỏ chú thích, log/lỗi kỹ thuật và `ui-preview.ts`; rà thường/HOA cho tên Việt, đúng kiểu chữ cho tên ASCII và các biến thể ghi ở ghi chú. Tên dài như Mỏ Vàng, Trại Lính được tách khỏi Vàng/Lính chung; tên riêng của 3 Thư Đồng được tách khỏi tên lớp. Các chuỗi id thuần chữ thường như `xung`, `tia`, `ray`, `draconis` không tính là tên hiển thị.
- **Số dòng cần sửa** ở tóm tắt là hợp các vị trí của những tên đề xuất đổi. Tổng “lượt tên–dòng” là tổng cột Chỗ, có thể lớn hơn vì một dòng nhắc nhiều tên.
- Các chỗ dùng `nameVi`/`view.name`/`gun.name` hiện tên động không nhân thêm vào cột Chỗ; file tiêu thụ được liệt kê riêng bên dưới.
- “trùng từ gõ: ...” là so **cả tên đề xuất**, bỏ khác biệt hoa/thường, với trường `en` của `shared/vocabulary/levels/*.json`. Không so từng thành tố của tên ghép. Không có ghi chú này nghĩa là không trùng cả tên.
- Nhãn chỉ số, kiểu từ gõ, tên ải/vùng/chế độ và kỹ năng động từ ở bảng **Cần Claude xem**; không tính vào số phải đổi. Danh từ mô tả thông thường trong câu như giây, mét, máu, mũi tên, cây không được suy thành một tên vật phẩm mới.
- Kiểm `rg -F` thô bao gồm cả chú thích/test/script, vì vậy số đó khác cột Chỗ; số dòng và vị trí đầy đủ nằm trong [báo cáo Phiếu 026](../codex-queue/026-report.md).


## Quyết định của Claude (27/10/2026)

Người duyệt: Claude, sau phiếu 026. Các quyết định dưới đây đứng trên các bảng phía dưới; những dòng đã sửa trong bảng có ghi lại ở đây.

**Ranh giới của luật.** Chủ dự án ví dụ "như các trụ, nhà hoặc nhiều lính", nên luật áp cho **vật và sinh vật người chơi thấy, mua, đánh hay nhặt được**. Theo đó:

- **Đổi sang tiếng Anh:**
  - trụ, tháp, nhà, bẫy;
  - lính, đơn vị phe ta, loại quái, tướng địch;
  - món đồ, súng, tài nguyên (Gold, Wood, Rice, Seeds, Knowledge, Dragon Rage);
  - kỹ năng mang tên một vật: Fire Breath, Sky Fire, Dragon Roar, Inferno, Fire Feather Rain, Word Shot;
  - hiểm họa là một vật trên sân: Rift.
- **Giữ tiếng Việt:**
  - chỉ số (Giáp, Khiên, Kháng phép, Mạng, Vỏ);
  - chế độ (Thư giãn, Cân bằng, Thử thách, Học, Hộp cát, Hành trình, Trận thử);
  - tên nơi chốn: bản đồ, đường, chương, ải (Đồng Cỏ Thác Bạc, Đường Cầu, Hành Lang VC-7…);
  - nhãn cơ chế và loại từ gõ (Chữ Chiêu, Từ Khẩn, Từ Ngắt, Từ Trợ, Từ Kích, Cụm Ấn, Ấn Phá, Héo lan, Vùng Chữ, Tối Thượng);
  - lời gọi là động từ (Xây, Gặt, Chặt, Đào, Bắn mạnh, Hỏi bài, Ngắt, Neo, Phá Khiên, Cắm Cờ, Nhổ cờ);
  - nhãn học (Thẻ Ôn, Học trước, Sổ Từ Ải, Sổ ôn), nhãn lớp trên thẻ chữ (Quái, Bầy, Tinh anh, Tướng, Bộ phận, Vật), mục tiêu, sự kiện, trạng thái.

  Chúng là menu, câu và gợi ý, mà luật giữ những thứ này bằng tiếng Việt.
- **Giữ tên riêng:** Hỏa Long, Bạch Long, Draconis, Mộc Tinh, Bà Cú Mực, Chấm, Phẩy, Gạch, Vanguard. Tên phe "Bầy Hố Đen" cũng là tên riêng.

**Đã chốt các dòng "Cần Claude xem":**

| Game | Tên Việt | Quyết định |
|---|---|---|
| Rồng Giữ Ải | Phun Lửa | **Fire Breath** (hơi lửa rồng) |
| Rồng Giữ Ải | Viêm Đế | **Inferno** (biển lửa), trùng id `inferno` trong mã |
| Tuyến Cuối | Vết nứt (hiểm họa) | **Rift** (vết nứt không gian). Tên ải "Vách nứt" giữ tiếng Việt |
| cả ba | các dòng còn lại | giữ tiếng Việt theo ranh giới trên |

**Đã sửa tên đề xuất trong bảng:**

| Game | Tên Việt | Codex đề xuất | Chốt | Lý do |
|---|---|---|---|---|
| Lời Gọi | Lũy Chữ | Keep | **Fort** | "keep" là động từ người học gặp hằng ngày, đọc dễ nhầm; "fort" ngắn, đúng nghĩa |
| Lời Gọi | Cương Thi | Zombie | **Hopping Zombie** | đúng loài trong truyện dân gian Á Đông (nhảy), khác thây ma phương Tây |
| Lời Gọi | Cương Thi Đầu Đàn | Horde Leader | **Zombie Leader** | đi cặp với Hopping Zombie, người chơi biết nó dẫn loài nào |
| Lời Gọi | Mầm Gỗ | Wood Sprout | **Sapling** | một từ tiếng Anh thật, đúng nghĩa cây non |
| Lời Gọi | Nuppeppō con | Flesh Bit | **Little Blob** | đi cặp với Split Blob, đọc nhẹ hơn với trẻ em |
| Tuyến Cuối | Đầu Đàn | Leader | **Pack Leader** | "Leader" chung chung; "Pack Leader" đúng nghĩa "đầu đàn" |
| Rồng Giữ Ải | Vệ Binh Rêu (lính phe ta) | Moss Warden | **Grove Warden** | quái phe địch là Moss Grunt và Moss Bannerman; lính phe ta mà cũng mở đầu bằng "Moss" thì đọc nhanh dễ nhầm phe |

**Cách áp dụng.**

- Mỗi game đổi tên trong một lượt riêng, chạy khi làn của game đó đã xong, không đổi lẻ tẻ.
- Lần đầu một tên hiện (thẻ ra mắt, chú thích ở cửa hàng), có thể kèm nghĩa Việt ở cột "Nghĩa Việt ngắn".
- Không đổi id trong mã hay tên file model.
- Tên trùng một từ người chơi phải gõ (cột ghi chú "trùng từ gõ") là bình thường, vì tên chỉ để đọc, không phải để gõ.
- Lượt đổi tên phải chạy lại test và golden của game đó.

## Rồng Giữ Ải (`games/dragon-hold`)

Nguồn: `src/content/data/{enemies,generals,our-side,maps,stages,waves}.ts`, `src/content/rules.ts`, `src/ui/**`, `src/app/**`; `docs/games/dragon-lane/02-enemies-generals-bosses.md` và `03-our-side-shop-traps-support.md`; `art-src/3d/SOURCES.json` và `tools/map-factory/registry/out/assets.dragon-hold.json`. Đối chiếu bổ sung `src/view/banners.ts` vì nhãn Cắm Cờ được vẽ ở đó.

### Bảng đề xuất

| id trong mã | Tên Việt hiện tại | Tên tiếng Anh đề xuất | Nghĩa Việt ngắn (cho lần đầu) | Loại | Chỗ hiện (file:dòng, đếm số chỗ) | Ghi chú |
|---|---|---|---|---|---|---|
| `moss-grunt` | Yêu Rêu Lính | Moss Grunt | lính rêu | Loại quái | **3 chỗ**; `games/dragon-hold/src/content/data/enemies.ts:43`; `games/dragon-hold/src/ui/wave-card.ts:83,85` | Có sẵn nameEn; model enemies/moss-grunt. Nhãn gọn Yêu Rêu do wave-card.ts xử lý riêng. Biến thể: `Yêu Rêu`. |
| `moss-archer` | Yêu Rêu Cung | Moss Archer | cung thủ rêu | Loại quái | **1 chỗ**; `games/dragon-hold/src/content/data/enemies.ts:75` | Có sẵn nameEn; model enemies/moss-archer. |
| `blight-wolf` | Sói Mục | Blight Wolf | sói héo mục | Loại quái | **1 chỗ**; `games/dragon-hold/src/content/data/enemies.ts:106` | Có sẵn nameEn; model enemies/blight-wolf. |
| `tusk-boar` | Heo Nanh Đá | Tusk Boar | heo rừng nanh lớn | Loại quái | **1 chỗ**; `games/dragon-hold/src/content/data/enemies.ts:138` | Có sẵn nameEn; model enemies/tusk-boar. |
| `thorn-wasp` | Ong Gai | Thorn Wasp | ong bắp cày gai | Loại quái | **1 chỗ**; `games/dragon-hold/src/content/data/enemies.ts:169` | Có sẵn nameEn; model enemies/thorn-wasp. |
| `thorn-ant` | Kiến Gai | Thorn Ant | kiến gai | Loại quái | **1 chỗ**; `games/dragon-hold/src/content/data/enemies.ts:201` | Có sẵn nameEn; model enemies/thorn-ant. |
| `moss-banner` | Yêu Rêu Cầm Cờ | Moss Bannerman | lính rêu cầm cờ | Tướng địch | **1 chỗ**; `games/dragon-hold/src/content/data/generals.ts:13` | Giữ nameEn hiện có; model generals/moss-banner chỉ người cầm cờ, không phải tên riêng. |
| `spikes` | Gai Chông | Spikes | chông nhọn | Bẫy | **3 chỗ**; `games/dragon-hold/src/content/data/our-side.ts:41`; `games/dragon-hold/src/ui/debut-card.ts:25,26` | Theo model traps/spikes. |
| `pine-bomb` | Bom Hạt Thông | Pine Bomb | bom quả thông | Bẫy | **2 chỗ**; `games/dragon-hold/src/content/data/our-side.ts:66`; `games/dragon-hold/src/ui/debut-card.ts:22` | Theo model traps/pine-bomb. |
| `net-launcher` | Lưới Phóng | Net Launcher | máy phóng lưới | Bẫy | **3 chỗ**; `games/dragon-hold/src/content/data/our-side.ts:91`; `games/dragon-hold/src/ui/debut-card.ts:23`; `games/dragon-hold/src/ui/wave-card.ts:276` | Theo model traps/net-launcher; đây là bẫy, không phải chiêu Rồng. |
| `herb-hut` | Lều Thuốc Nam | Herb Hut | lều thảo dược | Nhà | **1 chỗ**; `games/dragon-hold/src/content/data/our-side.ts:119` | Theo model houses/herb-hut. |
| `moss-warden` | Vệ Binh Rêu | Grove Warden | vệ binh rêu | Đơn vị phe ta | **3 chỗ**; `games/dragon-hold/src/content/data/our-side.ts:144`; `games/dragon-hold/src/ui/debut-card.ts:21,25` | Theo model units/moss-warden; giữ khác Moss Grunt và Moss Bannerman, phân biệt bằng danh từ cuối và màu phe. |
| `small-potion` | Bình Máu Nhỏ | Small Potion | bình hồi máu nhỏ | Đồ tiêu hao | **3 chỗ**; `games/dragon-hold/src/app/app.ts:826`; `games/dragon-hold/src/content/data/our-side.ts:172`; `games/dragon-hold/src/ui/hud.ts:399` | Có tên rút gọn Bình Máu trong HUD và cảnh báo. Biến thể: `Bình Máu`. |
| `dragon-heart` | Tim Rồng | Dragon Heart | tim rồng | Món nâng cấp | **1 chỗ**; `games/dragon-hold/src/content/data/our-side.ts:191` | id trong HERO_UPGRADES; không đổi id. |
| `hard-scale` | Vảy Cứng | Hard Scale | vảy cứng | Món nâng cấp | **1 chỗ**; `games/dragon-hold/src/content/data/our-side.ts:206` | id trong HERO_UPGRADES; đây là món tăng Giáp, không phải tiền Vảy Rồng. |
| `gold` | Vàng | Gold | vàng | Tài nguyên | **16 chỗ**; `games/dragon-hold/src/ui/hud.ts:161,242`; `games/dragon-hold/src/ui/learning-frame.ts:492,645`; `games/dragon-hold/src/ui/placement-ui.ts:72,81,533,636,649,651`; `games/dragon-hold/src/ui/results.ts:299,300`; `games/dragon-hold/src/ui/shop-strip.ts:84,215,216`; `games/dragon-hold/src/ui/wave-card.ts:368` | Đổi nhãn và danh từ trong giá/thưởng/cảnh báo; câu xung quanh giữ tiếng Việt; trùng từ gõ: 5 (A1 Foundation 005; 005.json) |
| `rage` | Long Nộ | Dragon Rage | nộ khí rồng | Tài nguyên | **4 chỗ**; `games/dragon-hold/src/ui/hud.ts:164,332,337`; `games/dragon-hold/src/ui/wave-card.ts:368` | Thanh năng lượng nạp Tối Thượng; không phải tên nhân vật. |
| `RINGS.daisMm; hero` | Bệ Rồng | Dragon Platform | bệ đứng của rồng | Công trình | **2 chỗ**; `games/dragon-hold/src/ui/hud.ts:432`; `games/dragon-hold/src/ui/results.ts:293` | Không có id Placeable riêng; chuỗi hiện trong thông báo thất thủ. |
| `plant-banner; flag` | cờ | Banner | cờ hiệu | Vật thể | **3 chỗ**; `games/dragon-hold/src/ui/debut-card.ts:27`; `games/dragon-hold/src/ui/tags.ts:461`; `games/dragon-hold/src/view/banners.ts:248` | Vật được tướng cắm; nhãn hành động Cắm Cờ/Nhổ cờ nằm ở bảng cần xem; trùng từ gõ: 12 (A1 Foundation 012; 012.json) |
| `skyfire` | Thiên Hỏa | Sky Fire | lửa từ trời | Kỹ năng tên vật | **3 chỗ**; `games/dragon-hold/src/ui/debut-card.ts:24,121`; `games/dragon-hold/src/ui/hud.ts:58` | Danh từ chỉ lửa; HUD và thẻ ra mắt. |
| `roar` | Long Hống | Dragon Roar | tiếng rồng gầm | Kỹ năng tên vật | **3 chỗ**; `games/dragon-hold/src/ui/hud.ts:324,469`; `games/dragon-hold/src/ui/tags.ts:463` | Danh từ chỉ tiếng gầm; kích bằng Từ Khẩn. |
| `hero` | Hỏa Long | — | rồng lửa | Nhân vật độc nhất | **12 chỗ**; `games/dragon-hold/src/app/app.ts:826`; `games/dragon-hold/src/ui/debut-card.ts:21,24`; `games/dragon-hold/src/ui/hud.ts:175,287`; `games/dragon-hold/src/ui/results.ts:194,196,198,201,203`; `games/dragon-hold/src/ui/shop-strip.ts:74,77` | giữ tên riêng |
| `guide` | Bạch Long | — | rồng trắng dẫn đường | Nhân vật độc nhất | **2 chỗ**; `games/dragon-hold/src/ui/hud.ts:281,282` | giữ tên riêng |

### Cần Claude xem

| id trong mã | Tên Việt hiện tại | Tên tiếng Anh đề xuất | Nghĩa Việt ngắn (cho lần đầu) | Loại | Chỗ hiện (file:dòng, đếm số chỗ) | Ghi chú |
|---|---|---|---|---|---|---|
| `breath` | Phun Lửa | — | — | Kỹ năng động từ | **5 chỗ**; `games/dragon-hold/src/ui/debut-card.ts:22,121`; `games/dragon-hold/src/ui/hud.ts:57`; `games/dragon-hold/src/ui/results.ts:196,198` | Động tác phun; Claude quyết định phạm vi luật danh từ. |
| `inferno` | Viêm Đế | — | — | Tên Tối Thượng | **1 chỗ**; `games/dragon-hold/src/ui/hud.ts:61` | Tên chiêu có sắc thái tước hiệu; không tự coi là vật hay nhân vật. |
| `seal` | Ấn Phá | — | — | Cơ chế gõ | **1 chỗ**; `games/dragon-hold/src/ui/tags.ts:460` | Có thể là vật ấn hoặc nhãn kiểu từ; cần quyết định cùng Chữ Chiêu/Cụm Ấn. |
| `skill` | Chữ Chiêu | — | — | Cơ chế gõ | **1 chỗ**; `games/dragon-hold/src/ui/tags.ts:464` | Tên loại từ điều khiển, không phải vật phẩm. |
| `urgent` | Từ Khẩn | — | — | Cơ chế gõ | **2 chỗ**; `games/dragon-hold/src/ui/hud.ts:324,469` | Tên loại từ điều khiển Long Hống. |
| `interrupt` | Từ Ngắt | — | — | Cơ chế gõ | **1 chỗ**; `games/dragon-hold/src/ui/tags.ts:462` | Tên loại từ điều khiển. |
| `assist` | Từ Trợ | — | — | Cơ chế gõ | **1 chỗ**; `games/dragon-hold/src/ui/tags.ts:465` | Tên loại từ hỗ trợ. |
| `trigger` | Từ Kích | — | — | Cơ chế gõ | **1 chỗ**; `games/dragon-hold/src/ui/tags.ts:466` | Tên loại từ kích bẫy. |
| `boss-seal` | Cụm Ấn | — | — | Cơ chế gõ | **1 chỗ**; `games/dragon-hold/src/ui/tags.ts:468` | Nhãn trong KIND_STYLE dù boss chưa được cài thành nội dung ải. |
| `plant-banner` | Cắm Cờ | — | — | Kỹ năng động từ | **2 chỗ**; `games/dragon-hold/src/ui/debut-card.ts:27`; `games/dragon-hold/src/view/banners.ts:248` | Chuỗi thực nằm ở view/banners.ts, ngoài UI; cần rà cùng nhãn cờ. |
| `flag` | Nhổ cờ | — | — | Hành động | **2 chỗ**; `games/dragon-hold/src/ui/debut-card.ts:27`; `games/dragon-hold/src/ui/tags.ts:461` | Động từ chỉ cách xử lý cờ, không tự đổi cả nhãn. |
| `armour` | Giáp | — | — | Chỉ số | **2 chỗ**; `games/dragon-hold/src/ui/hud.ts:289`; `games/dragon-hold/src/ui/shop-strip.ts:77` | Phân biệt chỉ số phòng thủ với món áo giáp. |
| `shield` | Khiên | — | — | Chỉ số | **2 chỗ**; `games/dragon-hold/src/ui/hud.ts:294,447` | Trong HUD là lượng khiên tạm, chưa có món tên Khiên. |
| `resist` | Kháng phép | — | — | Chỉ số | **1 chỗ**; `games/dragon-hold/src/ui/shop-strip.ts:77` | Nhãn thuộc tính, không phải món đồ. |
| `PRESSURE` | Héo lan | — | — | Cơ chế chiến đấu | **1 chỗ**; `games/dragon-hold/src/ui/results.ts:198` | Tên hiệu ứng rút máu; chưa quyết định có thuộc nhóm tên phải đổi. |
| `RINGS.wordZoneMm` | Vùng Chữ | — | — | Vùng cơ chế | **2 chỗ**; `games/dragon-hold/src/app/app.ts:706`; `games/dragon-hold/src/ui/results.ts:198` | Vùng chiến đấu, không phải tên công trình. |
| `L2-cau; MAP_L2_CAU` | Cầu và Suối | — | — | Tên bản đồ | **2 chỗ**; `games/dragon-hold/src/content/data/maps.ts:35`; `games/dragon-hold/src/content/data/stages.ts:13` | Giữ chờ Claude; chuỗi cũng nằm trong tên ải. |
| `cau` | Đường Cầu | — | — | Tên đường | **1 chỗ**; `games/dragon-hold/src/content/data/maps.ts:41` | Tên tuyến trên bản đồ. |
| `suoi` | Đường Suối | — | — | Tên đường | **1 chỗ**; `games/dragon-hold/src/content/data/maps.ts:49` | Tên tuyến trên bản đồ. |
| `troi` | Đường Trời | — | — | Tên đường | **2 chỗ**; `games/dragon-hold/src/content/data/maps.ts:58`; `games/dragon-hold/src/ui/debut-card.ts:23` | Tên tuyến trên bản đồ; được nhắc trong thẻ ra mắt. |
| `m0-l2-cau` | Bản thử: Cầu và Suối | — | — | Tên ải | **1 chỗ**; `games/dragon-hold/src/content/data/stages.ts:13` | Tên bản thử, không tự dịch. |
| `STAGE_M0.carry; createShopStrip` | Bộ Mang Theo | — | — | Nhãn giao diện | **2 chỗ**; `games/dragon-hold/src/ui/placement-ui.ts:524`; `games/dragon-hold/src/ui/shop-strip.ts:176` | Tên khay/cấu hình mang đồ, không phải một món. |
| `createResults` | Sổ Từ Ải | — | — | Nhãn học | **1 chỗ**; `games/dragon-hold/src/ui/results.ts:248` | Tên phần ôn từ ở kết quả. |
| `createReviewCard` | Thẻ Ôn | — | — | Nhãn học | **4 chỗ**; `games/dragon-hold/src/app/app.ts:531`; `games/dragon-hold/src/ui/learning-frame.ts:158,564,614` | Tên giao diện học, không tự coi là thẻ vật phẩm. |
| `createPrelearn` | Học trước | — | — | Nhãn học | **3 chỗ**; `games/dragon-hold/src/app/app.ts:531`; `games/dragon-hold/src/ui/learning-frame.ts:443,455` | Tên giao diện học. |
| `KIND_STYLE.enemy` | Quái | — | — | Nhãn loại mục tiêu | **21 chỗ**; `games/dragon-hold/src/app/app.ts:705,706`; `games/dragon-hold/src/app/pace-card.ts:29`; `games/dragon-hold/src/ui/debut-card.ts:117`; `games/dragon-hold/src/ui/hud.ts:324,469`; `games/dragon-hold/src/ui/placement-ui.ts:640,674`; `games/dragon-hold/src/ui/results.ts:196,198,199`; `games/dragon-hold/src/ui/shop-strip.ts:61,62,66,70`; `games/dragon-hold/src/ui/tags.ts:456`; `games/dragon-hold/src/ui/wave-card.ts:133,276,278,293,372` | Tên lớp mục tiêu trong thẻ chữ, không phải tên một loài quái. |
| `KIND_STYLE.cluster` | Bầy | — | — | Nhãn loại mục tiêu | **3 chỗ**; `games/dragon-hold/src/ui/debut-card.ts:22,26`; `games/dragon-hold/src/ui/tags.ts:457` | Nhãn cụm quái trong thẻ chữ; cần phân biệt với tên từng loài. |
| `KIND_STYLE.elite` | Tinh anh | — | — | Bậc quái | **1 chỗ**; `games/dragon-hold/src/ui/tags.ts:458` | Tên bậc ghép, chưa xác định có đổi như tên loài. |
| `KIND_STYLE.general` | Tướng | — | — | Nhãn loại mục tiêu | **10 chỗ**; `games/dragon-hold/src/ui/debut-card.ts:27,117`; `games/dragon-hold/src/ui/tags.ts:459`; `games/dragon-hold/src/ui/wave-card.ts:82,134,258,284,286,287,293` | Nhãn chung của tướng địch, không phải tên Yêu Rêu Cầm Cờ. |
| `KIND_STYLE["boss-part"]` | Bộ phận | — | — | Nhãn loại mục tiêu | **1 chỗ**; `games/dragon-hold/src/ui/tags.ts:467` | Nhãn bộ phận boss, chưa có nội dung boss tương ứng. |
| `KIND_STYLE.map` | Vật | — | — | Nhãn loại mục tiêu | **1 chỗ**; `games/dragon-hold/src/ui/tags.ts:469` | Nhãn chung cho vật trên bản đồ, không phải tên riêng một món. |

### Tóm tắt

**21 tên phải đổi theo đề xuất; 2 tên giữ (2 tên riêng); 31 dòng chờ Claude.** Có **55 dòng mã khác nhau** cần sửa literal, tương ứng 57 lượt tên–dòng.

File có literal tên đề xuất đổi:

- `games/dragon-hold/src/app/app.ts`.
- `games/dragon-hold/src/content/data/enemies.ts`.
- `games/dragon-hold/src/content/data/generals.ts`.
- `games/dragon-hold/src/content/data/our-side.ts`.
- `games/dragon-hold/src/ui/debut-card.ts`.
- `games/dragon-hold/src/ui/hud.ts`.
- `games/dragon-hold/src/ui/learning-frame.ts`.
- `games/dragon-hold/src/ui/placement-ui.ts`.
- `games/dragon-hold/src/ui/results.ts`.
- `games/dragon-hold/src/ui/shop-strip.ts`.
- `games/dragon-hold/src/ui/tags.ts`.
- `games/dragon-hold/src/ui/wave-card.ts`.
- `games/dragon-hold/src/view/banners.ts`.

File tiêu thụ tên động cần rà cách rút gọn, độ rộng và nội suy khi đổi:

- `games/dragon-hold/src/ui/debut-card.ts`.
- `games/dragon-hold/src/ui/hud.ts`.
- `games/dragon-hold/src/ui/placement-ui.ts`.
- `games/dragon-hold/src/ui/shop-strip.ts`.
- `games/dragon-hold/src/ui/tags.ts`.
- `games/dragon-hold/src/ui/wave-card.ts`.

Test có tên/literal liên quan (kết quả tìm thô; chỉ sửa chỗ assert/fixture phụ thuộc chuỗi, không tự sửa logic):

- `games/dragon-hold/tests/sim/battle-damage.test.ts` (đến dòng 136, 152, 167).
- `games/dragon-hold/tests/sim/battle-helpers.ts` (đến dòng 87).
- `games/dragon-hold/tests/sim/battle-species.test.ts` (đến dòng 173).
- `games/dragon-hold/tests/sim/bot-policy.test.ts` (đến dòng 73, 103).
- `games/dragon-hold/tests/sim/ourside-houses.test.ts` (đến dòng 17, 24).
- `games/dragon-hold/tests/sim/ourside-shop.test.ts` (đến dòng 138, 143).
- `games/dragon-hold/tests/sim/ourside-traps.test.ts` (đến dòng 34, 59, 84, 96).
- `games/dragon-hold/tests/ui/debut-card.test.ts` (đến dòng 22).
- `games/dragon-hold/tests/ui/placement.test.ts` (đến dòng 82).
- `games/dragon-hold/tests/ui/shop-strip.test.ts` (đến dòng 16, 61, 63).

Script kiểm/QA có nhắc tên: `games/dragon-hold/scripts/balance/policy.ts`; `games/dragon-hold/scripts/balance/reader.ts`; `games/dragon-hold/scripts/balance/report.ts`; `games/dragon-hold/scripts/visual/scenarios/dh-banner.mjs`; `games/dragon-hold/scripts/visual/scenarios/dh-crowd.mjs`; `games/dragon-hold/scripts/visual/scenarios/dh-placement.mjs`; `games/dragon-hold/scripts/visual/scenarios/dh-telegraphs.mjs`; `games/dragon-hold/scripts/visual/scenarios/ui-preview.mjs`.

Golden/snapshot dữ liệu đã dò: `games/dragon-hold/tests/golden/m0.json`.
Golden/snapshot có chuỗi: **không tìm thấy literal tên cần đổi** trong golden/snapshot đang có. Không tạo lại golden ở phiếu này. Khi đổi tên thật, làn game cần kiểm xem hàm băm có gộp nội dung hiển thị hay không.

## Lời Gọi (`games/typing-defense`)

Nguồn: `src/content/slice-1a.ts`, `rules.ts`, `src/ui/**`, `src/view/words/cards.ts`; `docs/td/TYPING_DEFENSE_DESIGN.md`; `tools/map-factory/registry/out/assets.typing-defense.json`. Đối chiếu bổ sung các trường `NPC_KIND`, `CALL_KIND` và chỗ vẽ tên động.

### Bảng đề xuất

| id trong mã | Tên Việt hiện tại | Tên tiếng Anh đề xuất | Nghĩa Việt ngắn (cho lần đầu) | Loại | Chỗ hiện (file:dòng, đếm số chỗ) | Ghi chú |
|---|---|---|---|---|---|---|
| `keep` | Lũy Chữ | Fort | lũy chính | Công trình | **15 chỗ**; `games/typing-defense/src/app/sandbox.ts:14`; `games/typing-defense/src/content/slice-1a.ts:36`; `games/typing-defense/src/main.ts:297`; `games/typing-defense/src/ui/build-menu.ts:34,36`; `games/typing-defense/src/ui/hud.ts:27,32,60,204,213`; `games/typing-defense/src/ui/sheets.ts:42,43,95`; `games/typing-defense/src/ui/team-bar.ts:20`; `games/typing-defense/src/ui/tips.ts:20` | Ưu tiên model buildings/keep; thiết kế gọi Bastion. Rà cả short Lũy; trùng từ gõ: 2 (Foundation 002; 002.json) Biến thể: `Lũy`. |
| `archer` | Tháp Cung | Archer Tower | tháp cung thủ | Tháp | **4 chỗ**; `games/typing-defense/src/content/slice-1a.ts:50`; `games/typing-defense/src/ui/sheets.ts:42,46`; `games/typing-defense/src/ui/tips.ts:19` | Theo model buildings/archer; short hiện là biểu tượng, không đổi phím. |
| `cannon` | Tháp Pháo | Cannon Tower | tháp đại bác | Tháp | **2 chỗ**; `games/typing-defense/src/content/slice-1a.ts:64`; `games/typing-defense/src/ui/sheets.ts:42` | Theo model buildings/cannon. |
| `barracks` | Trại Lính | Barracks | trại lính | Nhà | **3 chỗ**; `games/typing-defense/src/content/slice-1a.ts:76`; `games/typing-defense/src/ui/hud.ts:27,30` | Theo model buildings/barracks. |
| `gold-mine` | Mỏ Vàng | Gold Mine | mỏ vàng | Nhà | **1 chỗ**; `games/typing-defense/src/content/slice-1a.ts:81` | Theo model buildings/gold-mine. |
| `farm` | Ruộng | Rice Field | ruộng lúa | Công trình | **1 chỗ**; `games/typing-defense/src/content/slice-1a.ts:83` | Model buildings/farm; dùng Rice Field theo cây lúa thực tế và thiết kế. |
| `cuong-thi` | Cương Thi | Hopping Zombie | cương thi | Loại quái | **3 chỗ**; `games/typing-defense/src/app/sandbox.ts:22,23`; `games/typing-defense/src/content/slice-1a.ts:89` | Model giữ id enemies/cuong-thi; tên ngắn, quen thuộc cho người học; trùng từ gõ: 19 (A2 Foundation 019; 019.json) |
| `ma-troi` | Đàn Ma Trơi | Ghost Flame | ma trơi | Loại quái | **2 chỗ**; `games/typing-defense/src/content/slice-1a.ts:94`; `games/typing-defense/src/ui/tips.ts:19` | Rà cả Ma Trơi trong lời dạy; không có id tương ứng trong registry hiện đọc. Biến thể: `Ma Trơi`. |
| `thuong-luong` | Thuồng Luồng | River Serpent | rắn sông khổng lồ | Loại quái | **1 chỗ**; `games/typing-defense/src/content/slice-1a.ts:99` | Model enemies/thuong-luong; nghĩa diễn giải ngắn. |
| `mam-go` | Mầm Gỗ | Sapling | mầm cây | Loại quái | **1 chỗ**; `games/typing-defense/src/content/slice-1a.ts:110` | Model enemies/mam-go. |
| `tanuki` | Lửng Tanuki | Raccoon Dog | chó gấu tanuki | Loại quái | **3 chỗ**; `games/typing-defense/src/app/sandbox.ts:22`; `games/typing-defense/src/content/slice-1a.ts:119`; `games/typing-defense/src/ui/tips.ts:23` | Model enemies/tanuki; đây là loài quái lặp lại, không phải nhân vật độc nhất. Tên Việt gọi lửng; gloss sửa nghĩa loài. Rà Tanuki trong lời dạy. Biến thể: `Tanuki`. |
| `nuppeppo` | Nuppeppō | Split Blob | khối thịt tách đôi | Loại quái | **2 chỗ**; `games/typing-defense/src/app/sandbox.ts:22`; `games/typing-defense/src/content/slice-1a.ts:124` | Loài quái lặp lại; giữ id model enemies/nuppeppo. Dùng tên mô tả thay từ Nhật khó đọc. |
| `nuppeppo-con` | Nuppeppō con | Little Blob | mẩu thịt nhỏ | Loại quái | **1 chỗ**; `games/typing-defense/src/content/slice-1a.ts:129` | Con tách ra, không có model riêng trong registry; tên khác rõ Split Blob. |
| `cuong-thi-lead` | Cương Thi Đầu Đàn | Zombie Leader | cương thi đầu đàn | Loại quái | **2 chỗ**; `games/typing-defense/src/app/sandbox.ts:23`; `games/typing-defense/src/content/slice-1a.ts:137` | Chỉ có trong hộp cát theo dữ liệu; model gắn mũ cuong-thi-lead-hat. |
| `troll` | Quỷ Núi Troll | Troll | quỷ núi | Loại quái | **2 chỗ**; `games/typing-defense/src/app/sandbox.ts:23`; `games/typing-defense/src/content/slice-1a.ts:143` | Theo model enemies/troll; chỉ có trong hộp cát theo dữ liệu; trùng từ gõ: 24 (A2 Foundation 024; 024.json) |
| `NPC_KIND.villager` | Dân | Villager | dân làng | Đơn vị phe ta | **5 chỗ**; `games/typing-defense/src/ui/build-menu.ts:59,60`; `games/typing-defense/src/ui/hud.ts:31,101`; `games/typing-defense/src/ui/tips.ts:18` | Rà cả dân trong nút Thuê dân và lời dạy; trùng từ gõ: 69 (C1 Advanced 069; 069.json) |
| `NPC_KIND.builder` | Thợ xây | Builder | thợ xây | Đơn vị phe ta | **2 chỗ**; `games/typing-defense/src/ui/build-menu.ts:52,59` | Rà cả thợ trong thông báo chờ xây; trùng từ gõ: 35 (B1 Intermediate 035; 035.json) Biến thể: `thợ`. |
| `NPC_KIND.farmer` | nông dân | Farmer | nông dân | Đơn vị phe ta | **1 chỗ**; `games/typing-defense/src/ui/tips.ts:16` | Xuất hiện trong câu bác nông dân ở lời dạy; không đổi đại từ bác; trùng từ gõ: 8 (A1 Foundation 008; 008.json) |
| `barracks.soldiers` | Lính | Soldier | lính | Đơn vị phe ta | **2 chỗ**; `games/typing-defense/src/ui/tips.ts:19,32` | Tên lớp trong lời dạy; model units/linh-giao chưa có nhãn Lính Giáo trong nguồn UI; trùng từ gõ: 15 (A2 Foundation 015; 015.json) |
| `helpers` | Thư Đồng | Helper | trợ thủ nhỏ | Đơn vị phe ta | **1 chỗ**; `games/typing-defense/src/ui/tips.ts:20` | Đổi tên lớp chung; Chấm, Phẩy, Gạch giữ tên riêng; trùng từ gõ: 61 (B2 Upper Intermediate 061; 061.json) |
| `gold` | Vàng | Gold | vàng | Tài nguyên | **12 chỗ**; `games/typing-defense/src/app/sandbox.ts:15`; `games/typing-defense/src/ui/build-menu.ts:21,55,57,58,60`; `games/typing-defense/src/ui/hud.ts:28,57,70,206`; `games/typing-defense/src/ui/sheets.ts:96`; `games/typing-defense/src/ui/tips.ts:33` | Bao gồm vàng trong giá, thưởng và báo thiếu; trùng từ gõ: 5 (A1 Foundation 005; 005.json) |
| `wood` | Gỗ | Wood | gỗ | Tài nguyên | **8 chỗ**; `games/typing-defense/src/app/sandbox.ts:15`; `games/typing-defense/src/main.ts:297`; `games/typing-defense/src/ui/build-menu.ts:21,55,60`; `games/typing-defense/src/ui/hud.ts:28,57`; `games/typing-defense/src/ui/tips.ts:18` | Không nhận phần Gỗ thuộc tên quái Mầm Gỗ; trùng từ gõ: 12 (A1 Foundation 012; 012.json) |
| `food` | Lúa | Rice | lúa gạo | Tài nguyên | **6 chỗ**; `games/typing-defense/src/ui/build-menu.ts:59,60`; `games/typing-defense/src/ui/hud.ts:28,57`; `games/typing-defense/src/ui/tips.ts:16,30` | food ở mã; trong UI là lúa, không đổi thành Food; trùng từ gõ: 7 (A1 Foundation 007; 007.json) |
| `seeds` | Hạt giống | Seeds | hạt giống | Tài nguyên | **4 chỗ**; `games/typing-defense/src/ui/build-menu.ts:57,58`; `games/typing-defense/src/ui/hud.ts:57`; `games/typing-defense/src/ui/tips.ts:30` | Rà Hạt/hạt ở HUD và mua hạt. Biến thể: `Hạt`, `hạt`. |
| `knowledge` | Tri thức | Knowledge | tri thức | Tài nguyên | **2 chỗ**; `games/typing-defense/src/ui/hud.ts:59`; `games/typing-defense/src/ui/sheets.ts:96` | Tiền từ học; đang hiện ở HUD và kết quả; trùng từ gõ: 14 (A2 Foundation 014; 014.json) |
| `boss.chestGold` | Rương | Chest | rương thưởng | Vật phẩm | **1 chỗ**; `games/typing-defense/src/ui/sheets.ts:96` | Dòng thưởng kết ải; registry loot/chest-boss; trùng từ gõ: 14 (A2 Foundation 014; 014.json) |
| `ULT; ult.on` | Mưa lông lửa | Fire Feather Rain | mưa lông lửa | Kỹ năng tên vật | **2 chỗ**; `games/typing-defense/src/ui/hud.ts:33,100` | Tên chiêu đang xảy ra; Tối Thượng là nhãn loại chiêu, để Claude xem riêng. Biến thể: `Mưa lông`. |
| `CALL_KIND.power; STAT.wordShots` | Phát Chữ | Word Shot | phát bắn bằng chữ | Kỹ năng tên vật | **2 chỗ**; `games/typing-defense/src/ui/sheets.ts:42`; `games/typing-defense/src/ui/tips.ts:17` | Có nghĩa tiếng Anh trong bảng thuật ngữ thiết kế; chuỗi thật ở tips/sheets. |
| `moc-tinh` | Mộc Tinh | — | boss cây cổ thụ | Nhân vật độc nhất | **15 chỗ**; `games/typing-defense/src/app/sandbox.ts:21`; `games/typing-defense/src/content/slice-1a.ts:105`; `games/typing-defense/src/ui/hud.ts:32,155,158,161,162,203,204,205,206,213`; `games/typing-defense/src/ui/sheets.ts:43,94`; `games/typing-defense/src/ui/tips.ts:24` | giữ tên riêng; model bosses/moc-tinh |
| `draconis` | Draconis | — | rồng phe ta | Nhân vật độc nhất | **6 chỗ**; `games/typing-defense/src/content/slice-1a.ts:151`; `games/typing-defense/src/ui/hud.ts:33`; `games/typing-defense/src/ui/sheets.ts:42,47`; `games/typing-defense/src/ui/tips.ts:16,19` | giữ tên riêng; model mang id heroes/lam không phải lý do đổi tên nhân vật |
| `helper-cham` | Chấm | — | thư đồng kính tròn | Nhân vật độc nhất | **2 chỗ**; `games/typing-defense/src/content/slice-1a.ts:154`; `games/typing-defense/src/ui/tips.ts:20` | giữ tên riêng |
| `helper-phay` | Phẩy | — | thư đồng đuôi cong | Nhân vật độc nhất | **1 chỗ**; `games/typing-defense/src/content/slice-1a.ts:155` | giữ tên riêng |
| `helper-gach` | Gạch | — | thư đồng sọc ngang | Nhân vật độc nhất | **1 chỗ**; `games/typing-defense/src/content/slice-1a.ts:156` | giữ tên riêng |
| `narrator` | Bà Cú Mực | — | người kể chuyện | Nhân vật độc nhất | **1 chỗ**; `games/typing-defense/src/ui/hud.ts:170` | giữ tên riêng |

### Cần Claude xem

| id trong mã | Tên Việt hiện tại | Tên tiếng Anh đề xuất | Nghĩa Việt ngắn (cho lần đầu) | Loại | Chỗ hiện (file:dòng, đếm số chỗ) | Ghi chú |
|---|---|---|---|---|---|---|
| `CALL_KIND.power` | Bắn mạnh | — | — | Lời gọi động từ | **8 chỗ**; `games/typing-defense/src/ui/build-menu.ts:61`; `games/typing-defense/src/ui/hud.ts:161`; `games/typing-defense/src/ui/sheets.ts:42,43,45,47`; `games/typing-defense/src/ui/tips.ts:25`; `games/typing-defense/src/view/words/cards.ts:28` | Hành động nạp Phát Chữ, chưa tự dịch. |
| `CALL_KIND.build` | Xây | — | — | Lời gọi động từ | **10 chỗ**; `games/typing-defense/src/ui/build-menu.ts:52,59,97`; `games/typing-defense/src/ui/hud.ts:27,29,31,101`; `games/typing-defense/src/ui/sheets.ts:42`; `games/typing-defense/src/ui/tips.ts:18`; `games/typing-defense/src/view/words/cards.ts:28` | Giữ câu/menu Việt; cần quyết định với bộ CALL_NAME. |
| `CALL_KIND.harvest` | Gặt | — | — | Lời gọi động từ | **2 chỗ**; `games/typing-defense/src/ui/tips.ts:30`; `games/typing-defense/src/view/words/cards.ts:28` | Tên hành động thu hoạch. |
| `CALL_KIND.chop` | Chặt | — | — | Lời gọi động từ | **2 chỗ**; `games/typing-defense/src/ui/tips.ts:18`; `games/typing-defense/src/view/words/cards.ts:28` | Tên hành động chặt cây. |
| `CALL_KIND.mine` | Đào | — | — | Lời gọi động từ | **2 chỗ**; `games/typing-defense/src/ui/tips.ts:33`; `games/typing-defense/src/view/words/cards.ts:28` | Tên hành động đào mỏ. |
| `CALL_KIND.quiz` | Hỏi bài | — | — | Lời gọi động từ | **2 chỗ**; `games/typing-defense/src/view/words/cards.ts:28,151` | Tên hành động học. |
| `CALL_KIND.ult` | Chữ Chiêu | — | — | Cơ chế gõ | **1 chỗ**; `games/typing-defense/src/view/words/cards.ts:28` | Tên loại từ, không phải vật. |
| `CALL_KIND.direct; interrupt` | Ngắt | — | — | Lời gọi động từ | **3 chỗ**; `games/typing-defense/src/app/sandbox.ts:22`; `games/typing-defense/src/ui/tips.ts:23`; `games/typing-defense/src/view/words/cards.ts:28` | Chỉ hành động ngắt chiêu. |
| `anchor` | Neo | — | — | Lời gọi trực tiếp | **2 chỗ**; `games/typing-defense/src/app/sandbox.ts:23`; `games/typing-defense/src/view/words/cards.ts:33` | Có thể hiểu là vật neo hoặc động tác ghim quái; cần xem ngữ cảnh. |
| `shield` | Phá Khiên | — | — | Lời gọi động từ | **2 chỗ**; `games/typing-defense/src/app/sandbox.ts:23`; `games/typing-defense/src/view/words/cards.ts:33` | Chỉ hành động phá vòm của Troll, không phải món khiên. |
| `ULT` | Tối Thượng | — | — | Loại kỹ năng | **5 chỗ**; `games/typing-defense/src/app/sandbox.ts:20`; `games/typing-defense/src/ui/hud.ts:33,100`; `games/typing-defense/src/ui/team-bar.ts:25`; `games/typing-defense/src/ui/tips.ts:21` | Nhãn chung của chiêu cuối, không phải tên vật. |
| `ULT; TIPS.night3` | Lông lửa | — | — | Tài nguyên hay lời dẫn | **1 chỗ**; `games/typing-defense/src/ui/tips.ts:21` | Trong lời dạy là năng lượng nạp chiêu; chưa xác định cần đổi danh từ hay giữ cách kể. |
| `lives` | Mạng | — | — | Chỉ số sinh tồn | **4 chỗ**; `games/typing-defense/src/ui/hud.ts:57,60,158`; `games/typing-defense/src/ui/sheets.ts:96` | Không phải món đồ hay tiền; cần Claude quyết định phạm vi tài nguyên. |
| `typing.reviewN` | Sổ ôn | — | — | Nhãn học | **1 chỗ**; `games/typing-defense/src/ui/hud.ts:59` | Tên mục ôn bài, không phải sổ vật phẩm. |
| `w1-silverfall` | Đồng Cỏ Thác Bạc | — | — | Tên bản đồ | **2 chỗ**; `games/typing-defense/src/ui/hud.ts:55`; `games/typing-defense/src/ui/title.ts:21` | Tên vùng/bản đồ, không tự dịch. |
| `TitleScreen` | Văn | — | — | Tên vùng trên dấu | **1 chỗ**; `games/typing-defense/src/ui/title.ts:161` | Chữ đầu của dấu Văn/Điền ở màn đầu; hai chuỗi được ghép bởi thẻ br. |
| `TitleScreen` | Điền | — | — | Tên vùng trên dấu | **1 chỗ**; `games/typing-defense/src/ui/title.ts:161` | Chữ sau của dấu Văn/Điền; không có literal Văn Điền đầy đủ trong title. |
| `sandbox` | Hộp cát | — | — | Chế độ | **5 chỗ**; `games/typing-defense/src/app/sandbox.ts:13`; `games/typing-defense/src/main.ts:301`; `games/typing-defense/src/ui/hud.ts:30,55,56` | Tên chế độ thử. |
| `relax` | Thư giãn | — | — | Chế độ | **2 chỗ**; `games/typing-defense/src/app/sandbox.ts:17`; `games/typing-defense/src/ui/settings.ts:15` | Tên chế độ giữ chờ Claude. |
| `balanced` | Cân bằng | — | — | Chế độ | **2 chỗ**; `games/typing-defense/src/app/sandbox.ts:17`; `games/typing-defense/src/ui/settings.ts:15` | Tên chế độ giữ chờ Claude. |
| `challenge` | Thử thách | — | — | Chế độ | **2 chỗ**; `games/typing-defense/src/app/sandbox.ts:17`; `games/typing-defense/src/ui/settings.ts:15` | Tên chế độ giữ chờ Claude. |
| `learn` | Học | — | — | Chế độ | **3 chỗ**; `games/typing-defense/src/app/sandbox.ts:17`; `games/typing-defense/src/ui/settings.ts:15`; `games/typing-defense/src/ui/title.ts:24` | Tên chế độ; không thay mọi động từ học. |
| `S.staggerUntil` | Dễ Tổn Thương | — | — | Trạng thái | **1 chỗ**; `games/typing-defense/src/ui/hud.ts:210` | Tên trạng thái, chưa tự đưa vào nhóm món/loại quái. |
| `POWER; B.charges` | Lượt mạnh | — | — | Tài nguyên hay chỉ số | **1 chỗ**; `games/typing-defense/src/ui/build-menu.ts:61` | Số lượt Phát Chữ được nạp bằng Bắn mạnh; Claude chốt phạm vi nhãn tài nguyên. |

### Tóm tắt

**28 tên phải đổi theo đề xuất; 6 tên giữ (6 tên riêng); 24 dòng chờ Claude.** Có **59 dòng mã khác nhau** cần sửa literal, tương ứng 91 lượt tên–dòng.

File có literal tên đề xuất đổi:

- `games/typing-defense/src/app/sandbox.ts`.
- `games/typing-defense/src/content/slice-1a.ts`.
- `games/typing-defense/src/main.ts`.
- `games/typing-defense/src/ui/build-menu.ts`.
- `games/typing-defense/src/ui/hud.ts`.
- `games/typing-defense/src/ui/sheets.ts`.
- `games/typing-defense/src/ui/team-bar.ts`.
- `games/typing-defense/src/ui/tips.ts`.

File tiêu thụ tên động cần rà cách rút gọn, độ rộng và nội suy khi đổi:

- `games/typing-defense/src/ui/build-menu.ts`.
- `games/typing-defense/src/ui/team-bar.ts`.
- `games/typing-defense/src/view/debug-2d.ts`.

Test có tên/literal liên quan (kết quả tìm thô; chỉ sửa chỗ assert/fixture phụ thuộc chuỗi, không tự sửa logic):

- `games/typing-defense/tests/td-boss.test.ts` (đến dòng 101, 234, 353, 382).
- `games/typing-defense/tests/td-calls.test.ts` (đến dòng 439).
- `games/typing-defense/tests/td-content.test.ts` (đến dòng 154, 159).
- `games/typing-defense/tests/td-hud.test.ts` (đến dòng 34, 96, 98, 127, 128).
- `games/typing-defense/tests/td-input.test.ts` (đến dòng 253).
- `games/typing-defense/tests/td-learn.test.ts` (đến dòng 22).
- `games/typing-defense/tests/td-r2.test.ts` (đến dòng 24, 44, 163, 171, 178, 222, 232, 272, 276).
- `games/typing-defense/tests/td-r3-abilities.test.ts` (đến dòng 17, 38, 119).
- `games/typing-defense/tests/td-sim-block.test.ts` (đến dòng 54, 72, 227).
- `games/typing-defense/tests/td-sim-combat.test.ts` (đến dòng 58, 170).
- `games/typing-defense/tests/td-sim-perf.test.ts` (đến dòng 47, 77).
- `games/typing-defense/tests/td-stage.test.ts` (đến dòng 29).
- `games/typing-defense/tests/td-test-pass.test.ts` (đến dòng 18, 20, 24, 26, 29, 30, 65).
- `games/typing-defense/tests/td-tips.test.ts` (đến dòng 41, 104).
- `games/typing-defense/tests/td/balance.ts` (đến dòng 67, 96, 126, 150).
- `games/typing-defense/tests/td/flow.ts` (đến dòng 34, 137, 287, 351, 486).
- `games/typing-defense/tests/td/golden.ts` (đến dòng 71).
- `games/typing-defense/tests/td/policies/boss.ts` (đến dòng 2, 36).
- `games/typing-defense/tests/td/policies/layouts.ts` (đến dòng 7, 9, 12).

Script kiểm/QA có nhắc tên: `games/typing-defense/scripts/models/model-contracts.ts`; `games/typing-defense/scripts/models/presets/td-rigs/cuong-thi.json`; `games/typing-defense/scripts/models/presets/td-rigs/helper-owlet.json`; `games/typing-defense/scripts/models/presets/td-rigs/linh-giao.json`; `games/typing-defense/scripts/models/presets/td-rigs/mam-go.json`; `games/typing-defense/scripts/models/presets/td-rigs/nuppeppo.json`; `games/typing-defense/scripts/models/presets/td-rigs/tanuki.json`; `games/typing-defense/scripts/models/presets/td-rigs/thuong-luong.json`; `games/typing-defense/scripts/models/presets/td-rigs/troll.json`; `games/typing-defense/scripts/models/presets/typing-defense-static.json`; `games/typing-defense/scripts/visual/scenarios/td-1a6-tour.mjs`; `games/typing-defense/scripts/visual/scenarios/td-1b-boss.mjs`; `games/typing-defense/scripts/visual/scenarios/td-1b-build.mjs`; `games/typing-defense/scripts/visual/scenarios/td-1b-direct.mjs`; `games/typing-defense/scripts/visual/scenarios/td-1b-perf.mjs`; `games/typing-defense/scripts/visual/scenarios/td-1b-story.mjs`; `games/typing-defense/scripts/visual/scenarios/td-1b-tour.mjs`; `games/typing-defense/scripts/visual/scenarios/td-theme.mjs`.

Golden/snapshot dữ liệu đã dò: `games/typing-defense/tests/golden/td-1a.json`, `games/typing-defense/tests/golden/td-1b-boss.json`.
Golden/snapshot có chuỗi: **không tìm thấy literal tên cần đổi** trong golden/snapshot đang có. Không tạo lại golden ở phiếu này. Khi đổi tên thật, làn game cần kiểm xem hàm băm có gộp nội dung hiển thị hay không.

## Tuyến Cuối (`games/typing-survival`)

Nguồn: `src/content/{guns,foes,chapter-1,stage-rules,stage-s0,threat,rules}.ts`, `src/view/hud.ts`, `src/app/**`; `docs/BUILD_S1.md`. Đối chiếu bổ sung `src/view/screens-journey.ts` và `src/content/balance.ts` vì bảng tin/chế độ lấy chuỗi từ đó.

### Bảng đề xuất

| id trong mã | Tên Việt hiện tại | Tên tiếng Anh đề xuất | Nghĩa Việt ngắn (cho lần đầu) | Loại | Chỗ hiện (file:dòng, đếm số chỗ) | Ghi chú |
|---|---|---|---|---|---|---|
| `GUN.xung=0; xung` | XUNG | Pulse Gun | súng xung | Súng | **2 chỗ**; `games/typing-survival/src/app/main.ts:229`; `games/typing-survival/src/content/guns.ts:130` | Có sẵn en: pulse; title pháo xung liên thanh. Rà cả Xung trong menu. Biến thể: `Xung`. |
| `GUN.tia=1; tia` | TIA | Heat Beam | tia nhiệt | Súng | **2 chỗ**; `games/typing-survival/src/app/main.ts:229`; `games/typing-survival/src/content/guns.ts:131` | Có sẵn en: beam; title tia nhiệt quét. Rà cả Tia trong menu. Biến thể: `Tia`. |
| `GUN.tan=2; tan` | TÁN | Scatter Gun | súng bắn chùm | Súng | **1 chỗ**; `games/typing-survival/src/content/guns.ts:132` | Có sẵn en: scatter; title súng chùm đẩy lùi. Biến thể: `Tán`. |
| `GUN.ray=3; ray` | RAY | Rail Gun | súng ray | Súng | **1 chỗ**; `games/typing-survival/src/content/guns.ts:133` | Có sẵn en: rail; tên hiện RAY cần tránh hiểu nhầm với Heat Beam. Biến thể: `Ray`. |
| `GUN.phao=4; phao` | PHÁO SAO | Star Mortar | pháo cối sao | Súng | **1 chỗ**; `games/typing-survival/src/content/guns.ts:134` | Theo tên Việt và title pháo cối nổ vùng. en hiện là flak; Claude xem việc đồng bộ nhãn EN ở thẻ thưởng tương lai, không đổi key phao. Biến thể: `Pháo Sao`. |
| `KIND.mine=0` | Bầy | Swarm | bầy quái | Loại quái | **17 chỗ**; `games/typing-survival/src/app/journey.ts:273,274`; `games/typing-survival/src/app/main.ts:244`; `games/typing-survival/src/app/results.ts:57`; `games/typing-survival/src/content/balance.ts:28,30`; `games/typing-survival/src/content/foes.ts:44`; `games/typing-survival/src/content/guns.ts:132,148,149`; `games/typing-survival/src/view/hud.ts:362,365`; `games/typing-survival/src/view/screens-journey.ts:21,23,24,33,38` | mine là id lịch sử; tên hiển thị trong FOES và bảng tin. Không gọi Mine vì không phải mìn; trùng từ gõ: 40 (B1 Intermediate 040; 040.json) |
| `KIND.scout=1` | Lính | Scout | lính trinh sát | Loại quái | **4 chỗ**; `games/typing-survival/src/app/journey.ts:275`; `games/typing-survival/src/content/foes.ts:45`; `games/typing-survival/src/content/guns.ts:150`; `games/typing-survival/src/view/screens-journey.ts:22` | Theo KIND.scout; đây là phe địch; trùng từ gõ: 18 (A2 Foundation 018; 018.json) |
| `KIND.brute=2` | Trâu | Brute | quái lực lưỡng | Loại quái | **6 chỗ**; `games/typing-survival/src/app/journey.ts:276`; `games/typing-survival/src/content/foes.ts:46`; `games/typing-survival/src/content/guns.ts:151`; `games/typing-survival/src/view/hud.ts:57`; `games/typing-survival/src/view/screens-journey.ts:17,23` | Theo KIND.brute; model là máy/quái, không tự suy thành Buffalo từ tên Việt; trùng từ gõ: 47 (B2 Upper Intermediate 047; 047.json) |
| `KIND.shield=3` | Khiên | Shield Guard | lính mang khiên | Loại quái | **6 chỗ**; `games/typing-survival/src/app/journey.ts:277`; `games/typing-survival/src/content/foes.ts:47`; `games/typing-survival/src/content/guns.ts:152`; `games/typing-survival/src/view/hud.ts:59`; `games/typing-survival/src/view/screens-journey.ts:17,25` | Phân biệt loại quái với lượng khiên trong mô tả. Các chữ khiên thường chỉ tấm chắn cần xem câu. |
| `KIND.splitter=4` | Tách | Splitter | quái tách mảnh | Loại quái | **5 chỗ**; `games/typing-survival/src/app/journey.ts:278`; `games/typing-survival/src/content/foes.ts:48`; `games/typing-survival/src/content/guns.ts:153`; `games/typing-survival/src/view/hud.ts:60`; `games/typing-survival/src/view/screens-journey.ts:26` | Đây là tên loại quái dù tiếng Việt trùng động từ; theo KIND.splitter; trùng từ gõ: 97 (Advanced 097; 097.json) |
| `KIND.shard=5` | Mảnh | Shard | mảnh quái nhỏ | Loại quái | **5 chỗ**; `games/typing-survival/src/app/journey.ts:278`; `games/typing-survival/src/content/foes.ts:49`; `games/typing-survival/src/content/guns.ts:153`; `games/typing-survival/src/view/hud.ts:60`; `games/typing-survival/src/view/screens-journey.ts:26` | Theo KIND.shard; rà cả mảnh trong bảng khắc chế; trùng từ gõ: 87 (C2 Advanced 087; 087.json) |
| `KIND.leader=6` | Đầu Đàn | Pack Leader | thủ lĩnh bầy | Loại quái | **10 chỗ**; `games/typing-survival/src/app/journey.ts:276,305`; `games/typing-survival/src/content/foes.ts:50`; `games/typing-survival/src/content/guns.ts:151`; `games/typing-survival/src/content/stage-rules.ts:62`; `games/typing-survival/src/view/hud.ts:58,362`; `games/typing-survival/src/view/screens-journey.ts:17,24,33` | Theo KIND.leader; nhiều con lặp lại trong mục tiêu Săn. Tên ải c1-s2 cũng là Đầu Đàn nhưng để Claude xem riêng; trùng từ gõ: 5 (A1 Foundation 005; 005.json) |
| `PILOT_NAMES.vanguard` | Vanguard | Vanguard | tàu tiên phong | Tàu | **1 chỗ**; `games/typing-survival/src/app/main.ts:68` | đã là tiếng Anh; giữ tên tàu, không cần đổi; trùng từ gõ: 42 (B1 Intermediate 042; 042.json) |
| `PILOT_NAMES.draconis` | Draconis | — | tàu mang tên Draconis | Nhân vật độc nhất | **1 chỗ**; `games/typing-survival/src/app/main.ts:68` | giữ tên riêng; trong game này là lựa chọn tàu |

### Cần Claude xem

| id trong mã | Tên Việt hiện tại | Tên tiếng Anh đề xuất | Nghĩa Việt ngắn (cho lần đầu) | Loại | Chỗ hiện (file:dòng, đếm số chỗ) | Ghi chú |
|---|---|---|---|---|---|---|
| `HAZARD_LABELS.rift` | Vết nứt | — | — | Hiểm họa | **6 chỗ**; `games/typing-survival/src/app/journey.ts:297`; `games/typing-survival/src/content/stage-rules.ts:63`; `games/typing-survival/src/view/hud.ts:379,382`; `games/typing-survival/src/view/screens-journey.ts:17,38` | Danh từ có thể thuộc vật thể hay tên luật; Claude chốt phạm vi trước khi dịch. |
| `FOES.armour` | Vỏ | — | — | Thuộc tính quái | **8 chỗ**; `games/typing-survival/src/app/journey.ts:276`; `games/typing-survival/src/app/main.ts:282,295`; `games/typing-survival/src/content/guns.ts:151`; `games/typing-survival/src/view/hud.ts:57,58`; `games/typing-survival/src/view/screens-journey.ts:23,24` | Giáp trừ sát thương, không phải vật phẩm; khác Giáp của tàu. |
| `SHIP.hp; w.hp` | GIÁP | — | — | Chỉ số sinh tồn | **6 chỗ**; `games/typing-survival/src/app/main.ts:179`; `games/typing-survival/src/view/hud.ts:131`; `games/typing-survival/src/view/screens-journey.ts:32,55,68,119` | HUD viết hoa; menu, kết quả và tiếp tế dùng Giáp/giáp. Biến thể: `Giáp`. |
| `view (title.lead)` | Bầy Hố Đen | — | — | Tên phe | **1 chỗ**; `games/typing-survival/src/app/main.ts:282` | Tên tập thể riêng trong lời giới thiệu, chưa tự dịch. |
| `OBJECTIVE_LABELS.hold` | Trụ vững | — | — | Mục tiêu | **4 chỗ**; `games/typing-survival/src/app/journey.ts:304`; `games/typing-survival/src/app/main.ts:189`; `games/typing-survival/src/content/stage-rules.ts:62`; `games/typing-survival/src/view/screens.ts:129` | Tên mục tiêu, không tự đổi. |
| `OBJECTIVE_LABELS.hunt` | Săn Đầu Đàn | — | — | Mục tiêu | **1 chỗ**; `games/typing-survival/src/content/stage-rules.ts:62` | Phần động từ Săn giữ Việt; danh từ quái bên trong theo hàng Leader nếu đổi. |
| `LEARN_RULES.standard` | Chuẩn | — | — | Luật học | **3 chỗ**; `games/typing-survival/src/app/main.ts:244`; `games/typing-survival/src/app/results.ts:82`; `games/typing-survival/src/content/stage-rules.ts:74` | Tên luật học, không phải băng đạn như trong thiết kế. |
| `LEARN_RULES.missing` | Thiếu chữ | — | — | Luật học | **2 chỗ**; `games/typing-survival/src/content/stage-rules.ts:75`; `games/typing-survival/src/view/screens-journey.ts:17` | Tên luật học. |
| `FORGE` | Rèn | — | — | Cơ chế nâng cấp | **4 chỗ**; `games/typing-survival/src/content/stage-rules.ts:149`; `games/typing-survival/src/view/screens-journey.ts:55,68,92` | Động từ/cấp nâng súng, chưa có cửa thưởng trong mã hiện đọc. |
| `Hud (bay === 2)` | MỐC | — | — | Mốc tiến trình | **1 chỗ**; `games/typing-survival/src/view/hud.ts:161` | Chuỗi MỞ Ở MỐC có trong HUD, cơ chế chương tương lai; không suy ra vật phẩm. |
| `renderJourney` | HÀNH LANG VC-7 | — | — | Tên vùng | **1 chỗ**; `games/typing-survival/src/view/screens-journey.ts:53` | Tên chương hiển thị trên screens-journey.ts. |
| `c1-s1` | Ca trực đầu | — | — | Tên ải | **1 chỗ**; `games/typing-survival/src/content/chapter-1.ts:41` | Tên ải 1. |
| `c1-s2` | Đầu Đàn | — | — | Tên ải | **1 chỗ**; `games/typing-survival/src/content/chapter-1.ts:59` | Trùng literal tên quái nhưng là stage.name; tránh đổi theo tìm-thay toàn cục. |
| `c1-s3` | Vách nứt | — | — | Tên ải | **1 chỗ**; `games/typing-survival/src/content/chapter-1.ts:76` | Tên ải 3 khác nhãn hiểm họa Vết nứt. |
| `c1-s4` | Khiên sáng | — | — | Tên ải | **1 chỗ**; `games/typing-survival/src/content/chapter-1.ts:93` | Tên ải 4, không tự đổi thành tên loại quái. |
| `s0` | Trận thử | — | — | Chế độ/ải | **5 chỗ**; `games/typing-survival/src/app/main.ts:229,295,304`; `games/typing-survival/src/content/guns.ts:130`; `games/typing-survival/src/content/stage-s0.ts:56` | Tên bản thử. |
| `journey` | Hành trình | — | — | Chế độ | **3 chỗ**; `games/typing-survival/src/app/main.ts:228,264`; `games/typing-survival/src/view/screens-journey.ts:52` | Tên luồng menu/chương. |
| `relax` | Thư giãn | — | — | Chế độ | **1 chỗ**; `games/typing-survival/src/content/balance.ts:28` | Tên chế độ. |
| `balanced` | Cân bằng | — | — | Chế độ | **1 chỗ**; `games/typing-survival/src/content/balance.ts:29` | Tên chế độ. |
| `challenge` | Thử thách | — | — | Chế độ | **1 chỗ**; `games/typing-survival/src/content/balance.ts:30` | Tên chế độ. |
| `SUPPORT; repaired` | TIẾP TẾ | — | — | Sự kiện | **1 chỗ**; `games/typing-survival/src/app/main.ts:179` | Tên lần hồi giáp; chưa có món tiếp tế có nhãn riêng. |
| `STAGE_S0; showBanner` | ĐỈNH TRÀN | — | — | Sự kiện | **3 chỗ**; `games/typing-survival/src/app/results.ts:57`; `games/typing-survival/src/content/balance.ts:30`; `games/typing-survival/src/view/hud.ts:271` | Tên nhịp tràn, không phải loại quái. |

### Tóm tắt

**12 tên phải đổi theo đề xuất; 2 tên giữ (1 tên riêng); 22 dòng chờ Claude.** Có **46 dòng mã khác nhau** cần sửa literal, tương ứng 60 lượt tên–dòng.

File có literal tên đề xuất đổi:

- `games/typing-survival/src/app/journey.ts`.
- `games/typing-survival/src/app/main.ts`.
- `games/typing-survival/src/app/results.ts`.
- `games/typing-survival/src/content/balance.ts`.
- `games/typing-survival/src/content/foes.ts`.
- `games/typing-survival/src/content/guns.ts`.
- `games/typing-survival/src/content/stage-rules.ts`.
- `games/typing-survival/src/view/hud.ts`.
- `games/typing-survival/src/view/screens-journey.ts`.

File tiêu thụ tên động cần rà cách rút gọn, độ rộng và nội suy khi đổi:

- `games/typing-survival/src/app/journey.ts`.
- `games/typing-survival/src/app/main.ts`.
- `games/typing-survival/src/view/hud.ts`.
- `games/typing-survival/src/view/screens.ts`.
- `games/typing-survival/src/view/screens-journey.ts`.

Test có tên/literal liên quan (kết quả tìm thô; chỉ sửa chỗ assert/fixture phụ thuộc chuỗi, không tự sửa logic):

- `games/typing-survival/tests/balance.test.ts` (đến dòng 6, 205, 208).
- `games/typing-survival/tests/gun-feel.test.ts` (đến dòng 44, 48, 59).
- `games/typing-survival/tests/guns.test.ts` (đến dòng 5, 20, 21, 45, 48, 90, 101, 103, 113, 119, 120, 138, 141, 161, 171, 173, 176, 181, 184, 198, 210, 211, 226, 238, 239, 242, 247, 270, 285, 286, 309, 321, 333, 334, 337, 346, 383, 452, 460, 469, 475, 476, 508, 530).
- `games/typing-survival/tests/overrides.test.ts` (đến dòng 5, 14, 16, 17, 25, 31, 32, 33, 68, 70, 71).
- `games/typing-survival/tests/ship-motion.test.ts` (đến dòng 27, 86, 116).
- `games/typing-survival/tests/stage-rules.test.ts` (đến dòng 42, 81, 269, 302).
- `games/typing-survival/tests/survival-sim.test.ts` (đến dòng 3, 22, 170, 184, 185, 186, 194, 204, 217, 218, 255, 261, 274, 285, 294, 305, 334, 336, 340, 341, 343, 369, 370, 452, 478, 479, 480, 481, 482, 502, 524, 531).
- `games/typing-survival/tests/survival/bot.ts` (đến dòng 3).
- `games/typing-survival/tests/survival/counters.ts` (đến dòng 10, 65, 72, 84, 104, 139).
- `games/typing-survival/tests/survival/tactics.ts` (đến dòng 5, 6).
- `games/typing-survival/tests/survival/typist-bot.ts` (đến dòng 11, 12, 13, 14, 40, 46, 47, 48, 51, 52, 56, 65, 67, 89, 97, 102).

Script kiểm/QA có nhắc tên: `games/typing-survival/scripts/balance.ts`; `games/typing-survival/scripts/overrides.ts`; `games/typing-survival/scripts/s0-trace.ts`; `games/typing-survival/scripts/visual/scenarios/survival-feel-guns.mjs`; `games/typing-survival/scripts/visual/scenarios/survival-feel-ship.mjs`; `games/typing-survival/scripts/visual/scenarios/survival-feel.mjs`; `games/typing-survival/scripts/visual/scenarios/survival-s0-boot.mjs`; `games/typing-survival/scripts/visual/scenarios/survival-s0-frames.mjs`; `games/typing-survival/scripts/visual/scenarios/survival-s0-lib.mjs`; `games/typing-survival/scripts/visual/scenarios/survival-s1-guns.mjs`; `games/typing-survival/scripts/visual/scenarios/survival-s1-latency.mjs`; `games/typing-survival/scripts/visual/scenarios/survival-s1-loadout.mjs`; `games/typing-survival/scripts/visual/scenarios/survival-s1-perf.mjs`; `games/typing-survival/scripts/visual/scenarios/survival-s1-stage.mjs`.

Golden/snapshot dữ liệu đã dò: `games/typing-survival/tests/golden/s0-trace.json`.
Golden/snapshot có chuỗi: **không tìm thấy literal tên cần đổi** trong golden/snapshot đang có. Không tạo lại golden ở phiếu này. Khi đổi tên thật, làn game cần kiểm xem hàm băm có gộp nội dung hiển thị hay không.

## Phần chưa có tên hiển thị trong mã


Đã đối chiếu tài liệu thiết kế và registry, nhưng không đưa nội dung tương lai vào số tên cần đổi:

- **Rồng Giữ Ải:** danh sách thiết kế rộng hơn bản mã M0 hiện tại (6 loại quái, 1 tướng). Chưa có literal UI cho tiền Vảy Rồng/Tri Thức, Lông Bạc, các bẫy/nhà/lính/món về sau và các boss thiết kế. Không gán tên Draconis từ tên file model cho Hỏa Long/Bạch Long.
- **Lời Gọi:** registry có `seal-dais`, các loại lính và nhiều quái chưa có tên trong `slice-1a.ts`/UI; không tự thêm Đài Ấn, Lính Giáo/Lính Khiên hay tên loại quái tương lai. Đại Bàng Tinh chưa là boss trong nội dung hiện tại; khi xuất hiện sẽ giữ tên riêng. Nuppeppō và Tanuki hiện là loại quái lặp lại, có thể đổi tên loài; Chấm, Phẩy, Gạch là cá thể có tên, giữ nguyên.
- **Tuyến Cuối:** mã đang có 4 ải của Chương 1 và Trận thử; chưa có literal UI cho Lõi Trạm, Tổ, Bão ion, Giếng hấp dẫn, Cai Ngục, Đòn Sập. Bọc Thép có trong chú thích `ELITE`, chưa có nhãn người chơi; không lấy chú thích làm bằng chứng hiển thị.
