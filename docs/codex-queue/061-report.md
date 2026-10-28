# Phiếu 061 · Thư viện tài sản · AL-10: lib:find, lib:show, lib:play

Ngày 28/10/2026, repo cha trên Mac mini M4. Đã đọc thiết kế §3.3, §4.1–4.2, §5.2, §5.6 và cách dùng lại §6; đọc phiếu AL-09, mã lõi cùng báo cáo 060. Hoàn tất bốn kiểm riêng và K1–K4.

## File tạo hoặc sửa

| Đường dẫn | Thay đổi |
|---|---|
| `tools/asset-library/find.mjs` | Dùng lại lõi AL-09; bảng tám cột, JSON `asset-library/1`, đủ bộ lọc, giới hạn mặc định 20; kiểm thời gian các lock, SOURCES và manifest model lồng. Cảnh báo ra stderr để stdout JSON luôn đọc được. |
| `tools/asset-library/show.mjs` | Giải mã uid đầy đủ/mã ngắn duy nhất; giữ metadata thẻ, bảng file theo vai trò, `--all`, `--json`, lệnh copy bằng uid đầy đủ có quote đối số. Mã ngắn trùng báo cả các uid để chọn. |
| `tools/asset-library/play.mjs` | Chọn âm theo thứ tự biến thể từ 1, gọi afplay bằng mảng đối số; khi lỗi gọi ffmpeg PCM WAV rồi afplay. Chặn đường dẫn thoát cây và symlink nguồn/cache; đọc được đường dẫn AudioLab dạng `~/`. |
| `tools/asset-library/test/cli.test.mjs` | 12 test trên mẫu, cây tạm, chương trình giả và CLI thật; lớp bọc fs kiểm phạm vi ghi. |
| `package.json` | Chỉ thêm đúng 5 script: lib:scan, lib:find, lib:show, lib:play, lib:test. Diff **5 dòng thêm, 0 dòng xóa**, giữ nguyên trạng thái không có newline cuối file. |
| `docs/codex-queue/061-report.md` | Báo cáo này. |

Không sửa lõi AL-09 hay các đầu ra AL-05–AL-08. Hàm dùng chung của CLI nằm trong find.mjs để không tạo helper ngoài phạm vi phiếu.

## Kết quả kiểm

| Kiểm | Kết quả và số đo |
|---|---|
| K1 · Phạm vi ghi | **ĐẠT.** Các hàm CLI nhận lớp bọc fs promises, chặn writeFile, appendFile, mkdir, mkdtemp, rename, copyFile, symlink, link, unlink, rm, rmdir, truncate, chmod, utimes và open có cờ ghi nếu thoát cây tạm do test tạo. **3 lời gọi ghi qua lớp bọc**, đều là mkdir cache trong cây tạm. Chương trình giả ghi log và đúng **1 WAV** dưới cây tạm; đối số ffmpeg được kiểm. Find/show trên catalog thật dùng lớp bọc chỉ đọc, **0 lời gọi ghi**. |
| K2 · Cây Git | **ĐẠT.** So đầu/cuối chỉ thêm 5 file của phiếu và sửa package.json; cả hai bản status games/ giống nhau. Dòng game có sẵn thuộc làn khác; không có công cụ nào ghi vào game. Hai snapshot ở dưới. |
| K3 · Vùng cấm | **Không áp dụng điều kiện sinh file:** phiên này không sinh gì trong library/out hoặc library/.thumbs. Không đọc/ghi vùng game bị cấm, không đọc media/mã nguồn game khác; phép kiểm cũ chỉ lstat lock/SOURCES và đi các thư mục models của bốn game được phép, không đi qua symlink. Danh sách cấm cố định nằm trong mã kiểm đường dẫn. |
| K4 · Test | **ĐẠT.** `node --test tools/asset-library/test/cli.test.mjs`: **12 pass, 0 fail, 0 skip**, exit **0**, **1.108,30 ms**. Kiểm cú pháp cả 4 file mjs đạt; kiểm khoảng trắng và diff package đạt. |
| 1 · JSON và mã ngắn | **ĐẠT.** JSON find giữ schema asset-library/1, scannedAt và nguyên thẻ gốc; kiểm cấu trúc uid/type/files/role/path theo §4.1–4.2. Mẫu hut có **4 thẻ model**; tổ hợp bộ lọc trả **1 Herb Hut**. `dragon-hold:herb-hut` trỏ đúng `dragon-hold:houses/herb-hut`; show mặc định hiện **3 file mẫu**, `--all --json` bằng nguyên thẻ mẫu **5 file**. |
| 2 · Báo cũ | **ĐẠT.** Tạo media.md5, SOURCES.json và manifest `models/m0b/manifest.json` mới hơn scannedAt 10 giây trong cây tạm: **3 dòng cảnh báo**, stdout vẫn parse JSON. Lock cũ hơn 10 giây không báo. Thư mục thiếu và symlink được xử lý an toàn. |
| 3 · Phát thử qua WAV | **ĐẠT.** Chương trình afplay giả thoát **7** với OGG; gọi ffmpeg giả sinh WAV rồi afplay giả thành công: đúng **3 lần gọi**, thứ tự afplay → ffmpeg → afplay. `--variant 2` lấy đúng file thứ hai sau sắp biến thể; đường dẫn có dấu cách giữ nguyên một đối số. Nguồn giữ nguyên byte. Kiểm thêm phát trực tiếp không tạo cache, lỗi decoder/lần phát hai được truyền ra, nguồn thiếu và symlink cache bị chặn. |
| 4 · Hai lệnh thật | **ĐẠT.** `pnpm lib:find hut --type 3d`: exit **0**, **3/3 kết quả**, Herb Hut hạng **2**, **4.400 r**. `pnpm lib:show dragon-hold:herb-hut`: exit **0**, đúng thẻ, **9 file chính**, ẩn **25 file chi tiết**, in đúng lệnh copy đầy đủ. Đã in cả hai đầu ra trong phiên làm việc. |

