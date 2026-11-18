# Phiếu 231 · Wordwoven · Kiểm lại độc lập 199 và 202

Ngày 30/10/2026, Mac mini M4, macOS. **Hoàn tất kiểm lại chỉ đọc. Không có lỗi P0/P1; hai P2 của 199 là các tồn đọng đã được công bố, được xác nhận lại.** Không sửa mã, ảnh, manifest hoặc golden của hai phiếu. Hai làn oracle được giao model `gpt-6.1-sol`, mức `xhigh`; làn điều phối giữ kiểm định, mốc và tổng hợp.

## 1. Bảng tổng

| Phiếu | Kết luận | P0 | P1 | P2 |
|---|---|---:|---:|---:|
| 199 · atlas cảnh | **Commit được về kỹ thuật**, giữ lượt Claude duyệt ngoại lệ ảnh và đích byte trước commit | 0 | 0 | 2 |
| 202 · bố cục theo seed | **Commit được** trong phạm vi dữ liệu C9 | 0 | 0 | 0 |

Hai P2 bên dưới không phải lỗi mới bị báo cáo cũ bỏ sót. Quyết định 13:28 cho phép xuất q95 còn điểm để Claude chấm; đích byte riêng là đích tối ưu, phiếu 199 yêu cầu ghi vượt và đề xuất. Kết luận này không thay lượt duyệt của Claude hoặc nghiệm thu renderer L3.

## 2. Điều kiện, mốc và bản chép

- `199-report.md` và `202-report.md` có sẵn, đều ghi hoàn tất. Khi bắt đầu chưa có `tmp/codex-231/`, `231/`, `231-report.md`.
- Nhánh **`td-scenery`**, HEAD **`2a1f61d7da2ee6e6ca4abdc23f8775f872d9c9e7`**. `git --no-optional-locks status --short -uall` có đúng **11 đường**: sáu của 199 và năm của 202; **0 đường lạ, 0 đường thiếu**. Tracked diff: `package.json | 1 +`, chỉ thêm `td:scenery`; `git diff --check` exit 0.
- [before.json](231/before.json) lưu lệnh/đầu ra, danh sách đường, SHA-256, byte, mtime và symlink của worktree cùng public checkout chính. [copy.json](231/copy.json): **369 file thường** từ danh sách Git khớp byte; chép bổ sung public theo §“Dựng bản chép” của 224.
- Bản chép ở `games/typing-defense/tmp/codex-231/tree`. `node_modules` là thư mục thật, **11 mục symlink tuyệt đối**, loại `.vite`, `.vite-temp`, `.pnpm-workspace-state-v1.json`. Các liên kết art/public được chuyển thành tuyệt đối trong bản chép để không đứt khi đổi độ sâu. Riêng `scenery/meadow` được chép **nội dung bằng `rsync -aL`**, thành thư mục thật.
- Node **24.22.0**, pnpm **11.21.0**. Mọi lệnh pnpm dùng `pnpm_config_verify_deps_before_run=false`, `TMPDIR` trong codex-231, bỏ `VITE_PORTAL_URL`; ImageMagick dùng `ART_MAGICK=/opt/homebrew/bin/magick`. Không cài hoặc đồng bộ phụ thuộc.
- **359 file được Git theo dõi, 0 media** theo các đuôi ảnh/font/âm thanh/video/model/binary; mọi file thường được theo dõi đều là UTF-8, không có byte NUL; Git repo cha cũng không theo dõi các WebP scenery. **54 file** `src/content`, `src/sim`, `src/typing` và hai golden gameplay khớp byte HEAD ở cả worktree và bản chép. [git-and-hashes.json](231/git-and-hashes.json).

## 3. Số chạy lại cạnh số báo cáo

