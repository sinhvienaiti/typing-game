# Phiếu 031 · Map Factory · MapSpec v0

Ngày thực hiện: 28/10/2026. Worktree: `/Users/toandx/htdocs/typing-game-wt/map-codex`, nhánh `map-factory`, HEAD `1befb22c` giữ nguyên. Chỉ thực hiện phần mã; không dùng mạng, cổng, trình duyệt hoặc dev server; không chạy build hay bộ test của game.

Đã hoàn tất **9/9 mục kiểm**. Bộ map đạt **8 file, 302 test** ở hai lượt nghiệm thu; toàn bộ game-kit đạt **44 file, 591 test**. Node đạt **34 test, skipped 0** ở cả hai lượt. Hai specHash và toàn bộ 11 hash byte đúng số vàng; bảy spec hỏng mỗi spec đúng một lỗi.

## 1. Các file đã viết

- `shared/game-kit/map/sha256.ts`: SHA-256 đồng bộ thuần TypeScript theo FIPS 180-4, bộ nhớ làm việc cố định, giới hạn đầu vào 0xffffffff byte.
- `shared/game-kit/map/spec.ts`: Hằng và kiểu MapSpec v0; kiểm cấu trúc, hậu tố đơn vị và ngữ cảnh; JSON chuẩn và specHash.
- `shared/game-kit/map/sha256.test.ts`: 16 test: bốn vector FIPS, chín biên đệm, 200 dãy seed đối chiếu node:crypto, subarray và giới hạn độ dài.
- `shared/game-kit/map/spec.test.ts`: 101 test: JSON chuẩn, kiểm chéo 028, số vàng, hai mẫu, bảy spec hỏng, đủ 63 đột biến, mã lỗi và kiểm không suy diễn nghĩa.
- `shared/game-kit/map/index.ts`: Chỉ thêm hai dòng export cho toàn bộ hàm, hằng và kiểu của phiếu; giữ nguyên các dòng cũ.
- `tools/map-factory/cli.mjs`: Lệnh validate, nạp TypeScript động sau hook, stdout ổn định và mã thoát 0/1/2; build/check báo để phiếu 032.
- `tools/map-factory/lib/spec-context.mjs`: Nạp fixture có kiểm hash, nạp kit, đối chiếu hai tier runtime trong sổ 025 và gom lỗi đọc/JSON vào problems.
- `tools/map-factory/registry/kits/meadow.json`: Kit v0 meadow@1 đúng byte: 18 proto, mọi asset là null.
- `tools/map-factory/registry/kits/pine-river.json`: Kit v0 pine-river@1 đúng byte: 12 proto có đủ high và medium trong sổ 025.
- `tools/map-factory/maps/typing-defense/w1-silverfall/map.spec.json`: Chép nguyên khối JSON đầu §8.1 từ tài liệu bằng script trong RAM, giữ một newline cuối.
- `tools/map-factory/maps/dragon-hold/L2-cau/map.spec.json`: Chép nguyên khối JSON Rồng §8.1 bằng cùng script, giữ một newline cuối.
- `tools/map-factory/test/cli.test.mjs`: 21 test mới cho CLI, context, lỗi kit/fixture, tính lặp lại và 11 hash byte; cùng 13 test cũ thành 34 test.
- `tools/map-factory/test/fixtures/bad-spec/fractional-number/map.spec.json`: Một thay thế wobbleCm thành 40.5, kiểm not-integer.
- `tools/map-factory/test/fixtures/bad-spec/density-over-1000/map.spec.json`: Một thay thế densityPermille thành 1200, kiểm permille-range.
- `tools/map-factory/test/fixtures/bad-spec/unknown-proto/map.spec.json`: Một thay thế thêm mix chứa pine-giant, kiểm proto-unknown.
- `tools/map-factory/test/fixtures/bad-spec/gameplay-hash-mismatch/map.spec.json`: Một thay thế ký tự cuối gameplay.hash, kiểm gameplay-hash-mismatch.
- `tools/map-factory/test/fixtures/bad-spec/bad-pin-id/map.spec.json`: Một thay thế chuỗi keep mất dấu gạch dưới, kiểm pin-id-format.
- `tools/map-factory/test/fixtures/bad-spec/missing-budget/map.spec.json`: Một thay thế đoạn cuối loại budget và dấu phẩy, kiểm budget-missing.
- `tools/map-factory/test/fixtures/bad-spec/odd-cell/map.spec.json`: Một thay thế cellCm thành 45, kiểm cell-not-even.
- `docs/codex-queue/031-report.md`: Báo cáo này, ghi kết quả chín mục kiểm và phạm vi thay đổi.

