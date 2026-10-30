# Phiếu 212 · Last Line · Map 1 (c1-s1): danh sách âm Firefly với prompt tiếng Anh theo hướng B, kèm lược đồ chung cho ba game

**Nguồn:**
- `docs/HANDOFF_CURRENT.md` §3, hàng "Âm thanh: đường Firefly" (29/10 19:20). Làn FF phải soạn danh sách âm "theo mã sự kiện (prompt tiếng Anh, gợi ý diễn bằng giọng, nhịp VFX)". Làn dừng lúc 19:55. `docs/games/audio/` chưa có, không có commit nào (Claude đã kiểm).
- `AGENTS.md` (chủ dự án 28/10): âm là "real audio files made through docs/games/AUDIO_PIPELINE.md", không phải tiếng tổng hợp tạm.
- Chủ dự án 29/10: tự tạo SFX bằng Adobe Firefly Generate Sound Effects; mình soạn danh sách và nhận file về.
- `docs/games/MAP1_PRODUCTION.md`: Last Line có cổng sớm nhất (03/11). Cổng G3 ghi "Âm chưa ai nghe".
- Chủ dự án 30/10: "tăng thêm việc cho codex cho tôi".

**Không trùng:** 182, 189–193 (tiếng phím); 175 (texture VFX); 188 (giấy phép thư viện); 198 (kit phát file). Phiếu này chỉ viết danh sách, không làm âm, không gắn.

**Sau phiếu này:** Claude duyệt, commit, gửi danh sách cho chủ dự án tạo trong Firefly. Phiếu 217 (bước ingest) cắt file Firefly theo lược đồ này. Phiếu 213 (Dragonhold) chỉ chạy khi `schema.json` của phiếu này đã được Claude commit, và dùng lại lược đồ cùng hàm kiểm của `212/check.mjs`. Danh sách Wordwoven là phiếu sau, cùng lược đồ.

**Báo cáo:** `docs/codex-queue/212-report.md` (tiếng Việt), thư mục `docs/codex-queue/212/`.

## Trước khi chạy (việc của Claude)

1. Xác nhận làn FF của Claude đã dừng hẳn, không còn viết `docs/games/audio/FIREFLY_SOUND_LIST.md`. Làn còn sống thì dừng nó trước. Không để hai danh sách. (Kiểm 30/10: mọi làn dừng từ lúc chủ dự án reset máy; `docs/games/audio/` chưa có.)
2. Sửa hàng FF trong HANDOFF §3: trỏ tới `docs/games/audio/firefly/` và phiếu 212.

Codex chỉ chạy khi `grep -n "docs/games/audio/firefly" docs/HANDOFF_CURRENT.md` có kết quả. Không có thì dừng, ghi vào báo cáo.

## Nơi làm

- Repo cha, gốc repo (`.`), nhánh `feat/space-typing-admin-uiux`. Làn P10, phiếu thứ 1.
- Chỉ ghi vào:
  - `docs/games/audio/firefly/README.md`, `schema.json`, `typing-survival.md`, `typing-survival.json`;
  - `docs/codex-queue/212/` và `docs/codex-queue/212-report.md`.
- Repo cha đang bẩn vì việc khác. Không đụng, không dọn. Trước khi làm, lưu vào `212/`:
  - `git status --short -uall` và `git diff --stat` của repo cha → `status-before.txt`;
  - `git -C games/typing-survival rev-parse HEAD` và `status --short -uall` → `game-before.txt`.
- Mã game chỉ đọc, ở `games/typing-survival` (nhánh `main`). `SOUND_IDS` ở đó trùng với `.wt-ts-typefx` và `.wt-ts-codex` (Claude đã so).

## Đọc trước (chỉ đọc)

- Mã, trong `games/typing-survival/`: `src/audio/theme-audio.ts` (`SOUND_IDS`, `BUSES`, các hàm phát), `gun-audio.ts`, `type-audio.ts`, `src/content/guns.ts` (tên Anh của súng), `foes.ts`, `chapter-1.ts` (ải `c1-s1`), `stage-rules.ts` (`PACE_HOLD`), `src/view/gunfx.ts`, `src/view/combat.ts`, `src/app/main.ts`, `src/app/journey.ts`.
- Tài liệu game: `docs/audio/THEME_SOUND_LIST.md` (23/10, chủ đề trạm thép cũ, có trước hướng B).
- 46 thẻ spec có prompt tiếng Anh: `tools/audio-lab/specs/typing-survival/*.yaml` (lấy `when`, `purpose`, `duration`, `variants`).
- `docs/games/ART_DIRECTION_2026-10-28.md` §4.3 (bible hướng B) và §8.3 (cột "Tiếng bible đòi").
- `docs/games/VFX_STANDARD.md` §3.1 (5 pha). `docs/games/AUDIO_PIPELINE.md` §6.2, §6.4, §8.3. Luật Q6 trong `tools/audio-lab/DECISIONS.md`. `docs/games/NAMES_EN.md`.
- Mẫu cấu trúc: `docs/games/vfx/FIREFLY_VFX_LIST.md` (danh sách video Firefly, cùng đường làm).
- Kết quả Firefly đã biết (lô 189 của chủ dự án): WAV 48 kHz, stereo, 16-bit, khoảng 12 s mỗi file, nhiều cú trong một file. Tên file mở bằng đầu prompt ("An edited Foley sequence of isol…"). Được đọc tên file ở `~/Downloads/typing-mp3/` để biết mẫu; không sửa gì ở đó.

