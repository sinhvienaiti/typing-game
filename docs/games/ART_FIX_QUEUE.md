# Hàng việc ảnh sau lượt chấm lại

Ngày 26/10/2026. Luật chấm và mức: [ART_ACCEPTANCE.md](ART_ACCEPTANCE.md). Ảnh, model tạm chấp nhận: [ART_REPLACE_LATER.md](ART_REPLACE_LATER.md).

## 1. Tóm tắt

Lượt chấm lại 26/10 có 136 kết quả: Rồng Giữ Ải 57, Lời Gọi 71 (63 ở lượt đầu, 8 chấm thêm: V14, V15, V34, V35, U4–U7), Tuyến Cuối 8 (model rainbow-tank trong kho Space tính ở Tuyến Cuối). Có 92 mục Đạt, 42 Tạm chấp nhận, 0 Sửa, 2 Tạo lại. Hai mục Tạo lại là hai nhánh Trại Lính V34, V35 (P2, mục 3): mỗi ảnh một lượt vẽ lại 2D của Codex, rồi mới gửi Tripo. Ngoài hai mục này không có lượt sinh ảnh Codex hay model Tripo làm lại nào. Việc còn lại là sửa không tốn tiền cho 42 mục Tạm chấp nhận (mục 5): 24 mục có thể nâng điểm, 12 mục chỉ còn bước nhập hoặc dọn nhỏ, 6 mục không có cách sửa miễn phí. Các việc này không chặn game: bản hiện tại dùng ngay được. Ngoài mục 5 còn ba việc nhập cho ảnh Đạt: ba icon kỹ năng I09, I10, I12 dùng ứng viên `_review/015`, phải chạy `icon.sh` trước khi nhập (như I11); ba icon nhà U5 (9,5), U6 (9,5), U7 (9) chạy `icon.sh` (khóa nền, lề 8 %, cỡ 256 và 64) trước khi nhập, U6 nền magenta nên dùng `--src-bg auto` rồi kiểm viền hồng; Trại Lính (P5-barracks) chấm lại 9,5, Đạt, P2, nên không ghi trong ART_REPLACE_LATER.md và không làm lại trên Tripo; nhưng `public/` còn model cũ 1,8 m, cần dựng lại preset `buildings/barracks` (typing-defense-static.json) từ GLB hiện có và sửa `SOURCES.json` (còn ghi ảnh `barracks.png` cũ).

