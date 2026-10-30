# Phiếu 221 · Wordwoven · Map 1 (`w1-silverfall`): danh sách âm Adobe Firefly theo lược đồ chung của 212, kèm script kiểm

**Nguồn:**
- `docs/games/audio/firefly/README.md` dòng 3: "Dragonhold (213) và Wordwoven (phiếu sau) dùng lại `schema.json` và các hàm export của `docs/codex-queue/212/check.mjs`." Chưa có phiếu Wordwoven nào: quét `docs/codex-queue/` và `docs/CODEX_QUEUE.md` không thấy `typing-defense.json` hay danh sách Firefly của Wordwoven.
- `docs/games/MAP1_PRODUCTION.md` §2.1, cổng G3 của Lời Gọi (dòng 84): "Âm chỉ là tiếng tổng hợp." §2.2 mục 23 (dòng 116): "**A13** · P1 · G3. Chưa có file âm thật."
- Đầu file `src/view/sound-map.ts` của nhánh `td-1c`: "Ids marked new have no code-made sound (the owner's rule of 28/10: no synthesized stand-ins): they stay silent until their file." Hôm nay 26 trên 65 id đang câm.
- Chủ dự án 29/10: chủ dự án tự tạo SFX trong Adobe Firefly; mình lập danh sách và nhận file về (README Firefly, mục "Luật nguồn và nhận file"). Last Line đã có 212 (Claude commit `83217b53`), Dragonhold có 213 trong hàng, Wordwoven chưa có gì.
- `docs/HANDOFF_CURRENT.md:18`: 30/10 11:20, chủ dự án bảo Claude dừng việc của mình, giao nhiều việc cho Codex.

**Không trùng:**
- 212: danh sách và lược đồ của Last Line;
- 213: danh sách Dragonhold;
- 217: bước ingest;
- 189–193: các bộ tiếng phím;
- A13: lượt Stable Audio, nay thay bằng đường Firefly của chủ dự án.

Phiếu này chỉ viết danh sách: không tạo âm, không gắn vào game.

**Báo cáo:** `docs/codex-queue/221-report.md` (tiếng Việt) và thư mục `docs/codex-queue/221/`. Cả hai ở repo cha.

## Chỉ chạy khi

Chạy từng lệnh, lưu đầu ra vào `221/preconditions.txt`. Điều 2–6 sai thì dừng, ghi vào báo cáo:
1. Lược đồ 212 đã commit. Lệnh `git log -1 --format=%H -- docs/games/audio/firefly/schema.json docs/games/audio/firefly/README.md docs/codex-queue/212/check.mjs` ra một mã (30/10 là `83217b53870b330d345d1ee8a97f82e0adee757d`). Ghi md5 của ba file. Ngày 30/10 chúng là:
   - `schema.json`: `c37879d9b6b4a85470c10b92f937b538`;
   - `212/check.mjs`: `ffbeee75450361fe957bd6d4493cbc7d`;
   - `README.md`: `c0732e449f7e5e087460b796d686bb54`.
   md5 khác thì ghi md5 mới, làm tiếp nếu điều 2 và 3 còn đúng. Phiếu này không cần chờ commit nào.
2. `grep -n "^export function" docs/codex-queue/212/check.mjs` có `validateList`, `calculateTakes`, `calculateTotals`, `readSoundIds`, `audit`.
3. Trong `schema.json`:
   - mức file có `rows`, `excluded`, `retired`, `totals`, `sourceCommits`;
   - mỗi hàng có thêm ba trường tùy chọn `branchOnly`, `clips`, `clipsWhy`.
4. Checkout game:
   - `git -C games/typing-defense branch --show-current` ra `a2-days`;
   - `git -C games/typing-defense rev-parse td-1c` ra một mã (30/10 là `2a1f61d7da2ee6e6ca4abdc23f8775f872d9c9e7`). Mã khác thì đọc theo mã mới và ghi lại.
   Checkout đang bẩn thì ghi lại và làm tiếp: phiếu chỉ đọc object git.
5. `ls tools/audio-lab/specs/typing-defense/*.yaml | wc -l` ra 30.
6. `docs/games/audio/firefly/typing-defense.md`, `typing-defense.json`, `docs/codex-queue/221-report.md` chưa có (30/10 13:15 đều chưa có). Đã có thì có người làm rồi: dừng. Kiểm điều này **trước** khi tạo `221/`.

## Nơi làm

