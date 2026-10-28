# Thư viện tài sản: phiếu làm việc (28/10/2026)

**Đi kèm:** `ASSET_LIBRARY.md` cùng thư mục (gọi tắt là "thiết kế"; số mục § theo file đó).

**Tổng:** 25 phiếu. Codex 19 (mỗi phiếu dưới một giờ), Claude 5, chủ dự án 1.

**Số phiếu.** Mã AL-xx là mã thiết kế. Khi xếp phiếu Codex vào `docs/codex-queue/`, Claude gán số trống kế tiếp (kiểm `ls docs/codex-queue` lúc xếp; 050 và 051 đã dùng cho lượt tên tiếng Anh). Tên file: `<số>-al-xx-<tên>.md`. Báo cáo: `docs/codex-queue/<số>-report.md`.

## 0. Thứ tự

```text
Song song từ đầu:  AL-01 (Claude, khi làn Rồng rảnh)   AL-02   AL-03   AL-04   AL-17   AL-18   AL-21
Tuần tự (cùng sửa scan.mjs):  AL-05 → AL-06 → AL-07 → AL-08
Rồi:  AL-09 → AL-10 → AL-11 → AL-12 (Claude: duyệt, commit, tuyển chọn, tờ ghép dot3)
Sau AL-12:  AL-13 → AL-14      AL-15      AL-19 (cần AL-17, AL-18) → AL-20      AL-22
Sau AL-14, AL-15:  AL-16 (Claude: thử trang)
Sau AL-19, AL-21:  AL-23 (Claude: thí điểm Tuyến Cuối, khi làn rảnh)
Cuối:  AL-24 (Claude: nối quy trình)   AL-25 (chủ dự án; quyết định dot3 làm được ngay sau AL-12)
```

## 1. Luật chung

### 1.1 Mọi phiếu Codex

- **Thư mục làm việc:** repo cha `/Users/toandx/htdocs/typing-game`.
- **Chỉ được ghi:** đúng các đường dẫn phiếu liệt kê, cộng file báo cáo của phiếu.
- **Cấm:**
  - lệnh git có ghi (`add`, `commit`, `checkout`, `stash`, `reset`, `clean`…);
  - mạng, trình duyệt, dev server, server bất kỳ;
  - `pnpm media:push`; `pnpm media:pull` thật (chỉ chạy với rclone giả trong test);
  - xóa, dời, đổi tên, chép file ngoài thư mục tạm do test tự tạo dưới `os.tmpdir()`;
  - ghi bất kỳ gì dưới `games/**`, `shared/music`, `~/AudioLab`, `typing-game-handoff-2026-10-25` (những nơi này chỉ đọc);
  - ghi `.cache/media-hash.json` (chỉ đọc);
  - đọc hay ghi Tu Tiên: `games/immortality-cultivation`, `docs/games/tu-tien`, `TU_TIEN_*.md`, bản chép Tu Tiên trong handoff;
  - đọc `games/monkeytype` (GPL);
  - thêm gói npm hay pip (chỉ Node có sẵn; Python chỉ khi phiếu ghi rõ).
- **Kiểm chung, bắt buộc ở mọi phiếu:**
  - **K1 · Chỉ ghi chỗ được ghi.** Test của phiếu chạy công cụ với một lớp bọc `fs` (hoặc trên cây mẫu đã `chmod -R a-w`). Mọi lời gọi ghi (`writeFile`, `appendFile`, `mkdir`, `rename`, `copyFile`, `symlink`, `unlink`, `rm`, `open` có cờ ghi) phải nằm dưới thư mục được ghi của phiếu hoặc thư mục tạm của test.
  - **K2 · Cây Git.** `git status --porcelain` lúc cuối, so với lúc đầu, chỉ **thêm hoặc sửa** file trong danh sách được ghi. Dòng khác dưới `games/` (làn khác đang chạy) phải không phải do công cụ: báo cáo ghi cả hai bản `git status --porcelain games/`.
  - **K3 · Tu Tiên.** Nếu phiếu sinh file dưới `library/out` hay `library/.thumbs`: `grep -rlE 'immortality-cultivation|tu-tien' library/out library/.thumbs` không in gì. Chuỗi `immortality-cultivation` chỉ được có trong danh sách cấm của `library/sources.json` và trong mã danh sách cấm.
  - **K4 · Test.** `node --test <file test của phiếu>` đạt.
- **Thiếu quyền đọc `~/AudioLab` hay thiếu `ffprobe`, `magick`, Blender:** test bỏ qua phần đó, in rõ lý do. Claude chạy lại phần thật khi duyệt.
- **Quá một giờ:** dừng ở phần đã xong, ghi phần còn lại vào báo cáo.
- **Báo cáo:** tiếng Việt; danh sách file tạo hay sửa; kết quả từng kiểm, kèm số in ra.

### 1.2 Mọi phiếu Claude

- Commit vào repo cha trên một nhánh riêng `asset-library` (worktree riêng nếu checkout chính đang bẩn). Không media trong commit: `git diff --cached --stat` chỉ có `json`, `jsonl`, `mjs`, `py`, `md`, `md5`.
- Ghi vào một repo game chỉ khi làn của game đó rảnh, trên nhánh chính của game.
- Chỉ Claude chạy `pnpm media:push`.
- Ảnh chụp kiểm thử: ghép vào tờ, rồi dọn ảnh thô bằng `tools/capture-prune`.
- Commit kết thúc bằng dòng ghi công của phiên.

---

## 2. Phiếu

### AL-01 · [claude] Đóng nốt khoảng trống Drive và sổ model của Rồng

**Cần trước:** không. Phần push làm ngay; phần Git của Rồng chờ làn Rồng rảnh.

**Chỉ được ghi:**
- `games/dragon-hold/.gitignore`; file exclude cục bộ của repo Rồng (`git -C games/dragon-hold rev-parse --git-path info/exclude`);
- `games/dragon-hold/public/assets/dragon-hold/models/m0b/manifest.json` (đưa vào Git, không sửa nội dung);
- `games/typing-defense/art-src/3d/SOURCES.json` (qua `pnpm models:index`);
- `media/media.config.json` (chỉ trường `modelsManifest` của dragon-hold);
- các `games/*/media.md5` (qua `pnpm media:push`).

**Cấm:** dời, đổi tên, xóa file media; sửa nội dung manifest; đụng Tu Tiên.

**Việc:**
1. `pnpm media:status`. Ghi lại file chưa có trong lock theo game.
2. Lời Gọi: 157 GLB trong `art-src/3d`, 156 dòng lock (đo 12:10). Chạy `pnpm models:index --root games/typing-defense`, rồi push.
3. Rồng: mở `.gitignore` theo mẫu ba dòng của Lời Gọi (`!public/assets/dragon-hold/**/`, `!public/assets/dragon-hold/**/manifest.json`). Sửa dòng `public/assets` trong file exclude cục bộ để không chặn manifest. Commit `m0b/manifest.json` trong repo Rồng.
4. `media/media.config.json`: `modelsManifest` của dragon-hold → `public/assets/dragon-hold/models/m0b/manifest.json`.
5. `pnpm media:push` cho mọi file chính còn thiếu ở art-src/3d, art-src/models và public/assets của ba game.

