# Phiếu 054 · AL-03: Ngữ pháp tên file (vai trò, biến thể)

Ngày làm: 28/10/2026. **Hoàn thành 3/3 kiểm nghiệm thu; 13/13 test đạt.**

## File tạo

- `tools/asset-library/lib/grammar.mjs`: hai hàm thuần `parsePath(relPath, ctx)` và `groupFiles(paths, ctx)`; không I/O, không gói ngoài.
- `tools/asset-library/test/grammar.test.mjs`: test các quy tắc, fixture thật, danh sách tên thật của hai game và lớp bọc `fs`.
- `tools/asset-library/test/fixtures/grammar/herb-hut.txt`: đúng **32 đường dẫn** từ `find games/dragon-hold/art-src -iname '*herb-hut*'`, sắp theo tên; chỉ chữ, không media.
- `docs/codex-queue/054-report.md`: báo cáo này.

Đã đọc thiết kế §3.3–3.6, bảng vai trò §3.5, ví dụ Herb Hut §4.4 và âm thanh §4.6; đọc phiếu AL-03, kết quả AL-02 và mã/từ vựng đã có. Không viết lại file của phiếu trước.

## Kết quả kiểm

Lệnh: `node --test tools/asset-library/test/grammar.test.mjs` (Node **v24.22.0**). Lượt cuối: **13 đạt, 0 hỏng, 0 bỏ qua**, mã thoát **0**, tổng thời gian **132,38 ms**.

| Kiểm | Kết quả |
| --- | --- |
| K1 · Chỉ ghi nơi được phép | Đạt. Tiến trình con bọc các hàm ghi của `fs`, bản đồng bộ, `fs.promises`, luồng ghi và `open` có cờ ghi trước khi import công cụ. Sau khi Node nạp module, chặn thêm đọc/mở file trong API. Chạy `parsePath` và `groupFiles` trên toàn bộ **3.229 tên thật**, fixture Herb Hut và các ca đặc biệt. In **Lời gọi ghi: 0; lời gọi đọc trong API: 0**. Test không tạo thư mục tạm hay ghi file. |
| K2 · Cây Git | Đạt. Phiếu chỉ tạo bốn file trong danh sách trên. `library/` và `tools/asset-library/` đã xuất hiện trong trạng thái đầu; mã/từ vựng AL-02 giữ nguyên. Hai bản trạng thái `games/` giống nhau, chép bên dưới. |
| K3 · Sản phẩm và vùng cấm | Không áp dụng bước grep: phiếu không sinh `library/out` hay `library/.thumbs`. Không đọc hoặc ghi các vùng cấm. |
| K4 · Test | **13/13 đạt**, không chạy build hoặc test suite của game. |
| 1 · Herb Hut | **32 tên → đúng 1 stem `houses/herb-hut`**. Đúng đủ mười số đếm trong bảng dưới; test đối chiếu fixture với tên thật trên đĩa. |
| 2 · Ca đặc biệt | `bamboo-clump-v1.v1.png` có `role: draft`, `variant: a`; `barracks.r2-rejected.glb` là `rejected`. Kenney `click`: **1 stem, 5 biến thể 001–005**; `impactWood_light`: **1 stem, 5 biến thể 000–004**; VCSL `wood_click_f_rr1.wav`: stem `wood_click_f`, biến thể `rr1`. |
| 3 · Tỷ lệ unknown | Rồng: **9/1.651 = 0,5451%**. Lời Gọi: **14/1.578 = 0,8872%**. Cả hai dưới **1%**. Chỉ `readdirSync` lấy tên và loại mục, không đi theo symlink, không mở media; in đầy đủ số vai trò và từng đường dẫn unknown. |

Số đếm Herb Hut:

| Vai trò | Số file |
| --- | ---: |
| concept | 1 |
| tripo-source | 1 |
| glb-original | 1 |
| glb-processed | 1 |
| icon | 1 |
| icon-256 | 1 |
| icon-64 | 1 |
| rejected | 9 |
| prompt | 14 |
| report | 2 |

Số vai trò trên cây thật:

| Vai trò | Rồng Giữ Ải | Lời Gọi |
| --- | ---: | ---: |
| concept | 76 | 303 |
| tripo-source | 32 | 0 |
| glb-original | 24 | 157 |
| glb-processed | 24 | 38 |
| glb-spare | 0 | 4 |
| icon | 20 | 0 |
| icon-256 | 22 | 0 |
| icon-64 | 22 | 0 |
| derivative | 7 | 33 |
| draft | 38 | 43 |
| rejected | 255 | 0 |
| prompt | 449 | 346 |
| report | 54 | 71 |
| review | 619 | 569 |
| unknown | 9 | 14 |
| **Tổng** | **1.651** | **1.578** |

## Quy ước API cho phiếu sau

