# Phiếu 051 · Rồng Giữ Ải · Đổi tên tiếng Anh

Ngày 28/10/2026. Worktree `games/.wt-dh-names`, nhánh `dh-names`, HEAD `e91c155` (từ `main`). Đã đọc và áp dụng Phiếu 050, ưu tiên quyết định của Claude trong [NAMES_EN.md](../games/NAMES_EN.md).

**Chưa hoàn tất sáu kiểm.** Đã đổi các literal hiển thị được phép cho 21 tên trong bảng đề xuất và Fire Breath, Inferno. Hai mục cần chủ dự án chốt thêm phạm vi đã được hỏi, chưa có trả lời tại thời điểm báo cáo:

1. `src/ui/wave-card.ts:81–86`: `shortFoeName()` cắt tên theo cấu trúc tiếng Việt. Cần sửa tối thiểu hàm để trả tên tiếng Anh đầy đủ cho loài quái, giữ nhãn lớp “Tướng”. Chỉ thay literal sẽ cho tên rút gọn sai; sửa hàm vượt yêu cầu “chỉ đổi literal chuỗi” của kiểm 4. Chưa sửa hàm.
2. `tests/ui/hud.test.ts:73`: assert `Chưa đủ vàng` phải thành `Chưa đủ Gold`. File chưa được NAMES_EN.md liệt kê cho Rồng, nên chưa sửa. Đây là test duy nhất làm `pnpm check` lỗi.

Các đường dẫn dưới tính từ `games/.wt-dh-names/`. “Số chỗ đổi” là số dòng mã nguồn gốc chứa tên hoặc biến thể đã đổi, mỗi tên tính một lần mỗi dòng; không tính lại script báo cáo, assert hay nghĩa Việt mới thêm. Bảng phản ánh phần đã sửa, không tính hai dòng hàm đang chờ.

| Tên Việt | Tên tiếng Anh | Số chỗ đổi | File |
|---|---|---:|---|
| Yêu Rêu Lính | Moss Grunt | 1 | `src/content/data/enemies.ts` |
| Yêu Rêu Cung | Moss Archer | 1 | `src/content/data/enemies.ts` |
| Sói Mục | Blight Wolf | 1 | `src/content/data/enemies.ts` |
| Heo Nanh Đá | Tusk Boar | 1 | `src/content/data/enemies.ts` |
| Ong Gai | Thorn Wasp | 1 | `src/content/data/enemies.ts` |
| Kiến Gai | Thorn Ant | 1 | `src/content/data/enemies.ts` |
| Yêu Rêu Cầm Cờ | Moss Bannerman | 1 | `src/content/data/generals.ts` |
| Gai Chông | Spikes | 3 | `src/content/data/our-side.ts`, `src/ui/debut-card.ts` |
| Bom Hạt Thông | Pine Bomb | 2 | `src/content/data/our-side.ts`, `src/ui/debut-card.ts` |
| Lưới Phóng | Net Launcher | 3 | `src/content/data/our-side.ts`, `src/ui/debut-card.ts`, `src/ui/wave-card.ts` |
| Lều Thuốc Nam | Herb Hut | 1 | `src/content/data/our-side.ts` |
| Vệ Binh Rêu | Grove Warden | 3 | `src/content/data/our-side.ts`, `src/ui/debut-card.ts` |
| Bình Máu Nhỏ / Bình Máu | Small Potion | 3 | `src/app/app.ts`, `src/content/data/our-side.ts`, `src/ui/hud.ts` |
| Tim Rồng | Dragon Heart | 1 | `src/content/data/our-side.ts` |
| Vảy Cứng | Hard Scale | 1 | `src/content/data/our-side.ts` |
| Vàng / vàng | Gold | 17 | `src/ui/{hud,learning-frame,placement-ui,results,shop-strip,wave-card}.ts` |
| Long Nộ | Dragon Rage | 4 | `src/ui/hud.ts`, `src/ui/wave-card.ts` |
| Bệ Rồng | Dragon Platform | 2 | `src/ui/hud.ts`, `src/ui/results.ts` |
| cờ (vật thể) | Banner | 1 | `src/ui/debut-card.ts` |
| Thiên Hỏa | Sky Fire | 3 | `src/ui/debut-card.ts`, `src/ui/hud.ts` |
| Long Hống | Dragon Roar | 3 | `src/ui/hud.ts`, `src/ui/tags.ts` |
| Phun Lửa / phun lửa | Fire Breath | 5 | `src/ui/debut-card.ts`, `src/ui/hud.ts`, `src/ui/results.ts` |
| Viêm Đế | Inferno | 1 | `src/ui/hud.ts` |

## Mô tả đầu và câu chữ

