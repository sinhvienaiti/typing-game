# Phiếu 052 · Tuyến Cuối · Đổi tên tiếng Anh

Ngày 28/10/2026. Worktree `games/.wt-ts-names`, nhánh `ts-names`, HEAD `ea8e0f9` (từ `main`), sạch khi bắt đầu.

Đã đổi đủ **12 tên, 46 dòng mã gốc, 60 lượt tên–dòng** theo mục Tuyến Cuối trong [NAMES_EN.md](../games/NAMES_EN.md), cộng **Rift: 6 lượt tên–dòng** theo quyết định của Claude. Tổng cộng **13 tên, 50 dòng nguồn khác nhau, 66 lượt tên–dòng**; các vị trí bổ sung của Rift có 2 dòng trùng những tên khác. Tên Đầu Đàn của quái dùng **Pack Leader**.

Các đường dẫn trong bảng tính từ `games/.wt-ts-names/`. “Số chỗ đổi” là số dòng mã gốc chứa tên hoặc biến thể, mỗi tên chỉ tính một lần mỗi dòng; không tính lại script QA hay nghĩa Việt mới thêm.

| Tên Việt | Tên tiếng Anh | Số chỗ đổi | File |
|---|---|---:|---|
| XUNG / Xung | Pulse Gun | 2 | `src/app/main.ts`, `src/content/guns.ts` |
| TIA / Tia | Heat Beam | 2 | `src/app/main.ts`, `src/content/guns.ts` |
| TÁN | Scatter Gun | 1 | `src/content/guns.ts` |
| RAY | Rail Gun | 1 | `src/content/guns.ts` |
| PHÁO SAO | Star Mortar | 1 | `src/content/guns.ts` |
| Bầy | Swarm | 17 | `src/app/journey.ts`, `src/app/main.ts`, `src/app/results.ts`, `src/content/balance.ts`, `src/content/foes.ts`, `src/content/guns.ts`, `src/view/hud.ts`, `src/view/screens-journey.ts` |
| Lính | Scout | 4 | `src/app/journey.ts`, `src/content/foes.ts`, `src/content/guns.ts`, `src/view/screens-journey.ts` |
| Trâu | Brute | 6 | `src/app/journey.ts`, `src/content/foes.ts`, `src/content/guns.ts`, `src/view/hud.ts`, `src/view/screens-journey.ts` |
| Khiên (loại quái) | Shield Guard | 6 | `src/app/journey.ts`, `src/content/foes.ts`, `src/content/guns.ts`, `src/view/hud.ts`, `src/view/screens-journey.ts` |
| Tách | Splitter | 5 | `src/app/journey.ts`, `src/content/foes.ts`, `src/content/guns.ts`, `src/view/hud.ts`, `src/view/screens-journey.ts` |
| Mảnh | Shard | 5 | `src/app/journey.ts`, `src/content/foes.ts`, `src/content/guns.ts`, `src/view/hud.ts`, `src/view/screens-journey.ts` |
| Đầu Đàn (loại quái) | Pack Leader | 10 | `src/app/journey.ts`, `src/content/foes.ts`, `src/content/guns.ts`, `src/content/stage-rules.ts`, `src/view/hud.ts`, `src/view/screens-journey.ts` |
| Vết nứt (hiểm họa) | Rift | 6 | `src/app/journey.ts`, `src/content/stage-rules.ts`, `src/view/hud.ts`, `src/view/screens-journey.ts` |

## Mô tả đầu và câu chữ

Giữ câu, gợi ý và menu tiếng Việt quanh tên tiếng Anh; giữ đúng kiểu chữ tên mới cả trong literal HUD vốn viết hoa. Ví dụ `Săn Đầu Đàn` → `Săn Pack Leader`, `Lính và đạn lính` → `Scout và đạn Scout`, `BẦY RÚT LUI!` → `Swarm RÚT LUI!`.

Thêm nghĩa Việt vào mô tả đang có, không tạo thành phần giao diện:

