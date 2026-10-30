# Phiếu 213 · Dragonhold · Danh sách âm Firefly ghép clip lửa

Ngày 30/10/2026. Đã lập **116 hàng, 192 lượt dự kiến**, theo schema và công thức phiếu 212. Lửa có **9 hàng / 25 lượt**, đứng đầu danh sách để chủ dự án nghe cùng clip. Chưa tạo âm, chưa nghe duyệt, chưa gắn vào game; cổng G3 chưa được nghiệm thu.

## File giao

- [dragon-hold.md](../games/audio/firefly/dragon-hold.md): tám buổi tạo, tên tiếng Anh, khi phát, catalog/targetMs, mono/stereo, vòng lặp, biến thể/lượt, prompt nguyên văn, gợi ý diễn, clip/pha và inbox.
- [dragon-hold.json](../games/audio/firefly/dragon-hold.json): cùng tập hàng và prompt, đúng schema 212; sourceCommits main `1f1de48`, dh-vfx `ca64509`.
- [213/fired-ids.json](213/fired-ids.json): 115 id có đường phát theo mã trên hợp hai nhánh; 82 catalog (gồm type.key bị loại) + 33 id file riêng có điều kiện; hai id manifest-only ghi riêng. [callsite-inventory.json](213/callsite-inventory.json) giữ toàn bộ push/at/bed/play đã dò trong hai file, trên cả hai nhánh.
- [213/check.mjs](213/check.mjs), [check.txt](213/check.txt), [check.json](213/check.json), [check-selftest.txt](213/check-selftest.txt), [check-selftest.json](213/check-selftest.json): validator, phép tính, đối chiếu nguồn/thẻ/Markdown và selftest.
- Bằng chứng tại [213/](213/): source-snapshot.json giữ git object đã đọc; spec-evidence.json chỉ giữ các trường cần dùng từ thẻ; clip-metadata.json giữ metadata media ngoài Git; source-evidence.json ghi catalog/fallback/hash metadata; prerequisites.json ghi ba điều kiện 212. make-data.py và render.mjs dựng lại danh sách bằng hàm tính của 212; make-report.py dựng báo cáo.

## Điều kiện trước và phạm vi

Ba điều kiện chạy đều đạt trước khi viết danh sách: `git log -1 --format=%h -- docs/games/audio/firefly/schema.json docs/games/audio/firefly/README.md` trả `83217b53`; đọc check.mjs thấy export `validateList`, `calculateTakes`, `calculateTotals`; schema có đủ sourceCommits/branchOnly/clips/clipsWhy. Điều phối đã xác nhận Claude duyệt và commit 212 trong đề bài. Không chạy CLI của 212 vì nó ghi đầu ra ngoài phạm vi; chỉ import các hàm không có side effect.

Nhánh game trước/sau là `main`. Đọc dh-vfx qua git show/diff; không mở worktree khác. Main `1f1de48`, dh-vfx `ca64509`, mới hơn mã be6e2dc trong phiếu. Không mạng, trình duyệt, dev server, build/test suite game, tạo/sửa/tải âm hay ảnh; không tạo thư mục AudioLab; không có lệnh Git ghi; không chạm Tu Tiên. Dùng skill game-vfx-layered để đối chiếu pha và nhịp 60 Hz; phiếu chỉ lập tài liệu, không thay VFX và không tự nhận nghiệm thu hình/nghe.

Các file preflight.json/preflight.txt còn trong 213 là bằng chứng lần chạy dừng lúc 12:55, trước commit 212; giữ làm lịch sử, đã được prerequisites.json của lần chạy lại này thay thế.

## 1. Kiểm tập id và selftest

`node docs/codex-queue/213/check.mjs` — **thoát 0**:

```text
PASS · Phiếu 213
catalog main=83; dh-vfx=83; FOE_SFX_IDS=35
fired=115; manifestOnly=2; rows=116; dh-vfx-only=35; excluded=24
missing=0; unknown=0; duplicates=0; schemaErrors=0
promptErrors=0
nonAscii=0
markdownErrors=0
sourceErrors=0
specErrors=0
calculationErrors=0
clipErrors=0
takes=192; P0=89; P1=87; P2=16
main=1f1de48; dh-vfx=ca64509
```

`node docs/codex-queue/213/check.mjs --selftest` — **thoát 0, bắt 3/3**:

```text
PASS · Phiếu 213
catalog main=83; dh-vfx=83; FOE_SFX_IDS=35
fired=115; manifestOnly=2; rows=116; dh-vfx-only=35; excluded=24
missing=0; unknown=0; duplicates=0; schemaErrors=0
promptErrors=0
nonAscii=0
markdownErrors=0
sourceErrors=0
specErrors=0
calculationErrors=0
clipErrors=0
takes=192; P0=89; P1=87; P2=16
main=1f1de48; dh-vfx=ca64509
CAUGHT bỏ một hàng phát
CAUGHT thêm id lạ
CAUGHT thêm chữ có dấu vào prompt
selftest=3/3
```