File tạm chỉ nằm dưới `tools/map-factory/.cache/**`, gồm fixture JSON lỗi, bản lớp chơi sửa trong RAM rồi ghi vào cache, kit/sổ giả để kiểm lỗi và cây trích của test 028. `.cache` được Git bỏ qua. CLI validate không ghi file.

## 2. Điều kiện trước khi ghi

Lệnh đầu tiên:

```text
git status --short --untracked-files=all
(stdout rỗng)
Exit code: 0
```

Worktree ban đầu sạch, không có file phiếu hay file làn khác chưa commit cần giữ lại. Lịch sử hiện tại đã chứa phần 027–029; kiểm trên cây hiện tại thay vì dựng lại checkpoint cũ.

```text
pnpm --dir shared/game-kit exec vitest run map
Map core files (5): edt.ts, hash.ts, index.ts, raster.ts, seeds.ts; violations: 0
Test Files  6 passed (6)
     Tests  185 passed (185)
Duration  2.19s
Exit code: 0

shasum -a 256 tools/map-factory/test/fixtures/gameplay/*.json
ad67509d387ba403f4cb6b1860de98266c892758e233a8b78d71a522e2a9fb37  tools/map-factory/test/fixtures/gameplay/dragon-hold.L2-cau.json
71160a56c917a195f44baff68ceee9d2aa31e31e39169697ca839d7f54fc1428  tools/map-factory/test/fixtures/gameplay/typing-defense.w1-silverfall.json
Exit code: 0
```

Hai khối JSON được tìm trong §8.1 bằng biểu thức khối fenced JSON, kiểm đúng hai khối và đúng hash byte **trước** khi ghi. Kit dựng đúng mẫu byte của phiếu. Mỗi spec hỏng dùng một phép thay thế văn bản, có assert chuỗi trước xuất hiện đúng một lần và hash sau đúng phiếu. Không gõ lại spec hoặc đổi số vàng.

## 3. Chín mục kiểm bắt buộc

### Kiểm 1 · Bộ map

```text
pnpm --dir shared/game-kit exec vitest run map
Test Files  8 passed (8)
     Tests  302 passed (302)
Duration  2.56s
Exit code: 0
```

Tăng đúng **2 file và 117 test** so với đầu việc (6 file, 185 test). Các file cũ giữ nguyên: hash 25, seeds 34, raster 46, edt 14, fields-sample 3, lint 63. Hai file mới: sha256 16, spec 101.

### Kiểm 2 · TypeScript của map

```text
pnpm --dir shared/game-kit exec tsc -p map/tsconfig.json
(không có chẩn đoán)
Exit code: 0
```

### Kiểm 3 · Lint tất định của 027

Có trong cả hai lượt Kiểm 1 và lượt toàn bộ kit:

```text
Map core files (7): edt.ts, hash.ts, index.ts, raster.ts, seeds.ts, sha256.ts, spec.ts; violations: 0
```

Đúng bảy file, không có `along.ts` trên cây hiện tại. Không sửa lint/cấu hình hay file lõi của 027–029. Import của lõi tương đối, không đuôi; import chỉ lấy kiểu trong test dùng `import type`.

### Kiểm 4 · Node CLI và adapter

