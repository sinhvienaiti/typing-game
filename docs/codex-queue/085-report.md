# Phiếu 085 · AL-13: Ảnh nhỏ và dạng sóng

Ngày làm: 28/10/2026, tại repo cha trên Mac mini M4.

**Chưa đóng AL-13:** đã có ảnh cho **3.613/3.622 thẻ hiện**. Còn 9 thẻ GLB cần Blender; bản Blender trên máy thoát `SIGSEGV` ngay khi khởi động headless. Giới hạn dung lượng, lượt chạy lại, trần render và dừng khi thiếu chỗ đều đã kiểm đạt. Claude cần chạy lại phần Blender để đủ điều kiện «mọi thẻ hiện có ảnh nhỏ».

## File tạo

- `tools/asset-library/thumbs.mjs`: đọc hai mục lục hiện có và các dòng curated AL-12; giữ nguyên tên, loại, loại con và lựa chọn canonical. Sinh WebP bằng ImageMagick; dạng sóng bằng `ffmpeg showwavespic` từ biến thể đầu. Dùng md5/sha256 làm tên cache; không tải hay sửa nguồn.
- `tools/asset-library/blender/thumb.py`: import GLB, camera trực giao góc 3/4 cố định, ánh sáng trung tính, Cycles CPU, 256 × 256, nền trong. Node chuyển kết quả thành WebP. Chỉ dùng cho GLB không có ảnh nguồn liên kết; tối đa 150 lần render/lượt.
- `tools/asset-library/test/thumbs.test.mjs`: 13 ca, gồm hàng rào ghi `fs`, dữ liệu mẫu dưới `os.tmpdir()`, công cụ thật cho hình/âm, và kiểm Blender có điều kiện.
- `library/.thumbs/<md5>.webp`: **1.748 file**.
- `library/.thumbs/<sha256>.wave.png`: **1.788 file**, phục vụ đủ **1.849 thẻ âm/nhạc**; các hash trùng dùng chung file.
- `library/.thumbs/index.json` và `library/.thumbs/index-<sha256>.json`: **35 file metadata**, nối 3.613 uid với ảnh. Chia phần để cả metadata cũng tối đa 40.000 byte/file.
- `docs/codex-queue/085-report.md`: báo cáo này.

Không sửa `library/curated`, `library/out`, `package.json`, nguồn hình/âm/model hay mã game. Không tạo hình minh họa hoặc âm thanh mới.

## Kết quả kiểm

