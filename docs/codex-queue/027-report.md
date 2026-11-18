# Phiếu 027 · Map Factory · Lõi băm, seed, hạng và lint tất định

Ngày thực hiện: 27/10/2026. Worktree: `/Users/toandx/htdocs/typing-game-wt/map-codex`. Môi trường: macOS, Node **v24.22.0**, pnpm **11.21.0**, TypeScript **6.0.3**, Vitest **3.2.7** có sẵn.

Đã hoàn tất **7/7 mục kiểm bắt buộc**. Bộ map đạt **3 file, 122 test** trong cả hai lượt chạy riêng; toàn kit đạt **39 file, 411 test**. Hai lệnh TypeScript thoát **0**. Lint quét **3 file lõi, 0 vi phạm**. Không dùng mạng, cổng, trình duyệt, dev server, cài gói hay lệnh Git có ghi; không chạy build hoặc test của game.

## 1. Các file đã viết

- `shared/game-kit/map/tsconfig.json`: kế thừa cấu hình kit, bật `erasableSyntaxOnly`, đúng nội dung phiếu.
- `shared/game-kit/map/hash.ts`: kiểu `HashPart`, FNV-1a thuần, bộ hoàn tất MurmurHash3 và `hash32` với mã hóa có byte loại, độ dài UTF-8 và từ little-endian.
- `shared/game-kit/map/seeds.ts`: seed theo lớp, seed theo ô có tọa độ signed int32, hạng phần triệu và ngưỡng mật độ tăng đơn điệu.
- `shared/game-kit/map/index.ts`: xuất lại toàn bộ API và kiểu của hai module lõi.
- `shared/game-kit/map/hash.test.ts`: 25 test cho băm vàng, vector công khai, byte mã hóa, ranh giới kiểu/chuỗi và đầu vào sai.
- `shared/game-kit/map/seeds.test.ts`: 34 test cho seed/hạng vàng, 10.000 ứng viên, ngưỡng mật độ và kiểm đầu vào.
- `shared/game-kit/map/lint.test.ts`: 63 test cho bộ lọc file, scanner, mẫu cấm/sạch, chẩn đoán vị trí và bốn lần dịch nguồn ảo trong bộ nhớ.
- `docs/codex-queue/027-report.md`: báo cáo kết quả và các lựa chọn khi diễn giải phiếu.

## 2. Bảy mục kiểm bắt buộc

Mọi lệnh dưới đây chạy từ cwd `.` của worktree.

### 1. Test map lần thứ nhất

```text
pnpm --dir shared/game-kit exec vitest run map
Test Files  3 passed (3)
     Tests  122 passed (122)
Exit code: 0
```

Phân bố: `hash.test.ts` **25**, `seeds.test.ts` **34**, `lint.test.ts` **63**. Thời gian tổng: **9,45 s**.

### 2. Typecheck cấu hình map

```text
pnpm --dir shared/game-kit exec tsc -p map/tsconfig.json
Không có chẩn đoán.
Exit code: 0
```

### 3. Băm vàng và các phép kiểm thêm

Nằm trong lệnh `pnpm --dir shared/game-kit exec vitest run map` ở mục 1 và 6: **12/12 băm vàng khớp**, bảng chi tiết ở mục 3 của báo cáo.

| Phép kiểm thêm | Test nhận được | Phiếu yêu cầu |
| --- | ---: | ---: |
| `rankOf(2270686687, 1)` | 191962 | 191962 |
| `rankOf(2270686687, 2)` | 805752 | 805752 |
| Seed 2739991112, k = 0…9999, giữ ở 350 ‰ | 3463 | 3463 |
| Seed 2739991112, k = 0…9999, giữ ở 550 ‰ | 5519 | 5519 |
| Ứng viên giữ ở 350 ‰ nhưng mất ở 550 ‰ | 0 | 0 |
| `fnv1a32` byte rỗng | `0x811c9dc5` | `0x811c9dc5` |
| `fnv1a32` ASCII `a` | `0xe40c292c` | `0xe40c292c` |
| `fnv1a32` ASCII `foobar` | `0xbf9cf968` | `0xbf9cf968` |
| `fmix32(0)` | 0 | 0 |
| `fmix32(1)` | `0x514e28b7` | `0x514e28b7` |
| `fnv1a32` của `01 01 00 00 00` | `0x1b95c75d` | `0x1b95c75d` |
| `fnv1a32` của `02 0b 00 00 00 54 68 c3 a1 63 20 42 e1 ba a1 63` | `0xc55e45d6` | `0xc55e45d6` |

