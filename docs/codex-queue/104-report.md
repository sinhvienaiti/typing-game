# Phiếu 104 · Tuyến Cuối · Ba nhãn nhỏ

Thực hiện ngày 28/10/2026 tại `games/.wt-ts-codex`, nhánh `ts-codex`. **Đã làm bốn trong năm việc; chưa đủ điều kiện nhận vì Esc ở thẻ trước trận chưa sửa.** Không chạy lệnh Git ghi, dev server, trình duyệt hay tạo media.

HEAD ban đầu là `014d75096b4950240a6de67f91d68f7276953abc` (xem [HEAD thực tế](104/head-before.txt)); worktree sạch. Lịch sử đã có `8d63e07` (090) và `014d750` (092). Chụp SHA-256 toàn bộ 234 file đang được Git theo dõi trước sửa trong [tracked-before-sha256.json](104/tracked-before-sha256.json).

## File mới và đã sửa

Đường dẫn mã tính từ worktree:

- `src/view/hud.ts`: biểu tượng khóa bến 3, chú thích, biển mục tiêu, banner rút lui, bốn thẻ MỚI viết hoa.
- `src/view/screens-journey.ts`: chỉ hai chuỗi trả về của `ruleDetail`.
- `src/content/chapter-1.ts`: chỉ chuỗi `name` của ải 2.
- `scripts/visual/scenarios/survival-s1-stage.mjs`: chỉ hai chuỗi trong biểu thức so khớp `huntPlateCounts`.
- `tests/small-labels.test.ts`: mới, ba ca cho độ dài câu Luật học và tên ải 2 qua HTML Hành trình, trang giới thiệu, thẻ kết.
- `docs/changelog/2026-10-29-small-labels.md`: mới, tiếng Việt.

Repo cha: báo cáo này và bằng chứng trong [104/](104/), theo mục Báo cáo của luật chung. Không sửa `src/view/screens.ts` vì chưa thay đổi hành vi Esc. `LEARN_RULES` nằm ở `src/content/stage-rules.ts:73`; hai nhãn “Chuẩn”, “Thiếu chữ” đã ngắn, giữ nguyên cả file.

## Bảng Luật học để duyệt chữ

Đếm từ theo khoảng trắng, từng câu kết thúc bằng dấu chấm. [Số đo từng câu](104/word-counts.json).

| Luật | Cũ | Mới | Số từ từng câu mới |
| --- | --- | --- | --- |
| Chuẩn | từ và nghĩa trên bến; khi gõ, từ hiện to trên dòng gõ trên mũi tàu, bến đang gõ hiện IPA và nghĩa; gõ xong hiện "từ · nghĩa ✓". | Từ và nghĩa hiện trên bến. Từ đang gõ hiện lớn phía trên mũi tàu. Bến đang gõ hiện phiên âm và nghĩa. Gõ xong, từ và nghĩa hiện cùng dấu ✓. | 6 / 9 / 8 / 9 |
| Thiếu chữ | mỗi từ ẩn 1 chữ (từ 7 chữ trở lên: 2), không bao giờ là chữ đầu. IPA và nghĩa vẫn hiện. Gõ sai ô ẩn thì chữ đúng hiện ra. | Mỗi từ ẩn một chữ, từ có ít nhất bảy chữ ẩn hai. Chữ đầu luôn hiện. Nghĩa và phiên âm vẫn hiện. Gõ sai chữ ẩn sẽ hiện chữ đúng. | 13 / 4 / 6 / 8 |

Tổng tám câu, tối đa **13 từ**, dưới giới hạn 14. Không thay luật chữ ẩn, số chữ ẩn hay thông tin phiên âm/nghĩa. Không có danh từ game cần dịch trong hai đoạn này.

## Bảng biển và banner

`n` dưới đây là giá trị Vỏ đang đọc từ `FOES`, giữ nguyên.

