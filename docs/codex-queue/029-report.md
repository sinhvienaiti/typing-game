# Phiếu 029 · Map Factory · Tô hình và biến đổi khoảng cách số nguyên

Ngày thực hiện: 28/10/2026. Worktree: `/Users/toandx/htdocs/typing-game-wt/map-codex`, nhánh `map-factory`, HEAD `15601e78` giữ nguyên trong quá trình làm. Môi trường: macOS, Node **v24.22.0**, Vitest **3.2.7**. Máy M4 theo thông tin chủ dự án; lệnh đọc tên CPU bằng `sysctl` bị sandbox từ chối, không ảnh hưởng các lệnh kiểm bắt buộc.

Đã hoàn tất **8/8 mục kiểm**. Bộ map đạt **6 file, 185 test** ở hai lượt; toàn bộ kit đạt **42 file, 474 test**, không lỗi hoặc bỏ qua. Hai bộ trường khớp toàn bộ số vàng. Trung vị lượt đo riêng bộ trường Rồng: **4,190 ms**, đạt đích **≤ 60 ms**.

## 1. Các file đã viết

- `shared/game-kit/map/raster.ts`: kiểm đầu vào, tâm ô nguyên, tô đĩa/rect/đường/đa giác đóng; chỉ xét hộp bao đã cắt theo lưới, đường xét từng đoạn; giữ phép hợp trên mask.
- `shared/game-kit/map/edt.ts`: EDT bình phương chính xác bằng hai pha Meijster, O(w·h), bộ nhớ đệm dùng lại và kết quả mới mỗi lần gọi.
- `shared/game-kit/map/index.ts`: chỉ thêm hai dòng export, giữ nguyên hai dòng cũ.
- `shared/game-kit/map/raster.test.ts`: 13 ca tính tay, 200 ca seed so BigInt, biên số lớn, phép hợp và đầu vào sai.
- `shared/game-kit/map/edt.test.ts`: 3 ca tính tay, 200 lưới seed so vét cạn, quyền sở hữu kết quả/bộ đệm, kích thước tối đa và đầu vào sai.
- `shared/game-kit/map/fields-sample.test.ts`: kiểm fixture, dựng/băm hai bộ trường mẫu hai lần, kiểm số vàng và đo thời gian.
- `docs/codex-queue/029-report.md`: báo cáo này.

## 2. Điều kiện trước khi ghi mã

Lệnh đầu tiên là `git status --short --untracked-files=all`; kết quả được giữ nguyên ở mục Kiểm 8. Sau đó chạy:

```text
pnpm --dir shared/game-kit exec vitest run map
Map core files (3): hash.ts, index.ts, seeds.ts; violations: 0
Test Files  3 passed (3)
     Tests  122 passed (122)
Duration  5.36s
Exit code: 0
```

Kiểm cả byte file và trường `hash` trước khi ghi mã; test bộ trường tiếp tục khẳng định lại ở mọi lượt chạy:

```text
shasum -a 256 tools/map-factory/test/fixtures/gameplay/dragon-hold.L2-cau.json tools/map-factory/test/fixtures/gameplay/typing-defense.w1-silverfall.json
ad67509d387ba403f4cb6b1860de98266c892758e233a8b78d71a522e2a9fb37  tools/map-factory/test/fixtures/gameplay/dragon-hold.L2-cau.json
71160a56c917a195f44baff68ceee9d2aa31e31e39169697ca839d7f54fc1428  tools/map-factory/test/fixtures/gameplay/typing-defense.w1-silverfall.json
Exit code: 0
```

| Fixture | Trường `hash` đọc từ JSON | So với phiếu |
| --- | --- | --- |
| `dragon-hold.L2-cau.json` | `c852b4d70147c8d2bf87f22999334f090646d0ae87bde6a9873b35de45d9659a` | Khớp |
| `typing-defense.w1-silverfall.json` | `7faeaa7c0d5bf39803019444b1ae8056c36d3914a916a74baaed834e76ef4b23` | Khớp |

Đã chạy lại `shasum -a 256` ở cuối, hai kết quả không đổi.

## 3. Tám mục kiểm bắt buộc

### Kiểm 1 · Bộ map

