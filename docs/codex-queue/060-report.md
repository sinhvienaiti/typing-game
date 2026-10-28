# Phiếu 060 · Thư viện tài sản · AL-09: lõi tìm kiếm và câu tìm vàng

Ngày 28/10/2026, repo cha trên Mac mini M4. Đã đọc thiết kế §5.2, §5.6, phần từ vựng §3.6 và lược đồ §4.1–4.2; đọc đầu ra AL-07, AL-08 và dùng lại hàm nối dữ kiện AL-07. **Hoàn tất K1–K4 và cả tám kiểm riêng.**

## File tạo

| Đường dẫn | Nội dung |
|---|---|
| `tools/asset-library/lib/search.mjs` | Lõi thuần dùng chung cho Node và trang; chuẩn hóa, đồng nghĩa, từ liên quan, phạm vi từ Việt, xếp hạng và toàn bộ bộ lọc §5.2. |
| `tools/asset-library/test/search.test.mjs` | Kiểm trọng số, bộ lọc, trạng thái, phạm vi từ Việt, nhúng VM, tính bất biến, mục lục thật, tốc độ và lớp bọc fs. |
| `tools/asset-library/test/fixtures/catalog-small.json` | 15 thẻ mẫu công khai/giả lập, gồm model có runtime, âm thanh và các trạng thái cần kiểm. |
| `library/test/queries.json` | 7 câu tìm vàng; mỗi dòng có đúng `query`, `filters`, `mustInclude`, `topN`. |
| `docs/codex-queue/060-report.md` | Báo cáo này. |

Không sửa file nào đã có từ phiếu khác.

## Cách dùng và quy tắc điểm

```js
import { createSearch, search } from './tools/asset-library/lib/search.mjs';

const index = createSearch(catalog, { taxonomy });
const rows = index.search('chòi', { type: '3d', limit: 6 });
// rows: [{ card: thẻ_gốc, score: điểm_tìm }]
// Một lượt tìm: search(catalog, query, filters, { taxonomy }).
```

Module không import bất kỳ thứ gì, không I/O hay biến toàn cục của Node/browser. Bên gọi truyền cùng JSON taxonomy vào cả Node và trang. Sau khi đổi catalog hoặc taxonomy, tạo lại index. Kết quả giữ tham chiếu tới thẻ gốc và không sửa đầu vào.

- Mỗi trường góp tối đa trọng số của nó: tên **5**, alias **4**, loại con **3**, loại **3**, nhãn **2**, đường dẫn/chú thích **1**. Một trường chỉ khớp từ liên quan góp **một nửa** trọng số. Nhiều từ hoặc alias lặp trong cùng trường không nhân điểm. Câu nhiều từ lấy các trường khớp bất kỳ từ nào; không bắt buộc khớp mọi từ.
- Cộng **1** khi shipped/pass, cộng **0,5** khi có runtime, trừ **0,5** khi provisional. Hòa điểm ưu tiên loại/loại con hợp taxonomy, sau đó uid. Quy tắc này được kiểm riêng; không có ưu tiên theo uid hay tên món cụ thể.
- Thẻ thiếu tên dùng đoạn cuối uid làm tên dự phòng. Không ghi tên đó vào catalog.
- STOP được đối chiếu trực tiếp với mã tripo-match trong test. Cụm nhiều từ được nhận trước khi tách thành từ đơn; giữ phân biệt `gõ`/`gỗ` khi nhận đồng nghĩa rồi mới bỏ dấu. `cau`/`da` không dấu chỉ dịch ở phạm vi `viTokens` đã khai.
- `3d` và `model3d` cùng lọc model. Bộ lọc nhận khóa CLI kebab-case, cùng các dạng `subkind`, `usedBy`, `minScore`, `maxTris`. Các trục kết hợp AND; `tag`, `biome`, `has`, `used-by` dạng mảng yêu cầu đủ các giá trị; các lựa chọn loại/trạng thái cùng trục dùng OR.
- `min-score` lấy điểm đúng loại media; thiếu điểm bị loại. `max-tris` ưu tiên high runtime, rồi medium, rồi original; thiếu số đo bị loại. Kiểm cả trường hợp chỉ có số đo trong `files[].glb`, medium được liệt kê trước high và file bị loại chứa GLB.
- `all` mở trạng thái ẩn, không tự mở `requested`. Thẻ private được xem; lõi này không quyết định quyền chép. Đường dẫn file bị loại không tham gia chấm điểm hoặc kiểm khả năng.

