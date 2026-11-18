# Phiếu 199 · Wordwoven · Atlas cảnh C9

**Đã hoàn tất phần công cụ và bàn giao:** có script, tập 26 ảnh, manifest runtime của tám cây 116, năm WebP trong checkout chính, test và ba tờ kiểm. `pnpm check` xanh **474/474**, golden bằng; lượt dựng thứ hai và `--check` đều exit 0, không ghi file. Claude còn cần duyệt **14 điểm gần khóa ở q95**, chân tre v3 và đích byte riêng của scenery. Đã tiếp tục xuất đúng quyết định điều phối 13:28; không tự nhận phần chấm bằng mắt đã đạt.

## 1. Phạm vi và đầu vào

Worktree `games/.wt-td-scenery`, nhánh `td-scenery`, HEAD `2a1f61d7da2ee6e6ca4abdc23f8775f872d9c9e7`. Điều kiện worktree, liên kết art/UI/ground/models, thư mục scenery thật, symlink meadow và `node_modules` đều có sẵn. Tiếp tục phần dở đã được nêu trong phiếu. Năm file 202 giữ nguyên SHA-256 suốt lượt; không có file lạ. `git diff --stat -- src` rỗng và `git diff --check` exit 0. [Mốc đầu](199/preflight-1328.json), [phạm vi cuối](199/scope-final.json).

Các file 199 trong worktree:

- `scripts/td/prepare-scenery.mjs`, `scripts/td/scenery-set.json`, `tests/td-scenery-prep.test.ts`.
- `package.json`: chỉ thêm dòng `td:scenery`.
- `public/assets/typing-defense/scenery/manifest.json`.
- `docs/changelog/2026-10-30-scenery-atlas.md`.

Tám cây 116 dùng alpha bàn giao; RGB trong mask khớp **0/255**, tốt hơn ngưỡng 2/255. Chiều cao lấy từ `116/visual-final/mock-layout.json`. 117/118 vẫn `accepted:false`, chiều cao đề xuất có `heightSource`; 117 theo tờ cảnh, 118 quy đổi chiều rộng đề xuất bằng tỷ lệ hộp sát. Gốc cây nằm ở `scenery/shared/`. Không đổi ảnh nguồn, tự sinh tranh hoặc âm thanh, sửa runtime, đồng bộ kit, dùng mạng, mở trình duyệt/dev server, cài gói hay chạy Git ghi. Ba tờ là ảnh ghép kiểm bằng ImageMagick theo phiếu, không có lượt image_gen hoặc prompt sinh ảnh mới.

## 2. Quyết định 12:58 và 13:28, điểm cần Claude xem

Phép kiểm đếm pixel ở 2 px trong mép và vành nở màu phía ngoài (High 8 px, Medium 4 px). Pixel có RGB gần khóa theo khoảng cách kênh ≤60 hoặc hue khóa ±20°, S >0,5 được phân loại:

1. **Miễn do tối:** `V=max(R,G,B)/255 <0,25`, ở mọi alpha và mọi khoảng cách.
2. **Miễn do alpha 0:** nếu chưa thuộc mục 1, alpha bằng 0, cách vùng alpha ≥0,5 từ 3 px và luma Rec.709 dưới 0,2. Luma là `(0,2126R+0,7152G+0,0722B)/255`.
3. Còn lại là điểm bị bắt. Ngưỡng V không làm thay đổi RGB hay alpha; chỉ sửa bộ kiểm. Số miễn dưới đây chỉ đếm các điểm khớp hue/khóa trong dải kiểm, không phải mọi điểm tối của tranh.

Đã thử tuần tự **q90 → q92 → q95**: còn **16 → 12 → 14** điểm ở cả hai cấp cộng lại. Giữ kết quả q95 cuối theo chỉ đạo; normal và shadow giữ q90. Từng lượt có byte, số bị bắt và số miễn từng sprite/cấp trong [accepted-metrics.json](199/accepted-metrics.json). Không chuyển lossless hay sửa phần vẽ để ép số.

Bản q95 có **12 điểm High, 2 điểm Medium** còn bị bắt; miễn do tối **26/9** điểm, miễn alpha 0 riêng **0/0**. Các diện miễn không đếm trùng: điểm tối đủ điều kiện alpha 0 vẫn nằm trong cột miễn tối.

