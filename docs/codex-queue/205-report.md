# Phiếu 205 · Last Line · Model riêng và nạp theo bậc

Đã hoàn tất phần mã và kiểm trên ổ đĩa của TS-M1-01, TS-M1-14. **236/236 test xanh, kit 61/61, 0 `foreign-asset`, ván vàng và 152 hash chương giữ nguyên.** `deploy:pack` vẫn trả mã 1 vì duy nhất `local-host` thuộc phiếu 207. High vẫn vượt ngân sách; giữ nguyên model theo chỉ đạo.

## 1. Nơi làm, phạm vi và thay đổi

- Repo cha: `/Users/toandx/htdocs/typing-game`; mã trong `games/.wt-ts-codex`, nhánh `ts-codex`, HEAD `184c90d`, sạch trước khi làm. HEAD không đổi.
- `.gitignore`: thêm đúng ba ngoại lệ ngay sau `public/assets/**`. Manifest được mở lại, 24 GLB vẫn bị bỏ qua.
- `public/assets/typing-survival/models/`: 12 id × 2 bậc, 24 GLB chép nguyên; manifest cố định `generatedAt: 2026-10-30T00:00:00.000Z`. Không nhập `rainbow-mine-lod`, `rainbow-scout-lod`, `draconis-v2`, `draconis`; bỏ chúng khỏi bảng thử của game.
- `src/view/models.ts`: xuất URL manifest riêng và `modelTier()`, bảng yêu cầu thuần `crowdModelRequests()`/`shipModelRequest()`. Low/Medium → Medium; High/Ultra → High. Giữ API và hằng của kit nguyên vẹn.
- `src/view/crowd.ts`, `src/view/ship.ts`, `src/app/main.ts`: chọn cách **truyền bậc qua `load()`** (`crowd.load(tier)`, `ship.load(stage.scene, tier)`), dùng bậc trong yêu cầu để tải mesh/chọn URL. Không đổi constructor, phi công hoặc socket.
- `src/view/bolts.ts`, `src/view/combat.ts`, `src/app/main.ts`: `world.header.kit.guns` đi qua Combat vào Bolts. Bảng `boltModelRequests()` chọn Pulse Gun → vanguard-bolt (Draconis → dragon-fireball), Scatter Gun → solar-lance-bolt, Rail Gun → frost-seraph-bolt, Star Mortar → crimson-talon-bolt; Heat Beam không có đạn. Chỉ model súng được chọn mới được hỏi; Low hỏi 0 model đạn, `ready` vẫn true khi rỗng, `add()` thiếu model vẫn false.
- `vite.config.ts`: bỏ hoàn toàn plugin chỉ có `routes: {}`, các import và biến model Space; Vite phục vụ `public/` của game.
- `tests/own-models.test.ts`: 30 test mới, viết trước mã. Không sửa test cũ. README thêm mục Models và bỏ câu model Space chặn gói đã lỗi thời; changelog mới `docs/changelog/2026-10-30-own-models.md`.

Không sửa kit, sim, nội dung chương, media config, script nhập, nginx, cây chính hoặc game/worktree khác. Không dùng Git ghi, mạng, server, trình duyệt, `kit:sync`, `media:push`/`media:pull`. Không tạo ảnh/âm thanh nên không có prompt ảnh/âm.

## 2. Lệnh nhập và an toàn file

Chạy **đúng một lần**, từ repo cha:

```bash
pnpm models:prepare --root games/.wt-ts-codex \
  --out games/.wt-ts-codex/public/assets/typing-survival/models \
  --url-base /assets/typing-survival/models/ \
  --import games/space-typing/public/assets/space-typing/models/manifest.json \
  --only ships/vanguard,heroes/draconis-v3,enemies/rainbow-mine-3d,enemies/rainbow-scout-3d,enemies/rainbow-tank-3d,enemies/rainbow-shield-3d,enemies/rainbow-splitter-3d,skills/vanguard-bolt,skills/solar-lance-bolt,skills/frost-seraph-bolt,skills/crimson-talon-bolt,skills/dragon-fireball \
  --tiers high,medium --generated-at 2026-10-30T00:00:00.000Z
```

