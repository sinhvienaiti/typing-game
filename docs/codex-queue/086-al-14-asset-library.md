# Phiếu 086 · Thư viện tài sản · AL-14: Trang `catalog.html`

Thiết kế: [`docs/tools/ASSET_LIBRARY.md`](../tools/ASSET_LIBRARY.md). Danh sách phiếu gốc: [`docs/tools/asset-library/TICKETS.md`](../tools/asset-library/TICKETS.md), mục AL-14. Claude đã duyệt tên và loại ở `library/curated/*.jsonl` (AL-12, 28/10): dùng đúng các dòng đó, không đặt lại tên. Phiếu trước trong cùng làn có thể đã tạo file mà phiếu này dùng: đọc chúng, không viết lại.

**Báo cáo:** `docs/codex-queue/086-report.md`.

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

## AL-14 · [codex] Trang `catalog.html`

**Cần trước:** AL-09, AL-13.

**Chỉ được ghi:** `tools/asset-library/page.mjs`, `tools/asset-library/page/*.{html,css,js}` (khung trang), `tools/asset-library/test/page.test.mjs`, `library/out/catalog.html`, `library/out/catalog.data.js`, `package.json` gốc (chỉ thêm `lib:page`; Claude duyệt).

**Việc:** theo thiết kế §5.1:
- HTML nhỏ + `catalog.data.js` (`window.CATALOG = …`) nạp bằng `<script src>`; không fetch, không URL mạng;
- nhúng đúng `lib/search.mjs` (cùng mã, không viết lại);
- menu tiếng Việt, tên món tiếng Anh, tên Việt là chú thích xám;
- bộ lọc theo thứ tự: chữ, loại, kiểu, game, vùng, phong cách, chất lượng, trạng thái, Drive;
- lưới ảnh nhỏ; khung chi tiết (file theo vai trò, md5, Drive, đoạn prompt đọc lúc build từ file trên máy, mét, tam giác, clip, giấy phép, ai dùng, bản sao, món giống, nút nghe từng biến thể);
- nghe: `canPlayType` cho ogg vorbis/opus; không phát được thì đổi thành nút chép `pnpm lib:play <uid>`;
- nút chép lệnh (`navigator.clipboard`, đường lui chọn chữ);
- công tắc hiện bản ẩn; dòng "quét lúc …", đỏ khi quá 24 giờ;
- sáng và tối; dùng được ở 375 px.

**Kiểm (bắt buộc):** K1–K4, và (không cần trình duyệt):
1. Test nạp `catalog.data.js` bằng `node:vm`, đọc được mục lục.
2. Mọi đường dẫn ảnh nhỏ tương đối trỏ tới file có thật.
3. Hàm tìm trong trang (lấy từ file đã sinh) cho cùng 10 kết quả đầu như lệnh, với mọi câu tìm vàng.
4. `grep -cE 'https?://' library/out/catalog.html library/out/catalog.data.js` in 0 cho cả hai.
5. `catalog.html` tối đa 200 KB; hai file cộng lại tối đa 8 MB.

**Xong khi:** năm kiểm đạt. Claude thử bằng mắt ở AL-16.
