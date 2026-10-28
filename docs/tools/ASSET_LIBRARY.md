# Thư viện tài sản: tìm và dùng lại hình, model 3D, âm thanh giữa các game (28/10/2026)

**Đọc cho ai:** chủ dự án; Claude và Codex mỗi khi cần một hình, một model hay một âm thanh, cũ hay mới.

**Nguồn:**
- Ba bản khảo sát chỉ đọc sáng 28/10/2026 (khoảng 09:00): hình và 3D, âm thanh, công cụ. Số liệu mục 2 lấy từ đó.
- Claude đo lại một số chỗ lúc 12:10 cùng ngày. Chỗ đó ghi "(đo 12:10)". Một vài khoảng trống của buổi sáng đã được đóng trong ngày.
- Ba bản thiết kế: "tìm trước" (find-first), "ít xáo trộn" (migrate-light), "nhà chung" (library-home), và hai bài chấm. Hai giám khảo cùng chọn "tìm trước". Tài liệu này là bản đó, ghép ý tốt của hai bản kia, sửa mọi lỗi giám khảo nêu (bảng ở mục 11).
- Luật dự án: `docs/games/DEPLOY_INDEPENDENCE.md`, `docs/games/MEDIA_AND_MODELS.md`, `docs/games/ART_ACCEPTANCE.md`, `docs/games/NAMES_EN.md`, `docs/games/AUDIO_PIPELINE.md`, `docs/tools/MAP_FACTORY.md`.

**Trạng thái:** bản thiết kế, chờ duyệt. Phiếu làm việc ở `TICKETS.md` cùng thư mục (mã AL-01 … AL-25). Không đụng Tu Tiên: mọi công cụ ở đây chặn `games/immortality-cultivation`, `docs/games/tu-tien` và bản chép Tu Tiên trong thư mục handoff.

## Tóm tắt

- **Kết luận: lập mục lục tại chỗ, chép khi dùng lại.** Không dời file nào. Không lập kho media thứ hai, trên ổ đĩa hay trên Drive. Một mục lục (catalog) sinh tự động trỏ tới file ở đúng chỗ hôm nay.
- **Một thẻ cho một món.** Hôm nay Herb Hut là 32 file trong art-src (6 thư mục) cộng 2 file runtime. Trong thư viện nó là **một thẻ** "Herb Hut", file xếp theo vai trò: ảnh, ảnh gửi Tripo, GLB gốc, GLB đã xử lý, hai bậc runtime, icon. Prompt và 9 bản bị loại nằm trong phần chi tiết, mặc định ẩn.
- **Ba cách tìm, cùng một kết quả:**
  - trang `library/out/catalog.html`: ảnh nhỏ, bộ lọc, nghe thử; mở bằng Finder, không cần server;
  - thư mục Finder `library/browse/building/hut/`: toàn liên kết tượng trưng, 0 byte;
  - lệnh `pnpm lib:find chòi`, có `--json` cho agent.
- **Gõ tiếng Anh hay tiếng Việt đều ra.** "hut", "chòi", "choi", "lều" cùng ra một nhóm. Tên hiện cho người xem là tiếng Anh; tiếng Việt là dòng chú thích nhỏ (AGENTS.md "In-game names").
- **Dùng lại = `pnpm lib:copy`.** Lệnh chép file vào game đích lúc làm game (clone APFS, gần 0 byte), rồi ghi `library.lock.json` ở **gốc** repo game đích. Lệnh `check` của game kiểm md5 từng file đã chép. Lúc build và lúc chạy, không game nào đọc file của game khác hay của thư viện.
- **Không thứ gì riêng tư vào Git.** Repo cha công khai. Thẻ của nhạc riêng (`shared/music`) và tiếng Dota chỉ nằm trong thư mục bị Git bỏ qua.
- **Tìm trước khi làm.** Mọi yêu cầu vẽ, Tripo hay âm thanh mới phải dẫn kết quả `lib:find` hoặc `lib:check --request`. Ví dụ hôm nay: đợt Tripo dot3 của Rồng xin Wooden Jetty, Reed Clump, Wildflower Clump, trong khi Lời Gọi đã có `cau-tau` (cầu tàu, 3D 9 điểm), `meadow/reed-clump` và `meadow/wildflowers`.
- **Việc:** Codex 19 phiếu nhỏ, mỗi phiếu dưới một giờ. Claude 5 phiếu (đóng khoảng trống Drive; duyệt, commit và tuyển chọn tên; thử trang; thí điểm Tuyến Cuối; nối quy trình). Chủ dự án khoảng 15 phút: thử tìm trong một phút, và hai quyết định.

---

## 1. Mục tiêu

Chủ dự án (28/10, dịch ý): "Ta chưa thiết kế hình ảnh để dùng lại theo một cấu trúc. Ví dụ sang game khác cần hình chòi hay nhà để dùng lại, tôi sẽ không biết tìm ở đâu. Nên thiết kế cấu trúc hình ảnh và âm thanh để sau dễ tìm, dễ dùng lại."

Hôm nay, câu "ta có những chòi, nhà nào?" không có chỗ trả lời:
- Mục lục duy nhất (sổ model của Map Factory) tìm nhãn `house` chỉ ra **một** món: `herb-hut` của Rồng.
- Lời Gọi có khoảng 70 GLB loại công trình. Chúng nằm rải trong `buildings/`, `kits/`, `branches/`, `landmarks/`, `ruins/`, với id tiếng Việt (`choi-canh-doi`, `nha-rai-da`). Muốn thấy phải biết trước tên thư mục và id.
- Space không có nhà nào (chỉ `tower-*` khoa học viễn tưởng).

Thư viện phải trả lời các câu dưới đây, mỗi câu trong một phút:

| Câu hỏi | Gõ gì | Hôm nay phải làm gì |
|---|---|---|
| Ta có những chòi, nhà nào? | `pnpm lib:find hut`, hoặc gõ "chòi" trên trang | Biết tên thư mục từng game và id tiếng Việt |
| Có tiếng click gỗ cho menu không? | `pnpm lib:find "wood click" --type audio` | Không có chỗ tìm; âm thanh nằm ở 4 nơi rời nhau |
| Đá của vùng rừng thông? | `pnpm lib:find rock --biome pine-forest` | Mở `props/pine-river/` và đoán |
| Có cầu tàu chưa, trước khi tiêu credit Tripo? | `pnpm lib:check --request "wooden jetty"` | Không ai thấy `cau-tau` của Lời Gọi |
| Model nhẹ, có clip, dùng ngay? | `pnpm lib:find --type 3d --max-tris 5000 --has clips` | Đọc manifest từng game |
| File nào chưa lên Drive? | `pnpm lib:check --drive` | So tay `media.md5` với ổ đĩa |
| Ai đang dùng file này, đổi thì vỡ gì? | `pnpm lib:show <mã>` | grep mã nguồn |

Ngoài phạm vi:
- Tu Tiên (đang dừng).
- Xóa file. Công cụ chỉ báo cáo bản trùng; chủ dự án tự xóa nếu muốn (mục 10).
- Đổi chữ trong game. Tên tiếng Anh trong thư viện là đề xuất. Tên trong game đổi ở lượt đặt tên riêng của từng game (phiếu 050, 051 đang chạy).

---

## 2. Hiện trạng (28/10/2026)

### 2.1 Ở đâu, bao nhiêu

| Nơi | 2D | 3D | Âm thanh | `media.md5` |
|---|---|---|---|---|
| Rồng Giữ Ải `games/dragon-hold` | art-src 881 ảnh (580 MB); public 0 ảnh | 24 GLB gốc; 24 GLB đã xử lý; public 54 GLB (24 model × 2 bậc + 6 bản Draconis chép từ Space) | 0 file; âm tổng hợp trong mã; `src/audio/catalog.ts` có 83 id chờ file | sáng 1.138 dòng; 1.680 (đo 12:10), đã có 48 GLB M0b và 48 GLB đã xử lý |
| Lời Gọi `games/typing-defense` | art-src 528 ảnh (785 MB); public 1 ảnh | art-src/3d 156 GLB lúc sáng, 157 (đo 12:10); 38 GLB đã xử lý (298 MB); public 68 GLB | 0 file | sáng 914; 1.278 (đo 12:10), đã có đợt Tripo 2 |
| Tuyến Cuối `games/typing-survival` | 14 ảnh (16 MB) | 0; lúc chạy mượn model Space qua `/assets/space-typing/models/manifest.json` | 0 | 26 |
| Space `games/space-typing` | art-src 675; public 536; `src/assets` 498 | art-src/3d 205 GLB gốc (1,8 GB); `art-src/models` 3,3 GB, trong đó `raw/` 172 GLB, 160 là bản sao byte của `3d/` | 116 file trong Git, khóa bằng `tools/audio-lab/build/legacy-audio.json` | 1.509, 0 dòng âm thanh |
| Handoff `typing-game-handoff-2026-10-25` | tripo-upload 65 PNG; dot2 98; dot3 8 | tripo-upload 55 GLB; dot2 86; dot3 0 | — | không có; 627 MB là bản sao của art-src |
| `~/AudioLab` (ngoài repo) | — | 1,7 GB việc 3D lẫn vào (`_td-models`, `_glb-map`) | thư viện CC0 1.859 file có `index.json`; `work/` 391 master chưa ai duyệt | không bao giờ lên Drive; 20 GB |
| `shared/music` | — | — | 193 bài, 458 MB, 544,7 phút | `media/private.md5` (riêng, không vào Git) |

Ổ đĩa: 228 GB. Sáng 28/10 còn 41 GiB trống; sau khi dọn ảnh test còn 62 GiB (đo 12:10).

### 2.2 Vì sao khó tìm