- Đường vào tương đối dưới `art-src`, có thể kèm tiền tố `art-src/`; đường runtime bắt đầu bằng `public/` tính từ gốc game. Chấp nhận dấu phân cách Windows; từ chối đường tuyệt đối, đoạn `.`/`..`, đoạn rỗng, NUL và xuống dòng.
- `ctx.taxonomy` nhận dữ liệu JSON đã đọc, `ctx.game` chọn `folderMap[game]`; ưu tiên luật thư mục sâu nhất. Nếu chưa có taxonomy, có thể truyền `ctx.hyphenVariants: true/false` hoặc danh sách tiền tố như `['scenery/**']`. Bộ phân tích không tự nạp taxonomy.
- `ctx.sources` nhận nguyên dữ liệu `SOURCES.json`, `ctx.preset` nhận preset có `models[key].source`. Chúng nối ảnh, GLB gốc, GLB đã xử lý, báo cáo mã hóa `kind__id`, runtime và icon. Preset thắng `usedBy` cũ. Runtime hỗ trợ cả đường có thư mục lặp id như `props/herb-hut/herb-hut.high.glb`.
- `ctx.stems` là danh sách stem nguồn để nối icon/spare theo id duy nhất. `groupFiles` tự bổ sung stem từ các đường nguồn trong danh sách vào. Id mơ hồ giữ thẻ riêng; `ctx.links` cho phép ánh xạ tường minh từ stem sang stem khi bên gọi có bằng chứng.
- `parsePath` luôn trả đủ `{stem, role, variant, ticket, size, view, tier}`; trường không có là `null`. Biến thể ảnh `-v1/-v2` là `a/b`; biến thể âm giữ chuỗi `001`, `000`, `rr1`, `1`. Âm dùng vai trò `variant` đúng ví dụ §4.6.
- `groupFiles` trả `[{stem, files: [{path, role, variant, ticket, size, view, tier}]}]`, sắp ổn định theo stem và đường dẫn, bỏ đường trùng hoàn toàn; không sửa đầu vào hoặc context.
- Sidecar của file rejected vẫn là `prompt`, giữ `ticket`, `size`, `view`, `variant` nếu có; toàn bộ vùng `_review`, `review-vs*`, `_from-downloads` có vai trò `review`.
- Chỉ nối hậu tố Space `-2d` khi trường `image` chỉ ra liên kết. Không bỏ `-2d` hàng loạt. Nháp `.try1` vẫn là `draft`; xác định bản sao bằng md5 thuộc AL-06.

## Danh sách unknown

Rồng Giữ Ải, tương đối dưới `games/dragon-hold/art-src/` (**9 file**):

```text
2d/review-m0-wave4-5.html
3d/SOURCES.json
decals/pine-river/flower-clusters.015.1024.png
decals/pine-river/forest-litter.clean.png
ground/pine-river/grass-b.1024.png
ground/pine-river/grass-b.hue.png
ground/pine-river/moss.1024.png
ground/pine-river/rock.1024.png
ui/icons/hard-scale.warm.png
```

Lời Gọi, tương đối dưới `games/typing-defense/art-src/` (**14 file**):

```text
.vs-buildings.lock
3d/SOURCES.json
anim/mesh2motion/bird-animations.glb
anim/mesh2motion/human-addon-animations.glb
anim/mesh2motion/human-base-animations.glb
anim/mesh2motion/rig-bird.glb
anim/mesh2motion/rig-human.glb
anim/mesh2motion/rig-snake.glb
anim/mesh2motion/snake-animations.glb
portraits/dai-bang-tinh.fix2.png
props/gold-mine-cart.glb
tripo-spares/lam.tripo-skeleton.glb
ui/buildings/archer.1024.png
ui/buildings/archer.flag.png
```

## Bỏ qua và phần cần chủ dự án xem

- Không còn kiểm nghiệm thu nào chưa đạt. Không tạo hình/âm vì phiếu chỉ yêu cầu ngữ pháp và danh sách tên; không cần AudioLab, ffprobe, magick hay Blender.
- Không dùng mạng, trình duyệt, server, lệnh media, Git có ghi, build/test của game; không xóa, dời, đổi tên hoặc chép media.
- **Điểm cần xem khi duyệt:** ngoài các mẫu report nêu trực tiếp trong §3.5, có nhận diện hẹp bốn nhật ký sinh ảnh cũ ở gốc art-src của Lời Gọi: `vs-buildings-run.json`, `vs-characters-run.json`, `vs-buildings-005b.json`, `vs-buildings-005b-continuation.json`. Nội dung hiện có xác nhận chúng là nhật ký lượt sinh; mã chỉ xét tên theo mẫu `vs-(buildings|characters)-(run|<phiếu>[-continuation]).json`, không đọc chúng khi phân tích và không nhận mọi JSON là report. Nếu giữ chúng là unknown thì Lời Gọi có **18/1.578 = 1,1407%**, vượt trần. Các tên ngoài ngữ pháp khác vẫn được liệt kê nguyên trạng ở trên.

## Ảnh chụp Git

`git status --porcelain` lúc đầu:

```text
 M games/typing-survival
?? .claude/launch.json
?? TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md
?? docs/codex-queue/035-report.md
?? docs/codex-queue/036-report.md
?? docs/codex-queue/052-report.md
?? docs/codex-queue/053-report.md
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

Trạng thái chi tiết các đường được phép ghi, dùng `--untracked-files=all`:

```text
?? docs/codex-queue/054-report.md
?? tools/asset-library/lib/grammar.mjs
?? tools/asset-library/test/fixtures/grammar/herb-hut.txt
?? tools/asset-library/test/grammar.test.mjs
```

Dòng `M games/typing-survival` đã có từ đầu, thuộc làn khác; phiếu này không ghi dưới `games/`. Các dòng ngoài phạm vi khác giữ nguyên.