| Chỗ hiện | Cũ | Mới |
| --- | --- | --- |
| Biển đếm mục tiêu | Pack Leader 2/3 · LỌT 1/2 | PACK LEADER 2/3 · LỌT 1/2 |
| Biển rút lui | Swarm RÚT LUI | SWARM RÚT LUI |
| Banner rút lui | Swarm RÚT LUI! | SWARM RÚT LUI! |
| Thẻ mới Brute | MỚI · Brute · (quái lực lưỡng) Vỏ n | MỚI · BRUTE · (QUÁI LỰC LƯỠNG) VỎ n |
| Thẻ mới Pack Leader | MỚI · Pack Leader · (thủ lĩnh bầy) Vỏ n | MỚI · PACK LEADER · (THỦ LĨNH BẦY) VỎ n |
| Thẻ mới Shield Guard | MỚI · Shield Guard · (lính mang khiên) chắn đạn phía trước | MỚI · SHIELD GUARD · (LÍNH MANG KHIÊN) CHẮN ĐẠN PHÍA TRƯỚC |
| Thẻ mới Splitter | MỚI · Splitter · (quái tách mảnh) vỡ 3 Shard | MỚI · SPLITTER · (QUÁI TÁCH MẢNH) VỠ 3 SHARD |

Đã rà toàn bộ `hud.ts`: banner “ĐỈNH TRÀN … · DỮ DỘI” đã viết hoa; cảnh báo “⚠ Rift · … s” không có chữ Việt viết hoa bên cạnh nên giữ nguyên. Tên súng đọc từ dữ liệu giữ nguyên. Không sửa `foes.ts`, tên trong dữ liệu vẫn là “Pack Leader”.

## Tên mới ở từng màn

| Chỗ hiện | Đường đọc tên | Kết quả từ mã |
| --- | --- | --- |
| Hành trình | `src/app/journey.ts:122`, nối `stage.name` vào nhãn menu | `Ải 2 · Săn Pack Leader`, thêm sao khi đã mở |
| Trang giới thiệu ải, có Luật học | `src/view/screens-journey.ts:62`, `stage.name.toUpperCase()` | `ẢI 2 · SĂN PACK LEADER` |
| Thẻ chờ trước trận | `src/app/main.ts:304`, `level.name.toUpperCase()` | `ẢI 2 · SĂN PACK LEADER` |
| Banner lúc vào trận | `src/app/main.ts:548`, `level.name.toUpperCase()` | `ẢI 2 · SĂN PACK LEADER` |
| Thẻ kết | `src/app/main.ts:313` ghép tên thường; `src/view/screens.ts:129` viết hoa cả dòng gồm chế độ | `ẢI 2 · SĂN PACK LEADER · CÂN BẰNG`, hoặc chế độ đang chơi |
| Nạp súng | `src/view/screens-journey.ts:85`, chỉ đọc số thứ tự | `ẢI 2 · CHỌN 2 TRONG 5 · …/2`, không hiện tên ải |

Đây là đối chiếu nguồn và HTML trong test, chưa phải chấp nhận hình ảnh trên trình duyệt.

## Kiểm 1 · Test trước, mã sau; `pnpm check`

Chạy trong worktree, trước khi thêm test và sửa mã: exit **0**, [check-before.log](104/check-before.log):

```text
src/kit OK: 59 files match kit-manifest.json
Test Files  16 passed (16)
Tests       156 passed (156)
Duration    5.06s
✓ built in 974ms
```

Thêm test trước sửa mã: `pnpm exec vitest run tests/small-labels.test.ts`, exit **1**, **3/3 ca hỏng** như mong đợi: hai đoạn Luật học dài, tên ải 2 còn cũ. [labels-red.log](104/labels-red.log). Sau sửa cùng lệnh exit **0**, **3/3 đạt**, [labels-green.log](104/labels-green.log).

`pnpm check` sau sửa: exit **0**, [check-after.log](104/check-after.log):

```text
src/kit OK: 59 files match kit-manifest.json
Test Files  17 passed (17)
Tests       159 passed (159)
Duration    5.12s
✓ built in 933ms
```

**159 = 156 + 3**, thêm một file test. Kit, typecheck và build đạt. Cảnh báo chunk Vite trên 500 kB có cả trước và sau, không làm kiểm hỏng. Chỉ chạy lệnh build/test trong worktree do chính mục Kiểm 1 của phiếu yêu cầu; không chạy ở cây game chính hay game khác. Lệnh kiểm có tạo lại `dist/` và cache dependency được Git bỏ qua.

## Kiểm 2 · Băm chương giữ

`node --import tsx scripts/chapter-hashes.ts` trước/sau đều exit **0**:

- [chapter-before.txt](104/chapter-before.txt): **152 dòng**.
- [chapter-after.txt](104/chapter-after.txt): **152 dòng**.
- `diff -u` exit **0**, [chapter.diff](104/chapter.diff) rỗng, **0 byte**.
- SHA-256 hai file đều `ae7e9859269b2aece6a7bacbd946dfa93b9a131aeb68a5f5dbed97830dfe626e`.

Đổi tên ải 2 không đổi băm, nên giữ “Săn Pack Leader”; không cần phương án trả tên cũ. Không chạy cập nhật golden.

## Kiểm 3 · Chuỗi cũ

Trong worktree:

| Lệnh | Mã thoát | Số dòng |
| --- | --- | --- |
| `grep -rn "MỞ Ở MỐC" src` | 1, không tìm thấy | 0 |
| `grep -rn 'Swarm RÚT LUI\|"Đầu Đàn"' src scripts` | 1, không tìm thấy | 0 |

[grep-milestone.txt](104/grep-milestone.txt), [grep-old-labels.txt](104/grep-old-labels.txt) đều rỗng. Các chú thích lịch sử có từ Đầu Đàn không thuộc literal được yêu cầu tìm, giữ nguyên.

## Kiểm 4 · Esc và bộ test DOM

**Chưa sửa Esc.** `act()` ở `src/app/main.ts:457–459` trả ngay khi `mode === "intro"`; listener ở dòng 537–542 cũng loại `Escape`. `screens.ts` và `screens-journey.ts` dựng HTML, không sở hữu trạng thái `mode` và bộ súng của trận. Làm đúng cách điều hướng hiện có cần sửa tối thiểu `main.ts`, nhưng file này không nằm trong “Chỉ được ghi”.

Đã gửi câu hỏi xin mở đúng phạm vi `src/app/main.ts`; chưa nhận chấp thuận nên chưa ghi file đó. Không gắn xử lý phím vào hàm dựng HTML để lách danh sách đường dẫn. Không sửa phần cài `window.__survival` của 092.

`vitest.config.ts` đặt `environment: "node"`; hiện không có bộ test DOM cho thẻ trước trận, không có phụ thuộc jsdom/happy-dom. Ba ca mới chỉ kiểm HTML thuần, không xác nhận điều hướng Esc. Theo ngoại lệ của Kiểm 4, Claude cần kiểm bằng **`survival-s1-loadout`** sau khi sửa Esc: thẻ ải → Esc → Nạp súng, đúng ải và đúng thứ tự bộ súng đã chọn; chọn tiếp rồi vào trận, không gõ nhầm phím mở thẻ vào từ. Cần kiểm cả khi thẻ còn đang nạp.

## Kiểm 5 · Phạm vi và bảo toàn

[status-after.txt](104/status-after.txt) lưu `git -C games/.wt-ts-codex status --short -uall`; chỉ sáu đường dẫn liệt kê ở trên. [scope-check.json](104/scope-check.json) đối chiếu SHA-256 với mốc trước: chỉ bốn file tracked được phép đổi; các file tracked khác, bao gồm toàn bộ file của 090 và 092, giữ nguyên từng byte. HEAD không đổi. `git diff --check` exit **0**, [diff-check.txt](104/diff-check.txt) rỗng. [measurements.json](104/measurements.json) gom số đo.

## Khác phiếu và việc chủ dự án cần xem

- Mục 2 chưa thực hiện do xung đột danh sách đường dẫn: cần cho phép sửa `src/app/main.ts`, hoặc để Claude sửa phần đó. Phiếu chưa hoàn tất dù các kiểm mã đã xanh.
- Chưa chạy trình duyệt vì phiếu cấm server/trình duyệt. Claude cần xem thẻ ải 1/2, nạp súng, bến khóa, biển mục tiêu ải 2, banner và bốn thẻ MỚI ở **1280×720** và **1920×1080**; chưa xác nhận chữ viết hoa không tràn.
- Chủ dự án/Claude duyệt hai bảng câu cũ–mới ở trên, nhất là bốn thẻ MỚI cũng được viết hoa cả dòng theo yêu cầu rà thêm biển/banner.
- Không làm media, audio, GLB, không sửa cây chính, game khác, Tu Tiên, công cụ chung, kit hay golden. Không commit/push; việc kiểm lại, commit và gộp dành cho Claude.