**Kiểm (bắt buộc):**
1. `git -C games/dragon-hold check-ignore -v public/assets/dragon-hold/models/m0b/manifest.json` không in gì; `git -C games/dragon-hold ls-files` có đường dẫn đó.
2. Số GLB trong `games/typing-defense/art-src/3d` = số dòng `art-src/3d/.*\.glb` trong lock = số mục `files` của SOURCES.json (in cả ba).
3. `pnpm media:status` không còn file chưa khóa dưới `art-src/3d`, `art-src/models`, `public/assets/*/models` của Rồng, Lời Gọi, Space (trừ `models/raw` của Space, có chủ ý).
4. `pnpm media:test` và `pnpm media:check` đạt.
5. Diff của lock chỉ có dòng **thêm**.

**Xong khi:** năm kiểm đạt, commit ở repo Rồng (manifest, `.gitignore`) và repo cha (`media.config.json`, các lock).

---

### AL-02 · [codex] Từ vựng, từ đồng nghĩa, danh sách quét

**Cần trước:** không.

**Chỉ được ghi:** `library/.gitignore`, `library/taxonomy.json`, `library/sources.json`, `library/licences.json`, `tools/asset-library/lib/taxonomy.mjs`, `tools/asset-library/test/taxonomy.test.mjs`.

**Việc:**
- `library/.gitignore`: `out/`, `.thumbs/`, `.cache/`, `browse/`, `browse.new/`, `private/`.
- `taxonomy.json` theo thiết kế §3.6:
  - loại và loại con, mỗi cái có nhãn tiếng Việt cho menu; 16 loại hình/3D, 14 loại âm;
  - ít nhất 120 từ nhãn tiếng Anh, gồm đủ 30 từ của `inferTags` (đọc `tools/map-factory/registry/scan-assets.mjs` dạng chữ);
  - nhóm đồng nghĩa: lấy `SYNONYMS` của `tools/tripo-match/match.mjs`, thêm tiếng Việt có dấu và không dấu; nhóm liên quan;
  - `viTokens`: chữ Việt không dấu → từ Anh, kèm danh sách thư mục được áp (`cau` → bridge chỉ ở `typing-defense:landmarks`; `da` → stone chỉ ở `scenery/`, `landmarks/`);
  - vùng; phong cách theo game; trạng thái; bước làm (`pipeline`);
  - `folderMap` cho mọi thư mục cấp 1 (và cấp 2 khi thư mục tách đôi: `props/pine-river`, `scenery/<vùng>`, `landmarks` từng món) dưới `art-src` và `art-src/3d` của dragon-hold, typing-defense, typing-survival, space-typing, cộng các thư mục âm của Space; cờ `perItem`, `hyphenVariants`;
  - `audioFamilyMap` cho 9 họ AudioLab.
- `sources.json`: gốc quét (4 game × `art-src`, `public`, `src/assets`; `~/AudioLab/libraries`; `~/AudioLab/work` ở chế độ nháp; `shared/music` ở chế độ riêng; handoff ở chế độ chỉ-tìm-bản-sao); danh sách cấm (Tu Tiên, bản chép Tu Tiên trong handoff, `games/monkeytype`); thư mục bỏ qua (`tmp/`, `.wt-*`, `dist/`, `.visual/`, `.media-tmp/`, `node_modules/`, `library/browse/`).
- `licences.json`: `owner-tripo`, `owner-ai-2d`, `cc0-1.0`, `cc-by-4.0`, `stability-community`, `repo-synth`, `unknown`, `private-producer`, `private-valve`, mỗi khóa có `commercialOk`, `attribution`, `aiInputAllowed`, `private`, `notForRelease`.
- `taxonomy.mjs`: `load()`, `resolve(word, {folder})`, `related(a, b)`, `kindFor(game, relPath)`, `styleFor(game)`.

**Kiểm (bắt buộc):** K1–K4, và:
1. Test đi thật (chỉ đọc tên thư mục) các thư mục cấp 1 ở trên; hỏng nếu có thư mục chưa ánh xạ (bỏ qua `_review`, `review-vs*`, `_from-downloads`, `tmp`, thư mục bắt đầu bằng dấu chấm). In danh sách đã đi.
2. Không từ nào thuộc hai nhóm đồng nghĩa.
3. `resolve` của `hut`, `chòi`, `choi`, `lều`, `leu` đều ra `hut`; `resolve('nhà')` ra `house`; `related('hut','house')` là true.
4. `resolve('cau', {folder: 'typing-defense:landmarks'})` ra `bridge`; `resolve('cau')` không thư mục ra `null`.
5. Mọi khóa `CATEGORIES` và `FAMILIES` trong `tools/audio-lab/specs/taxonomy.py` (đọc dạng chữ) có ánh xạ.
6. `taxonomy.json` không quá 60 KB; ghi lại với khóa đã sắp cho đúng từng byte.

**Xong khi:** sáu kiểm đạt.

---

### AL-03 · [codex] Ngữ pháp tên file (vai trò, biến thể)

**Cần trước:** không (dùng `taxonomy.json` nếu đã có; nếu chưa, test dùng cờ thư mục giả).

**Chỉ được ghi:** `tools/asset-library/lib/grammar.mjs`, `tools/asset-library/test/grammar.test.mjs`, `tools/asset-library/test/fixtures/grammar/*.txt` (danh sách tên file, không media).

**Việc:** hàm thuần, không I/O:
- `parsePath(relPath, ctx)` → `{stem, role, variant, ticket, size, view, tier}`;
- `groupFiles(paths, ctx)` → thẻ theo stem.
Theo bảng thiết kế §3.5: nháp `.vN`/`.tryN` (dấu chấm); biến thể `-vN` chỉ trong thư mục có `hyphenVariants`; `.rejected-<phiếu>` ở bất kỳ đâu; `.tripo`; multiview `_front/_back/_left`; phái sinh `.alpha/.flat/.padded/.seamless/.trim/.crop/.coal/.fix`; `icons/normalized/*.64|.256`; sidecar `.prompt.txt` gắn vào stem; `tripo-spares` `.alt/.r2/*-old.*/*.raw-download-*` và `.r2-rejected`; bậc `.high/.medium`; biến thể âm `_000`, `_rr1`, `-1`, số cuối (`click1`); hậu tố `-2d` của Space qua liên kết `image`. Vai trò `unknown` cho phần còn lại. (Ca "`.try1` trùng md5 với file chính là bản sao" thuộc AL-06, không thuộc ngữ pháp.)

**Kiểm (bắt buộc):** K1–K4, và:
1. Danh sách thật `find games/dragon-hold/art-src -iname '*herb-hut*'` (32 tên, lưu vào fixture) cho đúng một stem `houses/herb-hut` với: concept 1, tripo-source 1, glb-original 1, glb-processed 1, icon 1, icon-256 1, icon-64 1, rejected 9, prompt 14, report 2.
2. `scenery/meadow/bamboo-clump-v1.v1.png` (Lời Gọi): biến thể a, vai trò draft. `tripo-spares/barracks.r2-rejected.glb`: rejected. Kenney `click_001..005`: một stem `click`, 5 biến thể. `impactWood_light_000..004`: stem `impactWood_light`. VCSL `wood_click_f_rr1`: stem `wood_click_f`.
3. Chạy thử trên danh sách tên của `games/dragon-hold/art-src` và `games/typing-defense/art-src` (chỉ liệt kê tên): số vai trò `unknown` không quá 1 % số file; in và liệt kê.

**Xong khi:** ba kiểm đạt.

---

### AL-04 · [codex] Đọc đầu file âm thanh

**Cần trước:** không.