1. **Không có mục lục chung cho 2D và âm thanh.** Sổ model Map Factory (`tools/map-factory/registry/out/assets.<game>.json`, phiếu 025) chỉ có 3D của ba game, chụp tối 27/10, thiếu đợt Tripo 2 của Lời Gọi. Nhãn lấy từ 30 từ cố định, nên 110/139 món Lời Gọi và 496/583 món Space không có nhãn.
2. **Cùng một thứ, mỗi game một tên thư mục.** Rồng: `houses/`, `props/pine-river/`. Lời Gọi: `buildings/`, `kits/`, `branches/`, `landmarks/`, `ruins/`, `scenery/<vùng>/`. Space: theo thế giới (`g01`…`g10`). Ngay trong một model, loại cũng đổi theo bước: `art-src/houses` → `art-src/models/props` → `public/.../m0b/props`.
3. **id lẫn tiếng Việt.** `choi-canh-doi`, `nha-rai-da`, `cau-tau`, `trau`, `cuong-thi`. Gõ "hut", "house", "jetty" không ra. Tên tiếng Anh chỉ có trong `NAMES_EN.md`, khóa theo id trong mã, không theo file.
4. **Tên file Tripo là chú thích của Tripo** (`thatched+hut+3d+model (2).glb`). Nối với id chỉ nằm trong bảng `3D_IMPORT_2026-10-26/28.md` và trường `downloadedAs` (40 trên 71 dòng Lời Gọi lúc sáng, 0 ở Rồng).
5. **Bản đạt và bản loại nằm chung.** Hậu tố `.tripo`, `.rejected-012b`, `.v1`, `.try1`, `.alpha`, `.flat`, `.256`… Không gì đánh dấu bản chính. Rồng có 507 file *rejected* (102 MB) nằm ngay cạnh ảnh đạt. `-v1` là "biến thể" ở `scenery/` của Lời Gọi, nhưng là "bản nháp cũ" ở chỗ khác. Điểm chấm nằm trong README, IMAGE_AUDIT, ART_REPLACE_LATER, không cạnh file.
6. **Sổ lệch ổ đĩa.** Lúc sáng `SOURCES.json` Lời Gọi có 71 trên 156 GLB, `usedBy` trống cả 71. `m0b/manifest.json` của Rồng không có trong Git lẫn Drive (đo 12:10: vẫn vậy; JSON không phải đuôi media, và `public/assets` bị bỏ qua cả ở `.gitignore` lẫn `.git/info/exclude`). `media.config.json` khai `models/manifest.json` cho Rồng, file đó không tồn tại.
7. **Âm thanh rời rạc.** 4 nơi không nối nhau: Space (116 file), AudioLab `work/` (391 master chưa duyệt), thư viện CC0 của AudioLab (1.859 file), nhạc riêng (193 bài). 30 file Space không có nguồn từng file. Họ âm của AudioLab đặt bằng chữ Việt không dấu (`phim-ui`, `trung`, `no`, `nen`). Thư mục âm Space đặt theo nơi dùng đầu (`duel/war`, `dragon/`), không theo nội dung.
8. **Làm lại thứ đã có.** dot3 ở trên. Không ai thấy món của game kia.
9. **Bản trùng tốn chỗ.** So md5: GLB thừa 2,19 GB; ảnh trên 100 KB thừa 1,33 GB. Lớn nhất: Space `art-src/models/raw` (~1,75 GB), handoff (627 MB), `tools/art-normalize/.tmp` (1,5 GB).
10. **Chép giữa game không để lại dấu.** 6 bản Draconis của Rồng giống byte Space, nhưng sổ model ghi "licence unknown, original-not-found". `models:prepare --import` không ghi game nguồn.

### 2.3 Thứ có sẵn, dùng lại được ngay

| Có sẵn | Dùng làm gì |
|---|---|
| `tools/map-factory/registry/scan-assets.mjs` (`walkFiles`, `inspectGlb`, `imageHeader`, chỉ dùng Node) | Đọc GLB: mét, tam giác, skin, clip. Thư viện gọi hàm này, không viết bộ đọc GLB thứ hai. Kết quả ở `registry/out/` dùng lại khi md5 khớp |
| `games/<g>/art-src/3d/SOURCES.json` + luật gương `art-src/<p>/<n>.png ↔ art-src/3d/<p>/<n>.glb` | Nối ảnh với GLB |
| `media.md5` từng game + `.cache/media-hash.json` (7.071 dòng md5 và sha256, khóa theo cỡ và mtime) | md5 là mã nội dung; biết file đã lên Drive chưa |
| Preset model (`dragon-hold-m0b.json` 24, `typing-defense-static.json` 30, Space 170) | Cỡ mét, góc xoay, tâm, socket |
| `pnpm models:prepare --import <manifest> --only <kind>/<id>` | Đường chép model đóng gói sang game khác (đã dùng cho Draconis) |
| `tools/tripo-match/match.mjs` (`SYNONYMS`, `unaccent`, `tokenize`, chấm hình khối và tam giác) | Từ đồng nghĩa Việt–Anh; so món giống nhau |
| Bảng tài liệu: NAMES_EN (148 dòng), 3D_REQUESTS, 3D_IMPORT ×2, ART_REPLACE_LATER, IMAGE_AUDIT, `INDEX.md` của handoff | Tên, điểm, mức, file Tripo, đọc máy được |
| `.prompt.txt` cạnh ảnh (Rồng 576, Lời Gọi 372, Tuyến Cuối 11) | Prompt từng file |
| `~/AudioLab/libraries/index.json` + `SOURCES.jsonl` | Mục lục âm CC0 có sha256, giấy phép, họ tiếng Anh (`ui/click`, `impact/wood`). Đã tìm lại nguồn của 29 trên 116 file Space |
| `tools/audio-lab/specs/taxonomy.py` (9 họ, 16 nhóm) | Từ vựng âm thanh, chỉ cần thêm nhãn tiếng Anh |
| Manifest âm v2 + `FileBank` của Rồng (`src/audio/bank.ts`) | File chép vào thay âm tổng hợp theo từng id, không sửa mã |
| `scripts/sync-game-kit.mjs` + `src/kit/verify-kit.mjs` | Mẫu "chép có ghim + băm + kiểm trong `check`" cho sổ chép của game |

---

## 3. Cấu trúc và cách đặt tên

### 3.1 Tám nguyên tắc

1. **Lập mục lục tại chỗ.** File ở yên chỗ cũ. Mục lục sinh từ ổ đĩa và từ sổ có sẵn. Làn đang chạy không thấy gì thay đổi.
2. **Chép khi dùng lại, có ghi nguồn.** Game đích nhận bản sao của chính nó (DEPLOY_INDEPENDENCE luật 3, 4). Sổ chép nằm ở gốc repo game đích và vào Git của game đó.
3. **md5 là danh tính.** Cùng md5 ở hai chỗ là cùng một món. Nhờ vậy gom bản sao, biết "ai dùng", và đổi tên không làm mất dấu.
4. **Một từ vựng tiếng Anh, có từ đồng nghĩa tiếng Việt.** Thư mục cũ của từng game được **ánh xạ** sang từ vựng, không đổi tên.
5. **Chữ trong Git, media ngoài Git.** Từ vựng, dòng tuyển chọn, mã, `CATALOG.md` (chỉ thẻ công khai) vào Git. Catalog đầy đủ, trang, ảnh nhỏ, thư mục Finder là sản phẩm sinh ra, Git bỏ qua.
6. **Riêng tư không vào Git.** `.gitignore` của repo cha đã giữ `media/private.md5` ngoài Git vì nó liệt kê tên nhạc có bản quyền. Thẻ nhạc riêng và tiếng Dota chỉ nằm trong `library/out/` và `library/private/`, cả hai bị bỏ qua.
7. **Không thêm gigabyte.** Không chép media vào thư viện. Chép vào game dùng clone APFS. Ảnh nhỏ có trần 150 MB.
8. **Chịu được làn đang chạy.** Bộ quét chỉ đọc `games/**`. File biến mất giữa chừng là cảnh báo, không là lỗi (thư mục `art-src/models` của Rồng từng biến mất rồi hiện lại lúc 08:59).

### 3.2 Thư mục

```text
library/                                 repo cha, chỉ chữ
  .gitignore                             out/  .thumbs/  .cache/  browse/  browse.new/  private/
  README.md                              tiếng Việt, một trang: tìm, xem, chép, kiểm
  taxonomy.json                          từ vựng: loại, nhãn, vùng, phong cách, trạng thái, từ đồng nghĩa, ánh xạ thư mục
  sources.json                           gốc quét, danh sách cấm, thư mục bỏ qua
  licences.json                          khóa giấy phép → commercialOk, attribution, private, notForRelease
  curated/dragon-hold.jsonl              dòng tuyển chọn, một file mỗi game (làn song song không đụng nhau)
  curated/typing-defense.jsonl  curated/typing-survival.jsonl  curated/space-typing.jsonl
  curated/audio-libraries.jsonl          Kenney, VCSL, VSCO-2-CE (CC0, tên công khai)
  imports.jsonl                          sổ mọi lần lib:copy, chỉ thêm dòng
  test/queries.json                      câu tìm vàng (hut, chòi, jetty, bridge, pine rock, wood click…)
  CATALOG.md                             sinh ra, CÓ trong Git: thẻ công khai đã duyệt, một bảng mỗi loại
  out/        (bỏ qua)                   catalog.json, catalog.data.js, catalog.html, doc-facts.json, scan-report.md
  .thumbs/    (bỏ qua)                   <md5>.webp 256 px; <sha256>.wave.png cho âm
  .cache/     (bỏ qua)                   hash.json: md5 + sha256 theo cỡ và mtime
  browse/     (bỏ qua)                   cây thư mục cho Finder, toàn liên kết tượng trưng
  private/    (bỏ qua)                   ghi chú tay cho nhạc riêng, nếu sau này cần
tools/asset-library/                     mã (Git); chỉ dùng Node, không gói ngoài
  lib/taxonomy.mjs  grammar.mjs  audio-header.mjs  search.mjs
  scan.mjs  scan-audio.mjs  doc-facts.mjs  seed-curated.mjs  thumbs.mjs  page.mjs  browse.mjs  catalog-md.mjs
  find.mjs  show.mjs  play.mjs  copy.mjs  copy-audio.mjs  check.mjs
  test/
shared/game-kit/tools/verify-library.mjs kiểm sổ chép trong `check` của game; chép vào game qua kit:sync
games/<g>/library.lock.json              repo game, CÓ trong Git: những gì game này chép từ nơi khác
```

Lệnh ở `package.json` gốc: `lib:scan`, `lib:thumbs`, `lib:page`, `lib:browse`, `lib:build` (scan → thumbs → page → browse → CATALOG.md), `lib:find`, `lib:show`, `lib:play`, `lib:copy`, `lib:check`, `lib:test`.

Vì sao sổ chép ở gốc game: cả bốn game có `art-src/*` trong `.gitignore`, chỉ cho `art-src/3d/SOURCES.json` qua. Một file `art-src/LIBRARY_IMPORTS.json` sẽ lặng lẽ không bao giờ vào Git. `library.lock.json` ở gốc thì Git theo dõi bình thường.

### 3.3 Mã thẻ (uid)

Mã thẻ sinh máy móc từ đường dẫn, không phải cấp phát:

