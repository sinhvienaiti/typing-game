# Phiếu 131 · Dragonhold · Chuyển chữ hiển thị sang tiếng Anh

## Trạng thái

Đã dịch phần nguồn được phép, lập đủ ba bảng và thêm test quét. **Chưa đủ
điều kiện đóng phiếu:** test quét toàn bộ `src/` gặp trang dev âm thanh ngoài
phạm vi được ghi. Không tự ý sửa trang đó hoặc nới test để lấy kết quả xanh.
Đã hỏi chủ dự án chọn loại riêng trang dev khỏi test hoặc mở phạm vi dịch;
đang chờ trả lời. Tên nhãn rất ngắn có một số trường hợp vượt 20%, đã gắn cờ
trong bảng để Claude duyệt; chưa xác nhận tiêu chí độ dài cho các ô này.

Mã nằm ở `games/.wt-dh-codex`, nhánh `dh-codex`, HEAD nền
`5a83f70e5072bcd45c18c2a6618b067e711bd0df`; lúc bắt đầu worktree sạch.
Đường dẫn mã bên dưới tính từ worktree. Báo cáo và các bảng được ghi ở repo
cha, đúng yêu cầu.

## Đã làm

- **325 chuỗi nguồn/trang**, **44 chuỗi kỳ vọng/fixture test** được đổi.
  Giữ id, tên trường `nameVi`, khóa lưu, event, phím và số. Không sửa sim,
  typing, luật hay dữ liệu golden.
- `index.html`: `lang="en"`, tên **Dragonhold**, mô tả bằng tiếng Anh.
- `src/app/{app,pace-card,typing-pace}.ts`: menu, tốc độ gõ, thông báo nạp,
  cảnh báo IME, mất tiêu điểm, gợi ý mức dễ và thông báo tua nhanh.
- `src/ui/{debut-card,hud,learning-frame,placement-ui,results,shop-strip,tags,ui-preview,wave-card}.ts`:
  thẻ, nhãn, tooltip, banner, toast, gợi ý phím và lời gợi ý thua.
- `src/content/data/{maps,stages}.ts`: chỉ đổi tên hiển thị của bản đồ,
  ba đường và ải. Các thực thể đã mang tên tiếng Anh theo `NAMES_EN.md`
  được giữ. Hai rồng giữ tên riêng dưới dạng `Hoa Long`, `Bach Long`.
- `src/view/{banners,bench,heroes,stage}.ts`: nhãn cắm cờ, hướng dẫn xem
  cảnh và nhãn chẩn đoán. Không đổi cách dựng cảnh.
- Tám test cũ trong `tests/{ui,app}` được cập nhật kỳ vọng chuỗi;
  `tests/english-ui.test.ts` mới có **5 test** quét chữ và tên trang.
- Changelog trong worktree:
  `docs/changelog/2026-10-29-english-ui.md`.

## Bảng duyệt và cách quét

- [Chuỗi trước sửa](131/strings-before.md): **329 dòng literal/template**
  có chữ Việt hoặc được bổ sung sau đọc các điểm hiển thị. Bỏ nghĩa từ và
  chú thích; có ghi nhãn chẩn đoán view. Số dòng theo HEAD nền.
- [Bảng cũ → mới](131/strings.md): **369 chuỗi đổi**. Template được ghi
  nguyên biểu thức, không đếm trùng literal con; vì vậy số dòng khác bảng
  kiểm kê ban đầu. Có ghi cả kỳ vọng/fixture test để duyệt đầy đủ.
- [Còn lại](131/remaining.md): 15 literal/template nghĩa từ được giữ,
  86 literal/template trong kit, chú thích và dữ liệu biên soạn cảnh,
  cùng ngoại lệ đang vướng ở trang dev âm thanh.
- [Quét thô](131/remaining-raw.txt): đầu ra đúng khoảng `[À-ỹđĐ]` trên
  toàn bộ nguồn. Khoảng này còn bắt dấu nhân × và ký tự IPA. AST kiểm
  các chữ Việt thực, chuẩn hóa NFC và đọc giá trị literal nên bắt cả
  chuỗi có Unicode escape.