| Kiểm | Số đo và kết quả |
|---|---|
| K1 · Phạm vi ghi của công cụ | Test bọc các API ghi, kể cả `open` có cờ ghi, rename, copy, symlink và xóa; chỉ cho ghi `.thumbs` trong cây tạm do test tạo. Đạt. Lượt chạy lại trên kho thật cũng dùng lớp bọc: **0 lần ghi**. Có tác dụng phụ của lệnh thăm dò môi trường ban đầu, ghi rõ bên dưới. |
| K2 · Git | So với đầu, chỉ thêm ba file mã/test và báo cáo trong danh sách được phép. `.thumbs` đã nằm trong ignore có sẵn. Trạng thái `games/` đầu/cuối giống nhau. |
| K3 · Chặn đường cấm | Lệnh grep bắt buộc bên dưới: **0 dòng**, mã thoát 1 theo quy ước grep khi không khớp. Không đọc cây game bị cấm. |
| K4 · Test | `node --test tools/asset-library/test/thumbs.test.mjs`: **13 ca; 12 đạt; 0 lỗi; 1 bỏ qua** vì Blender lỗi khởi động; mã thoát 0. |
| 1 · Mọi thẻ và dung lượng | **3.613/3.622** thẻ có ảnh: hình/3D **1.764/1.773**, âm/nhạc **1.849/1.849**. Phần bao phủ chưa đạt vì 9 GLB. Tất cả **3.571 file**, kể cả metadata: lớn nhất **40.000 byte**, tổng **44.430.658 byte**, dưới 150.000.000 byte. Riêng 3.536 file ảnh/dạng sóng: lớn nhất **39.962 byte**, tổng **43.101.673 byte**. |
| 1 · Kích thước, đường dẫn, curated | Dùng `magick identify` trên toàn bộ 3.536 file: **0 sai kích thước**; WebP có cạnh dài 256 px, dạng sóng 256 × 96. **0 đường dẫn ảnh bị thiếu**, **0 sai khác tên/loại/loại con** giữa bảng nối và các thẻ đã áp curated. |
| 2 · Lượt hai | Trên kho thật sau khi ổn định đầu ra: **tạo 0 file ảnh**, dùng lại **3.613**, **0 lần ghi fs**, bảng nối giữ nguyên. Đạt. |
| 3 · Blender | Kho thật: **0/150 lần render**, thăm dò khởi động thất bại một lần mỗi lượt rồi bỏ qua. Test giả lập 151 GLB khác hash: đúng **150 lần render**, GLB thứ 151 bị chặn; thêm thẻ trùng hash không tăng render. Phần giới hạn đạt; phần hình Blender thật chưa xác nhận. |
| 4 · Thiếu dung lượng | Giả lập **20 GiB − 1 byte**: thông báo dừng, **0 file tạo**, **0 API ghi**, **0 subprocess**, không đọc nguồn. Có thêm ca dung lượng giảm giữa lượt: không tạo ảnh kế tiếp hoặc bảng nối. Đạt. |

```sh
grep -rlE 'immortality-cultivation|tu-tien' library/out library/.thumbs
```

Lần test cuối với ImageMagick/ffmpeg thật trên mẫu tạm: 2/2 thẻ, file lớn nhất 29.456 byte, tổng cả metadata 30.052 byte; lượt hai 0 file mới. Dữ liệu mẫu được test tự dọn trong thư mục tạm của chính nó. Cú pháp `thumb.py` cũng được kiểm bằng `ast.parse`, không tạo `__pycache__`. Không chạy build hoặc bộ test game.

## Phần bỏ qua và việc cần xem

Blender có tại `/Applications/Blender.app/Contents/MacOS/Blender` nhưng thoát `SIGSEGV` trước khi chạy Python, với thông báo:

```text
ArchWarn: ARCH_CACHE_LINE_SIZE != Arch_ObtainCacheLineSize()
Function: Arch_ValidateAssumptions
```

Ca Blender thật được đánh dấu bỏ qua với lý do này. Không dựng ảnh giả cho chín thẻ sau:

```text
dragon-hold:public/assets/dragon-hold/models/guides/draconis-v4/draconis-v4
dragon-hold:public/assets/dragon-hold/models/heroes/draconis-v2/draconis-v2
dragon-hold:public/assets/dragon-hold/models/heroes/draconis-v3/draconis-v3
space-typing:bosses/auriel-hero
space-typing:guides/draconis-v4
space-typing:heroes/draconis
space-typing:heroes/draconis-v2
space-typing:heroes/draconis-v3
space-typing:skills/dragon-fireball
```

Sau khi Blender chạy được, Claude chạy lại:

```sh
ART_MAGICK=/opt/homebrew/bin/magick node tools/asset-library/thumbs.mjs
node --test tools/asset-library/test/thumbs.test.mjs
```

Công cụ trả mã 1 khi còn thiếu ảnh, tránh báo hoàn tất sai. Các ảnh đã có được tái dùng. Phiếu AL-14 có thể dùng `loadThumbIndex()` xuất từ `thumbs.mjs` để đọc đủ các phần metadata; `thumb` là đường dẫn từ gốc repo, trang trong `library/out/` đổi thành `../.thumbs/<tên file>`. Không cần sửa hay quét lại mục lục để đọc bảng nối này.