1. **Ảnh và GLB trong art-src:** `<game>:<p>/<n>`, với `art-src/<p>/<n>.png ↔ art-src/3d/<p>/<n>.glb` (luật gương của SOURCES.json). Khi trường `image` của SOURCES khác luật gương thì `image` thắng (ca đã biết: Space `ship-NN-<id>-2d.png ↔ ship-NN-<id>.glb`).
2. **GLB đã xử lý và GLB runtime** gắn vào thẻ qua trường `source` của preset (`"props/herb-hut": {"source": "houses/herb-hut.glb"}`) và khóa manifest (`props/herb-hut`). Thư mục runtime (`m0b/props`) không còn ảnh hưởng việc tìm. GLB đã xử lý không có nguồn thì thành thẻ riêng `<game>:models/<kind>/<n>`.
3. **Thứ khác trong game** (ảnh chỉ có ở runtime, âm Space): đường dẫn từ gốc game, bỏ đuôi. Ví dụ `space-typing:public/assets/audio/duel/war/railgun`.
4. **Thư viện ngoài:** đường dẫn dưới `~/AudioLab/libraries/<lib>/`, bỏ đuôi và bỏ số biến thể. Ví dụ `kenney:interface-sounds/Audio/click`.
5. **Nhạc riêng:** `music:<thư mục>/<tên>`. Chỉ có trong `library/out/`. Không bao giờ chép được.
6. **Handoff:** file trùng md5 với file trong game thành **bản sao** trên thẻ đó. File không trùng thành thẻ nháp `handoff:<path>`. Nhờ vậy một GLB Tripo vừa tải về mà chưa ai import vẫn hiện khi tìm.
7. **Dạng ngắn** `<game>:<id>` (đoạn cuối) dùng được khi duy nhất. Đây là dạng mà file kit của Map Factory (§4.5) dùng, nên bản đồ và thư viện chung một cách gọi.

### 3.4 Bản sao và file chính

Cùng md5 ở nhiều chỗ thì thẻ có danh sách `copies[]` kèm loại chỗ: `same-folder`, `game`, `handoff`, `models-raw`, `worktree`, `dist`.

File chính (master) chọn theo thứ tự:
1. thư viện ngoài;
2. art-src gốc;
3. `art-src/models`;
4. `public`;
5. `src/assets`;
6. handoff hoặc `raw`.

Hệ quả:
- Space `art-src/models/raw` (160 GLB) và GLB handoff gộp vào thẻ như bản sao, không thành kết quả riêng.
- 6 bản Draconis của Rồng hiện `copyOf space-typing:…`.
- `wooden-jetty.try1.png` trùng md5 với `wooden-jetty.png` (lượt try1 được chọn rồi chép thành tên chính). Nó là bản sao, không bị coi là bản nháp.

Mỗi vai trò trên thẻ có đúng **một** file chính (`canonical`). Mặc định là tên gốc ngoài `_review`. Dòng tuyển chọn ghi đè được (ví dụ `typing-defense:buildings/barracks` → `barracks-v2.png`). `lib:check` báo khi một vai trò có hai file chính.

### 3.5 Vai trò file (ngữ pháp hậu tố)

| Mẫu | Vai trò | Hiện ở |
|---|---|---|
| `art-src/<p>/<n>.png` | concept (ảnh 2D chính) | thẻ |
| `<n>.tripo.png` | tripo-source (ảnh gửi Tripo) | thẻ |
| `<n>_front` / `_back` / `_left` [`.alpha`/`.flat`] `.png` | multiview | chi tiết |
| `.alpha`, `.flat`, `.padded`, `.seamless`, `.trim`, `.crop`, `.coal`, `.fix` | derivative (sinh lại được bằng art-normalize) | chi tiết |
| `.v<N>`, `.try<N>` (dấu chấm), md5 khác file chính | draft | ẩn |
| `-v<N>` (gạch nối) trong thư mục có cờ `hyphenVariants` (Lời Gọi `scenery/**`) | biến thể a/b của cùng thẻ | thẻ |
| `.rejected-<phiếu>` ở bất kỳ đâu trong tên | rejected (giữ mã phiếu) | ẩn; md5 vào `rejectedMd5` |
| `icons/normalized/<n>.256.png`, `.64.png` | icon-256, icon-64 | thẻ |
| `ui/icons/<n>.png` cùng game | icon (nối theo id) | thẻ |
| `<stem>.prompt.txt` | prompt của file có cùng stem | chi tiết |
| `README*.md`, `.reports/*.json`, `.campaign3d-model-cache/*` | report | chi tiết |
| `art-src/3d/<p>/<n>.glb` | glb-original | thẻ |
| `tripo-spares/<n>.alt.glb`, `.r2.glb`, `*-old.*`, `*.raw-download-*` | glb-spare | chi tiết |
| `tripo-spares/<n>.r2-rejected.glb` | rejected | ẩn |
| `art-src/models/<kind>/<n>.glb` | glb-processed | thẻ |
| `public/…/<n>.high.glb`, `.medium.glb` | runtime-high, runtime-medium | thẻ |
| `_review/**`, `review-vs*/**`, `_from-downloads/**` | review | ẩn |
| Âm `_000`…`_004`, `_rr<N>`, `-<N>.ogg`, số cuối (`click1`) | biến thể của một bộ âm | thẻ |
| Còn lại | unknown, ghi vào báo cáo quét (trần 1 % số file) | chi tiết |

Ca thật phải qua test: `scenery/meadow/bamboo-clump-v1.v1.png` (bản nháp `.v1` của biến thể `-v1`); `herb-hut.tripo.rejected-012c.prompt.txt`; `tripo-spares/barracks-old.thatched-hut.glb`; Kenney `click_001..005` thành một thẻ `click` 5 biến thể.

### 3.6 Từ vựng (`library/taxonomy.json`)

**Loại (kind)**, tiếng Anh, có nhãn tiếng Việt cho menu:

| Nhóm | Loại |
|---|---|
| Hình và 3D | building, structure, nature, prop, character, creature, vehicle, weapon, projectile, item, trap, vfx, ui, ground, backdrop, motion |
| Âm thanh | ui, typing, reward, shot, impact, explosion, death, creature, voice, ambience, music, stinger, foley, movement |

**Loại con (subkind)**, ví dụ: building → house, hut, tower, barracks, farm, mine, keep, shrine, workshop, kit-part; structure → bridge, jetty, gate, fence, wall, lighthouse, well, dais, ruin, stairs; nature → tree, bush, rock, cliff, reed, flower, grass, stump, log, bamboo, waterfall, water.

**Nhãn (tags)**: từ tiếng Anh tự do nhưng phải nằm trong danh sách (ít nhất 120 từ, gồm 30 từ của `inferTags`): thatch, wood, stone, bamboo, stilts, lookout, healer, village, mossy, knock, dry, short…

**Vùng (biome)**: pine-forest, river, meadow, coast, rainforest, hill, village, space, any.

**Phong cách (style)**: câu hỏi đầu tiên khi dùng lại là "có hợp mắt game kia không".

| Phong cách | Của |
|---|---|
| `mythic-forest` | Rồng Giữ Ải |
| `viet-village` | Lời Gọi (cả `art-src/td` cũ trong Space) |
| `steel-station` | Tuyến Cuối |
| `sci-fi-space` | Space |
| `neutral` | Kenney UI và thư viện CC0 |

**Trạng thái (status)**: `shipped`, `pass`, `provisional`, `unscored`, `requested`, `draft`, `rejected`, `review`, `private`.

**Bước làm (pipeline)**, để lọc "có ảnh mà chưa có GLB": `concept-only`, `tripo-requested`, `glb-original`, `processed`, `runtime`.

**Từ đồng nghĩa**: một từ chỉ thuộc một nhóm. Gốc là `SYNONYMS` của tripo-match, thêm tiếng Việt có dấu và không dấu:
- hut = shack, cabin, cottage, lều, leu, chòi, choi
- house = home, nhà, nha
- jetty = dock, pier, wharf, cầu tàu, cau tau
- click = tap, tick, gõ, bấm
- wood = wooden, timber, gỗ, go
- buffalo = trâu, trau; dragonfly = chuồn chuồn, chuon chuon

**Từ liên quan** (cộng nửa điểm): hut ~ house, jetty ~ bridge, click ~ knock.

**Từ Việt theo thư mục.** Vài chữ Việt không dấu nhiều nghĩa: "cau" là cầu hay câu, "da" là đá hay da. Bảng ánh xạ chữ Việt → Anh chỉ áp ở thư mục được ghi: `cau` → bridge chỉ trong `landmarks/` và thư mục structure; `da` → stone chỉ trong `scenery/` và `landmarks/`.

**Ánh xạ thư mục (folderMap)**: mỗi thư mục cấp 1 (và cấp 2 khi thư mục tách đôi) của `art-src` và `art-src/3d` bốn game có một dòng. Test sẽ hỏng khi gặp thư mục chưa ánh xạ, nên thư mục mới không bao giờ lặng lẽ rơi khỏi kết quả tìm.

| Game | Thư mục | Loại |
|---|---|---|
| Rồng | `houses/` | building |
| Rồng | `props/pine-river/` (20 món) | theo từng món: bridge-old, wooden-jetty → structure; rail-fence, lantern-post → prop; còn lại → nature. Vùng pine-forest + river |
| Rồng | `enemies/ generals/ units/ traps/ vfx/ ground/ decals/ backdrops/ icons/ ui/` | creature, character, character, trap, vfx, ground, ground, backdrop, ui, ui |
| Lời Gọi | `buildings/ kits/ branches/` | building (kits → kit-part) |
| Lời Gọi | `landmarks/` (12) | theo từng món: choi-canh-doi, nha-rai-da → building; cau-tau, cau-go, cau-do, hai-dang → structure; vach-thac-bac, thac-ho-sut → nature |
| Lời Gọi | `ruins/`; `scenery/{meadow,coast,rainforest,shared}/` | structure/ruin; nature, vùng lấy từ thư mục con (`shared` → any), có cờ `hyphenVariants` |
| Lời Gọi | `workers/ helpers/ heroes/ units/`; `enemies/ bosses/ animals/`; `projectiles/ loot/ props/` | character; creature; projectile, item, prop |
| Space | `ships enemies bosses skills items heroes guides`; `gNN-*`; `icons/`; `td/` | vehicle, creature, creature, vfx, item, character, character; backdrop và prop vùng space; ui; `td/` là ảnh Lời Gọi cũ |
| Space âm | `sfx/kenney, duel/war, duel/sfx, dragon, ambient, stingers, music, src/assets/audio/ui` | theo từng món (thư mục đặt theo nơi dùng đầu) |
| Tuyến Cuối | `ui/` | ui |

**Họ âm AudioLab → tiếng Anh**: phim-ui → ui, thuong → reward, ban → shot, trung → impact, no → explosion, chet → death, sinh-vat → creature, nen → ambience, nhac → music. Chữ Việt cũ giữ làm alias, AudioLab không phải đổi tên.

### 3.7 Đặt tên cho file mới (từ nay)

File cũ giữ nguyên đường dẫn. id cũ chỉ đổi trong lượt đặt tên của từng game.