Bộ kiểm đọc catalog main từ checkout, catalog/foeSfx/FOE_SFX_SLOTS và content dh-vfx qua git object; không import mã thực thi game. Nó kiểm sự thay đổi commit và snapshot, bus/loop/lengthMs, số thẻ, mono/stereo/mode, phép tính, clip/pha, ASCII/Q6/phủ định, cùng tập id và prompt Markdown đúng từng chữ. Schema dùng nguyên hàm 212. Selftest chỉ sửa bản sao trong bộ nhớ; không sửa danh sách trên đĩa.

## 2. Lược đồ

Lệnh `node docs/codex-queue/213/check.mjs` gọi `validateList(list, schema)` import từ `../212/check.mjs`: **0 lỗi lược đồ**. Không sửa README, schema hoặc check của 212. Hàm kiểm hỗ trợ đúng tập từ khóa schema đang dùng, không phải trình thực thi mọi từ khóa JSON Schema 2020-12.

## 3. Số hàng và lượt

| Nhóm / buổi | Hàng | Lượt |
|---|---:|---:|
| Lửa | 9 | 25 |
| Rồng (khác lửa) | 7 | 9 |
| Quái | 56 | 99 |
| G01 | 11 | 20 |
| Bẫy và phe ta | 11 | 11 |
| Báo nguy và mốc trận | 8 | 12 |
| UI và học | 11 | 11 |
| Nền | 3 | 5 |

**Tổng 116 hàng / 192 lượt**; P0 89, P1 87, P2 16. Luật README: 12 s/file, 1000 ms lặng/cú, tối đa 8 cú, hao hụt dự toán 25%, P0 thêm một file. Không dùng variants.target làm số lượt trực tiếp vì README đã có công thức. Giữ nguyên variants.target của thẻ: hits/single/loop quyết định sức chứa. Lượt là file kết quả dự kiến, không suy ra thao tác/credit.

- Dh-vfx-only: **35 hàng** (7 × 5), trong đó **33** có điểm gọi có điều kiện và **2** chỉ manifest nhận (general.moss-banner.spawn/death). 35 id FOE_SFX_IDS hiện đều ở L2-cau; **0 ngoài map**, khác giả định roster lớn trong phiếu. Checker đọc roster thật, không giả định loài chưa có.
- Lửa có clip: **7** — fire.cast, fire.impact.a/b/c, impact.multi, dragon.skyfire.cast, dragon.skyfire.impact. Lửa không clip: **2** — Fire Breath dùng emitter breath 700 ms; Inferno dùng emitter inferno 10000 ms và finale bomb, không có cặp clip. Tổng âm giữ nguyên 1650/2400 ms tương ứng.
- Vòng lặp: **13** — amb.forest 6000 ms, amb.river 5000 ms, bốn enemy.*.march 4000 ms, bảy move riêng kế thừa 4000 ms. Amb.bird là âm lẻ 700 ms, không lặp. Mono/stereo theo thẻ: hai nền stereo; lớp march và move kế thừa mono, không tự sửa thành stereo.
- Loại: **24 id** = type.key **1** (bộ 189–192) + enemy.quadruped.howl **1** (catalog dành sẵn, mapper không gọi) + music.* **4** (VSCO-2-CE/VCSL, gồm bốn lớp trong music.ts) + nhãn show.sounds chưa đăng ký **18**. Mỗi id có lý do trong excluded của cả hai bản. Không có retired.

35 id riêng chưa có thẻ và số catalog riêng: giữ nguyên bus/loop/lengthMs và số thẻ của id lớp thật sự dùng làm fallback, ghi rõ trong basis; specCard null, không dựng thẻ mới. Engine có file thì thay lớp; thiếu file giữ lớp. Hit đòn chữ fileOnly bỏ lớp giọng riêng khi thiếu file nhưng fire.impact vẫn phát. Move chỉ chọn file khi tạo bed, không đổi loài giữa bed đang chạy. G01 spawn/death trả về sớm dùng general.g01.horn/death; danh sách không tự nhận hai file riêng đó đã được gọi.

## 4. Bảng nhịp lửa

Mốc 0 là sự kiện âm của từng hàng, riêng Sky Fire impact là cast+800 ms. Các số là tính tĩnh từ mã và metadata đã chụp, không phải đo browser. start/length số nguyên làm tròn; trường hợp ngẫu nhiên/đường bay ghi giới hạn và công thức ở cột cuối. Fire-burst chưa có metadata: ms dự toán ở 24 fps, cần tính lại khi có atlas. Smoke-column chưa khai báo trong bảng công cụ: pha F suy từ vai trò khói trong mã, nêu rõ; không sửa bảng. Một clip có nhiều dòng là nhiều khối/nhịp, hoặc nhánh thường/mạnh, không phải yêu cầu tạo thêm âm.

