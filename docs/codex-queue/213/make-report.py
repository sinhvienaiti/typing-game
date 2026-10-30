from pathlib import Path
import json

root=Path(__file__).resolve().parents[3]
out=root/'docs/codex-queue/213'
read=lambda n:(out/n).read_text()
data=json.loads((root/'docs/games/audio/firefly/dragon-hold.json').read_text())
groups=json.loads(read('group-totals.json'))
check=json.loads(read('check.json'))
state=json.loads(read('state-check.json')) if (out/'state-check.json').exists() else None
md=(root/'docs/games/audio/firefly/dragon-hold.md').read_text()
rhythm=md[md.index('| Id âm |'):md.index('\n## Id riêng')]
longest=max(data['rows'],key=lambda r:len(r['prompt']))
lines=['# Phiếu 213 · Dragonhold · Danh sách âm Firefly ghép clip lửa', '',
'Ngày 30/10/2026. Đã lập **116 hàng, 192 lượt dự kiến**, theo schema và công thức phiếu 212. Lửa có **9 hàng / 25 lượt**, đứng đầu danh sách để chủ dự án nghe cùng clip. Chưa tạo âm, chưa nghe duyệt, chưa gắn vào game; cổng G3 chưa được nghiệm thu.', '',
'## File giao', '',
'- [dragon-hold.md](../games/audio/firefly/dragon-hold.md): tám buổi tạo, tên tiếng Anh, khi phát, catalog/targetMs, mono/stereo, vòng lặp, biến thể/lượt, prompt nguyên văn, gợi ý diễn, clip/pha và inbox.',
'- [dragon-hold.json](../games/audio/firefly/dragon-hold.json): cùng tập hàng và prompt, đúng schema 212; sourceCommits main `1f1de48`, dh-vfx `ca64509`.',
'- [213/fired-ids.json](213/fired-ids.json): 115 id có đường phát theo mã trên hợp hai nhánh; 82 catalog (gồm type.key bị loại) + 33 id file riêng có điều kiện; hai id manifest-only ghi riêng. [callsite-inventory.json](213/callsite-inventory.json) giữ toàn bộ push/at/bed/play đã dò trong hai file, trên cả hai nhánh.',
'- [213/check.mjs](213/check.mjs), [check.txt](213/check.txt), [check.json](213/check.json), [check-selftest.txt](213/check-selftest.txt), [check-selftest.json](213/check-selftest.json): validator, phép tính, đối chiếu nguồn/thẻ/Markdown và selftest.',
'- Bằng chứng tại [213/](213/): source-snapshot.json giữ git object đã đọc; spec-evidence.json chỉ giữ các trường cần dùng từ thẻ; clip-metadata.json giữ metadata media ngoài Git; source-evidence.json ghi catalog/fallback/hash metadata; prerequisites.json ghi ba điều kiện 212. make-data.py và render.mjs dựng lại danh sách bằng hàm tính của 212; make-report.py dựng báo cáo.', '',
'## Điều kiện trước và phạm vi', '',
'Ba điều kiện chạy đều đạt trước khi viết danh sách: `git log -1 --format=%h -- docs/games/audio/firefly/schema.json docs/games/audio/firefly/README.md` trả `83217b53`; đọc check.mjs thấy export `validateList`, `calculateTakes`, `calculateTotals`; schema có đủ sourceCommits/branchOnly/clips/clipsWhy. Điều phối đã xác nhận Claude duyệt và commit 212 trong đề bài. Không chạy CLI của 212 vì nó ghi đầu ra ngoài phạm vi; chỉ import các hàm không có side effect.', '',
'Nhánh game trước/sau là `main`. Đọc dh-vfx qua git show/diff; không mở worktree khác. Main `1f1de48`, dh-vfx `ca64509`, mới hơn mã be6e2dc trong phiếu. Không mạng, trình duyệt, dev server, build/test suite game, tạo/sửa/tải âm hay ảnh; không tạo thư mục AudioLab; không có lệnh Git ghi; không chạm Tu Tiên. Dùng skill game-vfx-layered để đối chiếu pha và nhịp 60 Hz; phiếu chỉ lập tài liệu, không thay VFX và không tự nhận nghiệm thu hình/nghe.', '',
'Các file preflight.json/preflight.txt còn trong 213 là bằng chứng lần chạy dừng lúc 12:55, trước commit 212; giữ làm lịch sử, đã được prerequisites.json của lần chạy lại này thay thế.', '',
'## 1. Kiểm tập id và selftest', '',
'`node docs/codex-queue/213/check.mjs` — **thoát 0**:', '', '```text',read('check.txt').strip(),'```','',
'`node docs/codex-queue/213/check.mjs --selftest` — **thoát 0, bắt 3/3**:', '', '```text',read('check-selftest.txt').strip(),'```','',
'Bộ kiểm đọc catalog main từ checkout, catalog/foeSfx/FOE_SFX_SLOTS và content dh-vfx qua git object; không import mã thực thi game. Nó kiểm sự thay đổi commit và snapshot, bus/loop/lengthMs, số thẻ, mono/stereo/mode, phép tính, clip/pha, ASCII/Q6/phủ định, cùng tập id và prompt Markdown đúng từng chữ. Schema dùng nguyên hàm 212. Selftest chỉ sửa bản sao trong bộ nhớ; không sửa danh sách trên đĩa.', '',
'## 2. Lược đồ', '',
'Lệnh `node docs/codex-queue/213/check.mjs` gọi `validateList(list, schema)` import từ `../212/check.mjs`: **0 lỗi lược đồ**. Không sửa README, schema hoặc check của 212. Hàm kiểm hỗ trợ đúng tập từ khóa schema đang dùng, không phải trình thực thi mọi từ khóa JSON Schema 2020-12.', '',
'## 3. Số hàng và lượt', '', '| Nhóm / buổi | Hàng | Lượt |', '|---|---:|---:|']
lines += [f'| {g} | {v["rows"]} | {v["takes"]} |' for g,v in groups.items()]
lines += ['', '**Tổng 116 hàng / 192 lượt**; P0 89, P1 87, P2 16. Luật README: 12 s/file, 1000 ms lặng/cú, tối đa 8 cú, hao hụt dự toán 25%, P0 thêm một file. Không dùng variants.target làm số lượt trực tiếp vì README đã có công thức. Giữ nguyên variants.target của thẻ: hits/single/loop quyết định sức chứa. Lượt là file kết quả dự kiến, không suy ra thao tác/credit.', '',
'- Dh-vfx-only: **35 hàng** (7 × 5), trong đó **33** có điểm gọi có điều kiện và **2** chỉ manifest nhận (general.moss-banner.spawn/death). 35 id FOE_SFX_IDS hiện đều ở L2-cau; **0 ngoài map**, khác giả định roster lớn trong phiếu. Checker đọc roster thật, không giả định loài chưa có.',
'- Lửa có clip: **7** — fire.cast, fire.impact.a/b/c, impact.multi, dragon.skyfire.cast, dragon.skyfire.impact. Lửa không clip: **2** — Fire Breath dùng emitter breath 700 ms; Inferno dùng emitter inferno 10000 ms và finale bomb, không có cặp clip. Tổng âm giữ nguyên 1650/2400 ms tương ứng.',
'- Vòng lặp: **13** — amb.forest 6000 ms, amb.river 5000 ms, bốn enemy.*.march 4000 ms, bảy move riêng kế thừa 4000 ms. Amb.bird là âm lẻ 700 ms, không lặp. Mono/stereo theo thẻ: hai nền stereo; lớp march và move kế thừa mono, không tự sửa thành stereo.',
'- Loại: **24 id** = type.key **1** (bộ 189–192) + enemy.quadruped.howl **1** (catalog dành sẵn, mapper không gọi) + music.* **4** (VSCO-2-CE/VCSL, gồm bốn lớp trong music.ts) + nhãn show.sounds chưa đăng ký **18**. Mỗi id có lý do trong excluded của cả hai bản. Không có retired.', '',
'35 id riêng chưa có thẻ và số catalog riêng: giữ nguyên bus/loop/lengthMs và số thẻ của id lớp thật sự dùng làm fallback, ghi rõ trong basis; specCard null, không dựng thẻ mới. Engine có file thì thay lớp; thiếu file giữ lớp. Hit đòn chữ fileOnly bỏ lớp giọng riêng khi thiếu file nhưng fire.impact vẫn phát. Move chỉ chọn file khi tạo bed, không đổi loài giữa bed đang chạy. G01 spawn/death trả về sớm dùng general.g01.horn/death; danh sách không tự nhận hai file riêng đó đã được gọi.', '',
'## 4. Bảng nhịp lửa', '',
'Mốc 0 là sự kiện âm của từng hàng, riêng Sky Fire impact là cast+800 ms. Các số là tính tĩnh từ mã và metadata đã chụp, không phải đo browser. start/length số nguyên làm tròn; trường hợp ngẫu nhiên/đường bay ghi giới hạn và công thức ở cột cuối. Fire-burst chưa có metadata: ms dự toán ở 24 fps, cần tính lại khi có atlas. Smoke-column chưa khai báo trong bảng công cụ: pha F suy từ vai trò khói trong mã, nêu rõ; không sửa bảng. Một clip có nhiều dòng là nhiều khối/nhịp, hoặc nhánh thường/mạnh, không phải yêu cầu tạo thêm âm.', '',rhythm.strip(),'',
'Sky Fire: A 0–200 ms; R 200 ms bằng cone/flare, không dùng muzzle-flash; T 200–800 ms; âm cast 900 ms chồng 100 ms với impact 1800 ms. Charge-orb lúc gõ đi cùng type.key bị loại, nhưng cast Sky Fire vẫn dùng orb riêng ở A. Impact-burst pha gốc I được tái dùng làm lóe R tại miệng, đã ghi vai trò thực tế trong syncNote.', '',
'**Lệch tìm được:** mapper cho dragon.skyfire.impact nhận Inferno stage=impact, nhưng `src/sim/combat.ts:829–834` trên cả hai nhánh emit finale bằng stage=end. View bomb theo end, không có flipbook. Vì vậy hiện chưa có đường phát âm này ở finale Inferno, dù bộ định tuyến có nhánh dự kiến. Đã ghi cả hai trường hợp trong hàng; không sửa mã theo phạm vi phiếu.', '',
'Mục tiêu đầu tiếng trùng lóe trong 17 ms chưa được chứng minh: engine vary thêm 0–12 ms, đổi pitch ±4%, hit-stop/worldDt và chờ bolt có thể làm hình lệch sim. Lửa đòn chữ giữ đuôi thấp và giảm vùng 1–4 kHz sau đầu tiếng theo Q6; đây là ý đồ prompt, không phải kết quả đo phổ. Hình khói/đất cháy có thể lâu hơn âm, không tự kéo dài file catalog.', '',
'## 5. ASCII và từ cấm', '',
'Lệnh đếm đã chạy (Node, chỉ đọc JSON và ghi kết quả vào 213/ascii-check.txt):', '', '```js',
"const count = key => list.rows.reduce((sum, row) => sum + ((row[key] ?? '').match(/[^\\x00-\\x7f]/g) ?? []).length, 0);",
"console.log(count('prompt'), count('playerName'));",'```','',
'Chạy bằng `node --input-type=module` sau khi đọc dragon-hold.json với readFileSync. [ascii-check.txt](213/ascii-check.txt):', '', '```text',read('ascii-check.txt').strip(),'```','',
f'Checker cũng quét Q6 đầy đủ (kể cả nhóm bổ sung ngày 25/10), từ phủ định theo 212 và tên model bị cấm trong prompt: **0 lỗi**. Prompt dài nhất `{longest["id"]}`: **{len(longest["prompt"])} ký tự ASCII**; giới hạn giao diện Firefly chưa biết, cần chủ dự án thử lượt đầu.', '',
'## 6. Commit và nguồn', '',
'Hai lệnh riêng `git -C games/dragon-hold rev-parse --short main` → **1f1de48** và `git -C games/dragon-hold rev-parse --short dh-vfx` → **ca64509**. Checker đối chiếu lại cả hai ở mỗi lượt chạy, báo lỗi nếu nhánh hoặc source object đổi. Metadata atlas ngoài Git được chụp cùng SHA-256 trong source-evidence.json; không gán metadata đó cho commit. Claude cần chạy lại kiểm và rà cặp clip khi dh-vfx đổi/gộp.', '',
'## 7. Trạng thái repo trước/sau', '']
if state:
 lines += [f'Đã lưu [status-before.txt](213/status-before.txt), [status-after.txt](213/status-after.txt), [game-before.txt](213/game-before.txt), [game-after.txt](213/game-after.txt) và [state-check.json](213/state-check.json). Game status trước/sau giống từng byte: **{str(state["gameStatusIdentical"]).lower()}**; game sạch, nhánh sau **{state["gameBranchAfter"]}**.', '',
 f'So status repo cha: thêm/bớt ngoài phạm vi **{len(state["outsideAdded"])} / {len(state["outsideRemoved"])}** dòng. '+('Khác biệt chỉ nằm trong bốn vị trí được phép.' if not state['outsideAdded'] and not state['outsideRemoved'] else 'Có thay đổi đồng thời ngoài phạm vi; không sửa/dọn để ép so sánh đạt. Các dòng cụ thể giữ trong state-check.json; chỉ ghi các đường dẫn của phiếu.'),'']
else:lines+=['Chờ chụp trạng thái sau và đối chiếu.','']
lines += ['## Bỏ qua và việc chủ dự án cần xem', '',
'Không tạo/tải/sửa âm, ảnh, inbox, thẻ spec, schema, mã game hoặc hệ thống khác vì phiếu chỉ lập danh sách. Không thể nghe/chấm âm chưa tạo. Chủ dự án bắt đầu buổi lửa **25 file dự kiến**, kiểm prompt có vừa giao diện và nhịp có đúng clip, rồi ghi tỷ lệ cú dùng được để chỉnh dự toán. Claude duyệt danh sách trước khi commit; cần xem ba chỗ: finale Inferno chưa nối, hai id G01 manifest-only, metadata/pha của các clip khói mới và fire-burst dự phòng. Không commit/push trong lượt này.', '']
(root/'docs/codex-queue/213-report.md').write_text('\n'.join(lines))
