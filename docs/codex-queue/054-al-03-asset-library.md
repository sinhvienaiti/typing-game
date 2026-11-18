# Phiếu 054 · Thư viện tài sản · AL-03: Ngữ pháp tên file (vai trò, biến thể)

Thiết kế: [`docs/tools/ASSET_LIBRARY.md`](../tools/ASSET_LIBRARY.md). Danh sách phiếu gốc: [`docs/tools/asset-library/TICKETS.md`](../tools/asset-library/TICKETS.md), mục AL-03. Đọc thiết kế ở các mục phiếu nhắc tới trước khi làm. Phiếu trước trong cùng làn có thể đã tạo file mà phiếu này dùng: đọc chúng, không viết lại.

**Báo cáo:** `docs/codex-queue/054-report.md`.

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

## AL-03 · [codex] Ngữ pháp tên file (vai trò, biến thể)

**Cần trước:** không (dùng `taxonomy.json` nếu đã có; nếu chưa, test dùng cờ thư mục giả).

**Chỉ được ghi:** `tools/asset-library/lib/grammar.mjs`, `tools/asset-library/test/grammar.test.mjs`, `tools/asset-library/test/fixtures/grammar/*.txt` (danh sách tên file, không media).

**Việc:** hàm thuần, không I/O:
- `parsePath(relPath, ctx)` → `{stem, role, variant, ticket, size, view, tier}`;
- `groupFiles(paths, ctx)` → thẻ theo stem.
Theo bảng thiết kế §3.5: nháp `.vN`/`.tryN` (dấu chấm); biến thể `-vN` chỉ trong thư mục có `hyphenVariants`; `.rejected-<phiếu>` ở bất kỳ đâu; `.tripo`; multiview `_front/_back/_left`; phái sinh `.alpha/.flat/.padded/.seamless/.trim/.crop/.coal/.fix`; `icons/normalized/*.64|.256`; sidecar `.prompt.txt` gắn vào stem; `tripo-spares` `.alt/.r2/*-old.*/*.raw-download-*` và `.r2-rejected`; bậc `.high/.medium`; biến thể âm `_000`, `_rr1`, `-1`, số cuối (`click1`); hậu tố `-2d` của Space qua liên kết `image`. Vai trò `unknown` cho phần còn lại. (Ca "`.try1` trùng md5 với file chính là bản sao" thuộc AL-06, không thuộc ngữ pháp.)

**Kiểm (bắt buộc):** K1–K4, và:
1. Danh sách thật `find games/dragon-hold/art-src -iname '*herb-hut*'` (32 tên, lưu vào fixture) cho đúng một stem `houses/herb-hut` với: concept 1, tripo-source 1, glb-original 1, glb-processed 1, icon 1, icon-256 1, icon-64 1, rejected 9, prompt 14, report 2.
2. `scenery/meadow/bamboo-clump-v1.v1.png` (Lời Gọi): biến thể a, vai trò draft. `tripo-spares/barracks.r2-rejected.glb`: rejected. Kenney `click_001..005`: một stem `click`, 5 biến thể. `impactWood_light_000..004`: stem `impactWood_light`. VCSL `wood_click_f_rr1`: stem `wood_click_f`.
3. Chạy thử trên danh sách tên của `games/dragon-hold/art-src` và `games/typing-defense/art-src` (chỉ liệt kê tên): số vai trò `unknown` không quá 1 % số file; in và liệt kê.

**Xong khi:** ba kiểm đạt.
