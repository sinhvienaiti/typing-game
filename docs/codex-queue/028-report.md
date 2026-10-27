# Phiếu 028 · Map Factory · Bộ đọc lớp chơi ở commit ghim

Ngày thực hiện: 28/10/2026. Worktree: `/Users/toandx/htdocs/typing-game-wt/map-codex`. Môi trường: macOS, Node **v24.22.0**.

Đã hoàn tất **8/8 mục kiểm bắt buộc**: **13 test đạt, 0 lỗi, 0 bỏ qua**; hai fixture đúng từng byte và đúng SHA-256 trong phiếu ở cả hai lượt ghi. Không đổi commit ghim. Chỉ đọc nội dung game đã được `git archive` vào `.cache`; không đọc hoặc import mã từ cây làm việc của game.

## 1. Các file đã viết

- `tools/map-factory/lib/ts-hook.mjs`: hook đồng bộ bổ sung đuôi `.ts` cho import tương đối không có đuôi; Node tự bỏ kiểu.
- `tools/map-factory/adapters/extract.mjs`: tìm repo riêng, phân giải commit, trích archive, JSON chuẩn, băm và CLI.
- `tools/map-factory/adapters/typing-defense.mjs`: bộ đọc `w1-silverfall`, dùng đúng `groundLanes` và các luật ở commit ghim.
- `tools/map-factory/adapters/dragon-hold.mjs`: bộ đọc `L2-cau`, dùng đúng `compileLanes`, kiểm đơn vị và đếm phép đổi.
- `tools/map-factory/test/adapters.test.mjs`: tám nhóm kiểm theo phiếu, bốn subtest băm vàng và kiểm thêm hợp đồng tham số CLI.
- `tools/map-factory/test/fixtures/gameplay/typing-defense.w1-silverfall.json`: do CLI sinh, không viết tay.
- `tools/map-factory/test/fixtures/gameplay/dragon-hold.L2-cau.json`: do CLI sinh, không viết tay.
- `tools/map-factory/.gitignore`: đúng ba dòng của phiếu; chỉ bỏ qua `.cache/` và `out/` ở gốc công cụ.
- `docs/codex-queue/028-report.md`: báo cáo này.

Sản phẩm tạm ngoài Git nằm trong `tools/map-factory/.cache/`: cây archive của bốn commit được kiểm và thư mục rỗng `empty-games/dragon-hold` dùng kiểm chặn repo giả. Mỗi lần trích đều xóa và tạo lại thư mục commit đích.

## 2. Tám mục kiểm bắt buộc

Mọi lệnh chạy từ cwd `.` của worktree. Lệnh con được gọi bằng `execFileSync` với mảng tham số, không qua shell; mẫu `*.test.mjs` và `*.json` bên dưới được liệt kê bằng API thư mục của Node trước khi truyền cho lệnh.

### Kiểm 1 · Bộ test

```text
node --test tools/map-factory/test/*.test.mjs
tests 13
suites 0
pass 13
fail 0
cancelled 0
skipped 0
todo 0
duration_ms 2810.150916
Exit code: 0
```

Có **9 test cấp đầu và 4 subtest**. Lượt kiểm trước đó cũng đạt **13/13**, không bỏ qua; sau khi thu gọn stderr của các ca CLI cố ý sai, chạy lại nguyên bộ và nhận kết quả trên.

Ngoài các yêu cầu trong phiếu, test kiểm stdout của `all` bằng hai fixture nối theo đúng thứ tự; các tham số thiếu, tên game lạ, tham số thừa, cờ lạ, cờ ghi lặp, `all` kèm rev và ghi fixture từ rev khác PIN đều thoát **2**, không đổi fixture. `canonicalJson` kiểm thêm thứ tự UTF-16, giá trị không hợp lệ nằm trong object/mảng và số vượt miền nguyên an toàn.

### Kiểm 2 · Ghi fixture hai lần, cùng SHA-256

```text
node tools/map-factory/adapters/extract.mjs all --write
…/typing-defense.w1-silverfall.json 7faeaa7c0d5bf39803019444b1ae8056c36d3914a916a74baaed834e76ef4b23
…/dragon-hold.L2-cau.json c852b4d70147c8d2bf87f22999334f090646d0ae87bde6a9873b35de45d9659a
Exit code: 0

shasum -a 256 tools/map-factory/test/fixtures/gameplay/*.json
ad67509d387ba403f4cb6b1860de98266c892758e233a8b78d71a522e2a9fb37  …/dragon-hold.L2-cau.json
71160a56c917a195f44baff68ceee9d2aa31e31e39169697ca839d7f54fc1428  …/typing-defense.w1-silverfall.json
Exit code: 0
```