Thư mục tạm được tạo bằng mkdtemp dưới os.tmpdir(); dọn đúng các cây test này khi test kết thúc. Không tạo cache phát thật. Không chạy mạng, trình duyệt, server, build/test game, media:push/pull hay lệnh Git ghi.

## Đầu ra lệnh find thật

```text
$ node tools/asset-library/find.mjs hut --type 3d
#  uid                                     tên            loại/con        game     tam giác  chất lượng  Drive
1  typing-defense:landmarks/choi-canh-doi  Choi Canh Doi  building/hut    Lời Gọi  7.733     chưa chấm   có
2  dragon-hold:houses/herb-hut             Herb Hut       building        Rồng     4.400 r   đã ship     có
3  typing-defense:landmarks/nha-rai-da     Nha Rai Da     building/house  Lời Gọi  7.289     chưa chấm   có
(3 trên 3; --all hiện thêm bản dự phòng và bản loại, --requested hiện món mới xin)
```

Lệnh show thật in metadata đầy đủ cùng các vai trò: concept, glb-original, glb-processed, icon, icon-256, icon-64, runtime-high, runtime-medium, tripo-source. Kết thúc bằng:

```text
Ẩn 25 file chi tiết; dùng --all để xem.
pnpm lib:copy dragon-hold:houses/herb-hut --to <game>
```

## Phần bỏ qua và việc cần xem

- Không bỏ qua kiểm bắt buộc nào. Không cần ffprobe, magick, Blender hoặc truy cập AudioLab thật; đường dẫn AudioLab được kiểm bằng home giả trong cây tạm. Không nghe âm thật vì kiểm bắt buộc dùng chương trình giả.
- Catalog hiện tại có **2.936 thẻ** hình/3D, scannedAt **2026-10-28T06:17:54.475Z**, chưa gộp dữ kiện tài liệu AL-07 và âm AL-08. Vì vậy lệnh thật chỉ trả 3 hut, tên lấy dự phòng từ uid và chưa có điểm/giấy phép trên Herb Hut. CLI đọc nguyên catalog, không tự ghép hay sửa các đầu ra riêng. Cần Claude quét lại sau khi duyệt; phiên này không được phép ghi library/out.
- Claude cần duyệt diff **5 script** trong package.json. `lib:copy` chỉ là lệnh gợi ý cho phiếu sau, phiên này không tạo hay gọi công cụ copy.
- Khi dùng play ngoài test, chỉ nhánh fallback mới tạo WAV tên UUID dưới library/.cache/play; file cache được giữ lại, không xóa hay đổi tên nguồn. Phiên này chỉ chạy nhánh đó trong cây tạm.

## Git status --porcelain · lúc đầu

```text
 M docs/CODEX_QUEUE.md
 M games/typing-survival
?? .claude/launch.json
?? TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md
?? docs/codex-queue/035-report.md
?? docs/codex-queue/036-report.md
?? docs/codex-queue/066-report.md
?? docs/tools/map-factory/spike-l2-cau.md
?? shared/shared
```

## Git status --porcelain · lúc cuối

```text
 M docs/CODEX_QUEUE.md
 M games/typing-survival
 M package.json
?? .claude/launch.json
?? TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md
?? docs/codex-queue/035-report.md
?? docs/codex-queue/036-report.md
?? docs/codex-queue/061-report.md
?? docs/codex-queue/066-report.md
?? docs/tools/map-factory/spike-l2-cau.md
?? shared/shared
?? tools/asset-library/find.mjs
?? tools/asset-library/play.mjs
?? tools/asset-library/show.mjs
?? tools/asset-library/test/cli.test.mjs
```

## git status --porcelain games/ · lúc đầu

```text
 M games/typing-survival
```

## git status --porcelain games/ · lúc cuối

```text
 M games/typing-survival
```

