# Phiếu 203 · Wordwoven · C10 vòng 5

Ngày 30/10/2026, Mac mini M4. **Hoàn tất Phần A và các kiểm Codex; Phần B tự bỏ vì 133, 165, 172 chưa có kết luận Nhận.** `pnpm check` xanh **426/426 test, 46 file**; hai golden `same: true`; cả hai gói khởi động và phần 3D dưới trần. Chưa nghiệm thu cảm giác/thị giác: Claude chạy trình duyệt và gửi hai giám khảo C10 mức 8.

## Nơi làm, đầu vào và phạm vi

Worktree `games/.wt-td-ui`, nhánh **`td-ui`**, có tổ tiên **`2a1f61d`** (`merge-base --is-ancestor` exit 0). Trước sửa có đúng **13 đường dẫn của phiếu 200**, khớp `200-report.md`, được điều phối cho phép giữ. [status-before.txt](203/status-before.txt) lưu lệnh, kết quả và mã thoát. Không sửa file nào của 200, kể cả `src/ui/td.css`, danh sách chọn và `art.ts`; đã so lại diff `td.css` với bản đầu lượt, nguyên vẹn.

Áp skill `threejs-game-ui-designer` cho vùng HUD và kiểm trạng thái. Đây là lượt sửa mã, không phải lượt nghiệm thu trình duyệt. Không dev server, trình duyệt, mạng, ảnh mới hay âm thanh; không Git ghi, kit sync, sửa sim/router/content, game khác, Tu Tiên hay worktree khác. Chỉ đọc hai verdict C10 trong `games/.wt-td-1c/tmp/`.

Mã/test/changelog của 203 dưới worktree:

- `src/view/words/{cards.ts,feel.css,dom.ts,safe.ts,steps.ts,tray.ts}`;
- `src/view/3d/words.ts`;
- `scripts/visual/scenarios/td-1c-words.mjs`;
- `tests/{td-c10-r5,td-card-art,td-no-emoji}.test.ts`;
- `docs/changelog/2026-10-30-c10-fixes-and-card-icons.md`.

Báo cáo này và thư mục [203/](203/) nằm ở repo cha, chỉ chữ/số, không ảnh. Không tạo raw frame nên không có khung cần prune.

## Phần A · Năm sửa

**A1 — Hộp an toàn ở mỗi khung.** Trước đây cột tránh HUD khi xếp, nhưng thẻ sau nội suy/trượt, scale, nghiêng và bóp chưa được kẹp lại; ×N chỉ chọn trái/phải; chữ đóng dấu và nhãn hạng có thể vượt hộp thẻ. `keepIn(box, view, panels, pad)` xét các biên vùng cấm của góc trên trái, chọn phép dời có khoảng cách Euclid nhỏ nhất. Lề màn và khoảng HUD mặc định 8 px; hộp đã hợp lệ dời 0. Hết chỗ thì trả vị trí kẹp màn gần nhất và `ok: false`. `fitElement` đo sau biến đổi rồi dời bằng thuộc tính CSS `translate`, nên vẫn tránh được cả chữ sai đang dùng Web Animations. Áp mỗi khung cho thẻ, hộp lớn nhất của chữ đóng dấu và toàn đường rơi/co của nó, nhãn hạng đang nâng, chữ bay; điểm cuối của chữ bay cũng được kẹp riêng. Thẻ dự phòng thêm khoảng cho rim, nhãn Review và chấm tác nhân. `comboSide` thử phía hiện tại → đối diện → trên thẻ → kẹp; kích thước gồm cả dấu × và scale hiện tại. `CardFeel.frame` nhận tùy chọn `{width, height, panels}` từ `cards.draw`. `PANELS`/`Hud.boxes()` đã có `chip`, `strip`, `dock`, không cần sửa HUD.

