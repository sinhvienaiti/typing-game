# Phiếu 202 · Wordwoven · Dữ liệu bố cục cảnh C9 theo seed

Ngày 30/10/2026, chạy lại sau khi 199 đã xuất atlas và manifest. **Hoàn tất phần dữ liệu và bảy mục kiểm của 202:** `pnpm check` xanh **475/475 test, 44/44 file**, gồm **73/73 test 202**, không bỏ qua; TypeScript, build và ngân sách gói qua; golden gameplay thường/boss đều `same:true`. Giữ nguyên module và chín mã băm vàng của lượt trước, thêm một test đối chiếu tám sprite đã nhận với manifest 199. Xuất lại sáu tờ kiểm, ba JSON bố cục và toàn bộ số đo. Chưa gắn renderer; Claude duyệt rồi commit, L3 dựng cảnh.

## 1. Điều kiện đầu vào và phạm vi

- Làm trong `games/.wt-td-scenery`, nhánh `td-scenery`, HEAD `2a1f61d7da2ee6e6ca4abdc23f8775f872d9c9e7`. `node_modules/.modules.yaml`, các executable và dependencies đã có, lệnh test/tsx/tsc dùng được; không cài gói lại.
- Lúc bắt đầu lượt này có đúng **sáu file 199 chưa commit cộng năm file 202 đã biết**, không có file lạ. Tracked diff chỉ `package.json | 1 +` của 199. Áp dụng chỉ thị “Giữ phần đã làm”, không coi năm file 202 là file lạ. [Mốc đầu lượt hiện tại](202/rerun-preflight.json), [mốc đầu cũ](202/preflight.json), [lượt trước](202/restart-preflight.json). Nhánh và HEAD không đổi; lấy MD5 lúc **13:39:26** của sáu file 199 hiện hữu làm mốc, không khôi phục byte của lượt cũ.
- Tập thật có **26 mục: 8 đã nhận, 18 chờ nhận**. Manifest runtime của 199 có đúng tám mục đã nhận, năm WebP đã tồn tại. Test mới kiểm trùng khớp `id/type/variant/kind/heightM` và mọi sprite của bố cục accepted ở cả ba bậc đều tra được trong manifest. [Đối chiếu manifest và đường dẫn atlas](202/manifest-contract.json). Không sửa hoặc dựng lại bất kỳ file 199 nào. Điểm duyệt màu mép q95 của 199 vẫn thuộc [báo cáo 199](199-report.md), không chặn kiểm dữ liệu 202.
- Thêm đúng năm file trong worktree: `src/view/3d/scenery-layout.ts`, `tests/td-scenery-layout.test.ts`, `tests/golden/td-scenery-layout.json`, `scripts/td/scenery-layout-sheet.ts`, `docs/changelog/2026-10-30-scenery-layout.md`. Báo cáo/số đo ở repo cha; ảnh chỉ ở `games/.wt-td-scenery/tmp/202/`.
- Đã chạy `pnpm check` (kit + toàn bộ test), `pnpm build` riêng theo yêu cầu chạy lại, `pnpm td:golden:check`, đo media và xuất tờ kiểm theo ngoại lệ bắt buộc của lượt chạy lại. Không chạy Git ghi, dev server, trình duyệt, mạng, cài gói, đồng bộ kit hoặc chỉnh ảnh nguồn. Không đụng worktree khác, game khác hay Tu Tiên. JPG là hình kiểm dữ liệu bằng SVG/ImageMagick, không phải tranh mới hoặc âm thanh.

## 2. Đặc tả dữ liệu giao L3

Gọi `sceneryLayout(input, tier)`, với `tier` là `"low"`, `"medium"` hoặc `"high"`. Dùng cùng đầu vào và seed khi đổi bậc. Kết quả `{seed,tier,items,counts}`: `seed` là uint32; mặc định FNV-1a 32 bit trên ký tự của `map.id` (map 1 ASCII), hiện **3752287879**. `items` sắp tăng theo `sprite`, rồi `z`, rồi `x`, so sánh chuỗi trực tiếp, không phụ thuộc locale. `counts.large/cross/total` là tổng; các khóa `zone.kind` là số từng nhóm, khóa vắng nghĩa là 0.

Đầu vào `input`:

| Trường | Hợp đồng |
|---|---|
| `map` | `MapDef` chỉ đọc; dùng keep/gate/routes/water/bridges/nodes/trees/buildHalfM/halfM. |
| `houses` | Năm nền nhà đặt sẵn `{x,z,r}`; r lấy `BUILD.footprintR` theo footprint trong content. Giữ cả mỏ đặt sẵn. |
| `set` | Danh sách `{id,type,variant,kind,heightM}`. Bên gọi tự lọc `accepted:true` khi chơi; đủ 26 chỉ dùng kiểm trước khi được nhận. Không truyền đường dẫn file vào module. |
| `roadHalf` | `roadField(map, groundLanes(map.routes), halfM+BORDER_M).widths`, giữ đúng thứ tự lane/điểm. Thiếu thì dùng `map.roadHalfM × 1,5`; lề mòn thêm 0,8 m. |
| `dressing` | Chuyển `road.dressing` thành `{x,z,r}`. Vì chưa có footprint model chuẩn ở road.ts, đá dùng `1 × scale` m, thềm `3 × scale` m, đúng phương án dự phòng phiếu. |
| `heightAt` | Callback `(x,z)=>heightAt(map,x,z)` chỉ đọc, trả mét. Vắng thì không loại dốc. |
| `seed` | Số tùy chọn, chuẩn hóa uint32. Không có thời gian hoặc nguồn ngẫu nhiên bên ngoài. |

Một `SceneryItem`:

| Trường | Cách dùng ở L3 |
|---|---|
| `sprite` | id sprite đúng theo tập và manifest, ví dụ `almond-tree-v3`. Tra UV, chân và sizeM ở manifest. |
| `type`, `kind`, `variant` | Loại và biến thể; kind gồm tree/bamboo/canopy/bush/grass/flower/rock/log/stump. |
| `x`, `z` | Mét, mặt phẳng sim; gốc giữa sân, +x đông, +z nam/về Lũy. Module không có y; L3 đặt y theo ground. |
| `r` | Bán kính chân trên đất, mét, **đã nhân scale**. Đây không phải kích thước alpha của tán. |
| `scale` | Chiều cao vật = `scale × heightM` của entry được chọn. Nhân cả `manifest.sizeM` quanh chân đúng một lần; không dùng chiều cao quad có lề làm heightM. Ngoài rừng 0,85–1,15; rừng nhân tăng trưởng hàng. |
| `flip` | Lật hình ngang quanh chân; nếu đổi UV, nhớ chân ngang đổi `fx -> 1-fx` để thân không nhảy. |
| `tint`, `shade` | Hệ số sáng cuối `tint × shade`, áp một lần. tint 0,96–1,04; shade = 1 ngoài rừng và `0,92^row` trong rừng. |
| `row` | −1 ngoài hàng rừng; 0 trước, 1–3 lùi sau. Không phải độ cao y. |
| `zone` | Thứ tự xét sau cấm chung: water → keep → ring → band → field. Ring: ngoài 48 tới 88; band: ngoài 46 tới 48; field: phần còn lại trong 46. |
| `clearOnBuild` | true: L3 hạ/đổ vật khi nhà đè chân; mọi field đều true, kể cả đá. false: vật cố định, chân nằm hoàn toàn trong vùng cấm sim. Không dùng cờ này đổi quy tắc sim. |
| `cross` | true cho grass/flower: L3 dựng hai quad vuông góc; false cho vật lớn. Low không có cross. |
| `edge`, `slot` | Hai trường thêm phục vụ kiểm: edge 0/1/2/3 = bắc/đông/nam/tây; slot là chỉ số vòng lấy mẫu hình vuông trước bo góc. Cả hai −1 ngoài rừng. Không bắt buộc dùng để dựng. |

`buildableAt(input,x,z)` kiểm **một điểm đất** theo bounds, rect nước/cầu, tim lane với `BUILD.roadClearM`, vòng keep, nền nhà + gap và cây luật. Đây không phải `canPlace` cho một ngôi nhà: không xét bán kính nhà mới, giá, cap, phase hoặc connectivity. Test riêng đối chiếu `canPlace` với nhà S ở lưới 1 m và năm nhà đặt sẵn.

Nguyên tắc hạ bậc: một thứ tự ưu tiên các thành phần của đồ thị láng giềng cùng type, rừng trước, vật cố định khác tiếp, field sau; mỗi quỹ large/cross lấy phần đầu vừa ngân sách, dừng ở ranh thành phần. Giữ trọn thành phần bảo đảm láng giềng gần nhất không biến mất, hai màu biến thể và mọi trường đều giữ nguyên giữa bậc. Cặp gần nhất trùng khoảng cách phá hòa theo x rồi z. Có thể dư vài suất do không cắt đôi thành phần. Lật được xen kẽ theo type trong thứ tự giữ lại để mỗi prefix có xấp xỉ một nửa.