Chạy cặp lệnh trên **hai lần**; cả hai lần nhận đúng các dòng đường dẫn và băm trên. Thời gian CLI có `--write`: lượt 1 **1135,909 ms**, lượt 2 **413,709 ms**. Test 5 còn gọi từng game trong hai tiến trình Node riêng, so stdout từng byte với nhau và với fixture: đều đạt.

### Kiểm 3 · Bốn băm bản trích

Nằm trong test 3 của lệnh kiểm 1; mỗi subtest gọi `extract(rev)` đúng một lần. Cả bốn commit đều tồn tại, **0 subtest bỏ qua**.

| Game | Commit thực đã phân giải | Băm lớp chơi |
| --- | --- | --- |
| Lời Gọi, PIN | `10ce627ff4e1c91f29e808cb658c086f51bd97d6` | `7faeaa7c0d5bf39803019444b1ae8056c36d3914a916a74baaed834e76ef4b23` |
| Lời Gọi, `10ce627^` | `84d0ac116b396df2b341ed4330461653a05fd8b2` | `7faeaa7c0d5bf39803019444b1ae8056c36d3914a916a74baaed834e76ef4b23` |
| Rồng, PIN | `83da970eacbf85ea64da89f62a4d1b6622bc5c7b` | `c852b4d70147c8d2bf87f22999334f090646d0ae87bde6a9873b35de45d9659a` |
| Rồng, `3f3390d` | `3f3390d6bddf404a2dee508c80973181bd31795f` | `c852b4d70147c8d2bf87f22999334f090646d0ae87bde6a9873b35de45d9659a` |

Hai ca commit so sánh kiểm tồn tại bằng `rev-parse --verify --quiet --end-of-options <rev>^{commit}` và có lối bỏ qua có lý do khi commit mất. Hai ca PIN không có lối bỏ qua.

### Kiểm 4 · Sự thật về lớp chơi

Nằm trong test 1–2 của lệnh kiểm 1:

```text
Maximum lane deviation: 0.4999461656384483 cm; trees=36, preset=5
laneValues=37, checked=132, notDivisible=0; lane slots=11, house slots=6
```

- Lời Gọi: **36 cây**, đúng từng tọa độ và thứ tự; **5 nhà đặt sẵn**, đúng loại, tọa độ, cỡ và bán kính nền. `TREE.radiusM = 1,5`, `BUILD.roadClearM = 1,9`, `keepClearM = 11`, `gapM = 1`; bản trích lần lượt **150, 190, 1100, 100 cm**. Bán kính nền **S 200, M 230, L 270, XL 350 cm**. Kiểm đủ **1 rect nước, 2 rect cầu, 3 nút tài nguyên** với từng trường chính xác.
- Hai tuyến lấy trực tiếp từ `groundLanes`: **476/459 điểm**, dài **11880/11472 cm**, đúng ba điểm đầu và ba điểm cuối. Test tự tạo lại Lane và so mọi tọa độ mẫu với `xs/zs`: độ lệch lớn nhất **0,4999461656384483 cm**, đạt cả ngưỡng **≤ 1 cm** và **≤ 0,5 cm**.
- Rồng: bản trích bằng toàn bộ khối JSON vàng độc lập trong test. Kiểm **37 giá trị làn**, **132 giá trị tổng**, **0 giá trị không chia hết cho 600 u**; **17 ô = 7 trap + 4 block + 6 house**, trong đó **11 ô làn**. `STAGE_M0.lanes = ["cau","suoi","troi"]`.
- Test 7: cả `gameRepo("dragon-hold")` và `dragon.extract()` đều từ chối thư mục rỗng trong `.cache/empty-games`; biến môi trường được trả lại trong `finally`.

### Kiểm 5 · Sửa cây trong RAM

Nằm trong test 4 của lệnh kiểm 1:

```text
Tree 7: [250,-4450] -> [251,-4450]; hash=40ece390508961dfe18cd8d64de20c8d98e0382bc5327810a6a60064904e3784
```

Sao sâu `SLICE_1A` bằng `structuredClone`, cộng **0,01 m** vào x của cây 7. Băm khác băm vàng; mọi khóa ngoài `trees`, `hash` giống hệt; các cây còn lại cũng giống hệt. Không sửa nội dung trên đĩa.

### Kiểm 6 · Repo game không đổi trạng thái

Kiểm tự động trong test 6 đạt ngay **lần 1** ở cả hai game; không cần thử lại, không có dòng lệch.

Kiểm tay bổ sung: giữ stdout của hai lệnh dưới đây trước cặp lượt `all --write` ở kiểm 2, rồi chạy lại sau cả hai lượt và so bằng phép so chuỗi nghiêm ngặt:

```text
git --no-optional-locks -C /Users/toandx/htdocs/typing-game/games/typing-defense status --porcelain=v1
 M src/content/rules.ts
 M src/sim/systems/attention.ts
 M tests/td-balance-gates.test.ts
 M tests/td/balance.ts
Exit code: 0
before === after: true

git --no-optional-locks -C /Users/toandx/htdocs/typing-game/games/dragon-hold status --porcelain=v1
M  src/content/data/waves.ts
Exit code: 0
before === after: true
```

