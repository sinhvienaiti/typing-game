# Phiếu 132 · Chuỗi còn lại

Quét lại bằng `node docs/codex-queue/132/inventory.mjs` từ repo cha. TypeScript AST bỏ chú thích, giải Unicode escape và tách mảnh template. Khoảng thô `[À-ỹđĐ]` còn bắt dấu × và ký tự ngoài tiếng Việt; lọc chữ Việt thật sau chuẩn hóa NFC. Kết quả: **16 literal UI chưa dịch ngoài phạm vi**, **22 literal/mảnh chứa tên riêng được giữ**, **83 literal trong kit**; 0 literal tiếng Việt thường trong các thư mục được phép sửa.

## Chưa đạt: src/main.ts ngoài phạm vi ghi

Không thêm ngoại lệ cho file này vào test; test quét toàn `src/` phải đỏ cho tới khi chủ dự án cho phép dịch. Đã hỏi mở phạm vi, chưa có trả lời.

| file:dòng | chuỗi còn lại |
|---|---|
| `src/main.ts:109` | `Màn đầu chưa tải được: vào thẳng ván · F5 để thử lại` |
| `src/main.ts:144` | `Chơi lại Ngày n chưa tải được: ván mới từ đầu · F5 để thử lại` |
| `src/main.ts:223` | `Chép số chơi thử` |
| `src/main.ts:223` | `Chơi lại Ngày n` |
| `src/main.ts:223` | ` chưa tải được · F5 để thử lại` |
| `src/main.ts:225` | `Đã lưu` |
| `src/main.ts:225` | `Đã lưu file chơi thử và chép số` |
| `src/main.ts:301` | `Tạm dừng chiến thuật · Space để chạy tiếp` |
| `src/main.ts:301` | `Tắt bộ gõ tiếng Việt để gõ` |
| `src/main.ts:301` | `Esc hoặc Enter: xem lại thẻ kết` |
| `src/main.ts:302` | `Wood thừa: bán Wood ở thẻ Fort` |
| `src/main.ts:302` | `Từ dự phòng (máy chủ không có từ vựng)` |
| `src/main.ts:304` | `Tạm dừng · Esc để chạy tiếp (thẻ tạm dừng chưa tải được) · F5 để thử lại` |
| `src/main.ts:304` | `Hết ải · F5 để chơi lại (thẻ kết chưa tải được)` |
| `src/main.ts:305` | `Chơi lại Ngày n chưa tải được · F5 để thử lại` |
| `src/main.ts:306` | `Bảng hộp cát chưa tải được · F5 để thử lại` |

## Tên riêng giữ theo quy ước

`NAMES_EN.md` và AGENTS.md yêu cầu giữ tên nhân vật độc nhất: Mộc Tinh, Bà Cú Mực, Chấm, Phẩy, Gạch. Đây là ngoại lệ tên riêng, không phải nghĩa từ; nếu yêu cầu “chỉ còn nghĩa từ/kit/chú thích” hiểu tuyệt đối thì cần chủ dự án chốt lại. Phần câu quanh tên đã dịch.

| file:dòng | chuỗi còn lại |
|---|---|
| `src/app/sandbox.ts:21` | ` title="Summon Mộc Tinh"` |
| `src/content/slice-1a.ts:105` | `Mộc Tinh` |
| `src/content/slice-1a.ts:154` | `Chấm` |
| `src/content/slice-1a.ts:155` | `Phẩy` |
| `src/content/slice-1a.ts:156` | `Gạch` |
| `src/ui/hud.ts:32` | `Mộc Tinh is awake` |
| `src/ui/hud.ts:155` | `Mộc Tinh: ` |
| `src/ui/hud.ts:158` | `Mộc Tinh: ` |
| `src/ui/hud.ts:161` | `Mộc Tinh stunned! Type Power!` |
| `src/ui/hud.ts:161` | `Mộc Tinh: ` |
| `src/ui/hud.ts:162` | `Mộc Tinh: ` |
| `src/ui/hud.ts:170` | `Bà Cú Mực: ` |
| `src/ui/hud.ts:203` | `<b>Mộc Tinh</b> <small>asleep` |
| `src/ui/hud.ts:203` | ` · Boss</b> <small>Mộc Tinh awakens` |
| `src/ui/hud.ts:204` | `<b>Mộc Tinh in ` |
| `src/ui/hud.ts:205` | `<b>Mộc Tinh is rising</b>` |
| `src/ui/hud.ts:206` | `<b>Mộc Tinh retreats</b> <small>+` |
| `src/ui/hud.ts:213` | `<div class="td-row"><b>Mộc Tinh</b><small>` |
| `src/ui/sheets.ts:43` | `Foes reached Fort as Mộc Tinh arrived: type Power at nearby towers.` |
| `src/ui/sheets.ts:94` | `<p>Mộc Tinh remembers his name and leaves.` |
| `src/ui/tips.ts:20` | `Upgrade Fort to free Chấm. Helpers speed up work.` |
| `src/ui/tips.ts:24` | `Tonight Mộc Tinh awakens. Line the glowing root with towers.` |

## Nghĩa từ vựng

Không có nghĩa tiếng Việt hardcode trong literal nguồn ngoài kit. Nghĩa được đọc động từ trường `vi`/gloss: `src/app/vocab.ts`, `src/app/learn.ts`, `src/typing/decks.ts`, `src/view/words/cards.ts`, `src/ui/hud.ts`, `src/ui/sheets.ts`. Không loại cả file nào trong số này khỏi test: nhãn UI của chúng vẫn bị quét. Dữ liệu từ vựng ở `public/vocabulary/` giữ nguyên và ngoài phạm vi sửa.

## Kit — chỉ liệt kê cho Claude

Bản chép kit không đổi. Bảy lời khuyên `ADVICE_VI` từng hiện ở hồ sơ được thay bằng bảng tiếng Anh cục bộ ở UI; kit vẫn giữ nguyên. Các chuỗi balance/bot là nhãn công cụ và dữ liệu; chuỗi trong `input/keys.ts` là tập ký tự xử lý IME, không phải nhãn người chơi.