## Việc

1. **`README.md` và `schema.json`: lược đồ chung cho ba game.**
   - `schema.json` là JSON Schema 2020-12 cho một file danh sách game. Có `game`, `stage`, `direction`, `assumptions`, `rows`, `excluded`, `retired`, `totals`.
   - Mỗi hàng `rows` có: `id`, `playerName` (tên Anh trong game, có thể null), `when`, `bus`, `phase` (`charge`, `release`, `travel`, `impact`, `aftermath` hay null), `vfxSync` (khoảnh khắc VFX tiếng phải khớp), `priority` (`P0`, `P1`, `P2`), `priorityWhy`, `shape` (`hits`, `single`, `loop`), `prompt`, `targetMs` (`min`, `max`), `variants`, `hitsPerTake`, `takes`, `loop`, `voiceHint` (có thể null), `inbox`, `era`, `eraNote`, `specCard`, `basis`.
   - Trường tùy chọn cho phiếu 213 (Dragonhold đọc thêm nhánh `dh-vfx` chưa gộp và ghép âm với clip VFX Firefly). Last Line không cần thì bỏ trống hay để null, nhưng schema phải nhận:
     - cấp file: `sourceCommits` (object: tên nhánh → mã commit đã đọc);
     - cấp hàng: `branchOnly` (tên nhánh khi id chỉ có trên nhánh đó, hay null), `clips` (mảng `{ clip, phase, startMs, lengthMs, syncNote }`, có thể rỗng; `phase` là `A`, `R`, `T`, `I`, `F`), `clipsWhy` (chuỗi hay null: vì sao không có clip).
   - README giải thích từng trường bằng tiếng Việt và ghi luật chung:
     - chỉ model Firefly của Adobe; không model đối tác; giấy phép ghi "Adobe Firefly Generate Sound Effects, generated by the project owner (Adobe model)";
     - thư mục nhận: `~/AudioLab/inbox/firefly/<game>/<id>/`, mỗi id một thư mục, tên file để nguyên như Firefly đặt;
     - cái đã biết về Firefly (lô 189) và cái chưa biết. Chưa biết thì ghi "chưa biết", không đoán.
   - `assumptions` giữ mọi hằng số tính lượt (`fileSeconds: 12`, phần cú dùng được…), để Claude chỉnh sau lượt đầu.
2. **`typing-survival.json` và `typing-survival.md`: một hàng cho mỗi id phát được trong `c1-s1`.**
   - `c1-s1` (First Shift): giữ 150 s, không hiểm họa, Scout từ 12 s, đàn Brute từ 80 s, hai đợt dồn, người chơi chọn 2 trong 5 súng (nên cả 5 súng đều tính).
   - Mỗi id: chứng minh phát được hay không bằng `file:dòng` (nơi gọi và điều kiện ải). Ghi vào báo cáo.
   - Claude đọc sơ: ngoài `c1-s1` có `leader.*` (c1-s2), `rift.*` (c1-s3), `shield.*` (c1-s4), `foe.split` (chưa thấy Splitter ở c1-s1). Còn lại khoảng 35 hàng từ `SOUND_IDS`, cộng `hit.sub`, `hit.tail` (bước 4). Codex kiểm lại; khác thì ghi lý do.
   - `when`, `vfxSync`, `voiceHint`: tiếng Việt ngắn, tên trong game bằng tiếng Anh (Pulse Gun, Scout, Brute, Armor).
   - `phase` theo `VFX_STANDARD` §3.1. Âm không phải đòn (UI, kết trận, đợt dồn) để null.
   - `priority`: theo thứ tự §8.3 của ART_DIRECTION: đòn chữ và súng (P0) → trúng và chết (P0) → quái bắn, bị đánh, đợt dồn, kết trận (P1) → UI, sao, tiếp tế (P2). Lệch thứ tự thì ghi `priorityWhy`.
   - `targetMs`, `variants`: lấy từ thẻ spec (`duration`, `variants.target`). Thẻ trống thì lấy từ THEME_SOUND_LIST, ghi `basis`.
   - Bốn id có trong mã mà không có thẻ (`gun.tia.loop`, `gun.ray.armed`, `word.full`, `streak.up`): `specCard` null, lấy từ THEME_SOUND_LIST và hàm phát trong mã.
   - `inbox`: `~/AudioLab/inbox/firefly/typing-survival/<id>/`. Chỉ ghi đường dẫn, không tạo thư mục.
