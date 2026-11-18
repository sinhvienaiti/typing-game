# Phiếu 087 · Thư viện tài sản · AL-15: Thư mục Finder và `CATALOG.md`

Thiết kế: [`docs/tools/ASSET_LIBRARY.md`](../tools/ASSET_LIBRARY.md). Danh sách phiếu gốc: [`docs/tools/asset-library/TICKETS.md`](../tools/asset-library/TICKETS.md), mục AL-15. Claude đã duyệt tên và loại ở `library/curated/*.jsonl` (AL-12, 28/10): dùng đúng các dòng đó, không đặt lại tên. Phiếu trước trong cùng làn có thể đã tạo file mà phiếu này dùng: đọc chúng, không viết lại.

**Báo cáo:** `docs/codex-queue/087-report.md`.

## Luật chung (mọi phiếu Codex của thư viện)

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`.
- **Chỉ được ghi:** đúng các đường dẫn phiếu liệt kê, cộng file báo cáo của phiếu.
- **Cấm:**
  - lệnh git có ghi (`add`, `commit`, `checkout`, `stash`, `reset`, `clean`…);
  - mạng, trình duyệt, dev server, server bất kỳ;
  - `pnpm media:push`; `pnpm media:pull` thật (chỉ chạy với rclone giả trong test);
  - xóa, dời, đổi tên, chép file ngoài thư mục tạm do test tự tạo dưới `os.tmpdir()`;
  - ghi bất kỳ gì dưới `games/**`, `shared/music`, `~/AudioLab`, `typing-game-handoff-2026-10-25` (những nơi này chỉ đọc);
  - ghi `.cache/media-hash.json` (chỉ đọc);
  - đọc hay ghi Tu Tiên: `games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`, bản chép Tu Tiên trong handoff;
  - đọc `games/monkeytype` (GPL);
  - thêm gói npm hay pip (chỉ Node có sẵn; Python chỉ khi phiếu ghi rõ).
- **Kiểm chung, bắt buộc ở mọi phiếu:**
  - **K1 · Chỉ ghi chỗ được ghi.** Test của phiếu chạy công cụ với một lớp bọc `fs` (hoặc trên cây mẫu đã `chmod -R a-w`). Mọi lời gọi ghi (`writeFile`, `appendFile`, `mkdir`, `rename`, `copyFile`, `symlink`, `unlink`, `rm`, `open` có cờ ghi) phải nằm dưới thư mục được ghi của phiếu hoặc thư mục tạm của test.
  - **K2 · Cây Git.** `git status --porcelain` lúc cuối, so với lúc đầu, chỉ **thêm hoặc sửa** file trong danh sách được ghi. Dòng khác dưới `games/` (làn khác đang chạy) phải không phải do công cụ: báo cáo ghi cả hai bản `git status --porcelain games/`.
  - **K3 · Tu Tiên.** Nếu phiếu sinh file dưới `library/out` hay `library/.thumbs`: `grep -rlE 'immortality-cultivation|tu-tien' library/out library/.thumbs` không in gì. Chuỗi `immortality-cultivation` chỉ được có trong danh sách cấm của `library/sources.json` và trong mã danh sách cấm.
  - **K4 · Test.** `node --test <file test của phiếu>` đạt.
- **Thiếu quyền đọc `~/AudioLab` hay thiếu `ffprobe`, `magick`, Blender:** test bỏ qua phần đó, in rõ lý do. Claude chạy lại phần thật khi duyệt.
- **Quá một giờ:** dừng ở phần đã xong, ghi phần còn lại vào báo cáo.
- **Báo cáo:** tiếng Việt; danh sách file tạo hay sửa; kết quả từng kiểm, kèm số in ra.

## AL-15 · [codex] Thư mục Finder và `CATALOG.md`

**Cần trước:** AL-12.

**Chỉ được ghi:** `tools/asset-library/browse.mjs`, `tools/asset-library/catalog-md.mjs`, `tools/asset-library/test/browse.test.mjs`, `tools/asset-library/test/catalog-md.test.mjs`, `library/browse/**`, `library/browse.new/**`, `library/CATALOG.md`, `package.json` gốc (chỉ thêm `lib:browse`, `lib:thumbs`, `lib:build`; Claude duyệt).

**Việc:**
- `browse.mjs`: dựng `library/browse.new/<kind>/<subkind>/<Tên Anh> (<game>).<đuôi>` là liên kết tượng trưng tới file `hero` (âm: biến thể đầu); chỉ thẻ hiện, không thẻ riêng tư; xong thì thay `browse/` bằng `browse.new/`. Chỉ được gỡ **liên kết** trong `library/browse*`; gặp file thường thì dừng, mã thoát 2.
- `catalog-md.mjs`: `library/CATALOG.md`, tiêu đề tiếng Việt, một bảng mỗi loại; cột: tên Anh, tên Việt, uid, game làm ra, trạng thái và điểm, ai dùng. Chỉ thẻ công khai có `reviewed`. Không md5, không cỡ, không Drive.
- `lib:build` = scan → thumbs → page → browse → CATALOG.md.

**Kiểm (bắt buộc):** K1–K4, và:
1. Test: một file thường đặt trong `library/browse/` không bị gỡ; công cụ dừng mã 2.
2. Mọi liên kết trỏ tới file có thật; `du -sk library/browse` dưới 2 MB.
3. `CATALOG.md` sinh hai lần giống từng byte; không chứa md5 (không chuỗi 32 hex) và qua chặn rò của AL-11.
4. `library/browse/building/hut/` có Herb Hut và Hilltop Watch Hut (hay tên đã duyệt của chúng).

**Xong khi:** bốn kiểm đạt.


## Bổ sung của Claude (chủ dự án 28/10)

Chủ dự án muốn mở một thư mục là thấy quái theo từng loại, và nhìn tên file là biết đó là con gì. Vì vậy cây `library/browse/` đặt tên như sau:
- **Thư mục cấp 1 và cấp 2:** `<kind> (<labelVi của kind>)/<subkind> (<labelVi của subkind>)/`, lấy `labelVi` từ `library/taxonomy.json`. Ví dụ `creature (quái)/beast (thú)/`. Thẻ không có `subkind` vào `<kind> (…)/_khác/`.
- **Tên liên kết:** `<name> - <aliases[0]> - <nhãn game>.<đuôi>`. `aliases[0]` là tên Việt có dấu mà Claude đã duyệt. Nhãn game: `Rồng`, `Lời Gọi`, `Tuyến Cuối`, `Space`. Ví dụ `Blight Wolf - Sói Mục - Rồng.png`.
  - Nếu `aliases[0]` trùng `name`, bỏ phần đó.
  - Một thẻ có cả ảnh và model thì có hai liên kết: ảnh 2D đẹp nhất (`.png`/`.webp`) và GLB gốc (`… - 3D.glb`).
- Bỏ ký tự cấm trong tên file (`/`, `:`). Tên trùng thì thêm ` (2)`.
- Thêm kiểm: chạy thật trên máy rồi in cây cấp 1–2 kèm số liên kết. Liệt kê 10 tên đầu của `creature (quái)/beast (thú)/`.