- **id**: cụm danh từ tiếng Anh, kebab-case, danh từ chính ở cuối: `watch-hut`, `stilt-house`, `wooden-jetty`, `pine-rock-a`. Chữ Việt chỉ vào `aliases`.
- **Biến thể** dùng `-a`/`-b`/`-c`. **Bản nháp** dùng `.v1`/`.v2` có dấu chấm. Không bao giờ dùng `-v1` để chỉ biến thể.
- **Bản nháp và bản loại** của game mới vào `_review/<cùng đường dẫn>` ngay từ đầu.
- **Thư mục art của game mới** đặt theo loại số nhiều: `buildings/ structures/ nature/ props/ characters/ creatures/ vehicles/ weapons/ items/ traps/ vfx/ ui/ ground/ backdrops/`. Bộ đi cùng nhau thì có thư mục vùng: `nature/pine-forest/rock-a.png`.
- **GLB Tripo** đổi tên thành `<id>.glb` lúc import (như nay). Chú thích Tripo lưu vào `downloadedAs` của SOURCES.json. tripo-match đã sinh được ánh xạ đó. Chữ trong chú thích thành nhãn mồi ("thatched hut", "wooden dock bridge").
- **id âm thanh**: kiểu chấm, chỉ chữ Anh: `<kind>.<thing>[.<variant>]`, ví dụ `ui.select`, `impact.wood.light`. File theo AUDIO_PIPELINE §11: `sfx/<kind>/<id-gạch-nối>-<n>.ogg`. Chữ Việt trong id AudioLab hôm nay (`gun.xung`, `gun.tia`) có alias tiếng Anh ngay; đổi tên ở lượt đặt tên.
- **Đổi tên không làm mất dấu.** Dòng tuyển chọn lưu `md5s`. Bộ quét gắn lại dòng theo md5 và ghi `formerUids`.

---

## 4. Siêu dữ liệu

### 4.1 Thẻ (`library/out/catalog.json`, `"schema": "asset-library/1"`)

| Trường | Nghĩa | Lấy từ, theo thứ tự ưu tiên |
|---|---|---|
| `uid`, `short`, `formerUids[]` | danh tính (3.3) | bộ quét |
| `type` | `image`, `model3d`, `audio`, `music` | bộ quét (`model3d` khi có GLB) |
| `name` | tên tiếng Anh để hiện | tuyển chọn → NAMES_EN → phần Anh của 3D_IMPORT → dịch mồi (`nameSource: seed-translation`) |
| `aliases[]` | tiếng Việt có và không dấu, chữ trong id, chữ chú thích Tripo, mã duyệt (H1, V55) | tuyển chọn → NAMES_EN, 3D_IMPORT "Tên", `INDEX.md`, `downloadedAs` |
| `kind`, `subkind`, `tags[]`, `biome[]`, `style` | các trục lọc | tuyển chọn → folderMap → khớp từ vựng trên tên và ghi chú |
| `origin` | game hay thư viện nơi làm ra | đường dẫn file chính |
| `status`, `pipeline` | 3.6 | vai trò file; `shipped` khi runtime có tham chiếu; `provisional` khi có dòng ART_REPLACE_LATER; `requested` khi 3D_REQUESTS hay `notMadeYet` có dòng mà không có file |
| `quality` | `{score2d, score3d, level, need, evidence[]}` | IMAGE_AUDIT, 3D_IMPORT_2026-10-28 "Điểm/Mức", ART_REPLACE_LATER, báo cáo phiếu; với âm: điểm Bảng Nghe |
| `licence` | `{id, commercialOk, attribution, aiInputAllowed, private, notForRelease}` | `library/licences.json` + AudioLab `SOURCES.jsonl` + bảng ATTRIBUTION.md + `private.md5` |
| `provenance` | `{generator, ticket, prompt, tripoFile, faceLimit, rig, matchConfidence, date}` | sidecar, 3D_IMPORT, 3D_REQUESTS, báo cáo phiếu, AudioLab `SOURCES.json` |
| `model` | `{heightM, footprintM, triangles{original,high,medium}, skinned, clips[], sockets[], preset}` | `inspectGlb` (+Y, mét), manifest, preset |
| `audio` | `{variants, durationMs[], sampleRate, channels, codec, loop, lufsM?}` | bộ đọc đầu file, index AudioLab |
| `usedBy[]` | `{game, ref, manifestKey?, shipped, imported?}` | manifest, preset, tham chiếu trong mã, các `library.lock.json` |
| `copies[]` | `{path, location, md5}` | gom theo md5 |
| `rejectedMd5[]` | md5 các lượt bị loại | ngữ pháp hậu tố; dùng để chặn nhập lại |
| `similar[]` | thẻ giống ở game khác | cùng subkind + từ đồng nghĩa + chấm hình khối của tripo-match |
| `hero`, `thumb` | file đẹp nhất để hiện, ảnh nhỏ | thứ tự vai trò |
| `files[]` | 4.2 | bộ quét |
| `warnings[]` | ví dụ "manifest runtime không có trên Drive" | quét và kiểm |

**Hiện mặc định:** shipped, pass, provisional, unscored. **Ẩn:** draft, rejected, review, AudioLab `work/`. **Chỉ hiện với `--requested`:** requested. Thẻ `private` chỉ hiện trên máy này, có khóa, không chép được.

**Thước chất lượng** theo ART_ACCEPTANCE: 3D đạt từ 9, tạm 7–8,5 (ghi ART_REPLACE_LATER); 2D đạt từ 8 (8–8,5 vẫn ghi). **Âm thanh chưa có thước.** Claude chọn (chủ dự án đã giao việc theo đề xuất, đổi được): đã ship trong game và có nguồn biết rõ = dùng được; Bảng Nghe từ 4 sao = pass; 3 sao = provisional; còn lại unscored.

### 4.2 Một dòng file

```json
{"role": "glb-original", "path": "games/dragon-hold/art-src/3d/houses/herb-hut.glb",
 "md5": "b2ade5601998050f7e12beb3ba7e6459", "bytes": 3216504, "local": true, "canonical": true,
 "onDrive": "yes", "glb": {"triangles": 9858, "skinned": false, "clips": []}}
```

`onDrive` là `yes` (đường dẫn và md5 có trong lock), `changed` (đường dẫn có trong lock với md5 khác), `no`, `private` hoặc `external` (thư viện AudioLab, tải lại được). Ảnh có `image: {w, h, alpha}`. Âm có `audio: {durationMs, sampleRate, channels, codec}`.

### 4.3 Dòng tuyển chọn (`library/curated/<game>.jsonl`, mỗi uid một dòng, đã sắp)

```json
{"uid":"typing-defense:landmarks/choi-canh-doi","md5s":["64178d19879c55778426d74f126f56e5"],"name":"Hilltop Watch Hut","aliases":["Chòi canh trên đồi","choi canh doi","thatched hut","watchtower"],"kind":"building","subkind":"hut","tags":["thatch","wood","stilts","stairs","lookout"],"biome":["hill","meadow"],"style":"viet-village","canonical":{},"reuseNotes":"Sạch ở góc 55° và ở 1/4 cỡ. Chưa đóng gói runtime: cần preset tĩnh.","nameSource":"seed-translation","reviewed":null}
```

- Không chứa prompt, không chứa gì của bộ riêng tư.
- Bộ mồi chỉ thêm dòng. Không bao giờ ghi đè dòng đã có `reviewed`.
- Claude ghi `"reviewed": "claude-2026-10-29"` sau khi xem ảnh nhỏ.

### 4.4 Ví dụ 1: GLB một cái lều (giá trị đo trên ổ đĩa 28/10)

```json
{
  "uid": "dragon-hold:houses/herb-hut", "short": "dragon-hold:herb-hut", "type": "model3d",
  "name": "Herb Hut", "aliases": ["Lều Thuốc Nam", "lều thảo dược", "leu thuoc nam", "H1", "fantasy cottage"],
  "kind": "building", "subkind": "hut", "tags": ["thatch", "wood", "healer", "village", "small"],
  "biome": ["pine-forest", "village"], "style": "mythic-forest", "origin": "dragon-hold",
  "status": "shipped", "pipeline": "runtime",
  "usedBy": [{"game": "dragon-hold", "ref": "games/dragon-hold/src/content/data/our-side.ts:117",
              "manifestKey": "props/herb-hut", "manifest": "public/assets/dragon-hold/models/m0b/manifest.json", "shipped": true}],
  "quality": {"score2d": 9.5, "score3d": null, "level": "pass", "need": null,
              "evidence": ["docs/games/IMAGE_AUDIT_2026-10-25.md:42 (H1 Đạt 9,5)", "docs/games/NAMES_EN.md:89"]},
  "licence": {"id": "owner-tripo", "commercialOk": true, "attribution": null, "private": false, "notForRelease": false},
  "provenance": {"generator": "image-gen → tripo-web", "tripoFile": "fantasy+cottage+3d+model.glb", "faceLimit": 10000,
                 "rig": false, "matchConfidence": 0.98, "prompt": "games/dragon-hold/art-src/houses/herb-hut.prompt.txt",
                 "evidence": "docs/games/3D_IMPORT_2026-10-26.md:31"},
  "model": {"heightM": 2.01, "footprintM": [2.18, 2.08], "triangles": {"original": 9858, "high": 4400, "medium": 4400},
            "skinned": false, "clips": [], "sockets": ["FX_CORE", "FX_TOP"],
            "preset": {"file": "games/dragon-hold/scripts/models/presets/dragon-hold-m0b.json", "key": "props/herb-hut",
                       "measure": "width", "metres": 2.2, "yaw": 90}},
  "hero": "games/dragon-hold/art-src/houses/herb-hut.png",
  "thumb": "library/.thumbs/9907b30aabab57040e88be86ac89ec2b.webp",
  "files": [
    {"role": "concept", "path": "games/dragon-hold/art-src/houses/herb-hut.png", "md5": "9907b30aabab57040e88be86ac89ec2b", "image": {"w": 1254, "h": 1254}, "onDrive": "yes"},
    {"role": "tripo-source", "path": "games/dragon-hold/art-src/houses/herb-hut.tripo.png", "md5": "a61413b7274a3c61e6490b82b5debd06", "image": {"w": 1024, "h": 1024}, "onDrive": "yes"},
    {"role": "glb-original", "path": "games/dragon-hold/art-src/3d/houses/herb-hut.glb", "md5": "b2ade5601998050f7e12beb3ba7e6459", "bytes": 3216504, "onDrive": "yes"},
    {"role": "glb-processed", "path": "games/dragon-hold/art-src/models/props/herb-hut.glb", "md5": "08267409632cf407eafe60c2c2bfd989", "onDrive": "yes"},
    {"role": "runtime-high", "path": "games/dragon-hold/public/assets/dragon-hold/models/m0b/props/herb-hut/herb-hut.high.glb", "md5": "e6b8b309ea47c2ce140fbeaf511cffe6", "bytes": 230316, "onDrive": "yes"},
    {"role": "runtime-medium", "path": "games/dragon-hold/public/assets/dragon-hold/models/m0b/props/herb-hut/herb-hut.medium.glb", "md5": "7241e7200487086415c0e436cb68b29e", "bytes": 126416, "onDrive": "yes"},
    {"role": "icon", "path": "games/dragon-hold/art-src/ui/icons/herb-hut.png", "md5": "cc737bc005e37a54e8645b814a4158ef", "onDrive": "yes"},
    {"role": "icon-256", "path": "games/dragon-hold/art-src/icons/normalized/herb-hut.256.png", "md5": "f89feb3357dd70c2f8fd761f4f303279", "onDrive": "yes"},
    {"role": "icon-64", "path": "games/dragon-hold/art-src/icons/normalized/herb-hut.64.png", "md5": "1644c8b50f75c8513053306782411fb7", "onDrive": "yes"}
  ],
  "hiddenFiles": {"rejected": 9, "prompt": 14, "report": 2},
  "rejectedMd5": ["<9 md5 của herb-hut.tripo.rejected-012/012b/012c …>"],
  "copies": [],
  "similar": [{"uid": "typing-defense:landmarks/choi-canh-doi", "why": "subkind hut; 3D 9 Đạt", "style": "viet-village"}],
  "warnings": ["manifest m0b/manifest.json không có trong Git lẫn Drive: máy mới không dựng lại được mục props/herb-hut"]
}
```