**Tác dụng phụ cần ghi nhận:** lần thăm dò Blender trực tiếp đầu tiên, trước khi viết công cụ, Blender tự ghi `blender.crash.txt` ở thư mục tạm macOS `/var/folders/d7/2x1km_3s363175h285_zlz680000gn/T/`. Đây là file chẩn đoán ngoài danh sách được ghi của phiếu; không xóa hoặc sửa vì luật chỉ cho dọn thư mục tạm do test tự tạo. Các lần gọi Blender trong công cụ và test đã thêm `--disable-crash-handler --disable-abort-handler`.

## K2 · Trạng thái Git

`git status --porcelain` lúc đầu:

```text
 M games/typing-survival
?? .claude/launch.json
?? TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md
?? docs/codex-queue/035-report.md
?? docs/codex-queue/036-report.md
?? docs/codex-queue/066-report.md
?? docs/codex-queue/068-report.md
?? docs/codex-queue/069-report.md
?? docs/codex-queue/070-report.md
?? docs/tools/map-factory/spike-l2-cau.md
?? shared/shared
```

`git status --porcelain` lúc cuối:

```text
 M games/typing-survival
?? .claude/launch.json
?? TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md
?? docs/codex-queue/035-report.md
?? docs/codex-queue/036-report.md
?? docs/codex-queue/066-report.md
?? docs/codex-queue/068-report.md
?? docs/codex-queue/069-report.md
?? docs/codex-queue/070-report.md
?? docs/codex-queue/085-report.md
?? docs/tools/map-factory/spike-l2-cau.md
?? shared/shared
?? tools/asset-library/blender/
?? tools/asset-library/test/thumbs.test.mjs
?? tools/asset-library/thumbs.mjs
```

`git status --porcelain games/` lúc đầu:

```text
 M games/typing-survival
```

`git status --porcelain games/` lúc cuối:

```text
 M games/typing-survival
```

Dòng game này có từ trước, không do công cụ của phiếu. Các dòng ngoài phạm vi còn lại cũng có nguyên từ đầu. Không dùng lệnh Git có ghi.

## Claude duyệt (28/10/2026)

**Kết luận: nhận, kèm sửa. AL-13 đóng: 3.622/3.622 thẻ hiện có ảnh nhỏ.**

Blender 5.2.2 trên máy chạy headless bình thường; lỗi `SIGSEGV` chỉ xảy ra trong sandbox của Codex. Chạy thật lần đầu bằng mã của Codex: 3.622/3.622 thẻ, tạo 6 ảnh, Blender 6/150 (9 thẻ dùng chung 6 md5), mất 11,5 giây. Claude xem 24 ảnh mẫu: 6 bản render GLB; 12 hình gồm sinh vật, nhà, nhân vật, tàu, vật phẩm, VFX, nền và 2 thẻ GLB dùng ảnh nguồn; 6 dạng sóng. Claude cũng xem đủ 62 ảnh SVG và 13 chuỗi VFX động.

### Lỗi tìm thấy và đã sửa

