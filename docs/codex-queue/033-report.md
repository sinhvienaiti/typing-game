# Phiếu 033 · Đặt vật dọc đường gấp khúc bằng số nguyên

Hoàn thành trong worktree `/Users/toandx/htdocs/typing-game-wt/map-codex`. Chỉ ghi bốn đường dẫn được phép. Không chạy trình duyệt, máy chủ, mạng, build hay bộ test của game; không cài gói và không chạy lệnh Git có ghi.

## File đã viết

- `shared/game-kit/map/along.ts`: API hình học cung, chia nguyên, căn nguyên nhị phân, bảng góc, đặt vật với rung/cửa sổ cấm và băm một lần qua `hash32`; không có giá trị mặc định mang nghĩa bố cục.
- `shared/game-kit/map/along.test.ts`: 82 test, gồm bản BigInt độc lập dùng căn Newton, ba đường vàng, 100 đường có seed, tính chất hình học, kiểm đầu vào và kiểm chuỗi cấm.
- `shared/game-kit/map/index.ts`: chỉ thêm một dòng export cho đủ 18 tên của API, giữ nguyên mọi dòng đã có, kể cả export phiếu 031.
- `docs/codex-queue/033-report.md`: báo cáo này.

## Điều kiện trước khi ghi

Lệnh đầu tiên, đã giữ nguyên stdout để so ở Kiểm 8:

```text
git status --short --untracked-files=all
 M shared/game-kit/map/index.ts
?? docs/codex-queue/031-report.md
?? shared/game-kit/map/sha256.test.ts
?? shared/game-kit/map/sha256.ts
?? shared/game-kit/map/spec.test.ts
?? shared/game-kit/map/spec.ts
?? tools/map-factory/cli.mjs
?? tools/map-factory/lib/spec-context.mjs
?? tools/map-factory/maps/dragon-hold/L2-cau/map.spec.json
?? tools/map-factory/maps/typing-defense/w1-silverfall/map.spec.json
?? tools/map-factory/registry/kits/meadow.json
?? tools/map-factory/registry/kits/pine-river.json
?? tools/map-factory/test/cli.test.mjs
?? tools/map-factory/test/fixtures/bad-spec/bad-pin-id/map.spec.json
?? tools/map-factory/test/fixtures/bad-spec/density-over-1000/map.spec.json
?? tools/map-factory/test/fixtures/bad-spec/fractional-number/map.spec.json
?? tools/map-factory/test/fixtures/bad-spec/gameplay-hash-mismatch/map.spec.json
?? tools/map-factory/test/fixtures/bad-spec/missing-budget/map.spec.json
?? tools/map-factory/test/fixtures/bad-spec/odd-cell/map.spec.json
?? tools/map-factory/test/fixtures/bad-spec/unknown-proto/map.spec.json
Exit code: 0
```

Các dòng trên thuộc công việc có sẵn, không sửa/xóa. Đã lưu SHA-256 của cả 20 file trong trạng thái đầu việc; đối chiếu lại 19 file ngoài `index.ts` giữ nguyên byte. Với `index.ts`, bỏ đúng dòng export mới thì nội dung bằng nguyên văn đầu việc.

```text
pnpm --dir shared/game-kit exec vitest run map
Test Files  8 passed (8)
     Tests  302 passed (302)
Duration  1.64s
Exit code: 0

shasum -a 256 tools/map-factory/test/fixtures/gameplay/*.json
ad67509d387ba403f4cb6b1860de98266c892758e233a8b78d71a522e2a9fb37  tools/map-factory/test/fixtures/gameplay/dragon-hold.L2-cau.json
71160a56c917a195f44baff68ceee9d2aa31e31e39169697ca839d7f54fc1428  tools/map-factory/test/fixtures/gameplay/typing-defense.w1-silverfall.json
Exit code: 0
```

Hai hash file đúng phiếu. Test mới còn kiểm trường `hash` tương ứng là `c852b4d70147c8d2bf87f22999334f090646d0ae87bde6a9873b35de45d9659a` và `7faeaa7c0d5bf39803019444b1ae8056c36d3914a916a74baaed834e76ef4b23`, với lời nhắn “chạy lại phiếu 028” nếu sai.

## Tám kiểm bắt buộc

### Kiểm 1 · Map đạt, tăng đúng một file

```text
pnpm --dir shared/game-kit exec vitest run map
✓ map/along.test.ts (82 tests)
Test Files  9 passed (9)
     Tests  384 passed (384)
Duration  2.86s
Exit code: 0
```

Mốc đầu việc 8 file/302 test → 9 file/384 test: thêm đúng một file và 82 test. Có một lượt kiểm trong lúc phát triển đạt 9 file/383 test; sau khi bổ sung test lỗi đầu vào của `alongHash`, hai lượt cuối đều đạt 384 test.