## Mục lục thật dùng để kiểm

Catalog chung hiện có **2.936 thẻ** hình/3D, chưa nhận dữ kiện AL-07 hoặc âm AL-08. Test đọc `library/out/doc-facts.json`, dùng đúng `mergeDocFacts()` đã có để nối trong RAM, rồi gộp **1.849 thẻ** của `library/out/audio-catalog.json` theo uid. Kết quả là **4.785 thẻ thật**; không sửa dữ kiện, không thêm thẻ giả vào phép đo, không chạy lại scanner, không ghi `library/out`.

Đây là ảnh chụp đầu ra của các phiếu trước. Người nối CLI/trang cần dùng catalog đã được quét lại sau AL-07/08 để nhận cùng dữ kiện; việc quét lại không thuộc phạm vi ghi của phiếu này.

## K1–K4

| Kiểm | Kết quả |
|---|---|
| K1 · Chỉ ghi chỗ được ghi | **ĐẠT.** Test bọc fs callback, sync, promises, stream và open có cờ ghi trước khi nạp lõi; đồng bộ các export Node. Tất cả lượt trên mẫu, VM và catalog thật có **0 lời gọi ghi**. Test không tạo file tạm. Các thay đổi thủ công chỉ là 5 file được phép ở trên. |
| K2 · Cây Git | **ĐẠT.** So status đầu/cuối chỉ thêm 5 file của phiếu; `library/test/` là cách status gộp `queries.json`. Dòng game giống hệt; không ghi vào game. Hai bản đầy đủ và hai bản `games/` ở dưới. |
| K3 · Vùng cấm | Không sinh file dưới out hoặc thumbs nên điều kiện sinh file **không áp dụng**. Kiểm thêm `grep -rlE` trên `library/out`: **0 file khớp**, stdout rỗng, exit **1**. `library/.thumbs` chưa tồn tại. Không đọc/ghi vùng cấm, không duyệt media hay mã nguồn game. |
| K4 · Test | **ĐẠT.** `node --test tools/asset-library/test/search.test.mjs`: **20 pass, 0 fail, 0 skip**, exit **0**, **2.384,27 ms**. `node --check` trên lõi và test đạt; kiểm khoảng trắng trên cả 5 file đạt. |

Test nhúng bỏ từ khóa export rồi chạy đúng mã lõi trong VM trống, không có Node hay DOM. **15 tổ hợp** câu tìm/bộ lọc trả JSON giống hệt Node. Đây là kiểm mã có thể nhúng, không phải nghiệm thu bằng trình duyệt; phiếu cấm trình duyệt/server.

## Tám kiểm riêng

