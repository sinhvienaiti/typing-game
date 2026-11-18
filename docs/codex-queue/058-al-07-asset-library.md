# Phiếu 058 · Thư viện tài sản · AL-07: Đọc bảng tài liệu (doc facts)

Thiết kế: [`docs/tools/ASSET_LIBRARY.md`](../tools/ASSET_LIBRARY.md). Danh sách phiếu gốc: [`docs/tools/asset-library/TICKETS.md`](../tools/asset-library/TICKETS.md), mục AL-07. Đọc thiết kế ở các mục phiếu nhắc tới trước khi làm. Phiếu trước trong cùng làn có thể đã tạo file mà phiếu này dùng: đọc chúng, không viết lại.

**Báo cáo:** `docs/codex-queue/058-report.md`.

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

## AL-07 · [codex] Đọc bảng tài liệu (doc facts)

**Cần trước:** AL-06.

**Chỉ được ghi:** `tools/asset-library/doc-facts.mjs`, `tools/asset-library/scan.mjs` (chỉ bước gộp `doc-facts.json`), `tools/asset-library/test/doc-facts.test.mjs`, `tools/asset-library/test/fixtures/docs/**`, `library/out/doc-facts.json`.

**Cấm thêm:** đọc `docs/games/tu-tien/**`.

**Việc:** đọc bảng Markdown của `docs/games/NAMES_EN.md`, `3D_REQUESTS.md`, `3D_IMPORT_2026-10-26.md`, `3D_IMPORT_2026-10-28.md`, `ART_REPLACE_LATER.md`, `IMAGE_AUDIT_2026-10-25.md` và `typing-game-handoff-2026-10-25/tripo-upload*/INDEX.md`. Ghi theo game+id và theo đường dẫn file: tên Anh, tên Việt, nghĩa, điểm 2D/3D (dấu phẩy thập phân → chấm), mức (Đạt → pass, Tạm chấp nhận → provisional), cần P1–P3, file Tripo, tam giác, face limit, rig, độ tin, bằng chứng `file:dòng`. Tiền tố `rong_`, `loigoi_`, `tuyencuoi_` → game. `scan.mjs` gộp vào thẻ (sau dòng tuyển chọn về độ ưu tiên).

**Kiểm (bắt buộc):** K1–K4, và:
1. Số dòng đọc được mỗi tài liệu (in) bằng `grep -c '^| '` trừ dòng tiêu đề và dòng kẻ. Ít nhất: 3D_IMPORT_2026-10-28 86 dòng, 3D_IMPORT_2026-10-26 55, NAMES_EN khoảng 148.
2. `choi-canh-doi`: điểm 3D 9, pass, file Tripo `thatched+hut+3d+model (2).glb`, 7733 tam giác. `nha-rai-da`: 8,5, provisional. `barracks-kit-l2`: `wooden+hut+3d+model.glb`. `herb-hut`: tên Anh `Herb Hut`, điểm 2D 9,5 (IMAGE_AUDIT H1), file Tripo `fantasy+cottage+3d+model.glb`.
3. Mọi đường dẫn ở cột File và Đích hoặc có trên ổ đĩa, hoặc nằm trong `missing[]` (in danh sách).

**Xong khi:** ba kiểm đạt.