**Chỉ được ghi:** `tools/asset-library/lib/audio-header.mjs`, `tools/asset-library/test/audio-header.test.mjs`, `tools/asset-library/test/fixtures/audio/**` (file nhỏ do test tự sinh, dưới 50 KB tổng).

**Việc:** chỉ Node có sẵn. Đọc WAV (PCM, float), OGG Vorbis và Opus (độ dài từ granule cuối; Opus trừ pre-skip), MP3 (Xing/VBRI hoặc quét frame), M4A (`mvhd`). Trả `{codec, sampleRate, channels, durationMs, bytes}`.

**Kiểm (bắt buộc):** K1–K4, và:
1. 60 file lấy với hạt giống cố định từ `~/AudioLab/libraries/index.json` (kenney và vcsl): `sampleRate`, `channels` khớp đúng index; độ dài lệch không quá 5 ms hoặc 1 %.
2. Đủ 116 file âm của Space (`games/space-typing/public/assets/audio/**`, `src/assets/audio/ui/*`): khớp `/opt/homebrew/bin/ffprobe` trong 10 ms. `src/assets/audio/ui/click.ogg` ra vorbis, 44100 Hz, 1 kênh, 10 ms.
3. Cả lượt chạy dưới 5 giây. `dependencies` trong `package.json` không đổi.

**Xong khi:** ba kiểm đạt (kiểm 1 được bỏ qua có thông báo khi không đọc được `~/AudioLab`).

---

### AL-05 · [codex] Quét lõi 2D và 3D

**Cần trước:** AL-02, AL-03.

**Chỉ được ghi:** `tools/asset-library/scan.mjs`, `tools/asset-library/lib/hash-cache.mjs`, `tools/asset-library/test/scan-core.test.mjs`, `tools/asset-library/test/fixtures/scan/**` (PNG và GLB nhỏ do test tự sinh), `library/out/catalog.json`, `library/out/scan-report.md`, `library/.cache/hash.json`.

**Cấm thêm:** sửa `tools/map-factory/**` (chỉ `import` các hàm xuất ra).

**Việc:**
- Đi các gốc trong `library/sources.json` (chỉ 4 game, phần ảnh và GLB); tôn trọng danh sách cấm và thư mục bỏ qua; không đi theo symlink thư mục.
- Băm md5 + sha256 qua `hash-cache.mjs`: mồi chỉ đọc từ `.cache/media-hash.json` khi cỡ và mtime khớp; chỉ băm file mới; lưu ở `library/.cache/hash.json`.
- Ảnh: `imageHeader` (rộng, cao, alpha). GLB: lấy số đo từ `tools/map-factory/registry/out/assets.<game>.json` khi md5 khớp, ngược lại `inspectGlb`.
- Gom thẻ bằng `grammar.mjs` + luật gương; loại từ `kindFor`; phong cách từ `styleFor`.
- Ghi `catalog.json` (`schema: asset-library/1`, `scannedAt`, thẻ đã sắp theo uid) và `scan-report.md` (số thẻ, số file theo vai trò, `unknown`, cảnh báo).
- File biến mất giữa lúc đi (ENOENT) thành cảnh báo. Cờ `--game <id>` và `--scan-date <iso>` (cho test).

**Kiểm (bắt buộc):** K1–K4, và:
1. Test cây mẫu đã `chmod -R a-w`: quét đạt.
2. Hai lần chạy với cùng `--scan-date` cho `catalog.json` giống từng byte.
3. Test xóa một file mẫu giữa lúc đi (qua móc test): kết thúc bằng cảnh báo, mã thoát 0.
4. Chạy thật: in số `glb-original` theo game, cạnh `find games/<g>/art-src/3d -name '*.glb' | wc -l` (dragon-hold, typing-defense, space-typing). Hai số bằng nhau.
5. Không đường dẫn nào trong `catalog.json` chứa `immortality-cultivation` hay `tu-tien`.
6. Lần chạy thứ hai (ấm) dưới 60 giây; in thời gian.

**Xong khi:** sáu kiểm đạt.

---

### AL-06 · [codex] Quét: nối sổ, lock, bản sao, dòng tuyển chọn

**Cần trước:** AL-05.

**Chỉ được ghi:** `tools/asset-library/scan.mjs`, `tools/asset-library/lib/joins.mjs`, `tools/asset-library/test/scan-joins.test.mjs`, `tools/asset-library/test/fixtures/joins/**`, `library/out/**`.

**Việc:**
- Nối: `art-src/3d/SOURCES.json` (`image`, `usedBy`, `downloadedAs`, `notMadeYet`); preset (`scripts/models/presets/*.json`, `games/*/scripts/models/presets/*.json`, trường `source`); mọi `public/assets/<g>/models/**/manifest.json` (gồm `m0b/` của Rồng).
- `onDrive` từ `games/<g>/media.md5`: `yes`, `changed`, `no`. `private` từ `media/private.md5` (đọc trên máy; không chép tên nào ra ngoài `library/out`).
- Bản sao theo md5: handoff ở chế độ chỉ-tìm-bản-sao (không trùng thì thành thẻ nháp `handoff:<path>`); `art-src/models/raw` của Space chỉ là bản sao; `.tryN`/`.vN` trùng md5 với file chính là bản sao `same-folder`, không phải nháp; 6 bản Draconis ở Rồng có `copyOf`.
- `rejectedMd5`, `canonical` mỗi vai trò, `pipeline`, `status` từ vai trò (`shipped` khi manifest runtime có khóa).
- Đọc `library/curated/*.jsonl` nếu có: gắn theo uid, nếu không thấy thì theo `md5s` (ghi `formerUids`); trường tuyển chọn thắng trường tự sinh.
- `--locks-only`: dựng thẻ chỉ từ lock, SOURCES.json, preset, manifest có trong Git (`local: false`).

**Kiểm (bắt buộc):** K1–K4, và:
1. Thẻ `dragon-hold:houses/herb-hut` có 9 file hiện (concept, tripo-source, glb-original, glb-processed, runtime-high, runtime-medium, icon, icon-256, icon-64) và `hiddenFiles` rejected 9, prompt 14, report 2. `onDrive` từng file khớp `grep` dòng tương ứng trong `games/dragon-hold/media.md5` (in cả hai).
2. Thẻ `dragon-hold:props/pine-river/wooden-jetty`: `wooden-jetty.try1.png` là bản sao `same-folder`; `rong_wooden-jetty.png` của dot3 là bản sao `handoff`; `pipeline` là `tripo-requested`.
3. Không thẻ nào có file chính nằm dưới `art-src/models/raw` (in số 0).
4. 6 file Draconis runtime ở Rồng có `copyOf` trỏ `space-typing`.
5. Test: dòng tuyển chọn của một file mẫu bị đổi tên vẫn gắn được theo md5 và có `formerUids`.
6. `--locks-only` trên repo thật cho ít nhất 90 % uid của lượt quét đầy đủ (in hai số).

**Xong khi:** sáu kiểm đạt.

---

### AL-07 · [codex] Đọc bảng tài liệu (doc facts)

**Cần trước:** AL-06.

**Chỉ được ghi:** `tools/asset-library/doc-facts.mjs`, `tools/asset-library/scan.mjs` (chỉ bước gộp `doc-facts.json`), `tools/asset-library/test/doc-facts.test.mjs`, `tools/asset-library/test/fixtures/docs/**`, `library/out/doc-facts.json`.

**Cấm thêm:** đọc `docs/games/tu-tien/**`.