```text
pnpm --dir shared/game-kit exec vitest run map
Test Files  6 passed (6)
     Tests  185 passed (185)
Duration  2.69s
Exit code: 0
```

Lượt hai, cùng lệnh, sau khi TypeScript của map đã kết thúc:

```text
Test Files  6 passed (6)
     Tests  185 passed (185)
Duration  2.73s
Exit code: 0
```

Số test theo file: `hash.test.ts` 25; `seeds.test.ts` 34; `lint.test.ts` 63; `raster.test.ts` 46; `edt.test.ts` 14; `fields-sample.test.ts` 3.

### Kiểm 2 · TypeScript của map

```text
pnpm --dir shared/game-kit exec tsc -p map/tsconfig.json
(không có chẩn đoán)
Exit code: 0
```

### Kiểm 3 · Lint của phiếu 027

Nằm trong cả hai lượt lệnh Kiểm 1, cùng dòng kết quả:

```text
Map core files (5): edt.ts, hash.ts, index.ts, raster.ts, seeds.ts; violations: 0
```

Không sửa lint hoặc cấu hình. Mã hai module mới không dùng BigInt, phép lũy thừa, trig, thời gian hoặc nguồn ngẫu nhiên; phần hình học chỉ dùng phép tính và làm tròn được phiếu cho phép. Chú thích mã bằng tiếng Anh, có giải thích giới hạn chính xác của Number và trường hợp `c*c` vượt 2^53.

### Kiểm 4 · Ca tính tay và vét cạn

Nằm trong cả hai lượt lệnh Kiểm 1:

```text
raster brute-force: 200 cases; 209439 cells compared
edt brute-force: 200 grids; 219549 cells compared
```

- **13/13** ca tô hình tính tay và **3/3** ca EDT tính tay khớp từng ô theo bảng phiếu.
- **200/200** ca tô hình bằng vét cạn BigInt ở **209.439 ô**. Mỗi ca đặt sẵn vài ô bằng 1; oracle bắt đầu từ bản sao mask đó, xét mọi ô. Oracle đường dùng `(u·u)·len2 − t²`, khác công thức tích chéo trong lõi.
- **200/200** lưới EDT bằng vét cạn ở **219.549 ô**, có đủ lưới một chiều, rỗng, đầy, một ô nguồn; không thay đổi mask đầu vào.
- Ca tô hình có seed gồm bán kính 0, rect không bề rộng, đường một điểm, điểm liền nhau trùng nhau, đa giác tự cắt, từng loại hình ở ngoài lưới và phủ lưới; `hw` có 0 và 2000. Hai test vét cạn đặt thời hạn **60.000 ms**.
- Kiểm thêm đường chéo hết miền tọa độ để tích chéo bình phương vượt 2^53; EDT **4096 × 4096** với nguồn ở góc cho khoảng cách xa nhất **33.538.050**; kết quả cũ vẫn nguyên sau các lần dùng lại bộ đệm với kích thước thay đổi.
- Các ca lỗi bắt buộc đều ném `RangeError`; kiểm thêm NaN, vô cực, số không an toàn, bán kính/half-width phân số, tọa độ sai ở cuối danh sách và mask không bị tô dở khi đầu vào sai.

### Kiểm 5 · Bộ trường mẫu và tính lặp lại

Hai lượt lệnh Kiểm 1 đều in chính xác cùng hai dòng:

```text
field-set dragon-hold.L2-cau.json ca039deb73b5dc47e0a90ba7cd354719fed12419de77c7602a44e04cae2542b4 1327159
field-set typing-defense.w1-silverfall.json 885278a7f3e1547fee5d7c0c04fde305d54cec8c4cc6cf35f6717c2090f30507 589882
```

| Fixture | SHA-256 thực tế, cả hai lượt | SHA-256 vàng | Byte thực tế / vàng |
| --- | --- | --- | ---: |
| `dragon-hold.L2-cau.json` | `ca039deb73b5dc47e0a90ba7cd354719fed12419de77c7602a44e04cae2542b4` | `ca039deb73b5dc47e0a90ba7cd354719fed12419de77c7602a44e04cae2542b4` | 1327159 / 1327159 |
| `typing-defense.w1-silverfall.json` | `885278a7f3e1547fee5d7c0c04fde305d54cec8c4cc6cf35f6717c2090f30507` | `885278a7f3e1547fee5d7c0c04fde305d54cec8c4cc6cf35f6717c2090f30507` | 589882 / 589882 |

