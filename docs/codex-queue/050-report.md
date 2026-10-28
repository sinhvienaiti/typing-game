# Phiếu 050 · Lời Gọi · Đổi tên tiếng Anh

Ngày 28/10/2026. Worktree `games/.wt-td-names`, nhánh `td-names`, HEAD `ad4df6f552c847e45ce95c39e34dbf67f507d64f` (từ `a2-days`).

Đã đổi đủ **28 tên, 59 dòng mã gốc, 91 lượt tên–dòng** theo [NAMES_EN.md](../games/NAMES_EN.md), ưu tiên quyết định của Claude: Fort, Hopping Zombie, Zombie Leader, Sapling, Little Blob. Bổ sung nghĩa Việt ở 5 mô tả ô xây đang có; vì 2 dòng mô tả trước đó không chứa tên phải đổi, tổng diff phần `src` là 61 dòng. Không thêm thành phần giao diện.

Các đường dẫn trong bảng dưới tính từ `games/.wt-td-names/`. “Số chỗ đổi” theo quy ước Phiếu 026: số dòng mã gốc chứa tên hoặc biến thể của nó, mỗi tên tính một lần trên mỗi dòng; không tính lại assert, script QA hay nghĩa Việt mới thêm.

| Tên Việt | Tên tiếng Anh | Số chỗ đổi | File |
|---|---|---:|---|
| Lũy Chữ | Fort | 15 | `src/app/sandbox.ts`, `src/content/slice-1a.ts`, `src/main.ts`, `src/ui/build-menu.ts`, `src/ui/hud.ts`, `src/ui/sheets.ts`, `src/ui/team-bar.ts`, `src/ui/tips.ts` |
| Tháp Cung | Archer Tower | 4 | `src/content/slice-1a.ts`, `src/ui/sheets.ts`, `src/ui/tips.ts` |
| Tháp Pháo | Cannon Tower | 2 | `src/content/slice-1a.ts`, `src/ui/sheets.ts` |
| Trại Lính | Barracks | 3 | `src/content/slice-1a.ts`, `src/ui/hud.ts` |
| Mỏ Vàng | Gold Mine | 1 | `src/content/slice-1a.ts` |
| Ruộng | Rice Field | 1 | `src/content/slice-1a.ts` |
| Cương Thi | Hopping Zombie | 3 | `src/app/sandbox.ts`, `src/content/slice-1a.ts` |
| Đàn Ma Trơi | Ghost Flame | 2 | `src/content/slice-1a.ts`, `src/ui/tips.ts` |
| Thuồng Luồng | River Serpent | 1 | `src/content/slice-1a.ts` |
| Mầm Gỗ | Sapling | 1 | `src/content/slice-1a.ts` |
| Lửng Tanuki | Raccoon Dog | 3 | `src/app/sandbox.ts`, `src/content/slice-1a.ts`, `src/ui/tips.ts` |
| Nuppeppō | Split Blob | 2 | `src/app/sandbox.ts`, `src/content/slice-1a.ts` |
| Nuppeppō con | Little Blob | 1 | `src/content/slice-1a.ts` |
| Cương Thi Đầu Đàn | Zombie Leader | 2 | `src/app/sandbox.ts`, `src/content/slice-1a.ts` |
| Quỷ Núi Troll | Troll | 2 | `src/app/sandbox.ts`, `src/content/slice-1a.ts` |
| Dân | Villager | 5 | `src/ui/build-menu.ts`, `src/ui/hud.ts`, `src/ui/tips.ts` |
| Thợ xây | Builder | 2 | `src/ui/build-menu.ts` |
| nông dân | Farmer | 1 | `src/ui/tips.ts` |
| Lính | Soldier | 2 | `src/ui/tips.ts` |
| Thư Đồng | Helper | 1 | `src/ui/tips.ts` |
| Vàng | Gold | 12 | `src/app/sandbox.ts`, `src/ui/build-menu.ts`, `src/ui/hud.ts`, `src/ui/sheets.ts`, `src/ui/tips.ts` |
| Gỗ | Wood | 8 | `src/app/sandbox.ts`, `src/main.ts`, `src/ui/build-menu.ts`, `src/ui/hud.ts`, `src/ui/tips.ts` |
| Lúa | Rice | 6 | `src/ui/build-menu.ts`, `src/ui/hud.ts`, `src/ui/tips.ts` |
| Hạt giống | Seeds | 4 | `src/ui/build-menu.ts`, `src/ui/hud.ts`, `src/ui/tips.ts` |
| Tri thức | Knowledge | 2 | `src/ui/hud.ts`, `src/ui/sheets.ts` |
| Rương | Chest | 1 | `src/ui/sheets.ts` |
| Mưa lông lửa | Fire Feather Rain | 2 | `src/ui/hud.ts` |
| Phát Chữ | Word Shot | 2 | `src/ui/sheets.ts`, `src/ui/tips.ts` |