```text
node --test tools/map-factory/test/*.test.mjs
ℹ tests 34
ℹ suites 0
ℹ pass 34
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 2938.646
Exit code: 0
```

13 test cũ của 028 và 21 test mới cùng đạt. Test 028 trích bằng `git archive` vào cache, chỉ đọc checkout chính; trạng thái các repo game được test xác nhận không đổi. Các thay đổi có sẵn ở repo Lời Gọi do test báo (`AGENTS.md`, hai tài liệu) được giữ nguyên.

### Kiểm 5 · Lệnh tay, stdout và mã thoát

Mọi stdout bên dưới kết thúc bằng newline. Chín lệnh validate có stderr rỗng.

```text
$ node tools/map-factory/cli.mjs validate tools/map-factory/maps/typing-defense/w1-silverfall
ok d304337326698ceb407b6352e2c2ba8bffcb0effe53358cc7347e3be877e6f16
exit=0

$ node tools/map-factory/cli.mjs validate tools/map-factory/maps/dragon-hold/L2-cau
ok e77ce877fbcf6acb4baa04818249b770276d3c9a71ba508913bc85af64f6db83
exit=0

$ node tools/map-factory/cli.mjs validate tools/map-factory/test/fixtures/bad-spec/fractional-number
error not-integer "/layers/water/streams/0/wobbleCm"
exit=1

$ node tools/map-factory/cli.mjs validate tools/map-factory/test/fixtures/bad-spec/density-over-1000
error permille-range "/layers/vegetation/groves/densityPermille"
exit=1

$ node tools/map-factory/cli.mjs validate tools/map-factory/test/fixtures/bad-spec/unknown-proto
error proto-unknown "/layers/vegetation/groves/mix/pine-giant"
exit=1

$ node tools/map-factory/cli.mjs validate tools/map-factory/test/fixtures/bad-spec/gameplay-hash-mismatch
error gameplay-hash-mismatch "/gameplay/hash"
exit=1

$ node tools/map-factory/cli.mjs validate tools/map-factory/test/fixtures/bad-spec/bad-pin-id
error pin-id-format "/pins/0/keep"
exit=1

$ node tools/map-factory/cli.mjs validate tools/map-factory/test/fixtures/bad-spec/missing-budget
error budget-missing "/budget"
exit=1

$ node tools/map-factory/cli.mjs validate tools/map-factory/test/fixtures/bad-spec/odd-cell
error cell-not-even "/extent/cellCm"
exit=1

$ node tools/map-factory/cli.mjs
stdout=""
stderr=Usage: node tools/map-factory/cli.mjs validate <spec-directory>
exit=2
```

| Spec | Byte UTF-8 canonicalJson | specHash thực tế | Số vàng của phiếu |
| --- | ---: | --- | --- |
| w1-silverfall | 3189 | `d304337326698ceb407b6352e2c2ba8bffcb0effe53358cc7347e3be877e6f16` | `d304337326698ceb407b6352e2c2ba8bffcb0effe53358cc7347e3be877e6f16` |
| L2-cau | 1145 | `e77ce877fbcf6acb4baa04818249b770276d3c9a71ba508913bc85af64f6db83` | `e77ce877fbcf6acb4baa04818249b770276d3c9a71ba508913bc85af64f6db83` |

Kiểm chéo canonicalJson + SHA-256 của lõi với hai fixture 028 cũng đạt: `7faeaa7c0d5bf39803019444b1ae8056c36d3914a916a74baaed834e76ef4b23` và `c852b4d70147c8d2bf87f22999334f090646d0ae87bde6a9873b35de45d9659a`.

### Kiểm 6 · Lặp lại

```text
pnpm --dir shared/game-kit exec vitest run map
Test Files  8 passed (8)
     Tests  302 passed (302)
Duration  1.88s
Exit code: 0

node --test tools/map-factory/test/*.test.mjs
ℹ tests 34
ℹ suites 0
ℹ pass 34
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 2401.303875
Exit code: 0
```