Thêm nghĩa Việt theo bảng vào 7 dòng `does` của thẻ ra mắt ở `src/ui/debut-card.ts:21–27` và 8 mô tả món đồ trong `effectLine()` ở `src/ui/shop-strip.ts:61–79`. Ví dụ `(lính rêu) Đi bộ tới bệ rồi chém Hỏa Long.` và `(chông nhọn) Chậm …`. Không thêm thành phần giao diện mới.

Một sửa ngữ pháp tối thiểu tại `src/ui/results.ts:196`: “để Hỏa Long phun lửa hạ chúng” → “để Hỏa Long dùng Fire Breath hạ chúng”. Các câu còn lại chỉ đổi phần tên và thêm nghĩa Việt như trên.

Số Gold là 17 thay vì 16 trong bảng thống kê gốc vì đồng bộ cả regex `/ vàng$/` → `/ Gold$/` tại `src/ui/shop-strip.ts:85`, giữ chức năng rút gọn thông báo thiếu tiền.

Banner chỉ thay danh từ chỉ vật trong “quanh Banner” và “trên Banner”. Giữ các lời gọi hành động `cắm cờ`, `Cắm Cờ`, `nhổ cờ`, `Nhổ cờ` theo quyết định của Claude. Vì thế không sửa `src/ui/tags.ts:461` và `src/view/banners.ts:259`; đây là hai vị trí được bảng gốc đếm nhưng quyết định chốt giữ tiếng Việt.

Đã rà `src/app/pace-card.ts` và các chuỗi mức Dễ trong `src/app/app.ts`, `src/ui/results.ts`: không có tên vật/loài cần đổi thêm. Giữ `Dễ`, `Quái`, WPM và câu hướng dẫn tiếng Việt theo luật; các nhãn này không phải tên một loài hoặc món.

## Assert, fixture và script

Chỉ đổi literal phụ thuộc chuỗi hiển thị; không sửa logic test:

- `tests/ui/placement.test.ts:50`: thiếu tiền đặt đồ → `Thiếu 20 Gold`.
- `tests/ui/shop-strip.test.ts:34,53–58,63`: thiếu tiền, nghĩa Việt trong mô tả 5 món có assert toàn chuỗi, và tên `Herb Hut`.

`tests/ui/hud.test.ts:73` chưa sửa vì ngoài danh sách; đã hỏi chủ dự án như nêu đầu báo cáo. Không có fixture dữ liệu cần đổi. Giữ tiêu đề test và chú thích kỹ thuật không phụ thuộc hiển thị.

Đồng bộ literal hiển thị trong `scripts/balance/report.ts`: tên kỹ năng, Gold, Herb Hut, Net Launcher, Dragon Platform. Các script QA được liệt kê còn lại chỉ nhắc tên trong chú thích, không sửa. Không chạy script trình duyệt hoặc thêm lượt cân bằng ngoài `pnpm check`.

## Sáu kiểm bắt buộc

| Kiểm | Kết quả |
|---|---|
| 1. `cd games/.wt-dh-names && pnpm check` | **CHƯA ĐẠT**, exit 1: **452/453 test đạt, 50/51 file test đạt**. Kit 73 file khớp manifest. Lỗi duy nhất: `tests/ui/hud.test.ts:73` mong `Chưa đủ vàng`, nhận `Chưa đủ Gold`. Build chưa chạy do test lỗi. |
| 2. Golden giữ nguyên | **ĐẠT**. Cả 10 test golden M0 trong `pnpm check` đạt, gồm replay và log lệnh bot. SHA-256 golden giữ nguyên so với trước sửa và HEAD; không chạy lệnh cập nhật. Các test cân bằng hiện có trong `pnpm check` cũng đạt. |
| 3. Không sót tên Việt | **CHƯA ĐẠT**. Lệnh Node chạy trực tiếp, không lưu script vào repo: đọc 21 tên và biến thể từ mục Rồng của NAMES_EN.md, thêm 2 quyết định Fire Breath/Inferno, quét literal bằng AST TypeScript trong đúng 13 file của mục “File có literal tên đề xuất đổi”. Bỏ chú thích, nghĩa Việt đầu dòng trong ngoặc và các lời gọi Cắm Cờ/Nhổ cờ được chốt giữ Việt. In `leftoverCount: 3`, đều ở 2 dòng hàm `shortFoeName`: dòng 83 có `Yêu Rêu Lính`, `Yêu Rêu`; dòng 85 có tiền tố `Yêu Rêu`. |
| 4. Không đổi id/logic | **ĐẠT cho phần đã sửa**. Đã đọc `git diff -U0`: chỉ literal chuỗi/regex đổi. Lệnh Node so `git show HEAD:<file>` với hiện tại trên cả 8 file `src/content/**`: 1.438 id/khóa object, `idDifferenceCount: 0`. So token của 15 file mã đã sửa sau khi che literal: `nonLiteralChanges: []`. `git diff --check` đạt. Hàm rút gọn chưa sửa, chưa có ngoại lệ được duyệt. |
| 5. Độ dài | **ĐẠT phần thống kê**. Bảng bên dưới liệt kê tên tăng hơn 4 ký tự. Chưa xác nhận bố cục; Claude kiểm bằng trình duyệt sau khi hoàn tất hai mục còn lại. |
| 6. Phạm vi status | **ĐẠT đối chiếu mốc đầu**. Worktree chỉ sửa 12 file src, 2 file test, 1 script đã được liệt kê và thêm changelog đúng đường dẫn. Repo cha chỉ phát sinh báo cáo này so với mốc đầu. Không sửa cây chính, làn VFX hoặc công việc của agent khác. |

