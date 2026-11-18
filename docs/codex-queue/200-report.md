# Phiếu 200 · Wordwoven · Ảnh màn tựa và thẻ kết

Ngày 30/10/2026, chạy lại theo chỉ thị điều phối 12:58. **Đã hoàn tất phần gắn ảnh và các kiểm bắt buộc của Codex:** `pnpm check` xanh, 405/405 test; gói khởi động trước/sau **81.583 → 82.314 byte gzip**, dưới trần 85.000 byte. Còn lượt Claude duyệt diff, nghiệm thu trình duyệt và đẩy media theo quy trình bàn giao.

## Nơi làm và phạm vi

Worktree `games/.wt-td-ui`, nhánh `td-ui`, HEAD `2a1f61d`. Trạng thái trước lượt triển khai 11:54: `git status --short -uall` **rỗng** theo biên bản lượt trước. Đầu lượt chạy lại có đúng 13 đường dẫn của phiếu 200, được chỉ thị 12:58 cho phép giữ và tiếp tục. Có `node_modules/.modules.yaml`; không cài gói. `art-src/ui` và `public/assets/typing-defense/ui` trỏ đúng vào checkout chính. Phiếu 199 đã có báo cáo dừng và giao điểm chặn riêng; lượt này không làm tiếp hoặc sửa phần của 199.

Chỉ sửa các đường dẫn được phiếu cho phép. Không Git ghi, không sửa kit, `src/view`, luật chơi, ván vàng, worktree khác, game khác hoặc Tu Tiên. Không chạy dev server, trình duyệt hay mạng. Không sinh ảnh/âm thanh mới; ảnh dẫn xuất bằng công cụ từ sáu nguồn đã nhận, không có prompt sinh ảnh mới.

## Đã làm

Các đường dẫn mã dưới đây tính từ gốc worktree:

- `scripts/td/ui-picks.json`: sáu mục nhận, nguồn/điểm M–Q/file chấm, cắt và kích thước của 16 đầu ra; favicon có `until: "177"`.
- `scripts/td/prepare-ui.mjs`: `plan()` thuần; ImageMagick 7 qua `ART_MAGICK`, sRGB, Lanczos, chỉ cắt/trim alpha/đệm vuông/thu nhỏ. WebP nền Q84, alpha Q88 + alpha-quality 100 + exact. Kiểm kích thước nguồn và đầu ra. `--check` không ghi; mục cũ hơn nguồn báo lỗi, lượt xuất từ chối ghi đè. Mọi đầu ra nằm trong danh sách.
- `src/ui/art.ts`: nơi duy nhất trong `src/` có URL UI; srcset/sizes; xử lý cả sự kiện lỗi lẫn `complete && naturalWidth === 0`. Cảnh báo có tên và URL được chọn, ẩn ảnh; chữ logo dự phòng chỉ hiện khi ảnh lỗi.
- `src/ui/title.ts`, `title.css`: nền 158 v2 toàn màn, fade 1,4 giây; bỏ URL tranh cũ và lớp phủ tối toàn tranh. Logo nguyên khổ, hộp ảnh rộng 45vw, giữa ngang. Bù lề alpha trên (`153/2172 × 45vw ≈ 3,17vw`) để **mép phần vẽ** ở 5,5vh; không cắt logo. Phụ đề ở dưới, menu giữ nguyên vị trí. Không thêm vệt tối sau logo vì mock đọc được. Góc trên phải không có thành phần mới.
- `index.html`, `src/main.ts`: favicon 32/64 PNG; dòng nạp có logo 120/180 px CSS và “loading words…”. Tên trong `h1` được lấy từ `alt="Wordwoven"`; khi lỗi, ảnh ẩn và chữ thật hiện, không đọc hai lần.
- `src/ui/sheets.ts`, `td.css`: crest nằm trong thẻ, banner sau chữ tiêu đề thật, divider sau bảng số và trước ôn/nút. Cả ba trang trí `alt="" aria-hidden="true"`, chỉ tạo phần tử ảnh khi kết quả hiện. Crest thua `grayscale(0.5) brightness(0.75)`. Ở chiều cao ≤800 px: crest 72 px, thẻ kết có khoảng cách/dòng số và ôn gọn hơn; thẻ tạm dừng giữ nguyên.
- `scripts/visual/scenarios/td-theme.mjs`: kiểm nền mới, `painted: true`, `drawn: 0`, logo tải được/rộng 40–50%/tên Wordwoven, hai favicon HTTP 200 `image/png`, ba ảnh thẻ kết tải được. **Chỉ sửa, không chạy.**
- `tests/td-ui-art.test.ts`: danh sách ↔ catalog hai chiều; cỡ/cắt/không phóng to/bỏ mục chưa nhận; HTML màn tựa, thẻ thắng/thua/tạm dừng, divider trước ôn và trước nút; lỗi ảnh/cached load; favicon và dòng nạp. Môi trường Node, không thêm thư viện DOM, không yêu cầu media hiện diện.
- `docs/changelog/2026-10-30-title-results-art.md` và một hàng trong `docs/changelog/README.md`: ghi WW-01, WW-02, WW-03, WW-08, WW-56 đã gắn.