| Phép kiểm | 199 báo | 202 báo | 231 chạy lại |
|---|---:|---:|---:|
| `pnpm check`: file test | 44 | 44 | **44/44** |
| `pnpm check`: test | 474 | 475 | **475/475**, 0 lỗi, 0 bỏ qua; exit 0 |
| Test riêng `td-scenery-layout.test.ts` | — | 73 | **73/73**, exit 0 |
| Golden cảnh, fixture × seed × bậc | — | 9 | **9/9 khớp**, kể cả oracle tự tính |
| Golden gameplay `same:true` | 2 | 2 | **2/2**, exit 0 |
| `prepare-scenery.mjs --check` | exit 0, 0 ghi | — | **exit 0, 0 file đổi** cả byte/mtime |
| Scenery High | 4.032.026 B | 4.032.026 B | **4.032.026 B** |
| Scenery Medium | 1.332.774 B | 1.332.774 B | **1.332.774 B** |
| Tổng High / trần 16 MB | 15.247.852 B | 15.247.852 B | **15.247.852 B** |
| Tổng Medium / trần 9 MB | 7.253.820 B | 7.253.820 B | **7.253.820 B** |
| Khởi động / trần 3,5 MB | 3.422.868 B | 3.422.868 B | **3.422.868 B** |

Chênh 474 → 475 được giải thích bởi test hợp đồng manifest thêm trong lượt 202 sau mốc báo cáo 199. 231 không thêm test vào nguồn.

`pnpm check` gồm kit **42/42 file khớp**, TypeScript và production build; Vite **142 module**. Thời gian toàn lệnh **12,843 s**; `--check` **0,073 s** (script báo 0,040 s), test riêng **3,722 s**. Gzip `/` **81,58/85 kB**, `/?title=0` **83,04/85 kB**, 3D **171,83/260 kB**, JS tổng **292,75 kB**, khớp báo cáo. Cảnh báo Vite chunk minified >500 kB còn như cũ; ngân sách gzip đạt.

Hai ván giữ `content:f2a21037`, `deck:9c9b91d8`, `changed:{}`, `firstMovedAtTick:null`: thường **19.660 tick / 389 lệnh**, boss **5.695 tick / 49 lệnh**. Đầu ra nguyên văn nằm trong [check.json](231/check.json), [gameplay-golden.json](231/gameplay-golden.json), [prepare-check.json](231/prepare-check.json), [layout-tests.json](231/layout-tests.json); [comparison.json](231/comparison.json) tổng hợp số, [media-budget.json](231/media-budget.json) giữ receipt ngân sách.

## 4. Phiếu 199 · oracle ảnh độc lập

[atlas-audit.json](231/atlas-audit.json) giữ kế hoạch viết trước khi đọc triển khai, nguyên mã `oracleSource`, SHA-256 và cách tái tạo. Không import hoặc dùng helper của 199. Giải mã RGBA8 bằng ImageMagick; tự tính khoảng cách Chebyshev và kiểm chéo bằng tìm kiếm lân cận trực tiếp. Có **28.417 phép đối chiếu khoảng cách, 0 sai khác** trên hai bộ.

Vùng kiểm: **2 px trong vùng alpha ≥128**, và **8/4 px ngoài** ở High/Medium. Khớp khóa theo khoảng cách kênh ≤60 hoặc hue khóa ±20° với S>0,5. Phân loại theo thứ tự: V<0,25 miễn tối; sau đó alpha=0, cách vùng đặc ≥3 px và luma Rec.709<0,2 miễn trong suốt; còn lại bị bắt. Không đếm trùng hai diện miễn.

### Runtime tám sprite

| Sprite | High: còn / miễn tối / miễn alpha 0 riêng | Medium: còn / miễn tối / miễn alpha 0 riêng |
|---|---:|---:|
| almond-tree-v3 | 0 / 1 / 0 | 0 / 0 / 0 |
| almond-tree-v4 | 0 / 0 / 0 | 0 / 0 / 0 |
| bamboo-clump-v3 | 4 / 7 / 0 | 0 / 3 / 0 |
| bamboo-clump-v4 | 3 / 0 / 0 | 0 / 0 / 0 |
| canopy-block-v3 | 3 / 5 / 0 | 0 / 3 / 0 |
| canopy-block-v4 | 0 / 1 / 0 | 0 / 0 / 0 |
| mountain-pine-v3 | 0 / 4 / 0 | 2 / 2 / 0 |
| mountain-pine-v4 | 2 / 8 / 0 | 0 / 1 / 0 |
| **Tổng** | **12 / 26 / 0** | **2 / 9 / 0** |

