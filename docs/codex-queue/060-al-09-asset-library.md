# Phiếu 060 · Thư viện tài sản · AL-09: Lõi tìm kiếm và câu tìm vàng

Thiết kế: [`docs/tools/ASSET_LIBRARY.md`](../tools/ASSET_LIBRARY.md). Danh sách phiếu gốc: [`docs/tools/asset-library/TICKETS.md`](../tools/asset-library/TICKETS.md), mục AL-09. Đọc thiết kế ở các mục phiếu nhắc tới trước khi làm. Phiếu trước trong cùng làn có thể đã tạo file mà phiếu này dùng: đọc chúng, không viết lại.

**Báo cáo:** `docs/codex-queue/060-report.md`.

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

## AL-09 · [codex] Lõi tìm kiếm và câu tìm vàng

**Cần trước:** AL-08.

**Chỉ được ghi:** `tools/asset-library/lib/search.mjs`, `tools/asset-library/test/search.test.mjs`, `tools/asset-library/test/fixtures/catalog-small.json`, `library/test/queries.json`.

**Việc:** theo thiết kế §5.6:
- chuẩn hóa (chữ thường; bỏ dấu, đ → d; tách `- _ + . /`, khoảng trắng, camelCase; bỏ từ dừng `STOP` của tripo-match);
- mở rộng đồng nghĩa hai chiều; từ liên quan nửa điểm; `viTokens` theo thư mục;
- trọng số (tên 5, alias 4, loại con 3, loại 3, nhãn 2, đường dẫn/chú thích 1); cộng trừ (shipped/pass +1, runtime +0,5, provisional −0,5);
- lọc trạng thái ẩn trừ khi `all`; `requested` chỉ khi `requested`;
- bộ lọc như thiết kế §5.2.
Mã phải chạy được cả trong Node lẫn khi nhúng vào trang (không `import` Node, không `fs`).

`library/test/queries.json`: mỗi câu có `query`, `filters`, `mustInclude[]`, `topN`.

**Kiểm (bắt buộc):** K1–K4, và trên mục lục thật:
1. `hut --type 3d`: 6 kết quả đầu có `herb-hut`, `choi-canh-doi`, `nha-rai-da`, `barracks-kit-l2`.
2. `chòi` và `choi` ra cùng tập.
3. `jetty --type 3d`: `typing-defense:landmarks/cau-tau` trong 3 đầu.
4. `bridge`: `landmarks/cau-go` và `props/pine-river/bridge-old` trong 5 đầu.
5. `rock --biome pine-forest`: có `rock-boulder`, `rock-slab`, `river-stones`.
6. `wood click --type audio`: `kenney:impact-sounds/Audio/impactWood_light` trong 3 đầu.
7. Bản loại không hiện khi không có `all`.
8. p95 dưới 300 ms trên mục lục thật (in).

**Xong khi:** tám kiểm đạt.
