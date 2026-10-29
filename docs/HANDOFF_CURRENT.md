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

### Làn Claude (agent nền của coordinator-2, trừ làn cuối)

| Làn | Nơi làm | Việc | Khi xong |
|---|---|---|---|
| **R2** (map Rồng, chờ ảnh) | `games/.wt-dh-mappilot`, nhánh `map-pilot` (`ee6b6e4`, đã gộp `main` `4f61c6e`, chưa gộp ngược) | A3 xong: nắng thấp, sương, đất thông ô liu, vách hoa cương gấp đôi, impostor 16° cho màn tựa, tán bẻ sáng, dải ven làn; DH-12 (bản build đủ 12 ô đất, `b1d3e7e`). Tự chấm M 5,5–6,5. `dh-crowd` đạt; `dh-bench` +0,24 ms (đạt, đo lại khi máy rảnh); tương phản quái ở 1280 kém main một bậc (yếu 8,8 % so với 3,4 %) | **Việc kế (chưa giao, chờ chỗ trống):** hệ thống đường Dragonhold theo PATH_QUALITY, ảnh của phiếu 155. **Dừng chờ** phiếu 120 (trời) và 124 (mốc, Tripo). Gộp `map-pilot` vào `main` sau giám khảo AFTER (xem A1 tương phản). Nếu tới lúc dựng demo chưa gộp: làn T cherry-pick `b1d3e7e` (ô đất) vào `main` |
| **L2** (Wordwoven 1C, hết ngữ cảnh 29/10 08:45) | `games/.wt-td-1c` (nhánh `td-1c` `7b9de55`, chưa gộp) | Đã gộp `a2-days`; sửa C10 theo giám khảo (tự chấm 7,5; tờ `tmp/lane-l2/sheets2/`); đường map 1 bản đầu (`95f764d`: `src/view/3d/road.ts`, ảnh theo vai trò ở `road.json`, đá bờ `props/da-ke`, đã push media). Còn: khay mép, kẹp thẻ khi zoom, tờ đường theo PATH_QUALITY §5, sửa đá bờ, gắn 122/123c khi nhận (BUILD_NOTES §8.9–§8.12) | Giám khảo C10 vòng 2 đang chạy; làn mới (L3) nhận phần còn lại, đọc BUILD_NOTES §8.9–§8.12 |
| **V-ts** (VFX Last Line) | đã gộp vào `main` `e26e898` (cùng `ts-codex`), đã đẩy | TS-M1-04 đạt. TS-M1-05 **trượt giám khảo độc lập**: Pulse Gun 5,5, Heat Beam 5, tàu bị đánh 4,5, Pulse Gun trên nền sáng 4. Lóe bắn là đĩa trắng tròn quanh tàu, mất màu súng; đốm trúng trắng che bầy; khói mờ; thiếu lớp tối | Vòng 2 khi có chỗ trống (tối đa 4 làn) |
| **V-dh** (VFX Rồng, nhận từ session cũ 28/10 22:30) | `games/.wt-dh-vfx`, nhánh `dh-vfx` (25160fe, chưa gộp) | Vòng sửa ngắn cho 1a (người chấm vòng 2: 7 và 7,5; lõi trắng quá to, không ra lửa); Sky Fire từ phần sửa dở; VFX quái (gộp `main` vào trước) | Sau 1a, điều phối viên chạy một giám khảo độc lập (cần ≥ 8), rồi gửi chủ dự án tờ 1a |
| **J1** (giám khảo, xong 29/10 09:00) | `judge-r5/verdict.md`, `judge-c10/verdict.md` | 1a vòng 5 **trượt**: mạnh 6,75, thường 6,4 (A 5,5; trên đá sáng 4,5–5; nón R là hình thang cam phẳng, khối nổ một tông che quái, số sát thương sinh cao 100 px). C10 **trượt**: 6,5 (phím đúng 6,5, sai 7,5, xong từ 6, Word Shot 7,5, combo 6,5; vòng ấn che chữ, từ 13 px nhỏ hơn dòng nghĩa) | Đã gửi: V-dh dựng vật liệu lửa thật (nhiễu ăn mòn, ramp, khói tối cùng lúc) cho 1a vòng 6 và Sky Fire; L2 sửa 5 điểm C10 trước khi làm đường; R2 làm hệ thống đường Dragonhold |
| **J2** (nhận ảnh Codex, xong 29/10 08:30) | `docs/codex-queue/accept-29-10/verdict.md` | Nhận 36, làm lại 18: 113 nhận keyart, logo, emblem (logo và emblem sạch đã chép đè, bản cũ ở `_review/113/replaced-29-10/`); 114 nhận sky-beast, sky-beast-top; 115 nhận banner, portrait-ring, crest, divider; 137 nhận 8, 138 nhận 10, 139 nhận 9. Gốc lỗi: hậu kỳ phá tranh → luật `ART_ACCEPTANCE.md` §5, đã chép vào mọi phiếu ảnh còn chờ | Phiếu làm lại 158–161 đứng đầu làn M15. Gợi ý của người chấm còn mở: ổ icon kim loại và cỡ icon tối thiểu khoảng 20 px cho Dragonhold; vẽ lại bộ icon kiểu cũ của Dragonhold cho hợp bộ mới |
| **M-dh** (model Dragonhold theo mức, 29/10 08:50) | `games/.wt-dh-models`, nhánh `dh-models` (từ `main` `4f61c6e`, gộp `map-pilot`) | Chủ dự án 29/10: lỗi nhựa do ta cắt mặt và xóa map; giảm đúng chỗ (Low), Ultra phải tăng mạnh. Dựng 4 mức theo MODEL_QUALITY §2b từ file gốc Tripo, vật liệu dùng normal và roughness map, đo `dh-bench`/`dh-crowd` từng mức | `public/assets` của worktree là bản chép riêng; điều phối chép media vào checkout chính và push khi gộp |
| **J3** (giám khảo C10 vòng 2) | chỉ đọc | Chấm `sheets2/` của L2 | `judge-c10-r2/verdict.md` |
| **E** (duyệt chữ tiếng Anh, xong 29/10) | — | 130, 131, 132 đạt sau sửa, đã gộp: Last Line `main` `b904a54`, Dragonhold `main` `4f61c6e`, Wordwoven `a2-days` `1048f8a` (132 `c5c4f8c`, màn tựa bỏ hình vẽ bằng mã `c7942eb`: không cò, dây đèn, đom đóm, con dấu; thiếu tranh thì nền phẳng và `console.warn`). `NAMES_EN.md` theo luật 28/10 (`7617e17d`) | Tên file chơi thử `loi-goi-choi-thu-*.json` đổi ở lượt dọn công cụ (cùng `scripts/td/b9.ts`) |

**Đã xong 29/10:** kiểm kê hình ảnh và âm thanh UI (commit `330b4527`, `docs/games/map1/UI_IMAGERY.md`); chỉ đạo mỹ thuật (`b2b54ec5`). Làn R chạy lại dưới tên R2 lúc 05:00. Ổ đĩa còn 10 GB lúc 04:15 (74 GB lúc 05:00 sau khi V-dh dọn); `.wt-dh-vfx/tmp` 16 GB, đã bảo V-dh dọn khung thô của các vòng đã đóng.

## 4. Việc chờ, theo thứ tự

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
- **29/10 sáng, chủ dự án:** chọn Last Line hướng **B · Lightbearer** (bỏ tàu; ART_DIRECTION §4.3 đã đánh dấu chọn). Luật mới về đường đi: "phần đường đi cũng phải làm thật đẹp, chứ đường đi nhìn như kiểu lấy ngón tay quệt dài như kia nó rất xấu" → `docs/games/PATH_QUALITY.md` (áp ba game; ảnh: 122/123 tờ c cho Wordwoven, 155 cho Dragonhold, 125 cho Last Line; mã: làn map từng game).
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