- `src/content/guns.ts:130–134`: tiền tố `(súng xung)`, `(tia nhiệt)`, `(súng bắn chùm)`, `(súng ray)`, `(pháo cối sao)` cho mô tả thẻ súng ở kho súng và màn nạp súng.
- `src/view/screens-journey.ts:21–26`: tiền tố nghĩa Việt cho 6 loại quái có dòng mô tả trong bản giới thiệu ải. Riêng Swarm, thêm `"(bầy quái) " +` trước biểu thức số máu hiện có để giữ số động; đây là phép ghép phục vụ trình bày duy nhất thêm vào ngoài thay literal. Shard được giới thiệu trong câu Splitter vỡ thành 3 Shard, không có dòng mô tả riêng để thêm.
- `src/view/hud.ts:57–60`: nghĩa Việt mở đầu phần mô tả của 4 thẻ MỚI, sau tên Brute, Pack Leader, Shield Guard, Splitter.
- `src/view/screens-journey.ts:38`: `Rift (vết nứt không gian): mỗi …` trong mô tả hiểm họa.

**Câu sửa ngữ pháp:** không có câu nào cần sửa ngoài phần tên và các nghĩa Việt trong ngoặc. Không đổi các danh từ mô tả thông thường như tia, pháo xung, súng ray, tấm khiên hay lượng khiên thành tên thực thể.

**Hàm cắt/ghép tên:** đã rà các file tiêu thụ tên động `src/app/{journey,main}.ts`, `src/view/{hud,screens,screens-journey}.ts`. Tên súng được lấy nguyên từ `GUN_SPECS[].name`; `counterTag()` chỉ nối các tên đầy đủ bằng dấu phẩy. Không có hàm dựa vào cấu trúc tiếng Việt cần sửa và không cần test mới cho hàm này. Các lệnh cắt từ đang gõ giữ nguyên.

## Assert và fixture

Không có assert/fixture phụ thuộc tên hiển thị phải sửa trong các file test mà NAMES_EN.md liệt kê; các literal tên cũ ở đó là tiêu đề test, chú thích hoặc khóa kỹ thuật (`RAY.damage`, `XUNG`, v.v.). Không đổi logic hay tiêu đề test. Game hiện không có assert tên tài nguyên cần đổi như ví dụ Gold ở Phiếu 051.

Đổi đúng 3 dòng trong script đã được liệt kê `scripts/visual/scenarios/survival-s1-loadout.mjs`:

- Dòng 99: bản giới thiệu có Brute và `khắc: Rail Gun`.
- Dòng 102: cảnh báo hàng Brute chưa được khắc chế.
- Dòng 106: hai bến hiện Pulse Gun và Scatter Gun.

Chỉ thay chuỗi/regex, giữ nguyên điều kiện kiểm. `node --check` đạt; không chạy kịch bản trình duyệt. Các script khác trong danh sách chỉ nhắc tên cũ ở chú thích hoặc dùng id kỹ thuật, nên giữ nguyên.

## Sáu kiểm bắt buộc và băm chương