- **Model:** `gpt-6.1-sol`, effort `high`, sandbox `workspace-write`.
- Repo cha, nhánh đang có, cwd `.`. Không worktree, không đổi nhánh. Mọi thứ đã có sẵn; Claude không cần dựng gì.
- Đọc Wordwoven **chỉ qua object git của nhánh `td-1c`** (`2a1f61d`, nhánh 3D của map 1):
  - `git -C games/typing-defense show td-1c:<đường dẫn>`;
  - `git -C games/typing-defense grep -n '<mẫu>' td-1c -- src`.
- Không mở các worktree sau:
  - `games/.wt-td-1c` (làn L của Claude);
  - `.wt-td-scenery`, `.wt-td-ui` (làn s9 đang chạy);
  - `.wt-td-keys`, `.wt-td-vfx`.
- Checkout chính `games/typing-defense` (nhánh `a2-days`) chỉ đọc.
- Trước khi ghi gì, lưu:
  - `git status --short -uall` của repo cha vào `221/status-before.txt`;
  - `git -C games/typing-defense branch --show-current` và `git -C games/typing-defense status --short` vào `221/game-before.txt`.

**Chỉ được ghi** bốn chỗ:
- `docs/games/audio/firefly/typing-defense.md`;
- `docs/games/audio/firefly/typing-defense.json`;
- thư mục `docs/codex-queue/221/`;
- `docs/codex-queue/221-report.md`.

## Đọc trước