Trên ổ đĩa, thẻ này gom 32 file art-src và 2 file runtime. Không có thư viện thì chúng rải ở `houses/`, `3d/houses/`, `models/props/`, `icons/normalized/`, `ui/icons/`, `public/…/m0b/props/`.

### 4.5 Ví dụ 2: ảnh nguồn gửi Tripo, chưa có GLB

Món này cho thấy ba điều: ảnh 2D đạt mà chưa có model; bản `.try1` cùng md5 là bản sao, không phải nháp; và một món giống đã có ở game khác.

```json
{
  "uid": "dragon-hold:props/pine-river/wooden-jetty", "short": "dragon-hold:wooden-jetty", "type": "image",
  "name": "Wooden Jetty", "aliases": ["cầu tàu gỗ nhỏ", "cau tau go", "rong_wooden-jetty"],
  "kind": "structure", "subkind": "jetty", "tags": ["wood", "planks", "posts", "river", "small"],
  "biome": ["pine-forest", "river"], "style": "mythic-forest", "origin": "dragon-hold",
  "status": "pass", "pipeline": "tripo-requested",
  "quality": {"score2d": 9, "score3d": null, "level": "pass", "need": null,
              "evidence": ["docs/codex-queue/046-report.md:178 (Claude 9)", "docs/codex-queue/046-report.md:23 (Codex tự chấm 9,5)"]},
  "licence": {"id": "owner-ai-2d", "commercialOk": true, "attribution": null, "private": false, "notForRelease": false},
  "provenance": {"generator": "image-gen", "ticket": "046", "pickedTry": "try1",
                 "prompt": "games/dragon-hold/art-src/props/pine-river/wooden-jetty.prompt.txt",
                 "tripoRequest": {"folder": "face 4000 - không rig - 1 ảnh", "file": "rong_wooden-jetty.png", "note": "dài 4 m",
                                  "evidence": "typing-game-handoff-2026-10-25/tripo-upload-dot3/INDEX.md:20"}},
  "hero": "games/dragon-hold/art-src/props/pine-river/wooden-jetty.png",
  "files": [
    {"role": "concept", "tripoSource": true, "canonical": true,
     "path": "games/dragon-hold/art-src/props/pine-river/wooden-jetty.png",
     "md5": "805afcb508b3dbda47baff8aecb8fd19", "bytes": 1667900, "image": {"w": 1536, "h": 1024, "alpha": false}, "onDrive": "yes"},
    {"role": "prompt", "path": "games/dragon-hold/art-src/props/pine-river/wooden-jetty.prompt.txt",
     "md5": "70f8375216033ed357106bdc5b7bf72d", "onDrive": "yes"}
  ],
  "copies": [
    {"path": "games/dragon-hold/art-src/props/pine-river/wooden-jetty.try1.png", "location": "same-folder", "md5": "805afcb508b3dbda47baff8aecb8fd19"},
    {"path": "typing-game-handoff-2026-10-25/tripo-upload-dot3/face 4000 - không rig - 1 ảnh/rong_wooden-jetty.png", "location": "handoff", "md5": "805afcb508b3dbda47baff8aecb8fd19"}
  ],
  "hiddenFiles": {"review": 6, "prompt": 1},
  "similar": [{"uid": "typing-defense:landmarks/cau-tau", "why": "subkind jetty; 3D 9 Đạt; 7.465 tam giác; có bản dự phòng cau-tau.alt.glb",
               "style": "viet-village"}],
  "warnings": ["Đã xếp vào Tripo dot3, chưa có GLB. Món giống đã có: typing-defense:landmarks/cau-tau. Chủ dự án quyết trước khi tiêu credit (mục 10)."]
}
```

### 4.6 Ví dụ 3: tiếng click (SFX)

Thẻ này cho thấy so khớp sha256 tìm lại nguồn từng file, thứ mà ATTRIBUTION.md dạng văn xuôi của Space đã mất.

```json
{
  "uid": "kenney:interface-sounds/Audio/click", "type": "audio",
  "name": "UI Click (Kenney Interface)", "aliases": ["click", "tick", "gõ phím", "bấm nút", "phim-ui"],
  "kind": "ui", "subkind": "click", "tags": ["click", "short", "dry", "synthetic"], "style": "neutral",
  "origin": "kenney", "status": "shipped",
  "usedBy": [{"game": "space-typing", "ref": "games/space-typing/src/audio/Sfx.ts:36 (import.meta.glob ui/*.ogg) và :672 (uiFile \"click\")",
              "copyPath": "games/space-typing/src/assets/audio/ui/click.ogg", "variant": "002", "shipped": true}],
  "quality": {"level": "pass", "rule": "đã ship, nguồn CC0 biết rõ"},
  "licence": {"id": "cc0-1.0", "commercialOk": true, "attribution": null, "aiInputAllowed": true, "private": false, "notForRelease": false,
              "ledger": "~/AudioLab/libraries/SOURCES.jsonl (Kenney Interface Sounds 1.0)"},
  "audio": {"variants": 5, "codec": "vorbis", "sampleRate": 44100, "channels": 1, "loop": false,
            "durationMs": [100, 10, 10, null, null]},
  "files": [
    {"role": "variant", "variant": "001", "path": "~/AudioLab/libraries/kenney/interface-sounds/Audio/click_001.ogg",
     "sha256": "ccfb7fa0cccdd9fa…", "bytes": 4876, "onDrive": "external"},
    {"role": "variant", "variant": "002", "path": "~/AudioLab/libraries/kenney/interface-sounds/Audio/click_002.ogg",
     "sha256": "adcd1f4adc35f1b41bc1b5bbefeff7aa44f2f3f0d96d3199b544140c7c1e761c", "bytes": 4275, "onDrive": "external"},
    {"role": "variant", "variant": "003", "path": "~/AudioLab/libraries/kenney/interface-sounds/Audio/click_003.ogg",
     "sha256": "2fa929138bc3a0f4…", "bytes": 4371, "onDrive": "external"}
  ],
  "copies": [{"path": "games/space-typing/src/assets/audio/ui/click.ogg", "location": "game",
              "md5": "722ec540eb252470b8b0cf3577ceba27", "inGit": "khóa bởi tools/audio-lab/build/legacy-audio.json"}],
  "thumb": "library/.thumbs/adcd1f4a….wave.png"
}
```

`click_002` dài đúng 10 ms (ffprobe và afinfo cùng đo 0,010 s, 442 mẫu); `click_001` dài 100 ms. `null` là chỗ bộ quét điền.

Bạn gỗ của nó, thẻ mà ví dụ 6.2 chọn: `kenney:impact-sounds/Audio/impactWood_light`, 5 biến thể, mỗi biến thể 266 ms, stereo 44,1 kHz, CC0, trạng thái `unscored` (mẫu thư viện, chưa game nào dùng).

### 4.7 Sổ chép của game (`games/<g>/library.lock.json`, `"schema": "library.lock/1"`)

```json
{
  "schema": "library.lock/1", "game": "word-village",
  "items": [
    {"uid": "dragon-hold:houses/herb-hut", "as": "props/herb-hut", "date": "2026-11-02", "by": "claude", "reason": "lều trong làng",
     "licence": {"id": "owner-tripo", "commercialOk": true}, "statusAtCopy": "shipped", "quality": "2D 9,5; 3D chưa chấm",
     "files": [
       {"role": "glb-original", "from": "dragon-hold:art-src/3d/houses/herb-hut.glb", "to": "art-src/3d/buildings/herb-hut.glb", "md5": "b2ade5601998050f7e12beb3ba7e6459", "stage": "source"},
       {"role": "runtime-high", "from": "dragon-hold:public/assets/dragon-hold/models/m0b/props/herb-hut/herb-hut.high.glb", "to": "public/assets/word-village/models/props/herb-hut/herb-hut.high.glb", "md5": "e6b8b309ea47c2ce140fbeaf511cffe6", "stage": "runtime"},
       {"role": "runtime-medium", "from": "dragon-hold:…/herb-hut.medium.glb", "to": "public/assets/word-village/models/props/herb-hut/herb-hut.medium.glb", "md5": "7241e7200487086415c0e436cb68b29e", "stage": "runtime"}
     ]}
  ]
}
```

- `word-village` là id minh họa cho một game mới.
- `verify-library.mjs` (kit) đọc file này trong `check` của game: file `stage: runtime` sai md5 là lỗi; thiếu file là cảnh báo (máy chưa `media:pull`), là lỗi khi có `--strict` (dùng lúc deploy). Nó chỉ đọc trong gốc game, nên bản clone riêng của game vẫn build được.
- Với âm thanh, mỗi dòng thêm `sourceRow` (dòng `audiolab.sources/1` hoặc dòng thư viện CC0) và `licenceRow` (dòng `SOURCES.jsonl`), để nguồn đi theo game ngay cả khi `~/AudioLab/work` bị dọn.

---

## 5. Cách tìm

### 5.1 Trang `library/out/catalog.html`