Có ba điểm High cùng thỏa miễn alpha 0 và miễn tối; chúng được tính vào cột tối. Vì vậy alpha 0 riêng bằng 0 không có nghĩa diện miễn 12:58 bị bỏ qua. **Không có điểm ngoài hồ sơ.** Tập tọa độ/RGBA khớp chính xác cả manifest lẫn `199/edge-failures.json`.

Tọa độ cục bộ trong rect của cấp tương ứng, gốc trên trái:

| Sprite · cấp | x,y | RGBA | Qua cutoff 0,5 tại tâm texel |
|---|---|---|---|
| bamboo-clump-v3 · high | 573,317 | 83,32,67,104 | Không |
| bamboo-clump-v3 · high | 636,578 | 81,38,91,0 | Không |
| bamboo-clump-v3 · high | 636,579 | 84,31,88,0 | Không |
| bamboo-clump-v3 · high | 637,581 | 65,18,56,0 | Không |
| bamboo-clump-v4 · high | 659,874 | 67,31,56,0 | Không |
| bamboo-clump-v4 · high | 667,980 | 86,46,96,168 | Có |
| bamboo-clump-v4 · high | 667,981 | 87,49,103,36 | Không |
| canopy-block-v3 · high | 66,81 | 66,35,75,0 | Không |
| canopy-block-v3 · high | 384,621 | 60,13,65,87 | Không |
| canopy-block-v3 · high | 385,621 | 73,12,62,101 | Không |
| mountain-pine-v4 · high | 638,208 | 72,17,72,0 | Không |
| mountain-pine-v4 · high | 639,209 | 66,18,59,0 | Không |
| mountain-pine-v3 · medium | 67,22 | 107,56,114,8 | Không |
| mountain-pine-v3 · medium | 247,276 | 89,40,74,103 | Không |

**7 điểm alpha 0, 6 điểm alpha 1–127, 1 điểm alpha 168.** Chấm còn qua cutoff là tre v4 `[667,980]`, RGBA `[86,46,96,168]`, tọa độ atlas High `[667,2292]`.

Hai tờ mới dùng nền cỏ `#3f5a48` và tối `#101820`: [edges-x4.jpg](231/edges-x4.jpg) **210.279 B**, nearest ×4, đủ 14 điểm, so blend/cutoff; [edges-scale.jpg](231/edges-scale.jpg) **175.923 B**, các ô 64 px xem 1:1. Đã mở xem cả hai. Không thấy quầng magenta sáng rõ ở tờ tỷ lệ ước tính; điểm alpha 168 là một chấm tím sẫm sát thân. Claude vẫn chấm ngoại lệ.

Ước tính tỷ lệ dựa camera FOV 38°, pitch 55°, khoảng cách 58/22 m, viewport cao 1080 CSS px, scale 1; billboard nghiêng 0,4×pitch theo dải thiết kế 0,3–0,5. Texel High của tre v4 chiếm khoảng **0,375×0,315 px** ở 58 m và **0,990×0,830 px** ở 22 m; Medium thông v3 khoảng **0,750×0,631 / 1,979×1,660 px**. Đây là ảnh dẫn xuất và proxy lọc Lanczos, chưa mô phỏng shader, mipmap, ánh sáng, dither hay perspective theo chiều cao. RGB của 13 điểm dưới cutoff có thể vào mẫu lọc trước alpha test; không kết luận chúng luôn vô hình trong renderer.

### File, manifest và ngân sách

| File dưới `scenery/meadow/` | Cỡ | Byte | MD5 chạy lại |
|---|---|---:|---|
| color.high.webp | 4096² | 3,372,348 | `fef53b9ea18227487249a4d6537928f7` |
| normal.high.webp | 4096² | 611,454 | `321ac910a600294017a8d655ab84bba7` |
| color.medium.webp | 2048² | 1,137,886 | `de27494caf978c206f286f05d26bd837` |
| normal.medium.webp | 2048² | 194,888 | `fdd32fcf54d5998a2cbb3bb6e9b7c407` |
| shadow.high.webp | 1024² | 48,224 | `382a1b03bded6bd55e827c753b6015a5` |