| Id âm | Clip | Pha | Bắt đầu (ms) | Hiện (ms) | Âm catalog (ms) | Điểm khớp, công thức và điều kiện |
|---|---|---|---:|---:|---:|---|
| fire.cast | muzzle-flash | R | 0 | 67 | 750 | fx.ts:1196–1198; frame=6, rate=1, fps=24, life=4/60 s; đòn mạnh life=5/60 s (83 ms). Khè và bắt lửa cùng mốc R trong 17 ms; không thêm gồng sau phím cuối. |
| fire.cast | fireball-head | T | 17 | 183 | 750 | fx.ts:1376,2104,2121–2127; ONE_FRAME=0,1 ms được vẽ lại suốt đường bay; out=0 ở tuổi ≤1/60, hiện từ khung kế tiếp (khoảng 17–33 ms). Đây là cửa sổ danh định 12 tick=200 ms; thời gian thực theo min(0,2; max(0,12; distance/18)), catch-up tối đa 60 ms, worldDt và chờ hit. Vân lặp frame=time×24+from.x, không chạy từ frame 0 mỗi đạn. |
| fire.cast | flame-trail | T | 0 | 333 | 750 | fx.ts:1411–1418,2114,2087–2100; ribbon đọc pool trực tiếp, frame=floor(time×12)%16; 200 ms bay danh định + 8/60 s đuôi=333 ms, không phải độ dài atlas 1333 ms. Chuyển động âm bám đường bay, không thêm cú nổ khi nối vòng. |
| fire.cast | impact-burst | I | 0 | 50 | 750 | fx.ts:1223–1224: clip pha I theo bảng nguồn được tái dùng làm lóe R ngay tại miệng, không phải mục tiêu; frame=0, until=4, rate=6,5, life=3/60 s. Bắt lửa trùng khung đầu trong 17 ms. |
| fire.impact.a | impact-burst | I | 0 | 458 | 600 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Thường: frame=10, until=20, rate=2, fps=12; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. |
| fire.impact.a | impact-burst | I | 33 | 399 | 600 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Thường: frame=10, until=20, rate=2, fps=12; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Khối phụ trễ 2 khung, rate ×1,15. |
| fire.impact.a | fire-burst | I | 0 | 229 | 600 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Thường: frame=10, until=20, rate=2, fps=24; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Chưa có metadata của clip dự phòng; số ms là dự toán ở 24 fps theo FIREFLY_VFX_LIST §1; phải tính lại khi nạp. |
| fire.impact.a | fire-burst | I | 33 | 199 | 600 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Thường: frame=10, until=20, rate=2, fps=24; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Chưa có metadata của clip dự phòng; số ms là dự toán ở 24 fps theo FIREFLY_VFX_LIST §1; phải tính lại khi nạp. Khối phụ trễ 2 khung, rate ×1,15. |
| fire.impact.a | impact-big | I | 0 | 444 | 600 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Thường: frame=20, until=23, rate=0.75, fps=12; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. |
| fire.impact.a | impact-big | I | 33 | 386 | 600 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Thường: frame=20, until=23, rate=0.75, fps=12; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Khối phụ trễ 2 khung, rate ×1,15. |
| fire.impact.a | smoke-mask | F | 133 | 1100 | 600 | fx.ts:1602–1607; life=1,1 s, rate=2,6, fps=8; khói thay thế smoke-roll, fadeIn=100 ms. Đuôi thấp đi cùng khói; không kéo dài âm quá catalog. |
| fire.impact.a | smoke-roll | F | 233 | 1000 | 600 | fx.ts:1602–1607; dự phòng khi chưa có smoke-mask; life=1 s, rate=2,6, fps=8; fadeIn=100 ms. Đuôi thấp đi cùng khói. |
| fire.impact.b | impact-burst | I | 0 | 458 | 640 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Thường: frame=10, until=20, rate=2, fps=12; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. |
| fire.impact.b | impact-burst | I | 33 | 399 | 640 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Thường: frame=10, until=20, rate=2, fps=12; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Khối phụ trễ 2 khung, rate ×1,15. |
| fire.impact.b | fire-burst | I | 0 | 229 | 640 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Thường: frame=10, until=20, rate=2, fps=24; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Chưa có metadata của clip dự phòng; số ms là dự toán ở 24 fps theo FIREFLY_VFX_LIST §1; phải tính lại khi nạp. |
| fire.impact.b | fire-burst | I | 33 | 199 | 640 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Thường: frame=10, until=20, rate=2, fps=24; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Chưa có metadata của clip dự phòng; số ms là dự toán ở 24 fps theo FIREFLY_VFX_LIST §1; phải tính lại khi nạp. Khối phụ trễ 2 khung, rate ×1,15. |
| fire.impact.b | impact-big | I | 0 | 444 | 640 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Thường: frame=20, until=23, rate=0.75, fps=12; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. |
| fire.impact.b | impact-big | I | 33 | 386 | 640 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Thường: frame=20, until=23, rate=0.75, fps=12; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Khối phụ trễ 2 khung, rate ×1,15. |
| fire.impact.b | smoke-mask | F | 133 | 1100 | 640 | fx.ts:1602–1607; life=1,1 s, rate=2,6, fps=8; khói thay thế smoke-roll, fadeIn=100 ms. Đuôi thấp đi cùng khói; không kéo dài âm quá catalog. |
| fire.impact.b | smoke-roll | F | 233 | 1000 | 640 | fx.ts:1602–1607; dự phòng khi chưa có smoke-mask; life=1 s, rate=2,6, fps=8; fadeIn=100 ms. Đuôi thấp đi cùng khói. |
| fire.impact.c | impact-burst | I | 0 | 458 | 1000 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Thường: frame=10, until=20, rate=2, fps=12; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. |
| fire.impact.c | impact-burst | I | 33 | 399 | 1000 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Thường: frame=10, until=20, rate=2, fps=12; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Khối phụ trễ 2 khung, rate ×1,15. |
| fire.impact.c | fire-burst | I | 0 | 229 | 1000 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Thường: frame=10, until=20, rate=2, fps=24; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Chưa có metadata của clip dự phòng; số ms là dự toán ở 24 fps theo FIREFLY_VFX_LIST §1; phải tính lại khi nạp. |
| fire.impact.c | fire-burst | I | 33 | 199 | 1000 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Thường: frame=10, until=20, rate=2, fps=24; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Chưa có metadata của clip dự phòng; số ms là dự toán ở 24 fps theo FIREFLY_VFX_LIST §1; phải tính lại khi nạp. Khối phụ trễ 2 khung, rate ×1,15. |
| fire.impact.c | impact-big | I | 0 | 444 | 1000 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Thường: frame=20, until=23, rate=0.75, fps=12; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. |
| fire.impact.c | impact-big | I | 33 | 386 | 1000 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Thường: frame=20, until=23, rate=0.75, fps=12; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Khối phụ trễ 2 khung, rate ×1,15. |
| fire.impact.c | smoke-mask | F | 133 | 1100 | 1000 | fx.ts:1602–1607; life=1,1 s, rate=2,6, fps=8; khói thay thế smoke-roll, fadeIn=100 ms. Đuôi thấp đi cùng khói; không kéo dài âm quá catalog. |
| fire.impact.c | smoke-roll | F | 233 | 1000 | 1000 | fx.ts:1602–1607; dự phòng khi chưa có smoke-mask; life=1 s, rate=2,6, fps=8; fadeIn=100 ms. Đuôi thấp đi cùng khói. |
| fire.impact.c | impact-burst | I | 0 | 417 | 1000 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Mạnh: frame=11, until=19, rate=1.8, fps=12; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. |
| fire.impact.c | impact-burst | I | 33 | 362 | 1000 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Mạnh: frame=11, until=19, rate=1.8, fps=12; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Khối phụ trễ 2 khung, rate ×1,15. |
| fire.impact.c | fire-burst | I | 0 | 208 | 1000 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Mạnh: frame=11, until=19, rate=1.8, fps=24; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Chưa có metadata của clip dự phòng; số ms là dự toán ở 24 fps theo FIREFLY_VFX_LIST §1; phải tính lại khi nạp. |
| fire.impact.c | fire-burst | I | 33 | 181 | 1000 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Mạnh: frame=11, until=19, rate=1.8, fps=24; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Chưa có metadata của clip dự phòng; số ms là dự toán ở 24 fps theo FIREFLY_VFX_LIST §1; phải tính lại khi nạp. Khối phụ trễ 2 khung, rate ×1,15. |
| fire.impact.c | impact-big | I | 0 | 444 | 1000 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Mạnh: frame=20, until=23, rate=0.75, fps=12; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. |
| fire.impact.c | impact-big | I | 33 | 386 | 1000 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Mạnh: frame=20, until=23, rate=0.75, fps=12; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Khối phụ trễ 2 khung, rate ×1,15. |
| impact.multi | impact-burst | I | 0 | 458 | 700 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Thường: frame=10, until=20, rate=2, fps=12; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Lớp âm gom ≥3 hit trong cửa sổ 45 ms; không có clip riêng của impact.multi, chỉ các wordHit được ghép tại từng mục tiêu. startMs tính từ hit đầu, cộng độ lệch 0–45 ms của từng hit. |
| impact.multi | impact-burst | I | 33 | 399 | 700 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Thường: frame=10, until=20, rate=2, fps=12; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Khối phụ trễ 2 khung, rate ×1,15. Lớp âm gom ≥3 hit trong cửa sổ 45 ms; không có clip riêng của impact.multi, chỉ các wordHit được ghép tại từng mục tiêu. startMs tính từ hit đầu, cộng độ lệch 0–45 ms của từng hit. |
| impact.multi | fire-burst | I | 0 | 229 | 700 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Thường: frame=10, until=20, rate=2, fps=24; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Chưa có metadata của clip dự phòng; số ms là dự toán ở 24 fps theo FIREFLY_VFX_LIST §1; phải tính lại khi nạp. Lớp âm gom ≥3 hit trong cửa sổ 45 ms; không có clip riêng của impact.multi, chỉ các wordHit được ghép tại từng mục tiêu. startMs tính từ hit đầu, cộng độ lệch 0–45 ms của từng hit. |
| impact.multi | fire-burst | I | 33 | 199 | 700 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Thường: frame=10, until=20, rate=2, fps=24; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Chưa có metadata của clip dự phòng; số ms là dự toán ở 24 fps theo FIREFLY_VFX_LIST §1; phải tính lại khi nạp. Khối phụ trễ 2 khung, rate ×1,15. Lớp âm gom ≥3 hit trong cửa sổ 45 ms; không có clip riêng của impact.multi, chỉ các wordHit được ghép tại từng mục tiêu. startMs tính từ hit đầu, cộng độ lệch 0–45 ms của từng hit. |
| impact.multi | impact-big | I | 0 | 444 | 700 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Thường: frame=20, until=23, rate=0.75, fps=12; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Lớp âm gom ≥3 hit trong cửa sổ 45 ms; không có clip riêng của impact.multi, chỉ các wordHit được ghép tại từng mục tiêu. startMs tính từ hit đầu, cộng độ lệch 0–45 ms của từng hit. |
| impact.multi | impact-big | I | 33 | 386 | 700 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Thường: frame=20, until=23, rate=0.75, fps=12; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Khối phụ trễ 2 khung, rate ×1,15. Lớp âm gom ≥3 hit trong cửa sổ 45 ms; không có clip riêng của impact.multi, chỉ các wordHit được ghép tại từng mục tiêu. startMs tính từ hit đầu, cộng độ lệch 0–45 ms của từng hit. |
| impact.multi | smoke-mask | F | 133 | 1100 | 700 | fx.ts:1602–1607; life=1,1 s, rate=2,6, fps=8; khói thay thế smoke-roll, fadeIn=100 ms. Đuôi thấp đi cùng khói; không kéo dài âm quá catalog. Lớp âm gom ≥3 hit trong cửa sổ 45 ms; không có clip riêng của impact.multi, chỉ các wordHit được ghép tại từng mục tiêu. startMs tính từ hit đầu, cộng độ lệch 0–45 ms của từng hit. |
| impact.multi | smoke-roll | F | 233 | 1000 | 700 | fx.ts:1602–1607; dự phòng khi chưa có smoke-mask; life=1 s, rate=2,6, fps=8; fadeIn=100 ms. Đuôi thấp đi cùng khói. Lớp âm gom ≥3 hit trong cửa sổ 45 ms; không có clip riêng của impact.multi, chỉ các wordHit được ghép tại từng mục tiêu. startMs tính từ hit đầu, cộng độ lệch 0–45 ms của từng hit. |
| impact.multi | impact-burst | I | 0 | 417 | 700 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Mạnh: frame=11, until=19, rate=1.8, fps=12; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Lớp âm gom ≥3 hit trong cửa sổ 45 ms; không có clip riêng của impact.multi, chỉ các wordHit được ghép tại từng mục tiêu. startMs tính từ hit đầu, cộng độ lệch 0–45 ms của từng hit. |
| impact.multi | impact-burst | I | 33 | 362 | 700 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Mạnh: frame=11, until=19, rate=1.8, fps=12; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Khối phụ trễ 2 khung, rate ×1,15. Lớp âm gom ≥3 hit trong cửa sổ 45 ms; không có clip riêng của impact.multi, chỉ các wordHit được ghép tại từng mục tiêu. startMs tính từ hit đầu, cộng độ lệch 0–45 ms của từng hit. |
| impact.multi | fire-burst | I | 0 | 208 | 700 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Mạnh: frame=11, until=19, rate=1.8, fps=24; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Chưa có metadata của clip dự phòng; số ms là dự toán ở 24 fps theo FIREFLY_VFX_LIST §1; phải tính lại khi nạp. Lớp âm gom ≥3 hit trong cửa sổ 45 ms; không có clip riêng của impact.multi, chỉ các wordHit được ghép tại từng mục tiêu. startMs tính từ hit đầu, cộng độ lệch 0–45 ms của từng hit. |
| impact.multi | fire-burst | I | 33 | 181 | 700 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Mạnh: frame=11, until=19, rate=1.8, fps=24; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Chưa có metadata của clip dự phòng; số ms là dự toán ở 24 fps theo FIREFLY_VFX_LIST §1; phải tính lại khi nạp. Khối phụ trễ 2 khung, rate ×1,15. Lớp âm gom ≥3 hit trong cửa sổ 45 ms; không có clip riêng của impact.multi, chỉ các wordHit được ghép tại từng mục tiêu. startMs tính từ hit đầu, cộng độ lệch 0–45 ms của từng hit. |
| impact.multi | impact-big | I | 0 | 444 | 700 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Mạnh: frame=20, until=23, rate=0.75, fps=12; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Lớp âm gom ≥3 hit trong cửa sổ 45 ms; không có clip riêng của impact.multi, chỉ các wordHit được ghép tại từng mục tiêu. startMs tính từ hit đầu, cộng độ lệch 0–45 ms của từng hit. |
| impact.multi | impact-big | I | 33 | 386 | 700 | dh-vfx:fx.ts:1532–1541; chọn theo thứ tự impact-burst → fire-burst → impact-big. Mạnh: frame=20, until=23, rate=0.75, fps=12; (until+1-frame)/(fps×rate). Đầu nổ trùng lóe tiếp xúc trong 17 ms; đây là mục tiêu nghe duyệt, chưa đo. Khối phụ trễ 2 khung, rate ×1,15. Lớp âm gom ≥3 hit trong cửa sổ 45 ms; không có clip riêng của impact.multi, chỉ các wordHit được ghép tại từng mục tiêu. startMs tính từ hit đầu, cộng độ lệch 0–45 ms của từng hit. |
| dragon.breath | — | — | — | — | 1650 | Fire Breath dùng emitter breath 700 ms tại dh-vfx:fx.ts:1702–1708; không gọi flipbook. |
| dragon.skyfire.cast | charge-orb | A | 0 | 200 | 900 | skyfire.ts:346–349; ONE_FRAME vẽ lại frame=time×24; A f0–f11, dài 200 ms trong cửa sổ sim 800 ms. Gầm gồng bắt đầu ở cast, không dời tick. |
| dragon.skyfire.cast | fireball-head | T | 200 | 600 | 900 | skyfire.ts:39–42,485–492; ONE_FRAME vẽ lại frame=time×24, R tại f12=200 ms, I tại f48=800 ms. Tiếng bắt lửa phải trùng R trong 17 ms. R dùng cone/flare mã ở :427–433; không gọi muzzle-flash. |
| dragon.skyfire.cast | flame-trail | T | 200 | 733 | 900 | skyfire.ts:477 và fx.ts:1411–1418; frame=floor(time×12)%16; T=600 ms, tail=8/60 s sau I (:675–679), tổng 733 ms. Âm cast 900 ms chồng 100 ms với âm impact ở 800 ms; đuôi ribbon kết thúc khoảng 933 ms. |
| dragon.skyfire.impact | impact-big | I | 0 | 667 | 1800 | Sky Fire: skyfire.ts:555–562; chọn impact-big → fire-burst → impact-burst; frame=16, until=23, rate=1, fps=12. Mốc 0 của hàng là sim impact ở cast+800 ms; đầu âm trùng lóe tiếp xúc trong 17 ms. Inferno: cùng id âm nhưng bomb emitter ở fx.ts:1822–1834,2725, không dùng những clip này. |
| dragon.skyfire.impact | impact-big | I | 33 | 556 | 1800 | Sky Fire: skyfire.ts:555–562; chọn impact-big → fire-burst → impact-burst; frame=16, until=23, rate=1, fps=12. Mốc 0 của hàng là sim impact ở cast+800 ms; đầu âm trùng lóe tiếp xúc trong 17 ms. Inferno: cùng id âm nhưng bomb emitter ở fx.ts:1822–1834,2725, không dùng những clip này. Khối phụ thứ nhất, rate ×1,2. |
| dragon.skyfire.impact | impact-big | I | 67 | 556 | 1800 | Sky Fire: skyfire.ts:555–562; chọn impact-big → fire-burst → impact-burst; frame=16, until=23, rate=1, fps=12. Mốc 0 của hàng là sim impact ở cast+800 ms; đầu âm trùng lóe tiếp xúc trong 17 ms. Inferno: cùng id âm nhưng bomb emitter ở fx.ts:1822–1834,2725, không dùng những clip này. Khối phụ thứ hai, rate ×1,2. |
| dragon.skyfire.impact | fire-burst | I | 0 | 391 | 1800 | Sky Fire: skyfire.ts:555–562; chọn impact-big → fire-burst → impact-burst; frame=9, until=23, rate=1.6, fps=24. Mốc 0 của hàng là sim impact ở cast+800 ms; đầu âm trùng lóe tiếp xúc trong 17 ms. Inferno: cùng id âm nhưng bomb emitter ở fx.ts:1822–1834,2725, không dùng những clip này. Metadata dự phòng chưa có, ms dự toán theo 24 fps; tính lại khi nạp. |
| dragon.skyfire.impact | fire-burst | I | 33 | 326 | 1800 | Sky Fire: skyfire.ts:555–562; chọn impact-big → fire-burst → impact-burst; frame=9, until=23, rate=1.6, fps=24. Mốc 0 của hàng là sim impact ở cast+800 ms; đầu âm trùng lóe tiếp xúc trong 17 ms. Inferno: cùng id âm nhưng bomb emitter ở fx.ts:1822–1834,2725, không dùng những clip này. Metadata dự phòng chưa có, ms dự toán theo 24 fps; tính lại khi nạp. Khối phụ thứ nhất, rate ×1,2. |
| dragon.skyfire.impact | fire-burst | I | 67 | 326 | 1800 | Sky Fire: skyfire.ts:555–562; chọn impact-big → fire-burst → impact-burst; frame=9, until=23, rate=1.6, fps=24. Mốc 0 của hàng là sim impact ở cast+800 ms; đầu âm trùng lóe tiếp xúc trong 17 ms. Inferno: cùng id âm nhưng bomb emitter ở fx.ts:1822–1834,2725, không dùng những clip này. Metadata dự phòng chưa có, ms dự toán theo 24 fps; tính lại khi nạp. Khối phụ thứ hai, rate ×1,2. |
| dragon.skyfire.impact | impact-burst | I | 0 | 781 | 1800 | Sky Fire: skyfire.ts:555–562; chọn impact-big → fire-burst → impact-burst; frame=9, until=23, rate=1.6, fps=12. Mốc 0 của hàng là sim impact ở cast+800 ms; đầu âm trùng lóe tiếp xúc trong 17 ms. Inferno: cùng id âm nhưng bomb emitter ở fx.ts:1822–1834,2725, không dùng những clip này. |
| dragon.skyfire.impact | impact-burst | I | 33 | 651 | 1800 | Sky Fire: skyfire.ts:555–562; chọn impact-big → fire-burst → impact-burst; frame=9, until=23, rate=1.6, fps=12. Mốc 0 của hàng là sim impact ở cast+800 ms; đầu âm trùng lóe tiếp xúc trong 17 ms. Inferno: cùng id âm nhưng bomb emitter ở fx.ts:1822–1834,2725, không dùng những clip này. Khối phụ thứ nhất, rate ×1,2. |
| dragon.skyfire.impact | impact-burst | I | 67 | 651 | 1800 | Sky Fire: skyfire.ts:555–562; chọn impact-big → fire-burst → impact-burst; frame=9, until=23, rate=1.6, fps=12. Mốc 0 của hàng là sim impact ở cast+800 ms; đầu âm trùng lóe tiếp xúc trong 17 ms. Inferno: cùng id âm nhưng bomb emitter ở fx.ts:1822–1834,2725, không dùng những clip này. Khối phụ thứ hai, rate ×1,2. |
| dragon.skyfire.impact | embers | I | 33 | 1042 | 1800 | skyfire.ts:565–566; frames=30, start=0, fps=12, rate=2,4, không life riêng → 1042 ms. Đá/than bắt đầu f2, đuôi rơi nằm trong 1800 ms âm. |
| dragon.skyfire.impact | smoke-column | F | 367 | 2300 | 1800 | skyfire.ts:625–630; life=2,3 s, rate=1,7, fps=8; pha F suy từ vai trò khói trong mã vì tools/vfx-flipbook/dragon-hold.json chưa khai báo smoke-column. Âm tắt ở 1800 ms dù hình khói còn; không kéo file dài ra. |
| dragon.skyfire.impact | smoke-column | F | 467 | 2300 | 1800 | skyfire.ts:625–630; life=2,3 s, rate=1,7, fps=8; pha F suy từ vai trò khói trong mã vì tools/vfx-flipbook/dragon-hold.json chưa khai báo smoke-column. Âm tắt ở 1800 ms dù hình khói còn; không kéo file dài ra. |
| dragon.skyfire.impact | smoke-mask | F | 433 | 1300 | 1800 | skyfire.ts:632; khi có smoke-column, billow giữa: life=1,3 s, rate=2,2, fps=8. Đuôi nổ thấp lùi cùng khói. |
| dragon.skyfire.impact | smoke-mask | F | 433 | 1150 | 1800 | skyfire.ts:634–638; chỉ khi thiếu smoke-column; chọn smoke-mask rồi smoke-roll; life=1,15 s, rate=1 hoặc 2,2; fps=8. Âm đuôi đi cùng khói; không phát thêm tiếng khói. |
| dragon.skyfire.impact | smoke-mask | F | 500 | 1150 | 1800 | skyfire.ts:634–638; chỉ khi thiếu smoke-column; chọn smoke-mask rồi smoke-roll; life=1,15 s, rate=1 hoặc 2,2; fps=8. Âm đuôi đi cùng khói; không phát thêm tiếng khói. |
| dragon.skyfire.impact | smoke-mask | F | 567 | 1150 | 1800 | skyfire.ts:634–638; chỉ khi thiếu smoke-column; chọn smoke-mask rồi smoke-roll; life=1,15 s, rate=1 hoặc 2,2; fps=8. Âm đuôi đi cùng khói; không phát thêm tiếng khói. |
| dragon.skyfire.impact | smoke-roll | F | 433 | 1150 | 1800 | skyfire.ts:634–638; chỉ khi thiếu smoke-column; chọn smoke-mask rồi smoke-roll; life=1,15 s, rate=1 hoặc 2,2; fps=8. Âm đuôi đi cùng khói; không phát thêm tiếng khói. |
| dragon.skyfire.impact | smoke-roll | F | 500 | 1150 | 1800 | skyfire.ts:634–638; chỉ khi thiếu smoke-column; chọn smoke-mask rồi smoke-roll; life=1,15 s, rate=1 hoặc 2,2; fps=8. Âm đuôi đi cùng khói; không phát thêm tiếng khói. |
| dragon.skyfire.impact | smoke-roll | F | 567 | 1150 | 1800 | skyfire.ts:634–638; chỉ khi thiếu smoke-column; chọn smoke-mask rồi smoke-roll; life=1,15 s, rate=1 hoặc 2,2; fps=8. Âm đuôi đi cùng khói; không phát thêm tiếng khói. |
| dragon.skyfire.impact | ground-fire | F | 100 | 3200 | 1800 | skyfire.ts:648–661; chỉ điểm khô, trễ ngẫu nhiên 6–14/60 s (100–233 ms), life ngẫu nhiên 2000–3200 ms; lengthMs ghi cực đại; frame ngẫu nhiên 0–30, fps=24, loop=true. Đuôi lách tách trong âm 1800 ms; hình cháy lâu hơn âm, không tự thêm loop âm. |
| dragon.inferno | — | — | — | — | 2400 | Inferno dùng emitter inferno trong 10000 ms tại dh-vfx:fx.ts:1785–1787; âm mở 2400 ms. Finale bomb tại :2725 dùng lớp mã, không gọi flipbook. |

