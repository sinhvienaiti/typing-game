# Phiếu 058 · Thư viện tài sản · AL-07: đọc bảng tài liệu

Ngày 28/10/2026, repo cha trên Mac mini M4, Node v24.22.0. Đã đọc thiết kế §3.3, §4.1–4.3 và AL-06/AL-07; dùng nguyên mã AL-06 đang có. **Hoàn tất AL-07: K1–K4 và ba kiểm riêng đều đạt.**

## File tạo hoặc sửa

| Đường dẫn | Nội dung |
|---|---|
| `tools/asset-library/doc-facts.mjs` | Bộ đọc bảng Markdown, giới hạn nguồn, nối game+id/đường dẫn, bằng chứng dòng, kiểm file vắng và lệnh sinh JSON. |
| `tools/asset-library/scan.mjs` | Chỉ thêm import và bước gộp doc facts sau AL-06; ghi nhớ các dòng tuyển chọn đã đọc để giữ ưu tiên, kể cả khớp md5 sau đổi tên. Giữ toàn bộ thay đổi AL-06 có sẵn. |
| `tools/asset-library/test/doc-facts.test.mjs` | 7 test; fixture tự tạo dưới os.tmpdir(), tự dọn đúng cây của test. Không thêm fixture cố định. |
| `library/out/doc-facts.json` | 584 khóa game+id, 709 khóa đường dẫn, 1234 tham chiếu và 161 đường dẫn vắng. File bị Git bỏ qua. |
| `docs/codex-queue/058-report.md` | Báo cáo này. |

JSON dùng schema `asset-library-doc-facts/1`: `documents`, `byId`, `byPath`, `references`, `missing`, `warnings`. Mỗi fact giữ tên Anh/Việt/nghĩa khi tài liệu có, aliases, confidence, quality, provenance, triangles và evidence dạng file:dòng. `rong_`, `loigoi_`, `tuyencuoi_` lần lượt nối ba game đúng yêu cầu. Điểm/độ tin có dấu phẩy được đổi sang số; tam giác có dấu phân nhóm được đổi thành số nguyên.

Tên NAMES_EN ưu tiên cao nhất trong tài liệu; bản nhập 28/10 chốt điểm 3D, IMAGE_AUDIT chốt điểm 2D. Giữ riêng level2d/level3d để điểm đạt của ảnh không che mức tạm của model. Dòng chỉ có mã V/K nối qua mã duyệt 3D_REQUESTS khi xác định được đúng một id trong game. Bản GLB dự phòng giữ fact riêng theo đường dẫn, không đè bản chính theo game+id. Khi gộp thẻ, tuyển chọn vẫn thắng tài liệu; giữ trạng thái shipped/private/draft, số đo model có sẵn và thông tin nguồn AL-06. Không suy tên Anh khi tài liệu chưa cho tên.

## K1–K4

| Kiểm | Kết quả |
|---|---|
| K1 · Chỉ ghi chỗ cho phép | **ĐẠT.** Test bọc fs toàn cục: 2 lời gọi ghi trong cây tạm, 0 ghi khi đọc repo thật, 0 ngoài phạm vi. Lượt sinh thật dưới lớp bọc fs: đúng 2 lời gọi, mkdir `library/out` và writeFile `library/out/doc-facts.json`; 0 ngoài phạm vi. Chặn write/append/mkdir/rename/copy/symlink/unlink/rm/open có cờ ghi và các API đồng bộ tương ứng; không mở luồng ghi. |
| K2 · Cây Git | **ĐẠT đối với phiếu.** So đầu/cuối chỉ thêm 3 file mã/test/báo cáo được phép và bổ sung bước doc facts vào scan.mjs đã bẩn sẵn. Output JSON bị bỏ qua. Dòng games/typing-survival có sẵn từ đầu, giống cuối; không ghi vào game. Hai bản đầy đủ và hai bản games/ ở dưới. |
| K3 · Vùng cấm | **ĐẠT.** grep -rlE trên library/out: stdout rỗng, exit 1, 0 file khớp. library/.thumbs chưa tồn tại và không được tạo. Test: 0 lần đọc vùng cấm/symlink, 0 tên cấm rò vào JSON. Chặn 27 dòng trong bảng chung 3D_REQUESTS; không mở tài liệu riêng của game bị dừng hoặc monkeytype. |
| K4 · Test phiếu | **ĐẠT.** `node --test tools/asset-library/test/doc-facts.test.mjs`: 7 pass, 0 fail, 0 skip. Lượt xác minh cuối chạy cùng scan-joins.test.mjs: **16 pass, 0 fail, 0 skip**, exit 0, khoảng 1,06 giây. `node --check` hai file mới và `git diff --check -- tools/asset-library/scan.mjs` đạt, exit 0. |