**5/5 tên, cỡ, SHA-256 trong manifest và MD5/byte trong receipt 199 khớp file trên đĩa.** Manifest thực tế dùng SHA-256 cho `build.outputs`; MD5 được tính độc lập để so hồ sơ media, không giả định manifest có trường MD5. Tám id/metadata đã nhận, SHA ảnh nguồn, rect/UV/sizeM, không chồng rect và normal z dương đều đạt. Độ đầy High **50,657177%**, khớp 199.

Trần cứng đạt với dư **752.148 B High**, **1.746.180 B Medium**, **77.132 B khởi động**. Đích riêng scenery vượt **1.532.026 / 532.774 B**, giữ là P2-01 bên dưới. Bộ đo vẫn thiếu bốn model đã nêu trong hai báo cáo; không suy diễn đây là ngân sách Map1 đủ toàn bộ model.

### Pending 26 sprite

Đã chép riêng manifest và **năm WebP được manifest khai báo** từ `tmp/199/pending/` vào vùng tạm của 231, rồi dùng cùng oracle. Không tính các file thử codec dưới `work/` là đầu ra bàn giao. **406 High +77 Medium =483 điểm**, mọi tọa độ/RGBA, tên, cỡ, SHA và số miễn khớp hồ sơ; z normal dương. Miễn tối **4.421/815**, alpha 0 riêng **155/18**.

Scenery pending High **4.537.204 B**, Medium **1.468.556 B**; tăng **505.178/135.782 B**. Tổng dự phóng **15.753.030/7.389.602 B**, khởi động **3.558.650 B**, vượt **58.650 B**, đúng báo cáo 199. Bộ này chưa được nhận, giữ ngoài public; 231 không dựng lại hoặc xuất pending.

## 5. Phiếu 202 · đọc mã và kiểm hình học độc lập

Đọc toàn bộ năm file mới như diff thêm mới và dòng package của 199. [layout-audit.json](231/layout-audit.json) giữ oracle riêng, mã nguồn/SHA, bảng từng seed và đặc tả; không dùng `inspectLayout`, `SCENERY_TUNING`, `FOOT` hoặc helper kiểm hình học của 202. Đầu vào ground/road thật được giữ để kiểm đúng Map1.

| Mục | Kết quả |
|---|---|
| Module thuần | Chỉ import lanes, rules và type content; không DOM/three/file/đồng hồ/ngẫu nhiên hệ thống. Math chỉ abs/floor/imul/max/min/sqrt. `scenery-layout.ts:15`, `:258`. |
| Tất định | Cùng đầu vào giữ đúng JSON đầy đủ ở hai process riêng, không chỉ hash làm tròn; suite freeze/input/sort cũng xanh. |
| Golden | Tự tính FNV của fixture ×3 seed ×3 bậc: **9/9 khớp**, không cập nhật golden. |
| Chống lặp | Tự tìm láng giềng gần nhất cùng type: **0 trùng biến thể**; Poisson ngoài rừng có tỷ lệ nhỏ nhất **0,800036765 ≥0,8**. `:214`, `:298`. |
| Phân bậc | Mọi Low⊆Medium⊆High giữ nguyên mọi trường; **0 vượt ngân sách**, Low không cross. Chọn nguyên thành phần NN để không làm mất quan hệ biến thể. `:325`. |
| Hình học | **22 seed × 2 tập × 3 bậc = 132 bố cục**; **212.468 lượt vật**; mọi nhóm vùng cấm đều **0**. |
| Ô tháp | Lưới **8.649 điểm** trong [−46,46]², **4.757** được sim nhận sau đủ preset; **29.503 lượt điểm gần vật cố định**, **0 được nhận**. Điểm đối chứng (35,15) nhận; điểm buildable oracle và hàm export có **0 bất đồng**. |
| Chân trên đất xây | **0 vật cố định chạm đất xây được**; mọi vật field có `clearOnBuild:true`, phục vụ đổ khi xây. Không đổi quyền đặt nhà của sim. |
| Khoảng cách | Chân tới vùng mặt đường gần nhất dư **0,004257337 m**; cây cảnh tới cây luật gần nhất **4,093381538 m ≥4**; cây cao field cách tim đường **6,135035193 m ≥6**. |
| Cụm, rừng, lệch | High tập đủ VMR nhỏ nhất **26,549978 ≥1,5**; mỗi cạnh luôn **4 hàng**; scale hàng kế tăng ít nhất **1,110324×**, shade đúng 0,92^row; hàng trước cách mép **3,008448–5 m**; 0 khe không giải thích; flip ở type≥20 vật **50–52,381%**. |

