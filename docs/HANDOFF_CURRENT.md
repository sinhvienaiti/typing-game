# Bàn giao điều phối (cập nhật 29/10/2026, khoảng 08:40)

File này để **một session mới** nối tiếp mà không cần đọc lại lịch sử chat.
- Mỗi lần dừng hay chuyển session, cập nhật file này.
- Luật của chủ dự án nằm ở memory (tự nạp) và `AGENTS.md`. Ở đây chỉ nhắc ý chính.

## 0. Giai đoạn và mục tiêu (chủ dự án 28/10)

- **Tạm dừng tính năng mới.** Chỉ sửa lỗi, làm đẹp, làm mượt phần đang chơi được.
- **Mục tiêu:** map 1 của từng game đạt chuẩn production, để chủ dự án chơi thử qua `typing-game.local` trên Mac ở nhà (chưa đưa lên mạng):
  - Rồng: L2-cau;
  - Lời Gọi: w1-silverfall, làm 3D (bước 1C) cho riêng map 1;
  - Tuyến Cuối: c1-s1.
- **Kế hoạch chung:** [`docs/games/MAP1_PRODUCTION.md`](games/MAP1_PRODUCTION.md). Nó có 7 cổng cho từng game, danh sách P0, P1, P2, bốn làn T, V, R, L với lịch theo ngày, việc của chủ dự án và rủi ro. Ngày dự kiến đủ 7 cổng: Tuyến Cuối 03/11, Rồng 06/11, Lời Gọi 12/11.
- **Kết quả kiểm kê gốc:** `docs/games/map1/audit-2026-10-28.json`. Lô Codex 1: `docs/games/map1/CODEX_BATCH.md`, đã tách thành phiếu 094–105.
- **Session điều phối:** coordinator-2 (local_5e0da15c-bdaa-4ce5-b009-0c06fc42b9d7, CLI `f97baf5f`, mở 28/10 khoảng 18:15). Session cũ `157c54d6` đã xong và giao hết việc; chủ dự án có thể lưu trữ nó.

**30/10, 11:20: chủ dự án bảo Claude dừng mọi việc, chỉ giao việc cho Codex (ba làn, nhiều việc), rồi chờ giao việc.**

Việc của Claude đã dừng, và chỗ dừng của từng việc:

- **Sửa lỗi sau khi gắn 32 bộ phím:** workflow `wf_ef77bd64-ccb`. Bốn bản sửa đã commit, chưa gộp, chưa đẩy:
  - Last Line: `ts-typefx` `d15fed0`, `7a793c3`;
  - Dragonhold: `dh-keys` `568eb35`;
  - Wordwoven: `td-keys` `646e889`;
  - Monkeytype: `feature/typing-feel-32` `2bf28b79a`.

  Last Line và Dragonhold đã kiểm lại, đạt. Wordwoven và Monkeytype bị dừng giữa lúc kiểm lại. Làm tiếp: `Workflow({scriptPath: ".../workflows/scripts/keys-32-review-fixes-wf_ef77bd64-ccb.js", resumeFromRunId: "wf_ef77bd64-ccb"})`. Sau đó Claude kiểm bốn game trên trình duyệt.
- **Phân tích cách Codex xử lý âm phím, kèm bản mẫu tốt hơn** (chủ dự án yêu cầu): workflow `wf_5d707009-95f`. Mới xong nhánh "pipeline". Kết luận sơ bộ: khâu cắt và xử lý âm phần lớn ổn; 32 bộ nghe giống nhau là do cách v2 gom tiếng gõ thành bộ. Chưa phản biện. Làm tiếp bằng `resumeFromRunId: "wf_5d707009-95f"`; đầu ra ở `tmp/keys-firefly/diagnose/`.
- **Lửa Rồng vòng 11:** V-dh2 dừng giữa chừng khi đang thêm vòng sóng bám mặt đất cho Sky Fire. Có thay đổi chưa commit trong `games/.wt-dh-vfx`: `src/view/fx.ts`, `skyfire.ts`, `flipbook.ts`, `vfx-layers.ts`, `actors.ts`, `crowd.ts` và hai kịch bản chụp. Mốc commit cuối là `ca64509`.

Codex chạy ba làn (owner 30/10 11:15):
- `s7`: 194 → 195 → 197 trong `.wt-dh-codex`;
- `s8`: 214 → 215 → 216 → 217 → 206;
- `s9`: 199 → 202 → 200.

Lô phiếu mới 220+ đang soạn qua workflow `codex-batch-220` và sẽ được nối vào sau ba làn. 213 nối sau `s8`.

**Monkeytype đã đẩy (30/10, 14:25, chủ dự án bảo):**
- `feature/en-vn-translation` lên GitHub `sinhvienaiti/monkeytype` qua SSH, `85a8667a1..02d511788`, không ép. Gồm âm và hiệu ứng gõ, 32 bộ phím, các bản sửa, và commit mirror GitLab của chủ dự án đã gộp vào.
- Đã kiểm: lint, `ts-check`, 1.485/1.485 test; hai người kiểm độc lập; thử trên trình duyệt (danh sách 32 bộ theo họ, nghe thử khi rê chuột, chọn bộ, gõ có hiệu ứng).
- File âm không theo Git. Chủ dự án đã nhận zip 32 bộ (`tmp/keys-firefly/zip/keys-firefly-32-monkeytype.zip`). Máy khác: giải nén vào `~/AudioLab/review/staging/`, rồi `pnpm sync-keys`.
- **GitLab (máy Mac mini M2 ở công ty chỉ dùng GitLab):** workflow mirror trên GitHub chết từ 08/10. Đã đẩy tay `feature/en-vn-translation` lên `gitlab.com/sinhvienaiti/monkeytype`, `7d84bfb70..02d511788`, không ép, đầu nhánh khớp GitHub. Khóa dùng được là `~/htdocs/key/id_ed25519_github`; GitLab nhận khóa này là tài khoản `@toanjaco2`.
- Repo cha chưa đẩy: `build:monkeytype` có bước sync và `KEYS_FIREFLY_HANDOFF.md` chưa có trên remote; con trỏ `games/monkeytype` trong repo cha chưa cập nhật.

**Cập nhật 13:35:** Codex vẫn chạy ba làn.

- **Đã xong, chờ Claude duyệt và commit:**
  - 194, 195, 197 (Dragonhold, `.wt-dh-codex`; 197 xanh 593/593);
  - 200 (Wordwoven, `.wt-td-ui`; 405/405, gói 82,3 kB);
  - 206, 214, 215, 216, 217, 213.
- **Đã commit:** 212 (`83217b53`) và changelog của 198.
- **Ảnh 149–153:** `image_gen` của Codex vẫn trả 429 lúc 13:07, dù phần làm code đã có hạn mức. Chạy lại khi có hạn mức ảnh.
- **199:** quyết định lần hai lúc 13:28: phép kiểm màu khóa chỉ áp cho điểm có độ sáng ≥ 0,25.
- **Ba làn:**
  - `s13`: 199 → 202 → 226;
  - `s14`: 220, rồi lệnh chờ tự chạy `s14b`: 222 → 223;
  - `s15`: 221 → 227 → 224 → 225 (225 là ảnh, có thể gặp 429).
- **Lô 220–227** đã qua người kiểm, có hàng trong `CODEX_QUEUE.md`.
- **Vẫn chờ Claude chấm ảnh:** 203 (ảnh 133, 165, 172), 204 (lô UI Wordwoven), 211 (ảnh 149–153 và khung 127).

**Cập nhật cuối của session cũ (28/10, sau 22:10):** session cũ (157c54d6) đã xong cả 4 lượt và gửi kết quả sang `coordinator-2`. Từ đây mọi việc thuộc session mới:
- `codex-review-28-10`: kết quả nằm trong tin nhắn.
- `map-pilot-a`: trung vị 7,125, chưa đạt cổng A; nhánh `map-pilot`.
- `map1-production-audit`: `docs/games/MAP1_PRODUCTION.md`, `docs/games/map1/`.
- `vfx-dh-v2`:
  - bước 1a đã làm 2 vòng, người chấm cho 7/7,5, cần một vòng sửa lõi trắng;
  - Sky Fire dở, có sửa chưa commit trong `games/.wt-dh-vfx`;
  - VFX quái chưa làm.

Mục 3 bên dưới là lịch sử.