Đây là các thay đổi sẵn có của làn khác ở checkout chính, đã thấy từ lúc bắt đầu. Không sửa, hoàn tác hoặc ghi vào repo game.

### Kiểm 7 · Mẫu bỏ qua đúng phạm vi

Ba lệnh được gọi riêng:

```text
git check-ignore -q tools/map-factory/.cache/x
Exit code: 0

git check-ignore -q tools/map-factory/out/x
Exit code: 0

git check-ignore -q tools/map-factory/registry/out/assets.dragon-hold.json
Exit code: 1
```

Sổ model của phiếu 025 vẫn không bị bỏ qua.

### Kiểm 8 · Đối chiếu phạm vi ghi

Lệnh đầu tiên, chạy trước mọi lần ghi:

```text
git status --short --untracked-files=all
Không có stdout; worktree sạch.
Exit code: 0
```

Lệnh cuối:

```text
git status --short --untracked-files=all
?? docs/codex-queue/028-report.md
?? tools/map-factory/.gitignore
?? tools/map-factory/adapters/dragon-hold.mjs
?? tools/map-factory/adapters/extract.mjs
?? tools/map-factory/adapters/typing-defense.mjs
?? tools/map-factory/lib/ts-hook.mjs
?? tools/map-factory/test/adapters.test.mjs
?? tools/map-factory/test/fixtures/gameplay/dragon-hold.L2-cau.json
?? tools/map-factory/test/fixtures/gameplay/typing-defense.w1-silverfall.json
Exit code: 0
```

Chỉ thêm đúng **9 file được phép**, **0 dòng sửa hoặc xóa mới**, **0 file ngoài phạm vi**; `.cache` không hiện. Các file phiếu 027, `shared/game-kit/**` và `registry/**` không đổi.

```text
git diff --check
Không có stdout.
Exit code: 0
```

## 3. Thời gian và lựa chọn triển khai

```text
node tools/map-factory/adapters/extract.mjs all
Exit code: 0; elapsedMs=310.160; stdout=15535 bytes
```

Đo bằng `performance.now()` quanh một tiến trình Node con; gồm trích lại cả hai archive và tạo stdout, không ghi fixture. Đây là số đo một lượt, không phải cổng hiệu năng.

- CLI dùng `import()` động và gọi `main(...).catch(...)`, không giữ top-level `await` chờ `main`: adapter cần import lại các hàm chung từ module CLI. Lượt thử đầu dùng top-level `await` báo vòng chờ khi module chưa đánh giá xong; đã sửa trước khi tạo fixture và chạy kiểm đạt. Không có thay đổi định dạng hoặc dữ liệu để khớp băm.
- **37 giá trị làn** gồm cả `halfWidth = 0` của làn trời và `altitude = 0` của hai làn đất. Chúng vẫn qua phép kiểm chia hết, dù không xuất thành trường không áp dụng trong JSON; như vậy đếm đúng **26 + 3 + 3 + 3 + 2 = 37**.
- `--write` chỉ nhận nguyên chuỗi PIN đầy đủ hoặc không có rev, theo yêu cầu fixture chỉ được sinh từ commit ghim. Đọc ở rev khác vẫn được phép khi không ghi.
- Kiểm 3–5 là kết quả của các test trong lệnh kiểm 1; báo cáo giữ đủ tám mục theo thứ tự phiếu. Không có lệch dữ liệu, băm hoặc định dạng so với phiếu, không có kiểm bắt buộc nào bị bỏ qua.

Không tạo ảnh hoặc âm thanh vì phiếu chỉ yêu cầu mã. Không chạy game, build, test suite của game, trình duyệt, mạng, cổng hay cài gói; không dùng lệnh Git có ghi; không đụng Tu Tiên. Không còn việc bắt buộc nào chờ chủ dự án xử lý trong phiếu này.

## Claude duyệt (28/10/2026)

Chạy lại trong worktree `map-codex`, đều đạt:
- `node --test tools/map-factory/test/*.test.mjs` hai lần: 13/13 test, 0 bỏ qua. Hai fixture khớp sha256 của phiếu (`ad67509d…`, `71160a56…`). Hai repo game không đổi trạng thái: dòng `waves.ts` của Rồng là của làn Rồng, có từ trước.
- `vitest run map`: 6 file, 185 test. `tsc -p map/tsconfig.json`: sạch.
- Toàn kit: 42 file, 474 test. `tsc`: sạch.
- EDT là Meijster bằng số nguyên. Phép chia duy nhất là `Math.floor` của hai số nguyên dưới 2^26, nên kết quả chính xác trên mọi engine. Lõi không có lượng giác hay số ngẫu nhiên.
