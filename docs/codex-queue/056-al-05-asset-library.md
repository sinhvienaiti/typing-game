# Phiếu 056 · Thư viện tài sản · AL-05: Quét lõi 2D và 3D

Thiết kế: [`docs/tools/ASSET_LIBRARY.md`](../tools/ASSET_LIBRARY.md). Danh sách phiếu gốc: [`docs/tools/asset-library/TICKETS.md`](../tools/asset-library/TICKETS.md), mục AL-05. Đọc thiết kế ở các mục phiếu nhắc tới trước khi làm. Phiếu trước trong cùng làn có thể đã tạo file mà phiếu này dùng: đọc chúng, không viết lại.

**Báo cáo:** `docs/codex-queue/056-report.md`.

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

## AL-05 · [codex] Quét lõi 2D và 3D

**Cần trước:** AL-02, AL-03.

**Chỉ được ghi:** `tools/asset-library/scan.mjs`, `tools/asset-library/lib/hash-cache.mjs`, `tools/asset-library/test/scan-core.test.mjs`, `tools/asset-library/test/fixtures/scan/**` (PNG và GLB nhỏ do test tự sinh), `library/out/catalog.json`, `library/out/scan-report.md`, `library/.cache/hash.json`.

**Cấm thêm:** sửa `tools/map-factory/**` (chỉ `import` các hàm xuất ra).

**Việc:**
- Đi các gốc trong `library/sources.json` (chỉ 4 game, phần ảnh và GLB); tôn trọng danh sách cấm và thư mục bỏ qua; không đi theo symlink thư mục.
- Băm md5 + sha256 qua `hash-cache.mjs`: mồi chỉ đọc từ `.cache/media-hash.json` khi cỡ và mtime khớp; chỉ băm file mới; lưu ở `library/.cache/hash.json`.
- Ảnh: `imageHeader` (rộng, cao, alpha). GLB: lấy số đo từ `tools/map-factory/registry/out/assets.<game>.json` khi md5 khớp, ngược lại `inspectGlb`.
- Gom thẻ bằng `grammar.mjs` + luật gương; loại từ `kindFor`; phong cách từ `styleFor`.
- Ghi `catalog.json` (`schema: asset-library/1`, `scannedAt`, thẻ đã sắp theo uid) và `scan-report.md` (số thẻ, số file theo vai trò, `unknown`, cảnh báo).
- File biến mất giữa lúc đi (ENOENT) thành cảnh báo. Cờ `--game <id>` và `--scan-date <iso>` (cho test).

**Kiểm (bắt buộc):** K1–K4, và:
1. Test cây mẫu đã `chmod -R a-w`: quét đạt.
2. Hai lần chạy với cùng `--scan-date` cho `catalog.json` giống từng byte.
3. Test xóa một file mẫu giữa lúc đi (qua móc test): kết thúc bằng cảnh báo, mã thoát 0.
4. Chạy thật: in số `glb-original` theo game, cạnh `find games/<g>/art-src/3d -name '*.glb' | wc -l` (dragon-hold, typing-defense, space-typing). Hai số bằng nhau.
5. Không đường dẫn nào trong `catalog.json` chứa `immortality-cultivation` hay `tu-tien`.
6. Lần chạy thứ hai (ấm) dưới 60 giây; in thời gian.

**Xong khi:** sáu kiểm đạt.