Thêm hai việc trước khi gửi Tripo đợt 2 ([INDEX](../../typing-game-handoff-2026-10-25/tripo-upload-dot2/INDEX.md), mục "Ưu tiên"):
- V18, V37, V69 là ảnh nguồn 3D mức P2: bước "trước Tripo" ở mục 5.1 là bắt buộc, làm xong rồi mới gửi.
- Bốn ảnh nguồn Trại Lính VS (P2, INDEX P2 #38–41) đã chấm so với `barracks-v2.png` và render `3d/buildings/barracks.glb`. V14 `kits/barracks-kit-l2.png` 8 và V15 `kits/barracks-kit-l3.png` 8, Tạm chấp nhận: gửi ảnh hiện có (face 4000, không rig), nắn trong Blender sau khi có GLB (mục 5.1, 5.2). V34 `branches/barracks-khien-dong.png` 6,5 và V35 `branches/barracks-giao-dai.png` 5,5, Tạo lại: không gửi bản hiện có, vẽ lại 2D trước (mục 3).

## 2. Sửa bằng công cụ

Lượt chấm lại 26/10 không có mục mức Sửa. Lượt chấm đầu không có kết quả nào dưới 7 điểm; lượt chấm thêm có hai mục dưới 7 (V34, V35) nhưng lỗi không sửa được bằng công cụ, nên xếp Tạo lại (mục 3).

Thêm 27/10 từ Codex 015b lượt 3 (Codex tự chấm, Claude duyệt ảnh xem nhanh):

| Mã | File | Mức cần | Điểm | Việc sửa | Giữ file |
|---|---|---|---:|---|---|
| C21 Chân dung Mộc Tinh | [moc-tinh.png](../../games/typing-defense/art-src/portraits/moc-tinh.png) | P1 | 6 | Giữ dáng/màu Mộc Tinh nhưng ra toàn thân, mặt nhỏ ở 64 px, thiếu vệt mực tím và viền mực. Cần cắt đầu–tán–ngực, chuẩn hóa khổ/nền, bổ sung vệt mực và viền; lỗi sửa được, không tạo lại. Claude chấm độc lập. | Ảnh gốc giữ nguyên; bản cắt ghi tên mới. |


## 3. Tạo lại

**Xong 27/10:** cả hai đã vẽ lại một lần (Codex 015c, `games/typing-defense/art-src/README-015c.md`): V34 8, V35 7,5, tạm chấp nhận, chuyển sang ART_REPLACE_LATER.md; ảnh trong `tripo-upload-dot2` đã thay, gửi Tripo được. Bảng dưới là lý do lúc xếp mức.

2 mục, cả hai P2 (Lời Gọi, ảnh nguồn Tripo, INDEX P2 #40, #41). Mỗi mục tạo lại tối đa 1 lần (ART_ACCEPTANCE §2). Lần mới từ 7 điểm thì gửi Tripo face 10000 (KHÔNG bấm rig, Claude rig sau); vẫn dưới 7 thì dùng bản tốt hơn (bản hiện có từ 5 điểm) và ghi ART_REPLACE_LATER.md.

| Mã | File | Mức cần | Điểm | Vì sao không sửa được | Cách tạo lại |
|---|---|---|---:|---|---|
| V34 Trại Lính, nhánh Khiên Đồng | [barracks-khien-dong.png](../../games/typing-defense/art-src/branches/barracks-khien-dong.png) | P2 | 6,5 | Vẽ đẹp, cùng phong cách, đủ phần lớn nét nhánh (chân tường đá vôi, rào ốp khiên gỗ viền đồng, khiên đồng tròn trên cánh cổng, trống, mái ngói, mề đay, chóp bằng, bục bàn viết). Nhưng dáng gần y hệt `barracks.png` cũ (nhà dài thấp), trong khi Trại Lính đang dùng là tháp hai tầng (`barracks.glb` từ `barracks-v2.png`, 9,5). Cùng bề ngang chân chỉ cao khoảng nửa nhà gốc: lên nhánh thì nhà thấp đi, mất tháp. Phóng đều theo vòng Ø 4,6 m (02 §8) thì cao khoảng 2 m so với 4,5–5 m; kéo dãn Z khoảng 2 lần thì luật cấm, rào và cổng méo; phóng theo chiều cao thì chân rộng gấp đôi vòng. Gửi Tripo bản này là tốn face 10000 cho một model biết trước sai cỡ. | Codex, khối R-BRANCH, nền BG-G; tham chiếu chính `barracks-v2.png`, đính thêm ảnh này làm mẫu chi tiết. Giữ tháp trại hai tầng có sàn canh, cùng vòng chân, cao bằng hoặc hơn v2. Thêm chân tường đá vôi, rào ốp khiên gỗ viền đồng chồng lên nhau, cổng nặng có khiên đồng tròn trên mỗi cánh, trống cạnh cổng. Mái tháp lợp ngói đất nung, chóp bằng; giữ mề đay và bục bàn viết ở góc trước phải. Chấm lại. |
| V35 Trại Lính, nhánh Giáo Dài | [barracks-giao-dai.png](../../games/typing-defense/art-src/branches/barracks-giao-dai.png) | P2 | 5,5 | Có giá giáo cạnh cổng, trống bên kia cổng, sàn tập ván nâng phía sau, mề đay, chóp bằng, bục bàn viết. Thiếu rào cọc dài và cao hơn (nét đầu của đề); giáo trên giá rời, có khe; mũi giáo ở bốn góc sàn và dây lan can mảnh, trái luật không phần mảnh; mái rơm giống hệt nhà cũ, nên ở cỡ game gần như `barracks.png` cũ. Cùng lỗi gốc như V34: chỉ cao khoảng nửa tháp v2, phóng theo vòng thì cao khoảng 2 m, luật 02 §8 cấm kéo dãn riêng chiều cao; không ghép được vào chỗ Trại Lính. | Codex, khối A-BUILD + B-VILLAGE + R-BRANCH, nền BG-G; tham chiếu chính `barracks-v2.png`, đính ảnh này làm mẫu bố cục (giá giáo, trống, sàn tập). Giữ dáng tháp hai tầng có sàn canh, cùng vòng chân, cao bằng hoặc hơn v2. Rào cọc cao và dài hơn rõ, khoảng 1,5 lần rào v2. Giá gỗ cao cạnh cổng giữ một bó giáo to, buộc chặt thành một khối. Trống bên kia cổng; sàn tập ván nâng phía sau. Không mũi giáo rời, không dây mảnh; giữ mề đay, chóp bằng, bục bàn viết. Chấm lại. |

Bản hiện có của V34 (6,5) và V35 (5,5) giữ nguyên trong `art-src`, làm mẫu và làm bản dự phòng.

## 3b. Ảnh 2D dưới 8 (luật 27/10)

Chủ dự án 27/10: chỉ model 3D tiết kiệm theo luật 7 điểm; ảnh 2D phải từ 8 điểm mới đạt (ART_ACCEPTANCE §2.2). Chín ảnh 2D dưới đây trước ở ART_REPLACE_LATER.md (7–7,5), nay phải sửa hoặc tạo lại tới từ 8 điểm, tối đa 3 lượt một ảnh. Phiếu Codex [020](../codex-queue/020-2d-below-8-redo.md). C21 Chân dung Mộc Tinh (6, mục 2) đang sửa bằng công cụ ở phiếu 017; bản sửa chưa tới 8 thì tạo lại theo cùng luật.

V35 là ảnh nguồn Tripo (INDEX P2 #41): **chưa gửi Tripo** tới khi có bản từ 8 điểm.

| Mã | File | Mức cần | Điểm | Thiếu gì | Cách làm |
|---|---|---|---:|---|---|
| T3 Rêu dưới tán | [moss.png](../../games/dragon-hold/art-src/ground/pine-river/moss.png) | P1 | 7,5 | Rêu xanh đậm thành mảng tròn, khe lam lục tối; ghép 2×2 và 3×3 không thấy đường nối. Thiếu: mảng rêu đổ bóng như gò nổi, nhìn từ trên giống tán bụi; tương phản cao, tối hơn hẳn cỏ A/B; thêm lá tím lam và cành nâu ngoài đề, khá rối; khổ 1254×1254 thay 1024×1024. | Giữ prompt moss, nhấn: mảng rêu phẳng, chỉ chênh màu, không bóng, không gò; tương phản thấp ngang cỏ A; chỉ hai ba sắc xanh rêu và lam lục, không lá, cành hay kim thông; 1024×1024, lặp liền mép. |
| C23 | [draconis-ult.png](../../games/typing-defense/art-src/portraits/draconis-ult.png) | P1 | 7 | Rồng trắng cánh lông/giáp đen vàng rõ, chuyển động sang phải. Lửa thành xoáy hơn mưa lông xuống; nét dày chi tiết, nền đỏ hơn cam đào; cần kiểm dải cắt 3:1. | Tạo lại theo prompt cạnh ảnh (`.prompt.txt`), nhấn đúng chỗ ở cột Thiếu gì. |
| C9 | [lam.png](../../games/typing-defense/art-src/portraits/lam.png) | P2 | 7 | Giữ Lam và lửa xanh nhưng ra toàn thân, chưa cười lớn, ít viền mực; cần cắt đầu–thân trên, thêm lề phía tai/lửa, chuẩn hóa khổ và tách nền. | Tạo lại theo prompt cạnh ảnh (`.prompt.txt`), nhấn đúng chỗ ở cột Thiếu gì. |
| C10 | [tre.png](../../games/typing-defense/art-src/portraits/tre.png) | P2 | 7 | Tre giữ đồ và màu chuẩn, nhưng ra toàn thân, thiếu chuồn chuồn, búa chưa đặt trên vai và ít viền mực. Cần cắt chân dung, chuẩn hóa khổ/lề và nền. | Tạo lại theo prompt cạnh ảnh (`.prompt.txt`), nhấn đúng chỗ ở cột Thiếu gì. |
| C25 | [tre-ult.png](../../games/typing-defense/art-src/portraits/tre-ult.png) | P2 | 7 | Tre và búa/giàn tre đọc rõ; động tác vung ngang thay vì giơ cao, giàn giống đang vỡ hơn đang dựng. Nét nhiều chi tiết, cần kiểm dải cắt 3:1; giữ ảnh theo luật 7 điểm. | Tạo lại theo prompt cạnh ảnh (`.prompt.txt`), nhấn đúng chỗ ở cột Thiếu gì. |
| C22 | [dai-bang-tinh.png](../../games/typing-defense/art-src/portraits/dai-bang-tinh.png) | P2 | 7 | Đại Bàng Tinh giữ lông, mỏ, vòng vỏ sò/đồng; toàn thân quay trái, thiếu vệt mực và ít viền. Cần cắt đầu–ngực, lật ngang, bổ sung vệt mực/viền, xóa nét giống chữ nhỏ trên đồng, chuẩn hóa nền. | Tạo lại theo prompt cạnh ảnh (`.prompt.txt`), nhấn đúng chỗ ở cột Thiếu gì. |
| S15-v2 | [olive-tree-v2.png](../../games/typing-defense/art-src/scenery/coast/olive-tree-v2.png) | P2 | 7 | Giữ ô-liu cùng màu/nét v1; dáng nghiêng phải chưa rõ và còn gần v1, lá nhỏ nhiều. Cần thêm lề/đổi sang khổ dọc và khóa nền; không tạo lại. | Tạo lại theo prompt cạnh ảnh (`.prompt.txt`), nhấn đúng chỗ ở cột Thiếu gì. |
| S16-v2 | [casuarina-v2.png](../../games/typing-defense/art-src/scenery/coast/casuarina-v2.png) | P2 | 7 | Giữ phi lao và tán theo gió, nhưng thân vẫn gần thẳng/ngả trái nhẹ, khá gần v1, lá chi tiết. Cần thêm lề gốc và khóa nền; không tạo lại. | Tạo lại theo prompt cạnh ảnh (`.prompt.txt`), nhấn đúng chỗ ở cột Thiếu gì. |
| V35 Trại Lính, nhánh Giáo Dài | [barracks-giao-dai.png](../../games/typing-defense/art-src/branches/barracks-giao-dai.png) | P2 | 7,5 | Vẽ lại 27/10 theo tháp hai tầng. Thấp hơn tháp v2 khoảng 23 %; bó giáo còn khe giữa các mũi; một chấm xanh nhỏ ở sàn canh (do nền). | Prompt 015c, nhấn: giá giáo bó kín thành một khối, cao bằng tháp v2. |

## 4. Chờ kinh phí

Không có mục Tạo lại mức P3; các mục Tạm chấp nhận chờ thay khi có kinh phí ghi ở [ART_REPLACE_LATER.md](ART_REPLACE_LATER.md).

## 5. Sửa không tốn tiền

Việc tùy chọn, không chặn game. Ngoại lệ: bước "trước Tripo" của ảnh nguồn 3D mức P2 (V18, V37, V69) là bắt buộc trước khi gửi ảnh lên Tripo; gửi file mới trong `art-src`, không gửi bản chép trong thư mục handoff. Quy ước:
- Lệnh art-normalize chạy từ gốc repo, `export ART_MAGICK=/opt/homebrew/bin/magick` ([README](../../tools/art-normalize/README.md) §1). Trong bảng, `key-alpha`, `pad-margin`, `flat-bg`, `seamless`, `seam-check`, `icon` là `bash tools/art-normalize/<tên>.sh`; IN là file ở cột File.
- Mọi bản sửa ghi ra file mới cùng thư mục (vd. `.alpha.png`, `.1024.png`). Công cụ chặn ghi đè; giữ nguyên ảnh nguồn.
- Model sửa trong Blender: lưu GLB mới cạnh bản Tripo (vd. `<tên>.edit.glb`), không sửa bản gốc ([MEDIA_AND_MODELS.md](MEDIA_AND_MODELS.md) §4). Trỏ `source` trong preset sang bản mới, chạy `pnpm models:index --root games/<id>`.
- Chỉnh màu bằng magick làm sau khi tách nền: `-modulate` đổi cả màu nền khóa.
- Chỗ ghi "đã thử" là thử trên bản chép trong thư mục tạm, chưa ghi file nào vào `art-src`.
- Chấm lại sau khi sửa. Chỉ thay bản đang dùng khi điểm mới cao hơn; lên 9 thì gỡ khỏi ART_REPLACE_LATER.md.

### 5.1 Có thể nâng điểm

24 mục: 10 P1, 12 P2, 2 P3.

| Mã | File | Mức cần | Điểm | Việc làm | Có thể lên |
|---|---|---|---:|---|---|
| E01 Ong Gai | [thorn-wasp.glb](../../games/dragon-hold/art-src/3d/enemies/thorn-wasp.glb) | P1 | 7,5 | Khi tự rig trong Blender: xoay mỗi cánh quanh gốc 80–90° cho gần nằm ngang, chữ V nhẹ khi nhìn từ trước. Kiểm lại trên render 8 hướng ở 44 px. Vỏ Héo ở đầu vẫn giữ. | 8,5–9 |
| U1 Vệ Binh Rêu | [moss-warden.glb](../../games/dragon-hold/art-src/3d/units/moss-warden.glb) | P1 | 8 | Blender, trước bước rig: xóa nhánh chùy thừa (giữ nhánh khớp ảnh Front), xóa nửa khiên thừa, bịt mặt sau nếu hở. Mặt quay +X: xoay bằng preset. | 9 |
| K03 Thông non | [pine-young.glb](../../games/dragon-hold/art-src/3d/props/pine-river/pine-young.glb) | P1 | 8,5 | Preset static: `"material": {"metallic": 0, "roughnessMin": 0.9}` (khóa có sẵn trong `scripts/models/blender/static_model_tools.py`; Rồng Giữ Ải chưa có file preset). Blender: tô thân nâu đất như pine-tall. | 9 trở lên |
| K04 Cây tán tím | [tree-violet.glb](../../games/dragon-hold/art-src/3d/props/pine-river/tree-violet.glb) | P1 | 8,5 | Blender: tách texture màu, kéo mảng chàm ở nửa trước về #8E7CC3 (mặt nạ theo sắc), tô thân kem, nạp lại. Không dùng `colour.match` của preset: nó nhân đều cả texture. | 9–9,5 |
| K07 Đá tảng rêu | [rock-boulder.glb](../../games/dragon-hold/art-src/3d/props/pine-river/rock-boulder.glb) | P1 | 8,5 | Blender: kéo rêu xanh vàng về ôliu sẫm gần bụi rêu (mặt nạ theo sắc). Đo lại tỉ lệ texture gần #C8D24A, đích dưới 6 % như bush-moss. Dáng cụm khối góc cạnh vẫn còn. | 9 |
| T2 Cỏ xuân B | [grass-b.png](../../games/dragon-hold/art-src/ground/pine-river/grass-b.png) | P1 | 8,5 | `magick IN -modulate 100,115,85 grass-b.hue.png`. Đã thử: sắc trung bình 143° xuống 114° (A 90°), vẫn hơi lạnh như đề; hoa tím ngả lam. Đổi khổ giữ liền mép: `magick grass-b.hue.png -virtual-pixel tile -filter Lanczos -distort Resize 1024x1024 grass-b.1024.png`. Ghép xen A/B 2×2 để kiểm. | 9 |
| D4 Decal rêu, vũng nước | [moss-puddles.v1.alpha.png](../../games/dragon-hold/art-src/decals/pine-river/moss-puddles.v1.alpha.png) | P1 | 8 | magick, chỉ vùng rêu (mặt nạ sắc vàng lục): giảm sáng khoảng 10 %, xoay sắc về xanh đậm; xóa vài px tím hồng; giữ alpha. Rêu nổi khối, đá, lá phụ vẫn còn. | 8,5 |
| D2 Decal cụm hoa | [015-flower-clusters.png](../../games/dragon-hold/art-src/_review/015-flower-clusters.png) | P1 | 8,5 | Ghi README nguồn cho bản 015. `key-alpha IN <tên>.alpha.png --bg '#0000FF' --despill protect-interior` (D2 giữ mặc định, không `--no-key-hue`). Rồi `pad-margin <tên>.alpha.png <tên>.1024.png --size 1024 --margin 9.375% --grid 2x2` (lề 48 px mỗi ô; đường chia phải trống). Đặt bản mới trong `decals/pine-river/`. Kiểm tím còn nguyên. Trong lúc chờ dùng flower-clusters.alpha.png. Hoa chuông nghiêng vẫn còn. | 9 |
| I08 Icon Vảy Cứng | [hard-scale.256.png](../../games/dragon-hold/art-src/icons/normalized/hard-scale.256.png) | P1 | 8,5 | Trên ảnh gốc `ui/icons/hard-scale.png`: `-modulate 115,105,104` chỉ vùng đỏ cam sáng (mặt nạ, giữ viền nâu). Đã tính: #DB5E3F thành khoảng #E58A5F, gần cam đào Tim Rồng #F78759. Rồi `icon <file mới> games/dragon-hold/art-src/icons/normalized --sizes 256,64`. Dáng vảy méo ở 32 px vẫn còn. | 8,5–9 |
| U2 Icon Tháp Cung | [archer.png](../../games/typing-defense/art-src/ui/buildings/archer.png) | P1 | 8,5 | `key-alpha IN archer.alpha.png --bg auto` (nền xanh lá). `pad-margin archer.alpha.png archer.1024.png --size 1024 --margin 10%` (vuông, vật khoảng 80 % khung). Chỉnh màu cờ về #D9479B bằng magick, mặt nạ vùng cờ. Cung chìm ở 32 px vẫn còn. | 8,5–9 |
| S2-v2 Thông núi v2 | [mountain-pine-v2.png](../../games/typing-defense/art-src/scenery/meadow/mountain-pine-v2.png) | P2 | 8,5 | `key-alpha IN <tên>.alpha.png --bg '#FF00FF'`. Kéo tán về màu v1, chỉ vùng tán: đã thử `-modulate 94,78,100` toàn ảnh, tán gần v1 nhưng thân xỉn đi, nên phải có mặt nạ. Gốc lệch phải 76 px: neo ở gốc khi dựng, hoặc đệm 152 px trong suốt bên phải. Vòng quấn ở nhánh trái vẫn còn. | 9 |
| S6-v2 Cỏ lau v2 | [reed-clump-v2.png](../../games/typing-defense/art-src/scenery/meadow/reed-clump-v2.png) | P2 | 8,5 | `key-alpha IN <tên>.alpha.png --bg '#FF00FF'`; tẩy vệt tím ở khoảng x380 y780 và x880 y900. Kéo lá về xanh xám của v1, chỉ vùng lá: đã thử `-modulate 100,65,108` toàn ảnh, lá gần v1 nhưng bông lau ngả xanh. | 9 |
| S12-v1 Khối tán v1 | [canopy-block-v1.png](../../games/typing-defense/art-src/scenery/meadow/canopy-block-v1.png) | P2 | 8,5 | `key-alpha IN <tên>.alpha.png --bg '#FF00FF'`, rồi `magick <tên>.alpha.png -modulate 92,72,106 <tên>.tone.png`. Đã thử: tán gần màu bàng, thông, bớt vàng chanh. Vân lá ba thùy đều vẫn còn. | 9 |
| S12-v2 Khối tán v2 | [canopy-block-v2.png](../../games/typing-defense/art-src/scenery/meadow/canopy-block-v2.png) | P2 | 8,5 | Như S12-v1, cùng tham số để hai biến thể chung màu. | 9 |
| S13-v1 Gốc cây v1 | [tree-stump-v1.png](../../games/typing-defense/art-src/scenery/shared/tree-stump-v1.png) | P2 | 8,5 | `key-alpha IN <tên>.alpha.png --bg '#00FF00'`. `pad-margin <tên>.alpha.png <tên>.1024.png --size 1024 --margin 15%` (vật khoảng 70 % khung). Góc hơi nghiêng, đầu rễ mặt cưa vẫn còn. | 8,5–9 |
| S13-v2 Gốc cây v2 | [tree-stump-v2.png](../../games/typing-defense/art-src/scenery/shared/tree-stump-v2.png) | P2 | 8,5 | Như S13-v1. | 8,5–9 |
| F5 Đồi chè, cối xay | [layer-140-a.png](../../games/typing-defense/art-src/backdrops/w1-silverfall/layer-140-a.png) | P2 | 8,5 | `key-alpha IN <tên>.alpha.png --bg '#FF00FF' --mode global`: túi hồng trong khung cánh nhỏ hơn 64 px, chế độ connected bỏ sót. Còn hồng thì tô nâu khung cánh. Đường đồi 49,7 %: dời dải xuống 12,3 % chiều cao khi ghép; đỉnh cánh theo đó xuống khoảng 44 %, qua mốc 35 %. Hòa mép 6 % với ô b. Hồ, đảo đá vôi vẫn còn. | 9 |
| F6 Đồi chè trơn | [layer-140-b.png](../../games/typing-defense/art-src/backdrops/w1-silverfall/layer-140-b.png) | P2 | 8,5 | Như F5: `key-alpha … --mode global` khử viền hồng khóm tre; dời dải bằng ô a. Lặp bố cục với ô a vẫn còn. | 8,5–9 |
| V37 Mỏ Vàng, Lò Đúc Tiền | [gold-mine-lo-duc-tien.png](../../games/typing-defense/art-src/branches/gold-mine-lo-duc-tien.png) | P2 | 8,5 | Bắt buộc trước khi gửi Tripo (P2, INDEX P2 #27): tô miệng lò và dòng vàng chảy màu than đỏ sẫm, không sáng (magick, vùng chọn tay), ra file mới, gửi file này. Nếu đã lỡ dựng từ ảnh cũ thì tô lại trong Blender. Mất cửa hầm và ray vẫn còn. | 9 |
| V18 Bộ cấp Ruộng Lúa L2 | [farm-kit-l2.png](../../games/typing-defense/art-src/kits/farm-kit-l2.png) | P2 | 8,5 | Bắt buộc trước khi gửi Tripo (P2, INDEX P2 #10): `key-alpha IN <tên>.alpha.png --bg '#00FF00' --mode global --fuzz 25%`: lần thử khóa toàn ảnh 25–30 % giữ được cỏ, floodfill từ góc ăn mất cỏ góc trước phải. Khử loang mặc định xóa viền xanh ngọn bó lúa. Kiểm cỏ góc trước phải, rồi gửi bản `.alpha.png`. Giá phơi gỗ nâu vẫn còn. | 9 |
| V69 Hạt Mộc Tinh | [seed-drop.png](../../games/typing-defense/art-src/projectiles/seed-drop.png) | P2 | 8 | Bắt buộc trước khi gửi Tripo (P2, INDEX P2 #37): `flat-bg IN <tên>.flat.png --src-bg auto --bg '#00FF00' --size 1024x1024`, gửi bản `.flat.png`. Sau Tripo, Blender làm trơn múi (Smooth hoặc sculpt), giữ cuống và hõm đáy; hoặc dựng khối cầu có cuống. | 8,5–9 |
| V15 Bộ cấp Trại Lính L3 | [barracks-kit-l3.png](../../games/typing-defense/art-src/kits/barracks-kit-l3.png) | P2 | 8 | Gửi Tripo ảnh hiện có (INDEX P2 #39, face 4000, không rig); nền dải giữa lệch nhẹ, Tripo tự tách. Sau Tripo, Blender: chỉnh tỉ lệ từng trục cho vỏ mái khớp mái rơm `3d/buildings/barracks.glb`: thu bề ngang theo mặt bằng mái v2, nâng Z khoảng 15–25 % cho chụp kín chóp rơm (luật không kéo dãn riêng chiều cao của 02 §8 không áp cho bộ gắn); hoặc cắt mái rơm của nhà ở trên mép mái khi gắn cấp 3. Kiểm mặt dưới, đáy kín lộ ra thì khoét. Render ba góc trên `barracks.glb` rồi chấm lại. Không muốn tốn credit: tô lại mái rơm của `barracks.glb` thành ngói và gắn hai cột cờ, không gửi ảnh này. Ống ngói to ở mép trước vẫn còn. | 8,5–9 |
| V59 Mốc cảnh Đá Kê | [da-ke.png](../../games/typing-defense/art-src/landmarks/da-ke.png) | P3 | 8,5 | `flat-bg IN <tên>.flat.png --src-bg auto --bg '#00FF00' --size 1536x1024` trước Tripo. Sau Tripo, Blender hạ các đá cao về cùng một độ cao thấp. | 9 |
| gun-phao-sao Icon Pháo Sao | [gun-phao-sao.png](../../games/typing-survival/art-src/ui/icons/gun-phao-sao.png) | P3 | 8,5 | magick `-modulate 100,130,87` chỉ vùng đỏ cam (mặt nạ sắc). Đã tính: #E5684F thành khoảng #FC3864, gần #ff3f6c của theme. Rồi `pad-margin <file mới> <tên>.1024.png --size 1024 --margin 15%` (ảnh đã có alpha). Nòng cối mảnh, tối ở 32 px vẫn còn. | 8,5–9 |

### 5.2 Chỉ còn bước nhập hoặc dọn nhỏ, giữ điểm

12 mục: 6 P1, 3 P2, 3 P3. Lỗi chính của các mục này không sửa được bằng công cụ.

| Mã | File | Mức cần | Điểm | Việc làm |
|---|---|---|---:|---|
| T3 Rêu dưới tán | [moss.png](../../games/dragon-hold/art-src/ground/pine-river/moss.png) | P1 | 7,5 | Đổi khổ 1024 như T2. Đã thử hạ tương phản (`-brightness-contrast 15x-30`): ảnh bạc màu, gò rêu vẫn đổ bóng. Không nên dùng. |
| T7 Đá rêu dốc | [rock.png](../../games/dragon-hold/art-src/ground/pine-river/rock.png) | P1 | 8,5 | Đổi khổ 1024 như T2. Viền tối mép phiến vẫn còn. |
| T8 Lá thông rụng | [pine-litter.png](../../games/dragon-hold/art-src/ground/pine-river/pine-litter.png) | P1 | 8,5 | Mép lệch nhất bộ (MAE 11,8). Nếu phủ rộng thấy nối: `seamless IN <tên>.seamless.png --axis xy`, `seam-check <tên>.seamless.png <tên>.seam.png --axis xy --reference IN`, rồi mới đổi khổ 1024. Màu trung bình trùng earth nhưng hoa văn khác rõ; muốn tách tông thì `-modulate 110,110,100` (đã thử: sáng hơn earth một bậc). |
| D3 Decal sỏi, lá, kim thông | [forest-litter.alpha.png](../../games/dragon-hold/art-src/decals/pine-river/forest-litter.alpha.png) | P1 | 8,5 | Xóa khoảng 34 px xanh còn trên sỏi bằng magick (tô xám sỏi hoặc hạ alpha). Bóng khối, điểm sáng vẫn còn. |
| I11 Icon Long Hống | [015-skill-roar.png](../../games/dragon-hold/art-src/_review/015-skill-roar.png) | P1 | 8,5 | Bắt buộc trước khi nhập: `icon IN games/dragon-hold/art-src/icons/normalized --sizes 256,64` (ra `015-skill-roar.256.png`, `.64.png`). Đầu rồng khó nhận ở 32 px vẫn còn. |
| U4 Icon nhà Trại Lính | [barracks.png](../../games/typing-defense/art-src/ui/buildings/barracks.png) | P1 | 8,5 | Trước khi nhập: cắt sát vật trước khi đệm vuông để nhà to nhất có thể, rồi `icon IN games/typing-defense/art-src/ui/buildings/normalized --sizes 256,64` (khóa nền xanh, lề 8 %, vuông). Dáng nhà dài thấp cũ (khác tháp `barracks-v2`) và khổ 3:2 vẫn còn. |
| S3-v1 Khóm tre v1 | [bamboo-clump-v1.png](../../games/typing-defense/art-src/scenery/meadow/bamboo-clump-v1.png) | P2 | 8,5 | Sau `key-alpha --bg '#FF00FF'`: giảm bão hòa vàng chanh của thân (bắt đầu từ `-modulate 100,85,100`), cùng tham số với S3-v2 (Đạt, cùng lỗi màu). Thân thẳng, lá quả cầu vẫn còn. |
| nova Icon Nova | [nova.png](../../games/typing-survival/art-src/ui/icons/nova.png) | P2 | 8,5 | `pad-margin IN nova.1024.png --size 1024 --margin 15%` (ảnh đã có alpha). Hình bông tuyết ở 32 px vẫn còn. |
| V14 Bộ cấp Trại Lính L2 | [barracks-kit-l2.png](../../games/typing-defense/art-src/kits/barracks-kit-l2.png) | P2 | 8 | Gửi Tripo ảnh hiện có (INDEX P2 #38, face 4000, không rig); `flat-bg` trước là tùy chọn, Tripo tự tách nền. Sau Tripo, Blender: thu nhỏ đều ba chiều, đặt vào dải sân bên phải trong rào `3d/buildings/barracks.glb` (chân nằm trong vòng), render ba góc cùng nhà rồi chấm lại. Chòi lặp vai sàn canh v2 và chìm ở cỡ game vẫn còn. |
| V43 Đài Ấn, Vang Âm | [seal-dais-vang-am.png](../../games/typing-defense/art-src/branches/seal-dais-vang-am.png) | P3 | 8,5 | `flat-bg IN <tên>.flat.png --src-bg auto --bg '#00FF00' --size 1024x1024` trước Tripo. Khi dựng: khóa `sockets` của preset static đặt `FX_lantern_4` và `FX_banner` trên đầu cột khung đàn. Thiếu cột và móc đèn vẫn còn. |
| gun-tan Icon súng Tán | [gun-tan.png](../../games/typing-survival/art-src/ui/icons/gun-tan.png) | P3 | 8,5 | `pad-margin IN gun-tan.1024.png --size 1024 --margin 15%`. Viên đạn dính cụm ở 32 px vẫn còn. |
| gun-ray Icon súng Ray | [gun-ray.png](../../games/typing-survival/art-src/ui/icons/gun-ray.png) | P3 | 8,5 | `pad-margin IN gun-ray.1024.png --size 1024 --margin 15%`. Tấm giáp tối, mảnh vụn vẫn còn. |

### 5.3 Không có cách sửa miễn phí

6 mục, giữ nguyên đến khi có kinh phí:
- **tuyencuoi_rainbow-tank** (P1, 8,5, [rainbow-tank.glb](../../games/space-typing/art-src/3d/enemies/rainbow-tank.glb)): Trâu cần ảnh nguồn riêng. Việc không tốn tiền duy nhất: chụp trận rồi chấm lại (model runtime chưa có ảnh trận).
- **S4-v1, S4-v2** Bụi mâm xôi (P2, 8,5): lá nhiều chi tiết, rối ở cỡ thật.
- **S5-v1** Cỏ cao (P2, 8,5): lá mảnh, chìm trên nền cỏ.
- **V36** Mỏ Vàng, Hầm Sâu (P2, 8; INDEX P2 #26): thiếu miệng giếng, dáng gần nhà gốc. Gửi Tripo như ảnh hiện có.
- **title-horizon** (P3, 8,5): lệch phong cách với màn tựa 3D; src chưa nạp ảnh.

### 5.4 Kết quả phiếu 017 (27/10)

Codex làm 14 mục ([báo cáo](../codex-queue/017-report.md)). Claude chạy lại kiểm md5 nguồn (không đổi), xem hai tờ `_review/017-dh.jpg`, `_review/017-td.jpg` và chấm lại theo luật 2D từ 8. Codex tự chấm và Claude chấm cùng mức thì không cần người chấm thứ ba.

| Mã | File nhận | Claude chấm | Kết quả |
|---|---|---:|---|
| V18 | `kits/farm-kit-l2.alpha.png` | 8,5 | Nhận; đã thay vào bộ gửi Tripo (#10) |
| V69 | `projectiles/seed-drop.flat.png` | 8,5 | Nhận; đã thay vào bộ gửi Tripo (#37) |
| V37 | ảnh gốc giữ nguyên | 8,5 (gốc) | **Không nhận bản sửa**: hai lượt tô thành mảng đỏ phẳng. Ảnh gốc còn lò sáng, trái luật không ánh sáng, nên vẽ lại với lò nguội (phiếu [020c](../codex-queue/020c-td-gold-foundry-cold.md)): **xong 27/10**, lượt 3, Codex 8,5, Claude 8,5, Đạt; giảm 99,8 % px sáng gắt ở miệng lò và máng. `branches/gold-mine-lo-duc-tien.png` nay là bản mới (gốc giữ `.v1`), đã thay vào bộ gửi Tripo (#27), gửi được |
| C21 | không | 7,5 | Khung đầu, ngực đã đúng, nhưng vệt mực là hai dải phẳng. Vẽ lại ở phiếu [020b](../codex-queue/020b-td-moc-tinh-portrait.md): **xong 27/10**, lượt 1, Codex 8,5, Claude 8 (cùng phía ngưỡng), Đạt. `portraits/moc-tinh.png` nay là bản mới; bản cũ giữ `moc-tinh.v1.png` |
| T2 | ảnh gốc giữ nguyên | 8,5 (gốc) | **Không nhận bản chỉnh màu**: ngả vàng, ghép xen A/B lộ thành ô cờ, mép kém hơn gốc. Ảnh gốc đã đạt theo luật 2D |
| T3 | `ground/pine-river/moss.1024.png` (chỉ đổi khổ) | 7,5 | Đổi khổ không nâng điểm; vẽ lại ở phiếu 020 |
| T7 | `ground/pine-river/rock.1024.png` | 8,5 | Nhận (đổi khổ, mép giữ) |
| D4 | `decals/pine-river/moss-puddles.v1.tone.png` | 8,5 | Nhận: rêu xanh đậm hơn, hết px tím |
| D2 | `decals/pine-river/flower-clusters.015.1024.png` | 9 | Nhận, Đạt; rời ART_REPLACE_LATER |
| D3 | `decals/pine-river/forest-litter.clean.png` | 8,5 | Nhận (33 px xanh đã xóa) |
| I08 | `_review/017/hard-scale.warm.retry.256.png`, `.64.png` (lượt 2) | 8,5 | Nhận lượt 2; bản lượt 1 ở `icons/normalized/hard-scale.warm.*` có ranh gắt, không dùng |
| I11 | `icons/normalized/015-skill-roar.256.png`, `.64.png` | 8,5 | Nhận |
| U2 | `ui/buildings/archer.flag.png` | 8,5 | Nhận |
| U4 | `ui/buildings/normalized/barracks-v2.trim.256.png`, `.64.png` | 8,5 | Claude làm lại từ `buildings/barracks-v2.png`: bản của Codex vẫn là nhà dài thấp cũ, khác tháp hai tầng đang dùng trong game. Viền mực mảnh hơn icon cùng bộ |

Nhận ở đây là nhận file nguồn trong `art-src`. Đưa vào game (đổi đường dẫn nạp, chạy lại bản dựng) là bước nhập riêng của từng game.

## 6. Số lượng

**27/10, luật 2D từ 8 điểm:** bảng dưới là số của lượt chấm lại 26/10 theo luật cũ. Theo luật mới, mọi ảnh 2D 8–8,5 trong cột "Tạm chấp nhận" là Đạt. Còn 10 ảnh 2D dưới 8 phải sửa hoặc tạo lại: 9 ảnh ở mục 3b và C21 ở mục 2. Model 3D tạm chấp nhận còn 6: E01, U1, K03, K04, K07, rainbow-tank.

Theo game và mức:

| Game | Đạt | Tạm chấp nhận | Sửa | Tạo lại | Cộng |
|---|---:|---:|---:|---:|---:|
| Rồng Giữ Ải | 43 | 14 | 0 | 0 | 57 |
| Lời Gọi | 47 | 22 | 0 | 2 | 71 |
| Tuyến Cuối | 2 | 6 | 0 | 0 | 8 |
| Space Typing | 0 | 0 | 0 | 0 | 0 |
| **Cộng** | **92** | **42** | **0** | **2** | **136** |

Theo mức cần (Đạt / Tạm chấp nhận). Mười hai ảnh nguồn 3D VS của Lời Gọi (K04, K10, K13, V14, V15, V18, V34, V35, V36, V37, V68, V69) ghi P2 cho khớp INDEX đợt 2, nơi chúng nằm ở P2 cùng nhóm tổ thợ, bộ cấp và nhánh nhà bản đồ 1, Đại Bàng Tinh, Mộc Tinh đầy đủ. Hai mục Tạo lại (V34, V35) đều P2, không có trong bảng này:

| Game | P1 | P2 | P3 |
|---|---|---|---|
| Rồng Giữ Ải | 43 / 14 | 0 / 0 | 0 / 0 |
| Lời Gọi | 9 / 2 | 26 / 18 | 12 / 2 |
| Tuyến Cuối | 0 / 1 | 0 / 1 | 2 / 4 |
| **Cộng** | **52 / 17** | **26 / 19** | **14 / 6** |

Mục 5 theo mức cần:

| Nhóm | P1 | P2 | P3 | Cộng |
|---|---:|---:|---:|---:|
| 5.1 Có thể nâng điểm | 10 | 12 | 2 | 24 |
| 5.2 Chỉ bước nhập, dọn nhỏ | 6 | 3 | 3 | 12 |
| 5.3 Không sửa miễn phí | 1 | 4 | 1 | 6 |