**Việc:** đọc bảng Markdown của `docs/games/NAMES_EN.md`, `3D_REQUESTS.md`, `3D_IMPORT_2026-10-26.md`, `3D_IMPORT_2026-10-28.md`, `ART_REPLACE_LATER.md`, `IMAGE_AUDIT_2026-10-25.md` và `typing-game-handoff-2026-10-25/tripo-upload*/INDEX.md`. Ghi theo game+id và theo đường dẫn file: tên Anh, tên Việt, nghĩa, điểm 2D/3D (dấu phẩy thập phân → chấm), mức (Đạt → pass, Tạm chấp nhận → provisional), cần P1–P3, file Tripo, tam giác, face limit, rig, độ tin, bằng chứng `file:dòng`. Tiền tố `rong_`, `loigoi_`, `tuyencuoi_` → game. `scan.mjs` gộp vào thẻ (sau dòng tuyển chọn về độ ưu tiên).

**Kiểm (bắt buộc):** K1–K4, và:
1. Số dòng đọc được mỗi tài liệu (in) bằng `grep -c '^| '` trừ dòng tiêu đề và dòng kẻ. Ít nhất: 3D_IMPORT_2026-10-28 86 dòng, 3D_IMPORT_2026-10-26 55, NAMES_EN khoảng 148.
2. `choi-canh-doi`: điểm 3D 9, pass, file Tripo `thatched+hut+3d+model (2).glb`, 7733 tam giác. `nha-rai-da`: 8,5, provisional. `barracks-kit-l2`: `wooden+hut+3d+model.glb`. `herb-hut`: tên Anh `Herb Hut`, điểm 2D 9,5 (IMAGE_AUDIT H1), file Tripo `fantasy+cottage+3d+model.glb`.
3. Mọi đường dẫn ở cột File và Đích hoặc có trên ổ đĩa, hoặc nằm trong `missing[]` (in danh sách).

**Xong khi:** ba kiểm đạt.

---

### AL-08 · [codex] Quét âm thanh

**Cần trước:** AL-04, AL-07.

**Chỉ được ghi:** `tools/asset-library/scan-audio.mjs`, `tools/asset-library/scan.mjs` (chỉ bước gọi `scan-audio`), `tools/asset-library/test/scan-audio.test.mjs`, `tools/asset-library/test/fixtures/audio-scan/**`, `library/out/**`.

**Việc:**
- Âm Space: `public/assets/audio/**`, `src/assets/audio/**`, chỉ đọc. Đọc bảng trong `public/assets/audio/ATTRIBUTION.md` (Kenney, Freesound có số, tác giả, URL).
- `~/AudioLab/libraries/index.json` và `SOURCES.jsonl`: dùng sha256 sẵn trong index, không băm lại 1.859 file; `onDrive: external`. Thư viện ngoài là file chính, file Space trùng sha256 là bản sao.
- `~/AudioLab/work`: chỉ các lượt có `manifest.fragment.json` và `SOURCES.json`; trạng thái `draft`, ẩn mặc định.
- Riêng tư: `shared/music` (qua `media/private.md5` + bộ đọc đầu file) và `games/space-typing/art-src/Dota-Sounds` (`notForRelease`). Chỉ ghi vào `library/out`.
- Họ âm qua `audioFamilyMap`; gom biến thể số thành một thẻ.
- `usedBy` từ mã trong `games/*/src`: chuỗi đường dẫn âm, và thư mục của `import.meta.glob` (độ tin `folder`).

**Kiểm (bắt buộc):** K1–K4, và:
1. Đủ 116 file âm Space nằm trong thẻ.
2. Đúng 29 file Space trùng sha256 với một file Kenney; `src/assets/audio/ui/click.ogg` là bản sao trên `kenney:interface-sounds/Audio/click`, biến thể 002.
3. Báo hai cặp trùng byte: `confirm.ogg` (hai nơi) và `sfx/kenney/force-field.ogg` = `ui/deploy.ogg`.
4. 15 file Dota có `private` và `notForRelease`; 193 bài nhạc có `private`.
5. 0 thẻ AudioLab `work/` hiện khi không có `--all`.
6. `usedBy` của thẻ click chứa `games/space-typing/src/audio/Sfx.ts:36` (glob) và `:672`.

**Xong khi:** sáu kiểm đạt.

---

### AL-09 · [codex] Lõi tìm kiếm và câu tìm vàng

**Cần trước:** AL-08.

**Chỉ được ghi:** `tools/asset-library/lib/search.mjs`, `tools/asset-library/test/search.test.mjs`, `tools/asset-library/test/fixtures/catalog-small.json`, `library/test/queries.json`.

**Việc:** theo thiết kế §5.6:
- chuẩn hóa (chữ thường; bỏ dấu, đ → d; tách `- _ + . /`, khoảng trắng, camelCase; bỏ từ dừng `STOP` của tripo-match);
- mở rộng đồng nghĩa hai chiều; từ liên quan nửa điểm; `viTokens` theo thư mục;
- trọng số (tên 5, alias 4, loại con 3, loại 3, nhãn 2, đường dẫn/chú thích 1); cộng trừ (shipped/pass +1, runtime +0,5, provisional −0,5);
- lọc trạng thái ẩn trừ khi `all`; `requested` chỉ khi `requested`;
- bộ lọc như thiết kế §5.2.
Mã phải chạy được cả trong Node lẫn khi nhúng vào trang (không `import` Node, không `fs`).

`library/test/queries.json`: mỗi câu có `query`, `filters`, `mustInclude[]`, `topN`.

**Kiểm (bắt buộc):** K1–K4, và trên mục lục thật:
1. `hut --type 3d`: 6 kết quả đầu có `herb-hut`, `choi-canh-doi`, `nha-rai-da`, `barracks-kit-l2`.
2. `chòi` và `choi` ra cùng tập.
3. `jetty --type 3d`: `typing-defense:landmarks/cau-tau` trong 3 đầu.
4. `bridge`: `landmarks/cau-go` và `props/pine-river/bridge-old` trong 5 đầu.
5. `rock --biome pine-forest`: có `rock-boulder`, `rock-slab`, `river-stones`.
6. `wood click --type audio`: `kenney:impact-sounds/Audio/impactWood_light` trong 3 đầu.
7. Bản loại không hiện khi không có `all`.
8. p95 dưới 300 ms trên mục lục thật (in).

**Xong khi:** tám kiểm đạt.

---

### AL-10 · [codex] Lệnh `lib:find`, `lib:show`, `lib:play`

**Cần trước:** AL-09.

**Chỉ được ghi:** `tools/asset-library/find.mjs`, `show.mjs`, `play.mjs`, `tools/asset-library/test/cli.test.mjs`, `package.json` gốc (chỉ thêm `lib:scan`, `lib:find`, `lib:show`, `lib:play`, `lib:test`; Claude duyệt diff này).

**Việc:**
- `find.mjs`: bảng như thiết kế §5.2; `--json`; báo mục lục cũ khi một `games/*/media.md5`, `games/*/art-src/3d/SOURCES.json` hay manifest model mới hơn `scannedAt`.
- `show.mjs`: cả thẻ, bảng file theo vai trò, lệnh `lib:copy` đúng; `--all`, `--json`.
- `play.mjs`: `afplay`; nếu `afplay` thoát lỗi, `ffmpeg` giải mã ra WAV tạm trong `library/.cache/play/` rồi `afplay`. `--variant n`.