- **Luật chủ dự án 28/10 tối:** mọi chi tiết giao diện (thẻ, nút, ô, nhãn, biển, bảng tin, kết quả, cửa hàng) phải có hình thật đi kèm, không chỉ có chữ. **Tuyệt đối không dùng hình vẽ bằng mã để thay hình thật**: không SVG hay canvas vẽ cảnh, không icon bằng CSS, không emoji, không tranh dự phòng. Thiếu ảnh thì mở phiếu Codex. Âm thanh cũng phải là file thật, có chất lượng, làm theo `docs/games/AUDIO_PIPELINE.md`. Lượt rà toàn bộ giao diện và âm thanh đang chạy; kết quả sẽ ở `docs/games/map1/UI_IMAGERY.md` và `UI_IMAGERY_CODEX.md`.

- **Quyết định của chủ dự án 28/10 tối** (đã ghi vào `AGENTS.md`):
  - toàn bộ chữ trong game bằng tiếng Anh, tiếng Việt chỉ ở nghĩa của từ;
  - tên game: Dragonhold, Wordwoven, Last Line;
  - Wordwoven theo hướng sử thi: làm lại nền, trời, màn tựa, ảnh chủ đạo, khung UI; giữ 117 model và chỉnh ánh sáng;
  - cả ba game được chấm lại so với game thương mại, cái nào dưới 8 thì làm lại.
  Làn chỉ đạo mỹ thuật đang viết `docs/games/ART_DIRECTION_2026-10-28.md` và các phiếu từ 112. Phiếu 106, 110 đã rút khỏi làn ảnh M6.

- **Học từ Typing Break** (chủ dự án 29/10): `docs/games/TYPING_BREAK_STUDY.md` có 16 kỹ thuật kèm thông số, cách áp cho từng game, và top 10 việc nên làm. Dùng cho thẻ gọi của Wordwoven (C10); thẻ chữ, nút kỹ năng, thanh xây của Dragonhold; dòng gõ và ô súng của Last Line (làm sau khi chủ dự án chọn hướng ở phiếu 112).

## 1. Bắt đầu session mới

1. Đọc file này, `MAP1_PRODUCTION.md` §4, rồi `docs/CODEX_QUEUE.md` (các dòng 088 trở đi).
2. Kiểm các làn ở mục 3: `pgrep -fl codex-lane-mac` cho Codex; nhật ký Codex ở `.local/codex-runs/<phiếu>/`, báo cáo ở `docs/codex-queue/<số>-report.md`.
3. Làn Claude là agent nền của session điều phối. Session đó dừng thì làn cũng dừng: xem `git log` trong worktree của làn, rồi mở lại bằng một agent mới có ghi chú RESUME.

## 2. Luật chính (chi tiết ở memory)

- **Giao tiếp:** trả lời chủ dự án bằng tiếng Việt; tự làm theo khuyến nghị, chỉ hỏi quyết định thật sự chặn việc; cổng nào gãy thì báo kèm số.
- **Git và media:** không media trong Git; repo game đẩy qua SSH, không force; chỉ Claude chạy `pnpm media:push`; không đụng Tu Tiên.
- **Codex** (chủ dự án 28/10: "tăng gấp đôi công việc cho codex"):
  - luôn chạy **hai làn cùng lúc**, một làn ảnh và một làn mã, ghi vào các đường khác nhau;
  - giao một danh sách việc, ảnh trước;
  - Codex không chạy git có ghi; Claude duyệt rồi mới commit.
- **Làn Claude:** tối đa 4 cùng lúc. Ảnh test: giữ tờ ghép, xóa ảnh thô bằng `tools/capture-prune`.
- **Mức nhận:** ảnh 2D từ 8 điểm; model 3D từ 7 điểm; điểm 7–8,5 ghi vào `ART_REPLACE_LATER.md`.

## 3. Đang chạy (28/10, 19:40)

### Codex: hai làn (cập nhật 29/10, 03:50)

| Làn | Còn lại | Ghi chú |
|---|---|---|
| Ảnh M10, rồi M11 | 113 (đang chạy), 114 → 115, 116, 117, 118, 119, 120, 122, 123, 124, 128 | `.local/codex-lane-mac-m10.txt`, `-m11.txt` (M11 chờ M10 xong rồi tự chạy) |
| Mã M8, M9 | xong (130–132, 111b) | |
| Ảnh M15 (sau M14) | 155 đường đá Dragonhold, 125, 156 (Tripo Lightbearer và 5 súng canh), 121, 127, 126, 157 | `-m15.txt` (hướng B) |
| Ảnh M16 (sau M12) | 149, 150, 151, 153, 152: icon UI Last Line | `-m16.txt` |
| Ảnh M18 (sau M15) | 145, 147, 173, 176 | `-m18.txt` |
| Ảnh M19 (sau M17) | 174, 175, 177 | `-m19.txt` |
| **M17c** (từ 14:15, thay M17b) | 182 tiếng phím trước, rồi danh sách của M17b | `-m17c.txt`; M19 vẫn chờ tên `m17` |
| ~~M17b~~ (dừng 14:15) | 170, 119, 120 (đã sửa thiết kế vòng), 178, 179, 117, 118, 171, 162, 148, 163–167, 146 | `-m17b.txt`; M19 chờ tên `m17` nên vẫn nối sau |
| ~~M17~~ (dừng 13:40) (từ 29/10 10:45, chủ dự án: Codex còn nhiều hạn mức) | mã 168, 169, 170, 171 → ảnh 162, 148, 163, 164, 165, 166, 167, 146 | `-m17.txt`. Ba worktree Codex đã tua tới nhánh chính và có lượt đồng bộ kit chưa commit (kit 154, check-pack); Claude commit cùng phiếu 168–170 sau khi duyệt |

**Codex hết hạn mức 29/10 05:49, tự chạy lại lúc 09:45** (M11 dừng ở 116, M13 dừng ở 140).
| Ảnh M12 (sau M11) | 133–136, 141–144: icon UI Wordwoven | `-m12.txt` |
| Ảnh M13 (sau M9, chiếm chỗ làn mã khi hết phiếu mã) | 137–140: icon UI Dragonhold | `-m13.txt` |

- **Chờ quyết định, chưa xếp làn:** 121, 125, 126, 127 (Last Line, chờ chủ dự án chọn hướng từ 112); 129 (Wordwoven, chờ chủ dự án đồng ý dựng lại sáu nhà mái tranh).
- **Phiếu icon UI chờ điều kiện** (kiểm kê UI 29/10, `docs/games/map1/UI_IMAGERY.md`): 145 (chờ Claude nhận khung 115), 146 (chờ khung UI Dragonhold, chưa có phiếu AD), 147 (Claude dựng trước ảnh tham chiếu từ GLB rồng bằng `.local/bin/render-glb-views.py`), 148 (Claude thử cắt chân dung quái từ ảnh có sẵn trước), 149–153 (Last Line, chờ chọn hướng). Sáu phiếu vẽ lại có điều kiện (UIC-*-R) chưa tách số.
- **Kiểm kê UI 29/10, việc của Claude (làn gắn ảnh, chưa mở):** gắn icon súng 108 vào thẻ Nạp súng và hai bến chữ của Last Line; chân dung quái 089 vào thẻ ải; chân dung Draconis và Thư Đồng vào thanh đội Wordwoven; icon tài nguyên Wordwoven; 17 icon vẽ có sẵn thay SVG của Dragonhold. Làm sau khi duyệt và gộp 130–132, để không đụng phần đổi chữ.
- **Lỗi thật từ kiểm kê:** Dragonhold bản build không có ô đất (`src/view/paint.ts:372-375` chỉ nạp ô đất và decal từ `/art-src/` khi chạy dev; việc của làn map, MF-C24); màn tựa Wordwoven không có `onerror` nên thiếu ảnh thì lặng lẽ rơi về cảnh SVG (`src/ui/title.ts:180-185`). Bản chơi `games/.wt-play-typing-defense` thiếu `title-dusk.webp`: đã chép vào 29/10 04:10, kiểm trên trình duyệt thấy tranh. Ba bản chơi `.wt-play-*` đều cũ so với nhánh chính; làn T phải dựng lại cả ba.
- **Âm thanh:** cả ba game chưa có file âm nào (176 tiếng, 172 tổng hợp bằng mã). Claude chọn: tiếng phím dùng mẫu thật CC0, mã chỉ đổi cao độ (theo luật "âm thanh là file thật"). Chủ dự án cần chấm các lượt nghe trên Audio Lab (chưa ai chấm từ 23/10).
- **Xong, chờ Claude duyệt:** 112 (tờ `games/typing-survival/art-src/_review/112-directions.jpg`, đã gửi chủ dự án), 130, 131 (chữ tiếng Anh trên nhánh Codex của từng game).
- **Đã gộp 29/10 04:35:** `ts-codex` (104b, 130) vào `main` Last Line; `dh-codex` (080, 094, 101, 105, 105b, 131) vào `main` Dragonhold, trước `dh-vfx` (V-dh gộp `main` vào `dh-vfx` ở điểm sạch tới; `src/view/fx.ts` có nhãn PERFECT).
- **Đã gộp:** `td-codex` (091, 103) vào `a2-days`; `ts-codex` cũ vào `main` Tuyến Cuối `e26e898`.
- **Ảnh đã nhận:** 088, 089, 093, 095, 096, 097; 098–100 xong nhưng bị chấm lại theo mức chợ, thay bằng 116–118, 122, 123.

