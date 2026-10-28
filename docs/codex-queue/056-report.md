# Phiếu 056 · AL-05 · Quét lõi 2D và 3D

Ngày làm: 28/10/2026. Làm tại repo cha trên macOS, Node v24.22.0. Đã đọc thiết kế §3.1–3.6, §4.1–4.2, §7; phiếu AL-02, AL-03, AL-05 và ranh giới AL-06; mã và báo cáo của các phiếu trước. Sáu kiểm nghiệm thu riêng của AL-05 đều đạt. Có hai giới hạn dữ liệu cần xem ở cuối báo cáo.

## File tạo

- `tools/asset-library/scan.mjs`: quét các gốc `art-src`, `public`, `src/assets` của đúng bốn game trong `sources.json`; chặn danh sách cấm/bỏ qua trước khi đi; không theo symlink thư mục, file hoặc tổ tiên. Dùng lại `groupFiles`, `kindFor`, `styleFor`, `imageHeader`, `inspectGlb`. Có `--game <id>`, `--scan-date <iso>`; API `scan({repoRoot, io, hooks})` dành cho test và phần nối sổ kế tiếp.
- `tools/asset-library/lib/hash-cache.mjs`: md5 và sha256 theo cỡ + mtime; cache media chỉ làm mồi đọc. Cache riêng lưu thêm kết quả header/số đo để lượt ấm không mở lại media. File đổi trong lúc đọc bị bỏ qua với cảnh báo; ENOENT không làm hỏng lượt quét.
- `tools/asset-library/test/scan-core.test.mjs`: 8 test; PNG hợp lệ và GLB nhỏ được sinh trực tiếp trong cây tạm dưới `os.tmpdir()`. Không cần fixture media trong repo.
- `library/out/catalog.json`: `schema: asset-library/1`, `scannedAt`, `cards` sắp theo uid; file trong mỗi thẻ có vai trò, đường dẫn, md5, sha256, số byte, thông tin ảnh/GLB. Có danh sách cảnh báo đã sắp, bỏ dòng trùng.
- `library/out/scan-report.md`: số thẻ, file theo vai trò, danh sách unknown, GLB gốc theo game, thống kê cache và cảnh báo.
- `library/.cache/hash.json`: cache riêng của thư viện, chỉ chứa đường dẫn thuộc bốn game được phép.
- `docs/codex-queue/056-report.md`: báo cáo này.

Không sửa file đã có từ AL-02/AL-03 hoặc `tools/map-factory/**`. Phần nối ở đây chỉ dùng `SOURCES.json.image` để xử lý ngoại lệ của luật gương; preset, manifest, lock, bản sao và tuyển chọn dành cho AL-06.

## Kết quả quét thật

Sản phẩm cuối ghi `scannedAt: 2026-10-28T06:00:48.402Z` (13:00:48 giờ Việt Nam).

| Game | Thẻ | File | glb-original | unknown |
|---|---:|---:|---:|---:|
| dragon-hold | 475 | 1.616 | 24 | 7 |
| typing-defense | 812 | 1.539 | 157 | 12 |
| typing-survival | 11 | 26 | 0 | 0 |
| space-typing | 1.873 | 2.827 | 205 | 334 |
| Tổng | **3.171** | **6.008** | **386** | **353** |

Lượt đầu chưa có cache thư viện: **7,979 giây**; mồi media **4.771** file; băm mới **1.237** file / **189.179.157 byte**; dùng sổ GLB **800** lần; đọc GLB **515** lần. Không có GLB nào thiếu số đo do lỗi đọc.

Sau khi bổ sung cảnh báo unknown vượt ngưỡng, hai lượt xác nhận cuối mất **1,719383042** và **1,682989458 giây**. Lượt sau trúng cache **6.008** file, băm **0** file / **0** byte, đọc GLB **0** lần. Dùng sổ GLB **800** lần.

Catalog cuối: **5.798.971 byte**, sha256 `489b47c92ce0361977ee2bca71ce1d8ba875cd0c03ac57cb5a4d324428cc7799`.

## Các kiểm bắt buộc

| Kiểm | Kết quả và số đo |
|---|---|
| K1 · Đúng vùng ghi | Đạt. Test bọc `fs` toàn cục, cả lúc import Map Factory: **5 lời gọi ghi**, gồm đúng **3 writeFile + 2 mkdir** được phép. Test khác quét cây nguồn đã chmod a-w: **7 thẻ / 13 file**, đạt. Hai lượt quét thật cũng qua lớp bọc I/O: **10 lời gọi ghi**, đúng ba sản phẩm mỗi lượt. |
| K2 · Cây Git | Đạt trong phạm vi thao tác phiếu. Chỉ tạo các file liệt kê ở trên; không sửa nguồn hoặc game. Hai ảnh trạng thái đầy đủ và hai ảnh `games/` ở dưới. |
| K3 · Vùng cấm | Đạt. `grep -rlE` hai mẫu cấm theo phiếu trên `library/out` in **0 đường dẫn**. `library/.thumbs` chưa tồn tại, phiếu không tạo thư mục này. Test thêm deny, ignore, symlink thư mục/file/tổ tiên và gốc cấu hình không hợp lệ: **0 lần đọc** vùng bị chặn; cả ba file ra không rò vùng cấm. |
| K4 · Test phiếu | `node --test tools/asset-library/test/scan-core.test.mjs`: **8 đạt / 0 hỏng / 0 bỏ qua**, khoảng **292 ms** ở lượt cuối. |
| 1 · Cây mẫu chmod a-w | Đạt; **7 thẻ / 13 file**, ghi đúng ba sản phẩm ngoài cây nguồn. |
| 2 · Cùng ngày quét, giống từng byte | Đạt trên mẫu: **10.637 byte**. Đạt trên cây thật ở hai lượt xác nhận cuối: **5.798.971 byte**, cùng sha256 ở trên. |
| 3 · File biến mất | Đạt. Móc `beforeFile` xóa **1 file** mẫu sau khi liệt kê, trước lúc đọc. Có cảnh báo ENOENT, file không vào catalog; tiến trình gọi CLI kết thúc **mã 0**. |
| 4 · Đối chiếu GLB thật | Đạt cả **3/3** game, bảng dưới. |
| 5 · Đường dẫn không thuộc vùng cấm | Đạt; **0 đường dẫn** trong catalog chứa hai mẫu cấm. |
| 6 · Lượt ấm dưới 60 giây | Đạt: **1,682989458 giây**, băm mới **0**, đọc GLB **0**. |