Test A1 chạy **1.128 hộp lưới** ở hai cỡ: **0 hộp ngoài màn, 0 hộp cắt HUD**, hộp hợp lệ dời 0; thêm 19 khung nội suy mỗi cỡ, hộp chữ đầu ngay dưới bảng trái, trường hợp dời tối thiểu/hết chỗ/quá khổ, ×N ở bốn mép và đổi phía/lên trên. Fixture ghi rõ số từ CSS: rộng bảng 284/340,8 px, cách mép 12 px; thanh nhập rộng 360/432, cao 44/52,8, đáy 8 px; vị trí 720p theo media query, 1080p giữa màn. Chiều cao bảng thay đổi theo nội dung nên test dành hộp lớn 180/216 px cho chip và 330/396 px cho Build; **đây là fixture Node, không phải số đo trình duyệt**. Runtime luôn lấy hộp DOM thật. Test riêng xác nhận `Hud.boxes` trả đủ ba loại.

**A2 — Một chữ V cho bốn mép.** Mã cũ không có nhánh cố ý vẽ vòng C: nó xếp **hai chevron chuyển động**, mỗi cánh dài 28 px nhưng bề dày lớp mực 22 px/lớp sáng 14 px, hai cánh cách nhau khoảng 80°. Ở mép trái hai bộ cánh dày chồng sát đầu từ, phần đầu chìm vào nhau và đọc thành vòng hở/chữ C. Đây là giải thích từ mã, chưa phải chứng minh bằng render mới. Nay `trayPointer` tạo một V 90° đối xứng, cùng hình học quay ở mọi mép; cơ sở 16/24 px, hướng giới hạn ±60° quanh pháp tuyến, hộp gồm thêm 3 px cho nét, cách HUD/thanh nhập ít nhất 8 px. Bên trái đặt dưới dòng từ, ngoài thẻ. Kho `pool` vẫn vẽ V tạm bằng hai cánh, lớp mực 5 px và sáng 3 px, không tạo icon thay ảnh. Test **4 mép × 3 hướng × 2 cỡ = 24 trường hợp**, cộng hướng tiếp tuyến để kiểm giới hạn 60°; kiểm màn/HUD, đối xứng, hai đầu ở sau đỉnh, góc 90° và quay ngược về hình gốc lệch <0,5 px.

**A3 — Giữ màu chữ đầu của nhóm.** Trước đây `read()` chỉ tạo dấu `.k` cho các thẻ cùng chữ đầu, còn `typed` hiển thị vẫn 0; khi animation hết, chữ về màu mực. `typedShown` nay lấy tiền tố hiển thị từ router đang mở mà không sửa sim/router. `draw()` so số hiển thị này để render lại: nhóm `t` cho `team` và `thanks` đều 1, giữ qua 50 khung (~833 ms); phím `e` cho `team` 2 và `thanks` 0 ngay cùng khung; Backspace đóng nhóm về 0. `eye` luôn 0. Có cả test hàm thuần và test đi qua `WordCards.draw()` với world/router thật, nút DOM giả nhỏ trong Node, không thư viện DOM.

**A4 — Viền cứng trước quầng.** Trước đây `RIM` có inset/quầng mềm ngay từ khung đầu. `rimAt` nay cho t <34 ms nét `#FFF0D8`, blur 0, dày tối thiểu 4 px, mép ngoài 11% chiều cao thẻ mỗi phía. Sau đó thành quầng mềm với ánh sáng `exp(-(t-34)/45)`, hết ở 194 ms. `burst()` ghi outline/offset ngay; độ sáng hàm ở 0 ≥17 ≥34 ms. Nhịp `squeeze` giữ nguyên: giữ 34 ms, bóp ngang 100 ms, trống 60 ms. Test các mốc 0/17/34/100/194 ms ở UI 0,8 và 1,2, rim thuần dày 4/6 px. **Tỷ số sáng ảnh khung đầu/đỉnh ≥0,95 còn phải Claude đo lại**, không suy ra từ test ánh sáng hàm.

**A5 — Chữ đóng dấu ngay trong `draw`, chữ gốc luôn hiện.** Bỏ `td-key-hold` vốn làm chữ gốc trong suốt 50 ms, và bỏ bản sao `::before` chạy CSS 67 ms. Giả thuyết chậm một khung: `.k` được chèn qua `innerHTML`, rồi pseudo-element/animation mới được trình duyệt tạo ở lượt tính style/animation kế; trạng thái nghỉ của bản sao lại có opacity 0. Trong lúc đó chữ gốc đã bị ẩn, tạo ô khoét. Mã hiện tại chưa đủ để kết luận chính xác thời gian compositor.