| Id | Cấp | Số điểm còn | Tọa độ điểm V lớn nhất | RGBA điểm ấy | Max từng kênh trong nhóm |
|---|---|---:|---|---|---|
| bamboo-clump-v3 | high | 4 | [636, 578] | [81, 38, 91, 0] | [84, 38, 91, 104] |
| bamboo-clump-v4 | high | 3 | [667, 981] | [87, 49, 103, 36] | [87, 49, 103, 168] |
| canopy-block-v3 | high | 3 | [66, 81] | [66, 35, 75, 0] | [73, 35, 75, 101] |
| mountain-pine-v4 | high | 2 | [638, 208] | [72, 17, 72, 0] | [72, 18, 72, 0] |
| mountain-pine-v3 | medium | 2 | [67, 22] | [107, 56, 114, 8] | [107, 56, 114, 103] |

Tọa độ cục bộ trong rect của **cấp tương ứng**, gốc trên trái. Toàn bộ 14 tọa độ/RGBA nằm trong [edge-failures.json](199/edge-failures.json) và `manifest.build.edgeReview`. Phần cuối [edges-x4.jpg](../../games/.wt-td-scenery/tmp/199/edges-x4.jpg) có cả 14 điểm, phóng nearest ×4 trên ngọc và trắng; phần đầu vẫn đủ hai chỗ mép mỗi sprite. Claude quyết nhận bằng mắt; không dừng xuất vì điểm này theo quyết định 13:28.

Test được viết đỏ trước khi sửa bộ kiểm V. Test WebP ban đầu cũng đỏ khi còn 12 điểm High. Hợp đồng test đã cập nhật theo quyết định: mọi điểm còn lại phải được khai báo chính xác ở q95, đúng quyết định 13:28, tọa độ không trùng và RGBA khớp byte giải mã; **không có điểm chưa khai báo**. Đây là kiểm tính đầy đủ hồ sơ ngoại lệ, không phải khẳng định số pixel gần khóa bằng 0 hoặc tự chấm đạt thị giác. Test normal vẫn yêu cầu z dương ở mọi pixel đặc. [Ghi nhận test trước](199/test-first-1328.md).

**Chân tre v3 lệch phải +19,030505% chiều rộng rect**, vượt 15%; giữ đúng tâm thân, cần Claude xem vị trí neo. Canopy v4 chỉ 63,357143 px/m và thông v4 69,2 px/m do nguồn thấp hơn 72; không phóng to. Đây là giới hạn nguồn, không phải tự hạ mật độ chung dưới 64.

## 3. Chín mục kiểm

| Mục | Số và kết quả |
|---|---|
| 1. Check/build/golden | `pnpm check` exit 0: **44 file, 474 qua, 0 lỗi, 0 bỏ qua**; gồm test media giải mã thật. Kit verifier, TypeScript, Vite và đo gói xanh. Hai golden `same:true`, exit 0. |
| 2. Dựng lặp/check | Lượt dựng công cụ cuối **81.261913 s** toàn lệnh, trong đó pha dựng atlas **59,121 s**, phần còn lại là tạo tờ kiểm. Lượt hai **0.433831 s** toàn lệnh (**0,047 s** trong script), exit 0, **0 file đổi nội dung hoặc mtime**. `--check` **0.421299 s** (**0,036 s** trong script), exit 0 và không ghi. |
| 3. Sprite | Bảng mục 4; trước nén đều 0 khóa ở mép; sau nén 12/2 điểm theo ngoại lệ 13:28, đã lưu đủ để chấm. Z nhỏ nhất đều dương. |
| 4. Độ đầy | High tám cây **50,657177%**, rect không chồng, tọa độ/cỡ bội 4. |
| 5. Byte/ngân sách | `media-budget --json` trước/sau đều exit 0. Tổng thật High **15,247852 MB**, Medium **7,253820 MB**, khởi động **3,422868 MB**, dưới trần **16/9/3,5 MB**. Đích riêng scenery vượt, xem mục 5. |
| 6. Pending | `--pending` exit 0, pha dựng **67,748 s**, 26 ảnh ở **72 px/m**, đầy **54,026508%**. High thêm **505.178 byte**, Medium thêm **135.782 byte**. Khởi động dự phóng **3,558650 MB**, **vượt 58.650 byte**; chỉ nằm trong tmp, không xuất public. |
| 7. Ignore | Manifest `git check-ignore -q` exit 1 (không bị bỏ qua), luật phủ định manifest đúng. Cả năm WebP bị `*.webp` bỏ qua, kiểm trực tiếp ở đích checkout chính vì Git không đi qua symlink meadow. |
| 8. Phạm vi | Đúng sáu đường dẫn 199 và năm file 202 đã biết; không có đường dẫn lạ. Năm file 202 giữ nguyên hash; không sửa src. |
| 9. Media push | Năm file thật tại checkout chính, byte/MD5 ở mục 5 và `media-push.json`; Claude duyệt rồi commit/media:push. Chưa chạy commit hoặc push. |

