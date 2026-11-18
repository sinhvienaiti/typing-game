# Phiếu 057 · Thư viện tài sản · AL-06: Quét: nối sổ, lock, bản sao, dòng tuyển chọn

Thiết kế: [`docs/tools/ASSET_LIBRARY.md`](../tools/ASSET_LIBRARY.md). Danh sách phiếu gốc: [`docs/tools/asset-library/TICKETS.md`](../tools/asset-library/TICKETS.md), mục AL-06. Đọc thiết kế ở các mục phiếu nhắc tới trước khi làm. Phiếu trước trong cùng làn có thể đã tạo file mà phiếu này dùng: đọc chúng, không viết lại.

**Báo cáo:** `docs/codex-queue/057-report.md`.

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

## AL-06 · [codex] Quét: nối sổ, lock, bản sao, dòng tuyển chọn

**Cần trước:** AL-05.

**Chỉ được ghi:** `tools/asset-library/scan.mjs`, `tools/asset-library/lib/joins.mjs`, `tools/asset-library/test/scan-joins.test.mjs`, `tools/asset-library/test/fixtures/joins/**`, `library/out/**`.

**Việc:**
- Nối: `art-src/3d/SOURCES.json` (`image`, `usedBy`, `downloadedAs`, `notMadeYet`); preset (`scripts/models/presets/*.json`, `games/*/scripts/models/presets/*.json`, trường `source`); mọi `public/assets/<g>/models/**/manifest.json` (gồm `m0b/` của Rồng).
- `onDrive` từ `games/<g>/media.md5`: `yes`, `changed`, `no`. `private` từ `media/private.md5` (đọc trên máy; không chép tên nào ra ngoài `library/out`).
- Bản sao theo md5: handoff ở chế độ chỉ-tìm-bản-sao (không trùng thì thành thẻ nháp `handoff:<path>`); `art-src/models/raw` của Space chỉ là bản sao; `.tryN`/`.vN` trùng md5 với file chính là bản sao `same-folder`, không phải nháp; 6 bản Draconis ở Rồng có `copyOf`.
- `rejectedMd5`, `canonical` mỗi vai trò, `pipeline`, `status` từ vai trò (`shipped` khi manifest runtime có khóa).
- Đọc `library/curated/*.jsonl` nếu có: gắn theo uid, nếu không thấy thì theo `md5s` (ghi `formerUids`); trường tuyển chọn thắng trường tự sinh.
- `--locks-only`: dựng thẻ chỉ từ lock, SOURCES.json, preset, manifest có trong Git (`local: false`).

**Kiểm (bắt buộc):** K1–K4, và:
1. Thẻ `dragon-hold:houses/herb-hut` có 9 file hiện (concept, tripo-source, glb-original, glb-processed, runtime-high, runtime-medium, icon, icon-256, icon-64) và `hiddenFiles` rejected 9, prompt 14, report 2. `onDrive` từng file khớp `grep` dòng tương ứng trong `games/dragon-hold/media.md5` (in cả hai).
2. Thẻ `dragon-hold:props/pine-river/wooden-jetty`: `wooden-jetty.try1.png` là bản sao `same-folder`; `rong_wooden-jetty.png` của dot3 là bản sao `handoff`; `pipeline` là `tripo-requested`.
3. Không thẻ nào có file chính nằm dưới `art-src/models/raw` (in số 0).
4. 6 file Draconis runtime ở Rồng có `copyOf` trỏ `space-typing`.
5. Test: dòng tuyển chọn của một file mẫu bị đổi tên vẫn gắn được theo md5 và có `formerUids`.
6. `--locks-only` trên repo thật cho ít nhất 90 % uid của lượt quét đầy đủ (in hai số).

**Xong khi:** sáu kiểm đạt.