**Kiểm (bắt buộc):** K1–K4, và:
1. Test trên mục lục mẫu: `--json` hợp lược đồ; dạng ngắn `dragon-hold:herb-hut` mở đúng thẻ.
2. Test báo cũ: tạo `media.md5` giả mới hơn `scannedAt` trong cây tạm → có dòng cảnh báo.
3. Test `play` với `afplay` giả thoát lỗi → gọi `ffmpeg` giả, rồi `afplay` giả với file WAV.
4. Chạy thật `pnpm lib:find hut --type 3d` và `pnpm lib:show dragon-hold:herb-hut`: in ra, mã thoát 0.

**Xong khi:** bốn kiểm đạt.

---

### AL-11 · [codex] Dòng tuyển chọn mồi

**Cần trước:** AL-10.

**Chỉ được ghi:** `tools/asset-library/seed-curated.mjs`, `tools/asset-library/test/seed-curated.test.mjs`, `library/curated/dragon-hold.jsonl`, `typing-defense.jsonl`, `typing-survival.jsonl`, `space-typing.jsonl`, `audio-libraries.jsonl`.

**Cấm thêm:** ghi bất kỳ dòng nào cho thẻ `private` hay `notForRelease`; ghi prompt vào dòng.

**Việc:** mỗi thẻ hiện, công khai: một dòng, đã sắp. Trường: `uid`, `md5s`, `name` (NAMES_EN → phần Anh của 3D_IMPORT → dịch mồi, `nameSource: seed-translation`), `aliases` (Việt có và không dấu, chữ trong id, chữ chú thích Tripo), `kind`/`subkind` (folderMap + `perItem`), `tags` (khớp từ vựng trên tên, chú thích, ghi chú 3D_IMPORT), `biome`, `style`, `canonical: {}`, `reuseNotes: null`, `quality: null` (chỗ Claude ghi đè điểm khi tài liệu thiếu), `reviewed: null`. Chỉ thêm dòng mới; không bao giờ ghi đè dòng có `reviewed`.

**Kiểm (bắt buộc):** K1–K4, và:
1. Ít nhất 95 % thẻ hiện có `name` và `kind`; ít nhất 80 % thẻ `model3d` có từ 2 nhãn (in).
2. Chạy lại `pnpm lib:scan` rồi mọi câu trong `library/test/queries.json` đạt.
3. Chạy `seed-curated` lần hai: 0 dòng đổi.
4. Test: dòng có `reviewed` giữ nguyên từng byte.
5. Không `name` nào có dấu tiếng Việt.
6. **Chặn rò:** test đọc `media/private.md5` (nếu có trên máy) và tên file trong `games/space-typing/art-src/Dota-Sounds`; không tên file nào (bỏ đuôi) xuất hiện trong `library/curated/*`, `library/taxonomy.json`, `library/sources.json`. Không có `private.md5` thì bỏ qua, in lý do.
7. Báo cáo liệt kê 50 tên độ tin thấp nhất để Claude duyệt.

**Xong khi:** bảy kiểm đạt.

---

### AL-12 · [claude] Duyệt, commit, tuyển chọn lượt 1, tờ ghép dot3

**Cần trước:** AL-02 … AL-11.

**Chỉ được ghi:** mọi file của AL-02 … AL-11; `library/curated/*.jsonl`; `library/out/sheets/` (bỏ qua); `.gitignore` gốc nếu cần.

**Việc:**
1. Chạy lại kiểm bắt buộc của từng phiếu, gồm phần `~/AudioLab`, `ffprobe` mà Codex bỏ qua.
2. Commit vào nhánh `asset-library` của repo cha: mã, `library/*.json`, `library/curated/*.jsonl`, `library/test/queries.json`. Không gì dưới `games/`.
3. `pnpm lib:scan`. Tuyển chọn bằng mắt, xem ảnh nhỏ hay tờ ghép (`magick montage`): mọi thẻ `building`, `structure`, `nature` theo vùng (pine-forest, meadow, coast), và âm `ui`. Sửa tên, nhãn, `canonical`, `reuseNotes`; ghi `quality` khi tài liệu thiếu (ví dụ Wooden Jetty 2D 9 từ `docs/codex-queue/046-report.md:178`); đặt `reviewed`.
4. Tờ ghép dot3: `rong_wooden-jetty`, `rong_reed-clump`, `rong_wildflower-clump` cạnh `cau-tau`, `meadow/reed-clump`, `meadow/wildflowers`, kèm đề nghị dùng lại hay làm mới. Gửi chủ dự án (AL-25 quyết định 1).

**Kiểm (bắt buộc):**
1. Mọi câu tìm vàng đạt.
2. Ít nhất 90 % thẻ `building`, `structure`, `nature` có `reviewed`.
3. Chặn rò của AL-11 đạt trên dữ liệu thật.
4. `git diff --cached --stat` không có media.

**Xong khi:** bốn kiểm đạt, commit xong, tờ ghép dot3 đã gửi.

---

### AL-13 · [codex] Ảnh nhỏ và dạng sóng

**Cần trước:** AL-12.

**Chỉ được ghi:** `tools/asset-library/thumbs.mjs`, `tools/asset-library/blender/thumb.py`, `tools/asset-library/test/thumbs.test.mjs`, `library/.thumbs/**`.

**Việc:**
- Ảnh: `magick` → `library/.thumbs/<md5>.webp`, cạnh dài 256 px, tối đa 40 KB.
- Thẻ GLB: dùng ảnh nguồn liên kết nếu có. Chỉ GLB không có ảnh nguồn mới render bằng Blender headless (`/Applications/Blender.app/Contents/MacOS/Blender -b -P thumb.py`; camera 3/4 cố định, ánh sáng trung tính, nền trong). Trần 150 lần render mỗi lượt.
- Âm: `ffmpeg showwavespic` → `<sha256>.wave.png`, mỗi bộ một hình từ biến thể đầu.
- Kiểm trước: dưới 20 GiB trống thì dừng, in lý do.
- Không làm lại: khóa theo md5/sha256.

**Kiểm (bắt buộc):** K1–K4, và:
1. Mọi thẻ hiện có ảnh nhỏ; mỗi file tối đa 40 KB; tổng tối đa 150 MB (in hai số).
2. Lượt hai tạo 0 file.
3. Số lần render Blender in ra, tối đa 150.
4. Test giả lập ổ còn ít chỗ → dừng có thông báo, không tạo file.

**Xong khi:** bốn kiểm đạt.

---

### AL-14 · [codex] Trang `catalog.html`

**Cần trước:** AL-09, AL-13.

**Chỉ được ghi:** `tools/asset-library/page.mjs`, `tools/asset-library/page/*.{html,css,js}` (khung trang), `tools/asset-library/test/page.test.mjs`, `library/out/catalog.html`, `library/out/catalog.data.js`, `package.json` gốc (chỉ thêm `lib:page`; Claude duyệt).