Seed: mặc định, **1–20**, **20261030**. Tổng điểm gần vật cố định cộng theo bố cục, không phải 29.503 điểm lưới duy nhất. Dốc được kiểm cả bốn đường kính hợp đồng và thêm 64 hướng chẩn đoán: **0 vi phạm**. Các footprint có khe rất nhỏ vẫn dương; không tuyên bố còn biên sai số lớn khi renderer dùng kích thước khác.

Đếm seed mặc định đối chiếu báo cáo:

| Tập | Low lớn/cross | Medium lớn/cross | High lớn/cross |
|---|---:|---:|---:|
| Đủ 26 | **598/0** | **1000/1599** | **1500/4000** |
| Đã nhận 8 | **318/0** | **318/0** | **318/0** |
| Trần | 600/0 | 1000/1600 | 1500/4000 |

Tập chỉ tám cây giữ trống phần loại thiếu. Tán alpha, hướng camera, cây đổ và renderer chưa nằm trong hợp đồng dữ liệu; số cặp đĩa chân cùng sprite không chứng minh chống lặp tán thị giác theo TK §23.10. TK yêu cầu≥4 biến thể vẫn là thiếu hụt nguồn đã được 202 ghi nhận, không âm thầm coi v3/v4+lật là đủ bốn tranh.

### Hai đột biến trong bản chép riêng

| Đột biến ngữ nghĩa | Vị trí nguồn | Test đỏ / tổng | Assertion trực tiếp bắt được |
|---|---|---:|---|
| Bỏ `c.road(x,z,r)` khỏi `allowed` | `src/view/3d/scenery-layout.ts:160` | **14/73**, exit1 | 12 ca exclusions, fallback và golden |
| Ép `variants[0]` thay tô màu NN | `src/view/3d/scenery-layout.ts:244` | **16/73**, exit1 | 15 ca biến thể và golden |
| Khôi phục | Cùng file | **0/73**, exit0 | **73/73 xanh** |

SHA nguồn khôi phục **`d95372fdd22ab967052ea13f0c280a41d0cc870c721319613e4c4e4d324daa98`**, bằng worktree và bản chép chung. Test bắt luật sai độc lập với golden; không chỉ dựa vào đổi hash. [mutations.json](231/mutations.json) giữ câu thay thế, lệnh, exit, test đỏ và driver tái tạo.

## 6. Phát hiện và đề xuất

### P2-01 · Đích byte riêng của scenery chưa đạt · đã nêu trong 199

- **Tệp:dòng:** `scripts/td/prepare-scenery.mjs:328`, `public/assets/typing-defense/scenery/manifest.json:330`.
- **Tái tạo:** cộng byte color+normal+shadow High=**4.032.026**, color+normal Medium=**1.332.774**; so đích 2.500.000/800.000, vượt **1.532.026/532.774 B**. Tổng bộ hiện tại vẫn dưới trần; khởi động chỉ còn 77.132 B.
- **Đề xuất:** Claude chốt chấp thuận đích riêng hoặc giao lượt tối ưu có đo ở 64–72px/m, normal/codec. Không tự giảm mật độ dưới 64 hoặc sửa tranh trong phiếu kiểm. Pending chỉ được đưa vào runtime sau khi giải quyết phần vượt khởi động 58.650 B và nhận art.
- **Mức chặn:** không chặn commit công cụ hiện tại theo luật phiếu 199; phải giữ số liệu và kế hoạch tối ưu rõ.

### P2-02 · Một texel gần khóa còn qua cutoff và ảnh hưởng lọc cần chấm · đã nêu trong 199