Các ca lỗi bắt buộc đều ném đúng loại lỗi; có thêm kiểm ranh giới, Unicode không chuẩn hóa và đầu vào sai ở cả hai tọa độ.

### 4. Lint tất định và cú pháp chỉ xóa kiểu

Nằm trong cùng lệnh test map:

```text
Map core files (3): hash.ts, index.ts, seeds.ts; violations: 0
map/lint.test.ts (63 tests): passed
```

- **19/19** mẫu cấm của phiếu: mỗi mẫu đúng **1 vi phạm**.
- **11/11** mẫu sạch của phiếu: mỗi mẫu **0 vi phạm**.
- **23/23** tên hàm Math cấm được kiểm thêm với cả `.` và `?.`.
- Bộ lọc nhận file lõi ở thư mục con, loại `*.test.ts`; vì vậy `performance` dùng trong file test không nằm trong phạm vi quét lõi.
- Scanner xử lý template lồng nhau, brace trong biểu thức, regex và phép chia; báo từng vị trí một lần theo dạng `<file>:<dòng>: <token>`.
- Cấu hình đọc bằng API TypeScript có `erasableSyntaxOnly === true`, **0 lỗi phân tích cấu hình**.
- Ba nguồn ảo `enum`, `namespace` có giá trị, tham số thuộc tính constructor: **3/3 có lỗi 1294**.
- Nguồn đối chứng `export const a: number = 1;`: **0 chẩn đoán**.
- Bốn nguồn ảo chỉ ở bộ nhớ; không tạo `__virtual__` hoặc file mẫu trên đĩa. Test có thời hạn **30.000 ms**.

### 5. Toàn bộ kit

```text
pnpm --dir shared/game-kit exec vitest run
Test Files  39 passed (39)
     Tests  411 passed (411)
Exit code: 0

pnpm --dir shared/game-kit exec tsc -p tsconfig.json --noEmit
Không có chẩn đoán.
Exit code: 0
```

So với mốc **36 file, 289 test** của phiếu: thêm **3 file, 122 test**, tổng đúng **39 file, 411 test**.

Lượt toàn kit đầu tiên chạy đồng thời với typecheck có **38 file đạt, 1 file lỗi; 410 test đạt, 1 test lỗi**: test từ vựng cũ trong `typing/session.test.ts` vượt thời hạn 5.000 ms, mất khoảng **6.796 ms**. Chạy lại nguyên lệnh toàn kit riêng đạt toàn bộ; test đó mất khoảng **3.992 ms**, tổng lượt đạt **8,05 s**. Khả năng tranh CPU phù hợp với kết quả này, nhưng chưa đo riêng để khẳng định nguyên nhân. Không sửa test, cấu hình hoặc mã kit ngoài phạm vi phiếu.

### 6. Test map lần thứ hai

```text
pnpm --dir shared/game-kit exec vitest run map
Test Files  3 passed (3)
     Tests  122 passed (122)
Exit code: 0
```

Cùng số file, số test, băm vàng và kết quả lint như lần thứ nhất. Thời gian tổng: **3,08 s**.

### 7. Phạm vi file thay đổi

```text
git status --short --untracked-files=all
?? docs/codex-queue/027-report.md
?? shared/game-kit/map/hash.test.ts
?? shared/game-kit/map/hash.ts
?? shared/game-kit/map/index.ts
?? shared/game-kit/map/lint.test.ts
?? shared/game-kit/map/seeds.test.ts
?? shared/game-kit/map/seeds.ts
?? shared/game-kit/map/tsconfig.json
Exit code: 0
```

Trước khi làm: worktree sạch. Sau khi làm: đúng **8 file được phép**, **0 file ngoài phạm vi**.

## 3. Bảng 12 băm vàng

Giá trị nhận được được kiểm bằng `toBe` trong test; cột hex là cùng số viết ở hệ 16.