**Việc:** theo thiết kế §5.1:
- HTML nhỏ + `catalog.data.js` (`window.CATALOG = …`) nạp bằng `<script src>`; không fetch, không URL mạng;
- nhúng đúng `lib/search.mjs` (cùng mã, không viết lại);
- menu tiếng Việt, tên món tiếng Anh, tên Việt là chú thích xám;
- bộ lọc theo thứ tự: chữ, loại, kiểu, game, vùng, phong cách, chất lượng, trạng thái, Drive;
- lưới ảnh nhỏ; khung chi tiết (file theo vai trò, md5, Drive, đoạn prompt đọc lúc build từ file trên máy, mét, tam giác, clip, giấy phép, ai dùng, bản sao, món giống, nút nghe từng biến thể);
- nghe: `canPlayType` cho ogg vorbis/opus; không phát được thì đổi thành nút chép `pnpm lib:play <uid>`;
- nút chép lệnh (`navigator.clipboard`, đường lui chọn chữ);
- công tắc hiện bản ẩn; dòng "quét lúc …", đỏ khi quá 24 giờ;
- sáng và tối; dùng được ở 375 px.

**Kiểm (bắt buộc):** K1–K4, và (không cần trình duyệt):
1. Test nạp `catalog.data.js` bằng `node:vm`, đọc được mục lục.
2. Mọi đường dẫn ảnh nhỏ tương đối trỏ tới file có thật.
3. Hàm tìm trong trang (lấy từ file đã sinh) cho cùng 10 kết quả đầu như lệnh, với mọi câu tìm vàng.
4. `grep -cE 'https?://' library/out/catalog.html library/out/catalog.data.js` in 0 cho cả hai.
5. `catalog.html` tối đa 200 KB; hai file cộng lại tối đa 8 MB.

**Xong khi:** năm kiểm đạt. Claude thử bằng mắt ở AL-16.

---

### AL-15 · [codex] Thư mục Finder và `CATALOG.md`

**Cần trước:** AL-12.

**Chỉ được ghi:** `tools/asset-library/browse.mjs`, `tools/asset-library/catalog-md.mjs`, `tools/asset-library/test/browse.test.mjs`, `tools/asset-library/test/catalog-md.test.mjs`, `library/browse/**`, `library/browse.new/**`, `library/CATALOG.md`, `package.json` gốc (chỉ thêm `lib:browse`, `lib:thumbs`, `lib:build`; Claude duyệt).

**Việc:**
- `browse.mjs`: dựng `library/browse.new/<kind>/<subkind>/<Tên Anh> (<game>).<đuôi>` là liên kết tượng trưng tới file `hero` (âm: biến thể đầu); chỉ thẻ hiện, không thẻ riêng tư; xong thì thay `browse/` bằng `browse.new/`. Chỉ được gỡ **liên kết** trong `library/browse*`; gặp file thường thì dừng, mã thoát 2.
- `catalog-md.mjs`: `library/CATALOG.md`, tiêu đề tiếng Việt, một bảng mỗi loại; cột: tên Anh, tên Việt, uid, game làm ra, trạng thái và điểm, ai dùng. Chỉ thẻ công khai có `reviewed`. Không md5, không cỡ, không Drive.
- `lib:build` = scan → thumbs → page → browse → CATALOG.md.

**Kiểm (bắt buộc):** K1–K4, và:
1. Test: một file thường đặt trong `library/browse/` không bị gỡ; công cụ dừng mã 2.
2. Mọi liên kết trỏ tới file có thật; `du -sk library/browse` dưới 2 MB.
3. `CATALOG.md` sinh hai lần giống từng byte; không chứa md5 (không chuỗi 32 hex) và qua chặn rò của AL-11.
4. `library/browse/building/hut/` có Herb Hut và Hilltop Watch Hut (hay tên đã duyệt của chúng).

**Xong khi:** bốn kiểm đạt.

---

### AL-16 · [claude] Thử trang trên trình duyệt

**Cần trước:** AL-14, AL-15.

**Việc:** mở `library/out/catalog.html` qua `file://` trong trình duyệt. Thử tốc độ tìm, bộ lọc, công tắc bản ẩn, khung chi tiết, nghe thử, nút chép lệnh, sáng và tối, bề ngang 375 px. Mở `library/browse/building/hut/` trong Finder. Lỗi thì viết phiếu sửa cho Codex.

**Kiểm (bắt buộc):**
1. Gõ "chòi": các thẻ chòi hiện dưới 300 ms.
2. Từ lúc mở trang, tìm và nghe được một tiếng click gỗ trong 60 giây.
3. Console không lỗi.
4. Không cuộn ngang ở 375 px.
5. Ảnh chụp vào tờ ghép; ảnh thô dọn bằng `tools/capture-prune`.

**Xong khi:** năm kiểm đạt; trang sẵn cho chủ dự án thử (AL-25).

---

### AL-17 · [codex] Ghi nguồn khi import model

**Cần trước:** không.

**Chỉ được ghi:** `scripts/models/prepare-models.mjs`, `scripts/models/index-3d-sources.mjs`, `scripts/models/test/import-provenance.test.mjs`, `scripts/models/test/fixtures/import/**`.

**Cấm thêm:** đổi định dạng URL bậc (`?v=` tiền tố sha256); đổi hành vi khi không có `--import`.

**Việc:**
- `importModels()`: ghi `importedFrom: {game, manifest, key, md5High, md5Medium}` vào mỗi mục manifest được import. Trường thêm, tương thích ngược.
- `index-3d-sources.mjs`: giữ `importedFrom` của mục cũ như đang giữ `downloadedAs` (dòng 88).
- Liệt kê trong báo cáo các chỗ trong `games/*/src` đọc manifest theo lược đồ chặt (nếu có), để Claude biết.

**Kiểm (bắt buộc):** K1–K4, và:
1. `pnpm models:test` đạt (ca cũ không đổi).
2. Test mới: import một herb-hut mẫu → mục manifest có `importedFrom.game`, `key`, hai md5 đúng md5 file bậc.
3. Test: chạy `models:index` trên cây mẫu có `importedFrom` → trường còn nguyên.
4. Lượt `--manifest-only` trên mẫu Space cho đầu ra giống từng byte trước và sau sửa.

**Xong khi:** bốn kiểm đạt.

---

### AL-18 · [codex] Kéo một file từ Drive (`media:pull --game --path`)

**Cần trước:** không.

**Chỉ được ghi:** `scripts/media/**` (mã và test), `docs/MEDIA_STORAGE.md` (một đoạn mô tả cờ mới).

**Cấm thêm:** chạy rclone thật; `push`; thêm lệnh rclone ngoài `copy`, `check`, `lsjson`, `size`.

**Việc:** `pnpm media:pull --game <id> --path <glob>`: chỉ đọc dòng lock của game đó khớp glob; chép qua `.media-tmp/`, kiểm md5, rồi đặt vào chỗ. Không có `--game` và `--path` thì hành vi cũ không đổi.

**Kiểm (bắt buộc):** K1–K4, và:
1. `pnpm media:test` đạt, gồm test mới với rclone giả.
2. Glob không khớp dòng nào → mã thoát khác 0, thông báo rõ ("chưa có trong lock, Claude phải media:push game nguồn trước").
3. rclone giả trả file sai md5 → không file nào được đặt vào chỗ.
4. Ảnh chụp danh sách chép dự kiến của `pull` không cờ giống trước khi sửa.

**Xong khi:** bốn kiểm đạt.

---

### AL-19 · [codex] `lib:copy` cho hình và model

**Cần trước:** AL-06, AL-17, AL-18.

**Chỉ được ghi:** `tools/asset-library/copy.mjs`, `tools/asset-library/lib/lockfile.mjs`, `tools/asset-library/test/copy.test.mjs`, `tools/asset-library/test/fixtures/repo/**`, `package.json` gốc (chỉ thêm `lib:copy`; Claude duyệt).

**Cấm thêm:** chạy `--apply` trên repo thật; Codex chỉ chạy `--apply` trong repo mẫu dưới `os.tmpdir()`.

