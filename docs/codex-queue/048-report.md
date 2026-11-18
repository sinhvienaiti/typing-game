# Phiếu 048 · Công cụ dọn ảnh thô của lượt chụp test

Ngày 28/10/2026 · Mac mini M4, macOS, Node v24.22.0. Đã làm công cụ và chạy thử; **chưa đạt nguyên văn đủ bốn kiểm** vì lệnh test theo thư mục không được Node hiện tại hỗ trợ và số file/Git thay đổi trong lúc các làn khác chạy. Không chạy `--apply` trên dữ liệu thật.

## Sản phẩm và cách dùng

Đã tạo năm file được giao:

- `tools/capture-prune/prune.mjs`: CLI Node ESM, không gói ngoài; mặc định chỉ liệt kê, bảng nhóm cấp 1, JSON, tùy chọn xóa và nhật ký.
- `tools/capture-prune/test/prune.test.mjs`: 12 test, cây giả dưới `os.tmpdir()`, kiểm MD5 file giữ lại sau khi áp dụng.
- `tools/capture-prune/README.md`: hướng dẫn tiếng Việt, luật chọn/giữ/từ chối, mã thoát và giới hạn.
- `tools/capture-prune/.gitignore`: đúng một dòng `.tmp/`.
- `docs/codex-queue/048-report.md`: báo cáo này.

Đầu ra phụ được phiếu chỉ định: `tools/capture-prune/.tmp/dry-run.json`, bị Git bỏ qua. Không tạo ảnh, âm thanh hoặc bản chụp kiểm tra.

```bash
node tools/capture-prune/prune.mjs games/dragon-hold/tmp/run-cua-ban
node tools/capture-prune/prune.mjs games/dragon-hold/tmp/run-cua-ban --min-age-min 60 --docs docs games/dragon-hold/docs
node tools/capture-prune/prune.mjs games/dragon-hold/tmp/run-cua-ban --apply
```

Lệnh cuối là hướng dẫn cho chủ lượt chụp; không thực thi trên cây thật trong phiên. Luôn chọn lượt do chính mình tạo; công cụ không biết tác giả của ảnh. Dùng `--json <file.json>` ngoài các đích để lưu kết quả; cho phép ghi lại JSON thường, chặn symlink/hard link và kiểm đầu ra trước khi xóa.

## Luật giữ và từ chối

Chỉ xét PNG/JPG/JPEG/WebP, không phân biệt hoa thường. Giữ tên chứa `sheet`, `contact`, `compare`; ảnh dưới thư mục bắt đầu `compare`; ảnh được Markdown trỏ tới bằng chuỗi `tmp/...`; ảnh có mtime trong 30 phút gần nhất, trừ khi đổi `--min-age-min`. JSON ghi đủ lý do giữ nếu một ảnh khớp nhiều luật. Giữ nguyên file JSON/MD và mọi loại ngoài bốn đuôi ảnh.

Quét Markdown mặc định dưới `docs`, `games/*/docs`, `games/*/*.md`, không duyệt game Tu Tiên đang dừng. `--docs` nhận nhiều gốc hoặc file, thay thế mặc định. Chuỗi ảnh lấy bằng biểu thức trong phiếu, đối chiếu hậu tố của đường dẫn POSIX tính từ repo; cả `tmp/...` và `games/x/tmp/...` được kiểm trong test.

Từ chối đích nếu realpath không có thành phần `tmp`, ra ngoài repo và cây anh em `../typing-game-wt/`, hoặc có thư mục bảo vệ `art-src`, `public`, `docs`, `typing-game-handoff`, `immortality-cultivation`. So theo thành phần thư mục, gồm biến thể nối bằng `-`/`_`, để `htdocs` không bị nhầm thành `docs`. Không duyệt thư mục con bảo vệ, symlink thư mục hoặc file; realpath ra ngoài đích ghi `refused`. Mọi đích bị từ chối thì thoát 2.