## 3. Hằng đang dùng và bảng FOOT

Bán kính chân khởi điểm `r = FOOT[kind] × heightM × scale`. Khi kiểm vị trí, dùng chiều cao lớn nhất của type để dành chỗ cho cả hai biến thể; sau tô biến thể mới giảm về r thật. Chưa phải footprint đo từ alpha/model, cần L3 xem trong 3D.

| kind | FOOT × heightM × scale |
|---|---:|
| tree | 0.075 |
| bamboo | 0.075 |
| canopy | 0.22 |
| bush | 0.22 |
| grass | 0.08 |
| flower | 0.14 |
| rock | 0.32 |
| log | 0.38 |
| stump | 0.3 |

Mọi hằng chỉnh cảnh ở đầu module, bản đầy đủ máy đọc trong [tuning.json](202/tuning.json). Các số băm/PRNG và phép chiếu hình học là hằng thuật toán, không phải núm chỉnh mỹ thuật.

| Hằng trong SCENERY_TUNING | Giá trị |
|---|---:|
| `borderM` | 40 |
| `vergeM` | 0.8 |
| `fallbackRoadK` | 1.5 |
| `keepYardM` | 7 |
| `yardSoftM` | 1.5 |
| `oreMinM` | 3.7 |
| `oreBaseM` | 2.2 |
| `oreRichnessK` | 0.5 |
| `treeClearM` | 4 |
| `gateHalfM` | 6 |
| `slopeSpanM` | 2 |
| `slopeRiseM` | 1.4 |
| `bankM` | 0.6 |
| `scaleMin` | 0.85 |
| `scaleRange` | 0.3 |
| `tintMin` | 0.96 |
| `tintRange` | 0.08 |
| `forestRows` | 4 |
| `forestFrontM` | 5 |
| `forestRowM` | 7 |
| `forestStepM` | 6 |
| `forestCornerM` | 10 |
| `forestPhase` | 0.25 |
| `forestStagger` | 0.5 |
| `forestGrowth` | 1.12 |
| `forestShade` | 0.92 |
| `forestJitterMin` | 0.97 |
| `forestJitterRange` | 0.06 |
| `clusterMinM` | 20 |
| `clusterRangeM` | 10 |
| `densityCut` | 0.56 |
| `poissonK` | 0.8 |
| `poissonCandidateFootM` | 0.7 |
| `poissonTries` | 24 |
| `reseedTries` | 18000 |
| `crossTries` | 24000 |
| `gridM` | 8 |
| `roadIndexReachM` | 12 |
| `fieldTallRoadM` | 6 |

Trọng số là đề xuất đầu, không cam kết tỉ lệ kết quả sau khi loại hình học và Poisson. Slot được tạo với đủ danh mục trước, rồi bỏ type vắng; không dồn trọng số sang loại khác. Loại chưa có trong danh mục 13 loại này chưa được phân bổ.

| type | kind | Chiều cao dự phòng lớn nhất (m) | Trọng số vật lớn field/band |
|---|---|---:|---:|
| almond-tree | tree | 18 | 3 |
| mountain-pine | tree | 14 | 3 |
| bamboo-clump | bamboo | 16 | 4 |
| canopy-block | canopy | 14 | 0 |
| fern | bush | 2.3 | 25 |
| reed-clump | grass | 3 | 0 |
| tall-grass | grass | 2.5 | 0 |
| wildflowers | flower | 1 | 0 |
| raspberry-bush | bush | 1.8 | 25 |
| rock-medium | rock | 3.4 | 8 |
| rock-small | rock | 0.664719 | 20 |
| rotten-log | log | 2.462413 | 6 |
| tree-stump | stump | 2.3 | 6 |

Mix khác: hàng rừng trước `canopy-block:70, almond-tree:10, mountain-pine:10, bamboo-clump:10`; hàng sau `canopy-block:100`; cross đất `tall-grass:65, wildflowers:35`; cross nước `reed-clump:100`. Vật lớn nước sinh từ các slot rock hợp lệ, chủ yếu đá nhỏ vì chân phải lọt hoàn toàn trong 0,6 m sát bờ.

Rừng bo theo các đường song song: lõi vuông nửa cạnh 43 m, bán kính góc hàng r = `10 + 7r` m; nửa cạnh bao ngoài 53/60/67/74 m. Pha vòng 0,25 bước, hàng lẻ lệch thêm 0,5 bước. Cỡ hàng `1,12^row × [0,97;1,03]`, đủ biên để trung bình hàng sau luôn lớn hơn 1,05 lần. Nhiễu giá trị nội suy trơn ở ô 20–30 m, loại vùng dưới 0,56; Bridson có active list, 24 ứng viên vòng, tái gieo để nối các cụm tách rời. Poisson chỉ áp hai vật lớn ngoài hàng rừng. Tán trong rừng được chồng.