```
┌ Thư viện tài sản ── [ chòi                    ] [2D] [3D] [Âm thanh]  9 kết quả · 40 ms · quét 28/10 12:30 ┐
│ Loại             │ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐                                         │
│ ☑ building   7   │ │ ảnh  │ │ ảnh  │ │ ảnh  │ │ ảnh  │ │ ảnh  │                                         │
│ ☐ structure  2   │ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘                                         │
│ Game             │ Hilltop   Herb Hut  Barracks  Otter     Barracks                                    │
│ ☐ Rồng Giữ Ải 1  │ Watch Hut lều thảo  Kit L2    Stilt     (Long Spear)                                │
│ ☐ Lời Gọi     6  │ chòi canh dược      chòi gỗ   House     trại lính                                   │
│ Vùng · Phong cách│ 3D·9 ✓    ● ship    3D·9 ✓    3D·8,5 ~  3D·8 ~                                      │
│ Chất lượng       │                                                                                    │
│ Trạng thái · Drive│ ☐ hiện bản ẩn                                                                     │
└──────────────────┴────────────────────────────────────────────────────────────────────────────────────┘
```

- **Menu tiếng Việt, tên món tiếng Anh**, tên Việt là dòng chú thích xám nhỏ.
- **Bộ lọc**, theo thứ tự: chữ, loại, kiểu (2D, 3D, âm), game, vùng, phong cách, chất lượng (đạt, tạm, dưới thước, chưa chấm), trạng thái, Drive.
- **Bấm một thẻ** mở khung bên:
  - file theo vai trò, md5, cỡ, trạng thái Drive;
  - 300 ký tự đầu của prompt (chỉ đọc từ file trên máy, không lưu vào Git);
  - mét, tam giác, clip, socket;
  - giấy phép, ai dùng, bản sao, món giống ở game khác;
  - với âm: một nút nghe cho mỗi biến thể, dạng sóng, độ dài, tần số mẫu, số kênh;
  - hai nút chép lệnh: `pnpm lib:show <uid>` và `pnpm lib:copy <uid> --to <game>`.
- **Mặc định ẩn:** bản loại, `_review`, bản nháp (`.v1`, `.try1` khác md5), bản phái sinh (`.alpha`, `.flat`), `work/` của AudioLab. Một công tắc hiện tất cả.
- **Không cần server.** Trang là một file HTML nhỏ, nạp `catalog.data.js` cùng thư mục bằng thẻ `<script src>` (chạy được với `file://`, không dùng fetch). Ảnh nhỏ nạp theo đường dẫn tương đối `../.thumbs/<md5>.webp`. Không có URL mạng nào.
- **Nghe thử.** Thẻ `<audio>` trỏ thẳng file thật theo đường dẫn tương đối. Trang hỏi `canPlayType('audio/ogg; codecs=vorbis')` và `codecs=opus`. Trình duyệt không phát được thì nút nghe đổi thành nút chép lệnh `pnpm lib:play <uid>`.
- **Báo cũ.** Đầu trang ghi giờ quét. Quá 24 giờ thì chữ đỏ "mục lục cũ, chạy `pnpm lib:build`".
- Giao diện sáng và tối; dùng được ở bề ngang 375 px.

### 5.2 Lệnh

```
$ pnpm lib:find hut --type 3d
 #  uid                                            tên                     loại/con         game     tam giác  chất lượng      Drive
 1  typing-defense:landmarks/choi-canh-doi         Hilltop Watch Hut       building/hut     Lời Gọi  7.733     3D 9 đạt        có
 2  dragon-hold:houses/herb-hut                    Herb Hut                building/hut     Rồng     4.400 r   đã ship         có
 3  typing-defense:kits/barracks-kit-l2            Barracks Kit L2         building/kit     Lời Gọi  3.592     3D 9 đạt        có
 4  typing-defense:landmarks/nha-rai-da            Otter Stilt House       building/house   Lời Gọi  7.289     3D 8,5 tạm      có
 5  typing-defense:branches/barracks-giao-dai      Barracks (Long Spear)   building/barr.   Lời Gọi  9.324     3D 8 tạm        có
 (5 trên 7; --all hiện thêm bản dự phòng và bản loại, --requested hiện món mới xin)
```

- Số tam giác có `r` là bậc runtime; còn lại là bản gốc Tripo.
- Tên dòng 3–5 là tên mồi; Claude duyệt ở AL-12.
- Lệnh khác:
  - `pnpm lib:show <uid|dạng ngắn>`: cả thẻ; `--all` thêm file ẩn; `--json`.
  - `pnpm lib:play <uid> [--variant 2]`: phát bằng `afplay`. Nếu `afplay` không phát được (Opus), lệnh giải mã bằng `ffmpeg` ra WAV tạm trong `library/.cache/` rồi phát.
  - `pnpm lib:check --request "wooden jetty"`: món giống, kể cả món đang xin hay đang nháp.
- Bộ lọc của `lib:find`: `--type image|3d|audio|music`, `--kind`, `--sub`, `--tag`, `--biome`, `--style`, `--game` (nơi làm), `--used-by`, `--status`, `--pipeline`, `--min-score`, `--max-tris`, `--has glb|runtime|clips|rig|prompt|icon`, `--drive no`, `--all`, `--requested`, `--json`, `--limit N`.
- `lib:find` tự báo khi mục lục cũ: nếu một `media.md5`, một `SOURCES.json` hay một manifest model mới hơn giờ quét, nó in "mục lục cũ hơn …, chạy `pnpm lib:scan`". Chỉ cần vài lệnh `stat`.

### 5.3 Thư mục Finder `library/browse/`

`pnpm lib:browse` dựng cây theo nội dung, toàn liên kết tượng trưng tới ảnh đẹp nhất của mỗi thẻ:

```
library/browse/building/hut/Herb Hut (dragon-hold).png        → games/dragon-hold/art-src/houses/herb-hut.png
library/browse/building/hut/Hilltop Watch Hut (typing-defense).png
library/browse/structure/jetty/Wooden Jetty (dragon-hold).png
library/browse/ui/click/UI Click (kenney).ogg                 → biến thể đầu
```

- 0 byte media; Git bỏ qua cả thư mục. Quick Look của Finder xem được ảnh và nghe được âm qua liên kết.
- Mỗi lần chạy, lệnh dựng cây mới vào `browse.new/` rồi đổi tên. Nó chỉ gỡ **liên kết** trong `library/browse/`, không bao giờ gỡ file thường (có test).
- Chỉ thẻ hiện mặc định, không có thẻ riêng tư.

### 5.4 `library/CATALOG.md` (trong Git)

- Một bảng mỗi loại. Cột: tên tiếng Anh, tên Việt, uid, game làm ra, trạng thái và điểm, ai dùng.
- Chỉ thẻ công khai đã có `reviewed`. Không md5, không cỡ, không trạng thái Drive, nên chỉ đổi khi dòng tuyển chọn đổi. Không xáo lịch sử Git mỗi lần quét.
- Đọc được trên GitHub và trên máy mới chưa có media.

### 5.5 Agent

- AGENTS.md thêm một dòng: "Trước khi xin hay sinh hình, model, âm thanh mới, chạy `pnpm lib:find <từ tiếng Anh> --json` và dẫn kết quả."
- Agent đọc `library/out/catalog.json` hoặc gọi lệnh. Không cần trình duyệt, nên Codex dùng được.

### 5.6 Cách xếp hạng (chung cho trang và lệnh)

- **Chuẩn hóa:** chữ thường; bỏ dấu (đ → d); tách ở `- _ + . /`, khoảng trắng và camelCase (`impactWood_light` → impact, wood, light); bỏ từ dừng của tripo-match (3d, model, glb…); mở rộng từ đồng nghĩa hai chiều; từ liên quan tính nửa điểm.
- **Trọng số:** tên 5, alias 4, loại con 3, loại 3, nhãn 2, chữ trong đường dẫn hay chú thích Tripo 1.
- **Cộng trừ:** shipped hoặc pass +1; model sẵn runtime +0,5; provisional −0,5. Trạng thái ẩn bị lọc ra, không bị đẩy xuống.
- **Tốc độ:** p95 dưới 300 ms trên khoảng 3.000 thẻ. Trang nhúng đúng `lib/search.mjs`, nên trang và lệnh xếp giống hệt.

---

## 6. Cách dùng lại trong game mới

Game ví dụ là `games/word-village` (id minh họa). Các bước giống hệt với mọi game có trong `media/media.config.json`. Game mới phải được thêm vào `media.config.json` trước (Claude), để `media:push` gánh file của nó.

### 6.1 Một model lều

1. **Tìm (khoảng 5 giây).** `pnpm lib:find hut --type 3d` (5.2), hoặc gõ "chòi" trên trang. Hai ứng viên mạnh:
   - `dragon-hold:houses/herb-hut`: đã ship, runtime 230 KB / 126 KB, 4.400 tam giác, preset rộng 2,2 m, socket FX_CORE/FX_TOP;
   - `typing-defense:landmarks/choi-canh-doi`: 3D 9 đạt, bản gốc 7.733 tam giác, chưa đóng gói runtime.
2. **Xem (khoảng 10 giây).** `pnpm lib:show dragon-hold:herb-hut`: file theo vai trò, giấy phép `owner-tripo` (ship được), phong cách `mythic-forest`, prompt, cỡ, và cảnh báo nếu có.
3. **Lập kế hoạch chép.** Mặc định chỉ chạy thử:
   ```
   $ pnpm lib:copy dragon-hold:herb-hut --to word-village --as buildings/herb-hut
   kế hoạch (chạy thử; thêm --apply để làm):
     clone games/dragon-hold/art-src/houses/herb-hut.png         → games/word-village/art-src/buildings/herb-hut.png        1,85 MB md5 9907b30a
     clone games/dragon-hold/art-src/houses/herb-hut.prompt.txt  → games/word-village/art-src/buildings/herb-hut.prompt.txt
     clone games/dragon-hold/art-src/houses/herb-hut.tripo.png   → games/word-village/art-src/buildings/herb-hut.tripo.png  0,73 MB
     clone games/dragon-hold/art-src/3d/houses/herb-hut.glb      → games/word-village/art-src/3d/buildings/herb-hut.glb     3,22 MB
     run   pnpm models:prepare --root games/word-village \
             --import games/dragon-hold/public/assets/dragon-hold/models/m0b/manifest.json --only props/herb-hut
           (clone bậc high 230 KB + medium 126 KB, viết lại URL, ghi importedFrom {game, key, md5High, md5Medium})
     add   SOURCES.json của word-village: "buildings/herb-hut.glb" + importedFrom
     add   games/word-village/library.lock.json  +1 mục, kèm presetStub "props/herb-hut"
           {source, triangles 4400, yaw 90, metres 2.2, reviewed: false} (Claude gộp vào preset của game)
     add   library/imports.jsonl                 +1 dòng
     bỏ    9 bản loại, 2 báo cáo; icon cần --with icons
   cổng: giấy phép owner-tripo ship được · trạng thái shipped · md5 nguồn khớp lock Drive
   ổ đĩa: clone APFS, gần 0 byte cho tới khi sửa
   ```
   - `--as <kind>/<stem-tiếng-Anh>` cho thư mục và tên ở game đích. Nhờ vậy `choi-canh-doi` vào game mới thành `buildings/watch-hut` mà không đụng game nguồn.
   - Mặc định thư mục đích lấy từ loại trong từ vựng (`buildings/`).
