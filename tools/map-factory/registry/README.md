# Map Factory · Sổ model 3D

Bộ quét Node ESM độc lập, chỉ dùng thư viện chuẩn của Node; không cần cài package, mạng, trình duyệt hoặc build game. Nguồn đọc giới hạn ở `public/assets/<game>/models/**` và `art-src/3d/**` của `dragon-hold`, `typing-defense`, `space-typing`. Đi theo symlink của file và thư mục, chặn chu kỳ. Không đọc game Tu Tiên.

Chạy từ gốc repo:

```sh
node tools/map-factory/registry/scan-assets.mjs
node --test tools/map-factory/registry/test/*.test.mjs
```

Chạy bộ quét trước test: test đối chiếu sổ đã sinh với toàn bộ GLB hiện tại. Node v24.22.0 trên máy thực hiện không nhận đối số thư mục trong lệnh `node --test tools/map-factory/registry/test` (báo `MODULE_NOT_FOUND`); dùng glob ở trên để chạy các file `.test.mjs`. Không thêm `test/index.js` hoặc `test/package.json` vì chúng ngoài danh sách được phép ghi của phiếu 025.

Bộ quét chỉ ghi ba file JSON trong `out/`, không ghi media. Mỗi game có một object chứa `schemaVersion`, đơn vị, trục, scene, `statistics`, `mediaIntegrity`, `errors`, `needsDecompression` và mảng `assets`. Nội dung được sắp xếp cố định, không chèn thời gian chạy; cùng nguồn sẽ cho cùng kết quả. Mã thoát là 1 nếu có lỗi đọc hoặc md5 thay đổi; thiếu dữ liệu cần giải nén được ghi riêng để không biến metadata chưa biết thành số 0.

## Quy ước từng mục

| Trường | Ý nghĩa |
| --- | --- |
| `id`, `file`, `game`, `source`, `bytes` | Runtime: đường dẫn dưới `models/` bỏ `.glb`, giữ nguyên thư mục và hậu tố `.high`/`.medium`. Original: đường dẫn dưới `art-src/3d/` bỏ `.glb`. `file` luôn từ gốc repo. `source` phân biệt hai bản; dùng `file` làm khóa duy nhất. |
| `category`, `categoryHint` | `category` là thư mục đầu đúng theo đường dẫn. Vì vậy gói Dragon Hold có category `m0b`; `categoryHint` giữ nhóm trong manifest, hoặc nhóm sau tiền tố `m0b`, để hỗ trợ lọc `enemies`, `props`… Không thay category gốc bằng suy đoán. |
| `tags`, `tagsSource` | Token tiếng Anh đoán từ tên đường dẫn, một số ánh xạ thô như `hut` → `house`; luôn `tagsSource: "auto"`. Có thể có cờ sai vì tên vùng cũng xuất hiện trong đường dẫn; cần chủ dự án duyệt trước khi dùng để đặt vật thể. |
| `bounds` | `min`, `max`, `size`: mảng `[x,y,z]`, mét. `footprint`: `[sizeX,sizeZ]`, mét; `height`: `sizeY`, mét. Không phải diện tích m². Thiếu min/max ở bất kỳ POSITION đang dùng thì cả hộp là `null`, có lý do trong `needsDecompression`. |
| `upAxis`, `longestAxis`, `warnings` | Giả định `+Y` lên trên. Cạnh dài nhất chọn theo thứ tự X/Y/Z nếu bằng nhau. Sinh vật có cạnh dài nhất X/Z được gắn `creature-longest-axis-not-Y`. Chiều cao > 30 m hoặc < 0,05 m có cờ riêng. Đây là gợi ý rà soát, không tự chỉnh model. |
| `triangles` | Số tam giác trong scene 0; TRIANGLES lấy số index/3 hoặc POSITION count/3 nếu không có index. STRIP/FAN lấy `max(0,count-2)`; đếm cả tam giác suy biến nếu có. POINTS/LINES không thêm tam giác. Mesh dùng chung được nhân theo lượt node tham chiếu trong scene 0. |
| `meshes`, `primitives`, `meshInstances`, `primitiveInstances`, `materials` | Ba trường tài nguyên `meshes`, `primitives`, `materials` đếm mesh/primitive/material trong toàn GLB; hai trường `*Instances` đếm lượt sử dụng trong scene 0. Các tài nguyên không dùng trong scene 0 không thêm vào bounds hoặc triangles. |
| `textures` | `count` là số ảnh (`images`), `textureObjects` là số texture object của glTF. Mỗi ảnh giữ chỉ số, tên, MIME, byte, `format`, `width`, `height`. Đọc header PNG, JPEG và WebP VP8/VP8L/VP8X, không giải mã ảnh. KTX2 ghi `format: "ktx2"`, kích thước `null`. Hỗ trợ ảnh nhúng, data URI và URI file cục bộ; từ chối URI mạng. |
| `skinned`, `animations` | `skinned` cho biết GLB có skin. Mỗi clip có `name`, `start`, `end`, `duration = end - start`, giây; hợp khoảng của mọi input sampler. Ưu tiên min/max accessor thời gian; nếu thiếu thì đọc FLOAT SCALAR từ BIN chưa nén. Chưa đọc được thời gian thì duration `null` và ghi vào `needsDecompression`. |
| `extensions` | Hợp các tên trong `extensionsUsed`, `extensionsRequired` và object `extensions` trong cấu trúc glTF; không coi nội dung `extras` là extension. |
| `original`, `sourceRecord`, `sourcesFile` | Runtime nối bản gốc khi có bằng chứng; giữ đường dẫn, md5 thực đọc, cách nối (`match`) và nguyên mục trong `SOURCES.json`. Original giữ mục nguồn ở `sourceRecord`, gồm ảnh 2D, `usedBy`, md5 công bố. Không đọc/sửa ảnh 2D. Không khớp thì `original: null`, cờ `original-not-found`. |
| `licence` | Original dưới `art-src/3d` và runtime Dragon Hold/Typing Defense đã nối nguồn: `owner-tripo`. Runtime Space: `space-library`. Các runtime còn lại: `unknown`. Đây là nhãn theo quy ước của phiếu, không phải xác minh điều khoản cấp phép bên ngoài. |
| `manifest`, `manifestFile`, `manifestKey`, `tier` | Tìm theo URL GLB trong `models[*].tiers`, bỏ query/hash. `manifest` giữ nguyên mục, bao gồm size, scale hoặc preset nếu có. Không thay số trong manifest bằng số quét được. Không có mục tương ứng thì các trường là `null`. |
| `md5`, `md5After`, `errors`, `needsDecompression` | Chụp md5 mọi GLB trước khi phân tích metadata của mỗi game, kiểm lại buffer khi đọc và hash lại toàn bộ GLB sau khi phân tích. Mỗi mục giữ hai hash để kiểm lại được; lỗi và dữ liệu thiếu không bị bỏ qua. |

