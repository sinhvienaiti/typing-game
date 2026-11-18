# Phiếu 048 · Công cụ `tools/capture-prune`: dọn ảnh thô của lượt chụp test, giữ tờ ghép và ảnh tài liệu trỏ tới

**Bối cảnh:**
- Ngày 28/10 ổ đĩa đầy vì ảnh test: 94 nghìn PNG và 79 nghìn JPG, tổng 77 GB, nằm trong `tmp/` của các game.
- Chủ dự án chốt luật (`AGENTS.md`, mục "Test captures"): chụp xong và chấm xong thì xóa ảnh thô của chính lượt đó.
- Giữ lại: tờ ghép (sheet, contact), ảnh so sánh (compare), ảnh mà tài liệu trỏ tới, và số liệu JSON/MD.
- Claude đã dọn tay một lần bằng một đoạn bash. Phiếu này làm công cụ dùng lại được, an toàn, mặc định chỉ liệt kê.

**Thư mục làm việc:** repo cha (`.`).

**Chỉ được ghi:**
- `tools/capture-prune/prune.mjs`: Node ESM, không gói ngoài;
- `tools/capture-prune/test/prune.test.mjs`;
- `tools/capture-prune/README.md` (tiếng Việt);
- `tools/capture-prune/.gitignore` chứa một dòng `.tmp/` (giống `tools/art-normalize/.gitignore`);
- `docs/codex-queue/048-report.md`.

**Cấm:**
- chạy `--apply` trên bất kỳ thư mục thật nào; chỉ chạy `--apply` trong thư mục tạm do test tự tạo dưới `os.tmpdir()`;
- xóa, sửa, chép file nào ngoài thư mục tạm của test;
- lệnh git có ghi; mạng; dev server; trình duyệt;
- đụng Tu Tiên.

## Lệnh

```bash
node tools/capture-prune/prune.mjs <thư mục>... [--apply] [--min-age-min 30] [--docs <gốc tài liệu>...] [--json <file>]
```

- Mặc định chỉ chạy thử: in danh sách file sẽ xóa, rồi một bảng theo thư mục con cấp 1 (số file, MB) và một dòng tổng.
- `--apply` mới xóa, và chỉ xóa đúng danh sách vừa tính. Sau khi xóa, ghi danh sách vào `<thư mục>/.pruned-<YYYYMMDD-HHmm>.txt`: mỗi dòng gồm đường dẫn tương đối và số byte.
- `--json`: ghi kết quả dạng JSON gồm `targets`, `files[]`, `kept[]` (kèm lý do giữ), `bytes` và `refused[]`.

## Luật chọn file

1. **Chỉ ảnh:** đuôi `.png`, `.jpg`, `.jpeg`, `.webp`, không phân biệt hoa thường.
2. **Giữ, không liệt kê:**
   - tên file chứa `sheet`, `contact` hoặc `compare`, không phân biệt hoa thường;
   - file nằm trong thư mục có tên bắt đầu bằng `compare`;
   - file được tài liệu trỏ tới. Quét mọi `.md` dưới các gốc `--docs` (mặc định `docs`, `games/*/docs` và `games/*/*.md`). Lấy mọi chuỗi khớp `tmp/[^\s)\`"'<>]+\.(png|jpe?g|webp)`. Giữ file nếu đường dẫn POSIX của nó, tính từ gốc repo, **kết thúc bằng** chuỗi đó;
   - file sửa trong `--min-age-min` phút gần nhất (mặc định 30), để không xóa ảnh của lượt chụp đang chạy.
3. **Từ chối cả thư mục** (ghi vào `refused`, không liệt kê gì trong đó, mã thoát 2 nếu mọi thư mục đều bị từ chối):
   - đường dẫn thật (`realpath`) không chứa đoạn `/tmp/` hoặc không kết thúc bằng `/tmp`. Ví dụ `games/dragon-hold/art-src` bị từ chối, `games/dragon-hold/tmp/mac-2026-10-27` được nhận;
   - đường dẫn thật nằm ngoài gốc repo và ngoài `../typing-game-wt/`;
   - đường dẫn thật chứa `art-src`, `public`, `docs`, `typing-game-handoff`, `immortality-cultivation`.
4. **Liên kết tượng trưng:**
   - không đi theo symlink thư mục;
   - không liệt kê file là symlink;
   - file nào có `realpath` ra ngoài thư mục đích thì bỏ qua và ghi vào `refused`.

## Kiểm (bắt buộc)

1. `node --test tools/capture-prune/test`. Test tự dựng cây giả dưới `os.tmpdir()`, có ít nhất:
   - chạy thử liệt kê đúng ảnh thô; bỏ sheet, contact, compare và file trong thư mục `compare*`;
   - giữ ảnh được một `.md` giả trỏ tới bằng `tmp/...` và bằng `games/x/tmp/...`;
   - `--min-age-min` giữ file mới (đặt mtime bằng `fs.utimesSync`);
   - từ chối thư mục không có `/tmp/`, thư mục `art-src` và thư mục ngoài gốc;
   - symlink thư mục trỏ ra ngoài thì không đi theo; file symlink không liệt kê;
   - `--apply` xóa đúng danh sách và ghi `.pruned-*.txt`; file giữ lại còn nguyên (so md5).
2. **Chạy thử trên máy thật, không `--apply`:**
   - `node tools/capture-prune/prune.mjs games/dragon-hold/tmp games/typing-defense/tmp games/typing-survival/tmp --json tools/capture-prune/.tmp/dry-run.json`;
   - ghi vào báo cáo số file và MB của từng thư mục.

   Các lane đang chạy có thể đang chụp; luật `--min-age-min` phải giữ ảnh mới của họ, và báo cáo ghi số file được giữ vì quá mới.
3. **md5:**
   - tính `md5 -r` cho 200 file ảnh bất kỳ dưới `games/*/tmp`, trước và sau bước 2;
   - đối chiếu `find games -path '*/tmp/*' -type f | wc -l` trước và sau;
   - cả hai phải không đổi.
4. `git status --short`: so với lúc bắt đầu, chỉ **thêm** file trong `tools/capture-prune/` và `docs/codex-queue/048-report.md`. `git check-ignore tools/capture-prune/.tmp/dry-run.json` phải in ra luật của `tools/capture-prune/.gitignore`.

## Báo cáo `docs/codex-queue/048-report.md`

- Cách dùng.
- Luật giữ file và luật từ chối.
- Kết quả bốn kiểm, gồm bảng chạy thử theo thư mục.

**Xong khi:** bốn kiểm đạt.
