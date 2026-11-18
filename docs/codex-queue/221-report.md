# Phiếu 221 · Wordwoven · Map 1 · Danh sách âm Adobe Firefly

Ngày 30/10/2026. Làm tại repo cha, nhánh hiện có `feat/space-typing-admin-uiux`. Chỉ lập danh sách SFX cho `w1-silverfall`; chưa tạo âm, chưa nghe duyệt, chưa gắn vào game.

## Kết quả giao

Đã viết [bản chủ dự án đọc](../games/audio/firefly/typing-defense.md), [JSON theo lược đồ chung](../games/audio/firefly/typing-defense.json), [tập id phát](221/fired-ids.json) và [script kiểm](221/check.mjs). Danh sách có **61 hàng · 85 lượt dự kiến**, P0 **43**, P1 **30**, P2 **12**. Một lượt là một file kết quả dự kiến, chưa suy ra số thao tác/credit. `retired` có **0** mục.

Nguồn game được đọc **chỉ bằng `git show`/`git grep` object `td-1c`**, không đọc file checkout hay mở worktree bị cấm. Commit `td-1c`: `2a1f61d7da2ee6e6ca4abdc23f8775f872d9c9e7`; `a2-days`: `f9abfd09987dadd519233c2f38692758d35cefca`. Checkout chính chỉ dùng lệnh branch/status/rev-parse để lưu trạng thái; không ghi `games/**`.

Có [source-evidence.json](221/source-evidence.json) lưu 30 thẻ đã đọc các trường when, purpose, prompt.text, duration, variants, playback; danh sách 65 id và nhóm tạo. [source-checks.txt](221/source-checks.txt) giữ các lượt grep âm nền, emitter và stdout xác nhận phím sai ở `646e889` (lệnh log đó chạy đúng **1 lần**). [make-data.mjs](221/make-data.mjs) dựng lại JSON/Markdown/fired-ids từ dữ liệu biên tập; [make-report.py](221/make-report.py) dựng báo cáo và chụp trạng thái, đều chỉ ghi trong phạm vi phiếu.

Đối chiếu pha bằng skill [game-vfx-layered](../../.agents/skills/game-vfx-layered/SKILL.md), VFX_STANDARD §3.1/§3.4; chỉ đọc mã và ghi ý đồ, không dựng VFX, không capture hay tuyên bố nghiệm thu hình/nghe. Các bước sửa game, changelog và kiểm hình của skill nằm ngoài phiếu chỉ viết danh sách, nên không thực hiện.

## Điều kiện trước

**6/6 đạt**, đầu ra từng lệnh ở [preconditions.txt](221/preconditions.txt). Commit chung 212 là `83217b53870b330d345d1ee8a97f82e0adee757d`. Đủ 5 hàm export, các trường cấp file và 3 trường hàng tùy chọn. Game `a2-days` sạch; `td-1c` resolve đúng mã. Có **30** thẻ. Ba đường đích chưa tồn tại trước khi tạo `221/`. Ba MD5 trước/sau đều khớp:

| File chỉ đọc | MD5 cuối, giống trước |
|---|---|
| `docs/games/audio/firefly/schema.json` | `c37879d9b6b4a85470c10b92f937b538` |
| `docs/codex-queue/212/check.mjs` | `ffbeee75450361fe957bd6d4493cbc7d` |
| `docs/games/audio/firefly/README.md` | `c0732e449f7e5e087460b796d686bb54` |

## Bảy mục kiểm có số