## Hình học và giới hạn

Đọc header GLB 12 byte, JSON chunk và BIN chunk trực tiếp; không giải nén meshopt/Draco. Count accessor vẫn dùng được khi nén. Với POSITION số nguyên có `normalized: true`, đổi min/max về miền chuẩn hóa trước khi áp ma trận. Áp `parentWorld × local`, trong đó local là `matrix` hoặc `T × R × S`, biến đổi đủ tám góc hộp rồi hợp các hộp. Kích thước là quy ước mét của glTF, không suy ra kích thước vật thật từ bản gốc chưa chuẩn cỡ.

Theo phiếu, luôn đo **scene 0**, kể cả khi trường `scene` trỏ scene khác; trường hợp đó có cảnh báo. Đây là hộp ở transform tĩnh: không chạy clip, skinning, morph target hoặc instance GPU. Hộp xoay có thể rộng hơn hộp ôm sát các đỉnh; chưa đủ để kết luận va chạm hoặc hướng mặt model. Báo cáo chỉ kiểm dữ liệu, không chứng nhận hình ảnh hay chất lượng khi chạy game.

Thứ tự nối nguồn: `SOURCES.files[*].usedBy`, cùng id, bản `standIn` được khai báo trong `notMadeYet`, đường dẫn GLB được ghi rõ trong ghi chú `noOriginalOnThisMachine` của đúng id, rồi tên file duy nhất. Bước tên file chỉ gộp các thư mục nguồn thành dấu gạch nối và bỏ tiền tố `ship-NN-`; không so gần đúng, không chọn khi nhiều ứng viên. Khi nối `standIn`, giữ `requested` và nguyên `reference` để không nhầm bản thay thế với bản gốc còn thiếu.

## Kiểm chứng

Test dựng GLB hoàn toàn trong RAM để kiểm scale 2, ma trận/TRS cha con, quay, scale âm, số nguyên chuẩn hóa, scene và mesh dùng chung, ba mode tam giác, thiếu bounds, thời gian clip, header ảnh và nối nguồn. Không tạo fixture media trên đĩa.

Sáu bản gốc thật được đếm theo hai cách: bộ quét dùng accessor count; bộ kiểm độc lập tự đọc JSON/BIN và từng bộ ba index dựa trên độ dài bufferView, đồng thời kiểm index nằm trong số đỉnh. Có ít nhất một file của mỗi game và đủ bốn số chuẩn Dragon Hold. Test còn đối chiếu danh sách GLB, trường bắt buộc, byte, nguyên mục manifest, nguồn nối và md5 của mọi mục trong ba sổ với file hiện tại.

Báo cáo của lượt thực hiện nằm ở [`docs/codex-queue/025-report.md`](../../../docs/codex-queue/025-report.md). Không có build, dev server hay test của game trong quy trình này.