### Tiếng phím: 80 bộ trở lên (30/10, khoảng 08:40)

- **Nghe thử và làn Codex thứ hai (30/10, khoảng 10:50):**
  - Đã gửi chủ dự án 32 file nghe, mỗi bộ 9 giây, cùng nhịp và cùng độ to. File ở `tmp/keys-firefly/listen-sets/`, dựng bằng `bash tools/audio-lab/run.sh tools/audio-lab/keys/firefly_listen_sets.py`.
  - Chủ dự án bảo tăng thêm một làn Codex, nên giờ chạy **hai làn** song song:
    - `s4`: 212 → 214, 215, 216, 217, 206;
    - `s6`: 199, 202 trong `.wt-td-scenery` → 200 trong `.wt-td-ui`; khi `s6` xong, `s7` tự chạy 194 → 195 → 197 trong `.wt-dh-codex` (194 lượt 10:43 dừng vì phần dở của 195, bị cắt lúc đổi làn 08:43; đã ghi chú vào ba phiếu).
  - Hai worktree Wordwoven mới cắt từ `td-1c` `2a1f61d`, có liên kết media như `.wt-td-1c`.
  - Đã bỏ lệnh chờ `s5`, vì 194 nay nằm trong `s7`.
- **Nghe xong 32 bộ (30/10, khoảng 11:20):**
  - Chủ dự án thấy "âm nào cũng hơi giống nhau". 7 bộ bản 1 nghe khác hẳn nhau (ông gọi là clack, cream, poppy, thock, click).
  - Claude mở một vòng chẩn đoán, chủ dự án bảo dừng: "không cần chẩn đoán nữa, tạm thời cứ dùng 32 file âm đó". Đã dừng; chưa có kết luận lỗi do Codex hay do nguồn.
  - Nếu sau này cần bộ khác nhau rõ hơn: xem `KEYS_FIREFLY_HANDOFF.md` §5. Cách dễ thử nhất là chỉ giữ các bộ khác nhau nhất, hoặc dựng lại với vùng lấy mẫu mỗi bộ hẹp hơn.
- **Đã gắn 32 bộ** (chưa gộp, chưa đẩy):
  - Last Line: `ts-typefx` `e1c7d15`, `8956257`, `804429a`;
  - Dragonhold: `dh-keys` `2a8933f` (Codex 192), `7c84b64`, `255b452`;
  - Wordwoven: `td-keys` `0a63df2` (Codex 193), `023b995`;
  - Monkeytype: `feature/typing-feel-32` `8dead1a6d`, `44945ad4a`.
  - Workflow `keys-32-review-fixes` đang sửa các lỗi người kiểm tìm ra:
    - Dragonhold: đổi bộ không giải phóng bộ cũ;
    - Wordwoven: mất tiếng gõ sai, thiếu test bảng;
    - Monkeytype: danh sách vẽ lại toàn bộ.
  - Còn chờ:
    - Claude kiểm trình duyệt;
    - `media:push` sau khi gộp;
    - quyết định có làm manifest gọn cho game không (mỗi game hiện thêm khoảng 5 MB JSON vào Git, mỗi bộ khoảng 170 KB tải khi chọn).
- **Kết quả và quyết định (30/10, khoảng 10:45):** phiếu 218 chỉ ra 32 bộ (458 trên 490 bộ đạt điểm bị loại vì gần trùng). Chủ dự án nghe 10 bộ bị loại và chốt: **tạm giữ 32 bộ**, sau cần thì làm thêm. Cách làm thêm ghi ở `docs/games/audio/KEYS_FIREFLY_HANDOFF.md` §5 (hạ `MIN_DISTANCE`, sửa điểm độ lặp, ồn nền, hoặc tạo âm Firefly mới). Tài liệu đó cũng là README cho folder âm trên Drive.

- Chủ dự án thấy chỉ có 7 bộ ("tôi tải hơn 400 file âm cơ mà"), rồi chốt: **80 bộ trở lên, mỗi bộ 70–100 biến thể, khoảng 6 điểm là được**. Giữ 7 id cũ (mặc định Bright Clack) cho bộ tốt nhất mỗi họ.
- Phiếu Codex 218 (dựng bộ), 219 (kit: danh sách theo họ, nhiều biến thể). Làn `s4` thay `s3` sau khi 194 xong: 218, 219 chạy trước, rồi phần còn lại của `s3`. Vẫn một làn.
- Sau 218–219: Claude chép bản giao `tmp/keys-firefly/staging-v2/` sang `~/AudioLab/review/staging/keys-firefly/`, đồng bộ kit vào `ts-typefx`, `dh-keys`, `td-keys`, chép kit vào Monkeytype (`frontend/src/ts/custom/typing-feel/kit/`), chạy `pnpm sync-keys`, thử trình duyệt.
- Đã tạo 4 clip khói Firefly (chủ dự án đồng ý), cắt thành `~/VFXLab/out/dragon-hold/smoke-mask/`, giao V-dh2 cho vòng 10.

### Lửa Rồng vòng 10 đã chấm (30/10, khoảng 10:30): chưa đạt, đi ngang

- V-dh2 commit `5587bd7`, `c2a6f9b`, `8b028ce`, `d91586f`, `ca64509` trên `dh-vfx` (mặt nạ khói Firefly, sửa nêm 1/6 của mặt nạ vết nứt, Sky Fire vẽ đè quái, lóe đòn thường bằng flipbook…). Giám khảo A: mạnh 8,0, thường 7,7, Sky Fire 8,1; giám khảo B: 7,8, 7,4, 7,8. Vòng 8 khoảng 7,75, vòng 9 khoảng 7,8, vòng 10 khoảng 7,8: **đi ngang quanh 8**.
- Lỗi lặp lại cả ba vòng: lửa tắt bằng alpha trên cỏ ra vàng mù tạt, ô liu (cộng màu cam mờ lên xanh lá); khói còn phẳng; Sky Fire chưa có vòng sóng hay vòm, nổ không to hơn đòn chữ; vết cháy và lưới nứt quá đều. Clip PLAIN của vòng 10 chụp nhầm đòn mạnh (PERFECT 128).
- Phiếu: `games/.wt-dh-vfx/tmp/vfx/judge-r10a/verdict.md`, `judge-r10b/verdict.md`. Đang hỏi chủ dự án: làm vòng 11 có kiểm màu tại chỗ trước khi chấm, hay dừng ở khoảng 8 và gộp.

### Lửa Rồng vòng 9 đã chấm (30/10, khoảng 08:10): chưa đạt 8,5

- Giám khảo A: mạnh 7,9, thường 7,4, Sky Fire 7,9; giám khảo B: 8,0, 7,5, 8,0. Tiến trình: vòng 7 khoảng 7,4, vòng 8 khoảng 7,75, vòng 9 khoảng 7,8. Đã ngang game thương mại: T của đòn mạnh 8,5, R của Sky Fire 8,5, T của Sky Fire 9,0.
- Kéo xuống: khói pha F 6,0–6,5 ở cả ba đòn (mảng ô liu phẳng trên cỏ, dải mép thẳng trên sông), lửa tắt thành mảng đỏ cắt cứng, Sky Fire trúng còn đĩa hồng đào và chưa có vòng hay vòm theo bán kính luật, ngôi sao sticker ở đòn mạnh, quái lóe kem 4–5 khung ở đòn thường, vết cháy như cái lỗ, đòn Perfect chưa có vệt chữ. Tờ Sky 1280x720 play-dark bị lớp tạm dừng che, phải chụp lại.
- **Vòng 10** đã gửi V-dh2 (`judge-r9a/b/verdict.md`). Khói đổi sang mặt nạ mật độ, tô màu trong shader (than ấm, sáng trên, ửng lửa dưới). Clip Firefly khói trắng trên nền đen làm mặt nạ: hỏi chủ dự án trước khi tạo (đã dùng hết khoảng 25 clip được duyệt).

### Sau khi khởi động lại (30/10, khoảng 00:25)