Sky Fire: A 0–200 ms; R 200 ms bằng cone/flare, không dùng muzzle-flash; T 200–800 ms; âm cast 900 ms chồng 100 ms với impact 1800 ms. Charge-orb lúc gõ đi cùng type.key bị loại, nhưng cast Sky Fire vẫn dùng orb riêng ở A. Impact-burst pha gốc I được tái dùng làm lóe R tại miệng, đã ghi vai trò thực tế trong syncNote.

**Lệch tìm được:** mapper cho dragon.skyfire.impact nhận Inferno stage=impact, nhưng `src/sim/combat.ts:829–834` trên cả hai nhánh emit finale bằng stage=end. View bomb theo end, không có flipbook. Vì vậy hiện chưa có đường phát âm này ở finale Inferno, dù bộ định tuyến có nhánh dự kiến. Đã ghi cả hai trường hợp trong hàng; không sửa mã theo phạm vi phiếu.

Mục tiêu đầu tiếng trùng lóe trong 17 ms chưa được chứng minh: engine vary thêm 0–12 ms, đổi pitch ±4%, hit-stop/worldDt và chờ bolt có thể làm hình lệch sim. Lửa đòn chữ giữ đuôi thấp và giảm vùng 1–4 kHz sau đầu tiếng theo Q6; đây là ý đồ prompt, không phải kết quả đo phổ. Hình khói/đất cháy có thể lâu hơn âm, không tự kéo dài file catalog.