3. **Prompt tiếng Anh cho Firefly.**
   - Ý âm lấy từ cột "Tiếng bible đòi" của §8.3 trước, rồi `purpose` của thẻ spec. Đổi vật liệu cũ (thép công nghiệp, tàu, hành lang) sang hướng B: ánh sáng, plasma, kính đen nứt, súng canh bay, áo choàng giáp, sàn thép than chì và đá cổ, hố đen xa.
   - Câu khẳng định: tả cái muốn nghe. Không dùng "no", "not", "without", "never".
   - `shape: hits`: xin một chuỗi cú tách rời có khoảng lặng, như mẫu của lô 189, để 217 cắt. Ví dụ phần mở: "An edited sequence of isolated …, each one followed by a second of silence".
   - `shape: single`: một sự kiện mỗi file (âm dài như kết trận, đợt dồn).
   - `shape: loop`: một nền đều, không lên xuống, để cắt vòng (`gun.tia.loop`, `gun.ray.armed`).
   - Theo Q6: đòn đủ phần chuẩn bị, phát, thân, đuôi, trừ phần hành động không có. Cỡ âm theo cỡ nguồn.
   - Theo §6.2, §6.4: âm xong từ (`word.*`) có đầu sáng ngắn, phần ngân trầm. Đuôi nằm dưới 1 kHz hoặc trên 4 kHz; viết thành chữ, ví dụ "a short bright attack, then a low ringing body".
   - Không tên riêng, tên phe, tên hãng, tên game, phim hay người. Không chữ Việt.
   - Ví dụ hướng (Pulse Gun, `gun.xung`): "An edited sequence of isolated energy cannon shots from a floating sentinel gun: each shot a bright crystalline crack, a dense plasma punch with weight, a short glassy shimmer that settles into a low distant rumble, each one followed by a second of silence."
4. **Id loại trừ và id cũ.**
   - `excluded`: `key.ok`, `key.bad` (lý do: tiếng phím đi bộ Firefly của 189–191); `music.calm`, `music.surge` (lý do: nhạc là stem 96 BPM La thứ theo AUDIO_PIPELINE §8.3, không phải SFX); id ngoài `c1-s1`, kèm ải đầu tiên phát nó. Mỗi mục một lý do.
   - Tên mã thời tàu giữ nguyên trong `id` (`gun.xung`, `gun.tia`, `gun.tan`, `gun.ray`, `gun.phao`). Tên người chơi thấy ở `playerName`.
   - `era`: `kept` (cùng sự kiện, cùng nghĩa) hay `reworded` (cùng sự kiện, nghĩa đổi theo hướng B). Ví dụ cần xét: `hurt.hull` (thân tàu → giáp Lightbearer lóe khiên lam), `support.repair` (khoang sửa cập → vòng xanh từ trên xuống), `word.load` (băng đạn → vòng ký hiệu đóng quanh súng canh).
   - `retired`: id thời tàu không còn sự kiện ở hướng B. Đánh dấu, không xóa, không viết prompt.
   - 4 id chỉ có trong thẻ spec:
     - `hit.sub`, `hit.tail`: **có hàng** (P0). Đây là lớp sub và đuôi dùng chung của bậc trúng theo `AUDIO_PIPELINE.md` §6.3 mục 3; phiếu 198 ghi một phiếu gắn sau sẽ ghép chúng khi có file Firefly. Mã hôm nay chưa phát: ghi điều đó trong `basis`, kèm `file:dòng` của `flush()` trong `theme-audio.ts`.
     - `gun.xung.loop`, `kill.chime`: Codex xét, đưa vào `rows` hay `retired`, mỗi id một câu lý do.
5. **Số lượt cho chủ dự án.**
   - `hitsPerTake` = số cú vừa trong `fileSeconds` (mỗi cú chiếm `targetMs.max` cộng 1 s lặng), lấy phần nguyên, trần 8. `shape: single` và `shape: loop`: luôn 1.
   - `takes` = đủ để ra `variants` cú dùng được theo `assumptions`, cộng 1 lượt dự phòng cho P0. Ghi rõ công thức trong README.
   - `totals`: tổng hàng, tổng lượt, lượt theo P0, P1, P2.
   - Đầu `typing-survival.md`: một bảng tóm tắt (id, tên, ưu tiên, lượt) và tổng lượt. Sau đó mỗi id một khối theo P0 → P2: khi nào, pha, độ dài, số lượt, thư mục nhận, prompt trong khối mã để chép, gợi ý giọng.