## 4. Bảy mục kiểm và số chính

| Mục | Kết quả |
|---|---|
| 1 · Test, TypeScript, golden, build và gói | **`pnpm check` exit 0: 44/44 file, 475/475 test qua**, không lỗi/skip; **73/73 test 202**, chín mã băm cảnh giữ nguyên. Không có test thời gian đỏ cần chạy lại ba lần. `pnpm build` riêng **exit 0**, gồm tsc, Vite, bundle-budget, 142 module. Golden gameplay thường/boss **2/2 same:true**, exit 0. [Check đầy đủ](202/check-final.md), [build](202/build-final.md), [ngân sách gói](202/bundle-budget.json). |
| 2 · Phạm vi Git | Chỉ năm file mới 202 cộng đúng sáu file 199 đã có. Diff tracked chỉ `package.json | 1 +` của 199, như lúc vào; `git diff --stat -- src` rỗng. [Kiểm cuối](202/verification.json). |
| 3 · Giữ 199 | MD5 cả sáu file 199 đầu/cuối bằng nhau, gồm manifest runtime. [md5-199.txt](202/md5-199.txt). |
| 4 · Đếm | [counts.json](202/counts.json), bảng tổng và bảng vùng × kind bên dưới. |
| 5 · Luật | [rules.json](202/rules.json), toàn bộ vùng cấm 0; số chi tiết bên dưới. |
| 6 · Thời gian | Trung vị 5 lần High tập đủ **39.955 ms**, đích ≤50 ms, đạt. [timing.json](202/timing.json). Không có test thời gian cho sceneryLayout. |
| 7 · Tờ kiểm | Sáu JPG dưới 1 MB, đã xem từng tờ; ba JSON thô giao L3. Bảng đường dẫn/byte/nhận xét bên dưới. SVG trung gian đã tự xóa; không dùng prune --apply cho thư mục sản phẩm. |

Gói hiện tại (gzip): `/` **81,58 / 85 kB**, `/?title=0` **83,04 / 85 kB**; phần 3D **171,83 / 260 kB**; tổng JS **292,75 kB**. Dư tương ứng **3,42; 1,96; 88,17 kB**. Module bố cục chưa được renderer import, nên đây là số của bản game hiện tại, chưa phải số sau L3 gắn C9. Vite có cảnh báo chunk three >500 kB sau minify, nhưng ngân sách gzip đạt; không đổi cấu hình ngoài phạm vi.

[Đo media chỉ đọc](202/media-budget.json), exit 0: High **15.247.852 B / 16 MB**, Medium **7.253.820 B / 9 MB**, khởi động **3.422.868 B / 3,5 MB**, tới đêm 1 **4.065.425 B / 6 MB**. Đã gồm scenery 199: High **4.032.026 B**, Medium **1.332.774 B**. Trần tổng đều đạt; bộ khởi động còn **77.132 B**. Phần scenery vượt đích riêng 2,5/0,8 MB của phiếu 199; không hạ atlas trong phiếu 202, Claude xem theo báo cáo 199. Bộ đo liệt kê 53 model, còn thiếu bốn tên `enemies/moc-tinh`, `units/worker-base`, `heroes/draconis`, `helpers/helper-owlet`; chỉ ghi rủi ro, không sửa model.

Test đỏ trước mã ở lượt đầu: suite không tìm thấy module chưa tồn tại, lưu [test-red.md](202/test-red.md). Lượt này giữ nguyên module/vàng, thêm kiểm hợp đồng manifest vào test, kiểm lại bằng [suite đầy đủ](202/check-final.md) và [build gồm TypeScript](202/build-final.md). ECMAScript không cho freeze typed array có phần tử: test đóng băng sâu mọi object/array thông thường, giữ callback độ cao, và so JSON toàn bộ đầu vào gồm nội dung typed array trước/sau. Không sửa đầu vào.

Dòng golden gameplay (đầu ra nguyên văn đầy đủ ở [game-golden.md](202/game-golden.md)):