- Làn Codex `s1` chạy lại; 00:36 chủ dự án báo Codex đã có hạn mức, khởi động lại `s1` để chạy ngay (192 bắt đầu 00:36). Vẫn **một làn**. Chủ dự án: "Codex bao giờ xong thì kêu nó làm tiếp" — hết `s1` thì duyệt và nối phiếu 194–217.
- V-dh2 được gửi tin chụp tiếp vòng 9.
- **Monkeytype typing feel: xong (30/10, khoảng 09:05).** Nhánh `feature/typing-feel` trong `games/monkeytype` (6 commit) **đã gộp fast-forward vào `feature/en-vn-translation`** (30/10, chủ dự án bảo "gộp luôn"; HEAD `8a335aba6`, chưa push, checkout đang ở `feature/en-vn-translation`). Hai vòng kiểm độc lập: vòng 2 đạt. 1.457 test, oxlint và tsc sạch. Claude thử trình duyệt: nhóm "typing feel" ở tab custom, rê chuột tải đúng preview, chọn Bright Clack tải đủ 15 file và lưu, gõ chữ vẽ hiệu ứng trên hai canvas. `pnpm build:monkeytype` ở repo cha nay chạy `sync-keys` trước (commit `43a44fbf`). Khi có 80 bộ (218, 219): chép kit mới vào `frontend/src/ts/custom/typing-feel/kit/` và chạy `pnpm sync-keys` từ staging mới.
- **Việc mới của chủ dự án:** đưa tiếng phím Firefly và hiệu ứng gõ chữ vào **Monkeytype** (`games/monkeytype`, repo riêng, nhánh `feature/en-vn-translation`), cài đặt nằm trong tab "custom" của cửa sổ Custom Text (mã của chủ dự án ở `frontend/src/ts/custom/en-vn-translation/`). Workflow `monkeytype-typing-feel` đang chạy: ba người đọc, thiết kế, làm trên nhánh mới `feature/typing-feel`, hai người kiểm. Thử trình duyệt do điều phối làm sau. File âm không vào Git (script chép từ `~/AudioLab/review/staging/keys-firefly`).

### Dừng hết để chủ dự án khởi động lại máy (30/10, 00:18)

Chủ dự án: "dừng lại mọi thứ để tôi reset máy". Không còn tiến trình nào chạy (đã kiểm `queue.sh`, `codex exec`, vite, trình duyệt chụp).
- **Codex:** làn `s1` đã dừng. Phiếu 192 chưa chạy được vì Codex hết hạn mức tới **04:17 sáng 30/10**. Chạy lại: `tools/codex-run/queue.sh .local/codex-lane-mac-s1.txt` (một làn; còn 192, 193, 142–145, 148, 186, 149–153, 183–185, 176, 177).
- **Lửa Rồng vòng 9 (V-dh2):** dừng giữa lúc chụp. Trên `dh-vfx` đã commit `31e2191` (chín sửa chung của giám khảo vòng 8) và `196d490`; worktree sạch. Lượt chụp vòng 9 chưa xong: đòn mạnh đã chụp, thường và Sky Fire chưa. Mở lại: một agent mới đọc `docs/changelog` vòng 8, hai phiếu `judge-r8a/b/verdict.md` và hai commit trên, chụp lại đủ bộ vào `tmp/vfx/final9/`, rồi gửi hai giám khảo mới.
- **Phiếu Codex mới 194–217 (24 phiếu):** workflow `codex-next-tickets` đã viết xong bản nháp nhưng bị dừng trong bước kiểm. Các file chưa commit, chưa xếp làn. Mở lại: kiểm từng phiếu (đường dẫn, trùng, luật Codex), thêm hàng vào `docs/CODEX_QUEUE.md`, nối vào cuối làn `s1`.
- **Tiếng phím:** 189, 190, 191 xong (191 commit `de7176e` trên `ts-typefx`, mặc định Bright Clack). Chờ `media:push`; Drive cần chủ dự án chạy `pnpm media:setup --reconnect`.

### Codex vừa phải (30/10, 00:00; chủ dự án: "khi Codex có quota lại, hãy giao việc vừa phải thôi, không cần làm song song nhiều agent nữa")

- **00:02, một làn (chủ dự án: "tạm thời cho Codex về 1 làn thôi cũng được, khi nào tôi yêu cầu thì sửa sau"):** dừng ba làn `m1`–`m3` khi đang chờ giới hạn (không phiếu chạy dở), gom vào **một làn `s1`**: 192, 193, 142, 143, 144, 145, 148, 186, 149, 150, 151, 153, 152, 183, 184, 185, 176, 177. Phiếu mới (194 trở đi) nối vào cuối `s1`. Chỉ mở thêm làn khi chủ dự án bảo.
- Mười làn song song chạm giới hạn chỉ vài phút sau khi mở (23:35). Đã dừng cả mười khi đang chờ, gom phần còn lại vào **ba làn**: `m1` 192, 193, 176, 177; `m2` 142, 143, 144, 145, 148, 186; `m3` 149, 150, 151, 153, 152, 183, 184, 185. Cả ba chạy tiếp khi hết giới hạn (khoảng 00:05).
- Đã xong từ 23:15: 175, 188, 191 (Last Line: 7 bộ phím, mặc định Deep, 238 test xanh; chờ Claude kiểm trình duyệt và `media:push`).
- Phiếu mới của workflow `codex-next-tickets` (194 trở đi) nối vào cuối ba làn này, không mở làn mới.

### Codex chạy song song (29/10, 23:25; chủ dự án: "tăng việc song song", "cho nó làm song song")

- Dừng P1, P2, P3, P5 lúc đang chờ hết giới hạn (không phiếu nào chạy dở) và dừng vòng lặp P6b (phiếu 191 vẫn chạy tới hết). Chia việc còn lại thành 10 làn chạy cùng lúc, cách nhau 10 giây: `p1a` 142, 143; `p1b` 144, 145; `p2a` 148, 176; `p3a` 175, 149, 150; `p3b` 151, 153; `p3c` 152, 177; `p5a` 188, 183, 184; `p5b` 185, 186; `p6c` 192 (`.wt-dh-keys`); `p6d` 193 (`.wt-td-keys`). Danh sách ở `.local/codex-lane-mac-<làn>.txt`.
- Gặp giới hạn thì `queue.sh` tự chờ rồi chạy lại phiếu đó. Hạn mức Codex là trần thật, nhiều làn chỉ làm hàng đợi cạn nhanh hơn khi còn hạn mức.
- Workflow `codex-next-tickets` đang soạn 18–24 phiếu mới (194 trở đi) cho làn P7–P10; xong thì duyệt, thêm hàng vào `docs/CODEX_QUEUE.md`, chạy song song.

### Lửa Rồng nhắm 9 (29/10 tối)

- **Vòng 8 xong (29/10, khoảng 23:20):** V-dh2 commit trên `dh-vfx` (`bea3528` gộp main, `47efd27`, `210e94c`, `cc9d15c`, `e16fbf2` changelog), chưa gộp, chưa push. Đủ chín flipbook theo bản chọn; §5.6 đạt trừ thân sáng lóe / đầu đạn đòn mạnh 1,11–1,44 (dưới 1,5); `dh-perf` High trận 3,84–4,56 / 5,4–6,3 ms. Còn mở: bộ nhớ texture VFX khoảng 101 MB High (trần đề xuất 32 MB), số Sky Fire chồng thẻ chữ đang gập 3–5 khung (sửa ở `src/ui/tags.ts`). Media flipbook chờ `media:push` (Drive cần chủ dự án kết nối lại). Tờ và clip: `games/.wt-dh-vfx/tmp/vfx/final8/`. **Chấm vòng 8 (29/10, khoảng 23:45): chưa đạt 8,5.** Giám khảo A: mạnh 7,8, thường 7,4, Sky Fire 7,3; giám khảo B: 8,4, 8,0, 7,6 (vòng 7: 7,55/7,7, 7,35/7,1, 7,4/7,4). Hai người cùng chỉ: lửa additive vẫn phai qua vàng mù tạt, ô liu trên cỏ; khói Sky Fire là khối xanh đen đặc đứng yên hơn 1 s; đèn tung đòn rửa bệ sáng thành hồng cá hồi; số sát thương che lõi nổ hoặc nằm dưới thẻ chữ; nổ Sky Fire nhỏ hơn thiên thạch. Phiếu: `games/.wt-dh-vfx/tmp/vfx/judge-r8a/verdict.md`, `judge-r8b/verdict.md`. **Vòng 9:** đã gửi V-dh2 chín sửa chung của hai giám khảo cùng phần còn nợ; xong thì gửi hai giám khảo mới.