**Việc:** theo thiết kế §6.1 và §6.3:
- `lib:copy <uid> --to <game> [--as <kind>/<stem>] [--with icons] [--allow-unscored --reason "<…>"] [--apply]`; mặc định chạy thử, in kế hoạch;
- vai trò mặc định: concept, tripo-source, prompt, glb-original, runtime;
- chép bằng `fs.copyFile(..., COPYFILE_FICLONE)`; không clone được thì chép thường và in số byte;
- runtime: gọi `importModels()` (AL-17) với manifest nguồn và khóa;
- thêm mục SOURCES.json của game đích kèm `importedFrom`; ghi `presetStub` vào mục sổ chép và in ra (Claude gộp vào preset);
- ghi `games/<đích>/library.lock.json` (lược đồ thiết kế §4.7) và một dòng `library/imports.jsonl`;
- file nguồn không có trên máy → gọi `media:pull --game <nguồn> --path <file>` (AL-18);
- từ chối (mã thoát 2, kèm lý do): riêng tư, `notForRelease`, giấy phép `unknown` hay `commercialOk: false`, file bị loại hay md5 nằm trong `rejectedMd5`, đích là Tu Tiên, đích có file cùng đường dẫn khác md5, thẻ `unscored` chưa ship mà không có `--allow-unscored --reason`;
- `provisional` in ghi chú ART_REPLACE_LATER; CC-BY thêm dòng vào `CREDITS.md` của đích.

**Kiểm (bắt buộc):** K1–K4, và:
1. Repo mẫu: sau `--apply`, mọi file đích giống từng byte nguồn; `library.lock.json` hợp lược đồ, md5 khớp file.
2. Chạy lại cùng lệnh: không đổi gì.
3. Chạy thử không ghi gì (băm cây trước bằng sau).
4. Mỗi ca từ chối có test: file nhạc riêng, file Dota, đích Tu Tiên, xung đột md5, md5 bị loại, `unscored` không lý do.
5. Test đường lui: cờ clone không được hỗ trợ → chép thường, in byte.
6. Chạy thử trên repo thật `pnpm lib:copy dragon-hold:herb-hut --to typing-survival`: in đúng 4 clone, 1 lệnh import, 3 mục thêm (SOURCES, sổ game, `imports.jsonl`); lớp bọc `fs` xác nhận 0 lần ghi.
7. `pnpm models:test` vẫn đạt.

**Xong khi:** bảy kiểm đạt.

---

### AL-20 · [codex] `lib:copy` cho âm thanh

**Cần trước:** AL-08, AL-19.

**Chỉ được ghi:** `tools/asset-library/copy-audio.mjs`, `tools/asset-library/copy.mjs` (chỉ rẽ nhánh sang âm), `tools/asset-library/test/copy-audio.test.mjs`, `tools/asset-library/test/fixtures/repo-audio/**`.

**Cấm thêm:** chạy trên repo thật ngoài chế độ chạy thử; ghi vào `~/AudioLab`.

**Việc:** theo thiết kế §6.2:
- `lib:copy <uid> --to <game> --as <id> [--variants 1-3] [--transcode 48k] [--recipe] [--apply]`;
- chép thẳng (mặc định): clone byte, hoặc `--transcode 48k` bằng `ffmpeg` ra OGG Vorbis 48 kHz; đặt ở `public/assets/<đích>/audio/sfx/<kind>/<id-gạch-nối>-<n>.ogg`;
- gộp `public/assets/<đích>/audio/manifest.json` (v2: `sounds[id]`);
- mục sổ chép có `sourceRow` (đường dẫn, sha256 nguồn, giấy phép) và `licenceRow` (dòng `SOURCES.jsonl`);
- nếu `art-src/audio/` của đích được Git theo dõi (`git check-ignore -q`), ghi thêm dòng `art-src/audio/SOURCES.json` và `licences.jsonl` (AUDIO_PIPELINE §10.5–10.6);
- chạy `pnpm audio:licence-check` cho đích, hỏng thì hoàn tác các file vừa ghi trong lượt đó;
- `--recipe`: ghi `tools/audio-lab/build/recipes/<đích>/<id>.json` (lớp `library`, sha256, giấy phép, đích của nhóm trong `taxonomy.py`), không chép byte;
- từ chối: riêng tư, `notForRelease`, `unknown`, thẻ `draft` của AudioLab `work/`.

**Kiểm (bắt buộc):** K1–K4, và:
1. Repo mẫu: chép thẳng 3 biến thể → 3 file, manifest có `sounds["ui.select"]` đủ 3 đường dẫn, sổ chép có `sourceRow.sha256` đúng.
2. `--transcode 48k`: `ffprobe` đọc file ra vorbis, 48000 Hz (bỏ qua có thông báo khi thiếu `ffmpeg`).
3. Mỗi ca từ chối có test (một file `duel/sfx` giả có giấy phép `unknown`, nhạc riêng, Dota, nháp AudioLab).
4. `--recipe` ghi JSON hợp lệ, có sha256 nguồn và `cc0-1.0`.
5. `audio:licence-check` (hay lối vào Python của nó) đạt trên đích mẫu; không chạy được thì bỏ qua có thông báo, Claude chạy lại.

**Xong khi:** năm kiểm đạt.

---

### AL-21 · [codex] `verify-library` trong kit

**Cần trước:** không.

**Chỉ được ghi:** `shared/game-kit/tools/verify-library.mjs`, `shared/game-kit/tools/verify-library.test.mjs`, `shared/game-kit/README.md` (một đoạn).

**Cấm thêm:** chạy `kit:sync` (chép vào game là việc của Claude, khi làn rảnh).

**Việc:** script Node, chỉ dùng thư viện có sẵn:
- đọc `<gốc game>/library.lock.json`; không có file → in "không có món nào từ thư viện", mã 0;
- mỗi file `stage: runtime`: sai md5 → lỗi, mã 1; thiếu → cảnh báo, hoặc lỗi khi có `--strict`;
- in `uid` từng món;
- không đọc gì ngoài gốc game.

**Kiểm (bắt buộc):** K1–K4, và:
1. `node --test shared/game-kit/tools/verify-library.test.mjs`: đạt trên game mẫu; hỏng rõ ràng khi sai md5; thiếu file là cảnh báo, là lỗi với `--strict`; không có sổ thì đạt.
2. Test tĩnh: mã không có `..` trong đường nối, không có đường dẫn tuyệt đối tới repo cha.
3. `node scripts/sync-game-kit.mjs --check`: các game chỉ lệch đúng `tools/verify-library.mjs` (và bản kê kit); in danh sách.

**Xong khi:** ba kiểm đạt.

---

### AL-22 · [codex] `lib:check`

**Cần trước:** AL-07, AL-09.

**Chỉ được ghi:** `tools/asset-library/check.mjs`, `tools/asset-library/test/check.test.mjs`, `tools/asset-library/test/fixtures/check/**`, `library/out/check-*.json`, `package.json` gốc (chỉ thêm `lib:check`; Claude duyệt).