### Kiểm 2 · TypeScript của map

```text
pnpm --dir shared/game-kit exec tsc -p map/tsconfig.json
(không có chẩn đoán)
Exit code: 0
```

### Kiểm 3 · Lint tất định của phiếu 027

Trong lệnh Kiểm 1:

```text
Map core files (8): along.ts, edt.ts, hash.ts, index.ts, raster.ts, seeds.ts, sha256.ts, spec.ts; violations: 0
```

Có đủ mọi file lõi đầu việc và `along.ts`. Test đọc nguyên văn `along.ts` xác nhận không có chuỗi `Math.sqrt`, kể cả trong chú thích. Phép chia số học duy nhất của lõi nằm trong `floorDiv`.

### Kiểm 4 · Ba đường vàng

Các giá trị dưới đây lấy từ lượt test cuối, đặt cạnh giá trị của phiếu; mọi ô đều khớp.

| Đường | total thực tế | total phiếu | Số vật thực tế | Số vật phiếu | alongHash thực tế | alongHash phiếu |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| td-route0 | 12163917 | 12163917 | 14 | 14 | 1811293709 | 1811293709 |
| dh-cau | 2517567 | 2517567 | 12 | 12 | 1575973982 | 1575973982 |
| synthetic | 31636035 | 31636035 | 808 | 808 | 440583006 | 440583006 |

Mỗi vật ghi theo `[k,s,seg,x,z,yawDeg,offsetCm]`:

| Đường / vật | Thực tế | Phiếu |
| --- | --- | --- |
| td-route0 / 1 | `[1,1075200,41,-113,-4160,23,-280]` | `[1,1075200,41,-113,-4160,23,-280]` |
| td-route0 / 2 | `[2,1843200,71,287,-3370,37,280]` | `[2,1843200,71,287,-3370,37,280]` |
| td-route0 / 3 | `[3,2611200,101,422,-2801,149,-280]` | `[3,2611200,101,422,-2801,149,-280]` |
| td-route0 / cuối | `[15,11827200,461,417,3942,133,-280]` | `[15,11827200,461,417,3942,133,-280]` |
| dh-cau / 1 | `[0,74752,0,991,-2741,118,-200]` | `[0,74752,0,991,-2741,118,-200]` |
| dh-cau / 2 | `[1,204800,0,931,-2629,118,-200]` | `[1,204800,0,931,-2629,118,-200]` |
| dh-cau / 3 | `[2,276480,0,898,-2567,118,-200]` | `[2,276480,0,898,-2567,118,-200]` |
| dh-cau / cuối | `[19,2373632,3,264,-699,101,-200]` | `[19,2373632,3,264,-699,101,-200]` |
| synthetic / 1 | `[1,30720,1,30,-45,0,-45]` | `[1,30720,1,30,-45,0,-45]` |
| synthetic / 2 | `[2,89088,1,87,45,0,45]` | `[2,89088,1,87,45,0,45]` |
| synthetic / 3 | `[6,220160,1,215,45,0,45]` | `[6,220160,1,215,45,0,45]` |
| synthetic / cuối | `[811,30709760,11,15689,-15803,317,-45]` | `[811,30709760,11,15689,-15803,317,-45]` |

Test kiểm thêm: td-route0 có 475 đoạn, bốn độ dài đầu `25353,25353,26107,25353`; dh-cau có `755959,781534,562362,417712`; synthetic có `0,1024000,1024,715776,1013708,0,1158524,0,1228800,1228800,1013708,24251695`. Rung k=0…3 đúng lần lượt `13,20,-30,-27` và `-2,-7,13,4`; hash rung đầu của dh-cau là `2665129022`. Không thay số vàng để khớp mã.

Test gọi `placeAlong` hai lần cho từng đường vàng và so bằng từng phần tử. Băm mảng rỗng đúng `2872998923`.

### Kiểm 5 · BigInt và các tính chất

Dòng stdout trong lệnh Kiểm 1, giữ nguyên ở lượt Kiểm 6:

```text
Map core files (8): along.ts, edt.ts, hash.ts, index.ts, raster.ts, seeds.ts, sha256.ts, spec.ts; violations: 0
along roots: 22002 inputs; 10000 seeded
along yaw: 381200 vectors; max=0.499990793deg; different=0
along golden td-route0: total=12163917; items=14; hash=1811293709; edges=[[1,1075200,41,-113,-4160,23,-280],[2,1843200,71,287,-3370,37,280],[3,2611200,101,422,-2801,149,-280],[15,11827200,461,417,3942,133,-280]]
along golden dh-cau: total=2517567; items=12; hash=1575973982; edges=[[0,74752,0,991,-2741,118,-200],[1,204800,0,931,-2629,118,-200],[2,276480,0,898,-2567,118,-200],[19,2373632,3,264,-699,101,-200]]
along golden synthetic: total=31636035; items=808; hash=440583006; edges=[[1,30720,1,30,-45,0,-45],[2,89088,1,87,45,0,45],[6,220160,1,215,45,0,45],[811,30709760,11,15689,-15803,317,-45]]
along errors td-route0: arc=0.526497559cm; side=0.428899920cm; yaw=0.498565676deg
along errors dh-cau: arc=0.574439165cm; side=0.262327960cm; yaw=0.491477012deg
along errors synthetic: arc=0.701951017cm; side=0.276925691cm; yaw=0.224425926deg
along BigInt/properties: routes=103; items=17621; maxArc=0.708027956cm; maxSide=0.840979371cm; maxYaw=0.499872366deg
```

Căn nguyên: 10.000 số có seed ghép hai lần `next()`, cộng các số kề bình phương ở hai miền yêu cầu, tổng 22.002 đầu vào. Cả căn sàn và căn làm tròn đều bằng bản Newton BigInt.

Góc: đúng 381.200 vectơ, sai số vòng lớn nhất 0,499990793°, số vectơ khác `Math.round(a) % 360` là **0**. Bảng có đúng 45 literal và bằng từng giá trị tính bằng `Math.tan` trong test.

BigInt: **103 đường, 17.621 vật**, bằng từng trường. Bản đối chiếu dùng số nguyên lớn cho toàn bộ phép hình học, chia sàn có sửa số âm, căn Newton và bảng tan của lõi; chọn đoạn bằng quét ngược, độc lập với con trỏ đi tới của lõi. Chỉ chuyển sang Number tại ranh giới gọi `hash32` và lúc dựng kết quả so sánh.

Các tính chất đều đạt: `s` và `k` tăng ngặt; rung nguyên cm đúng miền; khoảng cách cung nguyên chính xác khi không rung và k liền nhau; đủ/đúng mọi ứng viên và cửa sổ đóng sau rung; dấu lệch ngang theo k gốc; không có `-0`; sai số cung số thực, độ dài lệch ngang và góc trong công thức của phiếu. Với ba đường vàng, cung và ngang đều ≤ 1 cm.

| Tập đường | Cung lớn nhất (cm) | Ngang lớn nhất (cm) | Góc lớn nhất (°) |
| --- | ---: | ---: | ---: |
| td-route0 | 0,526497559 | 0,428899920 | 0,498565676 |
| dh-cau | 0,574439165 | 0,262327960 | 0,491477012 |
| synthetic | 0,701951017 | 0,276925691 | 0,224425926 |
| Toàn bộ 103 đường | 0,708027956 | 0,840979371 | 0,499872366 |

### Kiểm 6 · Chạy map lần thứ hai

```text
pnpm --dir shared/game-kit exec vitest run map
✓ map/along.test.ts (82 tests)
Test Files  9 passed (9)
     Tests  384 passed (384)
Duration  2.77s
Exit code: 0
```

Đã so 23 dòng stdout dữ liệu tất định giữa hai lượt cuối bằng bộ điều phối: **23/23 giống nguyên văn**, sau khi sắp để bỏ khác biệt thứ tự chạy song song của Vitest. Bao gồm mọi dòng `along`, lint, hash/field, căn/BigInt cũ.

Dòng đo thời gian cũ `field-timing` có median 7,569 ms rồi 7,265 ms; thời gian, thứ tự file và dòng `Duration` của runner cũng thay đổi theo lần chạy. Không sửa test cũ để làm các số đo thời gian giống nhau.

### Kiểm 7 · Phần còn lại của kit

Hai lệnh chạy lần lượt, TypeScript chỉ bắt đầu sau khi Vitest kết thúc:

```text
pnpm --dir shared/game-kit exec vitest run
Test Files  45 passed (45)
     Tests  673 passed (673)
Duration  3.97s
Exit code: 0

pnpm --dir shared/game-kit exec tsc -p tsconfig.json --noEmit
(không có chẩn đoán)
Exit code: 0
```

Đạt ngay lần đầu bộ đầy đủ, không có test cũ quá hạn, không cần chạy lại hay sửa file ngoài phạm vi.

### Kiểm 8 · Phạm vi Git