`--apply` dùng đúng danh sách vừa tính, kiểm lại nhận dạng/kích thước/mtime/ctime, đường dẫn thật và symlink thư mục cha. File đã đổi bị bỏ qua, file mới xuất hiện không được thêm vào danh sách xóa. Ghi mỗi lần xóa thành công vào `.pruned-YYYYMMDD-HHmm.txt` của từng đích, đường dẫn tương đối và số byte. Nhật ký giữ chỗ độc quyền trước khi xóa để tránh ghi đè; nhật ký cùng phút đã tồn tại thì không xóa tại đích đó. Không xóa thư mục rỗng.

Lượt chạy thật đầu tiên từ chối cả ba đích vì kiểm chuỗi `docs` bắt nhầm `htdocs`. Đã sửa theo thành phần thư mục, thêm test hồi quy, chạy lại 12/12 và lấy lại mốc trước/sau cho lượt hợp lệ dưới đây. Không có ảnh nào bị xóa trong cả hai lượt.

## Bốn kiểm bắt buộc

| # | Kiểm | Kết quả |
|---:|---|---|
| 1 | `node --test tools/capture-prune/test` | **Không đạt nguyên văn**: Node v24.22.0 báo `MODULE_NOT_FOUND`, thoát 1 vì nhận thư mục như module. Lệnh tương thích `node --test tools/capture-prune/test/*.test.mjs` **đạt 12/12**, thoát 0. Không thêm `index.js` ngoài danh sách cho phép. |
| 2 | Chạy thử ba đích thật với `--json tools/capture-prune/.tmp/dry-run.json`, không `--apply` | **Đạt**, thoát 0, đủ ba đích. Dự kiến 52.404 ảnh, 24.996.732.841 byte; giữ 4.503 ảnh, gồm 2.278 ảnh quá mới. Bảng chi tiết bên dưới. |
| 3 | `md5 -r` 200 ảnh trước/sau; `find games -path '*/tmp/*' -type f \| wc -l` trước/sau | **MD5 đạt 200/200 không đổi**. **Số file không đạt điều kiện bất biến**: 112.912 → 113.013, tăng 101 trong khoảng kiểm tra có làn khác đang hoạt động. Hai lượt đếm này không báo lỗi. Không kết luận số file toàn cây không đổi. |
| 4 | `git status --short` so mốc đầu; `git check-ignore -v tools/capture-prune/.tmp/dry-run.json` | **Phạm vi phiếu đạt**: chỉ tạo năm file giao và JSON phụ được yêu cầu; JSON bị bỏ qua đúng dòng 1 `.tmp/`. **Git toàn repo không đạt nguyên văn “chỉ thêm”**: dòng `M games/dragon-hold` có đầu phiên đã biến mất trong lúc kiểm tra; không can thiệp thay đổi của làn khác. |

Bộ test gồm chọn đúng bốn đuôi ảnh; giữ sheet/contact/compare và thư mục compare; tham chiếu Markdown ở mọi gốc mặc định và `--docs`; mtime mới, đúng biên và tương lai; từ chối đích thiếu tmp, thư mục bảo vệ, ngoài gốc/tiền tố giả; worktree; đích trùng/chồng; symlink file/thư mục/gãy; `--apply` và nội dung nhật ký; MD5 mọi file giữ lại; file hoặc thư mục cha đổi sau lập danh sách; nhật ký trùng phút; JSON và mã thoát CLI. Mọi áp dụng/xóa fixture chỉ diễn ra dưới thư mục tạm do test tự tạo.

### Bảng chạy thử thật

Lệnh đã chạy:

```bash
node tools/capture-prune/prune.mjs games/dragon-hold/tmp games/typing-defense/tmp games/typing-survival/tmp --json tools/capture-prune/.tmp/dry-run.json
```

Đơn vị MB thập phân: 1 MB = 1.000.000 byte. Số liệu là tại thời điểm quét; không phải dung lượng đã giải phóng.