| Kiểm | Kết quả |
|---|---|
| 1. `cd games/.wt-ts-names && pnpm check` | **ĐẠT**, exit 0; **142/142 test, 14/14 file test**. Kit 59 file khớp manifest; typecheck và build đạt. Build có cảnh báo chunk trên 500 kB (chunk lớn nhất 547,18 kB); phiếu không chỉnh đóng gói. |
| 2. Golden giữ nguyên | **ĐẠT**. Cả **18 ca golden Trận thử** trong `tests/s0-trace.test.ts` đạt: sự kiện, số lượng, kết quả và hash khớp. File golden trùng HEAD và SHA-256 trước/sau giữ nguyên, ghi bên dưới. Không cập nhật golden. |
| 3. Không sót tên Việt | **ĐẠT**. Lệnh `node --input-type=module` chạy trực tiếp từ repo cha, không lưu script: đọc 12 tên cùng biến thể từ NAMES_EN.md, thêm Vết nứt theo dòng chốt Rift; duyệt literal bằng AST TypeScript trong đúng 9 file “File có literal tên đề xuất đổi”. Bỏ chú thích, nghĩa Việt trong ngoặc, tên riêng Bầy Hố Đen, khóa ASCII chữ thường và danh từ khiên chỉ tấm chắn/thuộc tính. Tên súng phân biệt kiểu chữ để giữ mô tả thông thường. In `nameCount: 13`, `fileCount: 9`, `leftoverCount: 0`. |
| 4. Không đổi id/logic | **ĐẠT**. Đọc `git -C games/.wt-ts-names diff -U0`: chỉ thay literal chuỗi/regex, cộng tiền tố nghĩa Việt bằng phép nối ở `screens-journey.ts:21` đã nêu. Lệnh Node so `id:`, `key:` và khóa object với `git show HEAD:<file>` trên **9 file `src/content/**`, 636 mục**, in `idDifferenceCount: 0`. So token toàn bộ 10 file mã sau khi che literal và trừ đúng phép ghép tiền tố trên: `nonLiteralChanges: []`. `git diff --check` đạt. |
| 5. Độ dài | **ĐẠT phần thống kê**. Đủ 5 tên tăng hơn 4 ký tự ở bảng dưới. Claude kiểm bố cục bằng trình duyệt trước commit; phiếu này chưa xác nhận bố cục. |
| 6. Phạm vi status | **ĐẠT đối chiếu thay đổi của phiếu**. Worktree có đúng 9 file src, 1 script được NAMES_EN.md liệt kê và changelog mới đúng đường dẫn. Repo cha phát sinh báo cáo `docs/codex-queue/052-report.md`; có thêm `shared/shared` từ công việc đồng thời, ghi rõ ở mục status. Không sửa hoặc dọn thay đổi của làn khác. |
| Bổ sung: băm chương | **ĐẠT**. Chạy `node --import tsx scripts/chapter-hashes.ts` trước và sau sửa. Mỗi lượt **152 dòng**. So bằng `diff -u` qua hai đầu vào process substitution: **stdout rỗng, exit 0**. SHA-256 toàn bộ đầu ra, gồm newline cuối, cả hai là `ae7e9859269b2aece6a7bacbd946dfa93b9a131aeb68a5f5dbed97830dfe626e`. Không sửa script băm. |

SHA-256 trước và sau:

| Tệp / đầu ra | SHA-256 không đổi |
|---|---|
| `tests/golden/s0-trace.json` | `42e4e5a9534bc78a0c252353ea7ee4670a1bec9e43eb42ef38c886aade530eea` |
| `scripts/chapter-hashes.ts` | `46167d49b2333b20bf3cac3a1b39810a8948dc97f45dbd405736b0d289845a4e` |
| 152 dòng stdout của `scripts/chapter-hashes.ts` | `ae7e9859269b2aece6a7bacbd946dfa93b9a131aeb68a5f5dbed97830dfe626e` |

### Danh sách độ dài cho Claude

Đếm ký tự Unicode, gồm khoảng trắng, không đếm byte UTF-8. Không thêm/bớt dòng nguồn nên số dòng giữ nguyên sau sửa.

| Tên cũ → tên mới | Độ dài cũ → mới | File và chỗ hiển thị cần xem |
|---|---:|---|
| XUNG / Xung → Pulse Gun | 4 → 9 (+5) | Nguồn `src/content/guns.ts:130`; ghi chú nút Trận thử `src/app/main.ts:229`; tên bến `src/view/hud.ts:170`; thẻ kho súng `src/view/screens.ts:90`; tiêu đề thẻ nạp súng `src/view/screens-journey.ts:92`; bảng khắc chế `src/app/journey.ts:283`; thẻ vào trận `src/app/main.ts:305`. |
| TIA / Tia → Heat Beam | 3 → 9 (+6) | Nguồn `src/content/guns.ts:131`; ghi chú nút Trận thử `src/app/main.ts:229`; các vị trí tên bến, thẻ kho, thẻ nạp súng, khắc chế và thẻ vào trận như Pulse Gun. |
| TÁN / Tán → Scatter Gun | 3 → 11 (+8) | Nguồn `src/content/guns.ts:132`; tên bến `src/view/hud.ts:170`; thẻ kho `src/view/screens.ts:90`; thẻ nạp súng `src/view/screens-journey.ts:92`; khắc chế `src/app/journey.ts:283`; thẻ vào trận `src/app/main.ts:305`. |
| RAY / Ray → Rail Gun | 3 → 8 (+5) | Nguồn `src/content/guns.ts:133`; tên bến, thẻ kho, thẻ nạp súng, khắc chế và thẻ vào trận như Scatter Gun. |
| Khiên / KHIÊN → Shield Guard | 5 → 12 (+7) | Nguồn `src/content/foes.ts:47`; tên hàng cảnh báo trang bị `src/app/journey.ts:277`; bảng khắc chế `src/content/guns.ts:152`; thẻ MỚI `src/view/hud.ts:59`; nhãn bài học và quái trong bản giới thiệu `src/view/screens-journey.ts:17,25,71`; các hàng khắc chế trong thẻ súng và tooltip của hàng hiểm họa ở màn nạp súng. |