Mã thoát 0; **không có dòng WARN** ([log](205/import.txt)). Script ghi tạm cạnh đích rồi rename; đã đối chiếu đường ra của lệnh và cách `writeAtomic` làm việc, mọi đích đều trong worktree. Sau lệnh có **0 file `*.tmp-*`** trong bộ model. Không phát hiện file do lượt nhập tạo ngoài worktree và `docs/codex-queue/205*`; không sửa script. [Danh sách media](205/media-list.json) ghi đủ 24 GLB và manifest, đường/byte/SHA-256.

## 3. Test trước mã và chín mục kiểm

| Kiểm | Kết quả và bằng chứng |
| --- | --- |
| 1 · `pnpm check` | Trước: mã 0, **206 test/22 file**, kit **61/61** ([log](205/check-before.txt)). Test mới trước mã: **26 đỏ, 4 xanh** ([log](205/test-red.txt)); sau mã: **30/30 xanh** ([log](205/test-green.txt)). Sau: mã 0, **236 test/23 file**, kit **61/61**, TypeScript/Vite xanh ([log](205/check-after.txt)). Không test thời gian đỏ, không cần chạy riêng ba lần. |
| 2 · Ván vàng/chương | SHA-256 golden **42e4e5a9534bc78a0c252353ea7ee4670a1bec9e43eb42ef38c886aade530eea** trước/sau giống hệt ([trước](205/golden-before.txt), [sau](205/golden-after.txt)). `node --import tsx scripts/chapter-hashes.ts` chạy ở worktree, chuyển đầu ra tới đường tuyệt đối của [chapter-before.txt](205/chapter-before.txt) và [chapter-after.txt](205/chapter-after.txt): mỗi file **152 dòng**; `diff` mã 0, [đầu ra rỗng](205/chapter-diff.txt). |
| 3 · Manifest/GLB/Git ignore | **12 mục × 2 bậc**. 24/24 file khớp byte, SHA-256 nguồn; 24/24 `?v=` bằng 10 ký tự đầu SHA-256. High **12.318.692 B**, Medium **4.423.884 B**, manifest **8.408 B** ([chi tiết](205/manifest-check.json)). `git check-ignore -v` cho manifest gặp luật `!`, 24 GLB gặp luật bỏ qua `public/assets/**`; còn luật `*.glb` toàn cục ([log](205/check-ignore.txt)). |
| 4 · Build/đường Space | `pnpm build` mã 0 ([log](205/build.txt)); quét **mọi file trong dist** bằng Python với byte chuỗi `/assets/space-typing/`: **0 file** ([lệnh/kết quả](205/dist-space-scan.json)). Hằng kit không dùng đã được Vite loại khỏi bundle, không cần sửa kit. |
| 5 · Gói deploy | `pnpm deploy:pack` build xanh, sau đó mã **1** do `local-host` ([log](205/deploy-pack.txt)). `node src/kit/tools/deploy/check-pack.mjs dist --game typing-survival --json` mã 1: **0 `foreign-asset`, 1 `local-host`**, không lỗi khác; `dist` **76 file, 18.273.794 B** ([JSON](205/check-pack.json)). |
| 6 · Lần chơi đầu | [first-play.mjs](205/first-play.mjs) chỉ đọc manifest và nhập chính các hàm yêu cầu id/bậc trong mã; bộ súng lấy từ `stageHeader()` với mặc định `TRIAL_KIT.guns` cho c1-s1 (Pulse Gun + Heat Beam). Không gõ tay byte hoặc danh sách model. Cộng manifest, khử URL trùng của bảy loại quái. [Kết quả](205/first-play.json), bảng ở mục 4. |
| 7 · Đối chiếu phiếu 168 | Đối chiếu đủ **46 vị trí** và thêm **52 dòng tham chiếu chữ** của phiếu 168; giải thích từng dòng trong [space-reference-audit.json](205/space-reference-audit.json), tóm tắt ở mục 5. |
| 8 · Media bàn giao | [media-list.json](205/media-list.json): **25 file**, từng đường/byte/SHA-256; lệnh nhập cây chính ở mục 6. GLB không đi theo nhánh Git. |
| 9 · Phạm vi/Git | [worktree-status.txt](205/worktree-status.txt) chỉ có file được phép, có `manifest.json`, **không GLB**; `git diff --check` xanh. [parent-status-before.txt](205/parent-status-before.txt) so với [parent-status-after.txt](205/parent-status-after.txt): phần do phiếu này ghi chỉ trong `205*`; có thêm diff đồng thời của tác nhân khác tại `tools/vfx-flipbook/dragon-hold.json`, không được sửa hoặc hoàn nguyên. Vì vậy so sánh toàn repo cha không còn chỉ `205*`; chi tiết có trong [verification.json](205/verification.json). Snapshot trước đã tự thấy `205/` vì cần tạo thư mục/file chứa chính đầu ra; không che thay đổi có sẵn. |