Nay mỗi thẻ tái dùng một phần tử thật `.td-key-stamp`, JS đặt opacity và pose đầu ngay trong lần `draw()` thấy nút `.k` mới. `stampStep`: 2,4 →1,8 →1,3 →1,0 ở 0/17/33/50 ms, −8° →−6° →−3° →0°, cộng 0,25 mỗi bậc trong ba bước lớn; 66 ms tắt. Trước pose hiện tại, đo pose lớn nhất và chừa 28 px cho đường về/glow rồi kẹp; không dùng animation-delay. `.k` gốc luôn màu đã gõ; chữ cuối trong `wordHit` cũng dùng đúng nút `.k` và luật này. Giảm chuyển động giữ scale 1, không rơi/nghiêng. Test t=0/17/33/50/66, bậc 3, quét CSS không còn luật làm `.k` trong suốt, và `draw()` thật cho nút chữ cuối ở cả hai chế độ chuyển động. Claude đo `keyFrames` và xem `key-dark` để xác nhận cảm giác.

### Bảng hàm và test

Đường dẫn/dòng tính từ worktree ở trạng thái giao:

| Sửa | Hàm thuần | Chỗ gắn chính | Test trong `tests/td-c10-r5.test.ts` |
|---|---|---|---|
| A1 | `safe.ts:8 keepIn`, `tray.ts:7 comboSide` | `words/dom.ts:4`, `cards.ts:288,301,331`; `3d/words.ts:416,422,499,523` | `grid stays in…`; `chooses the minimum translation…`; `combo keeps its side…`; `Hud.boxes includes…` |
| A2 | `tray.ts:18 trayPointer` | `3d/words.ts:531 pointers` | `4 edges x 3 headings…`; `limits a tangential direction…` |
| A3 | `steps.ts:2 typedShown` | `cards.ts:243` | `t, 50 held frames, e in the same frame…`; `draw keeps both t prefixes…` |
| A4 | `steps.ts:5 rimAt` | `cards.ts:104 burst` | `0, 17, 34, 100, 194 ms…` |
| A5 | `steps.ts:11 stampStep` | `cards.ts:307 keyStamps`, `feel.css:4` | `steps 2.4, 1.8, 1.3, 1…`; `has no transparent .k rule…`; `draw writes the first stamp pose immediately…` |

Tất cả hàm trên thuần, không DOM, `document` hay Three.js. Phần đọc DOM nằm riêng trong `dom.ts` và các view.

### A6 · Sửa kịch bản, không chạy

`td-1c-words.mjs` nay khởi động bộ đo rAF sau fonts ready, đo **mọi khung** tới hết các cửa sổ chụp/lượt kiểm zoom, không giữ danh sách phần tử cũ mỗi 10 khung. Bao gồm `.td-card`, `.td-key-stamp`, `.td-stamp`, `.td-fly`, `.td-combo`, `.td-tray-arrow` khi sau này có DOM ảnh. Ghi `boxAudit` gồm tổng khung, số khung vi phạm `overHud`/`offScreen`, tên lớp + chữ và bảng HUD bị đè; từng `meta.json` giữ vi phạm trong **đúng thời gian bắt đầu/kết thúc cửa sổ**, kể cả lúc hành động pan chưa trả về. Giữ dạng `dom` cũ cho phép đo pixel. `tdHudBudget`/`trayClear` dùng cả kết quả mới, thêm `offScreen`; các cổng khác không đổi. `node --check` exit 0; có test nguồn xác nhận nối bộ đo. Chưa có số vi phạm từ browser.

## Phần B · Cổng nhận và ảnh còn chờ