Đã chạy lại đủ mười lệnh tay ở Kiểm 5 bằng subprocess và so sánh nguyên stdout/stderr cùng mã thoát với kết quả lượt đầu. Kết quả:

```text
Second manual pass: all 10 exit codes and stdout/stderr bytes match the first pass.
```

Hai lần CLI cho mỗi mẫu trong `cli.test.mjs` cũng so sánh nguyên stdout, không chỉ hash đã cắt gọn.

### Kiểm 7 · Phần còn lại của game-kit

Chạy hai lệnh **lần lượt**, đợi Vitest kết thúc rồi mới chạy TypeScript:

```text
pnpm --dir shared/game-kit exec vitest run
Test Files  44 passed (44)
     Tests  591 passed (591)
Duration  3.53s
Exit code: 0

pnpm --dir shared/game-kit exec tsc -p tsconfig.json --noEmit
(không có chẩn đoán)
Exit code: 0
```

Không có test cũ hết hạn; không cần chạy lại bộ đầy đủ hoặc sửa test ngoài phạm vi. Mức tăng tương ứng mốc phiếu: 42 → 44 file, 474 → 591 test.

### Kiểm 8 · Đúng byte của hai mẫu, hai kit và bảy spec hỏng

```text
shasum -a 256 tools/map-factory/maps/typing-defense/w1-silverfall/map.spec.json tools/map-factory/maps/dragon-hold/L2-cau/map.spec.json tools/map-factory/registry/kits/meadow.json tools/map-factory/registry/kits/pine-river.json tools/map-factory/test/fixtures/bad-spec/*/map.spec.json
4c60f45b2eaaf8d8b56124eb0ffad60102510f4dacfd8d033a52a60b2da799a0  tools/map-factory/maps/typing-defense/w1-silverfall/map.spec.json
2d4620366e5942352f8eee34a7e2dc853b8746e85bdfbea1964dee0f43e26030  tools/map-factory/maps/dragon-hold/L2-cau/map.spec.json
ffe6a5eac17e103509f29e90615bc31e57e551c9a7f8177a644ab6dca8b954da  tools/map-factory/registry/kits/meadow.json
f8e574c5e4abc773ec3204f912af218d05f24ce13257773db974e9d8bc0ee73a  tools/map-factory/registry/kits/pine-river.json
c8cd22b18ae7389ccf38846a7cfb4facdc23694f3411001024415dc5ad48705b  tools/map-factory/test/fixtures/bad-spec/bad-pin-id/map.spec.json
3b9eb49201b8dd62b3f65da14f9f9381ab3bb6fd18a1518dd96e4cbfef39e39a  tools/map-factory/test/fixtures/bad-spec/density-over-1000/map.spec.json
193be3e3f5a1f460009efd4e1353c3dce9cccc7e8f4fb267354e6397e61630dd  tools/map-factory/test/fixtures/bad-spec/fractional-number/map.spec.json
7436981da69c115b957d741b40c57016481a3125b6fe6282a67645596d689090  tools/map-factory/test/fixtures/bad-spec/gameplay-hash-mismatch/map.spec.json
a099fd032dae6ad16b6df644cb4e1f45532a5e13de1820eb08da7498fc45346e  tools/map-factory/test/fixtures/bad-spec/missing-budget/map.spec.json
ab61bbfd7da596abdc38bdc433cfade00f8d6a6850ba1ccd304e9173569355ea  tools/map-factory/test/fixtures/bad-spec/odd-cell/map.spec.json
559d3eda596ff2551cdb07096c53c467dfa5a10ffb769228966e145348fc1254  tools/map-factory/test/fixtures/bad-spec/unknown-proto/map.spec.json
Exit code: 0
```

Cả 11 giá trị đúng phiếu; test Node cuối cũng kiểm riêng từng giá trị. Hai fixture lớp chơi được băm lại ở cuối và giữ nguyên hash đầu việc.