```text
{"same":true,"changed":{},"firstMovedAtTick":null,"content":"f2a21037","deck":"9c9b91d8","ticks":19660,"commands":389,"problems":0,"rejected":0,"summary":{"kills":51,"livesLost":4,"wavesCleared":3,"calls":64,"callWords":66,"callsPerfect":21,"keys":318,"keyErrors":14,"gold":29.8,"wood":87,"food":29,"bossDamage":0,"bossRetreats":0,"lives":16,"ultCasts":1,"ultFeathers":22,"directOk":0,"directMissed":1,"reviewBack":7,"reviewRedeemed":5,"freshWords":8}}
{"same":true,"changed":{},"firstMovedAtTick":null,"content":"f2a21037","deck":"9c9b91d8","ticks":5695,"commands":49,"problems":0,"rejected":0,"summary":{"kills":9,"livesLost":2,"wavesCleared":0,"calls":15,"callWords":9,"callsPerfect":4,"keys":39,"keyErrors":3,"gold":416.6,"wood":160,"food":18,"bossDamage":2110,"bossRetreats":1,"lives":18,"ultCasts":1,"ultFeathers":21,"directOk":0,"directMissed":0,"reviewBack":0,"reviewRedeemed":0,"freshWords":0}}
```

Các mã băm vàng cảnh đã làm tròn x/z/r đến 0,01 m; scale/tint/shade đến 0,001 trước khi băm JSON của items. Giữ nguyên thứ tự trường và items. File [golden cảnh](../../games/.wt-td-scenery/tests/golden/td-scenery-layout.json):

```json
{
  "1": {
    "low": "7ef26fa5",
    "medium": "a95c4fdb",
    "high": "c80acc03"
  },
  "20261030": {
    "low": "da7c5c45",
    "medium": "69a044aa",
    "high": "4deef4f9"
  },
  "default": {
    "low": "3af7e8a6",
    "medium": "cb54ec7a",
    "high": "16c5a3d3"
  }
}
```

| Tập | Bậc | Vật lớn / trần | Chữ thập / trần | Tổng |
|---|---|---:|---:|---:|
| Đủ 26 | low | 598 / 600 | 0 / 0 | 598 |
| Đủ 26 | medium | 1000 / 1000 | 1599 / 1600 | 2599 |
| Đủ 26 | high | 1500 / 1500 | 4000 / 4000 | 5500 |
| Đã nhận 8 | low | 318 / 600 | 0 / 0 | 318 |
| Đã nhận 8 | medium | 318 / 1000 | 0 / 1600 | 318 |
| Đã nhận 8 | high | 318 / 1500 | 0 / 4000 | 318 |

Tập chỉ tám cây đã nhận có ít hơn cả trần Low, nên ba bậc bằng nhau: **304 vật rừng + 14 cây field**, không thêm cây để bù cỏ/bụi/đá còn thiếu. Ngân sách là trần, không phải chỉ tiêu phải lấp đầy. Low ⊆ Medium ⊆ High với mọi trường bằng nhau ở cả tập mẫu và tập thật.

| Tập · bậc | Vùng | tree | bamboo | canopy | bush | grass | flower | rock | log | stump |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| all.low | field | 6 | 5 | 0 | 83 | 0 | 0 | 114 | 9 | 13 |
| all.low | band | 0 | 0 | 0 | 27 | 0 | 0 | 30 | 2 | 1 |
| all.low | keep | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| all.low | water | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 |
| all.low | ring | 8 | 8 | 288 | 0 | 0 | 0 | 0 | 0 | 0 |
| all.medium | field | 6 | 5 | 0 | 266 | 738 | 425 | 331 | 9 | 15 |
| all.medium | band | 0 | 0 | 0 | 27 | 187 | 138 | 30 | 2 | 1 |
| all.medium | keep | 0 | 0 | 0 | 0 | 27 | 16 | 0 | 0 | 0 |
| all.medium | water | 0 | 0 | 0 | 0 | 68 | 0 | 4 | 0 | 0 |
| all.medium | ring | 8 | 8 | 288 | 0 | 0 | 0 | 0 | 0 | 0 |
| all.high | field | 9 | 5 | 0 | 501 | 2361 | 1203 | 571 | 18 | 28 |
| all.high | band | 0 | 0 | 0 | 27 | 187 | 138 | 30 | 2 | 1 |
| all.high | keep | 0 | 0 | 0 | 0 | 27 | 16 | 0 | 0 | 0 |
| all.high | water | 0 | 0 | 0 | 0 | 68 | 0 | 4 | 0 | 0 |
| all.high | ring | 8 | 8 | 288 | 0 | 0 | 0 | 0 | 0 | 0 |
| accepted.low | field | 9 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| accepted.low | band | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| accepted.low | keep | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| accepted.low | water | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| accepted.low | ring | 8 | 8 | 288 | 0 | 0 | 0 | 0 | 0 | 0 |
| accepted.medium | field | 9 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| accepted.medium | band | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| accepted.medium | keep | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| accepted.medium | water | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| accepted.medium | ring | 8 | 8 | 288 | 0 | 0 | 0 | 0 | 0 | 0 |
| accepted.high | field | 9 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| accepted.high | band | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| accepted.high | keep | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| accepted.high | water | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| accepted.high | ring | 8 | 8 | 288 | 0 | 0 | 0 | 0 | 0 | 0 |