SHA-256 trước và sau không đổi:

| Golden | SHA-256 |
|---|---|
| `tests/golden/m0.json` | `c0f9770cf32f033988576c0da8a17b7ae817b20c676a7ae3cd78ef2860562b82` |
| `tests/golden/golden.test.ts` | `c41bd1dbdcff4895ab2e6ab4f9b3b110e1d3e90ad051c61c8e6afb222668f618` |

### Danh sách độ dài cho Claude

Đếm ký tự Unicode, gồm khoảng trắng; rà cả biến thể tên cũ được bảng liệt kê. Chỉ có một tên tăng hơn 4 ký tự:

| Tên cũ → tên mới | Độ dài cũ → mới | File và chỗ hiển thị cần xem |
|---|---:|---|
| Bệ Rồng → Dragon Platform | 7 → 15 (+8) | `src/ui/hud.ts:432`: dòng thông báo thất thủ; `src/ui/results.ts:293`: tiêu đề màn thua. Script báo cáo dùng tên tại `scripts/balance/report.ts:410`, không phải giao diện game. |

Claude cũng cần xem 7 thẻ ra mắt và mô tả món trên khay mua sau khi thêm nghĩa Việt; thanh Dragon Rage; tên quái trên thẻ đợt sau khi xử lý hàm rút gọn. Việc rà hiện tại là tĩnh, chưa xác nhận chữ vừa khung.

### Status và mốc thay đổi đồng thời

Mốc repo cha đầu phiếu có các dòng sau; giữ nguyên:

```text
 M games/typing-survival
?? .claude/launch.json
?? TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md
?? docs/codex-queue/035-report.md
?? docs/codex-queue/036-report.md
?? docs/codex-queue/043-report.md
?? docs/codex-queue/050-report.md
?? docs/tools/map-factory/
```

Dòng mới duy nhất của phiếu ở repo cha: `?? docs/codex-queue/051-report.md`. Worktree sạch khi bắt đầu. Không dọn hoặc hoàn nguyên thay đổi đồng thời.

## Giữ nguyên, bỏ qua và bàn giao

Giữ tên riêng Bạch Long, Hỏa Long, Draconis và tướng có tên riêng. Moss Bannerman là tên loại tướng G01, đã được bảng chốt đổi. Giữ các dòng “Cần Claude xem” khác bằng tiếng Việt, gồm Ấn Phá, Chữ Chiêu, Từ Khẩn, Từ Ngắt, Từ Trợ, Cụm Ấn, Tối Thượng, chỉ số, tên đường/ải và chế độ.

Không sửa `src/view/fx*` hoặc `src/view/vfx*`. Các tên trong `src/view/fx.ts` nằm ở chú thích: Phun Lửa (4, 414, 596), Thiên Hỏa (4, 53, 414, 613, 637, 959), Long Hống (4, 681), Viêm Đế (87, 693, 811, 1141, 1214), Gai Chông (720), Bom Hạt Thông (730), Lưới Phóng (746), Lều Thuốc Nam/Bình Máu Nhỏ (758, 775). Bỏ qua toàn bộ vì làn VFX bị cấm và đây không phải literal hiển thị. Không tìm thấy tên hiển thị cần đổi trong các file VFX bị cấm đã rà.

Không đổi id, khóa dữ liệu, từ phải gõ, lịch từ của ải, đường dẫn asset, public/assets hoặc golden. Không làm ảnh/âm thanh vì phiếu chỉ đổi chuỗi. Không mở dev server hoặc trình duyệt. Không chạy lệnh git có ghi.

Changelog: `games/.wt-dh-names/docs/changelog/2026-10-28-english-names.md`.

**Việc chủ dự án cần xem:** chốt hai ngoại lệ phạm vi đầu báo cáo; sau khi xử lý, chạy lại sáu kiểm rồi Claude kiểm bố cục trên trình duyệt trước commit. Chưa coi phiếu hoàn tất.