Lớp bọc fs của AL-06 cũng vẫn đạt: 8 lời gọi ghi, tất cả dưới out của cây tạm, 0 ngoài phạm vi. Không chạy build hoặc test game.

## Kiểm riêng 1 · Số dòng từng tài liệu

**ĐẠT.** Test gọi grep thật với mẫu `^| `, đếm header và dòng kẻ bằng phép kiểm độc lập. Tất cả dòng kẻ hiện tại không có dấu cách sau |, nên số dòng kẻ cần trừ khỏi kết quả grep bằng **0** cho cả 7 tài liệu. Số dòng thân bảng bằng grep trừ header.

| Tài liệu | grep | Header | Thân bảng | Dòng sinh fact | Dòng bị chặn |
|---|---:|---:|---:|---:|---:|
| `docs/games/NAMES_EN.md` | 167 | 8 | 159 | 148 | 0 |
| `docs/games/3D_REQUESTS.md` | 235 | 24 | 211 | 143 | 27 |
| `docs/games/3D_IMPORT_2026-10-26.md` | 57 | 1 | 56 | 56 | 0 |
| `docs/games/3D_IMPORT_2026-10-28.md` | 145 | 3 | 142 | 142 | 0 |
| `docs/games/ART_REPLACE_LATER.md` | 103 | 4 | 99 | 99 | 0 |
| `docs/games/IMAGE_AUDIT_2026-10-25.md` | 686 | 17 | 669 | 633 | 0 |
| `typing-game-handoff-2026-10-25/tripo-upload-dot3/INDEX.md` | 9 | 1 | 8 | 8 | 0 |

NAMES_EN có đúng **148 dòng tên**, cộng 11 dòng quyết định/tóm tắt thành 159 dòng thân bảng. Import 26/10 có **56 dòng**, trong đó **55 tên file GLB** và một dòng ghi chưa có file. Import 28/10 hiện có **87 dòng ghép GLB**, cộng 14 dòng việc tạo lại và 41 dòng mức cần thành **142 dòng**; tài liệu đã thêm Cannon Tower cấp 2 sau mốc 86 của phiếu. Các số khác mốc khảo sát phản ánh nguồn hiện tại, không bỏ dòng để khớp mốc cũ.

## Kiểm riêng 2 · Bốn ca mẫu

**ĐẠT.** Test trên repo thật, trên fixture và gộp bản catalog hiện có trong bộ nhớ đều xác nhận dữ liệu. Không ghi lại catalog thật.

| id | Kết quả |
|---|---|
| choi-canh-doi | score3d=9, level=pass, tripoFile=`thatched+hut+3d+model (2).glb`, triangles=7733; bằng chứng import 28/10 dòng 82. |
| nha-rai-da | score3d=8.5, level=provisional, need=P3; bằng chứng import dòng 87, ART_REPLACE_LATER dòng 118. |
| barracks-kit-l2 | tripoFile=`wooden+hut+3d+model.glb`; bằng chứng import 28/10 dòng 57. |
| herb-hut | name=`Herb Hut`, score2d=9.5, tripoFile=`fantasy+cottage+3d+model.glb`; NAMES_EN dòng 89, IMAGE_AUDIT dòng 42 (H1), import 26/10 dòng 31. |