Sáu nhóm test của phiếu được xử lý: manifest; 48 tổ hợp URL 12 id × 4 chất lượng; mock `loadMesh` theo súng/phi công/bậc; bảng yêu cầu tàu/quái thuần; quét source trừ kit, Vite và index; kiểm dist riêng sau build. Không dựng Crowd trong Node vì constructor gọi bộ texture canvas; tách bảng yêu cầu sang `models.ts`, dùng trực tiếp trong loader và test. Fixture cố ý của `tests/deploy-pack.test.ts` giữ nguyên. Không đưa build vào Vitest.

Thông tin của bộ kiểm không chặn gói: `kit.invalid` là gốc giả phân giải URL trong kit, không phải fetch ra ngoài; `vocabularyNotShipped: 97` là các level index chung mà game không dùng. Vite cảnh báo chunk trên 500 kB; không mở rộng sang tối ưu bundle.

## 4. Lần chơi đầu và ngân sách

Đặt cạnh số cũ **9,06 MB** của TS-M1-14; các số mới là phép tính bộ model trên ổ, **chưa phải đo mạng trình duyệt hoặc toàn bộ tài nguyên trang** (chưa cộng JS, từ vựng, font…). Script cộng cả năm model quái duy nhất vì mã hiện tại tải tất cả chúng khi dựng đàn quái, kể cả loại chưa xuất hiện ở c1-s1.

| Phi công | Chất lượng | Byte GLB + manifest | MB (10⁶ B) | MiB (2²⁰ B) | So với 4 MB |
| --- | --- | ---: | ---: | ---: | --- |
| Vanguard | High | 6.641.356 | 6,641 | 6,334 | Vượt |
| Vanguard | Medium | 2.282.576 | 2,283 | 2,177 | Trong ngân sách phần model |
| Draconis | High | 8.177.928 | 8,178 | 7,799 | Vượt |
| Draconis | Medium | 2.958.284 | 2,958 | 2,821 | Trong ngân sách phần model |

JSON ghi cả ngưỡng 4.000.000 B và 4 MiB (4.194.304 B); phân loại bốn trường hợp giống nhau ở cả hai ngưỡng. Không giảm mặt, nén lại, đổi texture hay bỏ bậc High. Bộ nguồn hiện tại khác số đo lịch sử trong tài liệu (đặc biệt scout/tank); hash đối chiếu là với **24 GLB hiện tại** được chủ dự án cho đọc, không dùng số cũ làm chuẩn.

## 5. Chỗ trỏ sang Space còn/hết

Trong 46 vị trí của phiếu 168:

- **34 vị trí** ở models/crowd/ship/bolts chuyển qua bộ riêng; một số dòng chung còn nguyên chữ nhưng không còn trỏ tới thư viện Space.
- **5 vị trí** ở main/combat giữ lựa chọn phi công và dùng loader riêng, đã nối tier/bộ súng.
- **2 vị trí** Vite đã bỏ hoàn toàn.
- **3 vị trí** ở shots giữ cờ Draconis để chọn màu/hiệu ứng; không tải file, không đổi trong phiếu.
- **2 vị trí** hằng/export `SPACE_MODEL_MANIFEST_URL` trong kit giữ nguyên theo lệnh cấm sửa kit; game không còn import/dùng, bundle không còn đường Space.