| file:dòng | chuỗi còn lại |
|---|---|
| `src/kit/balance/bands.ts:23` | `Thư giãn` |
| `src/kit/balance/bands.ts:23` | `Cân bằng` |
| `src/kit/balance/bands.ts:23` | `Thử thách` |
| `src/kit/balance/bands.ts:25` | `Thắng` |
| `src/kit/balance/bands.ts:26` | `Biên S` |
| `src/kit/balance/bands.ts:27` | `Áp lực P` |
| `src/kit/balance/bands.ts:28` | `Nhàn I` |
| `src/kit/balance/bands.ts:29` | `Ngộp O` |
| `src/kit/balance/bands.ts:30` | `Gần thua N` |
| `src/kit/balance/bands.ts:31` | `Quãng Q` |
| `src/kit/balance/gates.ts:87` | `Cùng vùng cuốn` |
| `src/kit/balance/gates.ts:88` | `Không quá dễ` |
| `src/kit/balance/gates.ts:89` | `Không quá khó` |
| `src/kit/balance/gates.ts:90` | `Chuẩn thắng ẩu` |
| `src/kit/balance/gates.ts:91` | `Gõ là sức chính` |
| `src/kit/balance/gates.ts:92` | `Chiến thuật có nghĩa` |
| `src/kit/balance/gates.ts:93` | `Bộ điều nhịp nhẹ tay` |
| `src/kit/balance/gates.ts:94` | `Học không bị lấn` |
| `src/kit/balance/gates.ts:95` | `Khớp người thật` |
| `src/kit/balance/gates.ts:146` | `trong dải` |
| `src/kit/balance/gates.ts:146` | `lệch: ` |
| `src/kit/balance/gates.ts:146` | `thấp` |
| `src/kit/balance/gates.ts:146` | `thiếu` |
| `src/kit/balance/gates.ts:159` | ` · tắt nhịp` |
| `src/kit/balance/gates.ts:172` | `không đồng thời S ≥ 90 % và I ≥ 20 %` |
| `src/kit/balance/gates.ts:178` | `novice · Cân bằng` |
| `src/kit/balance/gates.ts:178` | `thắng ` |
| `src/kit/balance/gates.ts:179` | `child · Thư giãn` |
| `src/kit/balance/gates.ts:179` | `thắng ` |
| `src/kit/balance/gates.ts:186` | `S chậm chắc > S ẩu` |
| `src/kit/balance/gates.ts:189` | `hạ quái ` |
| `src/kit/balance/gates.ts:189` | `chuẩn nhanh hơn` |
| `src/kit/balance/gates.ts:191` | `chuẩn hạ sớm hơn (Q thấp hơn)` |
| `src/kit/balance/gates.ts:192` | `standard/sloppy · thời gian hạ quái hoặc Q` |
| `src/kit/balance/gates.ts:202` | `thắng ` |
| `src/kit/balance/gates.ts:212` | `thắng ` |
| `src/kit/balance/gates.ts:212` | `Tốt hơn Kém ≥ 10 điểm %` |
| `src/kit/balance/gates.ts:223` | ` bậc/đợt, khoảng sinh ` |
| `src/kit/balance/gates.ts:223` | ` bậc/đợt, trong ±` |
| `src/kit/balance/gates.ts:225` | `nhật ký bộ điều nhịp` |
| `src/kit/balance/gates.ts:227` | `standard · tắt nhịp` |
| `src/kit/balance/gates.ts:231` | `đạt` |
| `src/kit/balance/gates.ts:231` | `trượt` |
| `src/kit/balance/gates.ts:231` | `cổng học của game` |
| `src/kit/balance/gates.ts:232` | `cổng học của game` |
| `src/kit/balance/gates.ts:247` | `lệch ≤ ` |
| `src/kit/balance/gates.ts:247` | `lệch: ` |
| `src/kit/balance/gates.ts:249` | `buổi chơi thử của người thật` |
| `src/kit/balance/gates.ts:260` | `ĐẠT` |
| `src/kit/balance/gates.ts:260` | `TRƯỢT` |
| `src/kit/balance/gates.ts:260` | `THIẾU SỐ` |
| `src/kit/balance/gates.ts:265` | `\| # \| Cổng \| Kết quả \| Số đo \|` |
| `src/kit/balance/gates.ts:268` | `thiếu: ` |
| `src/kit/balance/pace.ts:110` | `Tay bạn đang chậm dần: nghỉ vài phút rồi chơi tiếp nhé.` |
| `src/kit/balance/pace.ts:111` | `Bạn gõ nhanh nhưng hay sai: chậm lại một nhịp sẽ được Hoàn hảo nhiều hơn.` |
| `src/kit/balance/pace.ts:112` | `Gõ chắc từng chữ trước, tốc độ sẽ tự lên.` |
| `src/kit/balance/pace.ts:113` | `Nhịp gõ chưa đều: giữ một tốc độ vừa phải cho mọi từ.` |
| `src/kit/balance/pace.ts:114` | `Từ mới còn lạ: đọc nghĩa và nghe phát âm trước khi gõ.` |
| `src/kit/balance/pace.ts:115` | `Khi đông quái, chọn một từ và gõ dứt điểm rồi mới sang từ khác.` |
| `src/kit/balance/pace.ts:116` | `Bạn đang tiến bộ đều. Giữ phong độ!` |
| `src/kit/balance/typist.ts:86` | `Trẻ em` |
| `src/kit/balance/typist.ts:86` | `Hồ sơ trẻ em` |
| `src/kit/balance/typist.ts:87` | `Mới` |
| `src/kit/balance/typist.ts:87` | `Người mới tập gõ` |
| `src/kit/balance/typist.ts:88` | `Chậm chắc` |
| `src/kit/balance/typist.ts:88` | `Gõ chậm nhưng chuẩn` |
| `src/kit/balance/typist.ts:89` | `Chuẩn` |
| `src/kit/balance/typist.ts:89` | `Người chơi tham chiếu` |
| `src/kit/balance/typist.ts:90` | `Khá` |
| `src/kit/balance/typist.ts:91` | `Ẩu` |
| `src/kit/balance/typist.ts:91` | `Gõ nhanh nhưng ẩu` |
| `src/kit/balance/typist.ts:92` | `Người gõ giỏi` |
| `src/kit/balance/typist.ts:93` | `Không gõ` |
| `src/kit/balance/typist.ts:93` | `Kiểm "gõ là sức chính"` |
| `src/kit/balance/typist.ts:94` | `Chỉ gõ` |
| `src/kit/balance/typist.ts:94` | `Kiểm "hỗ trợ cần thiết"` |
| `src/kit/input/keys.ts:45` | `àáạảãâầấậẩẫăằắặẳẵ` |
| `src/kit/input/keys.ts:46` | `èéẹẻẽêềếệểễ` |
| `src/kit/input/keys.ts:47` | `ìíịỉĩ` |
| `src/kit/input/keys.ts:48` | `òóọỏõôồốộổỗơờớợởỡ` |
| `src/kit/input/keys.ts:49` | `ùúụủũưừứựửữ` |
| `src/kit/input/keys.ts:50` | `ỳýỵỷỹ` |
| `src/kit/input/keys.ts:51` | `đ` |

## Chú thích

Các chú thích cũ nhắc thuật ngữ tiếng Việt được giữ nguyên, không phải chữ người chơi đọc. Danh sách vị trí thu được từ trivia của AST:

| file:dòng | chú thích |
|---|---|
| `src/app/dev-tools.ts:32` | `/** The run's study lists (R3), and Học's store with the learning events sent and queued (td-1b-learn). */` |
| `src/app/dev-tools.ts:62` | `// Ages in ticks; the call is its id; review: a Từ Ôn (R3).` |
| `src/app/dev-tools.ts:90` | `// R2: Tối Thượng; the enemies with a mechanic (drumming until castEnd, stunned until stunUntil).` |
| `src/app/dev-tools.ts:101` | `// R3: the book with each word's due tick and times typed back (BUILD_1B §11.2), the plan's counts, the live Từ Ôn's slot.` |
| `src/app/learn.ts:1` | `/**\n * Học at the page (BUILD_1B §11.1, §11.3–§11.5, R3; docs/td/R3_PLAN.md §3.3), a chunk of its own. The store under\n * typing-defense.learn ({ v: 1, book: ids oldest first, ≤ 40; seen: id → times seen, ≤ 3 }) is the app's and the view's\n * only: never in the sim, never hashed (§11.1). Before a run planFor turns it into the run header's lists (a pure\n * function: the bots on Node call it too). During the run each word that shows bright counts as seen (the cards read it\n * for the meaning rule), and each word typed is one learning event, sent in batches every 5 s through the portal bridge;\n * a replayed day's events were dropped before anyone read them, so it sends none (the page asks the portal for focus once\n * this chunk is in). At each day, night and the run's end\n * (won, lost, the page left) the run's book is folded into the store: the words redeemed or quizzed right leave it.\n */` |
| `src/app/prefs.ts:1` | `/**\n * The settings kept under td.settings (SPLIT_PLAN D7): master, music and effects volumes 0–100, "Nhịp tự điều\n * theo cách bạn gõ" (BALANCE.md §4.2, on by default; a run keeps the value it started with) and the story's mode (BUILD_1B\n * §14, R3; null: by the profile). Read at boot; the card that changes them (ui/settings.ts) loads with the title or the\n * pause card (BUILD_1B §20: not in the start chunk). The stars of each stage won are kept under td.campaign (§4.3, R3).\n */` |
| `src/app/prefs.ts:18` | `/** The modes the settings card steps through, null ("theo hồ sơ") first. */` |
| `src/app/prefs.ts:37` | `/** The story's mode (§14, R3): the one set, else by the profile: a child plays Thư giãn, anyone else Cân bằng (BALANCE §3). */` |
| `src/app/retry.ts:1` | `/**\n * "Chơi lại Ngày n" (BUILD_1B §4.3) and "Chép số chơi thử" (§14), a chunk of its own (R3 step 1, docs/td/R3_PLAN.md §3.1):\n * the results card's buttons, a page that replays a kept run and the dev handle load it; a page with none of those never\n * does. A lost run keeps its header, its log up to the lost night's day and the day hashes in sessionStorage; the next\n * page load replays the log to that day's start and checks its hash there.\n */` |
| `src/app/retry.ts:24` | `/** The run the results card ends: what retryDay keeps, and the link of a fresh run of the page (\`learn\`: in Học). */` |
| `src/app/retry.ts:68` | `/** "Chép số chơi thử" (BUILD_1B §14, §22): the play-test file saved (loi-goi-choi-thu-….json) and copied to the clipboard. */` |
| `src/app/retry.ts:77` | `/** "Chơi lại Ngày n": the log up to the start of the lost night's day, and the hashes kept, for the next page load. */` |
| `src/app/selection.ts:50` | `/** The field point under the pointer (null: off the map): where \`=\` casts Tối Thượng when within reach (BUILD_1B §8.2). */` |
| `src/app/selection.ts:91` | `// R3: a Đầu Đàn comes with a pack of 5 to lead (Neo needs 4 by it), on the same road at the same tick; a Tanuki's pack of 8` |
| `src/app/session.ts:21` | `/** The hash of the world as each day began (index n: day n), for "Chơi lại Ngày n" (BUILD_1B §4.3). */` |
| `src/content/compile.ts:12` | `/** BUILD_1B §9.2: the direct calls' verbs (Ngắt, Neo, Phá Khiên), by index. */` |
| `src/content/rules.ts:1` | `/**\n * Starting constants of Typing Defense: the 1A part of docs/td/TYPING_DEFENSE_DESIGN.md Phụ lục A, with step 1A.6 "Lời\n * Gọi" (docs/td/BUILD_1A6.md) on top. This file is the source of truth: the bot retunes numbers here, never in the\n * rules' code. Times are seconds, distances metres; compile.ts turns times into ticks once. Per-building and per-enemy\n * numbers live in slice-1a.ts.\n */` |
| `src/content/rules.ts:64` | `/**\n * BUILD_1B §11 (R3, docs/td/R3_PLAN.md §3.2–§3.4): a word of the review book comes back returnS after it went in as the next\n * word of an economy call of ≥ minCallWords words (one Từ Ôn a call, so ≤ 25 % of its words), one live at a time, typed back\n * \`returns\` times a run at most. The study plan's shares of an economy call's words (\`plan\`; no due list: \`cold\`), freshMax\n * fresh words a run. The store keeps bookSaved words, the run's book takes the newest CALL.review; a meaning shows while a\n * word was seen fewer than \`seen\` times (by mode), the count stops at seenCap, seenIds ids kept; meaningErrors errors on a\n * word show it again; learning events go out every sendS.\n */` |
| `src/content/rules.ts:84` | `/**\n * BUILD_1B §8: Tối Thượng's charge (0–max): a call's word +perWord·(0.5 + 0.5 Q), a direct word +DIRECT.ult, an enemy dying within\n * ringM of Draconis +shard a Mảnh Chữ (SHARDS by tier; the boss's stagger \`stagger\`), +nightPerS a second by night; nothing while full;\n * minGapS at least between uses. Cast within castM of him (the app's spot otherwise: the most enemy hit points within areaM of a point\n * within autoM of him): a feather every everyTicks, each at the enemy with the most hit points within radiusM not yet aimed at (round\n * and round; none: the spot), landing ~fallS later in a blastM blast of \`damage\` magic; the boss takes ×bossMul and never burns; at the\n * rain's end the enemies left in it burn burnS. Chữ Chiêu: a call of \`words\` known short words living lifeS; each word typed brings\n * perWordFeathers more delayS later, a whole Perfect call perfectFeathers more. R2 review (G5 for every bot, BALANCE §9.1):\n * damage 25 → 21, the Khá bot's share of all damage 15–17 % → ~12 %; two feathers still fell a Cương Thi in Thử thách (2 × 21 ≥ 41.7).\n */` |
| `src/content/rules.ts:98` | `/** BUILD_1B §5.5 (R2): a helper within m of a building's rim when Rễ Trồi strikes runs to the Bastion and stands there s seconds. */` |
| `src/content/rules.ts:147` | `/** §10 "Đặt sẵn": Bastion level, villagers, how many trees nearest the Bastion are marked; the farm's plots (stage, work) so it shows every stage at once. */` |
| `src/content/rules.ts:150` | `/**\n * Balance step 4 (docs/games/BALANCE.md §4, §9.2). Pace k (the run header, k.min–k.max: BALANCE's 0.75–1.30, the floor\n * 0.70 here since R3's balance, BUILD_NOTES §7.9: the Mới bot's k is 0.70, at 0.75 it won 62 %) divides the night's pack gaps,\n * the day (the wave clock) and the day's call clocks (a quiz, a mine's half-full call), and enemies walk at\n * 1 + speedK·(k − 1) (spawn gaps alone barely moved a night, the other way at that: docs/changelog/2026-10-23-balance.md;\n * 1B R2 review: 0.2 → 0.3, Biên S of the slow and the fast bots towards each other, BUILD_NOTES §7.4).\n * An enemy within dangerM of the Bastion is danger (buildings and villagers cannot be hurt in 1A.6); the director\n * judges a night once a foe is within engageM. Step tables: at night spawn ±7 %, one elite affix (hit points\n * ×eliteHp at spawn), the peak and the lull ±3 s, a support drop near defeat (+supportLives lives, once a night);\n * by day only the call clocks ±7 %, against a band without pressure (no enemy comes by day).\n */` |
| `src/content/slice-1a.ts:1` | `/**\n * Map 1 "Đồng Cỏ Thác Bạc" (\`w1-silverfall\`, BUILD_1B §4): the 1A sandbox field \`td-sandbox\` (docs/td/BUILD_NOW.md\n * §3, TYPING_DEFENSE_DESIGN.md 22.9 cut down) with its trees (BUILD_1A6 §4.2), six buildings (the farm from 1A.6),\n * the enemies (Mộc Tinh and its Mầm Gỗ from 1B R1, Tanuki and Nuppeppō from R2), Draconis, the three Thư Đồng, the waves, the boss and the\n * five-night stage with its unlock days. Numbers come from the design (§11–14, 22.2–22.7); this file is where they\n * are retuned.\n */` |
| `src/content/slice-1a.ts:112` | `// BUILD_1B §10 (R2; TK 22.6): Tanuki drums (Ngắt breaks it) only within 9 m of a tower's or the Bastion's rim (BUILD_NOTES` |
| `src/content/slice-1a.ts:131` | `// BUILD_1B §9.2, §10 (R3; sandbox only, never in the story's waves): the Đầu Đàn hurries its pack (+20 % within 6 m;` |
| `src/content/slice-1a.ts:132` | `// Neo pins it 3 s), the Troll carries a stone dome by the towers (Phá Khiên breaks it). Melee: starting numbers.` |
| `src/content/slice-1a.ts:184` | `// 12 + 2); night 3 brings Nuppeppō (the cannon's foe), night 4 three Tanuki (Ngắt) first, the packs after them catch` |
| `src/content/slice-1a.ts:185` | `// up, then (lane A1, 27/10: P 0.3–4.7 % → 15–24 %) Ma Trơi, a pack, Ma Trơi; a second Thuồng Luồng lost gate 4.` |
| `src/content/slice-1a.ts:191` | `// BUILD_1B §4.2: the first part of night 5, one pack of Thuồng Luồng (§6.5 round 1: 5 → 4; R1 review: 5; R2: 6); the boss peak follows it.` |
| `src/content/slice-1a.ts:199` | `// BUILD_1B §5: Mộc Tinh retreats at half its hit points; its own moves; Draconis' fireballs ×0.35 on its bark (heroMul).` |
| `src/content/slice-1a.ts:200` | `// k factor (R2 §7.4: 0.3 / 6.5, cap 1.46; R3 §7.9: 0.4 / 5.5, cap 1.42; A1: 0.4 / 7.5, 1.49), Thư giãn, Học ×0.78, Thử thách ×0.9.` |
| `src/content/slice-1a.ts:201` | `// R3: Rễ hút sinh khí, a life every 30 s of its fight (R3_PLAN §7.1; 20 s cost the slow bots 10–12 points of wins, §7.9).` |
| `src/content/types.ts:77` | `/** Blast damage multiplier (Ma Trơi takes ×1.5). */` |
| `src/content/types.ts:89` | `/**\n * The three verbs of BUILD_1B §9.2, each a mechanic a direct call breaks (window T). Ngắt (interrupt): it stands and\n * drums; broken: stunned stunS, \`gold\`; let run: radiusM heals healPct. Neo (anchor, R3): broken, the pack within radiusM\n * stands freezeS and the leader takes ×takenMul for takenS; its aura ×auraSpeed within radiusM is always on. Phá Khiên\n * (shield, R3): a dome of domeM rides on it for T (shots from outside ×outsideMul); broken: stunned stunS, none for lockS.\n * Each starts with \`need\` others within radiusM and an attack building's rim within reachM; cooldownS from its end.\n */` |
| `src/content/types.ts:116` | `/** The sandbox's "Đặt sẵn" (§10): building id, x and z, put down at once. */` |
| `src/content/types.ts:131` | `/**\n * The boss of a stage (BUILD_1B §5): its enemy (whose hit points are the base), retreat at retreatPct of them, hit\n * points ×(1 + kHp·d + kHp2·max(0, d)²), d = k − 1 (both ways), up to kHpMax and ×modeHp of the run's mode, Draconis' own fireballs ×heroMul\n * ("Vỏ dày"), and its moves; the stagger's Dồn lửa calls ask round(E / burstPerE) words, 1 to burstWords.\n */` |
| `src/content/types.ts:150` | `/** Building id, "keep2", "keep3", "upgrade" or "ult" (Tối Thượng, R2) → the day it opens. */` |
| `src/kit/balance/flow.ts:40` | `/** This many dropped locks within \`abandonTicks\` is overload ("bỏ khóa liên tục"). */` |
| `src/kit/balance/flow.ts:85` | `/** Share of damage not done by typing ("phần phe ta"); null when the game reports no damage. */` |
| `src/kit/balance/profile.ts:203` | `/** Defaults blended into measurements by confidence (BALANCE.md §2: "trộn dần sang số đo"). */` |
| `src/kit/balance/typist.ts:84` | `/** BALANCE.md §6 "Bộ bot chuẩn". "Không gõ" has no a or CV: it never types (1 and 0 are placeholders). */` |
| `src/kit/input/keys.ts:2` | `/**\n * Reading the keyboard for Campaign 3D's typing, safely with Vietnamese input\n * methods on.\n *\n * Two kinds of Vietnamese input reach the page differently:\n *  - an input method of the OS or the browser (the Windows / macOS Vietnamese\n *    keyboards, Chrome IMEs) composes in the page: its presses arrive as\n *    \`isComposing\`, \`key === "Process"\` or keyCode 229. They are skipped, as\n *    the 2D game does (src/main.ts keydown), so a press still composing "â"\n *    from "a a", or the Enter that commits it, does nothing;\n *  - UniKey / EVKey work outside the browser: they swallow the modifier key\n *    (the second "o" of "good", the "s" of "is", the "w" of "how") and send a\n *    Backspace and the accented letter instead ("ô", "í", "ơ"). That key never\n *    reaches the page, so it cannot be read back here; the game can only see\n *    the accented letter and tell the player to switch the input method off.\n */` |
| `src/kit/input/keys.ts:42` | `// Latin letters with Vietnamese marks, and đ, in both cases.` |
| `src/main.ts:1` | `/**\n * Lời Gọi (index.html), step 1A "Cổng vui" (docs/td/BUILD_NOW.md) with 1A.6 "Lời Gọi" (docs/td/BUILD_1A6.md) and 1B's\n * map 1 with Mộc Tinh (docs/td/BUILD_1B.md) in the Văn Điền theme (SPLIT_PLAN D7): the title screen first (a link with\n * ?sandbox= skips it, ?title=1 / 0 forces it), while the vocabulary loads; the story stage, or the sandbox with\n * ?sandbox=1. A lost run may be played again from the day of the night it was lost ("Chơi lại Ngày n": the page\n * reloads, replays the log to that day's start and checks its hash). Then the world steps at 60 Hz in a session, the 2D\n * view draws it, the calls' word cards float over it, the keys, the mouse and the HUD act through the selection, sound\n * and music follow its events, Esc's pause card and the results card sit over it, and window.__td lets the browser\n * scenarios drive it through commands. The typing profile (app/skill.ts, BALANCE.md §2) gives the run its header (E,\n * pace k, the pace director by the settings) and takes each day and night's typing after it. The title, its settings\n * and Hồ sơ gõ cards, the pause and results cards, sound and the sandbox panel are chunks of their own (BUILD_1B §20):\n * at "/" the page starts with this entry and the title only (scripts/bundle-budget.mjs counts that start set), the rest\n * comes once the page is usable or when picked; each is retried, then the page falls back (src/app/chunks.ts, R2 review\n * fix 2) and asks again when it is wanted (R2 review fix 3). R3 step 1 (docs/td/R3_PLAN.md §3.1) took window.__td\n * (app/dev-tools.ts) and "Chơi lại Ngày n" with "Chép số chơi thử" (app/retry.ts) out of this entry too. Học (R3,\n * BUILD_1B §11; app/learn.ts, a chunk asked for at once, with the portal bridge) plans the run's study lists before its\n * first step, counts the words seen, sends the learning events and keeps the review book across runs; one that cannot\n * load plays with no lists. The teaching table (ui/tips.ts) is a chunk too: Bà Cú Mực's rows in the frame at the top,\n * what a building does on its card.\n */` |
| `src/main.ts:71` | `/** A fresh run's mode: Học with ?learn=1, the sandbox Cân bằng (its panel switches), the story the settings' (R3, BUILD_1B §14). */` |
| `src/main.ts:73` | `/** The run header from the profile and the "Nhịp tự điều" setting. */` |
| `src/main.ts:75` | `/** Học (app/learn.ts): the run waits for it at tick 0 (its study lists go in the header); one that cannot load plays with none. */` |
| `src/main.ts:84` | `// Hồ sơ gõ card when picked, its settings card when picked or with the pause card's chunk, which holds one, once the page` |
| `src/main.ts:113` | `/**\n * "Chơi lại Ngày n" (BUILD_1B §4.3) kept by the last page under td.retry (app/retry.ts RETRY_KEY), read once. Its chunk\n * (app/retry.ts, with "Chép số chơi thử") loads at once when there is one, else once the page is usable for the results\n * card's buttons; one that cannot load starts the run over, told in the HUD.\n */` |
| `src/main.ts:135` | `// test pass 27/10: "Bắt đầu · Bản đồ 1" from the sandbox's title opened the sandbox` |
| `src/main.ts:147` | `/** The run's mode at its start (the replay's header): Học with ?learn=1 or the title's choice, else the settings' (freshMode). */` |
| `src/main.ts:157` | `// A run left mid-cycle counts as a quit (the trend keeps it; the measures do not); the title alone is no run. Học keeps its book.` |
| `src/main.ts:166` | `/** The study lists the run plays (flags(), "Chơi lại Ngày n"): a replayed day's, else planned once app/learn.ts is in. */` |
| `src/main.ts:209` | `/**\n * Esc's pause card and the results card, with their settings card: a chunk fetched once the page is usable, asked again\n * when a card is wanted; without it the HUD says the pause or the end (R2 review fix 2). "Xem bản đồ" puts the results away.\n */` |
| `src/main.ts:254` | `// "Xem bản đồ" put the results away: Esc or Enter brings them back (test pass 27/10: it was one way, F5 only).` |
| `src/sim/commands.ts:309` | `/** §10 "Đặt sẵn": the Bastion at level 3, the map's preset put down built and free (a farm's plots at every stage), 5 villagers, the 8 standing trees nearest the Bastion marked. */` |
| `src/sim/events.ts:50` | `// Tối Thượng cast (R2)` |
| `src/sim/events.ts:52` | `// broken by its word, or let run; verb: Ngắt, Neo, Phá Khiên (VERBS)` |
| `src/sim/events.ts:54` | `// a Từ Ôn typed (R3): item its deck index; redeemed out of the book` |
| `src/sim/nav/astar.ts:106` | `/** The path pulled tight from (sx, sz) to (gx, gz) (TK 25.9 "kéo dây"): from each corner on to the furthest cell in a clear straight line. Writes ≤ max (x, z) points into \`out\` from \`at\`; returns how many, the goal last unless cut short. */` |
| `src/sim/nav/connectivity.ts:1` | `/**\n * Breadth-first reach on the walking grid (TK 12.5 "lối đi"): after a building goes down, every work socket must still\n * be reachable from the Bastion. Scratch arrays are allocated once per grid size.\n */` |
| `src/sim/nav/grid.ts:1` | `/**\n * The walking grid (docs/td/TYPING_DEFENSE_DESIGN.md 25.9): 1 m cells over the 96 × 96 m field. A cell is blocked by\n * any painted water not on a bridge or by a building disc; Thư Đồng walk it, and placement checks that every work\n * socket stays reachable from the Bastion on it.\n */` |
| `src/sim/stats.ts:11` | `// BUILD_1B §15: damage on the boss (all, typed, Draconis' own), retreats, lives lost at the peak, buildings rooted, the chest, Dồn lửa words typed and asked.` |
| `src/sim/stats.ts:13` | `// R2: Tối Thượng's casts, feathers, damage on the boss; Mảnh Chữ; direct words typed and mechanics let run; helpers panicked.` |
| `src/sim/stats.ts:15` | `// R3 (BUILD_1B §11): Từ Ôn typed back, redeemed of them, fresh words of the study plan dealt.` |
| `src/sim/stores/boss.ts:4` | `/**\n * The boss peak's state (BUILD_1B §15), hashed like every store. Times are ticks (−1: none). \`targets\` holds the ids\n * of the buildings Rễ Trồi aims at, its warning ending at \`rootsEnd\`; a slam aims along (slamX, slamZ).\n */` |
| `src/sim/stores/buildings.ts:8` | `/**\n * Buildings, the Bastion in slot 0 (TK 11). A new one is a site (BUILD_1A6 §4.3): \`upTo\` is the level being built (0:\n * none), \`progress\` 0–1 of that work, and nothing runs before \`ready\`; an upgrade keeps the building running at its\n * level meanwhile. \`builtTick\` and \`paidGold\`/\`paidWood\` are the last site or upgrade and its price: what an undo\n * within 5 s refunds; \`spentGold\`/\`spentWood\` everything it cost, what a sale refunds 60 % of (BUILD_1B §7). Rễ Trồi\n * stuns it until \`stunUntil\` (§5.5).\n */` |
| `src/sim/stores/calls.ts:3` | `/** BUILD_1A6 §5.1, in the director's priority order (§5.3): power, build, then harvest = chop = mine, then quiz; 1B R2: Chữ Chiêu (ult) and direct calls. */` |
| `src/sim/stores/calls.ts:5` | `/** Rank of each kind for the director: the economy three share one; Chữ Chiêu and direct calls rank with power (BUILD_1B §8.3, §9.1). */` |
| `src/sim/stores/calls.ts:36` | `/** A "Dồn lửa" power call of the boss's stagger (BUILD_1B §5.2). */` |
| `src/sim/stores/calls.ts:40` | `/** It had its Từ Ôn (R3, BUILD_1B §11.2: one a call). */` |
| `src/sim/stores/ult.ts:1` | `/**\n * Tối Thượng (BUILD_1B §8), hashed like every store: the charge (0–100), the last cast's tick, the rain (on: 1) at\n * (x, z) with its feathers left to drop, the next drop and the last one, feathers due at dueAt (Chữ Chiêu), its call's\n * id, and the enemies its feathers aimed at this round.\n */` |
| `src/sim/systems/agents.ts:1` | `/**\n * The hero and the helpers on the map (docs/td/TYPING_DEFENSE_DESIGN.md 5, 8.2–8.4, 25.9; 25.6 steps 3, 7;\n * BUILD_1A6 §6): Draconis flies, Thư Đồng and the NPC workers walk the A* path, pulled tight. Agents go to a\n * point or a building; their help rings light the calls inside them, and a helper near economy work speeds it.\n * The hero throws fireballs whenever it stands on the ground with an enemy in reach.\n */` |
| `src/sim/systems/agents.ts:111` | `/** Rễ Trồi struck building b (BUILD_1B §5.5, R2): a helper within 6 m of its rim panics and runs to the Bastion. */` |
| `src/sim/systems/attention.ts:99` | `// Each round opens a queued call or lights one in a ring, so it ends; at the cap new calls wait queued (CHỜ),` |
| `src/sim/systems/boss.ts:1` | `/**\n * Mộc Tinh, the boss peak at the end of the stage (BUILD_1B §4.4, §5). Day 5 warns of it and picks the branch it will\n * walk. Once night 5's first part has spawned and ≤ 2 live (or 30 s on), a 12 s lull, held while a heavy foe walks the\n * roads' shared end; then two escort packs leave the rift and, 6 s later, the boss comes up at the fork. It walks on,\n * never blocked, and strikes after a warning: Rễ Trồi stuns the buildings within 8 m, Quật cành hits and knocks back\n * the soldiers in front, at 70 % it staggers (5 s still and vulnerable, every stun lifted, "Dồn lửa" power calls on the\n * nearest attack buildings in reach), in phase 2 it calls Mầm Gỗ, at the Bastion it strikes 3 lives a blow; from its\n * rise its roots drain a life every drain.everyS (R3). At 50 % it retreats: the chest paid, 2 s later all foes melt.\n */` |
| `src/sim/systems/boss.ts:93` | `/** The buildings (not the Bastion) whose rim lies within Rễ Trồi's reach of it, by id; written to S.targets when \`keep\`. */` |
| `src/sim/systems/boss.ts:137` | `/** Quật cành: soldiers within reach of its rim, in the 120° in front of it (toward the nearest when it began). */` |
| `src/sim/systems/boss.ts:175` | `/** Phase 2: Mầm Gỗ sprout at its feet (0.8 s), then walk on its road. */` |
| `src/sim/systems/boss.ts:194` | `/**\n * A blow on the Bastion after a warning: Quật Lũy once it stands at it (−3 lives a blow); Rễ hút sinh khí from anywhere, every\n * drain.everyS from its rise, its clock started again by the stagger (R3, docs/td/R3_PLAN.md §7.1: a cost of the boss's time alive that\n * no clearing of the escort takes away; a quick kill pays less).\n */` |
| `src/sim/systems/boss.ts:220` | `/**\n * At 70 %: 5 s still, vulnerable, the roots pulled back (every stun ends), and "Dồn lửa" (§5.2; 1B R1 review): attack\n * buildings with it in reach + 2 m, nearest first, up to the mode's bright cap, get a power call of 1–3 words by E that\n * lights in a help ring or not; a power call already open becomes it.\n */` |
| `src/sim/systems/boss.ts:235` | `// R2: its Mảnh Chữ, Draconis within 12 m` |
| `src/sim/systems/boss.ts:297` | `/** A heavy foe (leak > 1, never the boss) on the roads' shared end, from the merge to the Bastion: Thuồng Luồng there reach it with the boss. */` |
| `src/sim/systems/calls.ts:43` | `/**\n * The bag of the band ending at \`hi\` letters, made on first use (a band's low end follows E alone); \`known\`: words of\n * the levels below the run's top only (Chữ Chiêu, direct calls: BUILD_1B §8.3, §9.1). The hook for word topics (§5.2,\n * TK 22.5: harvest words of fields and food…): a topic would key its own bag here; the vocabulary tags none yet.\n */` |
| `src/sim/systems/calls.ts:53` | `/** A call follows whoever makes it: its enemy (a direct call), its NPC, its helper (a quiz) or Draconis (Chữ Chiêu), else its building. */` |
| `src/sim/systems/calls.ts:85` | `/**\n * Gives bright call c its next word (tier 1 only: one first letter a live word), on the \`call\` kind's letters (Chữ Chiêu's and a\n * direct call's on their own kinds, which may take the letters the others leave: TK 6.5); a quiz waits for a word of the book quietly.\n * An economy call's (build, harvest, chop, mine) may be a Từ Ôn, else a word of the study plan (R3, BUILD_1B §11.2, §11.4: learn.ts).\n */` |
| `src/sim/systems/calls.ts:259` | `/**\n * Word s is typed: scored, the chain moved, the review book kept (§7: a word typed sloppy or with 2 errors goes in, to its\n * end if it was there; a quiz typed right takes its word out; a Từ Ôn by learn.ts), the work pushed; the call goes on locked, or ends.\n */` |
| `src/sim/systems/calls.ts:279` | `// BUILD_1B §8.1: every call's word charges Tối Thượng` |
| `src/sim/systems/calls.ts:294` | `// A call past its life gives no next word (R2: Chữ Chiêu lives 4 s, Dồn lửa 5 s, however its words go).` |
| `src/sim/systems/calls.ts:324` | `/** Whether call c lies in a help ring now (or is the locked one, or a Dồn lửa call: 1B R1 review): bright. */` |
| `src/sim/systems/combat.ts:1` | `/**\n * Damage, targeting, and the attacks of towers, the Bastion's crossbow, soldiers and enemies\n * (docs/td/TYPING_DEFENSE_DESIGN.md 10, 11.3, 12.4, 13; 25.6 steps 6–7; BUILD_1A6 §4.5).\n *\n *   dmg = round(base × power × (1 − armour) × crit), at least 1\n *\n * \`base\` is uniform in [min, max] on the "combat" stream, a crit is drawn on the "crit" stream, and rounding happens\n * once, on impact. A tower aims at the enemy furthest along its route (least distance left); ties go to the lower id.\n * A tower with a power charge fires a powered volley and spends it. The boss (BUILD_1B §5.1) takes Draconis' own\n * fireballs ×heroMul (0.35, "Vỏ dày"), every hit ×1.25 while it staggers, and never dies of it (it retreats at 50 %);\n * a hit stops at the stagger's line in phase 1 and at the retreat's till phase 2's first Mầm Gỗ sprout, so the\n * stagger's burst never skips phase 2 (test pass row 26). A building Rễ Trồi stunned does not fire.\n */` |
| `src/sim/systems/combat.ts:97` | `/** Burning (TK 10.3, Draconis' Word Shots from a cannon; Tối Thượng's rain): magic damage a second after resist, dealt in whole points, by who set it. */` |
| `src/sim/systems/deaths.ts:1` | `/**\n * Deaths and leaks (TK 25.6 step 15). A kill's gold reaches the treasury on the tick the enemy dies (TK 17.4: coins\n * flying to the HUD are only a picture), its Mảnh Chữ charge Tối Thượng near Draconis, and a Nuppeppō no blast killed\n * splits in two where it fell (BUILD_1B §8.1, §10); a leak costs the Bastion its lives, and at 0 the run is lost.\n */` |
| `src/sim/systems/direct.ts:1` | `/**\n * Direct calls and their verbs (BUILD_1B §9; R2 Ngắt, R3 Neo and Phá Khiên), where the village fights (an attack\n * building's rim within reachM: R2 learnt that by the rift no ring lit them): a Tanuki with 4 others within 6 m (9 m)\n * stands and drums; a Đầu Đàn with 4 others within 6 m (20 m) calls its pack on; a Troll (25 m) raises a 4 m dome\n * riding on it; those two also wait for a help ring (test pass 27/10: from 20–25 m out their calls lit late if ever). Each\n * lasts T = clamp(0.8 + k_d·(len + 1)·12 / E; 3; 7) s. A direct call of one known short word follows the enemy, lit in\n * a help ring and within the typing budget; at most 2 open (3 with the boss up), one more runs uncalled.\n * Typed: +2 gold (the leaf +5 more), Tối Thượng +3; the drum breaks (stunned 2 s), the pack stands 3 s and the leader\n * takes ×1.3 for 6 s, or the dome breaks (stunned 1.5 s, none for 10 s). Let run: a drum heals 25 % within 6 m (never\n * the boss); a pack walks on (the leader's +20 % aura, move.ts, is always on); a dome holds T (shots from outside ×0.3).\n */` |
| `src/sim/systems/direct.ts:44` | `/** The verb (VERBS) of call c's enemy: what typing it breaks (the view's icon and name); Ngắt when it has gone. */` |
| `src/sim/systems/direct.ts:119` | `/** The domes up this tick (Phá Khiên let run: x, z, radius, ×outside a dome), into \`out\`. */` |
| `src/sim/systems/learn.ts:1` | `/**\n * Học in the sim (BUILD_1B §11.2–§11.4, R3; docs/td/R3_PLAN.md §3.2). The run header carries three lists of deck ids that\n * src/app/learn.ts plans before the run (a replay file carries them too): \`book\`, the saved review book, goes into the\n * run's book at tick 0 (its newest 20; an id not in the deck is dropped); \`due\` and \`fresh\` feed the study plan. An\n * economy call's next word (harvest, chop, build, mine) is, in order:\n * - a Từ Ôn: a book word due again 25–45 s after it went in, its letter free; one live, one a call of ≥ 4 words, typed\n *   back twice a run at most. Typed clean or Good at least: "Chuộc lại", +1 knowledge, out of the book; else it stays\n *   and comes back later (a sloppy one at the book's end).\n * - with a plan, a part drawn on the \`words\` stream (due 60 %, current 25 %, fresh 15 %; no due list: current 85 %,\n *   fresh 15 %), then the part's first word not dealt yet that fits E's band and a free letter (a due word is reviewed\n *   once a run, R3_PLAN §5 A15); 8 fresh words a run at most, none while the boss is up (its night). A part with\n *   nothing that fits falls back to the current levels.\n * - else the bag of the current levels, as before.\n * A header with no list draws nothing, so an old replay plays as it did. The store is hashed (sim/hash.ts).\n */` |
| `src/sim/systems/learn.ts:29` | `/** The plan's lists as deck indices (a word dealt turns −1); counts; the live Từ Ôn's word slot (−1). */` |
| `src/sim/systems/learn.ts:95` | `/** A Từ Ôn for economy call c (word × 4 + 1), −1 none (§11.2). */` |
| `src/sim/systems/learn.ts:141` | `/** A Từ Ôn typed (§11.2): redeemed (clean, or Good at least) leaves the book with +1 knowledge; a miss goes to its end; else due again later. */` |
| `src/sim/systems/move.ts:1` | `/**\n * Enemies walk their lane (TK 25.6 step 4, 13). Blocked by enough soldiers they stop; blocked by fewer than their\n * weight they push on at half speed. One that reaches the Bastion is marked leaked; the deaths system takes the lives.\n * The boss is never blocked, stands while stunned and stops short of the Bastion to strike it (BUILD_1B §5.1, §5.3). R3\n * (§9.2, §10 "dẫn bầy"): a Cương Thi Đầu Đàn hurries every enemy within its radius but the boss (×auraSpeed, itself\n * too), always, and leads them: on its road none walks on past DIRECT.leadM ahead of it (they wait for it), so the pack\n * Neo pins stays by its leader.\n */` |
| `src/sim/systems/pace.ts:1` | `/**\n * The run's pace (docs/games/BALANCE.md §4, §9.2; 25.6 after step 17). The header, recorded with the run, holds the\n * player's pace k and the "Nhịp tự điều" setting. k is the night's intensity and the day's call frequency: the pack\n * gaps and the day (the wave clock) ÷ k, enemies walk ×(1 + speedK·(k − 1)), the quiz and mine calls come ÷ k sooner.\n * A night (the wave, BALANCE.md §3 "thời gian đợt": the stage's flow) and a day each feed their FlowMeter: danger is\n * an enemy within PACE.dangerM of the Bastion, HP its lives, live words, words waiting at the bright-call cap, busy a\n * lock or a decision open (a call waiting, an order under way, a building the treasury affords), kills with their\n * path fraction. The phase's director judges every 5 s once the night's foes have walked in: at night a step is the\n * spawn interval ±7 %, one elite affix, the peak or the lull ±3 s, or a support drop near defeat (once a night); by\n * day only the call clocks move. The AttentionDirector keeps the typing budget: a call made sooner waits for room.\n * Meters, directors and what they changed are hashed; every step is a \`pace\` event.\n */` |
| `src/sim/systems/pace.ts:59` | `/** The run's mode before its first step (the title's Học, a replay's header): the day's length, the directors' band, E's floor. */` |
| `src/sim/systems/projectile.ts:1` | `/**\n * Shots fly and land (TK 25.6 step 8). A shot follows its target while it lives, then flies on to the last point it\n * saw. On arrival a blast hurts its target at whatever height the attack aimed (Draconis hits high flyers), and every\n * other enemy in its radius at a height blasts reach (COMBAT.splashHits, TK 10.4: ground and low), from full damage at\n * the centre down to the rim's share (cannon: 50 %), times the enemy's blast multiplier (Ma Trơi ×1.5); a single shot\n * hurts its target if it still lives. A burning shot (Draconis' Word Shot from a cannon) sets every enemy it hurts on\n * fire. R3 (BUILD_1B §9.2): an enemy under a Troll's dome takes a shot launched outside it ×0.3 (Tối Thượng's feathers\n * fall from the sky, as before).\n */` |
| `src/sim/systems/rewards.ts:37` | `// A "Dồn lửa" call's shot goes at the boss while it is in reach (BUILD_1B §5.2).` |
| `src/sim/systems/spawn.ts:1` | `/**\n * Spawning (TK 25.6 step 2): queued spawns whose tick has come enter at the gate, spread across the road by the spawn\n * stream, with the mode's hit points (BUILD_1A6 §2). Enemies may also come up along a road (the boss, its Mầm Gỗ, a\n * Nuppeppō's halves) and packs be queued into the running wave.\n */` |
| `src/sim/systems/ult.ts:1` | `/**\n * Tối Thượng, Mảnh Chữ and Chữ Chiêu (BUILD_1B §8; after step 7). The charge fills from typed words, broken mechanics,\n * Mảnh Chữ (enemies dying within 12 m of Draconis, the boss's stagger) and the night itself, never past full. Cast\n * (the \`ult\` command) within 20 m of Draconis once it is full and 45 s after the last: "Mưa Lông Lửa", a feather every\n * 10 ticks, each falling ~0.8 s onto the enemy with the most hit points in the 6 m it has not aimed at yet (round and\n * round; none: the spot) in a 1.5 m blast of 25 magic (the boss ×0.25: combat.ts). The Chữ Chiêu call (3 known short\n * words over Draconis, 4 s) brings 3 feathers a word 0.3 s later, a whole Perfect call one more. Once the last has\n * fallen and the call is over, the enemies left in the rain burn 3 s (never the boss). The app picks the spot (ultSpot)\n * and the command carries it, so a replay casts the same rain.\n */` |
| `src/sim/systems/ult.ts:32` | `/** \`shards\` Mảnh Chữ of something brought down at (x, z): charge, if Draconis is within 12 m. */` |
| `src/sim/systems/ult.ts:54` | `/** Shut until the night of its unlock day (BUILD_1B §12 "dùng được từ Đêm 3"; test pass 27/10: day 3 already cast it). */` |
| `src/sim/systems/ult.ts:74` | `/** Chữ Chiêu: \`n\` feathers more, 0.3 s from now. */` |
| `src/sim/systems/waves.ts:50` | `/** A day's ticks at pace k: the wave clock (BALANCE.md §4.1 "giờ đợt"), ÷ k. */` |
| `src/sim/systems/waves.ts:72` | `/** The night falls: the next wave comes (the sandbox's "Sinh đêm" may add one to a night already running). */` |
| `src/sim/world.ts:83` | `/** Index n: the tick at which day n's world stands (after the step that began it): "Chơi lại Ngày n" replays to it. */` |
| `src/sim/world.ts:128` | `/** Tối Thượng (BUILD_1B §8, R2). */` |
| `src/sim/world.ts:130` | `/** Học (BUILD_1B §11, R3): the study plan from the run header, the live Từ Ôn. */` |
| `src/sim/world.ts:213` | `// BUILD_1B §8 (R2): Tối Thượng's charge and its feathers` |
| `src/typing/decks.ts:62` | `/**\n * A short meaning for a card: notes in brackets left out, the first sense, then more while it stays within 22 letters\n * (BUILD_1A6 §7). One over 26 keeps its words whole: up to its last comma that fits, else its last whole word and "…"\n * (review R2: "chưa bao giờ, không bao g…").\n */` |
| `src/ui/build-menu.ts:23` | `/** A building's "làm gì" line from the teaching table's chunk (none before it is in). */` |
| `src/ui/build-menu.ts:40` | `/** A farm's plots by stage (§4.1): "Chín 1 · Lớn 2 · Trống 1". */` |
| `src/ui/hud.ts:19` | `/** Mộc Tinh's own lines (TK 22.7); Bà Cú Mực's teaching table is ui/tips.ts, a chunk of its own (R3). */` |
| `src/ui/hud.ts:44` | `/**\n * Pause and sound; the resources and lives (BUILD_1A6 §9; a blow on the Bastion flashes "−3" there); "Ngày 2 · 0:41",\n * "Đêm 2 · còn 12 quái" or dawn; knowledge and the review book once there are any (§7); the early night call (§2).\n */` |
| `src/ui/hud.ts:65` | `/**\n * The early night call (the owner's play-test, 26/10/2026): its gold and the day's time left on the button, a bar that\n * empties with them, a pulse in the last 10 s; paused, "Đã dừng" where the time was.\n */` |
| `src/ui/hud.ts:96` | `/** Build and hire; Tối Thượng with its charge (BUILD_1B §8.2, R2); the tactical pause where the mode has it (§8). */` |
| `src/ui/hud.ts:105` | `/**\n * Bà Cú Mực's teaching rows and the boss bar (BUILD_1B §13.1: never in the middle of the screen, one line at a time): at\n * the start of each story day and night her row of the table (§12, R3; ui/tips.ts once its chunk is in), one sentence a\n * line, and its chip till the phase ends, in the teaching frame at the top right, off the field (teachHtml: at the top\n * middle it hid the rift the enemies come from, R3 pictures); from day 5's warning in the boss bar at the top middle, with\n * Mộc Tinh's lines and the stagger's call; a blow on the Bastion (R3: and each drain); the "ghost" health that follows a hit down 0.4 s late.\n * The sandbox skips the table but the boss's rows.\n */` |
| `src/ui/hud.ts:121` | `// the moves whose line it has said (Rễ Trồi; R3: Rễ hút sinh khí)` |
| `src/ui/hud.ts:144` | `// replayed day (Chơi lại Ngày n drops its events) gets its row too (review R1); dawn and the end clear the chip. The` |
| `src/ui/hud.ts:168` | `/** Bà Cú Mực's line, one sentence a line so it stays one line at 1280 × 720 (review R1); two at most (tests/td-tips.test.ts). */` |
| `src/ui/hud.ts:186` | `/** The teaching frame while there is no boss (R3): the chip, then Bà Cú Mực's line. */` |
| `src/ui/hud.ts:189` | `// A chip wraps between its parts ("Gõ chữ đầu để chọn · Esc để thôi"), never inside one.` |
| `src/ui/profile.ts:1` | `/**\n * "Hồ sơ gõ" (docs/games/BALANCE.md §2): the card the title opens to show the player how they type, from the\n * profile kept under typing-defense.skill: speed, accuracy, the time to start a new word, evenness, one short\n * advice line (the kit's skillAdvice), and the pace the next run will take. Until enough has been measured the\n * numbers lean on the mode's defaults, and the card says so. Keyboard first: Enter or Esc closes.\n */` |
| `src/ui/settings.ts:1` | `/**\n * The settings card (SPLIT_PLAN D7) the title and the pause card open, over app/prefs.ts (td.settings): the volumes,\n * "Nhịp tự điều theo cách bạn gõ" and the story's mode (BUILD_1B §14, R3: "Theo hồ sơ", Thư giãn, Cân bằng, Thử thách, Học;\n * set on the title it is the run's, during a run the next one's). A chunk of its own (BUILD_1B §20). Keyboard first: ↑ ↓\n * pick a row, ← → move a volume by 10, switch the pace or step the mode, Enter or Esc closes; a click on a bar sets it, on\n * the pace row switches it, on the mode row steps it.\n */` |
| `src/ui/settings.ts:16` | `/** The mode row's value: the mode's name, or "Theo hồ sơ" (a child plays Thư giãn, anyone else Cân bằng). */` |
| `src/ui/sheets.ts:1` | `/**\n * The pause and results cards (SPLIT_PLAN D7): dó paper in the middle of the map, never a HUD panel (the word cards do\n * not part around them). Pause (Esc, the HUD's Ⅱ): Chơi tiếp, Cài đặt, Về màn đầu. Results (BUILD_1B §4.3, §13.1): "Giữ\n * được làng" with its stars stamped one by one, or "Lũy đã vỡ" with a hint read off the run, and on a story won the\n * best stars kept (R3: "Kỷ lục ★★", new or not); the numbers, "Từ cần ôn" (the review book's newest five with their\n * meaning); Chơi lại Ngày n (after a night past the first was lost), Chơi lại (từ đầu), Chép số chơi thử, Xem bản đồ,\n * Về màn đầu. Keyboard first: ↑ ↓ pick, Enter chooses, Esc goes back to the game (or closes the settings).\n */` |
| `src/ui/sheets.ts:19` | `/**\n * The results card's run: a story or the sandbox, a "Chơi lại Ngày n" this run came from (0: none), whether its chunk is in\n * (R3 step 1), the story's best stars after this run and whether this win set them (R3, td.campaign), the lives the boss's blows took.\n */` |
| `src/ui/sheets.ts:28` | `/** The won card's record line: the best stars kept, "mới" when this win set them (none in the sandbox). */` |
| `src/ui/sheets.ts:31` | `/**\n * The loss card's hint, read off the run (BALANCE §4.3): before the boss, what the run lacked (a tower, a typed word; the\n * Pháo's fire once it opens: test pass 27/10); from the lull, enemies that got in when they took more lives than the boss's\n * \`blows\` (counted by the page); it passed the merge with less than half of what had to come off; Dồn lửa words left\n * untyped in the stagger; buildings rooted again and again.\n */` |
| `src/ui/team-bar.ts:1` | `/**\n * The team bar (BUILD_NOW §5.3, BUILD_1A6 §9, TK 23.5, 23.7): Draconis and the Thư Đồng with their number keys and a\n * badge for the building each was sent to, a closed slot's Bastion level, and the "Đang gọi n/N" chip: bright calls\n * against the mode's cap (BUILD_1A6 §5.3).\n */` |
| `src/ui/team-bar.ts:23` | `// Draconis' lantern carries Tối Thượng's charge in a ring (BUILD_1B §13.3), in steps of 5 % so the HTML changes seldom.` |
| `src/ui/tips.ts:1` | `/**\n * The map 1 teaching table (docs/td/BUILD_1B.md §12; R1 its two boss rows, R3 the rest; docs/td/R3_PLAN.md §3.5). At the\n * start of each story day and night Bà Cú Mực says the row's line (two sentences at most, one a line) and its tip chip stays\n * in the teaching frame till the phase ends (ui/hud.ts BossBanner; R3_PLAN §5 A9). What a building opened by day does is a\n * line on its card and on its build-menu row while picked, in the story, until the row that teaches it has come (§12: read\n * when wanted, never shown by itself). Text only, a chunk of its own: the frame and the cards show none of it before it is\n * in. The sandbox skips the table but the boss's two rows (R1: its \`boss\` and \`skipTo\` warn Mộc Tinh).\n */` |
| `src/ui/title.ts:1` | `/**\n * The title screen (SPLIT_PLAN §1.2, D7; TK 22.1, 22.9): Văn Điền at dusk. The scene is painted in code as\n * flat SVG shapes (sky, limestone towers, terraced paddies, a bamboo village on stilts, bamboo clumps); one\n * painted backdrop (/assets/typing-defense/ui/title-dusk.webp, not in Git) replaces it when the file is there.\n * A string of paper lanterns lights up one by one, villagers call across the fields (audio-min.ts), the name\n * "Lời Gọi" is brushed in Baloo 2 by a vermilion seal. Keyboard first: ↑ ↓ pick, Enter or 1–5 choose, Esc\n * goes back to the run left open; while the title is up it takes every key and the world does not step.\n * "Hồ sơ gõ" opens the typing profile (BALANCE.md §2) in the menu's place, as "Cài đặt" opens the settings. Those two\n * cards are chunks of their own (BUILD_1B §20, R2 review fix 2): asked for when picked, an error sound if one cannot load.\n * "Bắt đầu" shows the best stars of map 1 once it was won (td.campaign, BUILD_1B §4.3, R3).\n */` |
| `src/ui/title.ts:28` | `/** The best stars on "Bắt đầu" (none before a win). */` |
| `src/ui/title.ts:192` | `/** Shows the title; "Chơi tiếp" is open only with a run left to go back to; \`best\`: map 1's stars. Lanterns light one by one. */` |
| `src/view/audio-min.ts:1` | `/**\n * Lời Gọi's sound made in code (docs/td/BUILD_NOW.md §5.5, TK 24; SPLIT_PLAN §1.2), no files: bamboo, wood, bronze\n * bells and paper (folk.ts), the list and the prompts for the real files in docs/audio/THEME_SOUND_LIST.md. Buses (TK\n * 24.2): music (ducked under a spoken word), typing (its own light compressor), world, ui, a shared reverb, master and\n * a limiter; the settings set master, music and effects. A call that lights up rings its kind's alert (power a trống\n * cơm pair, build two bamboo taps, harvest a high bell, chop a low wood knock, mine a small clink, quiz a sáo call; at\n * most 3 a second); a right key is a bamboo tick a semitone higher per letter, a wrong or stray one a dull "tóc" 12 dB\n * lower; a finished word a đàn tranh note on the ngũ cung by chain tier (Perfect and Flash add a bell). Word Shots\n * whoosh, blasts thud, the ink folk puff like paper, a leak rings a gong; night and dawn have their own calls. The\n * title adds far villagers calling across the fields. Mộc Tinh (BUILD_1B §13.2): day 5's two low wood beats; the lull's\n * swelling rumble and a low drum every 3 s, faster at the end; the ground breaking and a roar as it rises and staggers;\n * Rễ Trồi's creak through its warning, a wooden "cộp" as it lands; Quật cành's whoosh and thud; the stagger's bell and\n * gong; the retreat's falling chord and leaves; the chest's coins up the scale. A direct word breaking its mechanic: a\n * drum's thump (Ngắt), a bronze stroke and knock (Neo), a stone dome cracking (Phá Khiên).\n */` |
| `src/view/audio-min.ts:160` | `/** Mộc Tinh's sounds (BUILD_1B §13.2); a warning's sound is never capped. */` |
| `src/view/audio-min.ts:174` | `// R3: Rễ hút sinh khí draws in, then a knock and a low bell` |
| `src/view/boss-2d.ts:1` | `/**\n * Mộc Tinh on the 2D map (docs/td/BUILD_1B.md §13.1, R1): a placeholder in ink like everything on the map (a lumpy\n * canopy, amber eyes, root legs), never a model. It reads the world and the combat ring, never changes them. Under\n * the buildings: the warned branch's root vein (day 5 on), the lull's crack crawling to where it rises, Rễ Trồi's\n * striped ring sweeping round under each building it aims at, root spikes and dust. Over the enemies: the body with\n * its anticipation and follow-through (a bob and squash as it steps, the canopy lagging; leaning back before Quật\n * cành and overshooting after; sinking 5 % while it roots; tilting with stars in the stagger), the red arcs of Quật\n * cành and of the blow on the Bastion, Mầm Gỗ (a leafy dot that wobbles, wilting when it dies), the numbers its hits\n * leave; stunned buildings' marks over all of it (1B R1 review). At the Bastion the body fades so the Bastion and the\n * blow's arc under it read. R2's polish: the vein swells with each drum of the lull, leaves fall as it walks, wood chips\n * fly off a rooted building, soil at the sprouts, bark at the stagger, stone at the Bastion's blow, a big hit shakes it.\n * R3: Rễ hút sinh khí's root crawling to the Bastion, its ring, the leaves drawn off. Particles come from the fixed pool\n * of fx-2d.ts; nothing is allocated a frame. With reduced motion nothing shakes; every warning stays.\n */` |
| `src/view/boss-2d.ts:92` | `// R3, Rễ hút sinh khí: the life drawn off the Bastion, embers along the root to its canopy after the pulse (under()).` |
| `src/view/boss-2d.ts:131` | `/** Under the buildings: the root vein of the warned branch, the lull's crack, Rễ Trồi's rings, particles. */` |
| `src/view/boss-2d.ts:161` | `// Rễ Trồi's warning: under each building aimed at, a striped red ring and a sweep going round the warning's time.` |
| `src/view/boss-2d.ts:188` | `// R3, Rễ hút sinh khí: over its warning a root crawls from its feet to the Bastion, ink-edged so it reads on the road;` |
| `src/view/boss-2d.ts:212` | `/** Mộc Tinh's body and its warnings, Mầm Gỗ, the numbers. Over the other enemies. */` |
| `src/view/boss-2d.ts:219` | `// Mầm Gỗ: a leafy dot that wobbles as it walks.` |
| `src/view/boss-2d.ts:229` | `// R2: Quật cành's blow flashes the soldiers it threw white for 60 ms.` |
| `src/view/boss-2d.ts:256` | `/** Quật cành's arc, the blow on the Bastion's arc, the sprouts nudging up: red where it will land, darkening to the hit. */` |
| `src/view/boss-2d.ts:322` | `// Quật cành: it leans back before, overshoots after (150 ms).` |
| `src/view/boss-2d.ts:418` | `/** Stunned buildings' marks, over the boss (review R1): a grey ring and "Tê N s" on a paper chip. */` |
| `src/view/debug-2d.ts:1` | `/**\n * The 1A picture (docs/td/BUILD_NOW.md §5.1, BUILD_1A6 §9): the world seen from above on a Canvas 2D, no media. Grass,\n * lanes, the Silver Stream and its bridges, ore nodes, trees (stumps once felled, a gold rim when marked), buildings as\n * discs of their true radius (a site dashed, its progress an arc), a farm's four plots by stage with a harvest bar, a\n * tower's five power charges, enemies as ink-purple dots sized by tier, soldiers, the NPC workers lettered (a miner by\n * each mine) with "!" at work and "…" when their call waits, shots and short-lived hit marks read from the combat ring;\n * the hero and the helpers with their paths and the selected one's help ring; Word Shots with a jade head trailing\n * their word; a dim call's faded bubble (no word: walk over to help), an arrow at the edge for a call off screen; the\n * player's hand. The camera zooms and pans. It reads the world and never changes it. Painted in the Văn Điền palette\n * (SPLIT_PLAN D7; theme.css): terraced paddies in the field, ripe paddies and stilt-house roofs beyond a bamboo hedge,\n * a silver stream, earth paths, trees as bamboo clumps. The ground that does not change is painted once per camera into\n * a second canvas; at night an indigo wash falls on it and the buildings glow like lanterns (eased over ~1 s, the\n * picture's own clock).\n */` |
| `src/view/debug-2d.ts:32` | `/** The Văn Điền palette (theme.css --vd-*): paddies, bamboo, silver water, earth paths; the meaning colours as TK 23.3. */` |
| `src/view/debug-2d.ts:91` | `/** Mộc Tinh's layers (BUILD_1B §13.1) and R2's Tối Thượng and direct calls (§13.3); main.ts hands them each frame's events. */` |
| `src/view/debug-2d.ts:262` | `/**\n   * Paddies: terraces whose dikes follow slow waves, green in the field (one in five flooded), ripe gold beyond\n   * it out to what the camera can see; the village out there (hipped thatch roofs, a pond, bamboo); the bamboo\n   * hedge (lũy tre) round the field.\n   */` |
| `src/view/debug-2d.ts:402` | `// The rift: a pool of Mực Câm ink with splashes round it.` |
| `src/view/debug-2d.ts:661` | `// test pass 27/10: Ma Trơi read as walkers` |
| `src/view/debug-2d.ts:663` | `// boss-2d.ts draws Mộc Tinh and its sprouts` |
| `src/view/debug-2d.ts:671` | `// Đầu Đàn's aura ring and pennant (both pulse while Neo is open); a Troll's stone dome, dashed; a pinned pack's slate rim.` |
| `src/view/debug-2d.ts:690` | `/** A Đầu Đàn: its aura's faint ring and a red pennant over it; \`pulse\` (0–1) brightens both while Neo is open. */` |
| `src/view/debug-2d.ts:714` | `/** A walker's path ahead, dashed; Thư Đồng as lettered discs, Draconis a winged triangle over its shadow. */` |
| `src/view/debug-2d.ts:797` | `/** Where the action is, CSS px, which the word cards keep off (test pass 27/10): Mộc Tinh with 1.5 m round it, the rain of Tối Thượng, a word shot's target and where one landed in the last 0.7 s. */` |
| `src/view/folk.ts:1` | `/**\n * Văn Điền instruments made in code (TK 24.6, 24.8; SPLIT_PLAN §1.2), no files: a đàn tranh pluck, a sáo\n * trúc note, a trống cơm hit, a bronze bell, a bamboo or wood knock, a paper puff and a far villager's\n * call. Each schedules its nodes at time t into \`to\` and lets them go when done. Placeholders until the\n * real files of docs/audio/THEME_SOUND_LIST.md arrive.\n */` |
| `src/view/folk.ts:9` | `/** Ngũ cung (Hò, Xự, Xang, Xê, Cống ≈ C D F G A): semitones over C. Typing notes and music share it (TK 24.8). */` |
| `src/view/folk.ts:55` | `/** Đàn tranh: a bright string that darkens as it rings; \`slide\` bends up into the note (vuốt). */` |
| `src/view/folk.ts:70` | `/** Sáo trúc: a breathy sine with a late vibrato, \`length\` s held. */` |
| `src/view/folk.ts:90` | `/** Trống cơm: a tuned skin that drops in pitch, with a soft slap. */` |
| `src/view/folk.ts:126` | `/** Mộc Tinh's roar: low noise and a falling saw through a lowpass. */` |
| `src/view/folk.ts:134` | `/** A villager calling across the fields, far off: "Ơ… ơi!" (a voice through two vowel formants, rising, then falling). */` |
| `src/view/fx-2d.ts:1` | `/**\n * The 2D map's particles (docs/td/BUILD_1B.md §16, §20): one fixed pool of 300 (no allocation a frame), at most 40 new\n * a frame. Kinds: dust that swells, wood chips, root spikes that grow then fade, leaves that fall, coins, embers, stones\n * (inked chunks) and rootlets that whip out from where they start (the boss's rise: R2 review, seen at 1280 × 720).\n * Positions are metres; the pen draws in the map's transform. FxView (Tối Thượng, the direct calls' outcomes) lives in\n * fx-pipe.ts, a lazy chunk (ticket 036).\n */` |
| `src/view/fx-pipe.ts:1` | `/**\n * The 2D view's effects chunk (ticket 036, VFX_STANDARD §5.4 V4a), loaded once the page is usable. FxPipe: shots and\n * hits read from the combat ring for FxDraw. FxView (R2, BUILD_1B §13.3): Tối Thượng (Draconis' portrait sliding in\n * from the left, a shadow under each falling feather, the ember pool of its burn) and the direct calls' outcomes (a\n * broken drum bursting into letters, a heal ring spreading 6 m; R3: a pinned pack's ring closing in, a broken dome\n * bursting into stones), from the world and its events; it emits into fx-2d.ts's particle pool.\n */` |
| `src/view/music.ts:1` | `/**\n * The music placeholder made in code (TK 24.8; SPLIT_PLAN §1.2), on its own bus: one tempo (84 BPM), one scale (ngũ\n * cung, shared with the typing notes), two layers that start together and cross-fade over 2 s. Calm (day, the title):\n * đàn tranh figures over a low string, a sáo trúc phrase every four bars. Tension (night): trống cơm, a low tranh\n * ostinato, bamboo clicks on the off-beats, a bronze gong every four bars. At night both play, the calm one 6 dB down.\n * Before Mộc Tinh rises the music steps back; while it fights a steady low drum joins (BUILD_1B §13.2). Eighths are\n * scheduled a quarter second ahead from the frame loop; a layer faded out schedules nothing.\n */` |
| `src/view/music.ts:37` | `/** The sáo phrase being played: [eighth it starts on, scale step, eighths held]. */` |
| `src/view/music.ts:77` | `// Every fourth bar a sáo phrase: a short walk on the scale, held notes at its ends.` |
| `src/view/words/cards.ts:1` | `/**\n * Word cards (docs/td/BUILD_NOW.md §5.2, TK 23.4; BUILD_1A6 §7, §9): a pool of 20 DOM cards over the canvas. A frame\n * changes only transform and opacity; text and classes change when a word's state does. A bright call's word is its\n * bubble over its NPC (or building): the kind's icon and colour, the word, dots for the words the call still asks\n * (●●○), the meaning under it by the rule of BUILD_1B §11.1 (R3: meaningShown); a Từ Ôn is jade with its "Ôn" tag, its\n * meaning always, "Chuộc lại" stamped when redeemed; a quiz shows the meaning and the first letter with blanks ("tốt;\n * hay · g _ _ _"). It grows when locked with the typed part in jade, shakes on a wrong key; typed, it shows its meaning\n * for 1 s (the grade's own name, TK 0.6, stamped over it) or, with none, flies home; it folds when its call dims or\n * closes. A power call's bar is its 6 s. Columns part at once and ease back on the spring, so no frame shows two cards\n * overlapping. A card on its way out has the class is-gone (is-mean while it shows a meaning), so the browser checks\n * can tell it from a live one.\n */` |
| `src/view/words/cards.ts:25` | `/** By call kind (CALL_KIND): power, build, harvest, chop, mine, quiz; R2: Chữ Chiêu, a direct call (Ngắt). */` |
| `src/view/words/cards.ts:29` | `/** Call c's icon and name; a direct call's by its enemy's verb (R3: Ngắt, Neo, Phá Khiên). */` |
| `src/view/words/cards.ts:35` | `/**\n * BUILD_1B §11.1 (R3): the meaning under a word before it is typed: always in Học and Thư giãn and for a child, else\n * while the word was seen at most twice (Cân bằng) or once (Thử thách), this sighting counted; \`seen\` null (Học's chunk\n * not in) shows it. A quiz and a Từ Ôn always show it; 3 errors on a word show it again (the cards).\n */` |
| `src/view/words/cards.ts:83` | `/** Học (R3): a child's profile, and the times a deck word was seen (app/learn.ts; null until it is in). */` |
| `src/view/words/cards.ts:98` | `// A Từ Ôn redeemed (its review event comes just before its wordHit) is stamped "Chuộc lại" in place of its grade (R3).` |
| `src/view/words/cards.ts:137` | `// A "Dồn lửa" call: amber (BUILD_1B §13.1); R2 (§13.3): Chữ Chiêu glows orange, a direct call is a scroll with its window's clock.` |

## Kết quả thô không phải tiếng Việt

| file:dòng | literal |
|---|---|
| `src/app/sandbox.ts:19` | `0,75×` |
| `src/app/sandbox.ts:19` | `1×` |
| `src/app/sandbox.ts:19` | `2×` |
| `src/app/sandbox.ts:24` | `<div class="td-row"><small>Pace</small><span>k ×` |
| `src/ui/build-menu.ts:20` | `×` |
| `src/ui/profile.ts:46` | `×` |
| `src/view/boss-2d.ts:390` | `Burn ×1.25` |
| `src/view/debug-2d.ts:683` | `×` |