- **Chủ dự án:** "cố gắng lên 9, 8,5 vẫn chấp nhận được" (ghi ở `VFX_STANDARD.md` §5.6). Duyệt khoảng 25 clip Firefly.
- **Firefly Video không trừ credit:** tài khoản ghi "Standard features: Unlimited access"; số dư đứng 8.900/10.010 sau khi bấm tạo. Credit chỉ dùng cho model đối tác (không dùng).
- **Clip:** điều phối tạo trong tab Firefly của chủ dự án theo `docs/games/vfx/FIREFLY_VFX_LIST.md` (22 lệnh lúc khoảng 21:00, một lệnh báo "Something went wrong"); tải về `~/VFXLab/inbox/firefly/dragon-hold/<id>/`.
- **Làn FXV** (agent nền, mở lại): dựng `tools/vfx-flipbook/` (`run.sh ingest`, `run.sh all`), không commit, báo danh sách file để điều phối duyệt.
- **Làn V-dh2** (agent nền): `games/.wt-dh-vfx` nhánh `dh-vfx`; gộp `main`, làm 15 sửa của hai giám khảo vòng 7, lớp flipbook, rồi chụp vòng 8. Không tự chấm thay giám khảo: điều phối gửi hai giám khảo độc lập (mức 9, sàn 8,5).

### Làn Claude (agent nền của coordinator-2, trừ làn cuối)

| Làn | Nơi làm | Việc | Khi xong |
|---|---|---|---|
| **R2** (map Rồng, chờ ảnh) | `games/.wt-dh-mappilot`, nhánh `map-pilot` (`51fb5b2`, chưa gộp) | Đường vòng 2: mọi lối mòn thành dải đường, cụm 1–3 món mỗi 2–4,5 m (56 món), hết khung giật (vẽ một khung lúc nạp), `dh-bench` +0,30 ms; tự chấm đường M 6,0, "vệt quệt" còn ít. Model ven đường: cliff-rock-a/b, grass-tuft, lantern-post, rail-fence | **Dừng chờ** 155 (đá lát), 120 (trời), 124 (mốc) và M-dh; khi có thì chạy lại `dh-foe-contrast` 1920 và `dh-crowd`, rồi giám khảo đường và cổng C |
| **L2** (Wordwoven 1C, hết ngữ cảnh 29/10 08:45) | `games/.wt-td-1c` (nhánh `td-1c` `7b9de55`, chưa gộp) | Đã gộp `a2-days`; sửa C10 theo giám khảo (tự chấm 7,5; tờ `tmp/lane-l2/sheets2/`); đường map 1 bản đầu (`95f764d`: `src/view/3d/road.ts`, ảnh theo vai trò ở `road.json`, đá bờ `props/da-ke`, đã push media). Còn: khay mép, kẹp thẻ khi zoom, tờ đường theo PATH_QUALITY §5, sửa đá bờ, gắn 122/123c khi nhận (BUILD_NOTES §8.9–§8.12) | Giám khảo C10 vòng 2 đang chạy; làn mới (L3) nhận phần còn lại, đọc BUILD_NOTES §8.9–§8.12 |
| **V-ts** (VFX Last Line) | đã gộp vào `main` `e26e898` (cùng `ts-codex`), đã đẩy | TS-M1-04 đạt. TS-M1-05 **trượt giám khảo độc lập**: Pulse Gun 5,5, Heat Beam 5, tàu bị đánh 4,5, Pulse Gun trên nền sáng 4. Lóe bắn là đĩa trắng tròn quanh tàu, mất màu súng; đốm trúng trắng che bầy; khói mờ; thiếu lớp tối | Vòng 2 khi có chỗ trống (tối đa 4 làn) |
| **V-dh** (VFX Rồng, dừng 29/10 19:30) | `games/.wt-dh-vfx`, `dh-vfx` `2ed786a` (sạch, chưa gộp) | Vòng 7 hai giám khảo: mạnh 7,55/7,7, thường 7,35/7,1, Sky Fire 7,4/7,4, dáng 7,5/7,5. Bloom chỉ ở Ultra (`?bloom=1` tới khi có Cài đặt), thước đo vùng màu lửa `fireRegion`, số Sky Fire cạnh thẻ. Bước 3: VFX quái 5 pha và mã SFX từng quái đã commit; chưa chụp đợt 7 đông, chưa đo riêng, chưa chấm. Bàn giao: mục 8 cuối `docs/changelog/2026-10-29-vfx-round7.md`; công cụ ở `tmp/vfx/lane-tools/` | **Làn mới V-dh2 (chưa mở):** vòng 8 dùng texture lửa (Codex 173, làn M20) và có thể flipbook từ video Firefly (Adobe Firefly Video Model, nền đen); sửa của hai giám khảo `judge-r7a/`, `judge-r7b/` |
| **J5** (xong) | `judge-r6/verdict.md` | 1a vòng 6 **trượt**: mạnh 7,3, thường 7,0; Sky Fire 7,4 (ô 720 nền sáng 6,5–6,75). Đạt: số sát thương, vùng tối quanh quái | V-dh dừng bước 3, làm vòng 7 cho cả hai; vòng sau hai giám khảo |
| **Âm thanh: đường Firefly** (từ 29/10 19:20) | `docs/games/audio/firefly/` (phiếu Codex 212 lập danh sách Last Line, 213 Dragonhold), `tools/audio-lab/firefly/` (phiếu 217) | Chủ dự án tự tạo âm trong Adobe Firefly (Generate Sound Effects; Adobe cho dùng thương mại với model của Adobe; không dùng model đối tác; không bán lại gói). Làn FF soạn danh sách âm theo mã sự kiện (prompt tiếng Anh, gợi ý diễn bằng giọng, nhịp VFX) và dựng bước `run.sh firefly ingest` / `listen` | Chủ dự án thả WAV vào `~/AudioLab/inbox/firefly/<game>/<mã>/`; điều phối chạy ingest, gửi bản nghe 20 s, gắn vào game sau khi chủ dự án duyệt |
| **FXV** (video Firefly thành flipbook, 29/10 19:45) | `docs/games/vfx/FIREFLY_VFX_LIST.md`, `tools/vfx-flipbook/` | Chủ dự án tạo video hiệu ứng bằng Firefly Video Model của Adobe (nền đen hoặc xanh; an toàn thương mại theo Adobe). Kling và model đối tác chỉ để tham khảo animation, không đưa vào game. Làn FXV soạn danh sách hiệu ứng (prompt, blend, lưới atlas) và dựng `run.sh ingest`: cắt đoạn, tách nền, căn tâm, nối vòng, atlas PNG, JSON, tờ xem | Chủ dự án thả MP4 vào `~/VFXLab/inbox/firefly/<game>/<id>/`; V-dh2 dùng flipbook cho vòng 8 |
| **J1** (giám khảo, xong 29/10 09:00) | `judge-r5/verdict.md`, `judge-c10/verdict.md` | 1a vòng 5 **trượt**: mạnh 6,75, thường 6,4 (A 5,5; trên đá sáng 4,5–5; nón R là hình thang cam phẳng, khối nổ một tông che quái, số sát thương sinh cao 100 px). C10 **trượt**: 6,5 (phím đúng 6,5, sai 7,5, xong từ 6, Word Shot 7,5, combo 6,5; vòng ấn che chữ, từ 13 px nhỏ hơn dòng nghĩa) | Đã gửi: V-dh dựng vật liệu lửa thật (nhiễu ăn mòn, ramp, khói tối cùng lúc) cho 1a vòng 6 và Sky Fire; L2 sửa 5 điểm C10 trước khi làm đường; R2 làm hệ thống đường Dragonhold |
| **J2** (nhận ảnh Codex, xong 29/10 08:30) | `docs/codex-queue/accept-29-10/verdict.md` | Nhận 36, làm lại 18: 113 nhận keyart, logo, emblem (logo và emblem sạch đã chép đè, bản cũ ở `_review/113/replaced-29-10/`); 114 nhận sky-beast, sky-beast-top; 115 nhận banner, portrait-ring, crest, divider; 137 nhận 8, 138 nhận 10, 139 nhận 9. Gốc lỗi: hậu kỳ phá tranh → luật `ART_ACCEPTANCE.md` §5, đã chép vào mọi phiếu ảnh còn chờ | Phiếu làm lại 158–161 đứng đầu làn M15. Gợi ý của người chấm còn mở: ổ icon kim loại và cỡ icon tối thiểu khoảng 20 px cho Dragonhold; vẽ lại bộ icon kiểu cũ của Dragonhold cho hợp bộ mới |
| **M-dh** (model Dragonhold theo mức) | `games/.wt-dh-models` (`dh-models` `d84a433`; kit cha `da4bd842` bậc `ultra`) | Bốn mức dựng từ file gốc, normal và map nhám; LOD xa làm camera chơi vẫn dùng lưới Medium (High 6,25–7,26 ms); Ultra sửa hộp đen (NaN MSAA). Tải: High 10,6 MB, Ultra 15,8 MB. Quyết định 29/10: High vẽ lưới đầy đủ ở camera chơi, cổng High mới ≤ 10 ms TB, ≤ 14 ms p95; thử nén KTX2; tải texture dần ở `view/stage.ts` | Gộp vào `main` Dragonhold sau khi đo lại; chép `m0b/`, `kit3/` (128 file) sang checkout chính rồi `media:push` (Drive cần `pnpm media:setup --reconnect`) |
| **J4** (xong) | `tmp/lane-l3/judge-c10-r3/verdict.md` | C10 vòng 3 **trượt** 7,5 (phím đúng 8, sai 7,5, xong từ 7,5, Word Shot 7,5, combo 7,5, khay 7); lõi trắng R 0,46–0,6 bán kính | Vòng sau cần hai giám khảo (dải 7,5–8,5) |
| **L4** (Wordwoven C10, **đạt 8,0** 29/10 19:00) | `games/.wt-td-1c` (`td-1c` `2a1f61d`) | Hai giám khảo C và D cùng 8,0 (khay 7,5 và 7,0): C10 qua mức VFX 8. Quyết định: khung đầu đo theo từng nhịp (nhịp hai ở nhà nhận là sự kiện riêng). Việc sửa còn lại cho vòng sau: giữ màu đã gõ trên mọi thẻ khớp; mũi chỉ khay dùng chữ V ở mọi mép (vòng hở ở mép trái đọc thành chữ "C"); ×N và chữ đóng dấu không ra khỏi màn, không đè HUD (kiểm `overHud` mọi khung); nét viền cứng 1–2 khung khi gõ xong; chữ đóng dấu hiện ngay khung phím. Dải chữ giữa màn dùng chung (TF2) sẽ gắn sau | Làn Wordwoven kế: gắn ảnh đã nhận (116 cây, 158 nền tựa, khung 115), sửa các điểm trên, đường dùng ảnh 122/123 khi nhận |
| **J3** (giám khảo C10 vòng 2, xong) | `tmp/lane-l2/judge-c10-r2/verdict.md` | **Trượt** 7,0 (phím đúng 7, sai 7,5, xong từ 6,5, Word Shot 7,5, combo 7): vòng tối vẫn đè từ; thẻ mới hiện cùng khung nổ; đích đáp lại +125–208 ms; số combo nghỉ 13 px; lõi R nửa bán kính | Đã giao L3 |
| **L3** (Wordwoven, xong 29/10 10:30) | `games/.wt-td-1c` (`td-1c` `bc05e67`, chưa gộp) | C10 vòng 3 (`012774b`: vòng ấn dưới mép thẻ, nổ tại thẻ rồi bóp, nhà lóe 65–89 ms, combo 34 px, khay mép, kẹp thẻ mọi zoom; tự chấm 7,7). Đường (`bc05e67`: đá bờ hết viền đen do GTAO, vai tối hơn; lõi − cỏ 0,159/0,155; tự chấm M 5,5, còn "vệt quệt" ở camera mặc định). Còn: lõi R có thể > 30 %; chưa chụp cặp bậc 2; nét trắng mảnh lượn trên cỏ (chưa rõ nguồn); khay mép cần icon nhà và mũi tên bằng ảnh thật; emoji ở thẻ chờ phiếu 133 | Giám khảo J4 chấm C10 vòng 3; đường chờ ảnh 122, 123c |
| **TF2** (phản hồi gõ chữ, thay TF từ 29/10 14:30) | repo cha `shared/game-kit/feedback/typing-fx/`, `ui/quick-settings/`; `games/.wt-ts-typefx` (`ts-typefx`, `4d84efa` chỉ có đồng bộ kit) | TF đã làm: cỡ dải (Large mặc định), móc texture, mặt nạ chữ ẩn, Stamp nâng cấp (tự chấm phím 8,5, xong từ 8,5–9, sai 8; commit `33836dc2`, `9fb51362`, `f6f154ee`). TF2: khảo sát thư viện, Stamp rồi 5 kiểu lên 9, kit quick-settings, gắn Last Line (giữ tiếng phím cũ tới khi Audio Lab được duyệt) | Hai giám khảo trên Lab khi TF2 báo |
| **AN** (thiết kế animation, xong 29/10 14:45) | `docs/games/CHARACTER_ANIMATION.md` (`1accc46d`) | Chưa nhân vật nào lên 7: chuyển tiếp clip 3,5–4 (quái Dragonhold bật tư thế nghỉ, Hỏa Long nằm rạp 70° một khung), chuẩn bị 4–6, khối lượng quái 4,5–5; Wordwoven chưa có nhân vật 3D; Last Line chưa có Lightbearer. Thiết kế: kit `shared/game-kit/anim/` (chuyển tiếp quán tính, sự kiện clip, clip cộng, đám đông skin GPU), Anim Lab `tools/anim-lab/`, thư viện: AnimationMixer, SkeletonUtils, CCDIK (MIT), `@pixiv/three-vrm-springbone` (MIT), clip CC0 Mesh2Motion và Quaternius UAL1, UAL2 | **Bước kế (chưa giao, chờ chỗ trống):** làn ANIM1 dựng lõi kit `anim/` và Anim Lab, sửa hai lỗi bật tư thế của Dragonhold. Đã báo V-dh thử cờ additive cho Attack/Hit/Cast của Hỏa Long sau vòng 7. Codex 181 vẽ tờ tư thế khóa. Chờ chủ dự án: tải Mesh2Motion (rồng, cáo, ngựa, nhện, kaiju; 4,3 MB), Quaternius UAL1, UAL2 Standard (CC0) |
| **E** (duyệt chữ tiếng Anh, xong 29/10) | — | 130, 131, 132 đạt sau sửa, đã gộp: Last Line `main` `b904a54`, Dragonhold `main` `4f61c6e`, Wordwoven `a2-days` `1048f8a` (132 `c5c4f8c`, màn tựa bỏ hình vẽ bằng mã `c7942eb`: không cò, dây đèn, đom đóm, con dấu; thiếu tranh thì nền phẳng và `console.warn`). `NAMES_EN.md` theo luật 28/10 (`7617e17d`) | Tên file chơi thử `loi-goi-choi-thu-*.json` đổi ở lượt dọn công cụ (cùng `scripts/td/b9.ts`) |

