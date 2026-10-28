# Phiếu 059 · Thư viện tài sản · AL-08: Quét âm thanh

Thiết kế: [`docs/tools/ASSET_LIBRARY.md`](../tools/ASSET_LIBRARY.md). Danh sách phiếu gốc: [`docs/tools/asset-library/TICKETS.md`](../tools/asset-library/TICKETS.md), mục AL-08. Đọc thiết kế ở các mục phiếu nhắc tới trước khi làm. Phiếu trước trong cùng làn có thể đã tạo file mà phiếu này dùng: đọc chúng, không viết lại.

**Báo cáo:** `docs/codex-queue/059-report.md`.

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

## AL-08 · [codex] Quét âm thanh

**Cần trước:** AL-04, AL-07.

**Chỉ được ghi:** `tools/asset-library/scan-audio.mjs`, `tools/asset-library/scan.mjs` (chỉ bước gọi `scan-audio`), `tools/asset-library/test/scan-audio.test.mjs`, `tools/asset-library/test/fixtures/audio-scan/**`, `library/out/**`.

**Việc:**
- Âm Space: `public/assets/audio/**`, `src/assets/audio/**`, chỉ đọc. Đọc bảng trong `public/assets/audio/ATTRIBUTION.md` (Kenney, Freesound có số, tác giả, URL).
- `~/AudioLab/libraries/index.json` và `SOURCES.jsonl`: dùng sha256 sẵn trong index, không băm lại 1.859 file; `onDrive: external`. Thư viện ngoài là file chính, file Space trùng sha256 là bản sao.
- `~/AudioLab/work`: chỉ các lượt có `manifest.fragment.json` và `SOURCES.json`; trạng thái `draft`, ẩn mặc định.
- Riêng tư: `shared/music` (qua `media/private.md5` + bộ đọc đầu file) và `games/space-typing/art-src/Dota-Sounds` (`notForRelease`). Chỉ ghi vào `library/out`.
- Họ âm qua `audioFamilyMap`; gom biến thể số thành một thẻ.
- `usedBy` từ mã trong `games/*/src`: chuỗi đường dẫn âm, và thư mục của `import.meta.glob` (độ tin `folder`).

**Kiểm (bắt buộc):** K1–K4, và:
1. Đủ 116 file âm Space nằm trong thẻ.
2. Đúng 29 file Space trùng sha256 với một file Kenney; `src/assets/audio/ui/click.ogg` là bản sao trên `kenney:interface-sounds/Audio/click`, biến thể 002.
3. Báo hai cặp trùng byte: `confirm.ogg` (hai nơi) và `sfx/kenney/force-field.ogg` = `ui/deploy.ogg`.
4. 15 file Dota có `private` và `notForRelease`; 193 bài nhạc có `private`.
5. 0 thẻ AudioLab `work/` hiện khi không có `--all`.
6. `usedBy` của thẻ click chứa `games/space-typing/src/audio/Sfx.ts:36` (glob) và `:672`.

**Xong khi:** sáu kiểm đạt.