## 5. ASCII và từ cấm

Lệnh đếm đã chạy (Node, chỉ đọc JSON và ghi kết quả vào 213/ascii-check.txt):

```js
const count = key => list.rows.reduce((sum, row) => sum + ((row[key] ?? '').match(/[^\x00-\x7f]/g) ?? []).length, 0);
console.log(count('prompt'), count('playerName'));
```

Chạy bằng `node --input-type=module` sau khi đọc dragon-hold.json với readFileSync. [ascii-check.txt](213/ascii-check.txt):

```text
promptNonAsciiCharacters=0
englishNameNonAsciiCharacters=0
```

Checker cũng quét Q6 đầy đủ (kể cả nhóm bổ sung ngày 25/10), từ phủ định theo 212 và tên model bị cấm trong prompt: **0 lỗi**. Prompt dài nhất `enemy.moss-archer.attack`: **450 ký tự ASCII**; giới hạn giao diện Firefly chưa biết, cần chủ dự án thử lượt đầu.

## 6. Commit và nguồn

Hai lệnh riêng `git -C games/dragon-hold rev-parse --short main` → **1f1de48** và `git -C games/dragon-hold rev-parse --short dh-vfx` → **ca64509**. Checker đối chiếu lại cả hai ở mỗi lượt chạy, báo lỗi nếu nhánh hoặc source object đổi. Metadata atlas ngoài Git được chụp cùng SHA-256 trong source-evidence.json; không gán metadata đó cho commit. Claude cần chạy lại kiểm và rà cặp clip khi dh-vfx đổi/gộp.