## Chín mục kiểm

| Mục | Kết quả thật |
|---|---|
| 1 · `pnpm check` | **Exit 0**, kit **42/42 file khớp**, **43 file test / 405 test qua**, 0 đỏ; Vitest 8,30 giây, TypeScript và build qua. Không có test thời gian đỏ nên không cần chạy riêng ba lần. [check.txt](200/check.txt). Lượt trước: **21/21 test riêng qua** (13 mới, 8 có sẵn); test mới viết/chạy trước mã, lượt đỏ đầu do chưa có module danh sách chọn. |
| 2 · Ngân sách `/` ≤85 kB gzip | **Trước 81.583 B (81,583 kB), sau 82.314 B (82,314 kB)**; tăng **731 B**, còn dư **2.686 B**. Mốc trước build đúng mã `2a1f61d` bằng `git archive` trong `games/.wt-td-ui/tmp/200-baseline-2a1f61d/`, dùng cùng bộ dependency đã cài. [budget.json](200/budget.json), [baseline-budget.txt](200/baseline-budget.txt), [after-budget.txt](200/after-budget.txt). |
| 3 · Golden | `pnpm td:golden:check` exit **0**, **2/2 same:true**, changed `{}`, problems/rejected 0. Nội dung `f2a21037`, bộ từ `9c9b91d8`; thường 19.660 tick/389 lệnh, boss 5.695 tick/49 lệnh. |
| 4 · Media | **16/16 đúng px**, tổng **1.121.340 B**. Hai nền **256.422 B / 332.700 B**, đều ≤400 kB. [media.json](200/media.json) có px, byte, md5 và **đường dẫn thật trong `games/typing-defense/public/assets/typing-defense/ui/`** để Claude `media:push`. |
| 5 · Check/cache | Kiểm lại trong lượt này: `ART_MAGICK=/opt/homebrew/bin/magick node scripts/td/prepare-ui.mjs --check` exit **0**; chạy script tiếp theo exit **0**, **0 written, 16 fresh**. Toàn bộ media giữ nguyên md5. Trong lượt triển khai đầu, phép co theo hộp làm divider 640 còn 638 px; đã sửa co theo chiều rộng, chỉ bỏ và xuất lại file lỗi do chính lượt đó vừa tạo. Kết quả cuối 640 ×95. |
| 6 · Nguồn | **6/6 md5 trước = sau**, [sources-md5.json](200/sources-md5.json). Không sửa màu ruộng, không ghi `art-src`. |
| 7 · Chuỗi URL | `title-dusk`: **0** trong `src/` và `index.html`. Tiền tố URL UI chỉ có ở **`src/ui/art.ts`, `index.html`**. File media cũ `title-dusk.webp` vẫn còn nguyên. |
| 8 · Xem tĩnh | Lượt này đã mở lại đủ năm file của bốn nhóm tờ ở độ phân giải gốc và đối chiếu mock 158, gồm hai nền giấy/tối và favicon ×4 không làm mượt. Không thấy vệt khối lớn, dải màu rõ hoặc viền hồng quanh logo/huy hiệu ở cỡ dùng. Logo đọc rõ trên trời; crest thua giảm màu/sáng nhưng còn đọc như huy hiệu chiến thắng, nên nhận diện thua cần Claude xem tiếp. Đây là mock, **không phải nghiệm thu trình duyệt**. |
| 9 · Phạm vi Git | Trạng thái cuối chỉ 13 đường dẫn mã/test/changelog được phép trong worktree; danh sách ở [status.txt](200/status.txt). Media và mock bị ignore, không đưa ảnh vào Git. Báo cáo/số liệu nằm đúng repo cha. |