Vitest **10,07 s**, Vite **0,949 s**. Gói gzip `/` **81,58 kB** (trần 85), `/?title=0` **83,04 kB** (85), 3D **171,83 kB** (260). Không đổi ván vàng. [Kiểm tổng hợp](199/verification.json), [lượt hai](199/build-second.json), [check chỉ đọc](199/check-read-only.json), [ignore](199/ignore-check.json). Nhật ký lệnh gốc ở `tmp/199/{build-final-first,check-final,golden-1328,pending-final}.log` trong worktree.

## 4. Bảng tám sprite

Nguồn là rộng,cao; hộp sát và rect High là x,y,rộng,cao, đơn vị px. Chân [từ trái,từ đáy] chuẩn hóa; độ lệch tính % rộng rect. “Sửa H/M” là số pixel đã khử khóa (High gồm nguồn + sau đổi cỡ); “khóa/tối/alpha0” tách rõ số còn bị bắt và hai diện miễn. Z là normal sau giải mã.

| Id | Nguồn | Hộp sát | Rect High | px/m | Chân | Lệch % | Sửa H/M | Khóa/tối/alpha0 H | Khóa/tối/alpha0 M | z min H/M |
|---|---|---|---|---:|---|---:|---:|---:|---:|---:|
| almond-tree-v3 | 1536,1536 | 77,95,1382,1349 | 0,0,1344,1312 | 72 | 0.460588,0.006098 | -3.941235 | 1/0 | 0/1/0 | 0/0/0 | 0.623529/0.639216 |
| almond-tree-v4 | 1536,1536 | 77,296,1382,1148 | 788,2480,1232,1024 | 72 | 0.499044,0.007813 | -0.095589 | 0/0 | 0/0/0 | 0/0/0 | 0.639216/0.647059 |
| bamboo-clump-v3 | 1024,1536 | 59,93,905,1351 | 0,2480,788,1168 | 72 | 0.690305,0.006849 | +19.030505 **XEM** | 2/3 | 4/7/0 | 0/3/0 | 0.639216/0.662745 |
| bamboo-clump-v4 | 1024,1536 | 51,156,921,1288 | 0,1312,840,1168 | 72 | 0.560269,0.006849 | +6.026926 | 0/0 | 3/0/0 | 0/0/0 | 0.631373/0.647059 |
| canopy-block-v3 | 1536,1024 | 77,178,1382,785 | 2744,0,1284,736 | 72 | 0.484983,0.01087 | -1.501684 | 0/0 | 3/5/0 | 0/3/0 | 0.639216/0.639216 |
| canopy-block-v4 | 1536,1024 | 77,76,1382,887 | 1344,0,1400,904 | 63.357143 | 0.506697,0.009956 | +0.669725 | 0/0 | 0/1/0 | 0/0/0 | 0.639216/0.639216 |
| mountain-pine-v3 | 1024,1536 | 68,93,887,1351 | 840,1312,680,1024 | 72 | 0.606788,0.007813 | +10.678755 | 0/1 | 0/4/0 | 2/2/0 | 0.670588/0.694118 |
| mountain-pine-v4 | 1024,1536 | 51,752,921,692 | 2744,736,940,708 | 69.2 | 0.536152,0.011299 | +3.615244 | 0/1 | 2/8/0 | 0/1/0 | 0.631373/0.654902 |

Chiều cao theo thứ tự: bàng v3/v4 18/14 m; tre 16/16 m; khối tán 10/14 m; thông 14/10 m. Không nung tối đáy, ramp, rim hoặc lật vào atlas. Chỉ tờ chiếu sáng thử có đèn trên trái, ramp ba bậc và tối đáy 25%.

## 5. Media và ngân sách