| # | Gọi | Test nhận được | Trong phiếu | Hex nhận được / phiếu |
| ---: | --- | ---: | ---: | --- |
| 1 | `hash32()` | 2872998923 | 2872998923 | `0xab3e7c0b` / `0xab3e7c0b` |
| 2 | `hash32(0)` | 3758500711 | 3758500711 | `0xe0062b67` / `0xe0062b67` |
| 3 | `hash32(1)` | 2798434716 | 2798434716 | `0xa6ccb99c` / `0xa6ccb99c` |
| 4 | `hash32(-1)` = `hash32(4294967295)` | 3872971898 | 3872971898 | `0xe6d8dc7a` / `0xe6d8dc7a` |
| 5 | `hash32("")` | 1404927536 | 1404927536 | `0x53bd7e30` / `0x53bd7e30` |
| 6 | `hash32("vegetation")` | 3618500123 | 3618500123 | `0xd7adee1b` / `0xd7adee1b` |
| 7 | `hash32("Thác Bạc")` (NFC) | 2036913320 | 2036913320 | `0x7968d4a8` / `0x7968d4a8` |
| 8 | `layerSeed(20261027, "vegetation", 1)` | 2739991112 | 2739991112 | `0xa350f248` / `0xa350f248` |
| 9 | `layerSeed(20261028, "fields", 1)` | 3301207131 | 3301207131 | `0xc4c46c5b` / `0xc4c46c5b` |
| 10 | `cellSeed(2739991112, 0, 0)` | 578876828 | 578876828 | `0x2280f59c` / `0x2280f59c` |
| 11 | `cellSeed(2739991112, -5, -4)` | 2270686687 | 2270686687 | `0x8757eddf` / `0x8757eddf` |
| 12 | `rankOf(2270686687, 0)` | 693049 | 693049 | — |

## 4. Điểm chưa rõ và cách chọn

- `version` được yêu cầu là số nguyên an toàn ≥ 1, đồng thời `layerSeed` phải bằng `hash32(mapSeed, layer, version)`. Cách chọn: kiểm số nguyên an toàn dương trước, rồi gọi nguyên `hash32`; vì thế phiên bản lớn hơn **4294967295** vẫn ném `RangeError` theo giới hạn mã hóa số của hash. Không cắt bit âm thầm hoặc đổi phiên bản thành chuỗi. Có test cho phiên bản tối đa được mã hóa và giá trị vượt giới hạn. Đây là điểm chủ dự án cần lưu ý khi viết spec hoặc tăng phiên bản.
- Phiếu gọi là “bảy lệnh kiểm”, nhưng mục 3–4 nằm trong lệnh 1 và mục 5 có hai lệnh. Báo cáo giữ đủ **bảy mục** theo đúng thứ tự phiếu, ghi lệnh và dòng tổng ở từng chỗ tương ứng.
- Quy tắc lint cho `Math` cấm tính một vi phạm tại token `Math`; vì vậy chẩn đoán là `sample.ts:1: Math`, theo đúng định dạng token đã yêu cầu. Không dùng parser hoặc phân tích alias; các module sau dùng lại scanner và danh sách quét ngay trong file test này.

Không bỏ sót hạng mục triển khai nào của phiếu 027. Không tạo ảnh, âm thanh hay kiểm trình duyệt vì phiếu chỉ yêu cầu mã; không sửa game, Tu Tiên, checkout chính, công cụ khác hoặc cấu hình chung của kit. Chưa thực hiện phiếu 028–029 vì nằm ngoài phạm vi hiện tại.

## Claude duyệt (28/10/2026)

- **Chạy lại kiểm, đều đạt:**
  - `pnpm --dir shared/game-kit exec vitest run map`: 3 file, 122 test.
  - `tsc -p map/tsconfig.json --noEmit`: thoát 0.
  - Toàn kit: 39 file, 411 test; `tsc -p tsconfig.json --noEmit` thoát 0.
- **Đọc mã:**
  - `hash.ts`, `seeds.ts` đúng đặc tả. FNV-1a có thẻ kiểu và độ dài, rồi qua fmix32. Mọi phép tính dùng `Math.imul` và `>>> 0`.
  - Đầu vào ngoài miền thì báo lỗi. `rankKept` đúng nghĩa "tăng mật độ thì không dời vật cũ".
- **Hai điểm đã biết:**
  - Phiếu được sửa câu chữ Kiểm 7 sau khi Codex bắt đầu; đặc tả không đổi.
  - Test từ vựng cũ của kit có lúc quá 5 s khi máy bận. Đó không phải lỗi của phiếu này.