Số liệu tổng hợp: [verification.json](200/verification.json). `node --check scripts/visual/scenarios/td-theme.mjs` exit 0.

**Cách build mốc trước:** bản archive nằm trong `tmp/`, không tạo Git worktree hay sửa Git. `pnpm build` tại archive bị pnpm từ chối trong kiểm dependency tự động vì `node_modules` là liên kết ra ngoài gốc archive ([log](200/baseline-pnpm-attempt.txt)); chưa cài hoặc xóa dependency. Đã chạy trực tiếp đủ ba bước đúng script build: `node node_modules/typescript/bin/tsc --noEmit && node node_modules/vite/bin/vite.js build && node scripts/bundle-budget.mjs`, exit **0**. Cả trước/sau dùng cùng dependency hiện có, không mạng. Kích thước gzip tính từ manifest và byte JS bằng `gzipSync`, cùng phép đo của `bundle-budget.mjs`. Gói vào thẳng `/?title=0`: **83.041 → 83.754 B**; phần 3D riêng **171,83 kB**, cũng qua trần của script. Cảnh báo Vite về chunk Three.js >500 kB có ở cả hai bản; không có lỗi build hay ngân sách.

## Tờ xem

Đặt tại **`games/.wt-td-ui/tmp/200/`**, không trong `docs`, `art-src` hoặc `public`:

- [files.jpg](../../games/.wt-td-ui/tmp/200/files.jpg): mọi đầu ra ở cỡ dùng trên tối `#1c1824` và giấy `#fff4d6`.
- [title-mock-1280.jpg](../../games/.wt-td-ui/tmp/200/title-mock-1280.jpg), [title-mock-1920.jpg](../../games/.wt-td-ui/tmp/200/title-mock-1920.jpg): nền/logo theo tọa độ CSS; phụ đề minh họa bằng Arial. Không mô phỏng toàn bộ menu hay font game.
- [favicon.jpg](../../games/.wt-td-ui/tmp/200/favicon.jpg): 32/64 trên tab sáng/tối, ×4 nearest-neighbour.
- [results-mock.jpg](../../games/.wt-td-ui/tmp/200/results-mock.jpg): ảnh thẻ thắng/thua trên giấy; bản thua dùng ma trận tương ứng bộ lọc CSS. Không phải kết quả dựng DOM.

Phiếu gọi “bốn tờ” nhưng liệt kê **năm tên file** (hai cỡ title). Đã giữ đủ năm tên, tương ứng bốn nhóm trên; không giữ khung thô. Có script dựng lại `tmp/200/make-mocks.py`, không tạo raw frame nên không có raw frame cần prune.

## Còn mở và bàn giao

**Cần chủ dự án/Claude xem:** duyệt diff; chạy `td-theme` ở 1280 ×720 và 1920 ×1080, kiểm tên đọc màn hình, ảnh lỗi, crest trong thẻ và thẻ thắng đủ năm từ ôn không cuộn. Codex đã chạy đủ kiểm tĩnh, toàn bộ test, build và ngân sách theo chỉ thị chạy lại; không còn chờ ngoại lệ. Claude `media:push` theo `200/media.json`, rồi commit sau nghiệm thu. Lượt này không thay logic hay ghi lại media; cập nhật số kiểm, báo cáo và changelog.

Chưa làm và đúng ngoài phạm vi: crest thua riêng (nếu lớp làm mờ chưa đủ), icon sao WW-57, bảng `panel-large` 115 chưa nhận, tranh thắng/thua 183, favicon mới chờ 177, nút Settings/loa 193. Không sửa ruộng vàng chanh của 158; lượt sửa tranh sau đã được quyết trong verdict. Khi gộp 193 từ `td-keys`, Claude giải xung đột màn tựa sau 200 và 203 theo phiếu; không đổi tên class hoặc sắp lại phần điều khiển có sẵn.