### Kiểm 9 · Phạm vi Git

So với stdout rỗng lúc bắt đầu, chỉ có thêm 19 file được phép và sửa `index.ts`. Kết quả sau khi tạo báo cáo:

```text
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

$ git check-ignore tools/map-factory/.cache/cli-test/broken-json/map.spec.json
tools/map-factory/.cache/cli-test/broken-json/map.spec.json
Exit code: 0

$ git diff --check
(stdout rỗng)
Exit code: 0
```

Không có dòng M/D mới ngoài `index.ts`, không có thay đổi file bảo vệ của 027–029 hoặc sổ 025. Diff của `index.ts` chỉ thêm hai dòng export. Không chạy lệnh Git ghi, không ghi vào checkout chính hoặc `games/**`, không đụng Tu Tiên.

## 4. Cách hiểu, lỗi trong lúc phát triển và phần để lại

- Không có lệch với luật, bảng đột biến hoặc số vàng của phiếu. Khối lớp chỉ kiểm JSON/số nguyên, hậu tố đơn vị và ba khóa cấu trúc `id`, `proto`, `mix`; mọi chuỗi tham chiếu gameplay và cặp min/max giữ nguyên nghĩa chưa xác định. Có test khẳng định `count: [9, 6]` và tham chiếu không tồn tại vẫn qua.
- Mẫu JSON được tìm theo nội dung §8.1 thay vì số dòng; nội dung không đổi. Không cần hỏi chủ dự án.
- Hàm nạp chỉ đưa bản trích/kit đã qua kiểm vào danh sách ngữ cảnh; mọi lỗi môi trường vẫn được gom để CLI thoát 2. Sổ model được đọc một lần mỗi game trong một lượt loadKits. Cách này không thêm luật vào MapSpec.
- Một lượt TypeScript trong khi đang viết báo TS18046 do thu hẹp kiểu của `registry` không giữ trong callback; đã giữ tên kit ở biến cục bộ. Một lượt Vitest trong khi dựng test lỗi ở tên ca `%j` khi formatter cố JSON.stringify BigInt (7 file/201 test đã qua, spec.test chưa thu thập được); đã sửa dữ liệu ca thành object chứa `value` và dùng chỉ số làm nhãn. Hai lượt nghiệm thu sau đó đều đạt đầy đủ; không sửa test cũ hoặc nới kết quả mong đợi.
- `rg` không có trên máy; dùng Python/find để tìm và đọc file. Không cài gói.
- Để lại `cli build` và `cli check` cho phiếu 032, đúng thông báo chưa triển khai và mã thoát 2. Luật thực vật/lối mòn/sơn đất, bố cục và kit đầy đủ để sau spike như phiếu yêu cầu.
- Không tạo hình/âm thanh vì phiếu chỉ yêu cầu mã. Không thực hiện browser QA hoặc test/build của game vì nằm ngoài phạm vi được giao.

Chủ dự án có thể xem diff mã và báo cáo này; không còn mục kiểm thủ công bắt buộc hoặc blocker của phiếu 031.

## Claude duyệt (28/10/2026)

Chạy lại trong worktree `map-codex`, đều đạt:
- `vitest run map`: 9 file, 384 test.
- Toàn kit: 45 file, 673 test. Hai lệnh `tsc` sạch.
- `node --test tools/map-factory/test/*.test.mjs`: 34 test, 0 bỏ qua.
- `cli validate`: hai spec mẫu thoát 0 và in `ok <specHash>`. Bảy spec hỏng mỗi spec thoát 1 với đúng một dòng `error <code> "<path>"` như phiếu. Thư mục không có hoặc thiếu đối số thì thoát 2.
- Lõi (`spec.ts`, `sha256.ts`, `along.ts`) không có lượng giác, `sqrt` hay số ngẫu nhiên. SHA-256 viết thuần TS, nên chạy được trong trình duyệt.
