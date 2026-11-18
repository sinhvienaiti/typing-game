# Trang xem lại Firefly

Dựng HTML tĩnh bằng Python 3; máy chủ dùng Node.js và chỉ nghe `127.0.0.1`.
Chạy từ gốc repo:

```sh
python3 tools/review-gallery/build.py \
  --sprint games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05 \
  --lab games/immortality-cultivation/art-src/lab \
  --jobs 'docs/work/tasks/*.json' \
  --root /Volumes/SS990TPRO/htdocs \
  --notes tools/review-gallery/notes-2026-11-05.json \
  --out /private/tmp/firefly-review.html
```

Mỗi lần kiểm hoặc test phải truyền `--out` tới tệp tạm. Nếu bỏ `--out`, script
ghi vào trang hiện tại của anh:
`<htdocs>/typing-game-review/owner-review/2026-11-05/tu-tien/firefly-gallery/index.html`.
Các mặc định khác: sprint như ví dụ, lab là thư mục cha của sprint, jobs như ví dụ,
root là thư mục cha của repo. Gốc repo được suy từ vị trí script, không theo thư mục
đang chạy; glob `--jobs` tính từ gốc repo, cũng nhận glob tuyệt đối.

`--notes` là tùy chọn. Không truyền thì dùng tiêu đề chung, không có danh sách loại
riêng cho đợt 05/11. File mẫu chứa `title`, `h1`, `lead`, `notes` (ID → lý do),
`stone` (ID bị gỡ vì nền đá), `rejectedDirs` (tên thư mục con của sprint → lý do).
`lead` nhận `{jobs}`, `{takes}`, `{stills}` để chèn tổng. Chữ được escape khi xuất
HTML. Chỉ đọc tên thư mục đúng trong `rejectedDirs`, không quét bằng glob.
Manifest `lab/vfx/*/manifest.json` có `/video/<id>/take` đánh dấu việc đó “Trong lab”,
ưu tiên trước ghi chú loại. Video xem trước chỉ phát khi rê chuột; mỗi lúc một video.

```sh
node tools/review-gallery/serve.mjs --root /Volumes/SS990TPRO/htdocs --port 4330
# Tương thích lời gọi cũ:
node tools/review-gallery/serve.mjs 4330
```

Máy chủ mặc định dùng htdocs suy từ vị trí script và cổng 4330. Nó phục vụ file
trong root, hỗ trợ Range cho video và chặn đường dẫn/symlink đi ra ngoài root.
Mở URL tính từ root. HTML ở `/private/tmp` trong ví dụ dùng để kiểm và so sánh;
khi xuất trang để xem qua máy chủ, chọn `--root` chứa cả HTML lẫn media và đặt
`--out` bên trong gốc đó.

Mục **`review-gallery` trong `.claude/launch.json` đang trỏ tới bản ở scratchpad**.
Anh cần đổi đường dẫn script sang `tools/review-gallery/serve.mjs`, giữ đối số
`4330` hoặc dùng `--port 4330`. Codex không sửa `launch.json` trong phiếu này.

Kiểm công cụ, không chạy build/test game:

```sh
python3 -B -m unittest discover -s tools/review-gallery -p test_build.py -v
```

Test dùng thư mục tạm và luôn truyền `--out` khi gọi CLI.