Trong 52 dòng nhắc chữ Space của lượt quét cũ, còn **46 dòng**: chú thích xuất xứ (kit và motion/scenario), hằng/export kit, danh sách game hợp lệ của bộ kiểm và fixture kiểm ranh giới. Sáu dòng liên quan đường/import Space ở game/Vite đã hết. Chúng không tạo request sang Space. Bảng JSON giữ đường/dòng cũ, ghi dòng nguyên văn còn hay hết và lý do; không diễn giải mọi dòng còn chữ Space thành lỗi runtime.

## 6. Bàn giao cho Claude

Sau khi duyệt và gộp `ts-codex`, chạy từ repo cha để nhập GLB vào **cây chính** (lệnh này chưa chạy):

```bash
pnpm models:prepare --root games/typing-survival \
  --import games/space-typing/public/assets/space-typing/models/manifest.json \
  --only ships/vanguard,heroes/draconis-v3,enemies/rainbow-mine-3d,enemies/rainbow-scout-3d,enemies/rainbow-tank-3d,enemies/rainbow-shield-3d,enemies/rainbow-splitter-3d,skills/vanguard-bolt,skills/solar-lance-bolt,skills/frost-seraph-bolt,skills/crimson-talon-bolt,skills/dragon-fireball \
  --tiers high,medium --generated-at 2026-10-30T00:00:00.000Z
```

Không cần `--out`/`--url-base` ở cây chính; với nguồn giữ nguyên, manifest và 24 hash phải khớp danh sách bàn giao (đổi tiền tố worktree sang `games/typing-survival`). Claude chạy `media:push`, xử lý alias nginx sau khi gộp (phiếu 216 giữ tới đó), rồi kiểm trình duyệt 1280 và 1920. Chưa kết luận G7 triển khai/HTTP đạt vì phiếu cấm server, mạng và trình duyệt.

## 7. Cần Claude quyết

1. **Low của tàu/quái:** đã nạp Medium, giữ 3D theo luật chủ dự án 28/10. `DEPLOY_INDEPENDENCE.md` §5 dòng 2 còn ghi “Low bỏ 3D”; tài liệu đó không được sửa trong phiếu.
2. **Đạn ở Low:** giữ quy tắc cũ, không GLB, chỉ vệt sáng; cần Claude duyệt cách áp dụng luật art cho trường hợp này.
3. **High vượt ngân sách:** 6,334 MiB Vanguard và 7,799 MiB Draconis chỉ riêng phần model + manifest đã vượt 4 MB. Cần quyết hướng xử lý; phiếu này không thu nhỏ model.

## 8. Rủi ro và phần chưa làm

- Vanguard chỉ là bản chép tạm; hướng B thay bằng Lightbearer, model Tripo chưa dựng. Không sửa lựa chọn phi công hay socket; không đụng ảnh nguồn phiếu 156.
- Lỗi `local-host` là việc phiếu 207, giữ nguyên; `deploy:pack` production còn đỏ vì lỗi thật đó.
- GLB bị Git bỏ qua nên bước nhập vào cây chính và đẩy media là bắt buộc sau khi gộp.
- Rủi ro script ghi tạm ra ngoài worktree đã kiểm ở mục 2; không thấy file tạm sót và không sửa script.
- Kiểm 9 của toàn repo cha có delta đồng thời `tools/vfx-flipbook/dragon-hold.json` ngoài phiếu; delta này xuất hiện sau lượt nhập/build, không phải file do lệnh nhập hay phiếu 205 ghi. Giữ nguyên để tác nhân sở hữu xử lý.
- Không commit/gộp, không deploy, không kiểm trình duyệt hoặc phát sinh art/audio. Các bước này theo phân công sau phiếu, không phải bỏ sót kiểm đã cho phép.