Ngoài ngưỡng bắt buộc, nên xem tên bến Star Mortar (11 ký tự), mục tiêu Pack Leader, 4 thẻ MỚI có nghĩa Việt mới, 5 mô tả súng và 6 dòng mô tả quái ở bản giới thiệu. Không chỉnh CSS hoặc nới kiểm để làm tên vừa.

### Status và mốc thay đổi đồng thời

Repo cha lúc bắt đầu đã có:

```text
 M games/typing-survival
?? .claude/launch.json
?? TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md
?? docs/codex-queue/035-report.md
?? docs/codex-queue/036-report.md
?? docs/tools/map-factory/
```

Các dòng trên được giữ. Trong lúc chạy xuất hiện thêm `?? shared/shared` (symlink tới thư mục shared của repo, thời điểm tạo 12:17 ngày 28/10, trước lượt `pnpm check` lúc 12:18); phiếu không tạo, sửa hay xóa đường dẫn đó. Dòng mới của phiếu ở repo cha là `?? docs/codex-queue/052-report.md`. Vì có làn khác chạy đồng thời, không coi toàn bộ status repo cha là thay đổi của phiếu.

Status cuối worktree:

```text
 M scripts/visual/scenarios/survival-s1-loadout.mjs
 M src/app/journey.ts
 M src/app/main.ts
 M src/app/results.ts
 M src/content/balance.ts
 M src/content/foes.ts
 M src/content/guns.ts
 M src/content/stage-rules.ts
 M src/view/hud.ts
 M src/view/screens-journey.ts
?? docs/changelog/2026-10-28-english-names.md
```

## Giữ nguyên và bàn giao

Giữ tên riêng Vanguard, Draconis, Bầy Hố Đen; tên ải Đầu Đàn, Vách nứt, Khiên sáng; chỉ số Giáp, Vỏ, lượng khiên; chế độ, luật học, tên vùng, sự kiện và các dòng “Cần Claude xem” chưa được chốt đổi. Mục tiêu Săn giữ động từ Việt, phần tên quái bên trong đổi theo bảng.

Các trường `GUN_SPECS[].en` vẫn là `pulse`, `beam`, `scatter`, `rail`, `flak` như ghi chú bảng tên; không dùng lượt này để đồng bộ nội dung thẻ thưởng tương lai. Không đổi id, khóa dữ liệu, từ phải gõ, dữ liệu số, file/đường dẫn asset, public/assets hay golden.

**File cấm:** `src/view/fx.ts` có Xung/Tia trong chú thích ở dòng 7, 9, 333; bỏ qua nguyên file. Không tìm thấy file `src/view/glows*` trong worktree này. Không có literal hiển thị bắt buộc nào trong nhóm file cấm bị bỏ sót.

Không đụng cây chính `games/typing-survival`, game khác, Tu Tiên hoặc làn công cụ. Chỉ chạy `pnpm check` được phiếu yêu cầu trong worktree; không chạy build/test của cây chính hay game khác. Không chạy dev server, trình duyệt, cập nhật golden hoặc lệnh git có ghi. Không làm ảnh/âm thanh vì phiếu chỉ đổi tên.

Changelog: `games/.wt-ts-names/docs/changelog/2026-10-28-english-names.md`. Claude kiểm các chỗ ở bảng độ dài và mô tả đầu trong trình duyệt rồi mới commit.