Đọc toàn bộ **2/2** file hiện có: `accept-29-10/verdict.md` và `accept-29-10b/verdict.md`. **Không có mục phiếu 133, 165, 172**, nên không có dòng kết luận Nhận để dẫn. Chỗ khớp số “133” ở file thứ hai dòng 133 là giá trị RGB trong nhận xét phiếu 140, không phải nhận ảnh 133. Bằng chứng: [acceptance-scan.json](203/acceptance-scan.json). Thực hiện đúng chỉ thị giao 14:16: **bỏ toàn bộ B1–B5**, không sửa hay chép media, không thêm mục chọn.

| Bộ ảnh | File chấm/dòng của bộ | Kết luận | Bản thu dùng | Chỗ gắn của phiếu này |
|---|---|---|---|---|
| 133: `call-power`, `build`, `harvest`, `chop`, `mine`, `quiz`, `spell`, `interrupt`, `anchor`, `shield-break` | Chưa có mục | Chờ chấm | Không | Chưa gắn; đầu thẻ, Build và 2D Low giữ nguyên |
| 172: `pip-full`, `pip-empty`, `pip-gold`, `badge-ok`, `badge-flash`, `badge-calling`, `badge-review`, `badge-chain` | Chưa có mục | Chờ chấm | Không | Chưa gắn; sau này phải lấy `_review/172/delivery-final/`, không bản thu cũ |
| 165: 6 nhà `keep`, `archer`, `cannon`, `barracks`, `gold-mine`, `farm`; `tray-arrow`, `tray-call` | Chưa có mục | Chờ chấm | Không | Chưa gắn; giữ V tạm của A2 và 2D Low cũ |

Chưa dùng bản thu 133 có ngoại lệ alpha/sắc khóa, chưa dùng bất kỳ bản thu nào khác. **0 media chép, 0 MD5 mới, 0 lần cần `check-ignore` cho media hay liên kết `ui/`**; liên kết/ảnh nguồn giữ nguyên. Không sinh ảnh nên không có prompt mới. `tests/td-card-art.test.ts` chỉ giữ hai test chạy được của trạng thái chờ: tám nhãn hiện tại và nghĩa full/full/empty của lời gọi ba từ, một từ không hạt. Các test mã ảnh/huy hiệu/icon nhà ↔ danh sách chọn sẽ viết khi B được mở, chưa khẳng định những tính chất chưa triển khai.

`pip-gold` chưa có trạng thái mã, không thêm luật. `Perfect`, `Good`, `Sloppy`, `Redeemed`, hết giờ và hủy chưa có ảnh huy hiệu, giữ nguyên. Gợi ý phiếu sau: `badge-calling` ở dòng đầu lời gọi/“Calling”; `badge-review` cạnh nhãn Review; `badge-chain` ở dải Chain hoặc ×N. Chưa gắn ba huy hiệu này.

## Các kiểm có số

Test viết trước mã: [tests-first.txt](203/tests-first.txt) lưu lượt đỏ do chưa có module hàm thuần; hai test art chờ và test quét đã xanh. Chốt sau với toàn bộ `pnpm check`, không có test thời gian đỏ nên không cần ba lượt chạy riêng.

| Kiểm | Trước | Sau / bằng chứng |
|---|---:|---|
| `pnpm check` | Exit 0; 43 file / **405 test** | Exit **0**; 46 file / **426 test**, kit **42/42**; [before.txt](203/before.txt), [after-check.txt](203/after-check.txt) |
| Golden | Không sửa luật hoặc file golden | Exit **0**, **2/2 `same:true`**, changed `{}`, problems/rejected 0; [golden.txt](203/golden.txt) |
| `/` gzip ≤85.000 B | **82.314 B** | **83.233 B**, +919 B, dư **1.767 B** |
| `/?title=0` gzip ≤85.000 B | **83.754 B** | **84.677 B**, +923 B, dư **323 B** |
| Phần 3D ≤260 kB gzip | **171,83 kB** | **172,347 kB**, dư 87,653 kB |
| `.ts` ngoài `src/kit` ≤16.500 | **13.101** | **13.231**, +130, dư **3.269**; [lines-after.txt](203/lines-after.txt) |
| Kịch bản | Chưa sửa bộ đo | `node --check` exit **0**, chưa chạy |
| Phạm vi luật/kit | Có 13 file 200 đã biết | `git diff --quiet -- src/kit src/sim src/typing src/content` exit **0**; [protected.txt](203/protected.txt) |
| Git và khoảng trắng | [status-before.txt](203/status-before.txt) | [status-after.txt](203/status-after.txt), `git diff --check` exit **0** |