- **Tệp:dòng:** `public/assets/typing-defense/scenery/manifest.json:428`, phần xử lý ngoại lệ `scripts/td/prepare-scenery.mjs:359`.
- **Tái tạo:** giải mã `color.high.webp`, crop tre v4, đọc `[667,980]=[86,46,96,168]`; alpha 168≥128. Xem hàng6 của tờ ×4 và nhóm tre v4 của tờ tỷ lệ. 13 texel còn lại dưới cutoff tại tâm vẫn có thể ảnh hưởng mẫu lọc.
- **Đề xuất:** Claude chấm theo quyết định 13:28, lưu ngoại lệ; khi L3 dựng renderer kiểm alpha test/lọc ở chính vị trí này. Nếu không nhận, giao lượt xử lý codec có so ảnh, không tự sửa tranh nguồn trong 231.
- **Mức chặn:** không chặn bàn giao kỹ thuật theo ngoại lệ13:28; chưa thay nghiệm thu thị giác cuối.

**202 không có phát hiện P0/P1/P2 trong phạm vi kiểm.**

## 7. Cần mắt của Claude

1. **Hai tờ của 231:** [phóng×4](231/edges-x4.jpg), [tỷ lệ camera ước tính](231/edges-scale.jpg), nhất là tre v4 `[667,980]`. Tờ×4 có cỏ/tối và blend/cutoff, không bỏ qua các texel alpha 0 chỉ vì chưa hiện ở tâm mẫu.
2. **Chân tre v3 lệch +19,030505%:** đối chiếu [sprites.jpg của199](../../games/.wt-td-scenery/tmp/199/sprites.jpg) và `manifest.json:134`; oracle xác nhận đúng hồ sơ, Claude chốt neo theo thân thật.
3. **Bố cục nhìn bằng vòng chân:** [seeds.jpg của202](../../games/.wt-td-scenery/tmp/202/seeds.jpg) và tờ chỉ tám cây đã nhận. Các cụm đổi theo seed, đường/nhà thoáng, rừng bốn hàng; cần L3 xem tán alpha, lặp sprite, mật độ, rừng nam che camera và dither trong 3D.
4. **Đích byte và nguồn biến thể:** chốt hai P2, kế hoạch pending, và phần≥4 biến thể còn thiếu. Đây là quyết định duyệt,231 không tự nhận ảnh 117/118.

## 8. Phạm vi bỏ qua có chủ ý và dọn

- Không sửa lỗi, commit/push hoặc chạy Git ghi. Không vào `.wt-td-ui`/200/203, không đụng Tu Tiên, game khác, audio-lab hoặc tài liệu nguồn của hai phiếu.
- Không dev server, trình duyệt, mạng, install, kit sync hoặc media commands. Build/test chỉ trong bản chép theo ngoại lệ của 231. Không chạy lại lệnh dựng atlas/pending; yêu cầu231 là chạy `--check` và kiểm độc lập đầu ra hiện có.
- Không sinh tranh/âm thanh. Hai JPG là ảnh ghép đo kiểm từ atlas; không có lượt image_gen và không phát sinh prompt sinh ảnh.
- Bộ đếm và driver được nhúng trong JSON để có thể tái tạo sau khi dọn. Các lệnh tái tạo dùng lại cách chép224 cùng các điều chỉnh symlink của mục 2, rồi chạy `pnpm check`, `pnpm td:golden:check`, `node scripts/td/prepare-scenery.mjs --check`, `pnpm exec vitest run tests/td-scenery-layout.test.ts`, giữ môi trường như mục 2.
- Đã prune thử rồi apply đúng vùng ảnh thô do làn atlas tạo: **136 ảnh / 6,993 MB**; dọn thêm **94 rawRGBA /187.692.992 B**; không xóa ảnh nguồn hay ảnh người khác. Receipt ở `atlas-audit.json.prune`.
- Kiểm cuối và việc xóa toàn bộ `games/typing-defense/tmp/codex-231/` được ghi trong [after.json](231/after.json), [cleanup.json](231/cleanup.json). Chỉ giữ báo cáo này, JSON và **hai JPG dưới 1 MB** trong 231.

**Kết quả cuối:** `find games/.wt-td-scenery games/typing-defense/public -newer <marker>` exit **0**, **0 dòng**. Toàn bộ inventory byte/SHA/mtime/symlink của worktree và public checkout chính không đổi; HEAD, status 11 đường và diff-stat giữ nguyên. **Đã xóa toàn bộ `games/typing-defense/tmp/codex-231/`; kiểm lại không còn tồn tại.** Chỉ giữ 14 JSON và hai JPG trong `231/`, cùng báo cáo này.