### Số luật

| Tập · bậc | Cố định chạm đất xây | canPlace nhận / điểm thử | Cây luật gần nhất (m) | Cùng biến thể | Cặp đĩa cùng sprite chạm | Khoảng cách / tổng r nhỏ nhất | VMR |
|---|---:|---:|---:|---:|---:|---:|---:|
| all.low | 0 | 0 / 171 | 8.516419 | 0 | 77 | 0.823557 | 10.411473 |
| all.medium | 0 | 0 / 760 | 8.516419 | 0 | 78 | 0.800326 | 27.652250 |
| all.high | 0 | 0 / 760 | 7.618737 | 0 | 79 | 0.800326 | 41.601786 |
| accepted.low | 0 | 0 / 0 | 7.618737 | 0 | 77 | 1.352274 | 0.902778 |
| accepted.medium | 0 | 0 / 0 | 7.618737 | 0 | 77 | 1.352274 | 0.902778 |
| accepted.high | 0 | 0 / 0 | 7.618737 | 0 | 77 | 1.352274 | 0.902778 |

Các mục vùng cấm `road`, `dressing`, `water`, `bridge`, `yard`, `house`, `ore`, `ruleTree`, `bounds`, `keepLarge`, `gateLarge`, `slope` đều **0 ở cả sáu tổ hợp**. Tất cả điểm field có clearOnBuild=true. Không có scale ngoài khoảng cho vật ngoài rừng hoặc tint sai khoảng; type có ≥20 vật đều đạt flip 40–60%, số đầy đủ theo từng type trong rules.json.

Điểm canPlace là **điểm lưới duy nhất**, không nhân lại cho nhiều vật: Low đủ 171, Medium/High đủ 760; cả ba tập đã nhận 0 vì rừng đứng xa lưới trong sân hơn `2+r`. Do đó số 0/0 ở tập đã nhận không phải 0 lỗi trên 760 phép thử. Có điểm đối chứng (35,15) mà cả buildableAt và canPlace nhận ở mỗi ca. Chân cố định còn được chứng minh hình học bằng đĩa nằm ngoài vuông xây, hoặc lọt trọn nước/keep, cộng kiểm điểm giữa và 16 điểm vành ở vùng chạm sân với buildableAt.

`touchingSameSprite` đếm cặp **đĩa r cùng sprite** chạm nhau (`d < rA+rB`, bỏ cross), làm số để L3 soi chỗ tán lặp. Vì hợp đồng bố cục chỉ có bán kính chân, phép đo này chưa dùng chiều rộng quad/alpha trong manifest, **chưa đo được số cặp alpha tán chồng chính xác**. Đây là giới hạn của tờ dữ liệu, không kết luận tranh tán đã chống lặp đạt. Nearest variant không có lỗi ở mọi bậc, dù các cặp xa hơn có thể cùng sprite.

VMR dùng 144 ô 8 m phủ [−48,48]², đếm vật lớn field, giữ cả ô 0; mẫu High mặc định bằng tập đủ hiện tại: **41,601786 ≥1,5**. Rất có cụm, còn phải xem mật độ trong 3D. Tập đã nhận không áp ngưỡng VMR theo phiếu.

Mép rừng mọi tổ hợp: **[4,4,4,4] hàng theo bắc/đông/nam/tây**, front cách mép sân **3,008448–5,000000 m**, khoảng hàng **[7,7,7] m**. Trung bình scale hàng 0→3: **1,001584; 1,123238; 1,256279; 1,405952**; tỉ số **1,121462; 1,118444; 1,119140**. Shade **1; 0,92; 0,8464; 0,778688**, các tỉ số 0,92; sai shade/zone = 0.

Hàng 0 có bước vòng danh nghĩa **6,057143 m**, khe vòng lớn nhất **42,4 m** ở vùng bị loại; có **11 slot miễn do cửa/nước/dốc và hình học cấm**. Khe không có lý do lớn nhất **6,057143 m ≤1,5 bước**, số khe không giải thích **0**. Đo theo tham số vòng trước bo góc (bảo thủ hơn chiều dài dây nối trong góc), không coi khe thác/cửa là lỗi kín rừng.