**Đã xong 29/10:** kiểm kê hình ảnh và âm thanh UI (commit `330b4527`, `docs/games/map1/UI_IMAGERY.md`); chỉ đạo mỹ thuật (`b2b54ec5`). Làn R chạy lại dưới tên R2 lúc 05:00. Ổ đĩa còn 10 GB lúc 04:15 (74 GB lúc 05:00 sau khi V-dh dọn); `.wt-dh-vfx/tmp` 16 GB, đã bảo V-dh dọn khung thô của các vòng đã đóng.

**29/10 19:50, phiên mở lại:** mọi làn Codex cũ (M11–M20) đã dừng khi phiên khép. Chủ dự án bảo giao nhiều việc cho Codex: dựng lại bốn làn song song từ mọi phiếu chưa xong (`.local/codex-lane-mac-p1…p4.txt`):
- P1: 173, 124, 128, 117, 118, 174, 134, 135, 136, 141, 142, 143, 144, 145;
- P2: 179, 155, 162, 181, 163, 164, 146, 147, 148, 176;
- P3: 125, 156, 121, 127, 126, 157, 175, 149, 150, 151, 153, 152, 177;
- P4: 133, 172, 180, 171, 165, 166, 167;
- P5 (sau P4, chủ dự án bảo giao thêm): 187, 188, 183, 184, 185, 186.
Đã xong chờ chấm nhận: 119, 120, 122 (tự báo chưa đạt), 123, 140 (lượt b), 158, 159, 160, 161, 178; mã 170 chờ duyệt; 182 âm thanh (đường Firefly thay thế).

**29/10 19:55, chủ dự án bảo dừng hết việc khoảng 10 phút** (sẽ đăng nhập Firefly trong khung trình duyệt của app để Claude tự xem). Đã dừng bốn làn Claude giữa chừng, gửi tin để chạy tiếp từ chỗ dừng: TF2 (hiệu ứng gõ, đang làm cú nổ riêng từng kiểu), M-dh (model, đang thêm nén KTX2), FF (danh sách âm Firefly và bước ingest), FXV (danh sách video Firefly và công cụ flipbook). Ba làn Codex vẫn chạy.