4. **Làm và ghi.** Claude chạy `--apply` khi làn của game đích rảnh. Rồi:
   - `pnpm media:push` (chỉ Claude): `media.md5` của game đích có thêm dòng cùng md5 với nguồn;
   - commit trong repo game: `library.lock.json`, `art-src/3d/SOURCES.json`, preset, manifest (nếu game theo dõi manifest);
   - commit trong repo cha: `library/imports.jsonl`.
5. **Kiểm.** `node src/kit/tools/verify-library.mjs` trong game đích (nằm trong `pnpm check`). Rồi `pnpm lib:scan --game word-village`: thẻ Herb Hut có thêm `usedBy` word-village (imported). Tìm "hut" vẫn ra **một** thẻ.

Bản chép là bản ghim: game đích build và deploy một mình. Muốn sửa mái thì sửa bản của mình; md5 tách ra thành thẻ riêng, có dấu `derivedFrom` lấy từ sổ.

Nếu file nguồn không có trên máy: `lib:copy` gọi `pnpm media:pull --game dragon-hold --path <đường dẫn>` để kéo đúng file đó, kiểm md5. Nếu đường dẫn chưa có trong lock của game nguồn thì dừng: "chưa lên Drive, Claude phải `media:push` dragon-hold trước".

### 6.2 Một tiếng click gỗ cho menu

1. **Tìm.** `pnpm lib:find "wood click" --type audio`:
   1. `kenney:impact-sounds/Audio/impactWood_light`: 5 biến thể, 266 ms, CC0;
   2. `kenney:impact-sounds/Audio/impactWood_medium`;
   3. `vcsl:…/Woodblock/wood_click_f`: rr1–2, cần cắt;
   4. `kenney:interface-sounds/Audio/click`: không phải gỗ; đã ship ở Space.

   Nghe: `pnpm lib:play kenney:impactWood_light --variant 2`, hoặc nút nghe trên trang.
2. **Chép.** Có hai đường; `lib:copy` chọn theo việc cần làm:
   - **(a) Chép thẳng** (mặc định, cho mẫu CC0 và âm đã ship):
     ```
     pnpm lib:copy kenney:impact-sounds/Audio/impactWood_light --to word-village --as ui.select --variants 1-3 --transcode 48k
     ```
     - ghi `games/word-village/public/assets/word-village/audio/sfx/ui/ui-select-1..3.ogg` (OGG Vorbis 48 kHz qua `ffmpeg`, đúng AUDIO_PIPELINE §11); không có `--transcode` thì clone nguyên byte;
     - gộp vào `public/assets/word-village/audio/manifest.json` (v2): `sounds["ui.select"]`;
     - ghi mục vào `library.lock.json` kèm `sourceRow` (đường dẫn, sha256 nguồn, CC0) và `licenceRow` (dòng Kenney trong `SOURCES.jsonl`);
     - nếu game đã mở `art-src/audio/` trong `.gitignore` (AUDIO_PIPELINE §11), ghi thêm dòng vào `art-src/audio/SOURCES.json` và `licences.jsonl`;
     - chạy `pnpm audio:licence-check` cho game đích, hỏng thì dừng.
   - **(b) Qua công thức** (`--recipe`, khi cần cắt, ghép lớp, chỉnh độ to): ghi `tools/audio-lab/build/recipes/word-village/ui.select.json` với lớp `library` (đường dẫn, sha256, CC0) và đích của nhóm `ui` trong `taxonomy.py`. Claude chạy `pnpm audio:build`, nghe trên Bảng Nghe, rồi phát hành vào game.
3. Claude chạy `media:push` và commit. Game dựng theo mẫu `FileBank` của Rồng tự thay âm tổng hợp của `ui.select` bằng file, không sửa mã.

Âm do AudioLab làm (`~/AudioLab/work`) không chép thẳng được: nó là bản nháp. Nó vào game qua bước phát hành của AudioLab. Bước đó phải chép dòng `audiolab.sources/1` và dòng giấy phép vào game **trước** khi `work/` bị dọn. `lib:check --audiolab` báo âm đã phát hành mà nguồn chưa nằm trong game nào.

### 6.3 Cổng chặn khi chép

`lib:copy` từ chối, kèm lý do:
- thẻ riêng tư (`shared/music`, Dota-Sounds, `public/local-assets`);
- `notForRelease`;
- giấy phép `unknown` (28 file Space không rõ nguồn, gồm 22 file `duel/sfx`) hay `commercialOk: false`;
- file bị loại, hoặc file có md5 nằm trong `rejectedMd5` của thẻ nào đó;
- đích là Tu Tiên;
- đích đã có file cùng đường dẫn mà khác md5;
- thẻ `unscored` chưa ship, trừ khi có `--allow-unscored --reason "<lý do>"`; lý do ghi vào sổ chép.

Khác:
- thẻ `provisional` in ghi chú ART_REPLACE_LATER của nó lúc chép;
- giấy phép CC-BY tự thêm dòng ghi công vào `CREDITS.md` của game đích;
- món đã ship mà chưa chấm (như Herb Hut 3D) chép được, kèm ghi chú "chưa chấm 3D, đang dùng ở Rồng".

### 6.4 Lần dùng thật đầu tiên: Tuyến Cuối

- `pnpm lib:find --used-by typing-survival` liệt kê các model Space mà Tuyến Cuối còn nạp lúc chạy qua `/assets/space-typing/models/manifest.json`.
- `lib:copy space-typing:<kind>/<id> --to typing-survival` cho 7 model ở DEPLOY_INDEPENDENCE §5.1 (11.501.400 B bậc high, 3.969.672 B bậc medium). Lệnh gọi `models:prepare --import` và ghi nguồn.
- Rồi đổi `src/view/models.ts` sang manifest của chính game, bỏ mục Vite `serveSharedFolders` và hai alias nginx. Luật 3 của DEPLOY_INDEPENDENCE hết bị vi phạm, và 7 model có nguồn ghi rõ (6 bản Draconis ở Rồng chưa từng có).

---

## 7. Drive và `media.md5`

- **Không thêm chỗ chứa trên Drive.** Thẻ trỏ file bằng `<game>:<path>` cộng md5. Cặp đó đúng là một dòng `media.md5`.
- **Thư viện không bao giờ ghi lock.** `media.md5` vẫn là sự thật duy nhất về byte. Bộ quét đọc `.cache/media-hash.json` chỉ đọc (để mồi bộ đệm của mình ở `library/.cache/hash.json`), nên không đụng bộ đệm của công cụ media khi `media:push` đang chạy.
- **Thấy được độ trễ Drive.** `lib:check --drive` liệt kê file chưa lên Drive theo game, kèm số byte, file chính trước. Sáng 28/10 thiếu: 86 GLB đợt 2 Lời Gọi, 48 GLB M0b và 48 GLB đã xử lý của Rồng, vài trăm file `_review`. Lúc 12:10 phần lớn đã push. Còn thiếu chắc chắn: `public/assets/dragon-hold/models/m0b/manifest.json` (không có ở Git lẫn Drive) và 1 GLB mới của Lời Gọi (157 trên ổ, 156 trong lock). AL-01 đóng nốt.
- **Kéo một file.** Lệnh mới `pnpm media:pull --game <id> --path <glob>` chỉ đọc dòng lock của game đó, kéo qua `.media-tmp/`, kiểm md5 rồi đặt vào chỗ. `lib:copy` cần nó trên máy mới. Đây cũng là bước "media:pull theo game" mà DEPLOY_INDEPENDENCE §11 đã định.
- **Chép vào game thêm dòng lock** ở game đích. Drive giữ thêm một bản cho mỗi lần dùng lại: cỡ MB, là giá của luật deploy riêng. Kho Drive gom theo md5 thì hoãn, vì `media.mjs` chỉ dùng `rclone copy` và đường dẫn theo game.
- **Riêng tư.** `media/private.md5` (`shared/music`, Dota-Sounds) cho ra thẻ `private: true`, chỉ trong `library/out/`. Trang hiện chúng cho chủ dự án với dấu khóa; `lib:copy` từ chối.
- **Thư viện ngoài.** Thư viện AudioLab là `onDrive: "external"`: tải lại được từ URL trong `SOURCES.jsonl` và kiểm sha256, nên không push.
- **Mục lục và ảnh nhỏ** không push. `pnpm lib:build` sinh lại trong vài phút.
- **Máy mới.** `pnpm lib:scan --locks-only` dựng mục lục tìm được từ lock, SOURCES.json, preset và tài liệu trong Git, không cần kéo media. Ảnh nhỏ cần file. `library/CATALOG.md` đọc được ngay cả trước đó.
- **Bản trùng ở handoff** hiện như bản sao kèm số byte trong `lib:check --dupes`. Chỉ đề nghị xóa sau khi `lib:check --drive` cho thấy mọi file gốc tương ứng đã lên Drive.

---

## 8. Các bước chuyển đổi

Không bước nào dời file mà làn đang dùng. Mọi thứ ghi vào `games/` chỉ làm khi làn của game đó rảnh.

| Bước | Có gì | Đụng gì | Ảnh hưởng làn đang chạy |
|---|---|---|---|
| 0. Đóng khoảng trống Drive (AL-01, Claude) | push nốt file chính chưa lên Drive; đưa `m0b/manifest.json` của Rồng vào Git; sửa `modelsManifest` của Rồng trong `media.config.json` | `games/dragon-hold/.gitignore`, `.git/info/exclude` của Rồng, `media/media.config.json`, các `media.md5` | chỉ khi làn Rồng rảnh; không đổi đường dẫn |
| A. Mục lục (AL-02 … AL-12) | từ vựng, ngữ pháp, đọc đầu file âm, quét 2D/3D/âm, đọc bảng tài liệu, tìm, dòng tuyển chọn mồi | file mới trong `library/`, `tools/asset-library/`; lệnh trong `package.json` gốc | không: chỉ đọc `games/`; test kiểm `git status games/` không đổi |
| B. Nhìn (AL-13 … AL-16) | ảnh nhỏ, trang, thư mục Finder, `CATALOG.md`; Claude thử trang | `library/out`, `library/.thumbs`, `library/browse` (bỏ qua); `library/CATALOG.md` | không |
| C. Dùng lại (AL-17 … AL-21, AL-23) | `importedFrom` ở `models:prepare --import`; `media:pull --game --path`; `lib:copy` hình, model, âm; `verify-library` trong kit; thí điểm Tuyến Cuối | `scripts/models`, `scripts/media` (thêm, tương thích ngược), `shared/game-kit/tools` | không, cho tới khi Claude chủ động chép vào một game rảnh |
| D. Giữ (AL-22, AL-24) | `lib:check`; luật "tìm trước khi làm"; tài liệu | AGENTS.md, mẫu yêu cầu ảnh, 3D_REQUESTS, `library/README.md` | từ đây mọi yêu cầu mới dẫn `lib:find` |
| E. Sau (chủ dự án quyết) | xóa bản trùng; dời file `*rejected*` vào `_review/` bằng bản kế hoạch dời; lượt đặt tên từng game | file trong game, chỉ trong cửa sổ rảnh, chỉ khi chủ dự án đồng ý | lên lịch từng game; md5 gắn lại dòng tuyển chọn nên tìm vẫn đúng |