| Thư mục | Ảnh dự kiến xóa | Byte | MB | Ảnh giữ | Giữ vì quá mới | Giữ vì tài liệu |
|---|---:|---:|---:|---:|---:|---:|
| `games/dragon-hold/tmp` | 15.924 | 5.798.361.199 | 5.798,361 | 1.096 | 348 | 18 |
| `games/typing-defense/tmp` | 1 | 104.573 | 0,105 | 274 | 0 | 1 |
| `games/typing-survival/tmp` | 36.479 | 19.198.267.069 | 19.198,267 | 3.133 | 1.930 | 2 |
| **Tổng** | **52.404** | **24.996.732.841** | **24.996,733** | **4.503** | **2.278** | **21** |

Lý do giữ có thể chồng nhau. Có 710 mục trong `refused`: 53 symlink ra ngoài đích (`outside-target`), 622 symlink còn lại (`symlink`), 35 thư mục con bảo vệ (`protected-path`). Đây là các mục bị bỏ qua bên trong ba đích hợp lệ, không phải ba đích bị từ chối. JSON giữ đầy đủ đường dẫn, ảnh dự kiến, byte, lý do giữ và từ chối; stdout in cả bảng nhóm cấp 1.

### Bằng chứng MD5 và số file

Chọn 200 ảnh thường dưới `games/dragon-hold/tmp`, không theo symlink; giữ nguyên danh sách trong bộ nhớ phiên và gọi trực tiếp lệnh `md5 -r` trước/sau lượt chạy hợp lệ. So toàn bộ stdout theo cùng thứ tự: bằng nhau, không file thiếu hay đổi nội dung. Không ghi snapshot cạnh media. Ảnh đầu là `games/dragon-hold/tmp/tag-compare.png`, ảnh cuối là `games/dragon-hold/tmp/m0b/preview/props__pine-river-bush-blossom__front.png`.

SHA-256 của stdout MD5 UTF-8, gồm dấu xuống dòng cuối:

```text
f029c1badf4c619be366a8f82976860e89f4d95ff487f199f9a482e38098bbd4
```

Lệnh đếm nguyên văn trước/sau cho 112.912 và 113.013. Mức tăng phù hợp với bối cảnh các lượt chụp đồng thời, nhưng không dùng nhận định đó để đánh dấu kiểm bất biến là đạt. Một lượt đếm thăm dò trước khi sửa công cụ có cảnh báo hai thư mục worktree biến mất; không dùng lượt đó làm mốc kiểm cuối.

### Git đầu phiên và phạm vi

```text
 M docs/games/3D_REQUESTS.md
 M games/dragon-hold
 M games/typing-defense
 M games/typing-survival
?? .claude/launch.json
?? TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md
?? docs/codex-queue/035-report.md
?? docs/codex-queue/036-report.md
?? docs/codex-queue/047-report.md
?? docs/tools/map-factory/
```

Phần riêng phiếu được kiểm bằng `git status --short --untracked-files=all -- tools/capture-prune docs/codex-queue/048-report.md`; chỉ năm đường dẫn sản phẩm. Kiểm ignore có kết quả:

```text
tools/capture-prune/.gitignore:1:.tmp/  tools/capture-prune/.tmp/dry-run.json
```

## Bỏ qua và phần chủ dự án cần xem

- Không xóa ảnh thật, không chạy game/build/test suite game, mạng, dev server hoặc trình duyệt; không dùng Git có ghi; không sửa Tu Tiên, game code/docs, audio-lab hay file của làn khác.
- Chưa thể đánh dấu “xong khi bốn kiểm đạt”: cần chủ dự án chấp nhận lệnh test glob trên Node này hoặc mở quyền thêm điểm vào test; kiểm bất biến số file/Git toàn repo cần một khoảng không có thay đổi đồng thời. Không làm sạch hay giữ chân các làn khác để ép kết quả.
- Chủ dự án có thể xem JSON và bảng nhóm trước khi quyết định dọn từng lượt của mình; 24.996,733 MB là dung lượng có thể chọn theo luật, chưa được giải phóng.