## Kiểm riêng 3 · File có thật hoặc nằm trong missing[]

**ĐẠT.** Kiểm độc lập **283 đường dẫn ở hai cột File/Đích**, 0 đường dẫn chưa được kiểm. Toàn bộ **1234 tham chiếu** đều có exists hoặc thuộc missing[]. Không đi theo symlink; đường dẫn đi ra khỏi repo bị chặn. **missing[] có 161 đường dẫn**, danh sách đầy đủ in dưới đây và trong JSON. Các file chưa có được báo cáo, không kéo media về hoặc sửa tài liệu nguồn.

```text
games/space-typing/art-src/3d/enemies/rainbow-scout.glb
games/typing-defense/art-src/backdrops/w1-rootwood/layer-140-a.png
games/typing-defense/art-src/backdrops/w1-rootwood/sky-a.png
games/typing-defense/art-src/backdrops/w1-whitestone/layer-140-a.png
games/typing-defense/art-src/backdrops/w1-whitestone/sky-a.png
games/typing-defense/art-src/fauna/butterfly.png
games/typing-defense/art-src/fauna/egret.png
games/typing-defense/art-src/fauna/firefly.png
games/typing-defense/art-src/fauna/gull.png
games/typing-defense/art-src/portraits/crew-archer.png
games/typing-defense/art-src/portraits/crew-barracks.png
games/typing-defense/art-src/portraits/crew-cannon.png
games/typing-defense/art-src/portraits/crew-farm.png
games/typing-defense/art-src/portraits/crew-gold-mine.png
games/typing-defense/art-src/portraits/crew-infirmary.png
games/typing-defense/art-src/portraits/crew-keep.png
games/typing-defense/art-src/portraits/crew-lumber.png
games/typing-defense/art-src/portraits/crew-scribe.png
games/typing-defense/art-src/portraits/crew-seal-dais.png
games/typing-defense/art-src/scenery/coast/basket-boat-v2.png
games/typing-defense/art-src/scenery/coast/basket-boat-v3.png
games/typing-defense/art-src/scenery/coast/basket-boat-v4.png
games/typing-defense/art-src/scenery/coast/casuarina-v3.png
games/typing-defense/art-src/scenery/coast/casuarina-v4.png
games/typing-defense/art-src/scenery/coast/limestone-medium-v3.png
games/typing-defense/art-src/scenery/coast/limestone-medium-v4.png
games/typing-defense/art-src/scenery/coast/limestone-small-v3.png
games/typing-defense/art-src/scenery/coast/limestone-small-v4.png
games/typing-defense/art-src/scenery/coast/morning-glory-v2.png
games/typing-defense/art-src/scenery/coast/morning-glory-v3.png
games/typing-defense/art-src/scenery/coast/morning-glory-v4.png
games/typing-defense/art-src/scenery/coast/net-rack-v2.png
games/typing-defense/art-src/scenery/coast/net-rack-v3.png
games/typing-defense/art-src/scenery/coast/net-rack-v4.png
games/typing-defense/art-src/scenery/coast/olive-tree-v3.png
games/typing-defense/art-src/scenery/coast/olive-tree-v4.png
games/typing-defense/art-src/scenery/coast/sea-grass-v2.png
games/typing-defense/art-src/scenery/coast/sea-grass-v3.png
games/typing-defense/art-src/scenery/coast/sea-grass-v4.png
games/typing-defense/art-src/scenery/meadow-neon/almond-tree-v1.png
games/typing-defense/art-src/scenery/meadow-neon/almond-tree-v2.png
games/typing-defense/art-src/scenery/meadow-neon/almond-tree-v3.png
games/typing-defense/art-src/scenery/meadow-neon/almond-tree-v4.png
games/typing-defense/art-src/scenery/meadow-neon/bamboo-clump-v1.png
games/typing-defense/art-src/scenery/meadow-neon/bamboo-clump-v2.png
games/typing-defense/art-src/scenery/meadow-neon/bamboo-clump-v3.png
games/typing-defense/art-src/scenery/meadow-neon/bamboo-clump-v4.png
games/typing-defense/art-src/scenery/meadow-neon/canopy-block-v1.png
games/typing-defense/art-src/scenery/meadow-neon/canopy-block-v2.png
games/typing-defense/art-src/scenery/meadow-neon/canopy-block-v3.png
games/typing-defense/art-src/scenery/meadow-neon/canopy-block-v4.png
games/typing-defense/art-src/scenery/meadow-neon/fern-v1.png
games/typing-defense/art-src/scenery/meadow-neon/fern-v2.png
games/typing-defense/art-src/scenery/meadow-neon/fern-v3.png
games/typing-defense/art-src/scenery/meadow-neon/fern-v4.png
games/typing-defense/art-src/scenery/meadow-neon/mountain-pine-v1.png
games/typing-defense/art-src/scenery/meadow-neon/mountain-pine-v2.png
games/typing-defense/art-src/scenery/meadow-neon/mountain-pine-v3.png
games/typing-defense/art-src/scenery/meadow-neon/mountain-pine-v4.png
games/typing-defense/art-src/scenery/meadow-neon/raspberry-bush-v1.png
games/typing-defense/art-src/scenery/meadow-neon/raspberry-bush-v2.png
games/typing-defense/art-src/scenery/meadow-neon/raspberry-bush-v3.png
games/typing-defense/art-src/scenery/meadow-neon/raspberry-bush-v4.png
games/typing-defense/art-src/scenery/meadow-neon/reed-clump-v1.png
games/typing-defense/art-src/scenery/meadow-neon/reed-clump-v2.png
games/typing-defense/art-src/scenery/meadow-neon/reed-clump-v3.png
games/typing-defense/art-src/scenery/meadow-neon/reed-clump-v4.png
games/typing-defense/art-src/scenery/meadow-neon/rock-medium-v1.png
games/typing-defense/art-src/scenery/meadow-neon/rock-medium-v2.png
games/typing-defense/art-src/scenery/meadow-neon/rock-medium-v3.png
games/typing-defense/art-src/scenery/meadow-neon/rock-medium-v4.png
games/typing-defense/art-src/scenery/meadow-neon/rock-small-v1.png
games/typing-defense/art-src/scenery/meadow-neon/rock-small-v2.png
games/typing-defense/art-src/scenery/meadow-neon/rock-small-v3.png
games/typing-defense/art-src/scenery/meadow-neon/rock-small-v4.png
games/typing-defense/art-src/scenery/meadow-neon/rotten-log-v1.png
games/typing-defense/art-src/scenery/meadow-neon/rotten-log-v2.png
games/typing-defense/art-src/scenery/meadow-neon/rotten-log-v3.png
games/typing-defense/art-src/scenery/meadow-neon/rotten-log-v4.png
games/typing-defense/art-src/scenery/meadow-neon/tall-grass-v1.png
games/typing-defense/art-src/scenery/meadow-neon/tall-grass-v2.png
games/typing-defense/art-src/scenery/meadow-neon/tall-grass-v3.png
games/typing-defense/art-src/scenery/meadow-neon/tall-grass-v4.png
games/typing-defense/art-src/scenery/meadow-neon/wildflowers-v1.png
games/typing-defense/art-src/scenery/meadow-neon/wildflowers-v2.png
games/typing-defense/art-src/scenery/meadow-neon/wildflowers-v3.png
games/typing-defense/art-src/scenery/meadow-neon/wildflowers-v4.png
games/typing-defense/art-src/scenery/meadow/almond-tree-v3.png
games/typing-defense/art-src/scenery/meadow/almond-tree-v4.png
games/typing-defense/art-src/scenery/meadow/bamboo-clump-v3.png
games/typing-defense/art-src/scenery/meadow/bamboo-clump-v4.png
games/typing-defense/art-src/scenery/meadow/canopy-block-v3.png
games/typing-defense/art-src/scenery/meadow/canopy-block-v4.png
games/typing-defense/art-src/scenery/meadow/fern-v3.png
games/typing-defense/art-src/scenery/meadow/fern-v4.png
games/typing-defense/art-src/scenery/meadow/field-marker-v1.png
games/typing-defense/art-src/scenery/meadow/field-marker-v2.png
games/typing-defense/art-src/scenery/meadow/field-marker-v3.png
games/typing-defense/art-src/scenery/meadow/field-marker-v4.png
games/typing-defense/art-src/scenery/meadow/mountain-pine-v3.png
games/typing-defense/art-src/scenery/meadow/mountain-pine-v4.png
games/typing-defense/art-src/scenery/meadow/raspberry-bush-v3.png
games/typing-defense/art-src/scenery/meadow/raspberry-bush-v4.png
games/typing-defense/art-src/scenery/meadow/reed-clump-v3.png
games/typing-defense/art-src/scenery/meadow/reed-clump-v4.png
games/typing-defense/art-src/scenery/meadow/rock-medium-v3.png
games/typing-defense/art-src/scenery/meadow/rock-medium-v4.png
games/typing-defense/art-src/scenery/meadow/rock-small-v3.png
games/typing-defense/art-src/scenery/meadow/rock-small-v4.png
games/typing-defense/art-src/scenery/meadow/rotten-log-v3.png
games/typing-defense/art-src/scenery/meadow/rotten-log-v4.png
games/typing-defense/art-src/scenery/meadow/tall-grass-v3.png
games/typing-defense/art-src/scenery/meadow/tall-grass-v4.png
games/typing-defense/art-src/scenery/meadow/wildflowers-v3.png
games/typing-defense/art-src/scenery/meadow/wildflowers-v4.png
games/typing-defense/art-src/scenery/rainforest/jungle-canopy-block-v3.png
games/typing-defense/art-src/scenery/rainforest/jungle-canopy-block-v4.png
games/typing-defense/art-src/scenery/rainforest/jungle-tree-v3.png
games/typing-defense/art-src/scenery/rainforest/jungle-tree-v4.png
games/typing-defense/art-src/scenery/rainforest/mossy-boulder-v3.png
games/typing-defense/art-src/scenery/rainforest/mossy-boulder-v4.png
games/typing-defense/art-src/scenery/rainforest/mushroom-cluster-v2.png
games/typing-defense/art-src/scenery/rainforest/mushroom-cluster-v3.png
games/typing-defense/art-src/scenery/rainforest/mushroom-cluster-v4.png
games/typing-defense/art-src/scenery/rainforest/orchid-clump-v2.png
games/typing-defense/art-src/scenery/rainforest/orchid-clump-v3.png
games/typing-defense/art-src/scenery/rainforest/orchid-clump-v4.png
games/typing-defense/art-src/scenery/rainforest/root-tangle-v2.png
games/typing-defense/art-src/scenery/rainforest/root-tangle-v3.png
games/typing-defense/art-src/scenery/rainforest/root-tangle-v4.png
games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v1-d0.png
games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v1-d1.png
games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v1-d2.png
games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v1-d3.png
games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v1-d4.png
games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v1-d5.png
games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v1-d6.png
games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v1-d7.png
games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v2-d0.png
games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v2-d1.png
games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v2-d2.png
games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v2-d3.png
games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v2-d4.png
games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v2-d5.png
games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v2-d6.png
games/typing-defense/art-src/scenery/rainforest/stilt-house-ruin-v2-d7.png
games/typing-defense/art-src/scenery/rainforest/tree-fern-v2.png
games/typing-defense/art-src/scenery/rainforest/tree-fern-v3.png
games/typing-defense/art-src/scenery/rainforest/tree-fern-v4.png
games/typing-defense/art-src/scenery/rainforest/vine-stump-v2.png
games/typing-defense/art-src/scenery/rainforest/vine-stump-v3.png
games/typing-defense/art-src/scenery/rainforest/vine-stump-v4.png
games/typing-defense/art-src/scenery/shared/tree-stump-v3.png
games/typing-defense/art-src/scenery/shared/tree-stump-v4.png
games/typing-defense/art-src/story/draconis/1.png
games/typing-defense/art-src/story/draconis/2.png
games/typing-defense/art-src/story/lam/1.png
games/typing-defense/art-src/story/lam/2.png
games/typing-defense/art-src/story/tre/1.png
games/typing-defense/art-src/story/tre/2.png
games/typing-defense/art-src/vfx/ma-troi-sheet.png
```