Thứ tự làm, kể cả phần song song: xem `TICKETS.md`.

---

## 9. Rủi ro

| Rủi ro | Cách giảm |
|---|---|
| Làn dời thư mục giữa lúc quét | Mục lục là ảnh chụp có `scannedAt`. File mất giữa chừng thành cảnh báo. Bộ quét không ghi gì trong `games/`. Chạy lại là hội tụ |
| Mục lục cũ: file mới không thấy, dòng tuyển chọn mồ côi | Quét ấm dưới 60 giây; chạy sau mỗi lần import. `lib:find` và trang tự báo cũ. `lib:check --orphans` liệt kê dòng không còn file và file chưa có loại hay tên. md5 gắn lại file đổi tên |
| Gom file sai do ngữ pháp hậu tố | Test với ca thật (herb-hut, `-v1.v1`, tripo-spares, tên Kenney, `try1` trùng md5). Vai trò `unknown` được liệt kê, trần 1 % |
| Tên hay nhãn mồi sai (dịch id Việt dở) | Trường `nameSource` và `reviewed`; trang có chấm "chưa duyệt". Claude duyệt nhóm hay tìm trước, nhìn ảnh nhỏ |
| Chữ Việt không dấu nhiều nghĩa ("cau", "da") gây kết quả sai | Ánh xạ chữ Việt → Anh chỉ áp ở thư mục được ghi; dòng tuyển chọn thắng |
| Lộ thứ riêng tư lên repo công khai | Thẻ riêng tư chỉ ở `library/out/` và `library/private/` (bỏ qua). Test đọc `media/private.md5` trên máy và kiểm không tên file nào trong đó xuất hiện ở file Git theo dõi dưới `library/`. Dòng tuyển chọn không chứa prompt |
| Lộ giấy phép: nhạc riêng, tiếng Valve, bản fork GPL monkeytype, 28 file Space không rõ nguồn | Danh sách cấm; cờ `private` và `notForRelease`; `lib:copy` từ chối cứng; không bao giờ quét monkeytype |
| Ổ đĩa (62 GiB trống lúc 12:10, có lúc đầy) | Không chép media. Ảnh nhỏ tối đa 40 KB mỗi cái, 150 MB tổng. Kiểm trước: dưới 20 GiB trống thì không sinh ảnh nhỏ. Chép vào game dùng clone APFS. Chỉ báo bản trùng, không tự xóa |
| Hai mục lục: sổ Map Factory và thư viện | Thư viện gọi hàm của `scan-assets.mjs` và dùng lại kết quả của nó khi md5 khớp. Kit bản đồ gọi món bằng uid dạng ngắn `<game>:<id>`. Cho sổ đọc nhãn từ `taxonomy.json` là việc để sau, khi làn bản đồ rảnh |
| Trang `file://` bị trình duyệt chặn | Dữ liệu nạp bằng `<script src>`, không fetch; đường dẫn tương đối; `canPlayType` + `lib:play` cho âm |
| Đụng Tu Tiên | Danh sách cấm trong `sources.json` và trong mã; test kiểm không đường dẫn nào trong mục lục chứa `immortality-cultivation` hay `tu-tien`; `lib:copy` từ chối đích đó |
| Âm Space trong Git (116 file khóa bởi `legacy-audio.json`, khoảng 40 đường dẫn cứng) | Thư viện chỉ đọc, không dời, không đổi tên |
| AudioLab dọn `work/` làm mất nguồn | Bước phát hành chép dòng nguồn và giấy phép vào game; `lib:check --audiolab` báo chỗ thiếu; thư viện lập mục lục bản trong game |
| Dùng lại lệch phong cách | Trục `style`; trường `similar` ghi phong cách hai bên. Ca dot3 để chủ dự án quyết |
| Codex không nhìn được ảnh, không nghe được âm | Codex làm phần máy móc. Tên, nhãn nhìn hay nghe mới biết, và thử trang, là việc Claude |
| Phiếu xung đột số với hàng đợi Codex (050, 051 đã dùng) | Phiếu mang mã AL-xx; Claude gán số trống kế tiếp lúc xếp vào `docs/codex-queue` |

---

## 10. Việc cần chủ dự án quyết

Chỉ hai quyết định, cộng một lần thử:

1. **Đợt Tripo dot3 của Rồng: dùng lại hay làm mới?** dot3 có 8 ảnh `rong_`, 0 GLB. Ba ảnh trùng món đã có:

   | Rồng xin | Đã có |
   |---|---|
   | `rong_wooden-jetty` (2D 9) | `typing-defense:landmarks/cau-tau` (3D 9 đạt, 7.465 tam giác) + bản dự phòng `cau-tau.alt.glb` (9) |
   | `rong_reed-clump` | `typing-defense:scenery/meadow/reed-clump` (2D, billboard) |
   | `rong_wildflower-clump` | `typing-defense:scenery/meadow/wildflowers` (2D, billboard) |

   Hai game khác phong cách (rừng thông huyền thoại so với làng Việt). Claude đặt hai bên cạnh nhau trên một tờ ghép trong AL-12 và ghi đề nghị. Chủ dự án chọn trước khi tiêu credit Tripo của mình.

2. **Xóa bản trùng?** `lib:check --dupes` liệt kê kèm số byte. Ứng viên:
   - Space `art-src/models/raw` (160 GLB trùng `art-src/3d`, khoảng 1,75 GB, không có trong lock);
   - các thư mục handoff `tripo-upload*` (627 MB), chỉ sau khi `lib:check --drive` xác nhận mọi file gốc tương ứng đã lên Drive;
   - `tools/art-normalize/.tmp` (1,5 GB ảnh chạy thử).

   Agent không xóa. Nếu đồng ý, chủ dự án tự xóa sau khi `pnpm media:check` đạt; Claude báo dung lượng trống trước và sau.

3. **Thử một phút** (nghiệm thu, không phải quyết định): mở `library/out/catalog.html`, tìm mọi chòi và nhà, rồi tìm và nghe một tiếng click gỗ. Mỗi việc dưới một phút.

Claude tự quyết, theo việc chủ dự án đã giao: lược đồ, từ vựng, thứ tự phiếu, thước tạm cho âm thanh (4.1), nhóm tuyển chọn trước (công trình và kết cấu, thiên nhiên theo vùng, âm UI), và việc đưa `m0b/manifest.json` vào Git.

---

## 11. So với bản thắng: đã sửa gì

| Lỗi giám khảo nêu | Sửa |
|---|---|
| Sổ chép `art-src/LIBRARY_IMPORTS.json` bị `art-src/*` bỏ qua ở cả bốn game | `games/<g>/library.lock.json` ở gốc game; thêm `importedFrom` trong SOURCES.json (bộ `index-3d-sources.mjs` giữ trường này như `downloadedAs`) và trong manifest |
| `curated/music.jsonl` đưa tên nhạc riêng lên repo công khai | Không có dòng tuyển chọn riêng tư nào trong Git; test chặn rò |
| 13 phiếu, phiếu quét và phiếu tìm quá to; Blender tới 300 lần; CLAP | Tách quét thành lõi / nối nguồn / âm; tách tìm thành lõi / lệnh. Blender chỉ cho GLB không có ảnh nguồn, trần 150. CLAP để sau |
| Trang HTML tới 15 MB | Trang nhỏ + `catalog.data.js`, tổng dưới 8 MB |
| Mục lục cũ mà không báo | Trang và `lib:find` tự báo cũ |
| Không có thư mục xem bằng Finder | `library/browse/` toàn liên kết, 0 byte |
| Không có kiểm md5 lúc build | `verify-library.mjs` trong kit, chạy trong `check` của game |
| Nghe thử dựa vào `file://` và `afplay` | `canPlayType` trên trang; `lib:play` có đường lui `ffmpeg` → WAV |
| Âm thư viện phải qua công thức | Chép thẳng (byte hoặc `--transcode 48k`) là mặc định; công thức chỉ khi cần xử lý |
| Chép thường, không clone; không kéo được một file | Clone APFS; `media:pull --game --path` |
| Số phiếu trùng hàng đợi Codex | Mã AL-xx, số hàng đợi gán lúc xếp |
| Không có cổng trạng thái, `rejectedMd5`, kiểm yêu cầu trước Tripo | Cổng ở 6.3; `rejectedMd5` trên thẻ; `lib:check --requests` quét các dòng 3D_REQUESTS chưa làm và ảnh handoff chưa có GLB |
| Nguồn âm AudioLab mất khi dọn `work/` | `sourceRow` và `licenceRow` trong sổ chép; `lib:check --audiolab` |
| Usedby ghi `Sfx.ts:672` thay vì glob | Ghi cả hai: glob ở `:36`, chỗ phát ở `:672` |
| Độ dài `click.ogg` 10 ms bị nghi đọc sai | Đã đo: đúng 10 ms (ffprobe, afinfo) |

---

## 12. Để sau

- Dời file `*rejected*` của Rồng (507 file ngoài `_review`) vào `_review/` bằng một công cụ kế hoạch dời: giữ md5, viết lại đường dẫn lock, có alias `moved`. Chỉ trong cửa sổ rảnh, khi chủ dự án đồng ý.
- Nhãn âm thanh bằng CLAP (mô hình đã có trong `~/AudioLab/models`), khi nhãn tay không đủ.
- Sổ Map Factory đọc nhãn từ `library/taxonomy.json` thay cho 30 từ cố định.
- Tab "Thư viện" trên Bảng Nghe (`pnpm audio:board`), nếu trình duyệt chặn nghe thử qua `file://`.
- `lib:pull <uid>`: kéo riêng file của một thẻ từ Drive lên máy mới, để xem trước mà không kéo cả bộ.
- Kho Drive gom theo md5, nếu dung lượng Drive thành vấn đề.