| Mục | Số và kết quả |
|---|---|
| 1. Script kiểm thường | **Thoát 0**; thiếu **0**, lạ **0**, trùng **0**, lược đồ **0**, phép tính **0**, lệch thẻ **0**, ASCII prompt/tên **0/0**, tên riêng **0**, từ cấm **0**, phủ định **0**, cồng thiếu lý do **0**, lệch Markdown/JSON **0**. Xem nguyên stdout bên dưới. |
| 2. Selftest | **Thoát 0; bắt 3/3**: bỏ hàng map1=true, thêm id lạ, thêm chữ có dấu. Chỉ cài lỗi vào bản chép trong bộ nhớ. |
| 3. Tập id và sản lượng | **62/65** id mã có đường phát ở map 1; **0** id phát thêm; hợp mã/thẻ **71** id. **61** hàng, **10** excluded, **0** retired. Bảng nhóm và lý do loại ở dưới. P0 **43**, P1 **30**, P2 **12**, tổng **85** lượt. Prompt dài nhất `word-hit`: **463 ký tự ASCII**. |
| 4. Truy số về thẻ/mã | **23** hàng có thẻ, giữ nguyên min_ms/max_ms/variants.target; **38** hàng specCard=null có đề xuất số và căn cứ file:dòng trong basis. Tất cả **61** hàng có targetMs, variants và basis; **0** lệch số thẻ. Các số không thẻ là quyết định biên tập dựa nhịp sự kiện, không giả làm hằng số âm có sẵn. |
| 5. Commit nguồn | `td-1c` **2a1f61d7da2ee6e6ca4abdc23f8775f872d9c9e7**; `a2-days` **f9abfd09987dadd519233c2f38692758d35cefca**; script đọc lại refs, **0** lệch. Claude chạy lại sau khi merge hoặc ref đổi; phải rà căn cứ trước khi cập nhật hash. |
| 6. Checkout game trước/sau | **Đạt**, game-before và game-after giống từng byte. Nhánh `a2-days`; **0** dòng status sau. Phiếu này ghi **0** đường trong games/**. |
| 7. Repo cha trước/sau | Trước **1205**, sau **1306** dòng status. Phiếu thêm **19** file, chỉ trong 4 gốc được cho phép. Có **82** dòng thêm/đổi và **0** dòng mất/đổi ngoài phạm vi do làn đồng thời; liệt kê dưới, không chạm vào. |

### Ngoại lệ bắt buộc từ chính phiếu

Mục 1 đòi `map1` phản ánh khả năng phát; mục 6 lại bắt buộc **key-right vào excluded** vì thuộc bộ 189–193. Do đó giữ `key-right.map1=true` (không khai sai thành false), excluded có `firstStage=w1-silverfall`; luật “map1=true phải là rows” có đúng **1 ngoại lệ nguồn**, được công khai trong check.txt/check.json và script. **61** id map1 còn lại đều là hàng. Nếu áp nguyên văn cả hai mệnh đề mà không có ngoại lệ thì không thể đồng thời thỏa; Claude/chủ dự án cần xem quyết định này. Kiểm thường vẫn báo 0 lỗi theo chính sách nguồn cụ thể ở mục 6.

### Nhóm buổi tạo

| Nhóm | Hàng | Lượt |
|---|---:|---:|
| gõ và lời gọi | 16 | 25 |
| đạn, trúng, chết | 13 | 25 |
| boss Mộc Tinh | 12 | 14 |
| ngày và đêm | 8 | 8 |
| công trình và kinh tế | 8 | 9 |
| UI và nền | 4 | 4 |

Mỗi id rows thuộc đúng một nhóm. UI và nền có **4 UI**, **0** nền loop; toàn danh sách **60** hits, **1** single (`boss-lull`), **0** loop.

### Loại theo lý do

| Lý do | Id |
|---|---:|
| Phím đúng thuộc 189–193 | 1 |
| Loài chỉ ở hộp cát, chưa có ải truyện | 2 |
| Có khóa registry nhưng chưa có emitter | 1 |
| Giọng người do chủ dự án ghi | 1 |
| Nền chỉ có thẻ, chưa có mã phát | 1 |
| Nhạc theo đường riêng | 4 |

Hai id ngoài sóng truyện: `direct-pin` (Zombie Leader), `direct-shield` (Troll), chưa có ải đầu nên firstStage=null. Không suy đoán map sau. `amb-dusk` chỉ có thẻ: grep `amb-` **0 dòng**, grep `dusk` **6 dòng** chỉ màu/ảnh. Bốn music-* theo đường nhạc riêng ở `src/view/music.ts`, không thành hàng SFX.

**Phát hiện so với dự kiến đầu phiếu:** `feather-fall` chỉ có khóa FIRES (sound-map.ts:13), `ult.drop` (ult.ts:102–110) gọi P.add trực tiếp; P.add (projectiles.ts:33–46) không đẩy ring. Toàn src chỉ `combat.ts:86` đẩy FX.fire, và lông không đi qua launch đó. Vì vậy **map1=false, firstStage=null**, không tạo hàng giả. Lông lửa vẫn rơi và phát `blast` lúc chạm. Thời gian bay lông được ghi ở excluded.basis cho phiếu gắn: SPEED=12 m/s, FROM dài 9,6 m, fallS=0,8 s, khoảng **48 khung** với đích đứng yên. Không sửa mã để mở id trong phiếu này.

38 hàng không thẻ: `key-lock`, `key-group`, `chain-step`, `chain-tier`, `call-ult`, `call-direct`, `cannon-fire`, `bolt-fire`, `fireball-fire`, `hit`, `block`, `soldier-down`, `fizzle`, `direct-break`, `ult-cast`, `boss-warn`, `boss-lull`, `boss-emerge`, `boss-phase`, `boss-roots`, `boss-roots-hit`, `boss-slam`, `boss-drain`, `boss-drain-hit`, `boss-summon`, `boss-hit`, `boss-retreat`, `day-countdown`, `wave-start`, `night-called`, `victory`, `build-start`, `build-done`, `sell`, `house-stun`, `harvest-done`, `tree-fall`, `helper-panic`.

## Nguyên stdout kiểm

```text
PASS · Phiếu 221
SOUND_IDS=65; extra=0; spec=30; union=71
map1Fired=62; rows=61; excluded=10; retired=0
map1PolicyException=key-right (mục 6: bộ phím 189–193)
missing=0
unknown=0
duplicates=0
schemaErrors=0
firedErrors=0
map1Errors=0
calculationErrors=0
loopErrors=0
inboxErrors=0
specErrors=0
asciiPromptErrors=0
asciiNameErrors=0
properNameErrors=0
bannedErrors=0
negativeErrors=0
gongErrors=0
markdownErrors=0
busErrors=0
sourceCommitErrors=0
basisErrors=0
takes=85; P0=43; P1=30; P2=12
withSpec=23; withoutSpec=38
longestPrompt=word-hit: 463 ASCII characters
```

## Nguyên stdout selftest

```text
PASS · Phiếu 221
SOUND_IDS=65; extra=0; spec=30; union=71
map1Fired=62; rows=61; excluded=10; retired=0
map1PolicyException=key-right (mục 6: bộ phím 189–193)
missing=0
unknown=0
duplicates=0
schemaErrors=0
firedErrors=0
map1Errors=0
calculationErrors=0
loopErrors=0
inboxErrors=0
specErrors=0
asciiPromptErrors=0
asciiNameErrors=0
properNameErrors=0
bannedErrors=0
negativeErrors=0
gongErrors=0
markdownErrors=0
busErrors=0
sourceCommitErrors=0
basisErrors=0
takes=85; P0=43; P1=30; P2=12
withSpec=23; withoutSpec=38
longestPrompt=word-hit: 463 ASCII characters
CAUGHT bỏ hàng map1=true
CAUGHT thêm id lạ
CAUGHT thêm chữ có dấu
selftest=3/3
```

Kết quả máy đọc ở [check.json](221/check.json) và [check-selftest.json](221/check-selftest.json). Validator import của 212 kiểm đúng tập từ khóa lược đồ đang dùng; import không chạy CLI 212, MD5 file 212 không đổi. Phủ id được tự kiểm, **không dùng audit 212**, nên sáu id chỉ có thẻ được excluded đúng phạm vi.

## fired-ids rút gọn (65/65)

Đường trong trigger và map1Basis tính từ gốc object `td-1c`, không phải dòng của checkout `a2-days`. `map1=true` nghĩa có đường gọi âm khi đủ điều kiện, không phải luôn phát mọi ván và không phải đã có file thật. `bus` giữ đúng busOf: `wordshot-fire` là world, khác họ `word-*` có dấu gạch. `sourceEvent`, `firstStage` và đầy đủ căn cứ nằm trong JSON.

| Id | map1 | Trigger td-1c | Lý do loại / nơi xử lý |
|---|---|---|---|
| `call-power` | true | `src/view/sound-map.ts:12,36` | —; rows |
| `call-build` | true | `src/view/sound-map.ts:12,36` | —; rows |
| `call-harvest` | true | `src/view/sound-map.ts:12,36` | —; rows |
| `call-chop` | true | `src/view/sound-map.ts:12,36` | —; rows |
| `call-mine` | true | `src/view/sound-map.ts:12,36` | —; rows |
| `call-quiz` | true | `src/view/sound-map.ts:12,36` | —; rows |
| `key-right` | true | `src/view/sound-map.ts:37` | Phím đúng phát ở map 1 nhưng loại khỏi Firefly theo mục 6: thuộc các bộ tiếng phím 189–193; §8.2 giữ synth. |
| `key-wrong` | true | `src/view/sound-map.ts:37` | —; rows |
| `word-hit` | true | `src/view/sound-map.ts:38` | —; rows |
| `word-hit-bell` | true | `src/view/sound-map.ts:38` | —; rows |
| `chain-callout` | true | `src/view/sound-map.ts:39` | —; rows |
| `wordshot-fire` | true | `src/view/sound-map.ts:13,48 (FIRES)` | —; rows |
| `arrow-fire` | true | `src/view/sound-map.ts:13,48 (FIRES)` | —; rows |
| `blast` | true | `src/view/sound-map.ts:14,48 (RING)` | —; rows |
| `ink-puff` | true | `src/view/sound-map.ts:14,48 (RING)` | —; rows |
| `coin` | true | `src/view/sound-map.ts:14,48 (RING)` | —; rows |
| `leak` | true | `src/view/sound-map.ts:14,48 (RING)` | —; rows |
| `night-fall` | true | `src/view/sound-map.ts:40` | —; rows |
| `dawn` | true | `src/view/sound-map.ts:40` | —; rows |
| `defeat` | true | `src/view/sound-map.ts:27 (ONE)` | —; rows |
| `day-countdown` | true | `src/view/audio-min.ts:114` | —; rows |
| `direct-break` | true | `src/view/sound-map.ts:41` | —; rows |
| `direct-pin` | false | `src/view/sound-map.ts:41` | Zombie Leader chỉ có trong hộp cát, không nằm trong năm đêm của map 1; chưa có ải truyện mở. |
| `direct-shield` | false | `src/view/sound-map.ts:41` | Troll chỉ có trong hộp cát, không nằm trong năm đêm của map 1; chưa có ải truyện mở. |
| `helper-panic` | true | `src/view/sound-map.ts:27 (ONE)` | —; rows |
| `boss-warn` | true | `src/view/sound-map.ts:27 (ONE)` | —; rows |
| `boss-lull` | true | `src/view/sound-map.ts:27 (ONE)` | —; rows |
| `boss-emerge` | true | `src/view/sound-map.ts:27 (ONE)` | —; rows |
| `boss-phase` | true | `src/view/sound-map.ts:27 (ONE)` | —; rows |
| `boss-roots` | true | `src/view/sound-map.ts:43` | —; rows |
| `boss-roots-hit` | true | `src/view/sound-map.ts:43` | —; rows |
| `boss-slam` | true | `src/view/sound-map.ts:44` | —; rows |
| `boss-drain` | true | `src/view/sound-map.ts:43` | —; rows |
| `boss-drain-hit` | true | `src/view/sound-map.ts:43` | —; rows |
| `boss-retreat` | true | `src/view/sound-map.ts:27 (ONE)` | —; rows |
| `ui-move` | true | `src/view/audio-min.ts:127–129` | —; rows |
| `ui-pick` | true | `src/view/audio-min.ts:127–129` | —; rows |
| `ui-off` | true | `src/view/audio-min.ts:127–129` | —; rows |
| `ui-lamp` | true | `src/view/audio-min.ts:127–129` | —; rows |
| `key-lock` | true | `src/view/sound-map.ts:37` | —; rows |
| `key-group` | true | `src/view/sound-map.ts:37` | —; rows |
| `chain-step` | true | `src/view/sound-map.ts:39` | —; rows |
| `chain-tier` | true | `src/view/sound-map.ts:39` | —; rows |
| `call-ult` | true | `src/view/sound-map.ts:12,36` | —; rows |
| `call-direct` | true | `src/view/sound-map.ts:12,36` | —; rows |
| `cannon-fire` | true | `src/view/sound-map.ts:13,48 (FIRES)` | —; rows |
| `bolt-fire` | true | `src/view/sound-map.ts:13,48 (FIRES)` | —; rows |
| `fireball-fire` | true | `src/view/sound-map.ts:13,48 (FIRES)` | —; rows |
| `feather-fall` | false | `src/view/sound-map.ts:13,48 (FIRES)` | Có khóa FIRES nhưng chưa có đường phát: ult.drop thêm PROJECTILE.feather bằng P.add trực tiếp, không đẩy FX.fire. Chưa ải nào phát id; không đồng nghĩa không có lông lửa. |
| `hit` | true | `src/view/sound-map.ts:14,48 (RING)` | —; rows |
| `block` | true | `src/view/sound-map.ts:14,48 (RING)` | —; rows |
| `soldier-down` | true | `src/view/sound-map.ts:14,48 (RING)` | —; rows |
| `fizzle` | true | `src/view/sound-map.ts:14,48 (RING)` | —; rows |
| `boss-hit` | true | `src/view/sound-map.ts:14,48 (RING)` | —; rows |
| `boss-summon` | true | `src/view/sound-map.ts:44` | —; rows |
| `build-start` | true | `src/view/sound-map.ts:28 (ONE)` | —; rows |
| `build-done` | true | `src/view/sound-map.ts:28 (ONE)` | —; rows |
| `sell` | true | `src/view/sound-map.ts:28 (ONE)` | —; rows |
| `house-stun` | true | `src/view/sound-map.ts:28 (ONE)` | —; rows |
| `ult-cast` | true | `src/view/sound-map.ts:28 (ONE)` | —; rows |
| `wave-start` | true | `src/view/sound-map.ts:28 (ONE)` | —; rows |
| `night-called` | true | `src/view/sound-map.ts:28 (ONE)` | —; rows |
| `harvest-done` | true | `src/view/sound-map.ts:29 (ONE)` | —; rows |
| `tree-fall` | true | `src/view/sound-map.ts:29 (ONE)` | —; rows |
| `victory` | true | `src/view/sound-map.ts:28 (ONE)` | —; rows |

`day-countdown` và **4** id `ui-*` đều đã có trong SOUND_IDS.made, nên phát thêm **0**. Tiếng gọi màn tựa gọi goi trực tiếp không có id, được giải thích riêng dưới, không bịa entry trong fired-ids.

## Âm có cồng, chủ dự án ký duyệt

Theo AUDIO_PIPELINE §8.2, mỗi âm có cồng phải được chủ dự án duyệt riêng; chưa coi danh sách hay validator là đã nghe duyệt.

| Hàng | Lý do |
|---|---|
| `night-fall` | gong: báo nguy trang nghiêm khi đêm xuống; giữ cồng theo thẻ nhưng chuyển quy mô sang thung lũng đá vôi §2; chủ dự án duyệt riêng. |
| `leak` | gong: báo nguy Fort mất mạng, đúng §8.2; chủ dự án duyệt riêng. |
| `defeat` | gong: khoảnh khắc trang trọng kết trận thất thủ; chủ dự án duyệt riêng. |

**3 hàng**, mỗi eraNote chứa `gong:`. Các tiếng báo khác chọn kẻng sắt/trống hội; boss-phase bỏ cồng của mã cũ, giữ nứt vỏ gỗ và chuông đồng nhỏ để không dùng cồng tùy tiện.

## Việc ghi âm của chủ dự án, ngoài Firefly

**amb-villager-call — giọng người, chủ dự án ghi âm.** AUDIO_PIPELINE §3.2 **dòng 129**: chủ dự án/người nhà ghi **4 biến thể**, có giấy đồng ý, không dùng AI. Thẻ `tools/audio-lab/specs/typing-defense/amb-villager-call.yaml:13,96,102,170` ghi voice, owner-recording, chặn bởi chủ dự án ghi âm và giấy đồng ý. Không có prompt Firefly cho mục này.

Mã **vẫn có** tiếng gọi tổng hợp ở màn tựa: `src/view/audio-min.ts:119–124` gọi `goi` mỗi **3–7 s**, trái/phải, qua `src/view/folk.ts:135` mà không qua id. Phiếu gắn sau phải cho tiếng này đi qua **amb-villager-call** rồi dùng bản ghi thật. `firstStage=null` ở excluded nghĩa chưa có ải phát nó qua id, không phải màn tựa đang im. Không sửa hay tạo âm thay thế ở phiếu 221.

## Chọn chất liệu khi thẻ cũ lệch bible

ART_DIRECTION §2 và cột “Tiếng bible đòi” §8.2 thắng thẻ/THEME_SOUND_LIST về cách diễn; độ dài và biến thể vẫn giữ thẻ. Hướng mới là **cõi đá vôi huyền ảo hùng vĩ**, không gian sân đá và thung lũng; giữ độ nhỏ của phím, UI và cung, không biến mọi nguồn thành tiếng boss. Luật cứng AUDIO_PIPELINE §8.2/TK 22.1 giữ nguyên. Prompt khẳng định, ASCII, không tên riêng, không âm tôn giáo, không chất liệu điện tử hay nhạc cụ nước khác dán nhãn Việt; sáo là ống mở sạch, không rè màng.

| Hàng/họ | Khác nguồn cũ | Cách chọn |
|---|---|---|
| word-hit | Thẻ/THEME_SOUND_LIST:32 dùng đàn tranh | Chuyển chuông đồng nhỏ theo §8.2; giữ **640–960 ms**, **7** biến thể, 6 cao độ + 1 luyến là đề xuất chưa phải ngân hàng engine theo nốt. |
| call-harvest / Reap | Thẻ dùng chuông | Theo §8.2 chọn liềm cắt và sột lúa; giữ **720–1080 ms**, **1** biến thể. |
| call-quiz / Quiz | Thẻ dùng sáo | Chọn chuông theo chuỗi chất liệu lời gọi của §8.2; giữ **280–420 ms**, **1** biến thể. |
| dawn | Thẻ/THEME_SOUND_LIST:47 là câu sáo | Chọn gà gáy xa và gió bình minh theo §8.2; **800–1200 ms**, **1** biến thể. Gà là động vật, không phải giọng người. |
| key-wrong | Thẻ nói giữ tổng hợp | Mục 6 giữ hàng riêng; phách tre lệch theo §8.2, **32–48 ms**, **2** biến thể; log 646e889 xác nhận tiếng phím sai riêng. |
| UI, coin | Thanh tre/khay gỗ làng nhỏ | UI dùng gỗ sơn mài, giấy, đồng nhỏ theo §2/§8.2; coin chạm khay gỗ sơn mài. |
| wordshot-fire, arrow-fire, blast, ink-puff | Đuôi vang làng, nổ trống/giấy chung | Đuôi thung lũng đá vôi ngắn/thấp, Word Shot thêm ting cao; blast nổ ba lớp và mảnh đá; giữ số thẻ. ink-puff vẫn là id chết chung, không giả có âm từng loài. |
| Boss, direct-break, helper-panic | Chuông/cồng hoặc gõ ngắn của SYNTH | Gỗ cổ thụ/rễ/đá đúng cỡ boss; ngắt là trống ngừng, Helper chân/lông. Không thêm lời hô người vào prompt. |

`era=kept` ở word-hit-bell vì giữ cách diễn chuông của thẻ; các hàng còn lại `reworded` ghi đổi quy mô/chất liệu hoặc là đề xuất chưa có thẻ. Không sửa thẻ cũ, THEME_SOUND_LIST, README hay schema.

## Nhịp VFX và giới hạn tích hợp

- **Fort:** 34 m/s, 9 m → khoảng **265 ms**, **16 khung**. **Archer Tower:** 30 m/s, 10/11/12 m → **333/367/400 ms**, **20/22/24 khung**. **Cannon Tower:** 18 m/s, 9/9,5/10 m → **500/528/556 ms**, **30/32/34 khung**. Nguồn slice-1a.ts:25–30,41–59, compile.ts:42.
- **Word Shot:** rewards.ts:55 dùng attack của tháp, không có tốc độ riêng: cùng dải **333–400 ms** hoặc **500–556 ms**. Fort đi bolt (rewards.ts:51). **Draconis:** 20 m/s, 9 m → **450 ms**, **27 khung** (slice-1a.ts:148, agents.ts:166). Đây là ước tính rìa tầm, đích đứng yên; sim theo đích di chuyển và tick, không phải độ trễ mới.
- **Trúng/chết:** FX.hit khi tới đích đơn còn sống, FX.burst khi splash tới điểm, FX.death khi chết. R ở nguồn phải trước I; chuẩn bị đòn chữ trong gõ, không đợi file chạy hết.
- **Boss:** roots **1,5 s/90 khung**; slam và keep **1,2 s/72 khung**; drain **1,2 s/72 khung**, đều nhân warnK (relax/learn **1,33**, balanced **1**, challenge **0,8**) rồi quy tick. Summon **0,8 s/48 khung** không nhân warnK. Cửa sổ có thể dưới mức boss ≥72 khung của VFX_STANDARD §3.4; chỉ ghi hiện trạng, không đổi sim. boss-slam dùng cả keep hit; slam/keep báo đầu hiện không trả id. boss-summon hiện cùng id cả báo và chạm. drain-hit có thể chồng leak cùng tick. Phiếu gắn phải xử lý chọn/cắt và nghe chồng, không suy diễn prompt là đã tích hợp đúng.
- **61/61** hàng có `clips=[]`, cùng clipsWhy “docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven”. Đọc FxPool tuổi 0/đuôi, FxPipe, fx-2d và boss-2d chỉ cho căn cứ view; chưa có clip Wordwoven để ghép.

## Bible đòi nhưng mã chưa có id

Đây là danh sách cho phiếu gắn/thiết kế sau, **0 hàng bổ sung** ở JSON:

- Tiếng riêng theo từng loài khi ra, đi (loop), đánh, trúng và chết; Hopping Zombie, Ghost Flame, River Serpent, Sapling, Raccoon Dog, Split Blob và Little Blob. hit/ink-puff còn dùng chung.
- Phân pha và chất liệu đủ 5 pha của Fort/Archer Tower/Cannon Tower; tiếng cung cắm, nổ ba lớp riêng pháo, lửa hai lớp riêng Draconis hiện còn dùng chung các id.
- Draconis nón lửa/gầm riêng; trống tăng theo tiến độ Spell; mở emitter cho feather-fall nếu muốn file từng lông. Đã có id registry nên không bịa thêm id thay nó.
- Báo trước slam/keep riêng; phân âm báo và lúc mọc Sapling của summon. Không thêm chờ vào sim.
- Lính đâm giáo/hô ghi thật; Helper từng nhịp chân/giọng ghi; công trình bị đánh, đổ nát và sửa riêng ngoài các id chung đã có.
- Nền thác/gió/chim theo cõi đá vôi, không lấy thẻ amb-dusk là đã phát. Seal Dais, Herb House, Lumber Camp ngoài sáu công trình map 1 nên chỉ nêu thiếu, không mở hàng.
- amb-villager-call theo đường chủ dự án ghi âm và giấy đồng ý, không Firefly.

## Firefly còn chưa biết

Giống README 212: **giới hạn ký tự prompt**, tùy chọn và phạm vi **độ dài file**, **số kết quả mỗi lượt thao tác/credit**, giới hạn tốc độ, hiệu quả gợi ý giọng, khả năng cắt loop liền, tỷ lệ dùng được và chất lượng khi lặp dày. Lô 189 từng xuất WAV **48 kHz stereo 16-bit khoảng 12 s** chỉ là quan sát của lô đó; không xác minh mới bằng mạng, không coi là giới hạn sản phẩm. **75%** dùng được là giả định, cần sửa sau lượt đầu. Prompt dài nhất **463** ký tự chưa được thử trên giao diện. Không phát sinh file âm hoặc thư mục inbox.

## Trạng thái trước/sau và phạm vi ghi

[game-before.txt](221/game-before.txt) và [game-after.txt](221/game-after.txt): **giống từng byte**.

```text
a2-days
```

Ảnh chụp repo cha đầy đủ: [status-before.txt](221/status-before.txt), [status-after.txt](221/status-after.txt), đối chiếu [state-check.json](221/state-check.json). Repo vốn bẩn; không dọn thay đổi của làn khác. Những dòng mới thuộc phiếu:

```text
?? docs/codex-queue/221-report.md
?? docs/codex-queue/221/check-selftest.json
?? docs/codex-queue/221/check-selftest.txt
?? docs/codex-queue/221/check.json
?? docs/codex-queue/221/check.mjs
?? docs/codex-queue/221/check.txt
?? docs/codex-queue/221/fired-ids.json
?? docs/codex-queue/221/game-after.txt
?? docs/codex-queue/221/game-before.txt
?? docs/codex-queue/221/make-data.mjs
?? docs/codex-queue/221/make-report.py
?? docs/codex-queue/221/preconditions.txt
?? docs/codex-queue/221/source-checks.txt
?? docs/codex-queue/221/source-evidence.json
?? docs/codex-queue/221/state-check.json
?? docs/codex-queue/221/status-after.txt
?? docs/codex-queue/221/status-before.txt
?? docs/games/audio/firefly/typing-defense.json
?? docs/games/audio/firefly/typing-defense.md
```

Ngoài phạm vi, thêm/đổi hoặc mất/đổi so với ảnh chụp đầu (liệt kê nguyên từng đường, không khẳng định nội dung của làn khác):

```text
?? docs/codex-queue/199/build-second.json
?? docs/codex-queue/199/decoded-dimensions.json
?? docs/codex-queue/199/manifest-final.json
?? docs/codex-queue/199/media-push.json
?? docs/codex-queue/199/preflight-1328.json
?? docs/codex-queue/199/prune-1328-apply.json
?? docs/codex-queue/199/prune-1328-dry.json
?? docs/codex-queue/199/test-first-1328.md
?? docs/codex-queue/202/manifest-contract.json
?? docs/codex-queue/220/chapter-after.txt
?? docs/codex-queue/220/chapter-before.txt
?? docs/codex-queue/220/decision.md
?? docs/codex-queue/220/evidence/chapter-diff.exit
?? docs/codex-queue/220/evidence/chapter.diff
?? docs/codex-queue/220/evidence/golden-after.txt
?? docs/codex-queue/220/evidence/golden-before.txt
?? docs/codex-queue/220/evidence/parent-status-before.txt
?? docs/codex-queue/220/evidence/restricted-hunks.diff
?? docs/codex-queue/220/evidence/v6-repro.json
?? docs/codex-queue/220/evidence/wave-A.json
?? docs/codex-queue/220/evidence/wave-B.json
?? docs/codex-queue/220/evidence/wave-C.json
?? docs/codex-queue/220/evidence/wave-repro.json
?? docs/codex-queue/220/evidence/worktree.commit
?? docs/codex-queue/220/logs/check-after-initial.txt
?? docs/codex-queue/220/logs/check-after.exit
?? docs/codex-queue/220/logs/check-after.txt
?? docs/codex-queue/220/logs/check-before.exit
?? docs/codex-queue/220/logs/check-before.txt
?? docs/codex-queue/220/logs/mutations.txt
?? docs/codex-queue/220/logs/summarize-A.txt
?? docs/codex-queue/220/logs/summarize-B.txt
?? docs/codex-queue/220/logs/summarize-initial.txt
?? docs/codex-queue/220/logs/tests-green.exit
?? docs/codex-queue/220/logs/tests-green.txt
?? docs/codex-queue/220/logs/tests-red.exit
?? docs/codex-queue/220/logs/tests-red.txt
?? docs/codex-queue/220/logs/wave-A.txt
?? docs/codex-queue/220/logs/wave-B.txt
?? docs/codex-queue/220/logs/wave-C.txt
?? docs/codex-queue/220/logs/wave-repro.txt
?? docs/codex-queue/220/method.md
?? docs/codex-queue/220/runs/f1-s1.err
?? docs/codex-queue/220/runs/f1-s1.json
?? docs/codex-queue/220/runs/f1-s1.md
?? docs/codex-queue/220/runs/f1-s101.err
?? docs/codex-queue/220/runs/f1-s101.json
?? docs/codex-queue/220/runs/f1-s101.md
?? docs/codex-queue/220/runs/f2-s1.err
?? docs/codex-queue/220/runs/f2-s1.json
?? docs/codex-queue/220/runs/f2-s1.md
?? docs/codex-queue/220/runs/f2-s101.err
?? docs/codex-queue/220/runs/f2-s101.json
?? docs/codex-queue/220/runs/f2-s101.md
?? docs/codex-queue/220/runs/f3-s1.err
?? docs/codex-queue/220/runs/f3-s1.json
?? docs/codex-queue/220/runs/f3-s1.md
?? docs/codex-queue/220/runs/f3-s101.err
?? docs/codex-queue/220/runs/f3-s101.json
?? docs/codex-queue/220/runs/f3-s101.md
?? docs/codex-queue/220/runs/f4-s1.err
?? docs/codex-queue/220/runs/f4-s1.json
?? docs/codex-queue/220/runs/f4-s1.md
?? docs/codex-queue/220/runs/f4-s101.err
?? docs/codex-queue/220/runs/f4-s101.json
?? docs/codex-queue/220/runs/f4-s101.md
?? docs/codex-queue/220/runs/v6-s1.err
?? docs/codex-queue/220/runs/v6-s1.json
?? docs/codex-queue/220/runs/v6-s1.md
?? docs/codex-queue/220/runs/v6-s101.err
?? docs/codex-queue/220/runs/v6-s101.json
?? docs/codex-queue/220/runs/v6-s101.md
?? docs/codex-queue/220/start.txt
?? docs/codex-queue/220/summary.json
?? docs/codex-queue/220/summary.md
?? docs/codex-queue/220/tools/changes-from-209.diff
?? docs/codex-queue/220/tools/compare.py
?? docs/codex-queue/220/tools/run-wave.mjs
?? docs/codex-queue/220/tools/summarize.mjs
?? docs/codex-queue/220/tools/verify.py
?? docs/codex-queue/220/tools/write-report.py
?? docs/codex-queue/220/variants.json
```

Không chạy Git có ghi, không commit/push/reset/clean/stash; không đổi nhánh, không worktree; không mạng, dev server, trình duyệt, build hay test suite game. Không mở làn bị cấm, không chạm Tu Tiên, không sửa tools/** hoặc shared/**. Không tạo ảnh vì phiếu chỉ lập danh sách âm; không tạo/tải/sửa âm vì chủ dự án tự tạo SFX và tự ghi giọng người. **Claude duyệt rồi commit**, sau đó chủ dự án dùng Markdown để tạo âm; các mục cồng, ngoại lệ key-right và emitter feather-fall cần được đọc trước khi giao lô.