**Việc:**
- `--drive`: file chưa lên Drive theo game, kèm byte, file chính trước.
- `--dupes`: bản sao byte theo loại chỗ, kèm byte lấy lại được. Chỉ báo.
- `--orphans`: dòng tuyển chọn không còn file; file vai trò `unknown`; vai trò có hai file chính.
- `--request "<chữ>"`: thẻ giống, kể cả `requested` và `draft`.
- `--requests`: đọc các dòng 3D_REQUESTS chưa làm và các thẻ nháp `handoff:` chưa có GLB; in món đã có cho từng dòng, chấm thêm hình khối và tam giác bằng hàm của `tools/tripo-match/match.mjs`.
- `--stale`: mục lục cũ hơn lock, SOURCES hay manifest.
- `--audiolab`: âm đã phát hành vào game mà dòng nguồn chưa nằm trong sổ chép hay `art-src/audio/SOURCES.json` nào.
- Lệch cấu hình: đường dẫn `modelsManifest` trong `media.config.json` không tồn tại.
- Mã 0 khi chỉ có cảnh báo; 1 khi lỗi lược đồ.

**Kiểm (bắt buộc):** K1–K4, và:
1. Mỗi luật có test trên cây mẫu (gồm lệch `modelsManifest`).
2. Chạy thật `--dupes`: in tổng GLB và ảnh trên 100 KB, cạnh số khảo sát (2,19 GB và 1,33 GB); lệch quá 5 % thì giải thích trong báo cáo (đã có dọn đĩa trong ngày).
3. `--request "wooden jetty" --type 3d`: `typing-defense:landmarks/cau-tau` đứng đầu.
4. `--requests`: in ít nhất `rong_wooden-jetty` → `cau-tau`, `rong_reed-clump` → `meadow/reed-clump`, `rong_wildflower-clump` → `meadow/wildflowers`.
5. `--drive` chạy thật, in số theo game (sau AL-01 phải gần 0 ở art-src/3d).

**Xong khi:** năm kiểm đạt.

---

### AL-23 · [claude] Thí điểm: 7 model Space vào Tuyến Cuối

**Cần trước:** AL-19, AL-21. Làm khi làn Tuyến Cuối rảnh.

**Chỉ được ghi:** `games/typing-survival/**` (mã, `.gitignore`, `library.lock.json`, `art-src/3d/SOURCES.json`, `kit`), `infra/nginx/*.conf` (hai alias), `games/typing-survival/media.md5` (qua push), `library/imports.jsonl`.

**Việc:**
1. `pnpm lib:copy space-typing:<kind>/<id> --to typing-survival --apply` cho 7 model ở DEPLOY_INDEPENDENCE §5.1.
2. `.gitignore` của Tuyến Cuối: mở manifest model theo mẫu Lời Gọi (`!public/assets/typing-survival/**/`, `!public/assets/typing-survival/**/manifest.json`).
3. `src/view/models.ts` đọc `/assets/typing-survival/models/manifest.json`. Bỏ mục `serveSharedFolders` cho model Space trong `vite.config.ts`. Bỏ hai alias nginx (`play.conf`, `dev.conf`).
4. `kit:sync` cho Tuyến Cuối (đưa `verify-library.mjs` vào); thêm `node src/kit/tools/verify-library.mjs` vào lệnh `check`.
5. `pnpm media:push`; commit repo game và repo cha.

**Kiểm (bắt buộc):**
1. `library.lock.json` có 7 mục, md5 khớp file; mỗi mục manifest có `importedFrom`.
2. `node src/kit/tools/verify-library.mjs --strict` đạt.
3. `grep -rn "space-typing" games/typing-survival/src games/typing-survival/vite.config.ts` không còn đường dẫn runtime.
4. Bản clone riêng của game build được.
5. Kiểm trên trình duyệt: 7 model nạp từ `/assets/typing-survival/`, không yêu cầu nào tới `/assets/space-typing/`.
6. Tổng byte khớp §5.1 (11.501.400 B high, 3.969.672 B medium).

**Xong khi:** sáu kiểm đạt.

---

### AL-24 · [claude] Nối quy trình và tài liệu

**Cần trước:** AL-16, AL-22.

**Chỉ được ghi:** `docs/ASSET_LIBRARY.md` (bản thiết kế, cập nhật theo việc đã làm), `library/README.md`, `AGENTS.md`, `docs/games/3D_REQUESTS.md`, `docs/games/MEDIA_AND_MODELS.md`, `docs/games/AUDIO_PIPELINE.md`, `docs/games/DEPLOY_INDEPENDENCE.md`, skill trong `.agents/skills` nếu cần (rồi `bash scripts/sync-agent-skills.sh`); trong từng game khi làn rảnh: `kit:sync` và lệnh `check`.

**Việc:**
1. `library/README.md` tiếng Việt, một trang: tìm, xem, chép, kiểm.
2. AGENTS.md: một dòng "tìm trước khi làm" với `pnpm lib:find <từ tiếng Anh> --json`.
3. `3D_REQUESTS.md`: cột `lib:find` cho dòng mới ("không có" / "dùng lại <uid>" / "khác vì …"). Phần "Bối cảnh" của mọi phiếu ảnh, Tripo, âm mới dẫn `lib:find` hoặc `lib:check --request`.
4. Bước import Tripo (MEDIA_AND_MODELS): ghi `downloadedAs` từ `tools/tripo-match`, chạy `models:index`, rồi `pnpm lib:scan --game <g>`.
5. MEDIA_AND_MODELS §6: chép giữa game đi qua `lib:copy` (bọc `models:prepare --import`). AUDIO_PIPELINE §11: sổ chép và `sourceRow`. DEPLOY_INDEPENDENCE: ghi chú `library.lock.json` và `verify-library`.
6. Rồng và Lời Gọi, khi làn rảnh: `kit:sync` để có `verify-library.mjs`, thêm vào lệnh `check`.

**Kiểm (bắt buộc):**
1. Mọi lệnh nhắc trong tài liệu có trong `package.json`.
2. Liên kết trong các tài liệu đã sửa trỏ tới file có thật.
3. Lượt import Tripo kế tiếp: GLB mới hiện trong `lib:find` sau một lần quét, có `downloadedAs`.
4. Tài liệu bằng tiếng Việt, danh từ game tiếng Anh; commit không có media.

**Xong khi:** bốn kiểm đạt.

---

### AL-25 · [owner] Nghiệm thu và hai quyết định

**Cần trước:** quyết định 1 sau AL-12 (tờ ghép dot3). Lần thử sau AL-16. Quyết định 2 sau AL-22.

**Việc:**
1. **Dot3 của Rồng:** dùng lại `cau-tau`, `meadow/reed-clump`, `meadow/wildflowers` của Lời Gọi, hay giữ phong cách riêng và tiêu credit Tripo. Xem tờ ghép Claude gửi.
2. **Xóa bản trùng?** Đọc `lib:check --dupes`. Ứng viên: Space `art-src/models/raw` (~1,75 GB); handoff `tripo-upload*` (627 MB), chỉ sau khi `lib:check --drive` sạch; `tools/art-normalize/.tmp` (1,5 GB). Agent không xóa.
3. **Thử một phút:** mở `library/out/catalog.html`, tìm mọi chòi và nhà; rồi tìm và nghe một tiếng click gỗ.

**Kiểm (bắt buộc):**
1. Mỗi lần tìm dưới một phút.
2. Quyết định dot3 ghi vào `3D_REQUESTS.md` (Claude ghi theo lời chủ dự án).
3. Quyết định xóa ghi vào nhật ký thay đổi, kèm ngày. Nếu xóa: chủ dự án tự làm sau khi `pnpm media:check` đạt; Claude báo dung lượng trống trước và sau.

**Xong khi:** ba việc có câu trả lời.