1. **Render GLB đặt khung quá rộng.** Khung tính theo bán kính hộp bao × 2,3, nên vật chỉ chiếm 82–153 trên 256 px. `thumb.py` giờ khớp khung theo hình chiếu thật của các đỉnh (sau modifier) và chừa 5% mỗi bên; vật chiếm 233/256 px. Test Blender thật kiểm thêm điều kiện vật ≥ 200 px.
2. **Quả cầu lửa ra đốm trắng.** `emissiveFactor` (1,1,1) × 3 không có texture phủ trắng cả màu vẽ. Ảnh xem trước giờ bỏ phát sáng hằng; phát sáng có texture giữ nguyên. Trong game, model này dùng shader riêng.
3. **Dạng sóng phẳng.** 247/1.788 file (14%) chỉ cao ≤ 10/96 px, thêm 498 file cao 11–24 px. Nguyên nhân: các lớp velocity mềm VSCO2 có đỉnh −30…−40 dB, lại vẽ bằng `filter=average`. Giờ công cụ đo đỉnh bằng `astats`, đưa về −1 dBFS (khuếch đại tối đa +40 dB) rồi vẽ bằng `filter=peak`. Sau sửa: 0 file cao ≤ 24 px.
4. **Chuỗi VFX động lấy khung 0 gần trống.** 8/13 chuỗi combat-vfx chỉ ra một chấm nhỏ; `missile-salvo.webp` trong suốt hoàn toàn. WebP và GIF nhiều khung giờ lấy khung giữa sau `-coalesce`. Test thật có thêm ca khung 0 trong suốt.
5. **Phần index mồ côi.** File `index-<sha256>.json` đặt tên theo nội dung. Ở lượt 1, 34 phần mới được thêm mà 34 phần cũ vẫn nằm lại, nên mỗi lần bảng nối đổi cache phình thêm khoảng 1,3 MB. Giờ sau khi ghi `index.json`, công cụ xóa các phần `index-*.json` không còn được trỏ tới. Test có thêm ca này.

Để sinh lại, Claude đã chuyển 1.788 dạng sóng, 6 bản render và 13 ảnh động cũ ra thư mục tạm của phiên. Ảnh nhỏ khóa theo md5/sha256 của nguồn, không theo phiên bản bộ vẽ, nên mỗi lần đổi bộ vẽ phải xóa tay các file liên quan.

### Kết quả sau sửa

| Kiểm | Số đo |
|---|---|
| K4 | `thumbs.test.mjs`: **13/13 đạt, 0 bỏ qua** (ca Blender thật chạy). Cả bộ asset-library có 116 ca: 110 đạt, 6 lỗi. Trong đó 5 ca scan lỗi vì đường cache (chờ phiếu 084). Ca còn lại là search «p95 lạnh» (358 ms > 300 ms), một test đo thời gian chỉ lỗi khi cả bộ chạy song song; chạy riêng thì đạt 20/20. |
| 1 · Phủ, dung lượng | **3.622/3.622** thẻ hiện. Có 3.577 file (1.754 WebP, 1.788 dạng sóng, 34 phần index và `index.json`), file lớn nhất **39.994 byte**, tổng **44.791.161 byte**. |
| 1 · Kích thước | Đo cả 3.542 ảnh bằng `magick identify`: **0 file sai** (WebP có cạnh dài 256 px, dạng sóng 256 × 96). |
| 2 · Lượt hai | Tạo **0** file, dùng lại 3.622, Blender 0/150; danh sách file không đổi. |
| 3 · Blender | **6/150** lần render. |
| 4 · Thiếu chỗ | Test giả lập «20 GiB − 1 byte» đạt. |
| K2 | `git status --porcelain games/` chỉ có ` M games/typing-survival`, dòng này đã có từ trước. |
| K3 | `grep -rlE 'immortality-cultivation\|tu-tien' library/out library/.thumbs`: **0 dòng** (mã thoát 1). |

### Còn lại (chưa sửa)

- **62 ảnh SVG sai.** ImageMagick trên máy không có librsvg, nên bộ vẽ MSVG bỏ gradient (vẽ thành đen) và biến nền trong suốt thành trắng. 9 file chỉ còn một màu: 7 file `sky.svg` đen hoàn toàn, 2 tên lửa trắng hoàn toàn. Cách sửa: có `rsvg-convert` (cài librsvg qua brew, việc này chủ dự án quyết), sau đó xóa 62 ảnh SVG khỏi cache rồi chạy lại.
- Nhiều ảnh concept có sẵn nền chroma (xanh lá hoặc hồng) trong nguồn, và ảnh nhỏ giữ đúng như nguồn. Nếu trang AL-14 cần nền trong suốt, việc tách nền cần một phiếu riêng.
- 2 thẻ không có kind: `space-typing:src/assets/expansion-v2/icons/relic-first-light-seed` và bản `@2x`. Chúng thiếu dòng curated AL-12.