## 7. Trạng thái repo trước/sau

Đã lưu [status-before.txt](213/status-before.txt), [status-after.txt](213/status-after.txt), [game-before.txt](213/game-before.txt), [game-after.txt](213/game-after.txt) và [state-check.json](213/state-check.json). Game status trước/sau giống từng byte: **true**; game sạch, nhánh sau **main**.

So status repo cha: thêm/bớt ngoài phạm vi **24 / 0** dòng. Có thay đổi đồng thời ngoài phạm vi; không sửa/dọn để ép so sánh đạt. Các dòng cụ thể giữ trong state-check.json; chỉ ghi các đường dẫn của phiếu.

## Bỏ qua và việc chủ dự án cần xem

Không tạo/tải/sửa âm, ảnh, inbox, thẻ spec, schema, mã game hoặc hệ thống khác vì phiếu chỉ lập danh sách. Không thể nghe/chấm âm chưa tạo. Chủ dự án bắt đầu buổi lửa **25 file dự kiến**, kiểm prompt có vừa giao diện và nhịp có đúng clip, rồi ghi tỷ lệ cú dùng được để chỉnh dự toán. Claude duyệt danh sách trước khi commit; cần xem ba chỗ: finale Inferno chưa nối, hai id G01 manifest-only, metadata/pha của các clip khói mới và fire-burst dự phòng. Không commit/push trong lượt này.