**29/10 18:10:** Claude và Codex cùng hết hạn mức khoảng 14:50–18:10. Đã gửi lại bốn làn Claude (TF2, V-dh, L4, M-dh); ba làn Codex tự chạy lại 18:09 ở 122, 160, 120. Phiếu đã xong chờ chấm nhận: 119 (màn tựa Dragonhold), 170 (Wordwoven pack-and-kit, chưa duyệt), 182 (âm thanh, tạm dừng).

**Claude có lại hạn mức 29/10 13:10; Codex hết hạn mức 10:45, tự chạy lại 14:47 (ba làn chờ ở 122, 160, 170).** Đã gửi lại bốn làn Claude (AU-keys, V-dh, M-dh, L4); giám khảo nhận ảnh lô 2 (116–120, 140, 158, 159) đang chạy, kết quả ở `docs/codex-queue/accept-29-10b/`.

**Khi Claude có lại hạn mức (chủ dự án 29/10 11:40: hạn mức Claude sắp hết, giao Codex một lượt dài):** Codex chạy ba làn liền (khoảng 50 phiếu). Việc đầu tiên khi quay lại:
1. Đọc nhật ký làn `.local/codex-runs/` và báo cáo `docs/codex-queue/<số>-report.md` của mọi phiếu xong.
2. Chấm nhận ảnh theo lô (một agent giám khảo như `accept-29-10`), làm lại theo luật hậu kỳ §5; ảnh đạt thì báo làn game gắn.
3. Duyệt phiếu mã 168–171 trong ba worktree Codex (có lượt đồng bộ kit chưa commit), commit, gộp, đẩy.
4. Gửi chủ dự án danh sách dựng Tripo (124, 128, 156) kèm luật số mặt `MODEL_QUALITY.md`.
5. Kiểm các làn Claude còn chạy: V-dh (vòng 7), M-dh (model theo mức), TF (module gõ chữ, Lab), L4 (C10 vòng 4), AU-keys (tiếng phím); làn nào chết thì gửi tin cho nó chạy tiếp.

**Ảnh đã nhận, chờ gắn (29/10, `docs/codex-queue/accept-29-10b/verdict.md` mục "Sẵn sàng gắn"):** Wordwoven 116 (cây v3/v4), 158 `title-backdrop.v2` (cắt 16:9 `1536x864+0+80`, logo `logo.alpha.png` khoảng 45 % rộng); Dragonhold 140 (chín icon kết quả); cùng lượt a: 113 keyart, logo, emblem; 114 sky-beast; 115 banner, portrait-ring, crest, divider; 137 (8), 138 (10), 139 (9). Chưa có làn gắn ảnh UI: mở khi các làn game rảnh.

## 4. Việc chờ, theo thứ tự

0a. **Đẩy âm gõ phím lên Drive khi Codex xong hết (chủ dự án 30/10, khoảng 09:35).** Chủ dự án: "sau khi Codex làm xong toàn bộ, đẩy toàn bộ file âm gốc thành một folder riêng lên Drive, và file âm đã cắt thành folder riêng; folder âm cắt có cả file handoff để tải về máy khác biết đặt ở đâu, cần làm gì để chạy được sau khi pull code".
   - **Chờ:** phiếu 218 (80 bộ trở lên), 219 (kit theo họ) xong, Claude duyệt và gắn vào ba game và Monkeytype.
   - **Drive:** rclone `tgmedia:` (gốc là thư mục `typing-game-media`). Token hết hạn (`invalid_grant`, kiểm 30/10 09:38): chủ dự án chạy `rclone config reconnect tgmedia:` hoặc `pnpm media:setup --reconnect` trước khi đẩy.
   - **Folder 1, âm gốc:** `~/Downloads/typing-mp3/` (408 WAV, khoảng 889 MB) → `tgmedia:audio-sources/typing-firefly-original/`, giữ nguyên 9 thư mục. Đẩy bằng `rclone copy`, kiểm md5 (`rclone check`).
   - **Folder 2, âm đã cắt:** bản giao cuối (`~/AudioLab/review/staging/keys-firefly/` sau 218) → `tgmedia:audio-sources/typing-keys-cut/`, kèm `README.md` lấy từ `docs/games/audio/KEYS_FIREFLY_HANDOFF.md`. README ghi:
     - đặt folder ở đâu: `~/AudioLab/review/staging/keys-firefly/`; âm gốc ở `~/Downloads/typing-mp3/` (đường mặc định của `tools/audio-lab/keys/firefly.py`);
     - lệnh sau khi pull code: Monkeytype `pnpm --dir games/monkeytype/frontend sync-keys`; ba game: chép vào `public/assets/<game>/audio/keys/` hay `pnpm media:pull`; Lab `LAB_KEYS=...`;
     - cách dựng lại từ âm gốc: `bash tools/audio-lab/run.sh keys firefly survey` rồi `build` (hay `build-v2`).
   - Báo chủ dự án hai đường dẫn Drive và dung lượng.
0. **Ưu tiên sớm (chủ dự án 29/10, 20:50): tiếng phím từ Firefly của chủ dự án.** Chủ dự án đã tạo 408 file WAV bằng Adobe Firefly Generate Sound Effects ở `~/Downloads/typing-mp3/` (9 thư mục `Adobe_2026-10-29*`, 8 thư mục 50 file và 1 thư mục 8 file; mỗi file 12 giây, 48 kHz, stereo 16-bit; tên file mở bằng "An edited Foley sequence of isol…").
   - Việc: khảo sát cả 408 file, chọn bản hay cho năm hồ sơ `creamy`, `thock`, `marbly`, `clack`, `dome`, cắt `key-01` … `key-10`, `space-01` … `space-03`, làm sạch, cân độ to, ghi `keys-manifest.json` đúng định dạng `shared/game-kit/feedback/typing-fx/audio.ts`, file nghe 20 giây mỗi hồ sơ và một file so sánh.
   - Mức nhận: từ 9 (`SHARED_SYSTEMS_BAR.md`: bộ phê bình Audio Lab đạt mọi cổng, rồi chủ dự án nghe). Thay bộ Stable Audio và bộ Codex 182 đã bị trả.
   - Không đưa vào game trước khi chủ dự án nghe và đồng ý. File âm không vào Git.
   - **Chủ dự án 29/10, khoảng 22:00:** "tôi đánh giá âm typing hiện tại được rồi, không cần tạo thêm". Không tạo lô Firefly mới (ba giám khảo của workflow đoán bộ này chỉ 7–8,5 theo số đo và đã viết sẵn prompt bổ sung; tai chủ dự án là cổng cuối nên dựng từ 408 file này). Sau khi dựng xong, gửi file nghe để chủ dự án chốt từng hồ sơ.
   - **Chủ dự án 29/10, khoảng 21:55, đổi hướng:** "triển khai luôn, không cần dựng theo list (Creamy, Thock, Marbly, Clack, Dome), cứ tạo luôn, thêm tính năng khi hover vào thì phát ra âm 1 s"; "nếu Codex làm được và tốt thì kêu Codex làm luôn". Đã dừng workflow `keys-from-firefly` ở bước dựng (khảo sát và ba phiếu chọn nguồn vẫn còn ở `tmp/keys-firefly/` và trong journal của workflow). Giao Codex:
     - làn P6 (chạy 21:59): 189 (mỗi thư mục một bộ, tên tiếng Anh, `preview.ogg` 1 s, staging `~/AudioLab/review/staging/keys-firefly/`), rồi 190 (kit: danh sách chọn từ danh mục, rê chuột hay focus nghe thử 1 s);
     - làn P6b (`.local/codex-lane-mac-p6b.txt`, **Claude mở tay**): 191 Last Line (`.wt-ts-typefx`), 192 Dragonhold (`.wt-dh-keys` từ `main`), 193 Wordwoven (`.wt-td-keys` từ `a2-days`).
     - Trước P6b, Claude phải: duyệt và commit 189, 190 (giữ nguyên sửa chưa commit của TF2 trong `typing-fx/css.ts`, `draw.ts`, `quick-settings/css.ts`); thêm `ui`, `feedback`, `audio` vào `kit.config.json` của Wordwoven; tạo hai worktree; đồng bộ kit vào ba worktree; báo TF2 rằng 191 làm trong `.wt-ts-typefx`.
     - **Đã làm (29/10, khoảng 22:50):**
       - 189 và 190 đã duyệt, commit `9f7cac0f` và `7b677b5a`. Thử Lab ở 1280 × 720: danh sách Off cùng 7 bộ; rê chuột chỉ tải `preview.ogg` của bộ đó; chọn thì tải đủ file và giữ lựa chọn; không lỗi console.
       - 7 bộ: Deep, Warm, Rounded, Solid, Crisp, Clear, Bright Clack. Mức chung −34,5 LUFS-M max (thấp hơn −27, vì cú có crest lớn). Đã chép sang `~/AudioLab/review/staging/keys-firefly/`; sandbox Codex không ghi ra ngoài repo.
       - Kit đồng bộ từ bản HEAD sạch (worktree tạm, không kéo sửa dở của TF2): `ts-typefx` `0bc81b5`, `dh-keys` `d7717ac` (thêm a11y-dialog 8.1.5), `td-keys` `81baf46` (thêm module, a11y-dialog, test theo nhãn tiếng Anh của kit). `pnpm check` xanh cả ba.
       - **P6b sẵn sàng, chưa mở:** chờ chủ dự án nghe `tmp/keys-firefly/listen/so-sanh-cac-bo.mp3` và chọn bộ mặc định (đã hứa không gắn vào game trước khi có câu trả lời). Có câu trả lời thì ghi bộ mặc định vào cuối `docs/codex-queue/189-report.md` (phiếu 191 đọc ở đó), rồi chạy `tools/codex-run/queue.sh .local/codex-lane-mac-p6b.txt`.
   - **Đã dừng (29/10, khoảng 20:55):** workflow `keys-from-firefly` (khảo sát → ba giám khảo chọn nguồn → dựng → hai người kiểm bác bỏ → sửa, tối đa ba vòng). Mã ở `tools/audio-lab/keys/firefly.py`, đầu ra ở `tmp/keys-firefly/` (hồ sơ, `listen/<id>-20s.mp3`, `so-sanh-5-ban-phim.mp3`, `metrics.json`, `spectra.png`). Khi xong: duyệt mã, commit, gửi file nghe cho chủ dự án.