6. **Script kiểm một lần** `docs/codex-queue/212/check.mjs` (Node, không thêm thư viện; JSON Schema kiểm bằng mã tự viết).
   - Đọc `SOUND_IDS` từ mã nguồn (gồm `TYPE_SOUND_IDS`, `GUN_SOUND_IDS`, `LOOP_SOUND_IDS`); không chép tay danh sách. Đọc id thẻ spec từ tên file.
   - Đếm: id thiếu (mỗi id trong `SOUND_IDS` có đúng một lần trong `rows`, `excluded` hoặc `retired`; mỗi id chỉ có ở thẻ spec có đúng một lần trong `rows` hoặc `retired`), id trùng, id lạ (không thuộc `SOUND_IDS` hay thẻ spec), lỗi lược đồ.
   - Export hàm kiểm lược đồ (ví dụ `validateList(list, schema)` trả danh sách lỗi) và hàm tính lượt, để phiếu 213 import mà không sửa file này. Phần chạy chỉ chạy khi file được gọi trực tiếp.
   - Quét prompt: ký tự ngoài ASCII; từ cấm Q6 ("pop", "puff", "balloon", "thud", "thump", "toy", "cartoon", "retro", "8-bit", "chiptune"); từ thời tàu ("ship", "spaceship", "hull", "industrial", "corridor", "turret"); từ phủ định.
   - Quét mọi trường chữ (trừ `id`): tên Việt của đồ trong game (Xung, Tia, Tán, Pháo, Lính, Bầy, Trâu, Khiên, Vỏ, Đầu Đàn), nguyên từ, phân biệt hoa thường. Câu tiếng Việt cần từ thường ("tia lửa", "bầy") thì viết chữ thường.
   - So `typing-survival.md` với JSON: cùng tập id, cùng prompt từng chữ.
   - Tính lại `takes` và `totals` theo công thức README, so với JSON.
   - In độ dài prompt dài nhất (ký tự), để Claude so với giới hạn của Firefly khi biết.
   - `--selftest`: cài sẵn trong bộ nhớ ba lỗi (bỏ một hàng, thêm "pop" vào một prompt, thêm một id lạ) và cho thấy bắt đủ ba.
   - Lưu kết quả: `212/check.txt` và `212/check.json`.

## Cấm

- Mọi lệnh git có ghi.
- Ghi ra ngoài repo: không tạo `~/AudioLab/…`, không tạo thư mục nhận.
- Mạng; gọi Firefly hay bất cứ model âm nào; tạo hay tổng hợp âm.
- Sửa `games/**`, `tools/audio-lab/**` (kể cả thẻ spec), `shared/**`, `docs/HANDOFF_CURRENT.md`, `docs/CODEX_QUEUE.md`, tài liệu thiết kế. Claude sửa sau nếu báo cáo đề xuất.
- Đoán giới hạn của Firefly (độ dài prompt, chỉnh độ dài, credit, giới hạn tốc độ). Ghi "chưa biết" và đưa vào câu hỏi cho chủ dự án.
- Viết danh sách Dragonhold hay Wordwoven.
- Đụng worktree khác (`.wt-ts-typefx`, `.wt-dh-*`, `.wt-td-*`), Tu Tiên.

## Kiểm (ghi số)

1. `node docs/codex-queue/212/check.mjs`: thoát 0. Ghi số: `SOUND_IDS` (đọc từ mã), số hàng, số loại trừ theo lý do, số `retired`, **thiếu 0, trùng 0, lạ 0, lỗi lược đồ 0**, prompt lỗi 0, tên Việt 0, md lệch JSON 0, tổng lượt.
2. `node docs/codex-queue/212/check.mjs --selftest`: bắt đủ 3/3 lỗi cài sẵn.
3. Game không đổi: HEAD và `git -C games/typing-survival status --short -uall` sau khi làm giống hệt `212/game-before.txt`.
4. Repo cha: `git status --short -uall` so với `212/status-before.txt` chỉ thêm file trong `docs/games/audio/firefly/`, `docs/codex-queue/212/` và báo cáo.
5. Báo cáo có:
   - bảng từng id trong `SOUND_IDS`: trong hay ngoài `c1-s1`, bằng chứng `file:dòng`;
   - 4 id chỉ có ở thẻ spec, 4 id chỉ có ở mã (`gun.tia.loop`, `gun.ray.armed`, `word.full`, `streak.up`), xử lý thế nào;
   - các hàng `reworded` và `retired`, mỗi hàng một câu lý do;
   - câu hỏi cho chủ dự án về giới hạn Firefly.

**Xong khi:** đủ bốn file danh sách, script kiểm và đầu ra của nó, báo cáo có số; năm mục kiểm đạt. Claude duyệt, commit, gửi `typing-survival.md` cho chủ dự án tạo âm trong Adobe Firefly.
