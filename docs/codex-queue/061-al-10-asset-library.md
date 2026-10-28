# Phiếu 061 · Thư viện tài sản · AL-10: Lệnh `lib:find`, `lib:show`, `lib:play`

Thiết kế: [`docs/tools/ASSET_LIBRARY.md`](../tools/ASSET_LIBRARY.md). Danh sách phiếu gốc: [`docs/tools/asset-library/TICKETS.md`](../tools/asset-library/TICKETS.md), mục AL-10. Đọc thiết kế ở các mục phiếu nhắc tới trước khi làm. Phiếu trước trong cùng làn có thể đã tạo file mà phiếu này dùng: đọc chúng, không viết lại.

**Báo cáo:** `docs/codex-queue/061-report.md`.

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

## AL-10 · [codex] Lệnh `lib:find`, `lib:show`, `lib:play`

**Cần trước:** AL-09.

**Chỉ được ghi:** `tools/asset-library/find.mjs`, `show.mjs`, `play.mjs`, `tools/asset-library/test/cli.test.mjs`, `package.json` gốc (chỉ thêm `lib:scan`, `lib:find`, `lib:show`, `lib:play`, `lib:test`; Claude duyệt diff này).

**Việc:**
- `find.mjs`: bảng như thiết kế §5.2; `--json`; báo mục lục cũ khi một `games/*/media.md5`, `games/*/art-src/3d/SOURCES.json` hay manifest model mới hơn `scannedAt`.
- `show.mjs`: cả thẻ, bảng file theo vai trò, lệnh `lib:copy` đúng; `--all`, `--json`.
- `play.mjs`: `afplay`; nếu `afplay` thoát lỗi, `ffmpeg` giải mã ra WAV tạm trong `library/.cache/play/` rồi `afplay`. `--variant n`.

**Kiểm (bắt buộc):** K1–K4, và:
1. Test trên mục lục mẫu: `--json` hợp lược đồ; dạng ngắn `dragon-hold:herb-hut` mở đúng thẻ.
2. Test báo cũ: tạo `media.md5` giả mới hơn `scannedAt` trong cây tạm → có dòng cảnh báo.
3. Test `play` với `afplay` giả thoát lỗi → gọi `ffmpeg` giả, rồi `afplay` giả với file WAV.
4. Chạy thật `pnpm lib:find hut --type 3d` và `pnpm lib:show dragon-hold:herb-hut`: in ra, mã thoát 0.

**Xong khi:** bốn kiểm đạt.