1. **Duyệt đầu ra Codex** khi từng phiếu xong. Phiếu mã thì chạy lại kiểm và đọc diff; phiếu đụng giao diện thì kiểm trên trình duyệt ở 1280 và 1920. Sau đó gộp:
   - `ts-codex` vào `main` Tuyến Cuối;
   - `td-codex` vào `a2-days`;
   - `dh-codex` vào `main` Rồng, theo thứ tự gộp map pilot → VFX → `dh-codex`.
2. **Làn T** (chưa mở; bắt đầu khi 090–094 đã gộp):
   - TS-M1-01: model riêng của Tuyến Cuối;
   - DH-02: báo lỗi khi bộ chữ rỗng; bỏ alias nginx;
   - `pnpm build:local`, rồi báo chủ dự án chạy sudo nginx;
   - kiểm cả ba game qua `typing-game.local`.
   Xem `MAP1_PRODUCTION.md` §4.3.
3. **Media:** sau khi nhận ảnh Codex hay model mới, chạy `pnpm media:push --yes`, commit `media.md5` của game, bump con trỏ.
4. **Repo cha:** nhánh `feat/space-typing-admin-uiux` chưa đẩy. Nhánh `map-factory` (Codex 071–075) chưa gộp vì đang tạm dừng.

## 5. Chủ dự án

- **7 câu hỏi** (`MAP1_PRODUCTION.md` §4.4): chủ dự án **đồng ý cả 7 đề xuất** ngày 28/10, khoảng 19:45:
  - Rồng tự tua ×1,75 khi không có chữ (DH-05 bước 0; sửa 06 §10);
  - Chữ Bẫy đo trên nhánh riêng, sau DH-08;
  - D27, D31, D33 chưa đổi núm nào;
  - tên ải 1 của Rồng "Ải 1 · Cầu và Suối" (phiếu 101);
  - C0 của Lời Gọi được duyệt;
  - Lời Gọi chấp nhận khoảng chờ ban ngày, đo lại sau 1C;
  - Tuyến Cuối: ải 2 tên "ẢI 2 · SĂN PACK LEADER", biển viết hoa cả câu (phiếu 104).
- **Trần media Medium của Lời Gọi** (chủ dự án 28/10, khoảng 23:20): tổng ≤ 9 MB, bộ khởi động ≤ 3,5 MB, tải dần theo ngày, byte tới Đêm 1 ≤ 6 MB.
- **Trần media High của Lời Gọi** (chủ dự án 28/10, khoảng 23:55): tổng ≤ 16 MB; High là bậc người chơi tự chọn trong Cài đặt, lần chơi đầu vẫn Medium.
- **Hỏi chủ dự án ngày 29/10, khoảng 03:50 (chưa trả lời):**
  - chọn hướng Last Line A Iron Warden, B Lightbearer hay C Rampart (tờ 112; người chỉ đạo mỹ thuật và Claude khuyên B);
  - dựng Tripo bằng tay: Dragonhold 6 mốc (phiếu 124, ~180 credit), Wordwoven 5 mốc (phiếu 128, ~150), Last Line nhân vật và 5 súng (~180, sau khi chọn hướng);
  - đồng ý hay không việc dựng lại sáu nhà mái tranh của Wordwoven (phiếu 129, ~180 credit);
  - nhận 109 (bốn ảnh ải Last Line) làm bản tạm cho tới khi 126 xong.
- **29/10 chiều, chủ dự án (3):** ba hệ dùng chung ưu tiên dùng thư viện và kho tài sản miễn phí có sẵn nếu an toàn giấy phép khi đưa site công khai (`SHARED_SYSTEMS_BAR.md` §5, sổ `docs/games/THIRD_PARTY.md`). Đã báo TF, AU-keys, AN; tải gói tài sản vẫn hỏi chủ dự án từng gói.
- **29/10 chiều, chủ dự án (2):** mỗi game có nút bánh răng và nút loa ngay trong trận, mở bảng cài đặt chung và bảng âm thanh, không phải ra màn cài đặt: `docs/games/IN_GAME_SETTINGS.md`, dòng trong AGENTS.md; kit `shared/game-kit/ui/quick-settings/` giao TF (gắn Last Line trước); icon ở phiếu Codex 180 (đầu làn M18).
- **29/10 chiều, chủ dự án:** tiếng phím Audio Lab, hiệu ứng gõ chữ và animation nhân vật là hệ dùng chung, phải đạt **từ 9** (hai giám khảo độc lập, không hạng mục con dưới 8,5; chủ dự án duyệt cuối): `docs/games/SHARED_SYSTEMS_BAR.md`, dòng trong AGENTS.md. Đã báo TF và AU-keys; làn **AN** (thiết kế animation) đang rà và viết `docs/games/CHARACTER_ANIMATION.md`.
- **29/10 sáng, chủ dự án:** chọn Last Line hướng **B · Lightbearer** (bỏ tàu; ART_DIRECTION §4.3 đã đánh dấu chọn). Luật mới về đường đi: "phần đường đi cũng phải làm thật đẹp, chứ đường đi nhìn như kiểu lấy ngón tay quệt dài như kia nó rất xấu" → `docs/games/PATH_QUALITY.md` (áp ba game; ảnh: 122/123 tờ c cho Wordwoven, 155 cho Dragonhold, 125 cho Last Line; mã: làn map từng game).
- Symlink lạc `shared/shared` → `shared` đã xóa 29/10 theo lời chủ dự án.
- **Sudo nginx một lần**, khi `pnpm build:local` xong.
- **Tripo đợt 4** (Campfire Ring, Woodpile, 60 credit): chủ dự án đang dựng. GLB thả vào `typing-game-handoff-2026-10-25/tripo-upload-dot4/_GLB tải về/`.
- **Tripo đợt 3** (8 model): đã xong, nằm trong `tripo-upload-dot3/_GLB tải về/`. Làn R đang nhập.
- **librsvg** cho 62 ảnh nhỏ SVG của thư viện: chờ chủ dự án cho cài. Không gấp, vì thư viện đang tạm dừng.

## 6. Tài liệu chính

- `docs/games/MAP1_PRODUCTION.md`, `docs/games/map1/`;
- `docs/games/VFX_STANDARD.md`, `docs/games/DEPLOY_INDEPENDENCE.md`;
- `docs/tools/map-factory/MAP_PLAN.md`, `tools/map-factory/docs/judge.md`;
- `docs/games/ART_ACCEPTANCE.md`, `ART_REPLACE_LATER.md`, `NAMES_EN.md`, `BALANCE.md`;
- `docs/CODEX_QUEUE.md`.