Số dễ đọc (chỉ ghi, không làm assertion):

| Tập · bậc | Cây cao / vật lớn field | Tỉ lệ | Cách tim đường gần nhất (m) |
|---|---:|---:|---:|
| all.low | 11 / 230 | 4.783% | 10.103798 |
| all.medium | 11 / 632 | 1.741% | 10.103798 |
| all.high | 14 / 1132 | 1.237% | 10.103798 |
| accepted.low | 14 / 14 | 100.000% | 10.103798 |
| accepted.medium | 14 / 14 | 100.000% | 10.103798 |
| accepted.high | 14 / 14 | 100.000% | 10.103798 |

Tập đủ đạt đề xuất cây cao ≤15%, tim đường ≥6 m. Tập đã nhận là 100% cây cao trên field do chỉ có cây, không vi phạm bằng cách sinh đồ chờ nhận để hạ tỉ lệ.

Năm lần đo lại High, đã có một lượt làm nóng và không chạy song song build/test: **39.686, 39.714, 40.510, 39.955, 40.598 ms**; trung vị **39.955 ms ≤50 ms**. Đo riêng sceneryLayout, không tính roadField, kiểm sim hoặc ImageMagick. Chưa đo trên Dell; không suy ra hiệu năng renderer.

## 5. Tờ kiểm và dữ liệu thô

| Tờ kiểm | Kích thước | Byte | Nhận xét khi xem |
|---|---|---:|---|
| [layout-high.jpg](../../games/.wt-td-scenery/tmp/202/layout-high.jpg) | 1760 × 1760 | 460508 | Cụm rõ ở bờ suối, đông bắc và giữa sân; bốn hàng rừng liên tục ngoài các khe hợp lệ; mặt đường thoáng. |
| [layout-medium.jpg](../../games/.wt-td-scenery/tmp/202/layout-medium.jpg) | 1760 × 1760 | 422393 | Cụm thưa hơn High, vẫn thấy phân bố theo vùng; rừng giữ đủ bốn hàng và đường thoáng. |
| [layout-low.jpg](../../games/.wt-td-scenery/tmp/202/layout-low.jpg) | 1760 × 1760 | 380261 | Không chữ thập, cụm vật lớn còn đọc được nhưng thưa; rừng giữ đủ bốn hàng, quanh đường rộng. |
| [layout-accepted-high.jpg](../../games/.wt-td-scenery/tmp/202/layout-accepted-high.jpg) | 1760 × 1760 | 368112 | Chỉ cây và tán: cụm field rất thưa vì loại chờ nhận để trống; mép rừng giữ nguyên, quanh đường thoáng. |
| [field-high.jpg](../../games/.wt-td-scenery/tmp/202/field-high.jpg) | 1920 × 1920 | 508749 | Phóng 20 px/m thấy cụm tách nhau, đĩa cây luật và nền nhà không bị lấn; chỉ thấy phần hàng rừng sát viền crop, không dùng tờ này để xét cả rừng. |
| [seeds.jpg](../../games/.wt-td-scenery/tmp/202/seeds.jpg) | 2640 × 880 | 544639 | Ba seed cho các cụm khác vị trí; bốn hàng rừng và khe địa hình giữ khung chung; đường trống ở cả ba ô. |

[layout-high-default.json](../../games/.wt-td-scenery/tmp/202/layout-high-default.json), [layout-medium-default.json](../../games/.wt-td-scenery/tmp/202/layout-medium-default.json), [layout-low-default.json](../../games/.wt-td-scenery/tmp/202/layout-low-default.json) giữ số thô không làm tròn vàng. JPG dùng vòng chân r, không giả lập alpha tán hoặc camera 3D. Nền thể hiện vuông 46/48/88, đường theo widths cộng lề 0,8, dressing, nước kéo dài, cầu, sân đá có mép mềm, nhà đặt sẵn, cây luật và hành lang cửa. Chú giải viền liền/đứt phân biệt cố định/đổ khi xây.

Script viết SVG nội bộ và xóa ngay chính SVG sau đổi JPG. Giữ cách phát stroke-opacity tường minh sau stroke để ImageMagick hiện đúng nét đường/vòng. Lượt này sửa tô màu rừng: nhân RGB với shade, giữ độ đục 0,65, để hàng sau tối hơn thay vì giảm độ đục làm nhạt trên nền sáng. Viền cũng nhân shade; dữ liệu items, thuật toán và chín golden không đổi. Lượt hiện tại xuất và xem lại đủ sáu tờ; tất cả có cùng byte như lượt trước. Đây chỉ là tờ kiểm, không ảnh người chơi thấy. Không còn ảnh thô cần prune. Chỉ chạy **dry run** trên thư mục sản phẩm; đầu ra nguyên văn ở [prune-dry.md](202/prune-dry.md), được chép ở phần cuối báo cáo.