MB = 1.000.000 byte. Tiền tố của mọi đường dẫn dưới đây là **`games/typing-defense/public/assets/typing-defense/scenery/`** tại checkout chính; file đã có sẵn qua symlink của worktree.

| File | Byte | MD5 |
|---|---:|---|
| `meadow/color.high.webp` | 3,372,348 | `fef53b9ea18227487249a4d6537928f7` |
| `meadow/normal.high.webp` | 611,454 | `321ac910a600294017a8d655ab84bba7` |
| `meadow/color.medium.webp` | 1,137,886 | `de27494caf978c206f286f05d26bd837` |
| `meadow/normal.medium.webp` | 194,888 | `fdd32fcf54d5998a2cbb3bb6e9b7c407` |
| `meadow/shadow.high.webp` | 48,224 | `382a1b03bded6bd55e827c753b6015a5` |

| Bộ | Scenery High | Scenery Medium | Tổng High | Tổng Medium | Khởi động |
|---|---:|---:|---:|---:|---:|
| Trước xuất | 0 | 0 | 11,215826 MB | 5,921046 MB | 2,090094 MB |
| Tám cây, public thật | 4,032026 MB | 1,332774 MB | 15,247852 MB | 7,253820 MB | 3,422868 MB |
| 26 ảnh, dự phóng từ pending | 4,537204 MB | 1,468556 MB | 15,753030 MB | 7,389602 MB | 3,558650 MB |

Tám cây vượt đích riêng High 2,5 MB **1.532.026 byte**, Medium 0,8 MB **532.774 byte**. Đề xuất cho lượt tối ưu sau khi Claude chấm mép: đo mật độ chung 64–72 px/m, đo riêng normal và lựa chọn nén màu theo chất lượng thị giác; không tự giảm dưới 64 hoặc trở về q thấp hơn để che điểm còn lại. Các phương án này chưa được đo, không cam kết đạt đích. Pending chưa được nhận và cần giảm ít nhất 58.650 byte phần khởi động trước khi đưa toàn bộ vào public.

Model manifest hiện chỉ liệt kê **53/57** model Map 1; thiếu Mộc Tinh, worker-base, Draconis và helper-owlet là tình trạng sẵn có. Các trần trên đạt theo bộ kiểm hiện tại, chưa chứng minh đủ toàn bộ media Map 1. [Trước](199/media-budget-before.json), [sau](199/media-budget-after.json), [dự phóng](199/budget-projection.json), [media push](199/media-push.json).

Pending có **483 điểm** còn bị bắt sau q95; không nhận thay Claude. Số miễn từng sprite/cấp, thử q90/q92/q95 và toàn bộ tọa độ ở [pending-metrics.json](199/pending-metrics.json). [Mép pending ×4](../../games/.wt-td-scenery/tmp/199/pending/edges-x4.jpg) lấy hai điểm V cao nhất mỗi nhóm sprite/cấp có lỗi. Bộ này không ảnh hưởng manifest/runtime tám cây.

## 6. Đặc tả manifest cho L3

Manifest chính: `public/assets/typing-defense/scenery/manifest.json` trong worktree; [bản lưu JSON](199/manifest-final.json).