Gói đo cùng cách `scripts/bundle-budget.mjs`: manifest import closure và `gzipSync`; [budget-after.json](203/budget-after.json), [verification.json](203/verification.json) có số byte/hash mã đã kiểm. Lượt build đầu vượt gói vào thẳng; đã bỏ mã đóng dấu lặp, bỏ `data-c` cũ và tách `comboSide`/`trayPointer` vào `words/tray.ts`, chỉ tải cùng phần 3D. Không đổi trần hay cấu hình chunk. Cảnh báo chunk Three.js >500 kB nguyên bản vẫn có ở trước/sau; cổng 3D gzip đều đạt. Các nhật ký `budget-iteration*.txt` là lượt trung gian đỏ, **không phải trạng thái giao**.

### Quét emoji/hạt và ký hiệu khác

Quét đủ **20 file** `.ts`/`.css` theo mẫu phiếu, kể cả chú thích: **23 lần khớp**, **19 cặp file/ký tự**, **3 mục cho phép**. [symbols.json](203/symbols.json) ghi từng dòng.

| Mục cho phép | Ký tự | Phiếu chờ | Số lần |
|---|---|---:|---:|
| `src/view/words/cards.ts` | `🏹 🔨 🌾 🪓 ⛏️ 📖 🔥 ✋ ⚓ 🛡️` | 133 | 10 |
| `src/view/words/cards.ts` | `● ○`, cả chú thích | 172 | 5 |
| `src/view/debug-2d.ts` | `⛏️ 🌾 🪓 🔨 ✋ ⚓ 🛡️`, cả chú thích | 133 | 8 |

Mục cho phép không còn xuất hiện sẽ làm test đỏ. 165 chưa nhận nhưng V/triangle không khớp mẫu Unicode này, nên không thêm mục giả vào danh sách. Ký hiệu chữ không thuộc mẫu giữ nguyên: `⇧` ở build-menu/hud; `▶`, `Ⅱ`, `…` ở hud; mũi tên bàn phím ở settings/sheets/title; `★` ở sheets/title và 2D Low; dấu ba chấm trong tips/2D Low. Đây là liệt kê, không sửa thay trong lượt này.

## Việc còn lại và bàn giao

Còn vẽ bằng mã trên/thành phần thẻ mà phiếu không thay ảnh: chấm tác nhân `td-card-dot`, vòng thời gian `conic-gradient` của direct call, nền/viền thẻ, thanh thời gian, nhãn Review, hạt/emoji chờ B và nhãn hạng dạng viên chữ. Vòng ấn dưới phím, rim, V tạm và chữ bay là VFX đang giữ theo phạm vi. Các hạng thiếu ảnh nêu ở Phần B cần brief ảnh riêng.

Đúng ngoài phạm vi: nền/viền tăng tương phản ×N ngọc trên cỏ; lệch chữ sai khỏi chữ cần gõ; Word Shot T/A/tâm lóe; thẻ khay đậu trên nhà khác; TF2 giữa màn; các ảnh 103/174 và Settings/loa/tiếng phím 193. Không sửa `BUILD_NOTES.md` hay `docs/changelog/README.md`.

**Claude cần:** duyệt diff của 203 cùng trạng thái 200 đã biết; chạy `td-1c-words` High ở **1280 ×720** và **1920 ×1080**; xem `key-dark`, `key-multi`, `word-dark`, `combo`, `tray-in`, `tray-type`, `tray`. Đọc số khung/tên phần tử ở `boxAudit` và từng capture; đo lại độ trễ đóng dấu, first/peak theo từng nhịp, và xem ×N đủ dấu ×, V ở mép trái/dưới rõ. Gửi **hai giám khảo C10 mức 8**, rồi commit sau duyệt. Không có media mới của 203 để `media:push`. Phần B chỉ mở lại sau verdict Nhận; không coi test Node là nghiệm thu cảm giác.