Đối chiếu trực tiếp với `find games/<g>/art-src/3d -name '*.glb' | wc -l`:

| Game | Catalog glb-original | find | Khớp |
|---|---:|---:|---|
| dragon-hold | 24 | 24 | Có |
| typing-defense | 157 | 157 | Có |
| space-typing | 205 | 205 | Có |

Các ca bổ sung đều đạt:

- Cache media có **1** mục khớp cả cỡ và mtime được dùng làm mồi; mục lệch riêng mtime hoặc riêng cỡ bị từ chối. Sau khi đổi một ảnh, chỉ **1** file được băm lại.
- Cache `.cache/media-hash.json` nguyên byte trước/sau quét thật; sha256 `a7b74ade3453209eb004a64210aa3a20fe656f7ebeb8453cf436c01494c8989f`.
- Sổ Map Factory có md5 khớp được dùng; md5 lệch gọi `inspectGlb` và trả **1 tam giác** của GLB mẫu, không nhận số **9.999** từ sổ sai.
- Luật gương và ngoại lệ `image` của Space gom đúng ảnh `-2d` với GLB; biến thể scenery `-v1/-v2` thành một thẻ với `a/b`. Thông tin alpha được kiểm bằng PNG RGBA, RGB, tRNS, WebP VP8X/VP8L; JPEG và SVG cũng có ca kiểm.
- `--game dragon-hold` chỉ xuất thẻ của game đó; game không hợp lệ, ngày không phải ISO và cờ lạ đều bị từ chối.

## Giới hạn và chỗ chủ dự án cần xem

- Có **353 unknown / 6.008 file = 5,8755%**, vượt ngưỡng **1%** trong thiết kế §3.5. Riêng Space có **334** file, phần lớn là ảnh WebP runtime có hậu tố kích thước như `.1024`, `.2048`, `.1672`; ngữ pháp AL-03 hiện giữ chúng là unknown. Phiếu này xuất nguyên danh sách trong `scan-report.md` và thêm cảnh báo vượt ngưỡng; không tự thay ngữ pháp hoặc giấu file để hạ tỷ lệ. Cần phiếu tiếp theo cho phép sửa `grammar.mjs` nếu áp ngưỡng 1% trên toàn bộ bốn game và runtime.
- Có **1** ảnh AVIF mà `imageHeader` chưa hỗ trợ: `games/space-typing/public/assets/space-typing/backgrounds/heaven/halo-garden-production-v2.avif`. Thẻ vẫn có đường dẫn, băm và số byte; `image` có `w/h/alpha: null`, kèm cảnh báo. Không tự viết bộ đọc AVIF thứ hai hay sửa Map Factory ngoài quyền phiếu.
- Tổng **285 cảnh báo**: **267** `creature-longest-axis-not-Y` và **16** `original-not-found` được giữ từ sổ Map Factory, **1** header AVIF chưa hỗ trợ, **1** cảnh báo unknown vượt ngưỡng. Đây là dữ liệu cần duyệt, không phải lỗi tiến trình quét.

Không bỏ qua kiểm nghiệm thu AL-05 nào. Không cần AudioLab, ffprobe, magick hoặc Blender. Không tạo tài sản hình/âm sáng tác hay prompt; PNG/GLB của test chỉ là dữ liệu nhị phân cực nhỏ do test tự sinh rồi dọn trong thư mục tạm của chính test. Không dùng mạng, trình duyệt, server, lệnh media, Git có ghi, build hoặc test suite của game.

## Ảnh trạng thái Git

`git status --porcelain` lúc đầu:

```text
 M games/typing-survival
?? .claude/launch.json
?? TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md
?? docs/codex-queue/035-report.md
?? docs/codex-queue/036-report.md
?? docs/codex-queue/052-report.md
?? docs/codex-queue/053-report.md
?? docs/codex-queue/054-report.md
?? docs/codex-queue/055-report.md
?? docs/tools/map-factory/
?? library/
?? shared/shared
?? tools/asset-library/
```

`git status --porcelain` lúc cuối:

```text
 M games/typing-survival
?? .claude/launch.json
?? TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md
?? docs/codex-queue/035-report.md
?? docs/codex-queue/036-report.md
?? docs/codex-queue/052-report.md
?? docs/codex-queue/053-report.md
?? docs/codex-queue/054-report.md
?? docs/codex-queue/055-report.md
?? docs/codex-queue/056-report.md
?? docs/tools/map-factory/
?? library/
?? shared/shared
?? tools/asset-library/
```

`git status --porcelain games/` lúc đầu:

```text
 M games/typing-survival
```

`git status --porcelain games/` lúc cuối:

```text
 M games/typing-survival
```

Dòng game đã có từ đầu, thuộc làn khác. Catalog, scan-report và cache nằm trong các thư mục bị Git bỏ qua theo AL-02; hai lệnh status thường không liệt kê từng file ở đó.