Các dòng chi tiết và bảng đối chiếu, giống nhau ở cả hai lượt:

| Fixture | Trường | Ô mask thực tế | Ô mask vàng | Max EDT thực tế | Max EDT vàng |
| --- | --- | ---: | ---: | ---: | ---: |
| Rồng `dragon-hold.L2-cau.json` | `lanes` | 613 | 613 | 43573 | 43573 |
| Rồng `dragon-hold.L2-cau.json` | `river` | 3794 | 3794 | 38597 | 38597 |
| Rồng `dragon-hold.L2-cau.json` | `dais` | 208 | 208 | 38088 | 38088 |
| Rồng `dragon-hold.L2-cau.json` | `slots` | 445 | 445 | 33800 | 33800 |
| Lời Gọi `typing-defense.w1-silverfall.json` | `roads` | 2632 | 2632 | 8689 | 8689 |
| Lời Gọi `typing-defense.w1-silverfall.json` | `water` | 1152 | 1152 | 19881 | 19881 |
| Lời Gọi `typing-defense.w1-silverfall.json` | `keep` | 1402 | 1402 | 31705 | 31705 |
| Lời Gọi `typing-defense.w1-silverfall.json` | `blockers` | 1692 | 1692 | 5941 | 5941 |

Trong mỗi test, dựng lại bộ trường lần hai và so **toàn bộ byte** bằng `Buffer.equals`. Tên dùng UTF-8, dấu kết thúc 0, kích thước dùng `writeUInt32LE`, khoảng cách dùng `writeInt32LE`, không dựa vào thứ tự byte của máy. Rồng chỉ đọc `lanes`, bỏ `sky`; bán kính sông dùng trung bình hai bề rộng chia 4 và làm tròn xuống, đúng phiếu. Không thay số vàng.

### Kiểm 6 · Thời gian bộ trường Rồng

Đo đúng **4 trường ở 288²**, gồm tạo mask, tô hình và EDT; không gồm đọc fixture, thống kê hoặc đóng byte/băm. Mỗi lượt có **1 lần làm nóng, 5 lần đo** bằng `performance.now()`.

| Lượt | 5 số đo theo thứ tự (ms) | Trung vị (ms) |
| --- | --- | ---: |
| Bộ map lần 1 | 17,413; 5,584; 4,510; 6,605; 5,320 | 5,584 |
| Bộ map lần 2 | 7,630; 3,719; 6,808; 3,699; 3,702 | 3,719 |
| Toàn bộ kit | 16,657; 6,605; 40,939; 15,060; 3,835 | 15,060 |
| Bộ trường chạy riêng | 3,641; 6,335; 4,190; 3,687; 4,471 | **4,190** |

Để tránh tải các test khác do agent này chạy, đợi toàn bộ kit và TypeScript kết thúc rồi chạy riêng:

```text
pnpm --dir shared/game-kit exec vitest run map/fields-sample.test.ts
field-timing dragon-hold.L2-cau.json median=4.190ms samples=3.641,6.335,4.190,3.687,4.471ms
Test Files  1 passed (1)
     Tests  3 passed (3)
Duration  462ms
Exit code: 0
```

**Đạt đích ≤ 60 ms** và ngưỡng hỏng test **250 ms**. Không khởi chạy việc nặng nào khác trong lượt đo riêng; không điều khiển tiến trình của các agent khác. Mọi trung vị đều dưới đích nên không cần phân rã phần tô/EDT; test có in phân rã nếu trung vị vượt 60 ms.

### Kiểm 7 · Phần còn lại của kit

Hai lệnh dưới được chạy **lần lượt**, đợi Vitest kết thúc rồi mới chạy TypeScript:

```text
pnpm --dir shared/game-kit exec vitest run
Test Files  42 passed (42)
     Tests  474 passed (474)
Duration  5.68s
Exit code: 0

pnpm --dir shared/game-kit exec tsc -p tsconfig.json --noEmit
(không có chẩn đoán)
Exit code: 0
```

