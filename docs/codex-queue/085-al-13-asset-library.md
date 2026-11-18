# Phiếu 085 · Thư viện tài sản · AL-13: Ảnh nhỏ và dạng sóng

Thiết kế: [`docs/tools/ASSET_LIBRARY.md`](../tools/ASSET_LIBRARY.md). Danh sách phiếu gốc: [`docs/tools/asset-library/TICKETS.md`](../tools/asset-library/TICKETS.md), mục AL-13. Claude đã duyệt tên và loại ở `library/curated/*.jsonl` (AL-12, 28/10): dùng đúng các dòng đó, không đặt lại tên. Phiếu trước trong cùng làn có thể đã tạo file mà phiếu này dùng: đọc chúng, không viết lại.

**Báo cáo:** `docs/codex-queue/085-report.md`.

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

## AL-13 · [codex] Ảnh nhỏ và dạng sóng

**Cần trước:** AL-12.

**Chỉ được ghi:** `tools/asset-library/thumbs.mjs`, `tools/asset-library/blender/thumb.py`, `tools/asset-library/test/thumbs.test.mjs`, `library/.thumbs/**`.

**Việc:**
- Ảnh: `magick` → `library/.thumbs/<md5>.webp`, cạnh dài 256 px, tối đa 40 KB.
- Thẻ GLB: dùng ảnh nguồn liên kết nếu có. Chỉ GLB không có ảnh nguồn mới render bằng Blender headless (`/Applications/Blender.app/Contents/MacOS/Blender -b -P thumb.py`; camera 3/4 cố định, ánh sáng trung tính, nền trong). Trần 150 lần render mỗi lượt.
- Âm: `ffmpeg showwavespic` → `<sha256>.wave.png`, mỗi bộ một hình từ biến thể đầu.
- Kiểm trước: dưới 20 GiB trống thì dừng, in lý do.
- Không làm lại: khóa theo md5/sha256.

**Kiểm (bắt buộc):** K1–K4, và:
1. Mọi thẻ hiện có ảnh nhỏ; mỗi file tối đa 40 KB; tổng tối đa 150 MB (in hai số).
2. Lượt hai tạo 0 file.
3. Số lần render Blender in ra, tối đa 150.
4. Test giả lập ổ còn ít chỗ → dừng có thông báo, không tạo file.

**Xong khi:** bốn kiểm đạt.
