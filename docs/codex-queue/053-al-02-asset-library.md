# Phiếu 053 · Thư viện tài sản · AL-02: Từ vựng, từ đồng nghĩa, danh sách quét

Thiết kế: [`docs/tools/ASSET_LIBRARY.md`](../tools/ASSET_LIBRARY.md). Danh sách phiếu gốc: [`docs/tools/asset-library/TICKETS.md`](../tools/asset-library/TICKETS.md), mục AL-02. Đọc thiết kế ở các mục phiếu nhắc tới trước khi làm. Phiếu trước trong cùng làn có thể đã tạo file mà phiếu này dùng: đọc chúng, không viết lại.

**Báo cáo:** `docs/codex-queue/053-report.md`.

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

## AL-02 · [codex] Từ vựng, từ đồng nghĩa, danh sách quét

**Cần trước:** không.

**Chỉ được ghi:** `library/.gitignore`, `library/taxonomy.json`, `library/sources.json`, `library/licences.json`, `tools/asset-library/lib/taxonomy.mjs`, `tools/asset-library/test/taxonomy.test.mjs`.

**Việc:**
- `library/.gitignore`: `out/`, `.thumbs/`, `.cache/`, `browse/`, `browse.new/`, `private/`.
- `taxonomy.json` theo thiết kế §3.6:
  - loại và loại con, mỗi cái có nhãn tiếng Việt cho menu; 16 loại hình/3D, 14 loại âm;
  - ít nhất 120 từ nhãn tiếng Anh, gồm đủ 30 từ của `inferTags` (đọc `tools/map-factory/registry/scan-assets.mjs` dạng chữ);
  - nhóm đồng nghĩa: lấy `SYNONYMS` của `tools/tripo-match/match.mjs`, thêm tiếng Việt có dấu và không dấu; nhóm liên quan;
  - `viTokens`: chữ Việt không dấu → từ Anh, kèm danh sách thư mục được áp (`cau` → bridge chỉ ở `typing-defense:landmarks`; `da` → stone chỉ ở `scenery/`, `landmarks/`);
  - vùng; phong cách theo game; trạng thái; bước làm (`pipeline`);
  - `folderMap` cho mọi thư mục cấp 1 (và cấp 2 khi thư mục tách đôi: `props/pine-river`, `scenery/<vùng>`, `landmarks` từng món) dưới `art-src` và `art-src/3d` của dragon-hold, typing-defense, typing-survival, space-typing, cộng các thư mục âm của Space; cờ `perItem`, `hyphenVariants`;
  - `audioFamilyMap` cho 9 họ AudioLab.
- `sources.json`: gốc quét (4 game × `art-src`, `public`, `src/assets`; `~/AudioLab/libraries`; `~/AudioLab/work` ở chế độ nháp; `shared/music` ở chế độ riêng; handoff ở chế độ chỉ-tìm-bản-sao); danh sách cấm (Tu Tiên, bản chép Tu Tiên trong handoff, `games/monkeytype`); thư mục bỏ qua (`tmp/`, `.wt-*`, `dist/`, `.visual/`, `.media-tmp/`, `node_modules/`, `library/browse/`).
- `licences.json`: `owner-tripo`, `owner-ai-2d`, `cc0-1.0`, `cc-by-4.0`, `stability-community`, `repo-synth`, `unknown`, `private-producer`, `private-valve`, mỗi khóa có `commercialOk`, `attribution`, `aiInputAllowed`, `private`, `notForRelease`.
- `taxonomy.mjs`: `load()`, `resolve(word, {folder})`, `related(a, b)`, `kindFor(game, relPath)`, `styleFor(game)`.

**Kiểm (bắt buộc):** K1–K4, và:
1. Test đi thật (chỉ đọc tên thư mục) các thư mục cấp 1 ở trên; hỏng nếu có thư mục chưa ánh xạ (bỏ qua `_review`, `review-vs*`, `_from-downloads`, `tmp`, thư mục bắt đầu bằng dấu chấm). In danh sách đã đi.
2. Không từ nào thuộc hai nhóm đồng nghĩa.
3. `resolve` của `hut`, `chòi`, `choi`, `lều`, `leu` đều ra `hut`; `resolve('nhà')` ra `house`; `related('hut','house')` là true.
4. `resolve('cau', {folder: 'typing-defense:landmarks'})` ra `bridge`; `resolve('cau')` không thư mục ra `null`.
5. Mọi khóa `CATEGORIES` và `FAMILIES` trong `tools/audio-lab/specs/taxonomy.py` (đọc dạng chữ) có ánh xạ.
6. `taxonomy.json` không quá 60 KB; ghi lại với khóa đã sắp cho đúng từng byte.

**Xong khi:** sáu kiểm đạt.