- `version:1`, `region:"meadow"`, `format:"webp"`; `uvOrigin:"top-left"`, `alphaCutoff:0.5`. `marginPx:8`, `bleedPx:8` tính theo High; Medium tương ứng 4 px. Căn rect lên bội 4, phần lề dư ở phải/đáy.
- `tiers.high/medium`: cỡ 4096²/2048², đường dẫn `color` và `normal` tương đối thư mục manifest, chung UV. Màu Medium Lanczos ×0,5; normal Medium dựng lại từ alpha Medium.
- `shadow`: cỡ 1024², `file`, chỉ `tiers:["high"]`; dáng alpha làm mờ nhẹ, chung bố cục UV. Nguồn là xám, không alpha; WebP giải mã RGB do đặc tính codec (chênh kênh tối đa đo được 1/255), đọc kênh R làm cường độ bóng. Medium dùng bóng tròn trong shader L3.
- `normal`: tangent; +x phải, +y lên trên ảnh, +z camera, `encode:"n*0.5+0.5"`. Giải mã `rgb*2-1` và chuẩn hóa; đọc dữ liệu tuyến tính (`colorSpace:"linear"`), không sRGB. Ngoài vật trước nén là `(128,128,255)`, trong vật z dương. WebP lossy có thể làm lệch chút giá trị phẳng ngoài vật.
- `sprites`: chỉ `accepted:true`. `id/type/variant/kind/ink` định danh; `ink:false`. `source` tương đối `art-src/`; `sha256` là PNG chính. Trường thêm `key` phục vụ kiểm mép.
- `uv:[x0,y0,x1,y1]`: rect cả lề chia cỡ atlas, gốc trên trái. `px:[w,h]`: rect High. Trường thêm `rect:[x0,y0,x1,y1]`: **hai góc pixel High**, dùng cắt chính xác thay vì đổi ngược UV đã làm tròn.
- `foot:[fx,fy]`: miền [0,1], từ trái và **từ đáy rect**. x trung bình tâm pixel alpha ≥0,5 trong 2% hàng dưới của hộp sát; y ở đáy hàng đặc thấp nhất. Đặt góc trái/dưới quad tại `chân thế giới − [fx*sizeM[0],fy*sizeM[1]]` trong mặt phẳng billboard.
- `heightM`: mét từ chân tới đỉnh hộp sát, không phải cả quad. `pxPerM`: chiều cao nội dung High chia `heightM`; `sizeM=px/pxPerM`: cỡ quad **cả lề**, mét. Giữ cỡ nguồn khi không đủ 72 px/m.
- Trường thêm gốc: `densityPxPerM` mật độ chung trước giới hạn nguồn, `pending` đánh dấu bộ thử. Các số thực làm tròn sáu chữ số.
- `build.recipe`: hash script, tập ảnh, SHA nguồn/alpha và phiên bản ImageMagick/cwebp. `build.outputs`: SHA năm WebP; `colorQuality`: q cuối, `edgeKeyPixels`: số còn bị bắt. `edgeReview` chỉ có khi q95 vẫn còn điểm, gồm quyết định 13:28, từng sprite/cấp, số điểm, max RGBA từng kênh và toàn bộ tọa độ/RGBA để kiểm lại. Đây là chẩn đoán, không phải sự phê duyệt của Claude.

`node scripts/td/prepare-scenery.mjs` dựng mục đã nhận. `--check` so recipe/hash đầu vào/đầu ra, chỉ báo thiếu/cũ và exit 1 khi khác, không tạo thư mục hoặc ghi file. `--pending` gồm toàn bộ 26 mục, chỉ ghi dưới `tmp/199/pending/`. `--review` tạo lại tờ kiểm; lượt dựng accepted còn điểm q95 tự tạo ảnh chứng cứ. `ink:true` lỗi rõ, không vẽ viền. Không có `toktx`, không thêm gói npm; cwebp lossy với alpha 100 và `-exact` giữ RGB nở màu dưới alpha 0.

## 7. Tờ kiểm và dọn

Đã mở xem ba tờ chính, đủ tám hàng, so ảnh giao/atlas cùng cao; tờ mép bổ sung cả High và Medium còn bị bắt:

- [atlas.jpg](../../games/.wt-td-scenery/tmp/199/atlas.jpg): 2048x1365, 596,624 byte.
- [sprites.jpg](../../games/.wt-td-scenery/tmp/199/sprites.jpg): 1920x3056, 867,019 byte.
- [edges-x4.jpg](../../games/.wt-td-scenery/tmp/199/edges-x4.jpg): 768x2521, 306,369 byte.

Đã chạy prune thử rồi mới apply trên đúng `games/.wt-td-scenery/tmp/199/work/`, dùng `--min-age-min 0` để dọn ảnh vừa tạo. Đã xóa **328 ảnh trung gian, 57,114,481 byte**, [nhật ký](199/prune-1328-apply.json); giữ ba tờ chính và toàn bộ `pending/`. Không prune cả `tmp/199`, không xóa ảnh của phiếu khác.

Các JSON thử nghiệm của lượt trước còn trong `199/` chỉ là lịch sử; số hiện hành nằm ở `accepted-metrics.json`, `pending-metrics.json`, `edge-failures.json`, `manifest-final.json`, `verification.json` và báo cáo này. Không còn điểm chặn cần hỏi trước khi xuất. Phần còn để Claude: chấm 14 điểm ×4, chân tre v3, quyết định đích byte riêng và kế hoạch tối ưu pending; sau duyệt mới commit/media:push.