- **Của 212:**
  - `README.md`: tên trường, luật lượt tạo, luật vòng lặp, prompt khẳng định, chuẩn pha;
  - `schema.json`;
  - `212/check.mjs`: hàm export; `audit` và `main()` để xem cách kiểm thẻ spec;
  - `typing-survival.json`: mẫu một hàng, `assumptions`;
  - `typing-survival.md`: mẫu Markdown. Có dòng tổng `**N hàng · M lượt dự kiến**`, bảng tóm tắt `| \`id\` | tên | P0 | lượt |`, mỗi id một khối `## \`id\`` với prompt trong khối ```` ```text ````;
  - `212-report.md`.
- **Nhánh `td-1c`:**
  - `src/view/sound-map.ts`:
    - `SOUND_IDS` (dòng 17–24): `made` 39 id, `new` 26 id, cộng 65;
    - `ONE` (dòng 26), `eventSounds` (33), `ringSound` (48), `busOf` (51), `FIRES`, `RING`.
  - `src/view/audio-min.ts`:
    - `play` (dòng 156), `read` (168), `SYNTH` (198), `CAPS` (237);
    - `frame`: `day-countdown` ở dòng 114; tiếng gọi của dân ở màn tựa ở dòng 119–124, gọi thẳng `goi`, không qua id;
    - `ui()` (dòng 127); kiểu `UiSound` (dòng 32): `move`, `pick`, `off`, `lamp`.
  - `src/view/folk.ts` (`goi` dòng 135). `src/view/music.ts` là nhạc, ngoài phạm vi.
  - `src/content/slice-1a.ts`, `id: "w1-silverfall"`:
    - công trình: Fort, Archer Tower, Cannon Tower, Barracks, Gold Mine, Rice Field;
    - năm đêm và các ngày mở khóa (`stage`, dòng 212–215);
    - quái (`waves.list`, dòng 186–195);
    - boss Mộc Tinh (dòng 199–210): `warnS` của `roots` 1.5, `slam` 1.2, `summon` 0.8, `keep` 1.2, `drain` 1.2.
  - Sim:
    - `src/sim/events.ts`: `FX` (dòng 10), `RareEvent` (dòng 35–71);
    - `src/sim/stores/projectiles.ts`: `PROJECTILE`;
    - `src/sim/systems/combat.ts:135`: Fort bắn `bolt`, tháp có `splash` bắn `shell`, tháp khác bắn `arrow`;
    - `agents.ts:166`: Draconis bắn `fireball`;
    - `ult.ts:107`: `feather`;
    - `rewards.ts:51`.
  - `src/view/words/cards.ts:29`: `CALL_NAME` = Power, Build, Reap, Chop, Dig, Quiz, Spell, Stop.
  - Chữ tiếng Anh người chơi thấy: `src/ui/hud.ts` (`BOSS_LINES` dòng 20, `REASON`), `src/ui/sheets.ts`, `src/ui/tips.ts`.
  - VFX, để điền `vfxSync`: `src/view/3d/fx-pool.ts`, `src/view/fx-2d.ts`, `src/view/fx-pipe.ts`, `src/view/boss-2d.ts`.
  - `docs/audio/THEME_SOUND_LIST.md`: mốc khi thẻ spec trống.
- **Thẻ spec:** 30 thẻ ở `tools/audio-lab/specs/typing-defense/`.
  - 24 thẻ trùng id mã.
  - 6 thẻ không có id mã: `amb-dusk`, `amb-villager-call`, `music-boss`, `music-calm`, `music-stingers`, `music-tension`.
  - Lấy `when`, `purpose`, `prompt.text`, `duration.min_ms`, `duration.max_ms`, `variants.target`, `playback.mode`, `playback.channels`, `playback.bus`.
- **Tên:** `docs/games/NAMES_EN.md`, mục Lời Gọi (dòng 211–330).
- **Chất liệu:**
  - `docs/games/AUDIO_PIPELINE.md` §8.2 (dòng 610–627), §6.2, §6.4, và §3.2 dòng 129 (giọng người: "Không dùng AI");
  - `docs/games/ART_DIRECTION_2026-10-28.md` §2 (bible Wordwoven, dòng 126–235) và §8.2 (dòng 513–546; cột "Tiếng bible đòi" của từng sự kiện);
  - `tools/audio-lab/DECISIONS.md` §Q6 (dòng 164).
- **Pha VFX:** `docs/games/VFX_STANDARD.md` §3.1 (năm pha), §3.4 (khung 60 Hz). `docs/games/vfx/FIREFLY_VFX_LIST.md` có 0 clip Wordwoven.

## Việc

1. **Tập id phát được, `221/fired-ids.json`.**
   - Một mục cho **mỗi** id trong `SOUND_IDS` của `td-1c` (65 id), cộng mọi id khác mà `audio-min.ts` phát. Claude đã kiểm 30/10: `day-countdown` và bốn id `ui-*` đều nằm trong `SOUND_IDS.made`. Codex kiểm lại; id phát mà ngoài `SOUND_IDS` thì thêm và ghi rõ.
   - Mỗi mục ghi:
     - `trigger`: `file:dòng` ở `td-1c` (nhánh của `eventSounds`, dòng `ONE`, khóa `RING` hay `FIRES` của `ringSound`, hay dòng trong `audio-min.ts`);
     - `bus`: theo `busOf`;
     - `sourceEvent`: loại `RareEvent` hay loại `FX`;
     - `map1`: `w1-silverfall` có phát được id này không (`true` hay `false`). Căn cứ ở `slice-1a.ts`: năm đêm, quái từng đêm, các đòn của Mộc Tinh, công trình và đạn, lời gọi, mở khóa;
     - `map1Basis`: `file:dòng` làm căn cứ;
     - `firstStage`: tên ải đầu tiên phát được, `null` khi chưa ải nào phát được.
   - Không bịa căn cứ. Không chắc thì ghi `map1: true` và giải thích trong `map1Basis`: thà có hàng thừa còn hơn thiếu âm.
2. **Mỗi id phát được ở map 1 là một hàng** theo `schema.json`, giống cách viết của `typing-survival.json`.
   - `game` là `typing-defense`; `stage` là `w1-silverfall`; `direction` ghi "Wordwoven · ART_DIRECTION_2026-10-28 §2"; `assumptions` chép nguyên của `typing-survival.json` (`fileSeconds` 12, `silenceMs` 1000, `maxHitsPerTake` 8, `usableFraction` 0.75, `p0ReserveTakes` 1), `note` viết lại tiếng Việt cho Wordwoven.
   - `prompt`: tiếng Anh, chỉ ký tự ASCII, câu khẳng định, chỉ dành cho Adobe Firefly Generate Sound Effects.
     - Không tên riêng: Mộc Tinh viết "an ancient tree spirit", Draconis viết "the fire dragon", các Thư Đồng viết "the small scholar helpers".
     - Không tên nhạc cụ tiếng Việt có dấu: viết "a two-headed Vietnamese rice-paste barrel drum", "a Vietnamese bamboo flute", "a Vietnamese sixteen-string zither".
     - Không chữ phủ định (danh sách `negative` của 212).
     - Theo README 212 và Q6: tả đủ chuẩn bị, phát, thân, đuôi khi hành động có; cỡ nguồn rõ; mỗi hàng `hits` xin một chuỗi cú rời, mỗi cú cách nhau một giây lặng.
   - `playerName`: tên tiếng Anh đúng trong game, chỉ ký tự ASCII. Nguồn: `NAMES_EN.md` mục Lời Gọi; `view.name` trong `slice-1a.ts`; `CALL_NAME`; chuỗi trong `src/ui/**`. Ví dụ: Fort, Archer Tower, Cannon Tower, Barracks, Gold Mine, Rice Field, Fire Feather Rain, Word Shot, Power. Sự kiện không có tên hiển thị, hay chỉ có tên riêng có dấu (Mộc Tinh, Chấm, Phẩy, Gạch, Bà Cú Mực), thì để `null`; nhắc tên riêng trong `when` (tiếng Việt được).
   - `when`: tiếng Việt, ngắn; phân biệt "luôn phát" và "có điều kiện".
   - `voiceHint`: gợi ý tiếng Việt để diễn nhịp bằng giọng, hoặc `null` (README 212: khả năng Firefly dùng gợi ý giọng chưa biết).
   - Hàng chỉ dùng các trường của `schema.json` (lược đồ cấm trường lạ). Thông tin thêm như trigger hay căn cứ map 1 để ở `221/fired-ids.json` và trong `basis`.
   - `bus`: `busOf` của mã (`typing`, `ui`, `world`).
   - `targetMs` và `variants`:
     - có thẻ thì lấy `duration.min_ms`, `max_ms`, `variants.target` của thẻ, không đổi số;
     - không có thẻ (`specCard: null`) thì căn cứ vào `THEME_SOUND_LIST.md` của `td-1c` và mã (`SYNTH`, `CAPS`, nhịp sự kiện). Ghi `file:dòng` vào `basis`.
   - `shape`: `hits`, `single` hay `loop`; `loop` là `true` đúng khi `shape` là `loop`.
   - `hitsPerTake` và `takes` tính bằng `calculateTakes` của 212; `totals` tính bằng `calculateTotals`.
   - `inbox`: `~/AudioLab/inbox/firefly/typing-defense/<id>/`. Chỉ ghi đường dẫn, không tạo thư mục.
   - `priority` và `priorityWhy` theo README 212: P0 đòn chữ, súng, trúng, chết; P1 quái đánh, bị đánh, đợt dồn, kết trận; P2 UI. Lệch thì giải thích.
   - `branchOnly: null`. `sourceCommits`: `{ "td-1c": "<hash đầy đủ>", "a2-days": "<hash đầy đủ>" }`; 30/10 là `2a1f61d7…` và `f9abfd09987dadd519233c2f38692758d35cefca`.
3. **Id map 1 không phát** vào `excluded`, mỗi mục có `id`, `reason` (tiếng Việt), `firstStage` (`null` khi chưa có ải nào), `basis`.
4. **Chất liệu.**
   - Luật cứng, theo AUDIO_PIPELINE §8.2 và TK 22.1:
     - không chuông chùa, không mõ, không tụng;
     - không nhạc cụ Trung Quốc hay Nhật Bản dán nhãn Việt (nhị dẫn giai điệu, shakuhachi, taiko, dizi);
     - không laser, không synth điện tử;
     - báo động dùng kẻng sắt hay trống hội;
     - cồng chỉ cho lúc trang trọng hay báo nguy;
     - sáo trúc không có tiếng rè màng.
   - **Thang của âm** theo ART_DIRECTION §2 (cõi đá vôi huyền ảo, hùng vĩ; không còn "làng quê ấm cúng"). Cột "Tiếng bible đòi" ở §8.2 thắng chất liệu cũ của thẻ khi hai bên khác nhau. Luật cứng ở trên vẫn giữ. Thẻ "làng tre" cũ khác §2 thì §2 thắng về thang của âm; độ dài và số biến thể vẫn lấy thẻ.
   - `era`: `kept` khi giữ cách diễn của thẻ; `reworded` khi đổi theo §2 hay §8.2. `eraNote` nói đổi gì, vì sao.
   - Hàng có chữ "gong" trong prompt: `eraNote` phải có cụm `gong:` kèm lý do (trang trọng hay báo nguy). AUDIO_PIPELINE §8.2: "Chủ dự án ký duyệt từng stem nhạc và từng âm có cồng". Báo cáo liệt kê các hàng này để chủ dự án duyệt.
   - Prompt của `THEME_SOUND_LIST.md` có chữ có dấu ("trống cơm", "sáo trúc") hay chữ phủ định ("no temple bell character") thì viết lại, không chép nguyên.
5. **Id chỉ có thẻ, không có id mã:**
   - `amb-villager-call`: vào `excluded`, `firstStage: null`, **không** thành hàng Firefly. Đây là giọng người ("Ơ… ơi!"): `docs/games/AUDIO_PIPELINE.md` §3.2 dòng 129 ghi "Chủ dự án và người nhà ghi 4 biến thể, có giấy đồng ý … Không dùng AI", và thẻ ghi `source_class: voice`, `source_plan.now: [owner-recording]`, `blocked_by: [chu-du-an-ghi-am, giay-dong-y]`. Danh sách Firefly là SFX, không thay luật nguồn của giọng. `reason` nói rõ "giọng người, chủ dự án ghi âm". `basis` ghi cả hai căn cứ đó, cộng việc mã **có** phát một tiếng gọi tổng hợp ở màn tựa: `audio-min.ts:119–124` gọi `goi` (`folk.ts:135`) mỗi 3–7 s, không qua id; bước gắn file sau phải cho tiếng này đi qua id `amb-villager-call`. Không ghi mục này vào `221/fired-ids.json` (mã không phát nó qua id). Báo cáo đưa nó vào danh sách việc của chủ dự án (ghi âm), không vào danh sách tạo trên Firefly.
   - `amb-dusk`: thẻ ghi "Màn đầu (chưa có)". `git -C games/typing-defense grep -n "amb-" td-1c -- src` không ra dòng nào. `git … grep -n dusk td-1c -- src` chỉ ra màu CSS (`src/ui/theme.css:23`, `src/ui/title.css`) và tên ảnh nền `title-dusk.webp` (`src/ui/title.ts`), không có âm (Claude kiểm 30/10, 13:15). Không mã nào phát nền này, nên vào `excluded`, `firstStage: null`. Codex kiểm lại cả hai; mã khác điều trên thì theo mã và ghi lại.
   - `music-boss`, `music-calm`, `music-stingers`, `music-tension`: `excluded`; nhạc có đường riêng (AUDIO_PIPELINE §8.2, `src/view/music.ts`).
6. **Tiếng phím.**
   - `key-right`: `excluded`. Tiếng của từng phím thuộc các bộ 189–193; ART_DIRECTION §8.2 ghi "giữ synth".
   - `key-wrong`, `key-lock`, `key-group` vẫn là hàng.
   - Chạy đúng một lệnh `git -C games/typing-defense log -1 --format=%s 646e889` (chỉ đọc object git), để xác nhận nhánh `td-keys` giữ tiếng riêng cho phím sai. 30/10 lệnh ra "fix(keys): wrong and stray letters keep their own cue on Firefly sets; …". Không mở `.wt-td-keys`.
7. **Khớp VFX.** Điền `vfxSync` từ view và nhịp sim của `td-1c`. Ghi riêng hiện trạng mã và ý đồ của §8.2; không đổi tick sim.
   - Đạn: `wordshot-fire`, `arrow-fire`, `cannon-fire`, `bolt-fire`, `fireball-fire`, `feather-fall`. Ghi thời gian bay, tính từ `projectileSpeed` và `rangeM` trong `slice-1a.ts` (Fort dòng 25–30, tháp từ dòng 41). Đạn không có số ở đó (Word Shot, lông lửa: `src/sim/systems/ult.ts:22` `SPEED`) thì lấy hằng trong mã, ghi `file:dòng`.
   - Trúng và chết: `hit`, `blast`, `ink-puff`.
   - Đòn boss: dùng `warnS` của `slice-1a.ts` (`roots` 1.5 s, `slam` 1.2 s, `summon` 0.8 s, `drain` 1.2 s; cộng `keep` 1.2 s nếu có id phát). Ghi âm báo trước và âm chạm khớp mốc nào.
   - `phase` theo VFX_STANDARD §3.1.
   - `clips: []`, `clipsWhy`: "docs/games/vfx/FIREFLY_VFX_LIST.md có 0 clip Wordwoven".
8. **`typing-defense.md`** cho chủ dự án đọc, giống cách trình bày của `typing-survival.md`.
   - Đầu file:
     - dòng tổng `**N hàng · M lượt dự kiến** (P0 …, P1 …, P2 …)`;
     - bảng tổng theo nhóm: số hàng và số lượt của từng nhóm;
     - bảng tóm tắt từng id.
   - Nhóm theo buổi tạo, theo thứ tự:
     1. gõ và lời gọi;
     2. đạn, trúng, chết;
     3. boss Mộc Tinh;
     4. ngày và đêm;
     5. công trình và kinh tế;
     6. UI và nền.
     Mỗi id nằm đúng một nhóm.
   - Mỗi hàng: id, tên tiếng Anh, khi nào phát, độ dài, lặp hay không, số lượt, prompt (khối `text`), nhịp VFX, thư mục nhận.
   - Giải thích viết tiếng Việt; prompt và tên trong game viết tiếng Anh.
   - Cuối file: mục "Bị loại" và mục "Bible đòi nhưng mã chưa có id". Mục sau ví dụ tiếng riêng từng loài khi ra, đi, đánh, trúng, chết (§8.2); chỉ liệt kê, không thành hàng.
9. **`typing-defense.json`**: đúng `schema.json`, cùng nội dung với `.md`.
10. **Script kiểm `docs/codex-queue/221/check.mjs`** (Node, không thêm thư viện, không sửa file của 212).
    - Import `validateList`, `calculateTakes`, `calculateTotals` từ `'../212/check.mjs'`. Import này không chạy CLI của 212.
    - Đọc `SOUND_IDS` của `td-1c` qua `git -C games/typing-defense show td-1c:src/view/sound-map.ts` (`execFileSync`); đọc tập id phát từ `221/fired-ids.json`; đọc tên thẻ từ thư mục spec.
    - **Luật phủ:** hợp của id mã, id phát thêm và id thẻ. Mỗi id trong hợp đó nằm ở đúng một chỗ: `rows`, `excluded` hay `retired`. Id có `map1: true` phải là hàng.
      - Không dùng `audit` của 212 để kiểm phủ: `audit` buộc id chỉ có thẻ phải là hàng hay `retired`, không cho vào `excluded`, nên `music-*` và `amb-dusk` sẽ bị đếm là thiếu.
    - Đếm và in ra:
      - thiếu, lạ, trùng;
      - lỗi lược đồ (`validateList`);
      - `hitsPerTake`, `takes`, `totals` khác với `calculateTakes`, `calculateTotals`;
      - `loop` không khớp `shape`; `inbox` sai mẫu;
      - `targetMs`, `variants` khác thẻ (đọc `min_ms`, `max_ms`, `variants.target` như `main()` của 212);
      - ký tự ngoài ASCII trong `prompt` và trong `playerName` khác `null`;
      - tên riêng viết không dấu trong prompt (so nguyên từ, không phân biệt hoa thường): `Moc Tinh`, `Draconis`, `Cham`, `Phay`, `Gach`, `Ba Cu Muc`, `Thu Dong`, `Wordwoven`; kiểm ASCII ở trên không bắt được các dạng này;
      - từ cấm trong prompt: danh sách Q6 của 212 (`pop`, `puff`, `balloon`, `thud`, `thump`, `toy`, `cartoon`, `retro`, `8-bit`, `chiptune`), cộng `temple bell`, `monk`, `chant` (mọi dạng), `wooden fish`, `shakuhachi`, `taiko`, `erhu`, `dizi`, `laser`, `synth` (mọi dạng), `electronic`;
      - chữ phủ định trong prompt (danh sách `negative` của 212);
      - hàng có "gong" mà `eraNote` không có `gong:`;
      - md và json: cùng tập id ở bảng tóm tắt, cùng prompt từng chữ trong khối `text`, cùng dòng tổng.
    - `--selftest` cài sẵn ba lỗi trên bản chép trong bộ nhớ và phải bắt đủ cả ba:
      1. bỏ một hàng có `map1: true`;
      2. thêm một id lạ;
      3. thêm một chữ có dấu vào một prompt.
    - CLI ghi `221/check.txt`, `check.json`, và với `--selftest` thì `check-selftest.txt`, `check-selftest.json`. Thoát 0 khi mọi số đếm bằng 0.

## Cấm

- Mọi lệnh git có ghi. Đổi nhánh của repo cha hay của `games/typing-defense`.
- Mở, đọc file hay ghi trong `games/.wt-td-1c`, `.wt-td-scenery`, `.wt-td-ui`, `.wt-td-keys`, `.wt-td-vfx`. Đọc `td-1c` chỉ qua `git show` và `git grep`.
- Sửa `games/**`, `tools/**` (kể cả thẻ spec), `shared/**`, `schema.json`, `README.md`, file của 212, `typing-survival.*`.
- Ghi ra ngoài repo, kể cả `~/AudioLab`. Tạo, tải hay sửa file âm.
- Mạng, dev server, trình duyệt.
- Nhắc model đối tác trong prompt hay ghi chú: danh sách này chỉ dành cho Adobe Firefly Generate Sound Effects.
- Chữ có dấu hay tên riêng trong prompt; chữ có dấu trong `playerName`.
- Đụng Tu Tiên.

## Kiểm (ghi số)

1. `node docs/codex-queue/221/check.mjs` thoát 0, với:
   - 0 thiếu, 0 lạ, 0 trùng;
   - 0 lỗi lược đồ (validator của 212);
   - 0 lỗi tính lượt;
   - 0 ký tự ngoài ASCII, 0 từ cấm, 0 chữ phủ định, 0 hàng "gong" thiếu lý do;
   - md khớp json.
   Đầu ra ở `221/check.txt` và dán vào báo cáo.
2. `node docs/codex-queue/221/check.mjs --selftest` bắt đủ 3/3.
3. Số:
   - id phát ở map 1 / 65 id mã (cộng id phát thêm, nếu có);
   - số hàng; số id bị loại, theo từng lý do;
   - số hàng mỗi nhóm;
   - lượt P0, P1, P2 và tổng lượt;
   - prompt dài nhất (id, số ký tự).
4. Mỗi hàng có `specCard` là đường dẫn thẻ, hoặc `null` kèm căn cứ trong `basis`. `targetMs` và `variants` truy được về thẻ hay về `file:dòng`. Ghi số hàng có thẻ và số hàng không thẻ.
5. `sourceCommits`: `td-1c` là `2a1f61d7da2ee6e6ca4abdc23f8775f872d9c9e7` (hay mã mới, ghi lại) và `a2-days` là `f9abfd09987dadd519233c2f38692758d35cefca`.
6. `221/game-before.txt` và `221/game-after.txt` (nhánh và `status --short` của `games/typing-defense`) giống hệt nhau. 30/10: `a2-days`, sạch. Làn khác chỉ ghi vào phần Git bỏ qua của checkout này (226: `tmp/`; 225: `art-src/`); nếu vẫn khác thì liệt kê từng đường, xác nhận phiếu này không ghi gì trong `games/**`.
7. `git status --short -uall` của repo cha trước và sau (`221/status-before.txt`, `status-after.txt`): đường dẫn mới chỉ có `typing-defense.md`, `typing-defense.json`, `221/` và `221-report.md`. Thay đổi của làn khác thì liệt kê, không đụng.

## Báo cáo phải có

- Số của Kiểm 1–7, đầu ra của script kiểm và của selftest.
- Bảng `fired-ids` rút gọn: id, `map1`, trigger, lý do loại.
- Các hàng có cồng, để chủ dự án duyệt.
- Việc ghi âm của chủ dự án, ngoài Firefly: `amb-villager-call` (giọng người, AUDIO_PIPELINE §3.2 dòng 129).
- Chỗ thẻ cũ hay `THEME_SOUND_LIST` khác ART_DIRECTION §2 và §8.2, và cách đã chọn.
- Mục "Bible đòi nhưng mã chưa có id": việc cho phiếu gắn sau, không phải hàng.
- Những gì chưa biết về Firefly, giống README 212 (giới hạn ký tự prompt, độ dài file, số kết quả mỗi lượt).

**Xong khi:** có `typing-defense.md`, `typing-defense.json`, `221/fired-ids.json`, `221/check.mjs` và đầu ra của nó (0 thiếu, 0 lạ, 0 lỗi lược đồ, selftest 3/3); đủ bảy mục kiểm có số. Claude duyệt rồi commit; sau đó chủ dự án nhận `typing-defense.md` để tạo âm.

## Rủi ro

- `td-1c` có thể còn đổi khi làn L của Claude chạy lại. Vì vậy phải ghi mã commit đã đọc; Claude chạy lại script kiểm khi `td-1c` được gộp.
- Phiếu 213 (làn s8) cũng đọc README, `schema.json` và `212/check.mjs`. Hai phiếu không ghi chung file nào: `typing-defense.*` khác `dragon-hold.*`.