## Mô tả đầu và câu chữ

Trong `src/ui/tips.ts:30–34`, thêm tiền tố `(Ruộng)`, `(Tháp Cung)`, `(Trại Lính)`, `(Mỏ Vàng)`, `(Tháp Pháo)` vào dòng mô tả đang có của ô xây/thẻ nhà. Nội dung mô tả tiếp tục bằng tiếng Việt quanh tên tiếng Anh, ví dụ `(Ruộng) Gieo Seeds; Rice chín thì gọi Gặt.` Không thêm mô tả hay thẻ ra mắt cho những thực thể chưa có dòng mô tả.

Một sửa ngữ pháp tối thiểu ở `src/ui/build-menu.ts:57`: `tự mua ${FARM.seedGold} vàng một hạt` → `tự mua ${FARM.seedGold} Gold/Seeds`, tránh cụm “một Seeds”. Không có câu nào khác phải sửa ngoài phần tên.

Đồng bộ hai nhãn rút gọn của nút Hộp cát trong `src/app/sandbox.ts:22–23`: `3 Nupp.` → `3 Split Blob`, `Đầu Đàn` → `Zombie Leader`. Biến thể `Tanuki` ở nút và lời dạy cũng thành Raccoon Dog; id `tanuki` giữ nguyên.

## Assert và fixture

Chỉ đổi chuỗi/regex phụ thuộc hiển thị, không đổi logic test:

- `tests/td-hud.test.ts`: nhãn kho, thưởng gọi đêm sớm, Knowledge/Sổ ôn, thẻ Rice Field và Fort.
- `tests/td-input.test.ts:253`: lý do không đặt được nhà quanh Fort.
- `tests/td-r2.test.ts:272`: nút Fire Feather Rain khi chiêu đang chạy.
- `tests/td-test-pass.test.ts:20,26,29,30`: gợi ý xây Archer Tower, Word Shot của Cannon Tower và quái lọt vào Fort.

Đổi literal kiểm giao diện trong 5 script đã được liệt kê: `scripts/visual/scenarios/{td-1a6-tour,td-1b-boss,td-1b-build,td-1b-story,td-theme}.mjs`. Cả 5 đạt `node --check`; không chạy kịch bản trình duyệt. Không có fixture dữ liệu cần đổi.

## Sáu kiểm bắt buộc

| Kiểm | Kết quả |
|---|---|
| 1. `cd games/.wt-td-names && pnpm check` | **ĐẠT**, exit 0; **350/350 test, 32/32 file test**. Kit 31 file khớp manifest; typecheck, build và budget đều đạt. Lượt cuối: trang đầu 84,91 kB gzip ≤ 85 kB; `/?title=0` 83,46 kB. |
| 2. Golden giữ nguyên | **ĐẠT**. 6 test golden trong `pnpm check` đạt; cả 327 hash thế giới của td-1a và 94 hash của td-1b-boss khớp. Content hash cả hai vẫn `f2a21037`; SHA-256 hai file không đổi so với trước sửa/HEAD. |
| 3. Không sót tên Việt | **ĐẠT**. Một lệnh `node --input-type=module` chạy trực tiếp từ repo cha, không lưu script, đọc 28 dòng phải đổi cùng biến thể từ mục Lời Gọi trong NAMES_EN.md, rồi duyệt literal bằng AST TypeScript trong đúng 8 file của mục “File có literal tên đề xuất đổi”. Bỏ chú thích và tiền tố nghĩa Việt trong ngoặc; khớp dài trước, ranh giới chữ Unicode, không nhầm id ASCII chữ thường với tên hiển thị. In `leftoverCount: 0`. |
| 4. Không đổi id/logic | **ĐẠT**. Đọc `git -C games/.wt-td-names diff -U0`: chỉ đổi literal chuỗi/regex. Lệnh Node so với `git show HEAD:<file>` trên 5 file `src/content/**`, so giá trị `id:` và khóa object: 1.245 mục, `idDifferenceCount: 0`. So thêm cấu trúc tất cả 17 file mã sau khi che literal: `nonLiteralChanges: []`. `git diff --check` đạt. |
| 5. Độ dài | **ĐẠT phần thống kê**. Bảng dưới có đủ tên tăng hơn 4 ký tự, kể cả biến thể rút gọn. Claude cần kiểm bố cục bằng trình duyệt trước commit; phiếu này không xác nhận bố cục. |
| 6. Phạm vi status | **ĐẠT đối chiếu mốc đầu**. Worktree chỉ có 8 file src, 4 file test, 5 script đều được NAMES_EN.md liệt kê, và changelog mới đúng đường dẫn. Repo cha chỉ phát sinh thêm `docs/codex-queue/050-report.md` so với mốc đầu; các thay đổi đã có của làn khác được giữ nguyên, chi tiết dưới đây. |

SHA-256 trước và sau:

| Golden | SHA-256 không đổi |
|---|---|
| `tests/golden/td-1a.json` | `d19dffacedde417fc19ab7d743f26c14ee5d8ce989a852173a27d5fa1c826f2b` |
| `tests/golden/td-1b-boss.json` | `259bc9aecf8bfc061cca766506cab5451e25c08e8c6c0776e4f6070f28a545a8` |

### Danh sách độ dài cho Claude

Đếm ký tự Unicode, gồm khoảng trắng, không đếm byte UTF-8. Mọi vị trí dưới đây giữ nguyên số dòng sau sửa.

| Tên cũ → tên mới | Độ dài cũ → mới | File và chỗ hiển thị cần xem |
|---|---:|---|
| Ruộng → Rice Field | 5 → 10 (+5) | Nguồn `src/content/slice-1a.ts:83`; nút chọn xây `src/ui/build-menu.ts:94`, tiêu đề thẻ nhà `:64`, tooltip huy hiệu đích trên thanh đội `src/ui/team-bar.ts:22`. Huy hiệu vẫn dùng short R. |
| Cương Thi → Hopping Zombie | 9 → 14 (+5) | Nguồn `src/content/slice-1a.ts:89`; tooltip gọi quái Hộp cát `src/app/sandbox.ts:22,23`. Hàm vẽ quái tại `src/view/debug-2d.ts:642` không in tên dài. |
| Dân/dân → Villager | 3 → 8 (+5) | Thẻ Fort và nút thuê `src/ui/build-menu.ts:59,60`; cảnh báo đủ người `src/ui/hud.ts:31`; nút thuê thanh hành động `:101`; chip lời dạy Ngày 2 `src/ui/tips.ts:18`. |
| Mưa lông lửa → Fire Feather Rain | 12 → 17 (+5) | Nút chiêu đang hoạt động `src/ui/hud.ts:100`. |
| Mưa lông → Fire Feather Rain | 8 → 17 (+9) | Cảnh báo chiêu đang hoạt động `src/ui/hud.ts:33`. |
| Tanuki → Raccoon Dog (biến thể ngắn) | 6 → 11 (+5) | Nút gọi quái Hộp cát `src/app/sandbox.ts:22`; lời dạy Đêm 4 `src/ui/tips.ts:23`. Tên đầy đủ Lửng Tanuki → Raccoon Dog đều dài 11, không tăng. |
| Nupp. → Split Blob (biến thể ngắn) | 5 → 10 (+5) | Nhãn nút `3 Nupp.` → `3 Split Blob` trong Hộp cát, `src/app/sandbox.ts:22`. |
| Đầu Đàn → Zombie Leader (biến thể ngắn) | 7 → 13 (+6) | Nút gọi quái Hộp cát `src/app/sandbox.ts:23`. |

Ngoài bảng tăng độ dài tên, Claude nên xem 5 mô tả có nghĩa Việt mới trong ngoặc ở ô xây/thẻ nhà. `tests/td-tips.test.ts` vẫn đạt nguyên giới hạn 14 âm tiết, 54 ký tự mỗi câu của lời dạy và 12 âm tiết của mô tả, không nới assert.

### Status và mốc thay đổi đồng thời

Mốc repo cha đầu phiếu đã có các dòng dưới; cuối phiếu vẫn giữ nguyên:

```text
 M games/typing-survival
?? .claude/launch.json
?? TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md
?? docs/codex-queue/035-report.md
?? docs/codex-queue/036-report.md
?? docs/codex-queue/043-report.md
?? docs/tools/map-factory/
```

Dòng mới duy nhất của phiếu ở repo cha: `?? docs/codex-queue/050-report.md`. Vì repo cha đã có công việc đồng thời, toàn bộ status không chỉ chứa báo cáo; phép kiểm phạm vi so với mốc đầu, không dọn thay đổi của người khác.

## Giữ nguyên và bàn giao

Giữ tên riêng Mộc Tinh, Draconis, Chấm, Phẩy, Gạch, Bà Cú Mực. Giữ tất cả dòng “Cần Claude xem” bằng tiếng Việt, gồm Bắn mạnh, Gặt, Ngắt, Neo, Phá Khiên, Tối Thượng, Lông lửa, Mạng, Sổ ôn và tên vùng/chế độ. Chú thích kỹ thuật và tiêu đề test không phụ thuộc hiển thị được giữ.

Không đổi id, khóa dữ liệu, từ phải gõ, lịch từ của ải, file/đường dẫn asset, public/assets hay golden. Không đụng cây chính games/typing-defense hoặc game khác; không chạy lệnh git có ghi, dev server, trình duyệt hay lệnh cập nhật golden. Không làm ảnh/âm thanh vì phiếu chỉ đổi tên.

Changelog: `games/.wt-td-names/docs/changelog/2026-10-28-english-names.md`. Chủ dự án/Claude xem bảng độ dài, ô xây và thanh hành động trong trình duyệt rồi mới commit.