Ngoại lệ nghĩa từ của test chỉ ở `src/ui/ui-preview.ts`: các trường `vi`
và đúng template hiện “khu rừng”. Không loại cả file này; các nhãn khác
trong cùng file vẫn được quét. Các chỗ đọc/hiện `vi` động trong khung học,
sổ từ và lớp học không bị dịch. Test bỏ chú thích mã và chú thích nhúng
CSS/GLSL; trường `brief` của JSON bản đồ là dữ liệu biên soạn, không hiện
cho người chơi.

Đã đọc toàn bộ các điểm hiển thị để bắt chữ Việt không dấu mà khoảng
ký tự không tìm được: `Nhanh`, `Tinh anh`, `Nghe`, `sao`, `bay`.
Các nhãn rút gọn và mọi chuỗi đo dài hơn 20% sau bỏ HTML được gắn cờ.
Phép đếm fragment không đại diện độ rộng của cả dòng sau nội suy;
chưa dùng trình duyệt để kết luận chữ không tràn. `Easy`, `Hard`, `Wave`,
`Armor`, `Sell` là các ví dụ cần Claude duyệt ở kích thước thật.

## Bốn mục kiểm bắt buộc

| Mục | Kết quả thực chạy | Bằng chứng |
| --- | --- | --- |
| `pnpm check` trước sửa | Mã thoát 0; **475/475 test**, **54/54 file**; kit, TypeScript, build xanh | [check-before.log](131/check-before.log) |
| UI/app sau dịch | Mã thoát 0; **109/109 test**, **14/14 file** | [ui-app-tests.log](131/ui-app-tests.log) |
| `pnpm check` sau sửa | Mã thoát 1; **479 test xanh, 1 đỏ / 480**, **54 file xanh, 1 đỏ / 55**; kit xanh; dừng ở test quét, chưa tới build | [check-after.log](131/check-after.log) |
| TypeScript sau sửa | `pnpm exec tsc --noEmit`, mã thoát 0 | [typecheck.log](131/typecheck.log) |
| Golden chạy riêng | Mã thoát 0; **10/10 test** | [golden.log](131/golden.log) |
| Diff golden | Rỗng, **0 byte** | [golden-diff-stat.log](131/golden-diff-stat.log) |
| Đột biến thêm `"Bắt đầu"` | Mã thoát 1; test quét ghi đúng file UI được chèn; **17 mục** thay vì 16 | [mutation-red.log](131/mutation-red.log) |
| Khôi phục đột biến | Khôi phục đúng từng byte; file UI không còn trong lỗi; **16 mục** cũ ở trang dev; mã thoát 1, **chưa xanh** | [mutation-restored.log](131/mutation-restored.log), [mutation.json](131/mutation.json) |
| Phạm vi status | Chỉ các đường dẫn được phép; chi tiết và số file ở `scope.json` | [status.txt](131/status.txt), [scope.json](131/scope.json) |

Số test **475 → 480 (+5)**. Các test cũ đều đạt trong lượt `check` sau sửa;
không có test thời gian đỏ, nên không phát sinh lượt chạy riêng ba lần.
Lỗi test quét duy nhất là **15 literal của `src/audio/dev/harness.ts` và
một mục `src/audio/dev/harness.html`**. Không nhập các đường dẫn này vào
ngoại lệ khi chưa có quyết định của chủ dự án.

## Phần bỏ qua và việc người duyệt cần xem

Không mở dev server/trình duyệt, không tạo media, không cập nhật golden,
không dùng Git ghi, không sửa kit, game chính, worktree khác hay Tu Tiên.
`pnpm check` trước sửa có build vì chính mục kiểm bắt buộc của phiếu yêu
cầu lệnh này; không chạy build độc lập.

Chủ dự án cần chốt phạm vi trang dev âm thanh. Sau đó mới hoàn tất lượt
quét xanh, đột biến đỏ → xanh và `pnpm check` xanh cuối. Claude cần duyệt
369 dòng chữ, các cờ độ dài/tên riêng, chuyển phần kit cho làn kit, rồi
kiểm từng màn ở 1280 và 1920 trước commit/gộp. Lượt này không tuyên bố
nghiệm thu hình ảnh hoặc hoàn tất cả bốn mục.