## Phần bỏ qua và việc cần chủ dự án xem

- Không quét lại catalog thật vì scan còn ghi catalog.json, scan-report.md và hash.json, ngoài danh sách được ghi của AL-07. Đã kiểm tích hợp bằng scan trong cây tạm và gộp catalog thật trong bộ nhớ. Claude có thể chạy `node tools/asset-library/scan.mjs` ở lượt được phép ghi các output đó; JSON facts đã sẵn sàng.
- Chỉ INDEX của tripo-upload-dot3 còn hiện diện tại gốc handoff được yêu cầu. Không có thư mục tripo-upload/tripo-upload-dot2 tại gốc handoff trên máy này; không tự mở bản tài liệu lưu nơi khác thay cho chúng.
- Chủ dự án/Claude cần xem missing[] (161 đường dẫn), gồm nguồn chưa làm và đường dẫn cũ. Ví dụ rainbow-scout.glb vắng đã được tài liệu nhập ghi dùng chung rainbow-tank; công cụ giữ bằng chứng và báo vắng, không sửa nội dung nguồn.
- Báo cáo AL-06 ghi độ phủ locks-only chưa đạt 90% và test AL-05 còn lệch đường cache. Đây là việc tiền nhiệm cần duyệt riêng, không sửa trong AL-07; 9 test riêng AL-06 vẫn đạt.
- Không sinh hình/âm vì phiếu này chỉ xử lý tài liệu; không cần magick, ffprobe, Blender hay AudioLab. Không dùng mạng, trình duyệt, server, lệnh media hoặc Git ghi. Không xóa/dời/chép file có sẵn; chỉ dọn fixture do test tự tạo trong thư mục tạm.

## Git status lúc đầu

```text
 M games/typing-survival
 M tools/asset-library/scan.mjs
?? .claude/launch.json
?? TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md
?? docs/codex-queue/035-report.md
?? docs/codex-queue/036-report.md
?? docs/codex-queue/057-report.md
?? docs/tools/map-factory/spike-l2-cau.md
?? shared/shared
?? tools/asset-library/lib/joins.mjs
?? tools/asset-library/test/scan-joins.test.mjs
```

## Git status lúc cuối

```text
 M games/typing-survival
 M tools/asset-library/scan.mjs
?? .claude/launch.json
?? TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md
?? docs/codex-queue/035-report.md
?? docs/codex-queue/036-report.md
?? docs/codex-queue/057-report.md
?? docs/codex-queue/058-report.md
?? docs/tools/map-factory/spike-l2-cau.md
?? shared/shared
?? tools/asset-library/doc-facts.mjs
?? tools/asset-library/lib/joins.mjs
?? tools/asset-library/test/doc-facts.test.mjs
?? tools/asset-library/test/scan-joins.test.mjs
```

## git status --porcelain games/ · lúc đầu

```text
 M games/typing-survival
```

## git status --porcelain games/ · lúc cuối

```text
 M games/typing-survival
```