| Kiểm | Số đo và kết quả |
|---|---|
| 1 · `hut --type 3d` | **ĐẠT.** `choi-canh-doi` hạng **1** (14); `herb-hut` hạng **2** (11,5); `nha-rai-da` hạng **3** (8,5); `barracks-kit-l2` hạng **4** (6). |
| 2 · `chòi` và `choi` | **ĐẠT.** So toàn bộ kết quả và điểm bằng nhau, cả khi không lọc và khi type=3d. |
| 3 · `jetty --type 3d` | **ĐẠT.** `typing-defense:landmarks/cau-tau` hạng **1**, điểm **14**. |
| 4 · `bridge` | **ĐẠT.** `dragon-hold:props/pine-river/bridge-old` hạng **1** (14,5); `typing-defense:landmarks/cau-go` hạng **3** (14). |
| 5 · `rock --biome pine-forest` | **ĐẠT.** `river-stones` hạng **1** (14,5), `rock-boulder` hạng **2** (14,5), `rock-slab` hạng **5** (11,5). |
| 6 · `wood click --type audio` | **ĐẠT.** `kenney:impact-sounds/Audio/impactWood_light` hạng **3** (15); trước nó là click (16) và impactWood_heavy (15). |
| 7 · Ẩn bản loại | **ĐẠT.** Mặc định không có **1.162** thẻ draft/review/rejected, trong đó **6 rejected**; `all` mở đủ. Requested vẫn cần cờ riêng. Mẫu còn kiểm hidden, AudioLab work và status filter không vượt qua cổng. |
| 8 · p95 dưới 300 ms | **ĐẠT.** **4.785 thẻ**: p95 tìm ấm **1,65 ms / 140 lượt**; p95 lạnh gồm tạo index + tìm **97,35 ms / 21 lượt**. Lượt tạo index ban đầu **96,94 ms**. |

Các số trên lấy từ lượt test cuối, sau khi bổ sung kiểm chọn số tam giác high thay vì medium khi chỉ có metadata từng file.

## Phần bỏ qua và việc cần chủ dự án xem

- Không bỏ qua kiểm bắt buộc nào. Không cần quyền AudioLab, ffprobe, magick, Blender hay sinh hình/âm; chỉ đọc đầu ra JSON đã có.
- Không quét lại catalog thật vì không được ghi out; không sửa scanner, taxonomy hay CLI/trang của phiếu sau. Khi nối CLI/trang, cần truyền taxonomy và cập nhật catalog chung sau AL-07/08 như mô tả trên.
- Cần lưu ý cách tính điểm mỗi trường một lần và quy tắc hòa điểm đã ghi rõ. `wood click` hiện đưa heavy trước light vì bằng điểm; phiếu chỉ yêu cầu light trong ba đầu. Tuyển chọn âm theo cảm nhận nằm ngoài lõi tìm kiếm.
- Không dùng mạng, trình duyệt, server, build/test game, lệnh media hay lệnh Git có ghi.

## Git status lúc đầu

```text
 M games/typing-survival
 M tools/asset-library/scan.mjs
?? .claude/launch.json
?? TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md
?? docs/codex-queue/035-report.md
?? docs/codex-queue/036-report.md
?? docs/codex-queue/057-report.md
?? docs/codex-queue/058-report.md
?? docs/codex-queue/059-report.md
?? docs/tools/map-factory/spike-l2-cau.md
?? shared/shared
?? tools/asset-library/doc-facts.mjs
?? tools/asset-library/lib/joins.mjs
?? tools/asset-library/scan-audio.mjs
?? tools/asset-library/test/doc-facts.test.mjs
?? tools/asset-library/test/scan-audio.test.mjs
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
?? docs/codex-queue/059-report.md
?? docs/codex-queue/060-report.md
?? docs/tools/map-factory/spike-l2-cau.md
?? library/test/
?? shared/shared
?? tools/asset-library/doc-facts.mjs
?? tools/asset-library/lib/joins.mjs
?? tools/asset-library/lib/search.mjs
?? tools/asset-library/scan-audio.mjs
?? tools/asset-library/test/doc-facts.test.mjs
?? tools/asset-library/test/fixtures/catalog-small.json
?? tools/asset-library/test/scan-audio.test.mjs
?? tools/asset-library/test/scan-joins.test.mjs
?? tools/asset-library/test/search.test.mjs
```

## git status --porcelain games/ · lúc đầu

```text
 M games/typing-survival
```

## git status --porcelain games/ · lúc cuối

```text
 M games/typing-survival
```