```text
git status --short --untracked-files=all
 M shared/game-kit/map/index.ts
?? docs/codex-queue/031-report.md
?? docs/codex-queue/033-report.md
?? shared/game-kit/map/along.test.ts
?? shared/game-kit/map/along.ts
?? shared/game-kit/map/sha256.test.ts
?? shared/game-kit/map/sha256.ts
?? shared/game-kit/map/spec.test.ts
?? shared/game-kit/map/spec.ts
?? tools/map-factory/cli.mjs
?? tools/map-factory/lib/spec-context.mjs
?? tools/map-factory/maps/dragon-hold/L2-cau/map.spec.json
?? tools/map-factory/maps/typing-defense/w1-silverfall/map.spec.json
?? tools/map-factory/registry/kits/meadow.json
?? tools/map-factory/registry/kits/pine-river.json
?? tools/map-factory/test/cli.test.mjs
?? tools/map-factory/test/fixtures/bad-spec/bad-pin-id/map.spec.json
?? tools/map-factory/test/fixtures/bad-spec/density-over-1000/map.spec.json
?? tools/map-factory/test/fixtures/bad-spec/fractional-number/map.spec.json
?? tools/map-factory/test/fixtures/bad-spec/gameplay-hash-mismatch/map.spec.json
?? tools/map-factory/test/fixtures/bad-spec/missing-budget/map.spec.json
?? tools/map-factory/test/fixtures/bad-spec/odd-cell/map.spec.json
?? tools/map-factory/test/fixtures/bad-spec/unknown-proto/map.spec.json
Exit code: 0
```

So với đầu việc chỉ thêm đúng ba file mới: `along.ts`, `along.test.ts`, `033-report.md`. Dòng ` M shared/game-kit/map/index.ts` đã có từ đầu, vẫn là dòng sửa duy nhất. Không thêm dòng ` M` hay ` D` khác; mọi dòng có sẵn được giữ.

Đối chiếu SHA-256 và nguyên văn export trước/sau:

```text
Baseline files unchanged: 19/19; index.ts: exactly one added export line.
```

Hai fixture được chạy lại cùng lệnh `shasum -a 256 tools/map-factory/test/fixtures/gameplay/*.json` ở cuối việc, giữ nguyên hai hash đầu việc, mã thoát 0. `git diff --check` không có đầu ra, mã thoát 0.

## Chỗ chưa rõ, lựa chọn và phần để lại

- Con số “8 nếu 031 đã chạy” ở Kiểm 1 không khớp hiện trạng: trước việc đã là **8** file test, vì vậy kết quả đúng yêu cầu tăng một là **9**. Giữ nguyên mọi file phiếu 031, không bỏ test để ép còn 8.
- “Cùng các dòng in” ở Kiểm 6 được hiểu là các dòng dữ liệu tất định; đo thời gian trong test cũ và runner luôn dao động. Đã ghi riêng số đo khác nhau ở trên, không tuyên bố toàn stdout giống byte.
- Chọn đoạn bằng danh sách đoạn dương và con trỏ đi tới vì rung giữ thứ tự. Đỉnh thuộc đoạn đi ra; đầu/cuối đường với điểm trùng đều đúng định nghĩa. Đây là lựa chọn triển khai, không đổi thuật toán.
- Phiếu không quy định cách ghép hai lần `next()` cho mẫu căn: test ghép uint64 bằng BigInt rồi lấy dư `2^52 + 1`, bao gồm miền hai đầu; các biên bình phương được kiểm riêng. Với 100 đường, lấy mỗi k chia hết cho 3 làm đường ngắn, dùng bước cộng [-3;3], các cửa sổ lấy hai đầu ngẫu nhiên rồi sắp cặp.
- `alongHash` kiểm hình dạng mảng/vật và bảy số trong miền số của `hash32` để đầu vào sai trả `RangeError`; vẫn gọi `hash32` đúng một lần theo thứ tự bảy trường.
- Không làm lớp dressing, đọc spec, chọn tuyến/proto, đổi `skipNearCm`, `maxRun`, `clearOnBuild`, luật khoảng cách từ spike hay tích hợp game: các phần đó nằm ngoài phiếu. Không đụng Tu Tiên, fixture hay file của agent khác.
- Không có chênh lệch số vàng hay sai số vượt công thức; không có lỗi sẵn có ngoài phạm vi cần sửa. Chủ dự án chỉ cần lưu ý hai điểm đếm file và dòng thời gian ở trên.


## Claude duyệt (28/10/2026)

Chạy lại trong worktree `map-codex`, đều đạt:
- `vitest run map`: 9 file, 384 test.
- Toàn kit: 45 file, 673 test. Hai lệnh `tsc` sạch.
- `node --test tools/map-factory/test/*.test.mjs`: 34 test, 0 bỏ qua.
- `cli validate`: hai spec mẫu thoát 0 và in `ok <specHash>`. Bảy spec hỏng mỗi spec thoát 1 với đúng một dòng `error <code> "<path>"` như phiếu. Thư mục không có hoặc thiếu đối số thì thoát 2.
- Lõi (`spec.ts`, `sha256.ts`, `along.ts`) không có lượng giác, `sqrt` hay số ngẫu nhiên. SHA-256 viết thuần TS, nên chạy được trong trình duyệt.