Cả hai đạt ngay lần đầu. Test cũ `typing/session.test.ts` đạt **3/3**, tổng **3839 ms**, không gặp timeout; không cần chạy lại. Không sửa test hoặc cấu hình ngoài phạm vi.

### Kiểm 8 · Đối chiếu trạng thái Git

Trước mọi lần ghi:

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

Sau khi đã viết báo cáo:

```text
git status --short --untracked-files=all
 M shared/game-kit/map/index.ts
?? docs/codex-queue/028-report.md
?? docs/codex-queue/029-report.md
?? shared/game-kit/map/edt.test.ts
?? shared/game-kit/map/edt.ts
?? shared/game-kit/map/fields-sample.test.ts
?? shared/game-kit/map/raster.test.ts
?? shared/game-kit/map/raster.ts
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

Chín dòng sẵn có vẫn giữ nguyên. Chỉ thêm sáu file được phép và một dòng ` M shared/game-kit/map/index.ts`; không có dòng sửa/xóa mới khác. Đối chiếu tự động tập dòng trạng thái đầu/cuối, khẳng định không mất dòng cũ và mọi dòng mới đúng danh sách cho phép.

```text
git diff --check
(không có lỗi khoảng trắng)
Exit code: 0

git diff --name-only
shared/game-kit/map/index.ts
Exit code: 0
```

Diff của `index.ts` chỉ có hai dòng export mới. Không sửa file của phiếu 027/028, không cài gói, dùng mạng, mở cổng/trình duyệt hoặc chạy build/test của game. Không chạy lệnh Git có ghi.

## 4. Chỗ chưa rõ và lựa chọn

- Phiếu chưa quy định chỉ số ngoài lưới của `cellCenterX/Z`: chọn kiểm số nguyên an toàn trong `[0, w−1]` hoặc `[0, h−1]`, ném `RangeError` khi sai. Cả hai hàm đều kiểm lưới.
- Phiếu để tự chọn cách phân phối 200 ca tô hình: giữ đúng seed và loại theo `k % 4`, buộc các ca suy biến/ngoài/phủ lưới vào những seed đầu, các ca còn lại dùng bộ sinh có seed. Đa số tọa độ là bội của nửa cỡ ô, một phần lệch 1–3 cm; oracle không dùng hộp bao của lõi.
- Khi hai parabola có cùng giá trị, giữ nguồn bên trái đến điểm phân cách rồi chuyển tại `Sep + 1`; chỉ trả khoảng cách nên lựa chọn nguồn khi bằng nhau không ảnh hưởng kết quả.
- Bộ đệm nội bộ giữ dung lượng lớn nhất từng dùng, không thu nhỏ; mọi kết quả trả về là mảng mới. Không định nghĩa API L1 thực trong test mẫu.

## 5. Phần để lại và chủ dự án cần xem

Không bỏ qua hạng mục nào của phiếu 029. `layers/fields.ts` để phiếu **032** theo phạm vi đã giao; không tạo API hoặc tích hợp vào game ở phiếu này. Không làm hình/âm thanh hay trình duyệt vì đây là phiếu chỉ mã. Không đụng Tu Tiên hoặc checkout chính `/Users/toandx/htdocs/typing-game`.

Chủ dự án có thể xem hai module, các test và bảng số vàng trong báo cáo; không có bước kiểm tay bắt buộc còn thiếu. Tất cả thay đổi để nguyên trong worktree, chưa commit.

## Claude duyệt (28/10/2026)

Chạy lại trong worktree `map-codex`, đều đạt:
- `node --test tools/map-factory/test/*.test.mjs` hai lần: 13/13 test, 0 bỏ qua. Hai fixture khớp sha256 của phiếu (`ad67509d…`, `71160a56…`). Hai repo game không đổi trạng thái: dòng `waves.ts` của Rồng là của làn Rồng, có từ trước.
- `vitest run map`: 6 file, 185 test. `tsc -p map/tsconfig.json`: sạch.
- Toàn kit: 42 file, 474 test. `tsc`: sạch.
- EDT là Meijster bằng số nguyên. Phép chia duy nhất là `Math.floor` của hai số nguyên dưới 2^26, nên kết quả chính xác trên mọi engine. Lõi không có lượng giác hay số ngẫu nhiên.