## 6. Khác phiếu, giới hạn và việc L3 còn giữ

1. Đã chạy đủ `pnpm check`, build, toàn bộ test và đo gói theo ngoại lệ điều phối. Điểm chặn thiếu manifest của lượt trước đã hết. Không sửa thuật toán hay vàng cảnh để làm xanh. Test đỏ trước mã được giữ ở `202/test-red.md`; lượt này chỉ bổ sung kiểm hợp đồng đầu ra 199.
2. Đã nối kiểm tra tám mục đã nhận với manifest thật và năm atlas có sẵn, không sửa file của 199. Không import manifest hoặc đọc file từ module thuần. L3 truyền `manifest.sprites` trực tiếp làm `set` khi dựng, hoặc truyền tập đã lọc accepted; hai tập khớp năm trường hợp đồng. Tập đủ 26 vẫn chỉ để kiểm trước nhận 117/118.
3. Ngoài sân đá cứng 7 m của keep còn chừa 1,5 m mép mềm, là lựa chọn bảo thủ từ groundMasks; đường dùng nửa rộng lớn hơn của hai đầu segment thay vì chỉ điểm gần nhất, tránh lọt mép giữa các sample 0,25 m. Dressing theo bán kính dự phòng được phiếu cho phép vì road.ts chưa khai báo footprint asset.
4. Giữ trọn thành phần NN làm Low hụt 2 suất lớn và Medium hụt 1 cross; không ép lấp ngân sách. Tập đã nhận ba bậc bằng nhau là chủ ý giữ phần loại thiếu trống.
5. Phép đo dữ liệu dùng đĩa chân để ghi cặp cùng sprite chạm nhau; chưa mô phỏng alpha tán và hướng camera. L3 kiểm độ chồng tán thật khi dựng 3D. `r` là chân, không được đem làm alpha tán khi dựng.
6. Hình dữ liệu có thể cần L3 bổ sung `stableId` để lưu cây đã đổ qua đổi bậc, `windSeed`, hoặc `crownRadius/quadWidth` từ manifest; hiện có thể dùng type+x+z làm khóa ổn định. Không tự thêm quyền hay tham số shader.
7. Số lượng/FOOT/mix có thể cần chỉnh sau khi Claude xem trong 3D. Rừng nam giữa camera và sân có thể che ở góc thấp: L3 xử lý dither. Không kết luận chất lượng cảnh thương mại qua các vòng tròn kiểm.
8. Mỗi loại chỉ v3/v4, TK yêu cầu ≥4; lật chỉ bù một phần. 117/118 vẫn accepted:false; bản chơi đầu chỉ cây và mép rừng. Low chưa là Tier3D (hiện medium/high), dữ liệu Low vẫn theo ngân sách TK.

Không tạo renderer, billboard, shader, mesh, y hoặc cây đổ. Claude duyệt rồi commit; L3 gắn scenery.ts. Chủ dự án nên xem tờ High, tờ chỉ cây đã nhận và đặc tả scale/flip/r trước khi chốt giao diện.

## 7. Chạy lại

Từ repo cha:

```sh
cd games/.wt-td-scenery
pnpm check
pnpm build
node scripts/td/media-budget.mjs --json
pnpm exec vitest run tests/td-scenery-layout.test.ts
pnpm td:golden:check
ART_MAGICK=/opt/homebrew/bin/magick node --import tsx scripts/td/scenery-layout-sheet.ts --report-dir ../../docs/codex-queue/202
```

Chỉ khi có thay thuật toán có chủ ý và đã duyệt thay vàng cảnh: `UPDATE_SCENERY_GOLDEN=1 pnpm exec vitest run tests/td-scenery-layout.test.ts`. Không chạy lệnh update vàng gameplay. Từ repo cha, chạy thử dọn: `node tools/capture-prune/prune.mjs games/.wt-td-scenery/tmp/202`; **không thêm --apply**.

### Đầu ra prune chạy thử

```text
Danh sách ảnh thô sẽ xóa (byte):

Thư mục / nhóm cấp 1	Số file	MB (1 MB = 1.000.000 byte)
/Users/toandx/htdocs/typing-game/games/.wt-td-scenery/tmp/202 [cộng]	0	0.000
Tổng: 0 file, 0.000 MB; giữ 6 ảnh, từ chối 0 mục.
```
