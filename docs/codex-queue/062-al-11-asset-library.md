# Phiếu 062 · Thư viện tài sản · AL-11: Dòng tuyển chọn mồi

Thiết kế: [`docs/tools/ASSET_LIBRARY.md`](../tools/ASSET_LIBRARY.md). Danh sách phiếu gốc: [`docs/tools/asset-library/TICKETS.md`](../tools/asset-library/TICKETS.md), mục AL-11. Đọc thiết kế ở các mục phiếu nhắc tới trước khi làm. Phiếu trước trong cùng làn có thể đã tạo file mà phiếu này dùng: đọc chúng, không viết lại.

**Báo cáo:** `docs/codex-queue/062-report.md`.

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

## AL-11 · [codex] Dòng tuyển chọn mồi

**Cần trước:** AL-10.

**Chỉ được ghi:** `tools/asset-library/seed-curated.mjs`, `tools/asset-library/test/seed-curated.test.mjs`, `library/curated/dragon-hold.jsonl`, `typing-defense.jsonl`, `typing-survival.jsonl`, `space-typing.jsonl`, `audio-libraries.jsonl`.

**Cấm thêm:** ghi bất kỳ dòng nào cho thẻ `private` hay `notForRelease`; ghi prompt vào dòng.

**Việc:** mỗi thẻ hiện, công khai: một dòng, đã sắp. Trường: `uid`, `md5s`, `name` (NAMES_EN → phần Anh của 3D_IMPORT → dịch mồi, `nameSource: seed-translation`), `aliases` (Việt có và không dấu, chữ trong id, chữ chú thích Tripo), `kind`/`subkind` (folderMap + `perItem`), `tags` (khớp từ vựng trên tên, chú thích, ghi chú 3D_IMPORT), `biome`, `style`, `canonical: {}`, `reuseNotes: null`, `quality: null` (chỗ Claude ghi đè điểm khi tài liệu thiếu), `reviewed: null`. Chỉ thêm dòng mới; không bao giờ ghi đè dòng có `reviewed`.

**Kiểm (bắt buộc):** K1–K4, và:
1. Ít nhất 95 % thẻ hiện có `name` và `kind`; ít nhất 80 % thẻ `model3d` có từ 2 nhãn (in).
2. Chạy lại `pnpm lib:scan` rồi mọi câu trong `library/test/queries.json` đạt.
3. Chạy `seed-curated` lần hai: 0 dòng đổi.
4. Test: dòng có `reviewed` giữ nguyên từng byte.
5. Không `name` nào có dấu tiếng Việt.
6. **Chặn rò:** test đọc `media/private.md5` (nếu có trên máy) và tên file trong `games/space-typing/art-src/Dota-Sounds`; không tên file nào (bỏ đuôi) xuất hiện trong `library/curated/*`, `library/taxonomy.json`, `library/sources.json`. Không có `private.md5` thì bỏ qua, in lý do.
7. Báo cáo liệt kê 50 tên độ tin thấp nhất để Claude duyệt.

**Xong khi:** bảy kiểm đạt.
