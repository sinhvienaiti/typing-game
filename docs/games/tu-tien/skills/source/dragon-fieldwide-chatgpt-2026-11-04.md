# Song Long toàn sân: ChatGPT, bốn lượt (04/11/2026)

Bản ghi nguyên văn cho [`../DRAGON_SKILL.md`](../DRAGON_SKILL.md) §9. Chế độ Chat, thinking High (không dùng Work), mỗi lượt một cuộc trò chuyện mới, trong một tab riêng của khung trình duyệt trong app.

**Cách lấy bản ghi:** chữ của từng tin nhắn đọc thẳng từ trang (`innerText` của từng khối `data-content-search-unit-key`), gom trong trang rồi gửi về bộ nhận cục bộ `127.0.0.1:8851` bằng form POST, không đi qua ngữ cảnh của Claude. Bong bóng tin nhắn đầu của mỗi lượt bị trang cắt ngắn, nên đề bài đặt ở đó là đúng văn bản Claude đã chèn vào ô soạn và so khớp trước khi gửi. Các khối "ChatGPT said:", "Plain text", bảng và khối mã giữ nguyên như trang hiện. Lượt 4 chưa có câu trả lời nên chỉ có đề bài.

**Kết quả các lần tự duyệt (mẫu §2 của `references/double-review.md`, thêm câu về phạm vi):**

| Lượt | Đề bài | Lần duyệt | Kết thúc |
|---|---|---|---|
| 1 | Thiết kế mở, đủ cả luật sát thương (`brief v1`) | FAIL, FAIL, FAIL | Dừng theo luật 4 lượt: không thể có hai PASS liên tiếp. Claude dừng bản viết lại thứ ba giữa chừng |
| 2 | Chỉ hình học, luật sát thương cố định (`brief v2`) | FAIL, FAIL, FAIL | Dừng theo luật 4 lượt |
| 3 | Sửa một bản đơn giản do Claude viết (`brief v3`) | FAIL, PASS, FAIL | Dừng theo luật 4 lượt; hai lỗi cuối là lỗi thật, Claude đã sửa |
| 4 | Bản hội tụ của lượt 3 cộng ba sửa của Claude (`brief v4`) | — | Anh dừng mọi việc lúc 14:02 khi ChatGPT còn đang nghĩ. Claude chuyển sang đường bước 9 (tự phân tích, giám khảo Claude) |

Không lượt nào đạt hai PASS liên tiếp, nên không có bản bàn giao nào được chuyển sang Gemini. Phần ChatGPT góp và chỗ Claude không đồng ý: §9.10 của tài liệu thiết kế; bảng kiểm ở cuối file này.


## Run 1

Verdicts: FAIL, FAIL, FAIL (dừng)

Page capture: ChatGPT run 1 (brief v1), verbatim page text

Chat URL: https://chatgpt.com/c/6aeab778-2904-83ec-a38d-114fd18a3bdd
Captured: 2026-11-04T05:28:22.915Z
Units: 10



---

#### fallback-turn-0:0:user · USER (Claude)

Role: you are the game-systems analyst for a browser typing game, "Tu Tien Thu Ai" (a xianxia defence game where every attack comes from typed words). Research, analyse and propose ONE concrete, implementable design for ONE skill. Write the prose in Vietnamese; keep every name, id, formula and pseudo-code in English. If you need clarifications, ask all of them in one message before you start; otherwise start directly.

GOAL
Redesign the Sword (Kiem) key-2 skill "Twin Dragons, One Burning Pearl" (id `twin-pearl`, motif 雙龍戲珠) as a FIELD-WIDE, MAP-AGNOSTIC area skill. The owner (04/11/2026) rejected the current grey box, where each dragon runs up one lane to one of the two gates. His words: "having the 2 dragons run up to the gates is not reasonable, because we are building skills to be shared; later maps will not only face 2 gates, so the skill must work on many maps instead of going to 2 gates; a field-wide area skill makes more sense." Keep: two dragons, one burning pearl, the lotus climax. The shape must not depend on the gate count, lane paths, waypoints or flow fields; it covers the field. Your design will be handed to a coding agent that implements it exactly, so be precise.

FACTS: the engine
- Deterministic lockstep sim, fixed 60 Hz tick, integer-only state. Space unit u: 1 m = 60,000 u. Damage in whole HP. Ratios in per-mille (‰). Helpers exist: mulDiv(a,b,c) (integer, round half up), mulDivSym, isqrt, dist2, within(x,z,cx,cz,r), unitPm(dx,dz,out) (unit vector in ‰). No floats or trig in sim state (the current code approximates sin(pi f) by 4f(1-f)). Same seed and same inputs must give the same world hash on every machine.
- Data files use mm, ms and W x 100; a loader converts. 1 W = 90 HP at K0. Today's key 2 ("Nhat Tuyen Xuyen Van", a 14 x 1.2 m line from the player): 2.5 W on the first beast, -15 % each next distinct beast, floor 40 %, posture (The) -20, cooldown 8 s, a typed word of 4-7 letters.
- F0 = the tick the last correct key resolves the Cast; frame Fn = tick F0+n. Design rule D58: the first hit lands within 50 ms (by F2); the charge shows only while typing, never a wait after F0. Fast attack, slow decay: hold the peak, then burn down by erosion. Caster side first (the release shows at the sword first).
- Field (today's only map, "Thanh Thach Ai"): a rectangle x -20..+20 m, z -18..+8 m (40 x 26 m, 1,040 m2). Formation centre ("heart") at (0;0); the player stands on (0;+3) and does not move in the bot. Barrier ring r 9 m round the heart. Ground gates A (-15;-18) and B (+15;-18). Crows (Hoa Nha) enter at the two top corners (+-20;-18) and fly straight to the heart, 4 m high, 2 m/s. Ground beasts walk a flow field to the heart edge (r 2 m) at 1.0-1.6 m/s, height about 0. Two pillars at (+-6.4;-7.68). Live cap 60.
- Map-agnostic data the sim already has: stage.field bounds (minX, maxX, minZ, maxZ in mm); the heart at the origin; the Cast's origin (the player's point); every live beast's x, z, y (height), tier (swarm/small/medium/general/boss), threatW100 (its W), hp, swarm cluster id (rats come in clusters of 7), boss flag, and a gate label "A" | "B" | "sky" (map-specific: it must not drive the shape). The type GateId is hard-wired to A/B/sky, so the sim cannot load a map with another gate count yet.
- Beasts (K0, Balanced): Thach Thu (rat, swarm cluster of 7, 30 HP, 1.6 m/s), Phong Lang (wolf, 90 HP, packs of 3-5), Hoa Nha (crow, flies, 72 HP), Nham Vien (ape, 180 HP, stops 11 m out to throw), Thiet Giap Tru (boar, 270 HP), Lang Dau Dan (general, 630 HP), the Vuong (boss). Peak live counts in waves 5-6: 25-44 (max 52); at one wave-6 peak: gate A 19, gate B 16-18, sky 1-3. Density at peaks: 3.3-4.4 other beasts within 1.5 m of a beast, 5.5-6.7 within 3 m, 7-13 within 6 m. Groups follow each other 2-5 m apart along a lane.
- Rules that stay: canon s7.2 swarm-cluster cap: one area hit deals at most 60 % of a swarm cluster's total HP, and the whole cast counts as ONE area hit. Typed damage ignores armour. The damage-share ledger counts effective damage (at most the HP left).

FACTS: the current grey box (to be replaced; behind the header flag `swordKey2: "twin-pearl"`, off by default; with the flag off the game is byte-identical to before and must stay so)
- Phases: F0 a "hold" strike on an 8 x 8 m box in front of the heart towards -z (towards the gates: map-specific). F1-F2 one touch box (4 x 4.4 m) per lane round that lane's beast nearest the heart. F3-F42 each head runs from the lanes' meeting point (0;-9.25, from the flow field's last bends) up its lane to its gate along a ground S path (amplitude 0.9 m, half-wave 4 m, a sample every 0.5 m); body capsule r 1.4 m, ground band 0-1.5 m; each sample keeps hitting for 54 ticks (0.9 s trail) after the head passes. F30-F50 each tail sweeps its side's sky route (corner to heart edge), capsule r 2.5 m, sky band 2.5-6 m high. F43-F50 roar (no new volume). F51-F71 the lotus at the meeting point: r 9 m, full damage on two long petals (4.4 m wide, 13 m along each head's base path) and in the hold box, 50 % elsewhere. Aftermath visuals until F300.
- Hits: each beast takes at most one hit of each kind (touch, corridor, lotus), at least 20 ticks apart, so at most 3 a cast; the kinds carry 15 / 45 / 40 % of the beast's key-2 damage (2.5 W x its falloff); the lotus deals half outside the petals. Each side (west = gate A and crows at x < 0; east = gate B and crows at x >= 0) has its own falloff ladder (100 %, -15 % per next distinct victim, floor 40 %) and its own budget: 2.5 W per side for ground (split 15/45/40 by part) plus 0.8 W per side for the sky sweep, scaled by the word quality M_q and the seat's bucket, spent first come; a spent part hits nobody more. The boss takes at most 1.5 W a cast (per cast id). Each tick all candidates are gathered in one pass and struck in one order (kind, then distance to the heart, then beast id), so neither side is favoured. The cast resolves only if some damageable beast is alive.
- Measured with bots (17 profiles x 20 seeds, Balanced, pacing on; plus a "peak sweep" that recasts key 2 at each wave's densest tick: 1,665 casts, 92 of them at 35-45 alive):
  - distinct beasts hit per cast at 35-45 alive: 17.2 (p10-p90 14-21), 80 % of casts within 12-20 (unlimited budget: 31.5; today's line: 2.8); 43 % of the live beasts hit;
  - left/right split 50/50 median, 92 % of casts within 40/60-60/40; 92 % of live crows hit; first hit at F0 or F1 (0-17 ms);
  - farthest ground hit at peak 15.4 / 20.2 m from the heart (the gates are 23.3 m away): the budget runs out before the heads reach the gates; only 26 % of the beasts farther than 12 m are hit;
  - damage by part at peak: hold 10 %, touch 3.5 %, body and trail 41 %, sky 12 %, lotus full 26 %, lotus half 7.4 %; overkill 27 %;
  - 5.9 W effective and 7.8 kills per cast at peak; one ultimate today deals 4.1 W;
  - whole match: key 2 = 41-50 % of all damage (canon s7.3 caps each area skill at 20 %); every bot from New (25 WPM) to Fast (70 WPM) wins 95-100 % (Balanced target 75-90 %), the Kid bot 5 %; pressure P 49-60 % (target 15-35 %); median kill distance Q 68-71 % (target 50-70 %); typed share 85 % (gate >= 55 %); key-1 share of typed damage 21-30 % (gate <= 30 %); auto-attack 6.4 % (target 12-18 %).
  - Budget sweep per side: 1.25 W -> 11.9 beasts hit, bots New->Fast win 0-60 %, key-2 share 29-36 %; 1.75 W -> 14.3, 30-100 %, 34-43 %; 2.0 W -> 15.2, 45-100 %, 37-45 %; 2.5 W -> 17.2, 95-100 %, 41-50 %; unlimited -> 31.5, 100 %, 57-64 %. No budget brings key 2 to 20 % or less while the bots still win.
  - Without the dragon (today's line) bots win 0-40 % (most 0 %): every skill's reach is too short (key 1 12 m, auto-attack 10 m; beasts walk 65 % of their path out of key-1 reach), and the game breaks when the second gate opens (wave 2). Raising every range x1.5 in memory lifted 45 WPM 97 % from 0 % to 95-100 % wins.

CONSTRAINTS
- Map-agnostic: the only inputs are (a) the field bounds or playable rectangle, (b) the formation centre and the caster point, (c) live foe positions, heights, weights, density and clusters, crows included. No gate ids, lanes, waypoints, flow-field routes or sky-entry points. Give a fallback for an empty field (the cast still resolves only when a damageable beast is alive, but the lab may cast on an empty field, so the path must stay well defined).
- Deterministic and integer-only; fixed tick; no float trig or float sqrt in the sim (integer isqrt is fine; a small integer lookup table is fine if it lives in content data). Bounded cost: at most 60 live beasts and at most 2 casts alive at once; aim for 50 microseconds or less per tick per cast in JS.
- Must keep: at most 3 hits per beast a cast, one of each kind, re-hit after at least 20 ticks; the boss cap per cast id; one swarm-cluster cap per cast (the whole cast is one area hit); crows are hit only by sky-band volumes and ground beasts only by ground-band volumes; the per-cast budget mechanism (amounts may change); `rulesHash` covers the trial table only when the flag is on; flag off stays byte-identical.
- Five phases (charge while typing, release at the caster, travel, impact, aftermath) with frame numbers; D58's instant first hit; caster side first; fast attack, slow decay.
- Already decided by the owner (do not reopen): two dragons, one burning pearl, the lotus climax; Sword key 2 with the Fire element look; field-wide; map-agnostic; an anime and mythic look. The art is made later with art tools (Firefly Video and Image, Blender); code only places and animates it.

DELIVER (numbered, with numbers everywhere)
1. Inputs: exactly which map-agnostic values, read when (once at F0, or per tick), and the empty-field fallback.
2. The two dragons' paths. Weigh at least (a) mirrored spirals or a figure-eight sized from the field bounds, (b) paths through the k densest clusters, (c) a sweep that splits the field into two halves by foe mass. Pick one (or a hybrid) and say why. Give the exact deterministic integer algorithm as pseudo-code with every parameter (mm, ticks, per-mille): the clustering method; how foes are split between the two dragons (this replaces west/east by gate); path construction and smoothing; the sampling step; length normalisation to ticks; the tick-to-sample mapping; ground and sky handling for crows; and what is stored in the cast state. Show that it works on today's two-gate map, a one-gate map, a three-gate map, an open arena with foes from every side, foes behind the caster, a single lone foe, and an empty field.
3. The pearl's point and the lotus: the formula (for example a density-weighted centre) with its clamps; the lotus size and its full and half regions defined without lanes.
4. The five phases with frame timing (F numbers). Replace the F0 hold box "towards the gates" and the per-lane touch boxes with map-agnostic equivalents; keep a hit within F0-F2.
5. Hit volumes and caps: radii, bands, trail ticks, kinds and shares, falloff, the budget per dragon and per part, the boss cap, the crows' sky band, the one swarm-cluster cap. The damage-share target: canon caps each area skill at 20 % of match damage, but bots win only 0-40 % without this skill. Say what share key 2 should have, at which budget, what else in the game must change (which systems), and mark explicitly which choices are the owner's decision.
6. Measurable targets and the bot plan: 12-20 distinct beasts per cast at 35-45 alive (p10-p90); a map-agnostic coverage measure (define it exactly, for example the share of live foes inside any hit volume before the budget, or the area covered) with a target; side balance redefined; first hit within 50 ms; crows hit; the BALANCE.md metrics (win, S, P, I, O, N, Q, typed share, key-1 share, key-2 share, auto-attack share). Synthetic layouts for unit tests while the sim can load only this map: exactly how to place foes for the one-gate, three-gate, arena, behind-the-caster and lone-foe cases (coordinates, counts, species), a rotation or mirror invariance check if useful, and determinism checks.
7. The VFX implication in one paragraph (no art work now): the dragons stay body plus trail along the computed paths; what the view needs from the sim.
8. Risks and how to check each; what you are not sure about.
Keep the whole answer under about 2,500 words; precise beats long. Cite a source for any external factual claim (most of this is engineering from the facts above, which needs no citation).

(The page clipped this bubble to 10246 characters; the text above is the exact brief inserted into the composer and checked equal before sending.)

---

#### fallback-turn-0:2:assistant · CHATGPT

ChatGPT said:
Thiết kế đề xuất: twin-pearl-v2

Skill: Twin Dragons, One Burning Pearl — 雙龍戲珠
Slot: Sword / Key 2
Element: Fire
Architecture: Threat-Adaptive Twin Sweep + Field-Wide Lotus

Quyết định: Hai rồng xuất phát từ người chơi, tách sang hai hướng, quét qua các cụm địch trên toàn chiến trường rồi hội tụ tại một viên hỏa châu. Viên châu nở thành hoa sen tám cánh, tạo đợt sát thương cuối bao trùm toàn bộ sân.

Đường bay không phụ thuộc cổng, lane, waypoint hay flow field. Ngân sách sát thương được tách khỏi diện tích hiệu ứng để bảo đảm quy mô hình ảnh lớn nhưng không phá cân bằng.

1. Input và thời điểm đọc

Input

	

Thời điểm

	

Công dụng




fieldBounds, heart, caster

	

F0

	

Hình học chiến trường




beast.id, x, z, y

	

F0

	

Chia nhóm, xây đường




tier, threatW100, clusterId, bossFlag

	

F0

	

Trọng số, giới hạn




hp, x, z, y, alive

	

Mỗi tick

	

Kiểm tra va chạm thực tế




M_q, seatBucketPm

	

F0

	

Ngân sách sát thương

Không đọc gateId, đường di chuyển hoặc vị trí sinh quái.

Toàn bộ phép tính hình học dùng số nguyên mm; tọa độ sim được lượng tử hóa bằng mulDivSym(u,1,60). Ngược lại, nhân tọa độ mm với 60 trước khi ghi vào sim.

Sân trống: pearl = clamp(heart, bounds). Hai rồng bay qua hai điểm lệch đối xứng cách trung điểm caster–pearl một đoạn 150‰ × min(fieldWidth,fieldHeight), rồi hội tụ. Lab vẫn dựng được đường; gameplay không giải quyết Cast khi không có địch có thể nhận sát thương.

Địch sinh sau F0 không được chọn làm mục tiêu trong Cast hiện tại. Vị trí và HP của địch đã được chọn vẫn cập nhật mỗi tick.

2. Thuật toán đường bay hai rồng
2.1. So sánh ba phương án

Phương án

	

Ưu điểm

	

Nhược điểm




Mirrored spirals / figure-eight

	

Dễ đọc, phủ đều địa hình

	

Lãng phí đường bay ở vùng trống




Top-k density clusters

	

Tập trung địch đông, linh hoạt

	

Có thể bỏ sót địch đơn lẻ




Threat-mass split sweep

	

Cân bằng hai rồng, không phụ thuộc cổng

	

Cần giải thuật phân vùng ổn định

Chọn hybrid: chia địch theo trọng số nguy hiểm, gom cụm, sau đó cho mỗi rồng đi qua tất cả cụm được giao. Sáu cụm quan trọng nhất được ưu tiên khi chọn hành trình, nhưng không bỏ những cụm còn lại.

2.2. Chia địch

Với mỗi địch:

Plain text
weight = clamp(isqrt(max(1, threatW100) * 100), 50, 300)

Tạo sáu trục phân vùng:

Plain text
(1000,0), (0,1000), (707,707), (707,-707)
farthestPairDirection
perpendicular(farthestPairDirection)

Cặp xa nhất được chọn bằng dist2, hòa điểm theo ID. Nếu không có hướng hợp lệ, dùng (1000,0).

Với mỗi trục, sắp địch theo tích vô hướng tọa độ, hòa theo ID. Thử mọi vị trí chia thành hai tập không rỗng, giới hạn mỗi tập 35–65% số lượng khi N>=4.

Chọn kết quả có:

Plain text
score = SSE_A + SSE_B + 2000000 * abs(massA - massB)

Trong đó SSE là tổng weight × dist2 tới trọng tâm có trọng số của tập. Hòa điểm theo thứ tự trục, rồi vị trí chia.

Hai tập được đặt tên dragon0 và dragon1, không phải west/east. Với một địch, giao nó cho dragon0; rồng còn lại vẫn bay nhưng không sở hữu sát thương.

2.3. Gom cụm và xây đường

Trong từng tập, dùng union-find:

Nối hai địch có khoảng cách mặt đất <=3000 mm.

Chỉ nối nếu cùng nhóm độ cao ground hoặc sky.

Trọng tâm cụm dùng weight.

Khóa hòa cuối cùng luôn là beast.id.

Tạo đường theo thuật toán:

Plain text

for dragon in [0, 1]:
    nodes = [caster, flankAnchor(dragon)]

    while unvisitedClusters:
        choose cluster minimizing:
            mulDiv(distanceToNearestMemberMm, 1000,
                   1000 + min(clusterMass, 3000))
        tie: smallest clusterMinId

        append weightedClusterCentroid

        while unvisitedMembersInCluster:
            append nearestMemberToLastNode
            tie: smallest beastId

    append pearl
    path = fixedPointCatmullRom(nodes)
    samples = tessellate(path, maxChordMm=500)
    length = cumulativeIntegerLength(samples)


flankAnchor nằm hai phía của vector caster→pearl, lệch 150‰ × min(fieldWidth,fieldHeight) và được clamp vào sân. Nếu vector bằng không, dùng hướng (1000,0).

Spline Catmull–Rom chuẩn được tính bằng hệ số nguyên tại tPm=0..1000; phép chia dùng mulDivSym. Mỗi đoạn bắt đầu với ceil(chordLength/250) khoảng tham số, chia đôi tiếp nếu chord kết quả vượt 500 mm. Clamp từng mẫu vào field. Các knot gốc được giữ nguyên để đường không bỏ qua vị trí mục tiêu.

Tính độ dài bằng isqrt, không dùng Math.sqrt.

2.4. Ánh xạ thời gian và va chạm
Plain text
travelTicks = 40
travelFrame = 3..42

k = frame - 2
headDistance = mulDiv(totalLength, k, 40)

Nội suy khoảng cách trên mảng cumulative length; kiểm tra tất cả đoạn bị đầu rồng quét qua kể từ tick trước, không chỉ vị trí cuối tick.

Hai đầu rồng hoạt động trên cùng mặt phẳng x,z. Mỗi đầu có hai collider theo độ cao:

ground: sát thương địch có y=0..1600 mm

sky: sát thương địch có y=2500..6000 mm

Cả hai dùng cùng đường chiếu xuống mặt đất. Dải lửa trên cao là phần thị giác của rồng, không phải rồng thứ ba.

Mỗi Cast lưu castId, snapshot mục tiêu, owner, cluster-cap ledger, hit masks, last-hit ticks, hai mảng sample, cumulative length, pearl, radius, budgets và các mục tiêu đã chọn.

2.5. Kiểm tra tính độc lập bản đồ

Hai cổng: các cụm trái/phải được phân phối theo trọng số, không có điểm đích tại cổng.

Một cổng: chia các địch trong cùng một đám cho hai rồng.

Ba cổng: hai rồng chia ba nhóm theo khối lượng, có thể một rồng xử lý hai nhóm.

Open arena: đường ghé qua những cụm trên cả bốn phía.

Behind caster: có waypoint ở z>caster.z; không ép bay về -z.

Lone foe: hai rồng xuất phát đối xứng, một rồng sở hữu mục tiêu.

Empty field: dùng hình học fallback mục 1.

3. Viên châu và hoa sen

Viên châu nằm tại trọng tâm có trọng số của toàn bộ địch F0:

Plain text
pearlX = roundSym(sum(weight*x) / sum(weight))
pearlZ = roundSym(sum(weight*z) / sum(weight))

Clamp vào 80% miền trong của mỗi chiều sân (lề 10%). Nếu không có địch, dùng heart.

Để hoa sen thực sự bao phủ toàn sân:

Plain text
lotusRadius =
    max(isqrt(dist2(pearl, corner)) for each fieldCorner)
    + 1000 mm

Vùng sát thương đầy đủ:

Đĩa trung tâm r <= 350‰ × lotusRadius.

Tám cánh radial theo tám hướng cố định (±1000,0), (0,±1000), (±707,±707).

Mỗi cánh là capsule từ tâm tới 850‰ × lotusRadius, bán kính 100‰ × lotusRadius.

Mọi vị trí còn lại trong bán kính hoa sen nhận 500‰ sát thương phần lotus.

Như vậy toàn bộ sân nằm trong vùng ảnh hưởng, nhưng chỉ trung tâm và tám cánh nhận toàn phần. Các hướng cố định không cần lượng giác.

4. Năm giai đoạn

Phase

	

Frame

	

Hành động




Charge

	

Trong lúc gõ

	

Hai luồng hỏa khí xuất hiện quanh kiếm




Release

	

F0–F2

	

F0 xung quanh caster; F1 đòn chạm tức thời vào mục tiêu gần nhất mỗi rồng




Travel

	

F3–F42

	

Hai rồng quét toàn sân, để lại vệt cháy




Impact

	

F43–F78

	

F43–F66 giữ đỉnh và gầm; F67 hoa sen gây sát thương; F68–F78 giữ hình




Aftermath

	

F79–F300

	

Lửa và vệt kiếm bị erosion, không thêm damage

F0 dùng vòng bán kính 3000 mm quanh caster thay hold box hướng cổng.

F1 tạo hai touch collider ở vị trí hiện tại của mục tiêu gần caster nhất chưa nhận touch, bán kính 1800 mm ground hoặc 2500 mm sky. Nếu mục tiêu biến mất, F2 thử mục tiêu hợp lệ tiếp theo.

Hiệu ứng bắt đầu tại kiếm ở F0; tia hỏa khí từ kiếm đến điểm chạm là visual, không có collider dọc tia.

D58: khi còn mục tiêu có thể nhận damage và ngân sách dương, hit đầu xảy ra chậm nhất F2.

5. Hit volumes và ngân sách
5.1. Ba loại hit

Kind

	

Volume

	

Damage share




touch

	

F0 radial + F1/F2 endpoints

	

15%




corridor

	

Ground r 2200 mm, sky r 3000 mm

	

55%




lotus

	

Field-wide tại F67

	

30%

corridor có trail gây sát thương trong bốn tick sau đầu rồng, kết thúc F46. Trail hình ảnh tồn tại thêm 54 tick rồi erosion.

Mỗi địch nhận tối đa một hit cho từng kind trên toàn Cast; hai hit cách nhau ít nhất 20 tick.

5.2. Ngân sách thử nghiệm

Đề xuất thay ngân sách cũ bằng 1.80 W mỗi Cast tại K0, chia 0.90 W = 81 HP mỗi rồng.

Damage danh nghĩa mỗi nạn nhân trước falloff:

Plain text
baseVictimDamage = 0.18 W = 16 HP
falloffPm = max(400, 1000 - 150 * distinctRank)

distinctRank tính riêng từng rồng theo thứ tự nhận damage thành công. Damage được nhân M_q và seatBucketPm bằng mulDiv theo thứ tự cố định, không dùng số thực.

Chia ngân sách mỗi rồng theo số mục tiêu sky đã chọn (s):

Plain text
T = mulDiv(mulDiv(81, M_q, 1000), seatBucketPm, 1000)
S = s == 0 ? 0 :
    min(T, mulDiv(2*s + 3, M_q, 1000))
G = T - S

groundTouch = mulDiv(G, 150, 1000)
groundCorridor = mulDiv(G, 550, 1000)
groundLotus = G - groundTouch - groundCorridor

skyTouch = min(1, S)
skyCorridor = min(s, S - skyTouch)
skyLotus = S - skyTouch - skyCorridor

Damage từng nạn nhân cũng được chia 15/55/30, phần lotus nhận phần dư để tổng không vượt damage danh nghĩa. Với damage dương, ưu tiên dành ít nhất 1 HP cho lotus.

Chọn số nạn nhân có thể nhận damage tại F0:

Plain text
victimQuota = min(N, clamp(mulDiv(N, 400, 1000), 12, 20))

Chia quota theo số lượng của hai tập, làm tròn bằng phần dư lớn nhất. Ưu tiên chọn tất cả crows nếu vừa quota, sau đó mục tiêu gần caster, rồi farthest-first theo minDist2 × weight, hòa ID.

Đường vẫn đi qua những địch không được chọn, nhưng chỉ mục tiêu trong quota được damage. Tại F67, xử lý trước 1 HP cho mọi mục tiêu đã chọn còn sống nhưng chưa từng trúng đòn, sau đó mới phân bổ damage lotus bổ sung. Cơ chế này tránh việc budget bị chiếm hết trước khi hoa sen nở.

Mọi ứng viên được xử lý cùng tick theo (kind, dist2ToHeart, beastId, dragonId).

Giới hạn:

bossCap = 1.5 W mỗi castId, dùng chung hai rồng.

swarmClusterCap = 600‰ × originalClusterTotalHP, dùng chung cả ba kind và cả hai rồng, lấy từ cơ chế s7.2 hiện có.

Trừ ngân sách và ghi ledger bằng damage thực tế, không tính overkill.

Typed damage xuyên armour.

posture = -20 một lần trên mỗi nạn nhân, không lặp theo ba kind.

5.3. Cân bằng toàn game

Mục tiêu đề xuất: key2Share = 15–20%, với 1.80 W là budget thử đầu tiên, không phải kết quả đã đo.

Không thể chỉ nerf key-2 rồi kết thúc. Cần đồng thời thử:

Tăng reach key-1 từ 12 lên 18 m và auto-attack từ 10 lên 15 m.

Kiểm tra reach của các skill còn lại, nhất là khi wave 2 mở thêm hướng tấn công.

Điều chỉnh auto-attack DPS để đạt share 12–18%.

Tuning pacing, spawn pressure và sức mạnh địch sau khi sửa reach; tránh để win rate lại đạt 95–100%.

Cần chủ game phê duyệt: budget 1.80 W, per-victim damage 0.18 W, victim quota, thay đổi reach và pacing. Hai rồng, hỏa châu, hoa sen, slot key-2 và field-wide là quyết định đã khóa.

6. Acceptance metrics và bot plan

Ở 35–45 địch sống, target:

| Metric | Acceptance |
|---|---|
| Distinct hits, p10–p90 | 12–20 |
| travelCoverage | >=85% |
| lotusCoverage | 100% trong field |
| Threat-mass balance | 40/60–60/40 trong >=90% peak casts |
| First damage | F0–F2 |
| Crow hit rate | >=90% với 1–3 crows |
| Processing P95 |

Báo cáo đầy đủ các metric BALANCE.md:

Win: 75–90% cho nhóm bot mục tiêu.

P: 15–35%; Q: 50–70%.

Typed share: >=55%; key-1 share typed:

---

#### fallback-turn-1:0:user · USER (Claude)

Your answer was cut off in section 6 (it ends at "key-1 share typed:"), and sections 7 and 8 are missing. Continue exactly from where it stopped: finish section 6, then write sections 7 and 8. Do not repeat sections 1-5.

---

#### fallback-turn-1:2:assistant · CHATGPT

ChatGPT said:

- Key-1 share of typed damage: =85%` là giả thuyết.** Đường qua vị trí F0 có thể bỏ lỡ quái di chuyển nhanh. Coverage hình học của lotus bằng 100% không chứng minh corridor hoạt động tốt.

4. Hình học F0 có thể vượt mục tiêu hiệu năng. Đặc biệt với 60 địch, clustering và spline tessellation phải có giới hạn số node, số lần chia đoạn và số sample. Benchmark cần tách F0 khỏi các tick thông thường.

5. Các ngưỡng S, I, O, N chưa được cung cấp. Coding agent phải đọc BALANCE.md, giữ nguyên công thức và acceptance gates hiện hành, không tự suy diễn.

6. Việc chọn riêng dragon0/dragon1 không được trở thành logic gameplay phụ thuộc trái/phải. Dragon ownership là kết quả phân nhóm theo foe mass; mọi quy tắc damage, cap và scheduling phải đối xứng.

8.2. Điều kiện nghiệm thu

Chỉ bật twin-pearl-v2 làm mặc định khi đồng thời đạt:

Độc lập hoàn toàn với gate count, lane và flow field.

First damage không muộn hơn F2 trong điều kiện có mục tiêu hợp lệ và đủ damage budget.

Không vi phạm hit-cap, boss-cap, swarm-cap và deterministic replay.

Đạt coverage, crow hit rate và distinct-victim targets trong peak sweep.

Key-2 share <=20%, win rate Balanced 75–90%, pressure 15–35%, cùng các gate hiện hành của BALANCE.md.

Flag off vẫn byte-identical với bản trước.

Kết luận: twin-pearl-v2 phải được đánh giá như một skill có hình ảnh phủ toàn sân nhưng sát thương có ngân sách, không phải một đòn gây full damage lên toàn bộ quái. Điều kiện quan trọng nhất trước khi phát hành là chứng minh đồng thời ba yếu tố: field-wide coverage, deterministic simulation và overall balance.

---

#### fallback-turn-2:0:user · USER (Claude)

Review your latest full answer above (the first answer plus its continuation) against the brief, the facts and the constraints. It FAILS only for a real defect: a wrong fact or source, a step that would not work, a missing step the goal needs, a contradiction with the constraints or the owner's decisions, or a part too vague for a worker to execute. Wording, style and optional extra ideas are not defects.
If it is correct and accurate, answer with exactly one line: VERDICT: PASS (you may add one line "Optional:" with ideas that do not change the verdict)
Otherwise answer: VERDICT: FAIL, then list each defect, then give the corrected FULL analysis and solution (not a diff). If the full version does not fit in one message, stop at a section boundary, end with the line PART 1 OF N, and I will ask for the next part.

---

#### fallback-turn-2:2:assistant · CHATGPT

ChatGPT said:
VERDICT: FAIL

Bản thiết kế trước đúng hướng field-wide, map-agnostic, giữ hai rồng và hoa sen, nhưng chưa đủ an toàn để giao coding agent triển khai trực tiếp.

Các lỗi thực sự

touch và corridor xung đột với quy tắc 20 ticks. Nếu mục tiêu nhận touch tại F1 và rồng đi qua tại F3, corridor không được gây damage. Trail chỉ tồn tại bốn tick sau khi rồng đi qua nên mục tiêu có thể mất hoàn toàn phần damage này. Chưa có cơ chế bảo đảm re-hit hợp lệ.

Thuật toán chia nhóm chưa xác định đúng. Công thức SSE_A + SSE_B + 2000000 × massDifference cộng các đại lượng khác đơn vị; không xác định được ý nghĩa thực tế của hệ số. Phép chọn trục, tie-breaking và cách tính centroid chưa đủ chính xác.

Path construction chưa triển khai được nguyên trạng. fixedPointCatmullRom, tessellate và flankAnchor chưa có công thức, giới hạn bộ nhớ, quy tắc tránh spline bỏ qua mục tiêu hoặc cách xử lý path quá dài. Không có giới hạn số sample thực sự.

Kiểm soát budget và quota không bảo đảm mục tiêu đề ra. Việc chọn 12–20 nạn nhân không bảo đảm họ nhận ít nhất 1 HP. Công thức cấp budget sky tùy ý, không xử lý đầy đủ làm tròn, budget thấp và phân bổ theo từng damage kind. Budget có thể bị tiêu trước F67.

D58 chưa được bảo đảm. F1 chọn mục tiêu gần nhất nhưng chưa bảo đảm mục tiêu đó có touchDamage > 0, còn sống và thuộc đúng height band. Vì vậy Cast có thể không gây damage trước F2 dù có địch hợp lệ.

Lotus sky collision chưa được định nghĩa đầy đủ. Hình học mặt đất có nhưng chưa xác định rõ collider sky tại F67, trong khi crows tuyệt đối không được nhận ground damage.

Chi phí mỗi tick chưa được khống chế. Kiểm tra 60 beasts với hàng trăm segment của hai rồng có thể vượt xa mục tiêu 50 µs/tick/cast nếu không có spatial index và giới hạn sample.

Swarm cap thiếu quy tắc làm tròn chính xác. Cap 60% phải dùng phép làm tròn xuống để không bao giờ vượt giới hạn khi HP tổng không chia hết.

Metamorphic tests chưa đủ chính xác. Một số tie-break theo ID, trục cố định và phép làm tròn có thể khiến đường bay không tương đương tuyệt đối khi mirror/rotation. Không nên dùng so sánh nguyên world hash giữa hai bản đồ có tọa độ khác nhau.

Có citation không được xác minh trong câu nói về Number.MAX_SAFE_INTEGER. Đây là dẫn nguồn không hợp lệ trong bản trước; yêu cầu giới hạn số nguyên an toàn có thể được kiểm tra trực tiếp bằng invariant và test, không cần citation đó.

Dưới đây là bản thiết kế đầy đủ thay thế, với toàn bộ thông số trial cố định. Những thông số chưa được kiểm chứng bằng bot được đánh dấu là đề xuất, không trình bày như kết quả thực nghiệm.

Corrected design: twin-pearl-v2

Skill: Twin Dragons, One Burning Pearl (雙龍戲珠)
ID: twin-pearl
Slot: Sword / Key 2
Element: Fire
Architecture: Threat-Balanced Coverage Routing + Field-Wide Lotus

Hai rồng xuất phát tại kiếm của caster, chia toàn bộ địch theo threat mass, đi qua các điểm đại diện đủ để phủ những vị trí địch đã chụp ở F0, rồi hội tụ vào một hỏa châu. Hoa sen tám cánh tại hỏa châu có collider phủ toàn sân, nhưng sát thương bị giới hạn bởi budget.

Hình dạng không sử dụng gate, lane, waypoint, flow field hoặc sky-entry point.

1. Input, snapshot và fallback

Input

	

Đọc

	

Mục đích




fieldBounds, heart, caster

	

F0

	

Phạm vi và gốc hình học




id, x, z, y, hp, threatW100, clusterId, bossFlag, tier

	

F0

	

Chia địch, routing, target allocation




M_q, seatBucketPm

	

F0

	

Damage budget




id, x, z, y, hp, alive

	

Mỗi tick

	

Actual hit validation

Dùng mm cho tất cả tọa độ của thuật toán. Chuyển từ sim u sang mm bằng mulDivSym(valueU,1,60); ghi ngược bằng valueMm*60.

groundBand = [0,1500] mm, skyBand = [2500,6000] mm, bao gồm biên. Phân loại theo y ở F0; tại lúc hit phải còn trong đúng band đã phân loại. Không dùng gateId hoặc tên species để xác định sky/ground. Địch ngoài cả hai band không hợp lệ cho damage.

Cast gameplay chỉ resolve khi tại F0 có ít nhất một beast sống, hp>0, nằm trong một band hợp lệ. Địch mới sinh sau F0 không tham gia Cast đang chạy.

Nếu lab yêu cầu dựng Cast khi sân trống:

Plain text
pearl = clamp(heart, fieldBounds)
dragon0 = [caster, flankAnchor(0), pearl]
dragon1 = [caster, flankAnchor(1), pearl]
damageEnabled = false

Nếu chỉ có một beast, nó thuộc dragon0; dragon1 dùng path fallback. Cả hai vẫn được render.

2. Thuật toán hai đường rồng
2.1. Chọn chiến lược

Phương án

	

Quyết định

	

Lý do




Mirrored spiral / figure-eight theo field

	

Reject làm routing chính

	

Phủ sân đều nhưng tốn quãng đường vùng trống




Top-k dense clusters

	

Adapt

	

Tốt cho ưu tiên đám đông nhưng không được bỏ địch lẻ




Threat-mass split

	

Adopt

	

Chia hai rồng dựa trên địch, không dựa trên cổng

Hybrid được chọn: threat-mass split → cluster coverage points → nearest-neighbour routing → integer spline. Không giới hạn ở top-k; các cluster nhỏ vẫn được thăm.

2.2. Chia hai rồng

Tại F0, sắp beasts theo id, rồi tính:

Plain text
weight = clamp(
    isqrt(max(1, threatW100) * 100),
    50, 300
)

Dùng sáu candidate axes:

Plain text
(1000,0), (0,1000), (707,707), (707,-707),
farthestPairDirection,
perpendicular(farthestPairDirection)

farthestPairDirection dùng unitPm từ cặp beast xa nhất theo dist2; hòa theo cặp ID tăng dần. Nếu mọi vị trí trùng nhau, dùng (1000,0).

Với mỗi axis:

Sort beasts theo dot(position, axis), hòa theo id.

Thử mọi cut k=1..N-1.

Tính mass và weighted centroid của hai tập.

Chấm điểm bằng những đại lượng đã chuẩn hóa.

Plain text
balancePm = mulDiv(abs(massA-massB),1000,totalMass)

compactPm = mulDiv(
    SSE(A)+SSE(B),
    1000,
    max(1,totalMass*fieldDiagonalSquared)
)

score = 7*balancePm + 3*compactPm

Trong đó:

Plain text
centroidX = mulDivSym(sum(weight*x),1,sum(weight))
centroidZ = mulDivSym(sum(weight*z),1,sum(weight))

SSE(group) =
    sum(weight * dist2(position, centroid))

Chọn minimum (score, axisIndex, cutIndex) theo thứ tự từ điển. Tập đứng trước cut là dragon0, tập còn lại dragon1.

Mọi intermediate phải là safe integer; nếu không, builder phải báo geometryOverflow, không silently round.

2.3. Clustering và coverage representatives

Trong từng dragon, dùng union-find trên những beasts cùng height band, nối cặp cách nhau <=3000 mm.

Mỗi cluster tạo representatives theo quy tắc:

Plain text
while uncoveredMembers exist:
    for each candidate v in cluster:
        coverMass(v) = sum(
            weight[j]
            for uncovered j
            if dist2(v,j) <= 1000*1000
        )

    choose v with maximum (coverMass, -beastId)
    append position(v)
    mark all members within 1000 mm covered

Như vậy mỗi beast F0 nằm cách ít nhất một representative cùng band không quá 1000 mm, không phụ thuộc việc cluster có kéo dài hay không.

2.4. Routing
Plain text
minDim = min(fieldWidth,fieldHeight)
forwardOffset = mulDiv(minDim,100,1000)
sideOffset = mulDiv(minDim,150,1000)

direction = unitPm(pearl-caster)
if direction == (0,0): direction = (1000,0)

normal = (-direction.z,direction.x)
sign = dragonId == 0 ? -1 : 1

flankAnchor = clamp(
    caster
    + mulDivSym(direction,forwardOffset,1000)
    + mulDivSym(normal,sign*sideOffset,1000),
    fieldBounds
)

Các phép vector được tính trên từng tọa độ.

Sau đó:

Plain text
path = [caster, flankAnchor]

while unvisitedClusters exist:
    choose cluster minimizing:
        mulDiv(distanceMm(lastNode,nearestRepresentative),
               1000,1000+min(clusterMass,3000))
    tie: smallest clusterMinId

    while unvisitedRepresentatives in chosenCluster:
        append nearestRepresentative(lastNode)
        tie: smallest beastId

append pearl

Không được bỏ waypoint chỉ vì nó không thuộc top-k cluster.

2.5. Smoothing và sampling

Dùng interpolating Catmull–Rom với arithmetic nguyên.

Cho bốn control points p0,p1,p2,p3, tính từng tọa độ:

Plain text
A = 2*p1
B = -p0+p2
C = 2*p0-5*p1+4*p2-p3
D = -p0+3*p1-3*p2+p3

q = C + mulDivSym(D,tPm,1000)
q = B + mulDivSym(q,tPm,1000)
q = A + mulDivSym(q,tPm,1000)

position = mulDivSym(q,1,2)

p0=p1 tại điểm đầu; p3=p2 tại điểm cuối.

Mỗi span dùng:

Plain text
subdivisions =
    clamp(ceilDiv(distanceMm(p1,p2),500),8,128)
tPm = mulDiv(j,1000,subdivisions)

Giữ điểm đầu/cuối, bỏ duplicate giữa các span, clamp các sample vào field.

Tạo dense polyline rồi resample theo cumulative length:

Plain text
sampleStepMm = max(500,ceilDiv(totalLengthMm,768))
K = max(1,ceilDiv(totalLengthMm,sampleStepMm))

sampleDistance[i] = mulDiv(totalLengthMm,i,K)
for i = 0..K

Nội suy integer trên dense polyline. Mỗi rồng tối đa 769 output points. Route luôn đi qua representative trước resampling; sai lệch do resampling phải được đo và assert <=500 mm.

2.6. Tick mapping và storage
Plain text
headDistance(F2) = 0
headDistance(Fn) =
    mulDiv(pathLengthMm,n-2,40)   // n = 3..42
headDistance(F42) = pathLengthMm

Mỗi tick kích hoạt toàn bộ phần đường từ head position trước đến hiện tại. Collider không được bỏ đoạn đường chỉ vì đầu rồng đi nhanh hơn một sample/tick.

Để đạt mục tiêu hiệu năng, xây spatial index ở F0:

tileSize = 4000 mm.

Mỗi segment được đăng ký vào các tile giao với AABB mở rộng 3200 mm.

Mỗi tick, chỉ kiểm tra segment trong tile chứa beast.

Segment được kích hoạt theo head progress, duy trì collider đến tối đa F46.

Các segment kiểm tra theo segment index tăng dần.

Cast state chứa castId, startTick, owners, band, representatives, paths, cumulativeLengths, headProgress, spatialIndex, pearl, lotusRadius, selectedVictims, damageEnvelopes, partBudgets, hitMasks, lastHitTick, bossLedger và clusterLedger.

Tối đa hai Cast có thể tồn tại đồng thời; toàn bộ ledger thuộc Cast riêng.

2.7. Tương thích bản đồ

Two-gate: các nhóm địch thường tự phân thành hai hướng nhưng đường rồng không chạm gate theo quy tắc.

One-gate: hai rồng có thể chia cùng một đoàn quái.

Three-gate: một rồng có thể quét nhiều nhóm.

Open arena: các representative được thăm quanh sân.

Behind caster: các điểm sau caster được giữ nguyên, không ép về -z.

Single foe: một rồng nhắm foe, rồng còn lại dựng hình đối ứng.

Empty field: cả hai dùng fallback.

Điểm kết thúc của cả hai rồng luôn là pearl, không phải gate.

3. Hỏa châu và hoa sen
3.1. Pearl position

Dùng toàn bộ beasts hợp lệ tại F0, không chỉ những mục tiêu được cấp damage.

Plain text
pearlX = mulDivSym(sum(weight*x),1,sum(weight))
pearlZ = mulDivSym(sum(weight*z),1,sum(weight))

Clamp trong hình chữ nhật có margin bằng 100‰ mỗi chiều:

Plain text
pearlX = clamp(pearlX,minX+0.1*width,maxX-0.1*width)
pearlZ = clamp(pearlZ,minZ+0.1*height,maxZ-0.1*height)

Trong code, 0.1*width dùng mulDiv(width,100,1000), không dùng float.

Fallback không có beast: pearl=clamp(heart,fieldBounds).

3.2. Lotus geometry

Bán kính đủ lớn để phủ cả bốn góc sân:

Plain text
lotusRadiusMm =
    max(distanceMm(pearl,corner) for corner in fieldCorners)
    + 1000

Phần full damage gồm:

Central disc: radius = 350‰ × lotusRadius.

Tám petals theo (±1000,0), (0,±1000), (±707,±707).

Mỗi petal là capsule từ pearl đến 850‰ × lotusRadius, bán kính 100‰ × lotusRadius.

Phần còn lại trong lotusRadius nhận 500‰ lotus damage.

Tại F67, dùng cùng footprint nhưng hai collider theo độ cao riêng biệt:

Plain text
groundLotus: y = 0..1500
skyLotus:    y = 2500..6000

Beast chỉ có thể bị đánh bởi collider thuộc band F0 của nó, đồng thời phải đang nằm trong band đó.

Lotus chỉ gây một damage event trên mỗi beast tại F67. Hình hoa sen có thể tồn tại lâu hơn nhưng không gây damage tiếp.

4. Năm phases và D58

Phase

	

Frames

	

Hành động




charge

	

Trước F0, trong lúc typing

	

Hỏa khí tập trung quanh kiếm, không gameplay damage




release

	

F0–F2

	

Release tại caster, tiếp theo là guided touch




travel

	

F3–F42

	

Hai rồng quét đường, mở rộng các corridor collider




impact

	

F43–F78

	

Hội tụ, roar, hoa sen phát nổ F67




aftermath

	

F79–F300

	

Erosion, không thêm damage

Release và touch

F0: xung touch bán kính 3000 mm tâm caster, gồm hai height-band collider riêng. Xử lý tất cả selected victims hợp lệ nằm trong vùng.

F1: mỗi rồng tạo một guided-touch collider quanh selected victim gần caster nhất chưa nhận touch, tại vị trí hiện tại của victim:

Ground radius 1800 mm.

Sky radius 2500 mm.

F2: nếu toàn Cast vẫn chưa gây damage, thử guided touch lại trên selected victim hợp lệ gần caster nhất.

Các guided touches luôn dùng cùng touch kind, không tạo loại hit thứ tư.

Hình ảnh bắt đầu từ kiếm ở F0. Guided touch F1/F2 được thể hiện bằng một đường hỏa khí lao tức thời từ kiếm đến mục tiêu; không dùng vị trí cổng hay điểm hội tụ.

Bản sửa ở mục 5 bảo đảm mỗi selected victim có ít nhất 1 HP touch được phân bổ khi budget hợp lệ, vì vậy D58 không còn phụ thuộc phép làm tròn share.

Điều kiện D58: nếu Cast có budget dương và ít nhất một selected victim còn sống, ở height band hợp lệ đến lúc F1/F2, damage đầu tiên xảy ra chậm nhất F2.

Travel và trail

F3–F42: kích hoạt những segment được head quét qua.

F43–F46: corridor còn gây damage trên những segment đã kích hoạt.

F47 trở đi: corridor ngừng gameplay collision.

F67: lotus damage.

Mỗi segment có:

Plain text
openTick = first tick reached by dragon head
damageCloseTick = min(openTick + 54, 46)
visualTrailTicks = 54

Ở F3–F42, segment cuối đang được head đi qua chỉ được mở đến vị trí head hiện tại, không mở trước toàn bộ segment.

Lý do chọn F46: mục tiêu vừa nhận touch tại F0/F1 có cơ hội nhận corridor từ F20/F21 nếu vẫn nằm trong trail. Mọi corridor hit đều không muộn hơn F46, nên lotus F67 cách hit trước ít nhất 21 ticks.

Phần trail hình ảnh sau F46 không gây damage, dù vẫn còn sáng.

5. Hit rules, budgets và balance
5.1. Hit volumes

Kind

	

Collider

	

Target




touch

	

F0 r 3000 mm; F1/F2 ground r 1800 mm, sky r 2500 mm

	

Ground hoặc sky, đúng band




corridor

	

Ground capsule r 2600 mm; sky capsule r 3200 mm

	

Đúng height band




lotus

	

Disc + 8 petals + half-damage region

	

Toàn field, theo height band

Mỗi beast có:

Plain text
hitMask: TOUCH | CORRIDOR | LOTUS
lastHitTick: integer

Điều kiện:

Plain text
not hitThisKind
currentTick - lastHitTick >= 20
insideCorrectHeightBand
insideActiveVolume
remainingAllocatedDamage > 0

Như vậy tối đa ba hit một Cast, không hit nào cách nhau dưới 20 ticks.

5.2. Trial damage data

Tất cả các thông số dưới đây là đề xuất cần bot validation.

Parameter

	

Trial value




castBudgetW100

	

180




castBudgetHpK0

	

162




baseVictimW100

	

22




baseVictimHpK0

	

20




falloffStepPm

	

150




falloffFloorPm

	

400




touchSharePm

	

150




corridorSharePm

	

550




lotusSharePm

	

300




lotusHalfPm

	

500




bossCapW100

	

150




cooldownMs

	

8000




wordLength

	

4–7

Giữ cooldown, typing requirement và posture=-20. Posture chỉ áp dụng một lần cho mỗi beast trong Cast, khi nó nhận effective damage đầu tiên.

5.3. Total budget và victim quota

Tại F0:

Plain text
B = mulDiv(
      mulDiv(162,M_q,1000),
      seatBucketPm,1000
    )

Nếu cả hai dragon có mục tiêu:

Plain text
B0 = floorDiv(B,2)
B1 = B-B0

Nếu chỉ một dragon có mục tiêu, toàn bộ B được chuyển cho dragon đó.

Victim quota:

Plain text
requestedQ =
    min(N,clamp(ceilDiv(400*N,1000),12,20))

if B >= 2:
    Q = min(requestedQ,floorDiv(B,2))
else:
    Q = min(requestedQ,B)

Chia Q theo số beast mỗi dragon, làm tròn bằng mulDiv. Giới hạn quota mỗi dragon bởi floorDiv(Bdragon,2) khi B>=2, và số beast của dragon đó. Phân phối slot dư lần lượt cho dragon còn capacity lớn hơn; hòa theo dragonId.

Selection trong mỗi dragon:

Chọn beast gần caster nhất.

Chọn các sky beasts chưa chọn theo khoảng cách caster, tới khi đủ quota.

Điền slot còn lại bằng farthest-first: chọn beast có minDist2 tới tập đã chọn lớn nhất; hòa bằng weight cao hơn, sau đó ID nhỏ hơn.

Với N=35–45, M_q=1000 và seatBucketPm=1000, quota danh nghĩa là 14–18. Đây là số được phân bổ damage, chưa phải số guaranteed actual hits.

5.4. Ground/sky allocation

Trong mỗi dragon, gọi g,s là số selected victims ground và sky.

Nếu chỉ một band có mục tiêu, band đó nhận toàn bộ Bdragon.

Nếu cả hai band có mục tiêu:

Plain text
Bsky = clamp(
    mulDiv(Bdragon,s,g+s),
    2*s,
    Bdragon-2*g
)

Bground = Bdragon-Bsky

Quota đã được giới hạn để mỗi selected victim có ít nhất 2 HP budget trong chế độ thông thường: một cho touch và một cho lotus.

Mỗi band có budget B và n selected victims, chia part budgets:

Plain text
L = max(n,mulDiv(B,300,1000))
T = max(n,mulDiv(B,150,1000))
C = B-L-T

Các giá trị hợp lệ khi B>=2*n. Nếu budget toàn Cast chỉ còn 1 HP, dùng special case: một target, 1 HP touch, 0 HP corridor/lotus.

Cách này giữ tỷ lệ danh nghĩa 15/55/30 khi ngân sách đủ, nhưng ưu tiên bảo đảm 1 HP cho touch và lotus ở quality thấp.

5.5. Per-victim envelopes

Trong mỗi dragon, sort selected victims bằng (dist2ToCaster,beastId) để xác định distinctRank.

Plain text
falloffPm = max(400,1000-150*distinctRank)

rawDamage = mulDiv(20,falloffPm,1000)
rawDamage = mulDiv(rawDamage,M_q,1000)
rawDamage = mulDiv(rawDamage,seatBucketPm,1000)

Với selected victim có budget từ 2 HP trở lên, đặt rawDamage=max(2,rawDamage). Đây là mức tối thiểu do damage granularity, không phải bypass total budget.

Tạo desired envelopes:

Plain text
desiredTouch =
    max(1,floorDiv(rawDamage*150,1000))

desiredCorridor =
    floorDiv(rawDamage*550,1000)

desiredLotus =
    max(1,rawDamage-desiredTouch-desiredCorridor)

if desiredTouch+desiredCorridor+desiredLotus > rawDamage:
    desiredCorridor =
        max(0,rawDamage-desiredTouch-desiredLotus)

Phân bổ trong mỗi band theo thuật toán cố định:

Cấp trước 1 HP touch và 1 HP lotus cho mỗi selected victim.

Trừ số đó khỏi T và L.

Với từng kind theo thứ tự touch, corridor, lotus, dùng round-robin theo distinctRank để phân phát 1 HP/lượt, không vượt desired envelope hay part budget.

Ghi allocatedTouch, allocatedCorridor, allocatedLotus vào Cast state.

Không chuyển budget đã cấp giữa những nạn nhân tại runtime. Nếu mục tiêu chết trước khi nhận một phần damage, phần đó không được tiêu và cũng không được cấp lại. Điều này tránh first-come budget starvation và giữ replay deterministic.

Khi xử lý một hit:

Plain text
requested = allocatedDamage[victim][kind]

if kind == LOTUS and outsideFullLotus:
    requested = mulDiv(requested,500,1000)

effective = min(
    requested,
    currentHp,
    remainingPartBudget,
    remainingBossCapIfBoss,
    remainingClusterCapIfSwarm
)

if effective > 0:
    hp -= effective
    spentPartBudget += effective
    updateHitMaskAndLastHitTick()
    damageShareLedger += effective

Ở phần half lotus, mulDiv làm tròn half-up; allocated 1 HP vẫn gây 1 HP. Không thể gây damage lớn hơn envelope.

Swarm cap:

Plain text
clusterCapHp =
    floorDiv(originalClusterTotalHp*600,1000)

Chụp originalClusterTotalHp tại F0 theo clusterId. Cả hai rồng, ba kind và toàn bộ thời lượng Cast cùng chia sẻ một ledger. Không vượt 60% dù các hit xảy ra khác tick.

Boss cap: 135 HP mỗi castId, áp dụng trên effective damage cộng dồn của cả hai rồng.

Candidate ordering: gom toàn bộ candidate events trong tick rồi sort theo (kindPriority,dist2ToHeart,beastId,castId,dragonId). Việc kiểm tra các cap và ghi HP thực hiện theo thứ tự này.

5.6. Cân bằng toàn game

Mục tiêu canon không đổi: key-2 phải chiếm tối đa 20% tổng match damage.

1.80 W là ngân sách trial, chưa chứng minh đạt mục tiêu. Dữ liệu cũ cho thấy 1.25 W mỗi bên vẫn cho share 29–36%, trong khi giảm quá mạnh làm win rate sụp. Vì vậy không được chỉ nerf skill này.

Phải chạy đồng thời các thay đổi thử nghiệm sau:

key1Reach: 12 → 18 m.

autoAttackReach: 10 → 15 m.

Kiểm tra và điều chỉnh reach của các active skills khác để phù hợp sân 40×26 m.

Retune auto-attack DPS, wave pacing, spawn pressure và enemy survivability sau khi reach thay đổi.

Các con số reach là giả thuyết bắt đầu từ quan sát range ×1.5 trước đó, không phải kết quả cân bằng cuối cùng.

Owner approval required: tất cả thay đổi budget, damage quota, reach, DPS và pacing. Những quyết định đã khóa — hai rồng, một hỏa châu, hoa sen, Sword key-2, Fire và field-wide — không cần xem xét lại.

6. Acceptance metrics và bot plan
6.1. Skill-specific targets

Metric

	

Định nghĩa

	

Target




distinctVictimsP10P90

	

Số beast nhận effective damage ≥1 HP mỗi Cast, khi F0 có 35–45 eligible beasts

	

12–20




travelCoverage

	

Số beasts F0 từng nằm trong active ground/sky corridor tại một tick chúng còn sống, trước budget, chia tổng eligible F0

	

≥85%




lotusAreaCoverage

	

Diện tích field nằm trong footprint lotus

	

100%




threatMassBalance

	

min(mass0,mass1)/(mass0+mass1)

	

≥400‰ trong ≥90% những Cast có thể chia cân bằng




firstHit

	

Tick effective damage đầu tiên sau F0

	

F0–F2




crowHitRate

	

F0 crows nhận ≥1 HP trước kết thúc Cast / F0 crows

	

≥90% tại peak có 1–3 crows




perfActiveTickP95

	

Thời gian xử lý mỗi Cast tại tick không lập path

	

≤50 µs

Báo cáo F0 planning cost riêng vì có clustering, spline và damage allocation; mục tiêu thử nghiệm <=1 ms, không được âm thầm gộp vào active-tick performance.

Đối với sân lớn, sampleStepMm có thể vượt 500. Khi đó kiểm tra waypoint deviation theo giới hạn sampleStepMm, đồng thời báo riêng coverage regression; không được coi độ phủ 85% là mặc nhiên đạt.

6.2. BALANCE.md metrics

Metric

	

Acceptance




Win rate, Balanced bot cohort

	

75–90%




P

	

15–35%




Q

	

50–70%




Typed damage share

	

≥55%




Key-1 share of typed damage

	

≤30%




Key-2 share of total match damage

	

≤20%




Auto-attack share

	

12–18%




S, I, O, N

	

Giữ nguyên công thức và ngưỡng hiện hành trong BALANCE.md

Không tự đặt định nghĩa S, I, O, N vì chưa có tài liệu. Coding agent phải đọc BALANCE.md trước khi xây acceptance runner.

6.3. Test matrix

Full-match: 17 bot profiles × 20 seeds × 4 configurations:

legacy-key2

twin-pearl-v2-only

reach-only

twin-pearl-v2-plus-reach

Tổng 1360 matches. Giữ Balanced và pacing enabled; đối chiếu New, Kid, Intermediate, Fast riêng để không che giấu regression.

Peak sweep: tái sử dụng tick có mật độ địch cao nhất từng wave, tối thiểu 20 seeds/profile. Báo cáo p10, median, p90 cho distinct victims, travel coverage, crow hits, overkill, damage theo kind và total key-2 share.

6.4. Synthetic layouts

Sử dụng cùng geometry, không tạo gate thực:

Plain text
field = [-20000,20000] x [-18000,8000]
heart = (0,0)
caster = (0,3000)

Layout

	

Vị trí test




one-gate

	

18 wolves: x=-9000+3600*(i%6), z=-15000+4000*floor(i/6); 7 rats quanh (0,-7500); 2 crows (±14000,-16000)




three-gate

	

3 cụm × 8 wolves; tâm (-16000,-15000), (0,-17000), (16000,-15000); offset trong cụm x=-2700+1800*(j%4), z=-1000+2000*floor(j/4); 3 crows tại ba tâm




open-arena

	

36 wolves: x=-17500+7000*(i%6), z=-16000+4000*floor(i/6); 4 crows (±18000,-16000) và (±18000,6000)




behind-caster

	

14 wolves: x=-14000+4500*(i%7), z=4500+1500*floor(i/7); 2 crows (±16000,6500)




lone-foe

	

1 ape (13000,4500)




empty-field

	

0 beasts

Với rats, đặt offset (0,0), (±500,0), (0,±500), (±500,±500) và cùng clusterId. Crows có y=4000; ground beasts y=0.

Các layout one-gate và three-gate chỉ mô phỏng phân bố địch. Chúng không đòi thay GateId, vì engine chưa load được số cổng khác.

Determinism và invariants:

Cùng seed/input → cùng world hash trên các JS runtimes.

Mirror/rotate positions cùng field geometry → đối chiếu coverage, số victims và damage sau khi ánh xạ ID; báo khác biệt do tie-break nếu có, không so nguyên world hash.

Không beast nào nhận hơn ba kind hits hoặc hai hits cách dưới 20 ticks.

Không vượt boss cap, cluster cap hoặc per-part budget.

Sky victims không bị ground collider đánh; ground victims không bị sky collider đánh.

Hai Cast chồng nhau vẫn có độc lập castId và ledgers.

Các waypoint và resampled polyline ở trong field.

Flag off giữ nguyên replay, RNG consumption, serialization và world hash byte-for-byte.

7. VFX implications

Hai rồng vẫn dùng animated body mesh cộng fire trail theo đường sim cung cấp; renderer không tự suy diễn hướng đi từ gate hoặc flow field. View nhận castId, dragonId, pathSamples, headProgress, pearlPosition, lotusRadius, phaseFrame và hit events. Đường rồng, độ cao thị giác và timing có thể được làm mượt ở render layer, nhưng không được thay gameplay colliders. Hỏa khí xuất phát từ kiếm tại F0, hai rồng lao qua các khu vực có địch, hội tụ vào pearl, rồi hoa sen tám cánh phủ sân tại F67. Hình ảnh giữ đỉnh trước khi erosion đến F300. Fire style phải anime/mythic, có dark ink backing để đọc trên đá sáng, và chỉ những lõi hỏa khí mảnh dùng bloom mạnh. Asset được tạo bằng Firefly và Blender sau; bước này chỉ triển khai placement và animation interface.

8. Risks, verification và uncertainty

Rủi ro

	

Kiểm tra / xử lý




Rồng bay quá nhanh vì đường dài

	

Đo pathLength, head speed và các góc đổi hướng; review slow-motion ở cả 6 layouts




Spline overshoot hoặc resampling hụt mục tiêu

	

Assert mọi sample nằm trong bounds và đo khoảng cách từ representative tới path




Địch di chuyển khỏi corridor

	

Đo coverage bằng live positions từng tick, không dùng vị trí F0 làm kết quả




F0 planning spike

	

Benchmark split, clustering, spline và allocation riêng; kiểm tra 60 beasts và 2 Cast




Spatial index quá đông ở một tile

	

Profile số segment candidates/tick; cải thiện index nếu P95 vượt 50 µs




Quota 14–18 nhưng actual hit dưới 12

	

Tách báo cáo allocated victims, victims còn sống tại F67 và actual effective hits




Crow được chọn nhưng không nhận damage

	

Kiểm tra sky band, sky budget và live HP sau từng kind




Lotus quá yếu vì nhiều victim chỉ nhận 1 HP

	

Đo lotus effective damage, số hit và tỷ lệ lotus/total damage




Budget vẫn khiến key-2 vượt 20%

	

Tuning budget cùng các hệ thống reach, DPS và pacing




Nerf làm người chơi không thắng wave 2

	

So sánh reach-only, skill-only và combined trên từng bot




Integer overflow hoặc rounding drift

	

Assert safe intermediates, test signed coordinates và replay trên nhiều runtimes




Cluster cap bị tính lại theo từng hit

	

Assert cluster ledger dùng chung toàn Cast và floor cap




Render khác collision

	

Debug overlay các corridor capsules, lotus footprint và height bands

Những điểm chưa chắc chắn

1. 1.80 W chưa được chứng minh là budget tối ưu. Đây là trial starting point. Cần chạy bot mới biết có đạt key-2 share ≤20% trong khi vẫn duy trì tỷ lệ thắng hay không.

2. 12–20 distinct victims là acceptance target, không phải bảo đảm mọi Cast. Một victim có thể chết trước F67, rời khỏi field hoặc không còn ở đúng height band. Phải đo actual effective damage.

3. Route theo snapshot F0 không dự đoán toàn bộ chuyển động. Với quái di chuyển nhanh hoặc đổi hướng, corridor coverage có thể giảm. Không tự ý thêm replanning mỗi tick vì điều đó tăng CPU, phức tạp state và ảnh hưởng determinism.

4. Những bản đồ lớn hơn có thể buộc adaptive sampling thưa hơn. Thuật toán vẫn map-agnostic, nhưng chất lượng phủ và tính đọc được của đường rồng cần được đánh giá theo kích thước field, không tự nhận đạt cùng coverage trên mọi kích thước.

5. Cân bằng toàn game phụ thuộc các hệ thống khác. Số liệu đã cung cấp chứng minh key-2 đang che lấp vấn đề reach của key-1 và auto-attack. Chỉ giảm skill sẽ không đủ.

Final acceptance gate

Chỉ bật twin-pearl-v2 mặc định khi đạt đồng thời:

Không phụ thuộc gate, lane, waypoint hoặc flow field.

F0–F2 có effective first hit trong điều kiện D58 hợp lệ.

Tuân thủ 20-tick re-hit, three-kind limit, boss cap và swarm-cluster cap.

Đạt distinct-victim, coverage, crow và performance targets.

Key-2 share ≤20%, Balanced win rate 75–90%, cùng các gate trong BALANCE.md.

Với flag off, mọi output legacy vẫn byte-identical.

rulesHash phải bao gồm toàn bộ trial table twin-pearl-v2 chỉ khi swordKey2: "twin-pearl" được bật. Khi tắt, không đăng ký trial table, không tạo Cast state mới, không tiêu thụ RNG và không thay serialization.

Kết luận: Giữ thiết kế Threat-Balanced Coverage Routing + Field-Wide Lotus. Hai rồng thực sự bay qua các khu vực có địch, viên châu và hoa sen bảo đảm hiệu ứng bao trùm sân, còn damage envelopes và per-cast ledgers kiểm soát sức mạnh. Đây là một thiết kế xác định để coding agent triển khai và kiểm thử; các ngưỡng balance vẫn phải được xác nhận bằng bot trước khi phát hành.

---

#### fallback-turn-3:0:user · USER (Claude)

Review your latest full answer above (the corrected full version) against the brief, the facts and the constraints. It FAILS only for a real defect: a wrong fact or source, a step that would not work, a missing step the goal needs, a contradiction with the constraints or the owner's decisions, or a part too vague for a worker to execute. Wording, style and optional extra ideas are not defects.
If it is correct and accurate, answer with exactly one line: VERDICT: PASS (you may add one line "Optional:" with ideas that do not change the verdict)
Otherwise answer: VERDICT: FAIL, then list each defect, then give the corrected FULL analysis and solution (not a diff). If the full version does not fit in one message, stop at a section boundary, end with the line PART 1 OF N, and I will ask for the next part.

---

#### fallback-turn-3:2:assistant · CHATGPT

ChatGPT said:
VERDICT: FAIL

Bản corrected full version vẫn có các lỗi ảnh hưởng trực tiếp đến tính đúng đắn, determinism, damage allocation và khả năng triển khai. Không phải lỗi diễn đạt.

Các lỗi cần sửa

Sai cơ chế bảo đảm damage budget. Công thức chia đều budget giữa hai rồng nhưng chia victim quota theo số lượng mục tiêu có thể khiến một rồng không đủ 2 HP × selectedVictims, dù toàn Cast còn ngân sách. Không có thuật toán phân bổ lại được xác định đầy đủ.

F0 allocation có thể giữ lại HP không bao giờ dùng. Mỗi selected victim được dành tối thiểu 1 HP cho touch, nhưng F0–F2 chỉ có thể chạm một số mục tiêu. HP dành cho các nạn nhân khác bị khóa, không chuyển sang corridor hoặc lotus, gây giảm damage không dự kiến.

Damage budget thiếu nhất quán khi chất lượng thấp. Quy tắc B>=2 chưa xử lý đầy đủ B=0, B=1, số dragon không có mục tiêu, quota và phần budget không chia hết. Cam kết hit đầu tiên F0–F2 vì vậy chưa được chứng minh.

Clustering và routing chưa có giới hạn chi phí đủ chặt. Thuật toán có thể sinh 60 representatives mỗi rồng trong một số trường hợp, sau đó Catmull–Rom, resampling và spatial indexing không có upper bound rõ ràng cho số phép kiểm tra. Mục tiêu 50 µs/tick/cast chưa có cơ chế kiểm soát.

Catmull–Rom chưa bảo đảm đường đi phủ các representative. Spline đi qua knot nhưng bước chia đoạn có giới hạn 128, rồi resampling xuống tối đa 769 điểm có thể đi tắt ở khúc cong và bỏ xa một waypoint. Assertion <=500 mm được nêu nhưng không có thuật toán bảo đảm.

Spatial index mới chỉ là mô tả, chưa thực thi được. Chưa xác định thời điểm segment mở, cách xử lý segment bị head đi qua một phần trong tick, cách lưu trail và cách tránh xét hàng nghìn segment cho mỗi beast.

Thứ tự tính damage và ledger chưa hoàn chỉnh. Có hai rồng, hai Cast chồng nhau, boss cap, swarm cap, damage share và posture, nhưng chưa có một quy trình commit duy nhất bảo đảm không tiêu budget trùng hoặc tính overkill sai.

Giới hạn swarm cluster dùng sai dữ liệu có thể xảy ra. sum(originalClusterTotalHp) không suy ra được từ HP hiện tại của các beast đang sống. Dùng HP còn lại như tổng HP gốc sẽ thay đổi semantics của s7.2; phải dùng nguồn cluster capacity đã được canon xác định.

Geometry và damage routing chưa phân biệt đủ rõ. Đường rồng đi qua mọi representative, nhưng chỉ selected victims được damage. Nếu không nêu rõ đây là deliberate budget selection, một coding agent có thể hiểu corridor là gây sát thương cho tất cả beast giao với collider.

Metric và test chưa thể chạy đầy đủ. Chưa quy định rõ snapshot denominator, thời điểm đếm damage, cách đo percentile, cách xử lý các Cast không đủ địch, fixtures có giá trị threatW100/ID cụ thể, và tiêu chí invariance khi tie-break không đối xứng.

Timing của trail còn mơ hồ. openTick, damageCloseTick, visualTrailTicks chưa đủ để biết chính xác một đoạn đã được head đi qua bao nhiêu tại tick hiện tại. Kết quả có thể là collider xuất hiện trước đầu rồng.

Một số giới hạn hiệu năng và balance được trình bày như thể đã có cơ sở bảo đảm. Trong thực tế chưa có benchmark hoặc bot run nào chứng minh budget 1.80 W, coverage ≥85%, 12–20 victims hay performance ≤50 µs.

Dưới đây là bản thay thế đầy đủ. Phần thuật toán, timing và damage được thống nhất thành một đặc tả triển khai; các mục tiêu performance/balance được giữ là acceptance gates cần đo.

Corrected full design — twin-pearl-v2

Skill: Twin Dragons, One Burning Pearl (雙龍戲珠)
ID: twin-pearl
Slot: Sword / Key 2
Element: Fire
Design: Threat-Balanced Twin Coverage + Field-Wide Lotus

Chốt một phương án: Hai rồng xuất phát từ caster, chia chiến trường theo khối lượng địch và đi qua những điểm đại diện cho các cụm. Cả hai hội tụ vào hỏa châu; hoa sen cuối phủ toàn bộ field. Đường hình học quyết định nơi collider hiện diện; một danh sách nạn nhân với ngân sách hữu hạn quyết định ai có thể nhận sát thương. Hai việc độc lập, không phụ thuộc số cổng.

1. Inputs và snapshot

Data

	

Read

	

Usage




fieldBounds, heart, caster

	

F0

	

Geometry




id, x, z, y, hp, threatW100, tier, clusterId, bossFlag

	

F0

	

Partition, clusters, path, allocation




M_q, seatBucketPm

	

F0

	

Budget




x, z, y, hp, alive

	

Every tick

	

Actual collision and effective damage

Tất cả tọa độ path dùng integer mm, chuyển từ sim bằng mulDivSym(u,1,60); khi ghi trở lại dùng mm*60.

Plain text
groundBandMm = [0,1500]
skyBandMm = [2500,6000]
maxLiveBeasts = 60
maxConcurrentCasts = 2

Phân loại height band tại F0; khi hit phải nằm trong band tương ứng. Không dùng gateId, tên species, flow field hoặc spawn point. Beast sinh sau F0 không tham gia Cast hiện tại.

Snapshot IDs được sort tăng dần và duy nhất. Tất cả tie-break dùng ID, sau đó dragon index.

Empty field: Gameplay giữ quy tắc không resolve Cast nếu không có damageable beast. Lab vẫn tạo một đường mặc định cho mỗi rồng từ caster qua hai điểm lệch đối xứng đến clamp(heart,fieldBounds), với damageEnabled=false. Trường hợp một beast phải có nhánh riêng, không chạy thuật toán chia hai tập.

2. Dragon path — deterministic algorithm
2.1. Lựa chọn

Candidate

	

Decision

	

Reason




mirrored-spiral

	

Reject làm đường chính

	

Phủ vùng trống quá nhiều




top-k-clusters

	

Adapt

	

Hiệu quả ở cụm đông nhưng có thể bỏ địch đơn lẻ




threat-mass-split

	

Adopt

	

Hai rồng được phân công theo dữ liệu địch, không theo cổng

Hybrid: mass split → cluster representatives → nearest-neighbour route → bounded corner smoothing.

2.2. Chia ownership

Với N>=2, tính cho từng beast:

Plain text
weight = clamp(isqrt(max(1,threatW100)*100),50,300)

Thử sáu trục:

Plain text
(1000,0), (0,1000), (707,707), (707,-707),
farthestPairAxis, perpendicularAxis

farthestPairAxis lấy từ cặp ID có dist2 lớn nhất; hòa theo (minId,maxId). Nếu không có độ dài, dùng (1000,0).

Sort theo signed dot product với trục, rồi theo ID. Thử mọi cut thành hai tập không rỗng. Tính:

Plain text
mass = sum(weight)
center = roundSym(sum(weight*position)/mass)
SSE = sum(weight*dist2(position,center))

imbalancePm = mulDiv(abs(mass0-mass1),1000,mass0+mass1)

compactPm = mulDiv(
    SSE0+SSE1,1000,
    max(1,(mass0+mass1)*fieldDiagonalSquared)
)

score = 700*imbalancePm + 300*compactPm

Chọn (score,axisIndex,cutIndex) nhỏ nhất. Đây là hai thành phần đã chuẩn hóa cùng đơn vị ‰, không cộng trực tiếp diện tích với khối lượng.

Hai tập được gán dragon0/dragon1, không phải west/east. Trường hợp N=1 gán beast cho dragon0.

2.3. Clustering và representatives

Trong mỗi tập, chạy union-find: hai beast cùng height band và cách mặt đất <=3000 mm thuộc cùng component. Sort components theo ID nhỏ nhất.

Với từng component, chọn representatives cho tới khi mọi member được cover:

Plain text
for candidate in uncoveredMembers:
    coveredMass = sum(
        weight[j]
        for uncovered j
        if dist2(candidate,j) <= 1000*1000
    )

choose maximum (coveredMass, -candidate.id)
append candidate.position
mark members within 1000 mm covered

Cùng vị trí vẫn có thể sinh representative riêng cho ground và sky, nhưng không trùng trong cùng band. Số representative toàn Cast <=N<=60.

2.4. Routing và smoothing

Tạo flankAnchor bằng hướng caster→pearl, một điểm lệch bên trái và một điểm lệch bên phải. Khoảng lệch bằng 150‰ × min(fieldWidth,fieldHeight); nếu hướng bằng zero, dùng (1000,0).

Trong mỗi dragon, từ caster → flankAnchor, chọn component tiếp theo có representative gần nhất, ưu tiên:

Plain text
cost = mulDiv(distanceMm,1000,1000+min(componentMass,3000))

Hòa theo component minimum ID. Trong component chọn representative gần điểm cuối đường nhất, hòa theo beast ID. Lặp đến hết, rồi nối pearl.

Thay Catmull–Rom bằng corner smoothing bị chặn độ lệch. Với mỗi internal waypoint P:

Plain text
d0 = min(250, floorDiv(distance(P,previous),4))
d1 = min(250, floorDiv(distance(P,next),4))

A = P + mulDivSym(unitPm(previous-P),d0,1000)
B = P + mulDivSym(unitPm(next-P),d1,1000)

Thay góc bằng quadratic Bézier A → P → B, lấy tPm = 0,250,500,750,1000. Tính tất cả trọng số bằng integer mulDivSym; clamp về field. Đường cong nằm cách P tối đa khoảng 250 mm. Các đoạn thẳng xen kẽ được chia theo chiều dài tối đa 500 mm.

Tạo cumulative integer arc length. Mọi đoạn có chiều dài zero được bỏ, trừ việc bảo toàn điểm đầu/cuối.

Giới hạn: tối đa 60 representatives, 64 routing knots mỗi rồng và 2048 output samples mỗi rồng. Nếu dense polyline vượt giới hạn, resample theo chiều dài với:

Plain text
K = min(2047, max(1,ceilDiv(totalLengthMm,500)))
distance[i] = mulDiv(totalLengthMm,i,K)

Tessellation không được bỏ các endpoints. Không khẳng định khoảng cách tới mỗi representative luôn ≤500 mm trong mọi map lớn; đó là giá trị phải đo. Hiệu ứng lotus không phụ thuộc sai số này.

2.5. Time normalization và collision
Plain text
travelStart = F3
travelEnd = F42
travelTicks = 40

headDistance(Fn) =
    mulDiv(totalLengthMm,n-2,40)  // 3 <= n <= 42

Dùng binary search trên cumulative length để lấy head position. Không chỉ kiểm tra vị trí đầu rồng: mỗi tick tạo các swept subsegments từ headDistance trước đến headDistance hiện tại.

Mỗi swept subsegment được đánh dấu openTick đúng lúc đầu rồng đi qua. Nó được phép gây corridor damage từ openTick tới:

Plain text
damageCloseTick = min(openTick+54,47)

Mỗi subsegment có hai collider theo cùng footprint:

Plain text
groundCorridorRadiusMm = 2600
skyCorridorRadiusMm = 3200

Kiểm tra height band độc lập; crow chỉ có thể nhận sky damage.

Để tránh quét toàn path mỗi tick, dùng fixed 4000 mm spatial grid: thêm subsegment mới vào các cell giao với expanded AABB, cập nhật beast cell theo vị trí thực, rồi chỉ xét subsegments thuộc cell của beast và đang active. Duyệt theo segment ID tăng dần. Sau khi một beast đã nhận corridor, bỏ nó khỏi các kiểm tra corridor sau của cùng Cast.

Giới hạn số sample được kiểm soát; thời gian ≤50 µs vẫn phải benchmark, không được xem là bảo đảm toán học.

2.6. Cast state
Plain text
castId, startTick, rulesVersion
fieldBounds, caster, pearl, lotusRadius
snapshotBeasts, ownership, clusterRepresentatives
routeKnots[2], samples[2], cumulativeLengths[2]
headDistance[2], activeSegments[2], spatialCells[2]
selectedVictims, allocatedDamage[3], hitMask
lastHitTick, partSpent, bossSpent, swarmClusterSpent
damageShareLedger

Hai Cast đồng thời có state và ledgers độc lập.

Map cases: hai cổng, một cổng, ba cổng, arena nhiều hướng và địch ở sau caster đều chạy cùng thuật toán. Không có nhánh theo gate count. Lone foe và empty field dùng hai trường hợp đặc biệt đã nêu.

3. Pearl và lotus

Pearl ở weighted centroid của tất cả eligible beasts F0:

Plain text
pearlX = roundSym(sum(weight*x)/sum(weight))
pearlZ = roundSym(sum(weight*z)/sum(weight))

Clamp vào 80% phần trong của rectangle, với margin 100‰ mỗi cạnh. Empty field dùng clamp(heart,fieldBounds).

Bán kính hoa sen:

Plain text
lotusRadiusMm =
    max(isqrt(dist2(pearl,corner)) for corner in fieldCorners)
    + 1000

Hình lotus có một full-damage central disc 350‰ × radius, tám full-damage capsule petals từ tâm ra 850‰ × radius với radius 100‰ × lotusRadius, theo tám hướng (±1000,0), (0,±1000), (±707,±707).

Phần còn lại trong đĩa lotus nhận 500‰ lotus damage. Vì bán kính vượt khoảng cách tới mọi góc rectangle nên footprint bao trùm cả field.

Ground và sky có collider riêng:

Plain text
groundLotusY = [0,1500]
skyLotusY = [2500,6000]

F67 chỉ có một lotus damage event mỗi beast. Full/half được xác định bằng hình học, không bằng lane.

4. Five phases và D58

Phase

	

Frame

	

Gameplay / visual




charge

	

Trước F0

	

Tích hỏa khí trên kiếm trong lúc gõ




release

	

F0–F2

	

Xung từ caster và guided touch




travel

	

F3–F42

	

Hai rồng quét đường, kích hoạt corridor




impact

	

F43–F78

	

Roar F43–F50; hoa sen gây damage F67; giữ đỉnh đến F78




aftermath

	

F79–F300

	

Erosion, không thêm damage

F0: Thay hold box hướng cổng bằng vòng touch bán kính 3000 mm quanh caster. Chỉ selected victims đúng height band mới có thể nhận damage.

F1: Nếu một dragon còn touchBudget nhưng chưa có touch hit, tạo guided-touch collider tại vị trí hiện tại của selected victim gần caster nhất thuộc dragon đó:

Plain text
groundTouchRadiusMm = 1800
skyTouchRadiusMm = 2500

F2: Nếu toàn Cast chưa gây damage, thử lại với selected victim hợp lệ khác. Không tạo thêm damage kind.

Để đạt D58, ngân sách touch phải được giữ ở mức pool cấp dragon/height band, không khóa cho một victim cụ thể. Chọn mục tiêu guided tại runtime từ danh sách F0, kiểm tra HP, band và cluster cap trước khi đánh.

Nếu có selected victim còn damageable, word-quality multiplier dương và touchBudget >=1 HP, hit đầu tiên xảy ra trong F0–F2. Không thể bảo đảm hit nếu toàn bộ mục tiêu hợp lệ chết hoặc mất khả năng nhận damage trước lúc collider kích hoạt; trường hợp đó cần được báo riêng, không tính là đạt D58.

Corridor: Các segment mở từ F3 đến F42, giữ gameplay collision tối đa đến F47. Vì lotus gây damage F67, mọi corridor hit đều cách lotus ít nhất 20 ticks. Trail visual có thể giữ 54 ticks tính từ lúc segment mở.

Không có khoảng chờ charge nào sau F0.

5. Hit rules, damage budgets và global balance
5.1. Thông số trial

Parameter

	

Value




castBudgetW100

	

180




castBudgetHpK0

	

162




baseVictimW100

	

22




baseVictimHpK0

	

20




falloffStepPm

	

150




falloffFloorPm

	

400




touchSharePm

	

150




corridorSharePm

	

550




lotusSharePm

	

300




lotusHalfPm

	

500




bossCapW100

	

150




cooldownMs

	

8000




wordLength

	

4–7




postureDelta

	

-20

Các lượng HP trên là cho K0. Ở K khác, dùng phép chuyển W→HP chính thức của loader, không hardcode tỷ lệ K0.

5.2. Quota và ngân sách hai rồng

Tại F0:

Plain text
B = mulDiv(
    mulDiv(w100ToHp(180), M_q, 1000),
    seatBucketPm, 1000
)

if M_q > 0 && seatBucketPm > 0:
    B = max(1,B)

Qrequested = min(N,clamp(ceilDiv(2*N,5),12,20))
Q = min(Qrequested, B >= 2 ? floorDiv(B,2) : B)

Nếu B=0, không có effective hit; nếu B=1, chỉ một victim được chọn, toàn bộ budget dùng cho guided touch F1.

Với Q>=2 và cả hai dragon có beast, chia quota gần tỷ lệ số beast:

Plain text
q0 = clamp(
    mulDiv(Q,n0,N),
    max(1,Q-n1),
    min(n0,Q-1)
)
q1 = Q-q0

Nếu Q=1, chọn beast gần caster nhất trên toàn Cast. Nếu chỉ một dragon sở hữu beast, dragon đó nhận toàn bộ quota.

Ngân sách chia theo quota, không chia đôi cố định:

Plain text
B0 = floorDiv(B*q0,Q)
B1 = B-B0

Với B>=2Q, quy tắc này bảo đảm Bdragon >= 2*qdragon.

5.3. Target selection và height-band budget

Mỗi dragon chọn đúng quota:

Beast gần caster nhất.

Các sky-band beasts chưa chọn, gần caster trước.

Các beasts còn lại bằng farthest-first so với tập đã chọn, hòa theo weight giảm dần, rồi ID tăng dần.

Mọi beast F0 đều góp phần xây path, nhưng chỉ selected victims mới nhận damage. Đây là giới hạn ngân sách có chủ đích, không phải thay đổi collider theo lane.

Chia ngân sách mỗi dragon thành ground/sky theo số selected victims:

Plain text
Bsky = floorDiv(Bdragon*skyCount,selectedCount)
Bground = Bdragon-Bsky

Với mỗi band có n>=1 selected victims và ngân sách Bb>=2n:

Plain text
L = max(n,mulDiv(Bb,300,1000))
T = min(Bb-L,max(1,mulDiv(Bb,150,1000)))
C = Bb-L-T

T, C, L lần lượt là touch, corridor và lotus budget. Mỗi band có thể giữ ít nhất 1 HP touch và 1 HP lotus cho mỗi victim về tổng capacity; không dự trữ touch riêng cho từng victim không thể tiếp cận.

5.4. Per-victim falloff và damage commit

Xác định distinctRank tại F0 bằng sort (dist2ToHeart,beastId) trong mỗi dragon. Không thay đổi rank theo thứ tự collider xảy ra.

Plain text
falloffPm = max(400,1000-150*distinctRank)

Dv = mulDiv(20,falloffPm,1000)
Dv = mulDiv(Dv,M_q,1000)
Dv = mulDiv(Dv,seatBucketPm,1000)
Dv = max(2,Dv)   // normal B>=2Q case

Mỗi victim có tổng damage cap Dv riêng và bitmask ba kind. Các kind có request tối đa:

Plain text
touchRequest    = max(1,mulDiv(Dv,150,1000))
corridorRequest = mulDiv(Dv,550,1000)
lotusRequest    = max(1,mulDiv(Dv,300,1000))

Với lotus half region, nhân lotusRequest với 500‰, sau đó giới hạn tối thiểu 1 HP nếu còn lotus budget.

Trước F67, giới hạn tổng damage từ touch+corridor mỗi victim ở Dv-1, để dành chỗ cho ít nhất một lotus hit nếu victim còn sống. Riêng B=1 sử dụng touch toàn phần.

Tại F67 thực hiện hai lượt, đều theo (dist2ToHeart,beastId):

Lượt 1: dành tối đa 1 HP lotus cho từng selected victim còn hợp lệ.

Lượt 2: phân phối phần lotus budget còn lại, không vượt lotusRequest, Dv hay các cap khác.

Nhờ vậy ngân sách touch không bị khóa cho mục tiêu không nằm trong release volume; lotus giữ capacity cho những selected victims còn sống.

Mỗi damage event có điều kiện:

Plain text
eligible =
    selectedVictim
    && hp > 0
    && insideCorrectHeightBand
    && insideActiveCollider
    && !hasHitKind(kind)
    && tick-lastHitTick >= 20

Giá trị effective:

Plain text
effective = min(
    requestedDamage,
    victimHp,
    victimRemainingDamageCap,
    partBudgetRemaining,
    bossCapRemaining,
    swarmClusterCapRemaining
)

Nếu effective>0, cập nhật HP, kind mask, last-hit tick và mọi ledger ngay lập tức. Damage-share ledger nhận đúng effective, không phải requested damage. Posture -20 chỉ áp dụng một lần tại effective hit đầu tiên.

Gom events theo tick, loại trùng (castId,beastId,kind), sort theo (castStartTick,castId,kindPriority,dist2ToHeart,beastId,dragonId) và commit tuần tự. Không thể vừa đọc cùng HP cũ vừa xử lý hai hits từ hai Cast.

Boss cap: 1.5 W trên tổng effective damage của mọi kind, cả hai dragon, cùng castId.

Swarm cap: mỗi Cast có một ledger theo clusterId. Dùng tổng HP cluster theo cơ chế canon s7.2; không suy ra originalClusterTotalHp từ HP hiện tại. Nếu đầu vào F0 không cung cấp được capacity gốc, có thể dùng giới hạn bảo thủ:

Plain text
clusterCap = floorDiv(
    600*sum(currentHpAtF0 of live cluster members),
    1000
)

Giới hạn này không vượt 60% HP gốc của cluster, nhưng có thể thấp hơn canon. Nếu implementation s7.2 yêu cầu đúng HP gốc, phải đọc từ spawn/cluster state hiện hành, không thay bằng giá trị suy đoán.

Trong mọi trường hợp, cả Cast chỉ được tính là một area hit đối với cluster cap.

5.5. Global balance

Target: key2Share <=20% tổng match damage.

1.80 W chỉ là trial starting point. Bản cũ có share 41–50%; ngay cả sweep ngân sách thấp vẫn không đạt cap mà giữ được win rate. Vì vậy bắt buộc chạy đồng thời:

key1Reach: thử 12 → 18 m.

autoAttackReach: thử 10 → 15 m.

Kiểm tra reach của các active skills khác.

Retune auto-attack DPS, wave pacing, spawn pressure và enemy survivability.

Những thay đổi reach ×1.5 có cơ sở thử nghiệm từ dữ liệu chủ game, nhưng chưa phải thông số phát hành.

Owner decision required: ngân sách 1.80 W, quota, damage cap, reach, DPS và pacing. Các quyết định khóa trước — hai rồng, hỏa châu, hoa sen, Fire Sword key-2 và field-wide — không được mở lại.

6. Acceptance và bot plan
6.1. Skill metrics

Metric

	

Exact measurement

	

Target




distinctVictimsP10P90

	

Số F0 beasts nhận effective damage ≥1 HP trong Cast, riêng mẫu 35–45 alive

	

p10 ≥12, p90 ≤20




travelCoverage

	

F0 eligible beasts có live position từng giao active ground/sky corridor, bỏ qua budget, chia số F0 eligible beasts

	

≥85%




lotusAreaCoverage

	

Area của field nằm trong lotus footprint / total field area

	

100%




massBalance

	

min(mass0,mass1)/totalMass

	

≥400‰ trên ≥90% cases có thể chia tương đối cân bằng




firstHit

	

Tick đầu tiên có effective damage

	

≤F2




crowHitRate

	

F0 sky beasts thực sự nhận effective damage / F0 sky beasts

	

≥90% ở peak có 1–3 sky beasts




activeTickP95

	

Wall-clock execution time của mỗi active tick/Cast

	

≤50 µs

travelCoverage được tính trong F3–F47. Không đưa beasts sinh sau F0 vào mẫu số. firstHit loại riêng trường hợp mọi damageable target biến mất trước F2; phải báo số lượng loại, không im lặng bỏ qua.

Các percentile dùng nearest-rank trên tập Cast đủ điều kiện, sort tăng dần. Mỗi metric phải có cả count, mean, median, p10 và p90.

6.2. Full-match metrics

Giữ ngưỡng trong brief:

BALANCE metric

	

Target




Balanced win

	

75–90%




P

	

15–35%




Q

	

50–70%




Typed damage share

	

≥55%




Key-1 share of typed damage

	

≤30%




Key-2 share of total damage

	

≤20%




Auto-attack share

	

12–18%




S, I, O, N

	

Theo BALANCE.md hiện hành

S, I, O, N chưa được định nghĩa trong brief, nên coding agent phải đọc BALANCE.md; không tự đặt ngưỡng.

6.3. Tests

Chạy 17 profiles × 20 seeds × 4 configurations = 1360 matches:

legacy-key2

twin-pearl-v2-only

reach-only

twin-pearl-v2-plus-reach

Peak sweep ở các ticks đông địch nhất từng wave; tách riêng mẫu 35–45 alive. Báo cáo damage theo kind, effective damage, overkill, number of victims, crow hit rate và budget unused.

6.4. Synthetic layouts

Dùng field [-20000,20000] × [-18000,8000] mm, heart=(0,0), caster=(0,3000). Ground y=0, sky y=4000. IDs tăng theo thứ tự tạo; rats cùng clusterId, các beasts khác có ID/cluster riêng.

Layout

	

Fixture




one-gate

	

18 wolves trên lưới 6×3: x=-9000+3600*(i%6), z=-15000+4000*floor(i/6); 7 rats quanh (0,-7500); 2 crows (±14000,-16000)




three-gate

	

3 nhóm ×8 wolves tại (-16000,-15000), (0,-17000), (16000,-15000); offsets (-2700,-1000), (-900,-1000), (900,-1000), (2700,-1000) và cùng bốn x ở z +1000; 3 crows tại ba tâm




open-arena

	

36 wolves lưới 6×6: x=-17500+7000*(i%6), z=-16000+4000*floor(i/6); 4 crows (±18000,-16000) và (±18000,6000)




behind-caster

	

14 wolves: x=-14000+4500*(i%7), z=4500+1500*floor(i/7); 2 crows (±16000,6500)




lone-foe

	

1 ape (13000,4500)




empty-field

	

0 beasts

Rat offsets đúng bảy điểm: (0,0), (500,0), (-500,0), (0,500), (0,-500), (500,500), (-500,-500).

Dùng HP K0: rat 30, wolf 90, crow 72, ape 180. Với fixture, threatW100 lần lượt 33, 100, 80, 200. Không đưa labels A/B/sky vào path builder.

Determinism: replay cùng input và seed trên nhiều JS runtimes phải cùng world hash. Mirror và rotation 180° dùng để so coverage, victim count và effective damage sau ánh xạ tọa độ, không yêu cầu hash của hai layout khác tọa độ giống nhau.

Invariant tests: hit-kind ≤3, re-hit ≥20 ticks, boss cap, cluster cap, part budget, sky/ground separation, two simultaneous Cast ledgers, empty fallback, F0 geometry bounds và full flag-off golden replay.

7. VFX implications

Renderer nhận castId, dragonId, pathSamples, headDistance, phaseFrame, pearlPosition, lotusRadius, petal axes và hit events. Hai rồng dùng body mesh cùng fire trail theo computed paths; không có animation ràng buộc với gate. Pearl xuất hiện tại kiếm khi release rồi được animate tới điểm hội tụ; lotus mở tại F67 và giữ đỉnh trước khi erosion đến F300. Ground/sky visuals có thể khác độ cao nhưng dùng đúng gameplay footprint. Fire look giữ anime/mythic, dark ink backing trên đá sáng, chỉ lõi sáng mảnh dùng bloom mạnh. Asset Firefly/Blender thực hiện sau; code hiện tại chỉ placement và timing.

8. Risks và uncertainty

Risk

	

Verification




Route quá dài, dragon bay khó đọc

	

Đo pathLength, headSpeed, số góc; review 6 layouts




Smoothing/resampling bỏ xa representative

	

Đo min distance của mọi representative tới actual path




Moving foes tránh corridor

	

Đo live-position travelCoverage, không đo trên snapshot




Cluster hoặc path F0 quá nặng

	

Benchmark planning riêng với N=60, hai Cast




Spatial grid quá nhiều candidates

	

Profile candidate count mỗi tick; tối ưu grid nếu activeTickP95 vượt 50 µs




Budget unused vì touch/corridor miss

	

Báo unused budget theo kind; điều chỉnh part ratios qua bot trial




Lotus 1 HP quá yếu

	

Đo lotus effective share, kill distance và áp lực trận




Swarm/boss cap làm first hit thất bại

	

Test target có low HP, cap gần hết và cùng Cast nhiều hits




Skill vẫn >20% tổng damage

	

Tuning cùng reach/DPS/pacing, không giảm footprint hình ảnh




Win rate sụp khi nerf

	

So sánh riêng từng bot, nhất là Kid/New và wave 2




Integer overflow

	

Validate safe integer trước SSE, weighted sums và squared distances




Legacy regression

	

Compare serialized state, RNG use, rules hash và replay byte-for-byte khi flag off

Giới hạn kỹ thuật: với trial hiện tại, yêu cầu các tọa độ field, caster và heart có trị tuyệt đối không quá 100000 mm để các tổng weight×dist2 vẫn nằm trong phạm vi integer an toàn. Map lớn hơn cần mở rộng arithmetic hoặc thêm kiểm chứng riêng; không silently overflow.

Các điểm chưa chắc chắn: budget 1.80 W, quota 12–20, travel coverage ≥85%, tỷ lệ thắng và giới hạn 50 µs chưa được benchmark. Các ngưỡng này là acceptance criteria, không phải kết quả đã đạt. Nếu thử nghiệm thất bại, coding agent phải báo thất bại và số liệu, không tự ý đổi quyết định owner hoặc làm nhỏ field-wide lotus.

Release gate: bật swordKey2: "twin-pearl" mặc định chỉ khi geometry độc lập gate/lane, D58, hit/cap invariants, bot balance và performance đều đạt. rulesHash thêm twin-pearl-v2 trial data chỉ khi flag on; flag off không tạo state mới, không tiêu RNG, không thay serialization hoặc world hash.

Kết luận: Phương án cuối cùng vẫn là Threat-Balanced Twin Coverage + Field-Wide Lotus, nhưng phải dùng pooling theo dragon/height band, lotus reservation, fixed-tick swept segments và ordered damage commits. Đây là đặc tả triển khai thử nghiệm; chỉ kết quả bot và invariant tests mới quyết định có đủ điều kiện phát hành hay không.

---

#### fallback-turn-4:0:user · USER (Claude)

Review your latest full answer above (the corrected full version) against the brief, the facts and the constraints. It FAILS only for a real defect: a wrong fact or source, a step that would not work, a missing step the goal needs, a contradiction with the constraints or the owner's decisions, or a part too vague for a worker to execute. Wording, style and optional extra ideas are not defects.
If it is correct and accurate, answer with exactly one line: VERDICT: PASS (you may add one line "Optional:" with ideas that do not change the verdict)
Otherwise answer: VERDICT: FAIL, then list each defect, then give the corrected FULL analysis and solution (not a diff). If the full version does not fit in one message, stop at a section boundary, end with the line PART 1 OF N, and I will ask for the next part.

---

#### fallback-turn-4:2:assistant · CHATGPT

ChatGPT said:
VERDICT: FAIL

Bản sửa trước đã đáp ứng ý tưởng nghệ thuật và yêu cầu không phụ thuộc cổng, nhưng vẫn có những lỗi thực sự khiến coding agent không thể triển khai chính xác hoặc khiến kết quả không tuân thủ các ràng buộc.

Các lỗi xác nhận được

1. Damage budget vẫn chưa nhất quán. Bản trước nói phải giữ touchBudget ở cấp pool, nhưng đồng thời giữ victimRemainingDamageCap và dự trữ damage cho lotus. Chưa có thuật toán chuyển ngân sách không sử dụng từ touch sang corridor, rồi sang lotus. HP có thể bị khóa và không bao giờ gây sát thương.

2. F0–F2 chưa bảo đảm first hit. Một selected victim có thể không đủ damage allowance, đã chết hoặc bị swarm cap chặn. B=1, B=0 và các nhóm swarm còn rất ít HP cũng chưa được xử lý nhất quán với điều kiện Cast phải có mục tiêu thực sự damageable.

3. Smoothing và sampling vẫn có thể làm mất độ phủ. Resample toàn bộ đường xuống tối đa 2048 điểm có thể đi tắt qua góc hoặc đi xa khỏi representative. Không được dùng một đường đã mất waypoint làm gameplay collider mà không kiểm soát sai số.

4. Thuật toán corridor có điểm mâu thuẫn về thời gian. Đoạn path được mở khi đầu rồng đi qua nhưng có thể được xét như toàn bộ segment ngay tại tick đầu tiên. Một đoạn bị kích hoạt sát F42 cũng chưa có quy tắc rõ ràng để tồn tại đến F47 mà không gây damage sau giới hạn 20 ticks trước lotus.

5. Quy tắc 20 ticks có thể làm giảm corridor damage không dự kiến. Touch F1 và corridor F3 không thể liên tiếp gây damage. Bản trước có trail nhưng chưa định nghĩa chính xác việc xét lại beast đã bị từ chối do cooldown hit.

6. Swarm cap chưa giữ chính xác ngữ nghĩa canon. Bản trước đưa ra hai cách tính khác nhau: tổng HP gốc của cluster và tổng HP hiện tại ở F0. Cách thứ hai là một giới hạn bảo thủ, không được âm thầm xem là tương đương với s7.2.

7. Phân bổ theo ground/sky chưa xử lý đủ các trường hợp biên. Khi một dragon chỉ có sky hoặc ground, khi quota nhỏ, hoặc budget chỉ đủ 1 HP, công thức chia phần có thể khiến một height band không còn ngân sách dù vẫn có selected victims.

8. Giới hạn Dv và part budgets chưa bảo đảm tổng chi không vượt cap. Nếu touchRequest + corridorRequest + lotusRequest > Dv, cần một quy tắc xác định phần nào bị giảm. Không thể dựa vào thứ tự phát sinh event để tự quyết định điều này mà không nói rõ.

9. Mục tiêu hiệu năng chưa có đường thực thi đủ chặt. Giới hạn 2048 samples mỗi dragon không đồng nghĩa với số collision checks hữu hạn nhỏ. Cần tách dữ liệu đường collider khỏi mẫu render và xác định chính xác spatial lookup.

10. Bộ test chưa bao phủ đầy đủ những trường hợp quyết định correctness. Thiếu test cho B=1, cluster cap bằng 0, hai Cast cùng tick, hit vào cuối corridor F47, F67 lotus, chuyển ngân sách và damage cap trên từng beast.

11. Cơ chế xác định damageable chưa chính xác. hp>0 không đủ nếu swarm area cap đã bằng 0. Trường hợp này phải được giải quyết ngay khi quyết định Cast có hợp lệ hay không.

12. Một số thông số trial chưa được xác minh. 1.80 W, số nạn nhân, tỷ lệ crows trúng và mốc 50 µs là giá trị đề xuất hoặc acceptance gates, không phải kết quả đo. Không thể kết luận skill đạt balance nếu chưa chạy bot.

Bản dưới đây thay thế toàn bộ đặc tả trước. Tôi giữ kiến trúc hai rồng quét các nhóm địch, nhưng sử dụng đường collider nguyên bản không bị giảm mẫu và ngân sách ba giai đoạn có chuyển phần dư một chiều để giải quyết những lỗi trên.

## Run 2

Verdicts: FAIL, FAIL, FAIL (dừng)

Page capture: ChatGPT run 2 (brief v2), verbatim page text

Chat URL: https://chatgpt.com/c/6aeac2a8-ac9c-83ec-b446-dbedce5a9d8a
Captured: 2026-11-04T06:23:40.684Z
Units: 8



---

#### fallback-turn-0:0:user · USER (Claude)

Role: you are the game-systems analyst for a browser typing game, "Tu Tien Thu Ai" (a xianxia defence game where every attack comes from typed words). Propose ONE concrete, implementable GEOMETRY design for ONE skill. Write the prose in Vietnamese; keep every name, id, formula and pseudo-code in English. If you need clarifications, ask all of them in one message before you start; otherwise start directly.

SCOPE (read first)
This is a narrowed second brief. A first run that also redesigned the damage machinery failed its self-reviews three times, each time on new budget rules. So the damage machinery below is FIXED: reuse it exactly and do not add mechanisms to it (no per-victim caps, no reserved or transferred budgets, no new part kinds). Only the numbers in its table may change. Your job is the geometry: which foes each dragon takes, where the dragons go, the pearl, the lotus, the hit volumes per tick, and how to test it.

GOAL
Redesign the Sword (Kiem) key-2 skill "Twin Dragons, One Burning Pearl" (id `twin-pearl`, motif 雙龍戲珠) as a FIELD-WIDE, MAP-AGNOSTIC area skill. The owner (04/11/2026) rejected the current version, where each dragon runs up one lane to one of the two gates: "having the 2 dragons run up to the gates is not reasonable, because we are building skills to be shared; later maps will not only face 2 gates, so the skill must work on many maps instead of going to 2 gates; a field-wide area skill makes more sense." Keep two dragons, one burning pearl and the lotus climax. The shape must not depend on the gate count, lane paths, waypoints or flow fields; it covers the field.

FACTS: the engine
- Deterministic lockstep sim, fixed 60 Hz tick, integer-only state. 1 m = 60,000 u. Damage in whole HP; ratios in per-mille. Helpers: mulDiv(a,b,c) (round half up), mulDivSym, isqrt, dist2, within(x,z,cx,cz,r), unitPm(dx,dz,out) (unit vector in per-mille). No float trig or float sqrt in the sim (integer isqrt is fine; a small integer table in content data is fine). Same seed and inputs give the same world hash everywhere. At most 60 live beasts, at most 2 casts alive at once; aim for 50 microseconds or less per tick per cast.
- F0 = the tick the last correct key resolves the Cast; Fn = tick F0+n. D58: the first hit lands by F2 (within 50 ms). Fast attack, slow decay; caster side first.
- Today's only map: a field rectangle x -20..+20 m, z -18..+8 m. Formation centre ("heart") at (0;0); the player stands at (0;+3) (the Cast's origin). Ground gates at (-15;-18) and (+15;-18); crows enter at (+-20;-18) and fly straight to the heart 4 m high at 2 m/s; ground beasts walk to the heart edge (r 2 m) at 1.0-1.6 m/s, height about 0. Peak live counts in waves 5-6: 25-44 (max 52), split roughly half and half between the two ground streams, plus 1-3 crows. Density at peaks: 3.3-4.4 other beasts within 1.5 m of a beast, 5.5-6.7 within 3 m, 7-13 within 6 m. Groups follow each other 2-5 m apart.
- Map-agnostic data the sim has: stage.field bounds (minX, maxX, minZ, maxZ, mm); the heart at the origin; the Cast's origin; each live beast's x, z, y (height), tier (swarm/small/medium/general/boss), threatW100, hp, swarm cluster id, boss flag, slot and serial (a stable id), and a gate label "A" | "B" | "sky" that is map-specific and must not drive the shape. The sim cannot load another map yet (GateId is hard-wired to A/B/sky), but tests can place beasts anywhere with spawnBeast(world, species, gate, {x, z}) and can build a world on a synthetic stage with other field bounds.

FACTS: the FIXED damage machinery (keep exactly)
- One cast = one record: castId, startTick, grade (word quality M_q), baseHp (today's key-2 damage on one beast, 2.5 W = 225 HP at K0), bossCap (1.5 W) and bossDealt, an AreaHit (the whole cast is ONE area hit: a swarm cluster loses at most 60 % of its total HP to it), a victim book, and a pool[side x 4 + part].
- Hit kinds: touch, corridor, lotus, carrying 15 / 45 / 40 % of baseHp x the victim's falloff factor; a lotus hit in the "half" region deals 50 %. mayHit: at most one hit of each kind per beast per cast, at least 20 ticks after its last hit, so at most 3; the boss stops when bossDealt reaches bossCap.
- Sides: each beast belongs to side 0 or side 1 for the whole cast (today sideOf(beast) uses the gate label: this is what you replace). Each side has its own falloff ladder (its n-th distinct victim gets 100 %, -15 % each next, floor 40 %) and its own budget parts: touch, corridor (ground), sky, lotus. Today: 2.5 W per side split 15/45/40 into touch/corridor/lotus, plus 0.8 W per side for sky, all scaled by M_q and the seat's bucket. A hit takes min(its damage, what is left in its side's part); a spent part hits nobody more this cast. Ground volumes (0-1.5 m) hit only ground beasts; sky volumes (2.5-6 m) hit only flyers; a sky-volume hit is kind corridor and spends the side's sky part.
- Each tick: one pass over live, damageable beasts; each beast's first kind it may still take, checked in the order touch, corridor (ground body or sky), lotus; then all candidates are struck in one order: kind, then distance to the heart, then serial. Neither side is favoured by the order volumes are listed in.
- The cast resolves only when a damageable beast is alive.

FACTS: today's geometry (to replace) and its frame map
- F0 hold strike: an 8 x 8 m box in front of the heart towards -z (towards the gates). F1-F2: one touch box (4 x 4.4 m) per lane round that lane's beast nearest the heart. F3-F42: each head runs from the lanes' meeting point (0;-9.25, from the flow field) up its lane to its gate; the path is sampled every 0.5 m with an S offset (sPath: amplitude 0.9 m, half-waves of about 4 m per segment, sin approximated by 4f(1-f)); the head passes sample i at tick pass[i] = 3 + arc_i x 39 / totalArc; the body capsule is r 1.4 m round every sample already passed and passed at most 54 ticks ago (0.9 s trail). F30-F50: each tail sweeps its side's sky route (corner to heart edge), capsule r 2.5 m in the sky band. F43-F50 roar (no new volume). F51-F71: the lotus at the meeting point, r 9 m: full on two long petals (4.4 m wide, 13 m along each head's base path) and in the hold box, half elsewhere. Visuals until F300.
- Measured on today's map with bots (peak sweep, 92 casts at 35-45 alive): 17.2 distinct beasts hit per cast (p10-p90 14-21), 80 % of casts within 12-20; left/right 50/50 median, 92 % within 40/60-60/40; 92 % of live crows hit; first hit F0 or F1. With the budget the damage stops 15-20 m from the heart, and only 26 % of beasts farther than 12 m are hit. Damage by part: hold 10 %, touch 3.5 %, body and trail 41 %, sky 12 %, lotus full 26 %, lotus half 7.4 %.
- Whole-match balance (only for item 6): key 2 deals 41-50 % of all damage (canon caps each area skill at 20 %); bots New->Fast win 95-100 % (target 75-90 %). The budget sweep per side gave: 1.25 W: 11.9 hit, win 0-60 %, share 29-36 %; 2.0 W: 15.2, 45-100 %, 37-45 %; 2.5 W: 17.2, 95-100 %, 41-50 %. Without the dragon, bots win 0-40 %: every other skill's reach is too short (key 1 12 m, auto-attack 10 m).

CONSTRAINTS
- Inputs only: (a) the field bounds, (b) the formation centre and the Cast's origin, (c) live beasts (positions, heights, weights, clusters, crows). No gate labels, lanes, waypoints, flow fields, sky-entry points. The lab may cast on an empty field: the geometry must stay defined (a fallback).
- Read the beasts once, at F0 (a snapshot), unless you show that per-tick reading is needed; store what the cast needs in its record as integers.
- Keep the frame map's spirit: a hit within F0-F2 at the caster side, travel about F3-F42, a sky part, the roar, the lotus at about F51-F71, the trail. Change frame numbers only with a reason.
- Already decided by the owner (do not reopen): two dragons, one burning pearl, the lotus climax; Sword key 2, Fire look; field-wide; map-agnostic; art comes later from art tools, code only places and animates.

DELIVER (numbered, with numbers)
1. The snapshot: exactly what is read at F0 and stored; the empty-field fallback.
2. The side split that replaces sideOf-by-gate: an exact integer rule that gives each dragon about half of the foes (say by what measure), stable under ties, defined for 0, 1 and 2 foes, and the side of a beast that appears after F0.
3. Each dragon's path: weigh at least (a) mirrored spirals or a figure-eight sized from the field bounds, (b) a route through its side's k densest clusters, (c) a sweep of its half; pick one or a hybrid and say why. Give exact integer pseudo-code: clustering (grid size, ranking, ties), the ordering of control points, the start (the caster) and the end (the pearl), clamping to the field bounds, a maximum path length and what happens beyond it, then the reuse of today's sampling (0.5 m samples, S offset, pass[i] mapping onto the travel ticks, the 54-tick trail, r 1.4 m).
4. The sky part for crows without sky routes: exact volume, ticks and how it finds the crows.
5. The pearl's point (formula and clamps) and the lotus: centre, radius, the full and half regions defined without lanes.
6. The F0 strike and the F1-F2 touches without "towards the gates": exact volumes. Show the first hit lands by F2 whenever a damageable beast is alive.
7. Walk-throughs with numbers: today's two-gate map at a peak; a one-gate map (one stream from the top centre); a three-gate map (streams from the left edge, the top centre and the right edge); an open arena with foes on every side; foes only behind the caster; one lone foe; an empty field. For each: the side split, the two paths in words with rough lengths, and why 12-20 distinct beasts are reachable at 35-45 alive.
8. Numbers in the fixed table you would change, if any (radii, trail ticks, budget per side, sky budget), and the key-2 damage-share target: canon caps each area skill at 20 % but bots win only 0-40 % without the skill; recommend a share and a budget, say what else in the game must change, and mark what is the owner's decision. No new mechanisms.
9. The test plan for the coding agent: unit tests with synthetic layouts (exact coordinates, counts, species) for every case of item 7; a rotation and mirror invariance check; determinism (two runs, same hashes; integer-only state); the flag-off check stays. Bot measures on today's map: distinct beasts hit per cast at 35-45 alive (target 12-20, p10-p90), a map-agnostic coverage measure that you define exactly (for example the share of live foes inside any hit volume before the budget), side balance on your new split, first hit by F2, crows hit, and the BALANCE.md metrics (win, S, P, I, O, N, Q, typed share, key-1 share, key-2 share, auto-attack share).
10. One paragraph on what the view needs from the sim to draw two dragons as body and trail along these paths (no art work now).
11. Risks and what you are not sure about.
Keep the whole answer under about 2,000 words; precise beats long.

(The page clipped this bubble to 10250 characters; the text above is the exact brief inserted into the composer and checked equal before sending.)

---

#### fallback-turn-0:2:assistant · CHATGPT

ChatGPT said:
Geometry Design — twin-pearl

Quyết định: Sử dụng Density-Guided Dual Sweep: hai rồng chia quái theo vị trí, ưu tiên quét các cụm đông, sau đó phủ những vùng còn thiếu và cùng hội tụ tại một viên châu. Hoa sen bùng nổ tại viên châu.

Thiết kế không sử dụng GateId, lanes, waypoints hoặc flow fields. Giữ nguyên toàn bộ damage machinery.

1. Snapshot tại F0

Đọc một lần:

stage.field, chuyển từ mm sang u bằng mm * 60.

heart, castOrigin.

Với mỗi quái có hp > 0: serial, slot, x, z, y, threatW100, hp.

Không đọc gate label. Không cần sao chép tier, boss flag hoặc cluster ID vào phần geometry; damage machinery hiện tại tiếp tục sử dụng chúng.

Lưu trong cast: pearl, splitKey, serialSide[], hai controlPoints[], samples[], spatial bins, các điểm touch, sky anchors và hai đoạn đường cuối dài 13 m.

Nếu không có quái: đặt pearl = heart, dựng hai đường quét theo field bounds. Cast thực tế vẫn không được kích hoạt; fallback chỉ phục vụ preview và synthetic tests.

2. Chia hai rồng

Chọn cân bằng theo số quái, không theo HP hoặc threatW100. Điều này bảo đảm hai rồng nhận số mục tiêu gần bằng nhau.

Plain text
U = 60000
f = heart - castOrigin

if f == (0, 0):
    f = (0, -U)

key(b) = (
    cross(f, b.pos - castOrigin),
    dot(f, b.pos - castOrigin),
    b.serial
)

sorted = sort(snapshot, key ASC)
n0 = ceil(n / 2)

side(sorted[0:n0]) = 0
side(sorted[n0:n]) = 1

n=0: hai side rỗng. n=1: một quái thuộc side 0. n=2: mỗi side một quái.

Lưu splitKey = key(sorted[n0]) khi side 1 tồn tại. Nếu chỉ có một quái, dùng (lateral, longitudinal, serial+1) của nó; nếu rỗng, dùng (0,0,0).

Quái xuất hiện sau F0 được gán side bằng phép so sánh key(newBeast) < splitKey. Quái đã nằm trong snapshot luôn dùng serialSide, không tính lại.

Trên bản đồ hôm nay, phép chiếu ngang gần tương đương chia trái/phải. Trên bản đồ xoay 90°, trục chia tự xoay cùng hướng từ caster tới heart.

3. Hai đường bay

So sánh ba phương án:

Phương án

	

Đánh giá




Mirrored spirals / figure-eight

	

Đẹp, dễ dự đoán nhưng lãng phí đường bay ở vùng không có quái




Top-k density route

	

Bắt trúng cụm đông, nhưng bỏ sót vùng trống có quái lẻ




Half-field sweep

	

Phủ sân ổn định, nhưng thiếu ưu tiên tại cụm đe dọa

Chọn hybrid: năm density anchors mỗi side, rồi bổ sung sweep anchors ở những vị trí xa đường hiện tại nhất.

Tạo đường bay

Pearl được tính trước:

𝐶
=
∑
𝑤
𝑖
𝑝
𝑖
∑
𝑤
𝑖
,
𝑃
=
clampField
⁡
(
2
𝐻
+
3
𝐶
5
)
C=
∑w
i
	​

∑w
i
	​

p
i
	​

	​

,P=clampField(
5
2H+3C
	​

)

Trong đó w = clamp(threatW100,1,400), dùng mulDivSym để làm tròn. Nếu rỗng, C=H. Clamp vào field với margin min(0.25m,width/4,depth/4).

Chia sân thành grid 4 m. Mỗi ô tính tổng w của ground beasts thuộc side. Xếp hạng theo sumW DESC, count DESC, gx ASC, gz ASC; chọn tối đa năm ô. Anchor là trọng tâm có trọng số của quái trong ô, được clamp.

Plain text
for side in [0, 1]:
    route = [castOrigin, pearl]

    for anchor in top5DensityCells(side):
        tryInsert(anchor)

    grid = uniformFieldGrid(
        nx=min(8, ceil(width / 6m)),
        nz=min(8, ceil(depth / 6m))
    )

    candidates = grid.centres belonging to side's
                 geometric half-plane through heart

    while candidates not empty:
        q = candidate with maximum distance
            to current route
        tie: gx ASC, gz ASC

        if distance(q, route) <= 3m:
            break

        tryInsert(q)
        remove q from candidates

    generateSamples(route)

tryInsert(q) xét mọi khoảng giữa hai control points, chọn vị trí tăng tổng chiều dài ít nhất, tie theo chỉ số khoảng nhỏ nhất. Chỉ chấp nhận nếu đường sau khi lấy mẫu không vượt Lmax. Nếu không, bỏ anchor đó.

Half-plane sử dụng dấu cross(f,q-heart); điểm nằm đúng đường chia được phân bổ theo parity của grid index.

Giới hạn:

Plain text
fieldDiagonal = isqrt(width² + depth²)
Lmax = 3 * fieldDiagonal

Với bản đồ hôm nay, Lmax ≈ 143.1m mỗi rồng. Nếu offset làm vượt giới hạn, lần lượt bỏ các optional anchors theo thứ tự thêm ngược lại rồi lấy mẫu lại. Đường trực tiếp từ caster đến pearl luôn còn khả thi.

Sampling và trail

Giữ quy tắc hiện tại:

Sample mỗi 0.5 m dọc control polyline.

S-offset tối đa 0.9 m, half-wave dài 4 m, theo 4f(1-f).

Side 0 và side 1 dùng dấu S ngược nhau.

Clamp samples vào field; ép sample đầu và cuối đúng caster và pearl.

Tính lại integer arc length sau S-offset.

Plain text
pass[i] = 3 + mulDiv(arc[i], 39, totalArc)

active(i,t) =
    pass[i] <= t &&
    t <= pass[i] + 54

Ground corridor là union các circle bán kính 1.4 m quanh active samples, áp dụng trong height band 0–1.5 m.

Dùng spatial bins 3 m, đăng ký sample vào mọi bin giao bounding box bán kính 1.4 m. Khi kiểm tra quái, chỉ duyệt sample trong bin tương ứng rồi kiểm tra dist2 chính xác. Không quét toàn bộ route cho từng quái ở mỗi tick.

4. Sky part

Tại F0, lưu vị trí mọi flyer đang sống vào skyAnchors[side].

F30–F50, sky volume gồm:

Các circle bán kính 2.5 m quanh snapshot sky anchors.

Các circle bán kính 2.5 m quanh dragon samples đã được đi qua, chiếu lên mặt phẳng x-z.

Chỉ tác động height band 2.5–6 m. Hit vẫn có kind corridor, tiêu thụ part sky của side tương ứng.

Flyer mới xuất hiện có thể bị trúng projected sweep, nhưng không được bảo đảm nếu ở ngoài đường đã định. Không đọc lại đội hình để đổi đường.

5. Pearl và lotus

Hai rồng bắt buộc tới pearl ở F42; F43–F50 roar, không có hit volume mới.

F51–F71 là lotus, chỉ đánh ground beasts:

Radius ngoài: 9 m.

Full region: disk trung tâm radius 4 m và hai petals.

Mỗi petal là phần đường cuối 13 m của một rồng, có capsule radius 2.2 m, được cắt bởi disk 9 m.

Phần còn lại trong disk 9 m là half region, damage multiplier 50%.

Petals theo đường rồng, không theo gates. Mỗi beast vẫn dùng side cố định và chỉ một lotus hit tối đa.

6. F0–F2: First contact

F0: ground circle radius 4 m tại castOrigin, hit kind touch.

Nếu snapshot không có ground beast trong circle này, tạo một backup circle ngay tại quái snapshot gần caster nhất, tie theo serial:

Ground: radius 1.5 m, kind touch.

Flyer: radius 2.5 m, sky band, kind corridor, tiêu thụ sky.

Backup là một hit volume thuộc kind hiện có, không phải damage mechanism mới. Nó giải quyết trường hợp quái duy nhất ở rất xa hoặc chỉ có crow.

F1–F2: mỗi side có circle radius 1.8 m tại ground beast snapshot gần caster nhất thuộc side đó. Nếu có flyer, thêm sky circle radius 2.5 m tại flyer gần nhất của side.

Tất cả vẫn đi qua candidate ordering và budget machinery cố định.

Bảo đảm first hit: ở F0, nếu có ground beast gần caster thì local circle có mục tiêu; nếu không, backup circle chứa một mục tiêu snapshot. Với valid grade, budget ban đầu dương và ít nhất một quái damageable, F0 có ít nhất một hit. Không phụ thuộc khoảng cách tới gates.

7. Walk-throughs

Các chiều dài dưới đây là ước lượng thiết kế, không phải kết quả benchmark. Giới hạn trên do Lmax bảo đảm.

Layout

	

Split

	

Đường đi và độ dài ước lượng




Two gates, 42 quái

	

21/21

	

Mỗi rồng quét một phía của hai dòng, thêm sweep vùng ngoài, hội tụ giữa sân. ~105–143 m




One gate, top centre

	

21/21

	

Cả hai xuất phát từ caster, chia đôi cụm giữa, sau đó mở rộng sang hai nửa sân. ~90–128 m




Three gates

	

21/21

	

Hai rồng phân chia các cụm trái, giữa, phải theo lateral order, bổ sung sweep ngoài. ~130–167 m




Open arena

	

21/21

	

Hai đường vòng qua các hướng có quái rồi lấp vùng còn thiếu. ~120–153 m




Behind caster

	

21/21

	

Cả hai quay về phía sau, xuyên các density anchors, rồi quét rộng. ~100–143 m




Lone foe

	

1/0

	

Rồng 0 tới mục tiêu; rồng 1 chạy fallback sweep. ~95–143 m




Empty

	

0/0

	

Hai sweep hình học đối ứng, pearl tại heart. ~95–143 m

Với 35–45 quái phân bố thành cụm, hai side có khoảng 18–23 mục tiêu mỗi bên. Density anchors, corridor, sky và lotus tạo cơ hội tiếp xúc rộng hơn đường đi tới gates.

Mục tiêu 12–20 distinct hits là kết quả cần đo, không phải bảo đảm toán học. Coverage hình học có thể đạt hơn 30 mục tiêu trong khi budget chỉ cho phép một phần nhận damage.

8. Damage table và cân bằng

Không thay tỷ lệ 15/45/40, falloff, cooldown, AreaHit, boss cap hoặc hit ordering.

Parameter

	

Đề xuất




Ground budget per side

	

2.0 W (từ 2.5 W)




Sky budget per side

	

0.8 W (giữ)




Ground corridor radius

	

1.4 m




Trail lifetime

	

54 ticks




Sky radius

	

2.5 m




Lotus radius

	

9 m

Chọn 2.0 W vì sweep cũ đo được trung bình 15.2 distinct hits, gần mục tiêu 12–20; 1.25 W chỉ đạt 11.9. Cần benchmark lại trên geometry mới.

Đề xuất mục tiêu dài hạn key-2 share = 18–20%, theo canon. Budget 2.0 W tự nó không đủ: số liệu cũ vẫn cho share 37–45%.

Các skill khác cần tăng khả năng tiếp cận quái: xem xét key 1 từ 12 m lên 16–18 m, auto-attack từ 10 m lên 13–15 m và tăng coverage của những skill còn lại. Sau đó cân chỉnh HP, wave pacing và difficulty để đạt 75–90% bot wins.

Owner decision: duyệt budget 2.0 W, share target và việc rebalance toàn game. Không được tuyên bố đạt 20% trước khi có bot results.

9. Test plan
Synthetic fixtures

Tất cả ground fixtures dùng 40 quái: 32 small, 4 medium, 4 general (i % 10 == 0 là medium, i % 10 == 5 là general). Thêm hai crows ở y=4 m, trừ lone/empty. Gán serial tăng dần. Tọa độ dưới đây tính bằng mét rồi chuyển thành u.

Fixture

	

Field và tọa độ




Two gates

	

[-20,20] × [-18,8]; hai nhóm 20: z=-17+0.9i, x=±15*max(0,-z)/18; crows (±19,-16)




One gate

	

[-16,16] × [-12,16]; i=0..39, x=0.55*(i%5-2), z=15-1.2*floor(i/5); crows (±12,12)




Three gates

	

[-24,24] × [-14,14]; left/right 14 mỗi nhóm: x=±(23-20i/13), z=0.6*(i%3-1); top 12: x=0.35*(2*(i%4)-3), z=13-i; crows (±20,12)




Open arena

	

[-18,18]²; 40 ground tại năm bán kính [4,7,10,13,16], mỗi bán kính dùng tám hướng unit-per-mille gồm cardinal và diagonal (707,707); crows (±15,0)




Behind caster

	

Field hôm nay; x=i%8-3.5, z=4+0.8*floor(i/8); crows (±4,6)




Lone

	

Một medium (18,-16)




Empty

	

Không có quái; gọi geometry builder trực tiếp

Trong fixtures, làm tròn tọa độ bằng mulDivSym; gate label chỉ là tham số bắt buộc của spawnBeast, không được ảnh hưởng geometry.

Assertions và benchmark

sideCount chênh tối đa một với snapshot; test 0/1/2 quái, ties cùng tọa độ, quái spawn sau F0.

First hit ≤F2, kể cả only-flyer, lone far và behind-caster.

Geometry giữ nguyên khi tráo gate labels.

Rotation 90°: biến đổi field, caster và quái; so sánh đường/hit volumes sau phép xoay. Mirror: so sánh coverage và hit counts sau hoán đổi side; cho phép khác ở serial ties và S-wave tại đường clamp.

Hai runs có seed/inputs giống nhau phải có world hashes giống nhau từng tick; mọi state thuộc sim là integer. Test flag-off giữ kết quả baseline byte-for-byte.

Profile F0 build và steady ticks riêng; mục tiêu ≤50 µs/tick/cast, tối đa hai casts.

Định nghĩa:

Plain text
geometryCoverage =
    count(F0 beasts intersecting >=1 eligible
          side-matched hit volume during F0..F71)
    / count(F0 damageable beasts)

Bỏ qua budgets và mayHit khi tính coverage, nhưng dùng vị trí quái thực tại từng tick. New spawns đo riêng.

Acceptance thử nghiệm: coverage ≥90% ở layouts có cụm, ≥80% ở open arena; empty là N/A. Các ngưỡng này là đề xuất, phải xác nhận bằng test.

Trên map hiện tại đo ít nhất 92 casts tại 35–45 live: p10–p90 distinct hits mục tiêu 12–20; side-hit ratio 40/60–60/40 ở ≥90% casts; crow-hit rate ≥92%; first-hit ≤F2. Ghi đầy đủ BALANCE.md: win, S, P, I, O, N, Q, typed share, key-1 share, key-2 share, auto-attack share.

10. Dữ liệu cho view

Sim xuất castId, startTick, pearl, controlPoints[2], samples[2] kèm passTick, trailTicks=54, roar ticks và lotus geometry. View nội suy giữa các samples để dựng đầu, thân và trail của hai rồng; renderer có thể dùng float để vẽ, nhưng không phản hồi vị trí về sim. View tự xử lý body thickness, fade và Fire look về sau.

11. Risks và điểm chưa chắc chắn

Rủi ro chính là coverage ≠ damage: fixed budgets và hit-ordering có thể làm đường rất rộng nhưng không đạt 12 distinct hits. Số liệu 2.0 W từ geometry cũ chỉ là điểm khởi đầu, không chứng minh hiệu quả mới. Một cụm quá tập trung cũng có thể làm nhiều corridor hits tiêu thụ budget trước lotus.

Với sân lớn bất thường, 3 * fieldDiagonal khiến đường dài và lượng samples tăng; cần benchmark F0 và memory. Sky budget 0.8 W có thể hụt nếu nhiều crow cùng side. Cuối cùng, mục tiêu share ≤20% phụ thuộc rebalance toàn game, không thể giải quyết bằng geometry riêng của twin-pearl.

---

#### fallback-turn-1:0:user · USER (Claude)

Review your latest full answer above against the brief, the facts and the constraints. Judge only what the brief asks of you: the damage machinery is fixed and given, so do not redesign it; balance numbers that only the bot can measure are targets, not defects. It FAILS only for a real defect: a wrong fact, a step that would not work, a missing step the goal needs, a contradiction with the constraints or the owner's decisions, or a part too vague for a coding agent to implement. Wording, style and optional extra ideas are not defects.
If it is correct and accurate, answer with exactly one line: VERDICT: PASS (you may add one line "Optional:" with ideas that do not change the verdict)
Otherwise answer: VERDICT: FAIL, then list each defect, then give the corrected FULL analysis and solution (not a diff). If the full version does not fit in one message, stop at a section boundary, end with the line PART 1 OF N, and I will ask for the next part.

---

#### fallback-turn-1:2:assistant · CHATGPT

ChatGPT said:

VERDICT: FAIL

Các lỗi thực sự cần sửa

Side của quái xuất hiện sau F0 không cố định. Công thức key(newBeast) < splitKey được mô tả nhưng không lưu kết quả khi quái xuất hiện. Nếu tính lại theo vị trí mỗi tick, quái có thể đổi side, trái với fixed machinery.

Side split và vùng sweep không nhất quán. Quái được chia theo trung vị vị trí ngang, nhưng sweep lại chia sân theo đường đi qua heart. Khi tất cả quái tập trung về một phía, cả hai rồng nhận quái ở phía đó nhưng một rồng vẫn ưu tiên quét nửa sân không có mục tiêu.

Thuật toán dựng đường chưa đủ để lập trình. tryInsert, khoảng cách tới route, cách tính grid, S-offset và giới hạn chiều dài chưa có quy tắc chính xác cho các trường hợp hòa, từ chối anchor và đoạn đường suy biến.

F0 backup xuất hiện trực tiếp tại quái ở xa mà không có đường hình học nối với caster. Điều này không giữ được ý đồ mở đòn từ phía caster. Cần một volume liên tục từ caster tới mục tiêu khẩn cấp, vẫn sử dụng hit kind hiện có.

Sky volumes có thể tách rời hoàn toàn khỏi hai con rồng. Các circle cố định tại vị trí crow snapshot chưa chỉ rõ cách đuôi rồng tới được các vùng đó. Cần một phép quét liên tục nối thân/đuôi rồng với crow anchors, không phụ thuộc sky routes.

Kiểm thử rotation/mirror chưa tương thích với thuật toán. Grid gắn vào world X/Z cùng tie-break gx, gz không bảo toàn hình học khi xoay hoặc phản chiếu. Cho phép sai khác tùy ý cũng làm phép kiểm tra invariance mất ý nghĩa.

Coverage metric chưa tách tác động của damage khỏi hình học. Khi một quái bị giết sớm, việc chỉ xét quái còn sống ở các tick sau làm kết quả phụ thuộc budget. Cần phép đo độc lập với damage.

Các lỗi trên đều thuộc geometry hoặc khả năng triển khai. Không cần thêm damage mechanism mới và không coi các mục tiêu balance chưa được benchmark là lỗi.

Corrected full design — twin-pearl

Chọn Balanced Density-Guided Dual Sweep. Hai rồng chia đều số quái có mặt tại F0, ưu tiên các cụm đông, quét bổ sung vùng chưa phủ và cùng hội tụ vào pearl. Các tác động sử dụng duy nhất touch, corridor, lotus và bốn budget parts hiện có.

1. Snapshot và fallback

Tại F0, đọc và lưu:

fieldBounds (mm → u bằng nhân 60), heart, castOrigin.

Mỗi quái hp > 0: serial, slot, x, z, y, hp, threatW100.

Kết quả phân side, pearl, controlPoints, samples, passTicks, skyAnchors, touchAnchors.

Không lưu hoặc sử dụng GateId, lanes, flow fields.

Việc đọc vị trí quái hiện tại mỗi tick để kiểm tra collision vẫn cần thiết; đây chính là live-beast pass thuộc fixed damage machinery, không phải lấy lại snapshot để dựng đường.

Nếu F0 không có quái: pearl=heart, sideCount=[0,0], hai đường fallback quét hai nửa field. Geometry builder vẫn chạy được trong lab; production không tạo cast.

2. Side split

Đo bằng số quái, bao gồm ground và flyers; mỗi side có chênh lệch tối đa một quái trong snapshot.

Dùng hệ tọa độ theo hướng từ caster tới heart:

Plain text
U = 60000
PM = 1000

F = unitPm(heart - castOrigin)
if heart == castOrigin:
    F = (0, -1000)

R = (-F.z, F.x)

v(p) = mulDivSym(dot(p - heart, R), 1, PM)
u(p) = mulDivSym(dot(p - heart, F), 1, PM)

key(b) = (v(b), u(b), b.serial)

sorted = sort(snapshot, key ASC)
n0 = (n + 1) // 2

side(sorted[0:n0]) = 0
side(sorted[n0:n]) = 1

Các phép dot và cross sử dụng integer signed 64-bit trong phạm vi tọa độ stage được engine hỗ trợ.

Lưu pivot=key(sorted[n0-1]). Khi quái mới xuất hiện:

Plain text
if serial not in serialSide:
    serialSide[serial] = 0 if key(beast) <= pivot else 1

Kết quả được lưu vĩnh viễn cho cast đó, kể cả khi quái di chuyển.

Với n=0, chỉ dùng fallback v<0 → side0, còn lại side1; không có cast thật. Với n=1: 1/0. Với n=2: 1/1.

Để chia vùng sweep, dùng vCut là trung bình có dấu của hai giá trị v ở giữa khi n>=2; với n=1, dùng v của quái duy nhất; với n=0, dùng 0. Vùng side0 có v<=vCut, side1 có v>=vCut. Các ô trên biên có thể được cả hai rồng quét.

Như vậy, vùng quét thích nghi với phân bố quái, không bị cố định tại hai nửa trái/phải của heart.

3. Path của hai rồng

Chọn hybrid Top-5 Density + Farthest-Uncovered Sweep.

Pearl
Plain text
w(b) = clamp(b.threatW100, 1, 400)

C = weightedCentroid(snapshot, w)
if snapshot empty:
    C = heart

pearl = clampToInsetField(
    heart + mulDivSym(C - heart, 3, 5),
    inset = min(0.25m, width/4, depth/4)
)

Áp dụng mulDivSym riêng cho hai trục. Cũng clamp heart, castOrigin theo yêu cầu hợp lệ của stage; production phải xác nhận caster nằm trong field.

Density grid

Chuyển bốn góc field sang (v,u) và lấy localAABB.

Grid có kích thước ô danh nghĩa tối đa 4 m:

Plain text
Nv = max(1, ceilDiv(vMax-vMin, 4*U))
Nu = max(1, ceilDiv(uMax-uMin, 4*U))

gv = min(Nv-1, floor((v-vMin)*Nv/(vMax-vMin)))
gu = min(Nu-1, floor((u-uMin)*Nu/(uMax-uMin)))

Nếu span bằng 0, index bằng 0. Sử dụng integer floor và clamp.

Với mỗi side, ground beasts được gom theo cell. Rank:

sumThreat DESC, count DESC, minSerial ASC.

Chọn tối đa năm cell có quái. Anchor là weighted centroid của các quái thuộc side trong cell, clamp vào field.

Sweep và thứ tự control points

Tạo grid thứ hai với ô danh nghĩa 6 m, tối đa 8 ô mỗi chiều, trong cùng local frame. Biến đổi các cell centres về world coordinates, clamp vào field, bỏ tọa độ trùng.

Chỉ lấy candidates thuộc nửa field tương ứng với vCut.

Plain text
route = [castOrigin, pearl]

for q in top5DensityAnchors:
    tryInsert(q)

while sweepCandidates not empty:
    q = argmax(
        distanceSqToPolyline(candidate, route),
        tie: distanceSq(candidate, castOrigin) ASC,
             localU(candidate) ASC,
             sideOutward(candidate) ASC
    )

    if distanceSqToPolyline(q, route) <= (3*U)^2:
        break

    tryInsert(q)
    remove q from sweepCandidates

Trong đó sideOutward(q) là vCut-v(q) cho side0 và v(q)-vCut cho side1.

distanceSqToPolyline dùng projection integer của điểm lên từng segment, clamp tham số vào [0,1000], rồi lấy khoảng cách bình phương nhỏ nhất.

tryInsert(q) chèn vào segment gây tăng chiều dài thấp nhất:

Plain text
delta(i) =
    dist(route[i],q)
  + dist(q,route[i+1])
  - dist(route[i],route[i+1])

insertAt = argmin(delta(i), i ASC)

if newPolylineLength <= Lmax:
    insert(q, insertAt)
    markOptional(q)

Khoảng cách là isqrt(dx²+dz²); tất cả phép chia có dấu dùng mulDivSym.

Sampling, S-offset và giới hạn
Plain text
Lmax = 3 * isqrt(width² + depth²)
step = 0.5 * U
halfWave = 4 * U
amplitude = 0.9 * U

Lấy sample mỗi 0.5 m theo cumulative arc của control polyline, bao gồm hai endpoint.

Với sample thuộc segment có unit tangent (tx,tz):

Plain text
phase = segmentArc % halfWave
wave = mulDiv(
    amplitude,
    4 * phase * (halfWave-phase),
    halfWave * halfWave
)

sign = (-1)^(floor(segmentArc / halfWave) + side)

offset = sign * wave * (-tz, tx) / PM
sample = clampToField(baseSample + offset)

Sử dụng integer operations; giữ sample đầu chính xác tại caster và sample cuối chính xác tại pearl.

Tính lại sampleArc sau offset. Nếu chiều dài vượt Lmax, xóa optional anchor được thêm gần nhất, xây lại samples và lặp. Đường thẳng caster→pearl luôn được giữ.

Plain text
pass[i] = 3 + mulDiv(sampleArc[i], 39, totalArc)

active(i,t) =
    pass[i] <= t &&
    t - pass[i] <= 54

Trường hợp totalArc=0, tất cả samples có pass=3.

Ground body/trail là hợp các disk radius 1.4 m quanh active samples, height band 0–1.5 m.

Spatial bins 3 m đăng ký trước các sample theo bounding box radius 1.4 m. Mỗi tick, collision query chỉ kiểm tra các sample trong bin của quái và các bin giao nhau tương ứng; xác nhận bằng dist2.

Frame map giữ nguyên: travel F3–F42, roar F43–F50, trail tồn tại tối đa 54 ticks sau mỗi sample.

4. Sky part

Tại F0, lưu từng crow dưới dạng skyAnchor=(x,z,serial,side).

Trong F30–F50:

Plain text
head(t) = latest sample with pass <= min(t,42)

for each skyAnchor a of side:
    skyVolume = capsule(
        head(t), a.position, radius=2.5m
    )

Volume được chiếu trong x-z và chỉ tác động height band 2.5–6 m. Đây là các đường nối liên tục từ rồng tới crow anchors, không phải sky routes lấy từ map.

Mọi hit dùng kind corridor, tiêu thụ side's existing sky budget. Quái mới vẫn có thể đi vào capsule và bị đánh trúng.

Với crow di chuyển 2 m/s, từ F0 đến F50 nó đi tối đa khoảng 1.67 m, nhỏ hơn radius 2.5 m nếu bay theo tốc độ đã nêu. Vì vậy anchor snapshot vẫn có khả năng bao phủ vị trí crow.

5. Lotus

F51–F71, tại pearl:

Disk radius 9 m.

Full disk radius 4 m.

Hai full petals là capsule radius 2.2 m quanh đoạn cuối dài 13 m của từng dragon path, cắt bởi disk 9 m.

Half region là phần còn lại bên trong disk 9 m.

Plain text
if dist2(beast, pearl) > (9*U)^2:
    no lotus

else if dist2(beast, pearl) <= (4*U)^2
     or distanceToEitherFinalPath(beast) <= 2.2*U:
    lotusFull

else:
    lotusHalf

Chỉ ground beasts. Vẫn một lotus kind, một lần tối đa cho mỗi victim; half multiplier giữ 50%.

6. F0 strike và F1–F2 touches

F0 tạo ground disk radius 4 m quanh caster, kind touch.

Để bảo đảm có contact ngay khi không có ground beast trong disk, tạo thêm một guided ray liên tục từ caster đến quái damageable gần nhất trong snapshot (tie bằng serial).

Nếu target là ground: capsule radius 0.5 m, endpoint disk radius 1.5 m, kind touch.

Nếu target là flyer: cùng capsule projected vào sky band, endpoint disk radius 2.5 m, kind corridor, dùng sky part.

Không tạo hit kind hay budget mới. Ray bắt đầu tại caster, thay vì sinh một hit volume rời rạc ở xa.

F1–F2: mỗi side có ground touch disk radius 1.8 m quanh ground beast snapshot gần caster nhất; nếu có crow, thêm sky corridor disk radius 2.5 m quanh crow gần nhất.

Tất cả đi qua fixed mayHit, candidate sorting và budgets.

Chứng minh first hit: tại F0, nếu có ground beast trong local disk, nó nằm trong touch volume. Nếu không, guided ray chứa chính mục tiêu F0 ở endpoint. Với một cast hợp lệ, positive budget và ít nhất một damageable beast thuộc các ground/sky height bands được engine hỗ trợ, có first hit tại F0, do đó đạt D58.

Nếu engine cho phép quái damageable ở khoảng cao 1.5–2.5 m hoặc ngoài 6 m, fixed height bands không thể bảo đảm hit; cần coi đó là unsupported input trong test, không tự sửa damage machinery.

7. Walk-throughs

Dùng 40 ground + 2 crows cho năm bố cục nhiều quái. Split luôn là 21/21 theo count.

Map

	

Đường đi dự kiến




Two gates, 40×26 m

	

Một rồng ưu tiên cụm trái, rồng kia cụm phải, sau đó bổ sung các cell xa route rồi về pearl gần giữa sân. Khoảng 105–143 m/rồng




One gate, 32×28 m

	

Mỗi rồng nhận một nửa đoàn quái từ top centre, tách ra hai phía để sweep, sau đó quay lại pearl phía trên heart. Khoảng 90–128 m




Three gates, 48×28 m

	

Cụm giữa được chia theo lateral rank; hai dòng bên được phân cho các side phù hợp. Mỗi rồng sweep vùng riêng rồi hội tụ. Khoảng 130–167 m




Open arena, 36×36 m

	

Hai rồng quét các điểm mật độ cao trong hai nửa phân bố, thêm các cung ở rìa sân và trở về giữa. Khoảng 120–153 m




Behind caster, 40×26 m

	

Hai rồng quay ngược hướng heart, đi xuyên các cụm phía sau caster, sau đó mở rộng sweep. Khoảng 100–143 m




Lone foe (18,-16)

	

1/0. Rồng 0 đi qua density anchor của mục tiêu; rồng 1 dùng fallback sweep. Guided ray bảo đảm first hit




Empty

	

0/0. Hai fallback sweeps, pearl=heart; không phát sinh cast

Các con số chiều dài là phạm vi ước lượng, bị chặn bởi Lmax, chưa phải kết quả thực thi thuật toán.

Với 35–45 live, density routing ưu tiên tiếp xúc các quái thực tế trước khi dùng chiều dài còn lại quét vùng trống. Vì vậy 12–20 distinct hits là mục tiêu hợp lý để kiểm chứng, nhưng không được bảo đảm chỉ bằng geometry: fixed budgets có thể hết trước khi các volume tiếp xúc hết mục tiêu.

8. Fixed table và balance

Không sửa AreaHit, mayHit, victim falloff, boss cap, candidate order hoặc part allocation logic.

Parameter

	

Proposed




Ground side budget

	

2.0 W




Touch / corridor / lotus allocation

	

15 / 45 / 40%




Sky side budget

	

0.8 W




Ground corridor radius

	

1.4 m




Trail

	

54 ticks




Sky radius

	

2.5 m




Lotus radius

	

9 m

Với 2.0 W, các ground parts có budget danh nghĩa tương ứng 0.30 W / 0.90 W / 0.80 W mỗi side, trước các phép scale cố định.

Đề xuất key-2 damage share 18–20%. Đây là mục tiêu balance, không phải dự đoán từ geometry.

Muốn giữ bot win 75–90%, cần tăng reach của các nguồn damage khác; thử key 1 từ 12 lên 16–18 m và auto-attack từ 10 lên 13–15 m, rồi điều chỉnh HP/wave pacing sau benchmark. Đây là thay đổi ở các hệ thống khác, không thuộc geometry của twin-pearl.

Owner decision: duyệt ground budget 2.0 W, share 18–20% và phạm vi rebalance toàn game.

9. Test plan cho coding agent
Synthetic fixtures

Dùng U=60000. Mỗi fixture nhiều quái gồm 40 ground (8 swarm, 24 small, 4 medium, 4 general theo thứ tự index) và hai crows ở y=4m. Dùng species IDs có sẵn của test registry; gate argument có thể là "A" cho toàn bộ quái vì geometry phải bỏ qua nó.

Fixture

	

Tọa độ chính xác bằng mét




Two gates

	

Field [-20,20]×[-18,8]. Mỗi bên 20 quái i=0..19: z=-17+0.9i, x=±(0.4+14.6*max(0,-z)/18). Crows (±19,-16)




One gate

	

Field [-16,16]×[-12,16]. i=0..39: x=0.55*(i%5-2), z=15-1.2*floor(i/5). Crows (±12,12)




Three gates

	

Field [-24,24]×[-14,14]. Left/right 14 mỗi bên: x=±(23-20i/13), z=0.6*(i%3-1); top 12: x=0.35*(2*(i%4)-3), z=13-i. Crows (±20,12)




Open arena

	

Field [-18,18]². Tám hướng unit-per-mille (±1000,0), (0,±1000), (±707,±707) tại năm bán kính [4,7,10,13,16] m. Crows (±15,0)




Behind caster

	

Field hôm nay. i=0..39: x=(2*(i%8)-7)/2, z=4+0.8*floor(i/8). Crows (±4,6)




Lone

	

Field hôm nay; một medium (18,-16)




Empty

	

Field hôm nay; không spawn quái

Tất cả phép tạo tọa độ dùng integer rational và mulDivSym, không dùng float trong sim.

Assertions

Kiểm tra:

Split chính xác 0/0, 1/0, 1/1 và chênh tối đa một; test nhiều quái cùng tọa độ và serial khác nhau.

Late-spawn side được lưu ngay lần đầu, không đổi khi quái di chuyển.

Không truy cập GateId hoặc dữ liệu route của map; thay mọi gate label không làm đổi geometry hash.

F0 hit trong mọi fixture không rỗng; riêng only-crow và lone-far phải kiểm chứng guided ray.

controlPoints và samples nằm trong field, sample đầu/cuối chính xác, totalArc ≤Lmax, pass ticks đúng F3–F42.

Hai lần chạy cùng seed/inputs có world hash giống nhau từng tick. Kiểm tra không có float state/trig/sqrt trong sim.

Flag-off giữ nguyên baseline hashes, wins và damage breakdown.

Rotation/mirror

Xoay toàn bộ field, caster và beasts 90° quanh heart; so sánh geometry sau phép xoay ngược.

Mirror theo trục x, so sánh sau khi hoán đổi side 0/1. Dùng fixtures có số quái chẵn và không có lateral ties tại trung vị để kiểm tra hoán đổi side chính xác. Kiểm tra ties và số lẻ riêng theo quy tắc serial, không áp đặt hoán đổi không thể thỏa mãn.

So sánh endpoints, hit-volume intersection sets và coverage; cho phép sai lệch tọa độ tối đa do integer rounding, không cho phép sai khác hit set nếu test points cách biên volume ít nhất 0.05 m.

Coverage metric

Đo độc lập với damage:

Plain text
coverage0 =
  F0 snapshot beasts whose frozen F0 positions
  intersect at least one side-matched volume
  during F0..F71
  /
  eligible F0 snapshot beasts

Dùng toàn bộ geometry theo frame nhưng không áp dụng damage, cooldown hoặc budget. Quái được kiểm tra tại vị trí F0 cố định nên death/despawn không làm sai metric. Đo thêm movingContactRate trong actual simulation để thấy ảnh hưởng chuyển động.

Targets thử nghiệm: clustered fixtures ≥90%, open arena ≥80%; lone =100%, empty=N/A.

Với map hiện tại, chạy ≥92 casts trong điều kiện 35–45 live, ghi:

Distinct hits p10–p90: target 12–20.

Side-hit ratio 40/60–60/40 ở ≥90% casts.

Crow-hit rate ≥92%, first hit ≤F2.

geometryCoverage, movingContactRate, per-part damage, elapsed CPU time và peak memory.

Toàn bộ metrics BALANCE.md: win, S, P, I, O, N, Q, typed share, key-1 share, key-2 share, auto-attack share.

Benchmark F0 construction riêng với steady-state tick. Mục tiêu steady-state ≤50 µs/cast/tick, kể cả khi hai casts cùng tồn tại.

10. View contract

Sim xuất castId, startTick, pearl, hai arrays samples[], passTick[], trailLifetime=54, sky anchor data, cùng roarStart=43, roarEnd=50, lotusStart=51, lotusEnd=71. View dựng head ở sample đã đi qua, nối các samples còn active thành thân/đuôi, vẽ sky tethers và lotus bằng interpolation tùy ý. Renderer có thể dùng float nhưng tuyệt đối không đưa dữ liệu hình ảnh ngược vào deterministic sim.

11. Risks và uncertainties

Rủi ro lớn nhất là Lmax và số anchors trên field lớn: phần sweep có thể bỏ những cell xa khi chiều dài hết, khiến coverage giảm. Rủi ro thứ hai là ground budget hết sớm ở cụm gần caster dù hình học phủ rộng. Hai hiện tượng cần được phân biệt bằng coverage0 và distinct hits. Spatial bins, số samples và F0 path construction cần profiling trên browser mục tiêu.

Việc crow tại F50 còn nằm trong radius 2.5 m dựa trên tốc độ 2 m/s được cung cấp; nếu species khác nhanh hơn, cần benchmark lại sky contact. Không thể bảo đảm hitting đối tượng ở height band không được engine hỗ trợ.

Phần geometry có thể triển khai và kiểm thử độc lập. Các ngưỡng hit, win và damage share vẫn là acceptance targets cần xác nhận bằng bot, không phải kết quả đã đo.

---

#### fallback-turn-2:0:user · USER (Claude)

Review your latest full answer above (the corrected full version) against the brief, the facts and the constraints. Judge only what the brief asks of you: the damage machinery is fixed and given, so do not redesign it; balance numbers that only the bot can measure are targets, not defects. It FAILS only for a real defect: a wrong fact, a step that would not work, a missing step the goal needs, a contradiction with the constraints or the owner's decisions, or a part too vague for a coding agent to implement. Wording, style and optional extra ideas are not defects.
If it is correct and accurate, answer with exactly one line: VERDICT: PASS (you may add one line "Optional:" with ideas that do not change the verdict)
Otherwise answer: VERDICT: FAIL, then list each defect, then give the corrected FULL analysis and solution (not a diff). If the full version does not fit in one message, stop at a section boundary, end with the line PART 1 OF N, and I will ask for the next part.

---

#### fallback-turn-2:2:assistant · CHATGPT

ChatGPT said:

VERDICT: FAIL

Các lỗi cần sửa

Chưa xác định chính xác tập quái hợp lệ tại F0. Bản trước dùng hp > 0 làm điều kiện chọn snapshot và mục tiêu cứu hộ. Trong khi đó, yêu cầu D58 áp dụng cho damageable beasts. Nếu engine có quái còn HP nhưng không thể nhận damage tại tick đó, fallback có thể chọn sai mục tiêu và không bảo đảm first hit.

Thuật toán S-offset chưa hoàn toàn xác định. segmentArc không nói rõ là chiều dài tính từ đầu toàn route hay đầu từng segment. Điều này làm phase, dấu uốn và các sample khác nhau giữa hai cách triển khai. Quy trình tính lại path length sau clipping cũng cần một thứ tự cố định.

Sky-anchor selection và collision chưa đủ chính xác. Bản trước nói lưu crow anchors nhưng snapshot không lưu species hoặc flyer flag, cũng không định nghĩa điều kiện chọn bằng height band. Với 60 live beasts, phải xác định rõ cách kiểm tra nhiều sky capsules mà không vô tình thay đổi candidate ordering của fixed machinery.

Fixture cho crow dùng gate "A" chưa được bảo đảm hợp lệ. Không sử dụng GateId để định hình skill không có nghĩa là có thể thay gate argument tùy ý khi gọi spawnBeast. Test nên dùng "sky" cho crow, sau đó kiểm tra gate-label independence bằng các trường hợp mà spawn API cho phép.

Điều kiện rotation/mirror cần được đưa vào quy tắc tạo geometry, không chỉ trong test. Cụ thể, integer rounding, thứ tự hòa khi chọn sweep cells và việc đổi dấu S-offset khi hoán đổi side phải được quy định thống nhất. Nếu không, coding agent có thể tạo hai implementations hợp với mô tả nhưng cho các hit volumes khác nhau.

Đây là lỗi thực thi/đặc tả geometry và test, không phải lỗi của damage machinery hoặc mục tiêu balance chưa đo.

Corrected full design — twin-pearl
1. Snapshot tại F0

Đơn vị: U=60000, PM=1000; tất cả tọa độ sim là integer u.

Lưu fieldBounds, heart, castOrigin và danh sách quái còn sống tại F0 gồm serial, slot, x, z, y, hp, threatW100, damageableAtF0.

damageableAtF0 dùng cùng predicate hợp lệ mà fixed hit pipeline sử dụng, không suy đoán từ hp. Chỉ quái damageable được đưa vào danh sách chia side và định tuyến; những quái khác vẫn do live hit pipeline xử lý sau này nếu trở nên damageable.

Lưu thêm serialSide, splitPivot, vCut, pearl, controls[2], samples[2], passTicks[2], touchAnchors, skyAnchors, finalPath[2].

Đọc vị trí quái hiện tại mỗi tick chỉ để kiểm tra hit volumes trong live-beast pass vốn có. Không tính lại paths.

Empty fallback: pearl=heart, vCut=0, hai density lists rỗng, hai field sweeps được tạo bằng cùng thuật toán. Production không tạo cast nếu không có damageable beast.

2. Side split

Chia theo count của damageable F0 beasts, mỗi side chênh lệch tối đa một.

Plain text
F = unitPm(heart - castOrigin)
if F == (0,0): F = (0,-1000)
R = (-F.z,F.x)

v(p) = mulDivSym(dot(p-heart,R),1,PM)
u(p) = mulDivSym(dot(p-heart,F),1,PM)

key(b) = (v(b),u(b),b.serial)
B = sort(snapshotDamageable,key ASC)

n0 = (len(B)+1)//2
assign B[0:n0] to side 0
assign B[n0:] to side 1

n=0: 0/0, vCut=0, không có pivot.

n=1: 1/0, vCut=v(B[0]).

n>=2: vCut=mulDivSym(v(B[n0-1])+v(B[n0]),1,2).

splitPivot=key(B[n0-1]) nếu n>0.

Với late-spawn, khi quái lần đầu được kiểm tra bởi cast:

Plain text
if serial not in serialSide:
    if snapshotCount == 0:
        side = 0 if v(beast) < 0 else 1
    else:
        side = 0 if key(beast) <= splitPivot else 1
    serialSide[serial] = side

Không bao giờ cập nhật side của cùng serial. Serial phải duy nhất trong vòng đời cast.

3. Hai dragon paths

Chọn Density-Guided Dual Sweep, kết hợp ưu điểm của ba phương án:

Mirrored Spiral: phủ đều nhưng mất quãng đường ở vùng trống.

Top-k Clusters: đánh cụm tốt, nhưng không phủ sân.

Half Sweep: phủ sân tốt, nhưng không ưu tiên mật độ.

Hybrid đi qua tối đa năm density anchors, sau đó dùng phần chiều dài còn lại để quét vùng xa route nhất.

Pearl
Plain text
w(b) = clamp(b.threatW100,1,400)
C.x = roundSym(sum(w*x)/sum(w))
C.z = roundSym(sum(w*z)/sum(w))
if snapshot empty: C=heart

pearl = heart + mulDivSym(C-heart,3,5)
pearl = clampToInsetField(pearl,inset)
inset = min(0.25*U,width/4,depth/4)

Các phép chia được áp dụng riêng cho x/z. Dùng integer arithmetic với kiểm tra overflow.

Density anchors

Biến đổi bốn góc field vào local (v,u), lấy localAABB. Chia thành grid với mỗi chiều ô tối đa 4 m:

Plain text
Nv = max(1,ceilDiv(vMax-vMin,4*U))
Nu = max(1,ceilDiv(uMax-uMin,4*U))

cellIndex(a,minA,maxA,N):
    if maxA == minA: return 0
    return clamp(
        floorDiv((a-minA)*N,maxA-minA),
        0,N-1
    )

Mỗi quái ground thuộc side của nó; ground là 0<=y<=1.5U. Mỗi cell có count, sumW, weightedCentroid, minSerial.

Rank: sumW DESC, count DESC, minSerial ASC. Chọn năm cell đầu tiên mỗi side; centroid được clamp vào field.

Sweep anchors và ordering

Grid thứ hai có ô tối đa 6 m, tối đa tám ô mỗi chiều. Cell centres biến đổi về world coordinates rồi clamp. Loại trùng theo tọa độ.

Side 0 chọn centres có v<=vCut, side 1 chọn v>=vCut.

Plain text
route = [castOrigin,pearl]
accepted = []

for q in top5DensityAnchors:
    tryInsert(q)

while sweepCandidates not empty:
    q = argmax(
        distanceSqToPolyline(q,route),
        tie: u(q) ASC,
             outward(q) ASC,
             stableCellId ASC
    )

    if distanceSqToPolyline(q,route) <= (3*U)^2:
        break

    tryInsert(q)
    remove q

Trong đó outward=vCut-v cho side 0, outward=v-vCut cho side 1. stableCellId là (localUIndex, sideOutwardIndex), không phải world X/Z index.

distanceSqToPolyline dùng nearest-point projection lên từng segment, tham số integer 0–1,000,000; tie bằng segment index nhỏ nhất.

tryInsert(q) chọn insertion gap có tăng integer polyline length nhỏ nhất, tie bằng gap index. Nếu path length vượt Lmax, từ chối.

Plain text
Lmax = 3*isqrt(width*width+depth*depth)

Không được bỏ castOrigin hoặc pearl.

Sampling và S-offset

Lấy base samples mỗi 0.5 m theo tổng chiều dài của control polyline.

arcBase luôn là cumulative arc từ đầu toàn route, không reset ở control point.

Plain text
halfWave = 4*U
A = 0.9*U

phase = arcBase % halfWave
wave = mulDiv(
    A,
    4*phase*(halfWave-phase),
    halfWave*halfWave
)

cycle = floorDiv(arcBase,halfWave)
sign = +1 if (cycle+side)%2 == 0 else -1

tangent = direction of current base segment
normal = (-tangent.z,tangent.x)

sample = base + sign*wave*normal/PM
sample = clampToField(sample)

Dùng mulDivSym cho offset có dấu. Tại đúng control point, dùng tangent của outgoing segment; ở endpoint cuối dùng incoming segment. Ép sample đầu bằng castOrigin, sample cuối bằng pearl.

Tính totalArc lại từ các samples đã clamp. Nếu vượt Lmax, xóa anchor tùy chọn được chấp nhận sau cùng và dựng lại toàn bộ sample list. Lặp đến hợp lệ. Đường trực tiếp caster→pearl là fallback cuối cùng.

Plain text
pass[i] = 3+mulDiv(sampleArc[i],39,totalArc)

active(i,t) =
    pass[i]<=t && t<=pass[i]+54

Nếu totalArc=0, tất cả pass=3.

Ground corridor F3 onward là union của các disk bán kính 1.4 m quanh active samples, height 0–1.5 m. Trail tồn tại 54 ticks sau khi head đi qua sample.

Dùng spatial bins 3 m để truy vấn samples; một sample được index vào mọi bin giao bounding box radius 1.4 m. Kiểm tra cuối bằng integer dist2.

4. Sky part

Chọn skyAnchors tại F0 bằng điều kiện:

Plain text
2.5*U <= y <= 6*U

Không dùng GateId để nhận diện flyer.

F30–F50, mỗi side có sky corridor là union của:

Capsule từ headPosition(side,t) đến từng skyAnchor thuộc side, radius 2.5 m.

Disk radius 2.5 m quanh các active dragon samples, chiếu lên sky band.

headPosition là sample cuối có passTick<=min(t,42). Các capsule liên tục nối đầu rồng với vị trí crow snapshot. Không dùng sky-entry points.

Collision sử dụng point-to-segment squared distance, không dùng float sqrt. Với mỗi beast, chỉ trả một boolean cho sky corridor union; fixed machinery vẫn tạo tối đa một candidate kind corridor cho beast đó.

Có thể kiểm tra tối đa 60 anchors, nhưng cần profile trường hợp toàn flyer. Nếu vượt 50 µs/tick, index bounding boxes của sky capsules vào spatial bins; không bỏ anchors hoặc thay đổi hit ordering.

Sky hit dùng part sky, giữ nguyên fixed budget và mayHit.

5. Lotus và burning pearl

Pearl đặt tại pearl đã tính ở mục 3. Hai dragon heads kết thúc tại đây ở F42; F43–F50 roar, không tạo hit volume mới.

F51–F71:

Region

	

Geometry

	

Damage




Full core

	

Disk radius 4 m tại pearl

	

100% lotus




Full petals

	

Capsule radius 2.2 m quanh 13 m cuối của mỗi path, cắt bởi disk radius 9 m

	

100% lotus




Half

	

Phần còn lại trong disk radius 9 m

	

50% lotus




Outside

	

Ngoài radius 9 m

	

Không hit

Tất cả chỉ áp dụng ground height band. Hai petals phụ thuộc đường rồng, không phụ thuộc gate count.

Không thay kind lotus, cooldown hoặc victim book.

6. F0 strike và F1–F2 touches

F0 có một ground disk radius 4 m tại castOrigin, hit kind touch.

Nếu không có damageable ground beast nằm trong disk, chọn beast gần caster nhất trong snapshotDamageable, tie theo serial, rồi tạo một guided capsule liên tục từ caster đến mục tiêu:

Ground: radius 0.5 m và endpoint disk radius 1.5 m, kind touch.

Flyer: projected capsule radius 0.5 m và endpoint disk radius 2.5 m trong sky band, kind corridor, part sky.

Đây là collision geometry của hit kinds hiện có, không phải cơ chế damage mới.

F1–F2, mỗi side:

Ground touch disk radius 1.8 m quanh ground beast snapshot gần caster nhất.

Nếu có flyer: sky corridor disk radius 2.5 m quanh flyer snapshot gần caster nhất.

Nếu side không có target thuộc band tương ứng thì không tạo volume đó.

D58: Khi F0 có ít nhất một damageable beast trong hai supported height bands và các budget/effective damage ban đầu dương, local disk hoặc guided capsule chắc chắn chứa ít nhất một candidate tại F0. Fixed machinery xử lý candidate đó, nên first hit ≤F2. Điều kiện này cần được kiểm thử trực tiếp, không suy từ hình ảnh.

Guided capsule là ngoại lệ cần thiết cho trường hợp một quái duy nhất ở góc xa sân: nếu cấm cả instant long-range geometry thì không thể bảo đảm D58 cho mọi vị trí.

7. Walk-throughs

Các ví dụ nhiều quái dùng 40 ground + 2 crows. Split theo count là 21/21. Chiều dài là ước lượng cần xác nhận bằng geometry tests, không phải số bot đo được.

Layout

	

Hai dragon paths

	

Length




Two gates, 40×26 m

	

Một rồng quét cụm trái, rồng kia cụm phải; cả hai bổ sung outer cells rồi gặp tại pearl

	

~100–143 m




One gate, 32×28 m

	

Chia đôi dòng ở top centre theo lateral rank; hai rồng mở rộng sang hai phía rồi hội tụ

	

~85–128 m




Three gates, 48×28 m

	

Cụm giữa chia theo rank, các cụm hai bên vào side tương ứng; mỗi rồng thăm density anchors rồi sweep

	

~120–167 m




Open arena, 36×36 m

	

Hai rồng quét các vòng phân bố trên nửa sân của mình, rồi về pearl

	

~110–153 m




Behind caster, 40×26 m

	

Hai rồng quay ra phía sau caster, đánh các cụm trước khi trở về pearl

	

~90–143 m




Lone foe (18,-16)

	

Side 0 có một mục tiêu; side 1 dùng fallback sweep. F0 guided capsule bảo đảm contact

	

≤143 m




Empty

	

0/0; hai geometric sweeps, pearl tại heart; không có cast damage

	

≤143 m

Ở 35–45 live, các density anchors giúp hai corridor tiếp xúc cụm thật thay vì quét ngẫu nhiên. Ground trail, sky part và lotus tiếp tục tạo cơ hội hit. 12–20 distinct hits là mục tiêu benchmark, không phải bảo đảm từ geometry.

8. Fixed table và balance

Chỉ đề xuất đổi các con số sau:

Parameter

	

Value




Ground budget/side

	

2.0 W, từ 2.5 W




Sky budget/side

	

0.8 W, giữ




Touch/corridor/lotus

	

15/45/40%, giữ




Ground corridor

	

r 1.4 m




Sky corridor

	

r 2.5 m




Trail

	

54 ticks




Lotus

	

r 9 m




Full core

	

r 4 m

Không sửa AreaHit, falloff ladder, boss cap, hit kinds, candidate sorting, minimum 20-tick gap hoặc victim book.

Ground budget 2.0 W là điểm khởi đầu vì sweep cũ đạt trung bình 15.2 distinct hits ở mức này, nhưng geometry mới phải benchmark lại.

Đề xuất target key-2 share = 18–20%. Chỉ giảm budget sẽ không đủ: số liệu cũ ở 2.0 W vẫn đạt share 37–45%.

Cần tăng reach/coverage của các skill khác, thử key 1 từ 12 lên 16–18 m, auto-attack từ 10 lên 13–15 m, sau đó rebalance HP/waves để đạt bot win 75–90%.

Owner decision: duyệt budget 2.0 W, target share và phạm vi rebalance toàn game.

9. Test plan
Synthetic fixtures

Đối với năm fixtures đầu, dùng 40 ground theo chỉ số i, gồm 8 swarm, 24 small, 4 medium, 4 general, và hai crows tại y=4m. Các phép chia tọa độ dùng integer rational với mulDivSym.

Case

	

Field; ground positions; crow positions (m)




Two gates

	

[-20,20]×[-18,8]; 20 mỗi bên: z=-17+0.9i, x=±(0.4+14.6*max(0,-z)/18), i=0..19; crows (±19,-16)




One gate

	

[-16,16]×[-12,16]; x=0.55*(i%5-2), z=15-1.2*floor(i/5), i=0..39; crows (±12,12)




Three gates

	

[-24,24]×[-14,14]; left/right 14 mỗi bên x=±(23-20i/13), z=0.6*(i%3-1); top 12 x=0.35*(2*(i%4)-3), z=13-i; crows (±20,12)




Open arena

	

[-18,18]²; năm bán kính [4,7,10,13,16], tám hướng (±1000,0), (0,±1000), (±707,±707); crows (±15,0)




Behind caster

	

Field hôm nay; x=(2*(i%8)-7)/2, z=4+0.8*floor(i/8); crows (±4,6)




Lone

	

Field hôm nay; một medium (18,-16)




Empty

	

Field hôm nay; không quái

Dùng species IDs thật từ test registry. Với crow, truyền gate "sky" khi API yêu cầu; với ground dùng labels hợp lệ. Test gate independence bằng cách thay labels trong những trường hợp spawn hợp lệ và kiểm tra geometry hash không đổi.

Assertions

sideCount chính xác với 0, 1, 2, 42 và 60 quái. Test ties theo serial và late spawn giữ side cố định.

Mọi path bắt đầu tại caster, kết thúc tại pearl; samples ở trong field; path length ≤Lmax; passTicks trong F3–F42.

Test F0 hit với ground gần, ground xa, only-flyer, behind-caster và lone; first hit ≤F2.

Test sky height bands, F30–F50, và từng capsule có đúng một corridor candidate trên mỗi beast.

Thay gate labels không đổi geometry.

Xoay field và positions 90°; phản chiếu qua trục x. So sánh samples và hit sets sau inverse transformation. Với mirror, hoán đổi side; sử dụng test có count chẵn và không có median ties. Kiểm tra riêng tie/rounding cases theo quy tắc serial.

Hai lần chạy cùng seed và inputs cho hashes giống nhau từng tick. Không có float state trong sim.

Flag-off giữ nguyên baseline hashes và damage results.

Coverage độc lập với damage
Plain text
coverage0 =
    count(F0 eligible beasts whose frozen F0 position
          intersects any side-matched hit volume F0..F71)
    / count(F0 eligible beasts)

Không áp dụng budgets, mayHit, death/despawn; dùng frozen F0 positions. Với thực chiến, đo thêm movingContactRate theo current positions.

Đề xuất targets: clustered fixtures ≥90%, open arena ≥80%, lone 100%, empty N/A.

Chạy ít nhất 92 bot casts tại 35–45 live trên map hiện tại. Báo cáo distinct hits p10–p90 target 12–20, side-hit ratio 40/60–60/40 ở ≥90% casts, crow-hit rate ≥92%, first hit ≤F2, damage by part và CPU ≤50 µs/tick/cast.

Ghi đầy đủ BALANCE.md: win, S, P, I, O, N, Q, typed share, key-1 share, key-2 share, auto-attack share.

10. View contract

Sim cung cấp castId, startTick, pearl, controls[2], samples[2], passTicks[2], trailLifetime=54, skyAnchors, roar F43–F50 và lotus F51–F71. View dựng hai dragon heads tại sample mới nhất theo tick, nối các active samples thành thân/đuôi, thêm sky tethers và lotus. Mọi interpolation của renderer không phản hồi vào sim.

11. Risks và uncertainties

Rủi ro lớn nhất là budget hết trước khi geometry chạm nhiều mục tiêu, đặc biệt khi density anchors tập trung gần caster. Vì thế phải phân biệt coverage0, movingContactRate và distinct damaged victims.

Rủi ro tiếp theo là số sky capsules trong trường hợp 60 flyers, cùng chi phí F0 path building. Cần profile riêng build time và steady-state tick time, không tuyên bố đạt 50 µs khi chưa đo.

Các giới hạn first-hit chỉ áp dụng những height bands được cung cấp. Trường hợp không có hướng caster→heart cũng cần regression test riêng cho fallback orientation; không đòi rotation equivariance tuyệt đối khi không có bất kỳ vector định hướng nào trong input.

Thiết kế giữ nguyên fixed damage machinery. Những giá trị coverage, win rate và damage share vẫn là acceptance targets phải kiểm chứng bằng test và bots.

---

#### fallback-turn-3:0:user · USER (Claude)

Review your latest full answer above (the corrected full version) against the brief, the facts and the constraints. Judge only what the brief asks of you: the damage machinery is fixed and given, so do not redesign it; balance numbers that only the bot can measure are targets, not defects. It FAILS only for a real defect: a wrong fact, a step that would not work, a missing step the goal needs, a contradiction with the constraints or the owner's decisions, or a part too vague for a coding agent to implement. Wording, style and optional extra ideas are not defects.
If it is correct and accurate, answer with exactly one line: VERDICT: PASS (you may add one line "Optional:" with ideas that do not change the verdict)
Otherwise answer: VERDICT: FAIL, then list each defect, then give the corrected FULL analysis and solution (not a diff). If the full version does not fit in one message, stop at a section boundary, end with the line PART 1 OF N, and I will ask for the next part.

---

#### fallback-turn-3:2:assistant · CHATGPT

ChatGPT said:

VERDICT: FAIL

Bản sửa trước vẫn có bốn lỗi thực sự:

Late-spawn side không nhất quán với phép mirror. Side của quái mới dùng splitPivot (khóa của quái cuối side 0), trong khi vùng quét dùng vCut (ranh giới giữa hai side). Một quái mới nằm giữa hai giá trị trung vị có thể không đổi side khi phản chiếu bản đồ, dù hai rồng đã đổi side. Cần dùng cùng một ranh giới hình học cho late spawns và sweep.

Density grid có thể tăng bộ nhớ không giới hạn theo diện tích sân. Chia toàn bộ localAABB thành các ô 4 m mà không quy định sparse storage sẽ tạo rất nhiều ô rỗng trên bản đồ lớn, trong khi chỉ có tối đa 60 quái. Cần lưu duy nhất occupied cells.

Sweep grid có hai giới hạn không thể đồng thời bảo đảm. Yêu cầu ô rộng tối đa 6 m nhưng cũng không quá tám ô mỗi chiều là mâu thuẫn khi chiều sân vượt 48 m. Cần quy định kích thước danh nghĩa và cách nới khoảng cách khi chạm giới hạn tám ô.

Chưa xử lý việc sweep anchor đổi nửa sân sau khi clamp. Cell centre được chọn theo vCut trước khi chuyển về world coordinates; clamp vào field rectangle có thể đẩy điểm sang phía còn lại. Điều này làm sai quy tắc vùng quét và có thể phá phép kiểm tra mirror. Cần kiểm tra lại side sau clamp, đồng thời cố định các tie-break và quy tắc lượng tử hóa.

Không có lý do để thay đổi fixed damage machinery. Các budget và ngưỡng bot vẫn là đề xuất cần đo, không phải lỗi.

Corrected full solution — twin-pearl
1. Snapshot

Tại F0, trước damage pass, đọc đúng một lần các quái hiện tại bằng cùng điều kiện damageable của engine. Lưu:

serial, slot, x, z, y, hp, threatW100, cùng fieldBounds, heart, castOrigin.

Sau khi dựng geometry, cast lưu serialSide, cut2, pearl, controls[2], samples[2], passTicks[2], touchAnchors, skyAnchors, finalPaths[2].

Không đọc hoặc sử dụng GateId, lane, waypoint hay flow field.

Các tick tiếp theo vẫn đọc vị trí quái trong live collision pass cố định; không lấy snapshot mới để điều chỉnh đường bay.

Nếu không có damageable beast tại F0: pearl=heart, hai rồng dùng fallback sweep đối xứng. Geometry builder vẫn trả kết quả để kiểm thử; production không kích hoạt cast.

2. Side split

Chia theo số quái tại F0, bao gồm ground và sky; chênh lệch tối đa một.

Dùng hệ trục địa phương gắn với caster và heart:

Plain text
U = 60000
PM = 1000

F = unitPm(heart.x-caster.x, heart.z-caster.z)
if F == (0,0): F = (0,-1000)
R = (-F.z,F.x)

v(p) = mulDivSym(dot(p-heart,R),1,PM)
u(p) = mulDivSym(dot(p-heart,F),1,PM)

key(b) = (v(b),u(b),b.serial)
B = sort(snapshot,key ASC)

n = len(B)
n0 = (n+1)//2

side(B[0:n0]) = 0
side(B[n0:n]) = 1

if n == 0: cut2 = 0
if n == 1: cut2 = 2*v(B[0])
if n >= 2: cut2 = v(B[n0-1])+v(B[n0])

cut2 biểu diễn hai lần lateral split coordinate, tránh làm tròn trung vị.

Với quái xuất hiện sau F0, khi nó lần đầu được live pass quan sát:

Plain text
if serial not in serialSide:
    dv = 2*v(beast)-cut2

    if dv < 0: side = 0
    else if dv > 0: side = 1
    else: side = beast.serial & 1

    serialSide[serial] = side

Kết quả không đổi khi quái di chuyển. Điểm đúng trên ranh giới sử dụng serial parity; trường hợp bất khả thi về đối xứng tại chính mirror axis được kiểm thử riêng, không tuyên bố mirror-equivariance cho tie đó.

Vùng side 0 có 2*v<=cut2; side 1 có 2*v>=cut2. Hai bên được phép dùng cùng một điểm nằm đúng ranh giới, nhưng mỗi victim chỉ thuộc một side.

3. Hai dragon paths

Chọn Balanced Density-Guided Dual Sweep, kết hợp ba phương án:

Mirrored Spiral: phủ rộng nhưng không ưu tiên quái.

Top-k Density: ưu tiên quái nhưng dễ bỏ sót rìa sân.

Half-Field Sweep: bao phủ ổn định nhưng lãng phí khi phân bố không đều.

Hybrid chọn tối đa năm density anchors mỗi side, sau đó bổ sung các điểm xa đường bay nhất.

Pearl

Ưu tiên ground beasts để lotus ground-volume có vị trí hữu ích. Nếu không có ground, dùng sky beasts; nếu rỗng, dùng heart.

Plain text
source = groundSnapshot if nonempty else snapshot
w(b) = clamp(b.threatW100,1,400)

C = weightedCentroid(source,w)
if source empty: C = heart

pearl = heart + mulDivSym(3*(C-heart),1,5)
pearl = clampToInsetField(pearl)

inset = min(15000,width//4,depth//4)

Mọi phép tính theo từng tọa độ, sử dụng integer và signed intermediate đủ rộng. clampToInsetField dùng khoảng [min+inset,max-inset] trên từng trục.

Density anchors

Chuyển bốn góc field sang (v,u); lấy localAABB.

Grid danh nghĩa 4 m, nhưng chỉ cấp phát ô chứa quái:

Plain text
Nv = max(1,ceilDiv(vMax-vMin,4*U))
Nu = max(1,ceilDiv(uMax-uMin,4*U))

index(a,aMin,aMax,N):
    if aMax == aMin: return 0
    return clamp(floorDiv((a-aMin)*N,aMax-aMin),0,N-1)

Với mỗi ground beast, thêm vào sparse cell của side. Lưu sumW, count, minSerial, weightedCentroid.

Sắp xếp sumW DESC, count DESC, minSerial ASC. Chọn tối đa năm occupied cells mỗi side. Anchor là centroid theo trọng số, clamp vào field.

Tối đa 60 occupied cells cho toàn cast; không tạo dense density array.

Sweep candidates

Dùng grid thứ hai:

Plain text
Sv = clamp(ceilDiv(vMax-vMin,6*U),1,8)
Su = clamp(ceilDiv(uMax-uMin,6*U),1,8)

Khi local span vượt 48 m, actual cell width được phép lớn hơn 6 m. Tổng candidates tối đa 64.

Dùng integer cell centres, chuyển về world:

Plain text
p = heart + (
    mulDivSym(v,R,PM)
  + mulDivSym(u,F,PM)
)
p = clampToField(p)

Chuyển và làm tròn riêng từng trục. Sau clamp, tính lại v(p), chỉ giữ candidate thỏa half-plane của side. Loại tọa độ trùng bằng (x,z); tie ưu tiên u ASC, rồi khoảng cách đi ra ngoài từ cut2 ASC.

Control-point ordering
Plain text
route = [castOrigin,pearl]

for q in top5DensityAnchors:
    tryInsert(q)

while sweepCandidates not empty:
    q = argmax(
        distanceSqToPolyline(q,route),
        tie: u(q) ASC,
             abs(2*v(q)-cut2) ASC,
             localCellOrder ASC
    )

    if distanceSqToPolyline(q,route) <= (3*U)^2:
        break

    tryInsert(q)
    remove q from sweepCandidates

localCellOrder dùng chỉ số theo hướng từ split outward, không dùng world X/Z.

distanceSqToPolyline chiếu điểm lên từng segment bằng integer parameter [0,1000000], clamp vào endpoints và chọn khoảng cách nhỏ nhất; tie theo segment index.

tryInsert(q) thử tất cả các khoảng giữa control points, tính tăng chiều dài bằng isqrt, chọn tăng ít nhất, tie theo gap index. Nếu vượt giới hạn, từ chối điểm.

Plain text
D = isqrt(width*width+depth*depth)
Lmax = 3*D

Bắt đầu luôn tại caster, kết thúc luôn tại pearl. Candidate bị từ chối không được thử vô hạn; sweep tiếp tục với những candidate còn lại.

Sampling và S-offset

Sample theo tổng chiều dài control polyline mỗi 0.5 m, không reset arc tại control points.

Plain text
step = 30000
halfWave = 240000
amplitude = 54000

phase = baseArc % halfWave
cycle = baseArc // halfWave

wave = mulDiv(
    amplitude,
    4*phase*(halfWave-phase),
    halfWave*halfWave
)

sign = 1 if (cycle+side)%2 == 0 else -1

T = unitPm(currentSegmentDelta)
N = (-T.z,T.x)

sample = baseSample + mulDivSym(sign*wave,N,PM)
sample = clampToField(sample)

Dùng outgoing tangent tại control point; sample cuối dùng incoming tangent. Ép sample đầu bằng caster, sample cuối bằng pearl.

Tính lại cumulative sample arc sau clamp. Nếu chiều dài vượt Lmax, bỏ optional anchor được chấp nhận sau cùng rồi dựng lại. Nếu không còn optional anchors, giảm S-amplitude về 0 cho đường trực tiếp để bảo đảm giới hạn.

Plain text
pass[i] =
    3 + mulDiv(sampleArc[i],39,totalArc)

active(i,t) =
    pass[i] <= t && t <= pass[i]+54

Nếu totalArc=0, đặt pass=3.

Mỗi active sample tạo ground disk radius 1.4 m, height 0–1.5 m. Union các disk là dragon body/trail. Index samples bằng spatial bins 3 m, đăng ký mọi bin giao bounding box bán kính 1.4 m, kiểm tra chính xác bằng dist2.

4. Sky part

Tại F0, lưu skyAnchors cho quái thuộc height band 2.5U..6U, gồm x, z, serial, side. Không suy ra crow từ gate label.

F30–F50, với mỗi side:

Plain text
head(t) = sample with greatest index
          satisfying passTick <= min(t,42)

skyVolume(side,t) = union(
    capsule(head(t),a,2.5*U)
        for a in skyAnchors[side],

    disk(s,2.5*U)
        for s in activeSamples(side,t)
)

Mọi volume chỉ tồn tại ở sky height band. Capsule là đoạn nối liên tục từ dragon head tới snapshot anchor; không cần sky route.

Dùng integer squared point-to-segment distance; AABB rejection trước phép chiếu. Mỗi beast trả về tối đa một sky-corridor boolean cho fixed candidate pipeline, dù giao nhiều volumes.

Sky damage luôn dùng kind corridor, part sky. Giữ budget riêng 0.8 W/side.

Crow di chuyển 2 m/s chỉ lệch tối đa khoảng 1.67 m khỏi snapshot trong 50 ticks nếu không đổi tốc độ hoặc teleport, nên anchor radius 2.5 m đủ về mặt hình học. Quái bay spawn sau F0 vẫn có thể bị projected active samples đánh trúng nhưng không tạo anchor mới.

5. Pearl và lotus

F42: hai dragon heads đến pearl.

F43–F50: roar, không có hit volume mới.

F51–F71: lotus tại pearl.

Region

	

Volume

	

Multiplier




lotusFullCore

	

Disk r 4 m

	

100%




lotusFullPetal

	

Hai capsule r 2.2 m quanh 13 m cuối dragon paths, giao disk r 9 m

	

100%




lotusHalf

	

Phần còn lại trong disk r 9 m

	

50%




Outside

	

Ngoài disk r 9 m

	

No hit

Xác định finalPath bằng cách đi ngược cumulative sampled arc từ endpoint 13 m, nội suy integer tại điểm cắt, rồi nối với các samples còn lại tới pearl. Nếu path ngắn hơn 13 m, dùng toàn bộ path.

Kiểm tra lotus:

Plain text
if !groundBand(beast.y): return NONE
if dist2(beast,pearl) > (9*U)^2: return NONE

if dist2(beast,pearl) <= (4*U)^2
   or intersectsEitherPetal(beast):
    return FULL

return HALF

Petal không lấy từ lane hoặc gate. Vẫn chỉ một kind lotus cho mỗi victim.

6. F0 strike và F1–F2 touches

F0 có ground disk radius 4 m tại caster, kind touch.

Nếu không có damageable ground beast trong disk, tạo thêm guided capsule từ caster tới quái damageable gần caster nhất tại F0, tie theo serial:

Ground target: capsule r 0.5 m + endpoint disk r 1.5 m, kind touch.

Sky target: projected capsule r 0.5 m + endpoint disk r 2.5 m trong sky band, kind corridor, part sky.

Hai trường hợp dùng hit kinds và parts sẵn có. Capsule nối liên tục từ caster, không xuất hiện như một volume rời rạc tại mục tiêu.

F1–F2, mỗi side đặt ground touch disk r 1.8 m tại ground beast snapshot gần caster nhất; nếu có flyer, đặt sky corridor disk r 2.5 m tại flyer gần nhất. Side không có mục tiêu tương ứng thì không tạo volume đó.

D58: Trong F0 collision phase, local disk chứa ít nhất một ground target hợp lệ hoặc guided capsule chứa target được chọn. Vì thế, với cast hợp lệ, positive budget và damageable beast trong một trong hai supported height bands, first hit xảy ra tại F0, không muộn hơn F2.

Mọi volume đi qua pipeline cố định. Mỗi beast chỉ tạo một candidate cho kind đầu tiên còn hợp lệ, xét theo touch, corridor, lotus; toàn bộ candidates vẫn sort theo kind, heart-distance, serial.

7. Walk-throughs

Các trường hợp đông quái dùng 40 ground + 2 crows. Chia theo count: 21/21. Chiều dài dưới đây là khoảng ước lượng thiết kế, chưa phải kết quả chạy code.

Map

	

Split và hướng bay

	

Rough length/dragon




Two gates, 40×26 m

	

21/21; mỗi rồng quét một dòng, bổ sung vùng ngoài, hội tụ gần heart

	

90–143 m




One gate, 32×28 m

	

21/21; cả hai chia đôi dòng top-centre, mở rộng sang hai phía rồi hội tụ

	

75–128 m




Three gates, 48×28 m

	

21/21; cụm giữa chia theo lateral rank, hai cụm ngoài vào hai side tương ứng

	

100–167 m




Open arena, 36×36 m

	

21/21; mỗi rồng đi qua density anchors trong nửa phân bố, rồi quét phần chưa phủ

	

90–153 m




Behind caster, 40×26 m

	

21/21; hai rồng quay về phía sau caster trước, rồi mở rộng sweep

	

85–143 m




Lone foe (18,-16)

	

1/0; rồng 0 đi qua mục tiêu, rồng 1 chạy fallback sweep

	

≤143 m




Empty

	

0/0; hai fallback sweeps, pearl=heart; không có damage cast

	

≤143 m

Các giới hạn trên suy ra từ Lmax. Với bản đồ hiện tại, Lmax≈143.1m.

Ở 35–45 live, density anchors giúp hai đường ưu tiên cụm quái, còn trail và lotus bổ sung khả năng tiếp xúc. Mục tiêu 12–20 distinct damaged beasts cần được bot xác nhận; không suy ra trực tiếp từ số quái nằm trong volume.

8. Budget và balance

Giữ nguyên machinery, chỉ đề xuất bảng số:

Parameter

	

Proposed




Ground budget/side

	

2.0 W, từ 2.5 W




Touch/corridor/lotus split

	

15/45/40%




Sky budget/side

	

0.8 W




Ground corridor radius

	

1.4 m




Sky radius

	

2.5 m




Trail lifetime

	

54 ticks




Lotus radius

	

9 m

Không thay AreaHit, victim book, falloff ladder, boss cap, hit ordering, cooldown hoặc part kinds.

Budget 2.0 W là điểm xuất phát vì sweep cũ đo được 15.2 distinct hits trung bình tại mức này. Geometry mới cần benchmark độc lập.

Đề xuất key-2 share = 18–20% để phù hợp canon. Các số cũ cho thấy 2.0 W vẫn chiếm 37–45%, nên giảm budget đơn độc không đủ.

Để giữ bot wins 75–90%, cần tăng reach của các skill khác: thử key 1 từ 12 lên 16–18 m và auto-attack từ 10 lên 13–15 m; sau đó rebalance HP và wave pacing bằng bot.

Owner decision: ground budget 2.0 W, share target 18–20% và phạm vi rebalance toàn game.

9. Test plan cho coding agent
Synthetic fixtures

Mọi layout dùng heart=(0,0), castOrigin=(0,3), U=60000. Chuyển tọa độ mét sang integer u bằng rational arithmetic và mulDivSym.

Với 40 ground, gán species theo:

Plain text
if i%5 == 0: swarm
else if i%10 == 1: medium
else if i%10 == 3: general
else: small

Kết quả: 8 swarm, 24 small, 4 medium, 4 general. Thêm hai crows ở y=4m, trừ lone/empty. Sử dụng species IDs thực tế của test registry.

Fixture

	

Exact positions (m)




Two gates

	

Field [-20,20]×[-18,8]; 20 mỗi bên, i=0..19: z=-17+9i/10, x=±(2/5+(73/5)*max(0,-z)/18); crows (±19,-16)




One gate

	

Field [-16,16]×[-12,16]; i=0..39: x=11*(i%5-2)/20, z=15-6*floor(i/5)/5; crows (±12,12)




Three gates

	

Field [-24,24]×[-14,14]; left/right 14 mỗi bên: x=±(23-20i/13), z=3*(i%3-1)/5; top 12: x=7*(2*(i%4)-3)/20, z=13-i; crows (±20,12)




Open arena

	

Field [-18,18]²; năm bán kính [4,7,10,13,16], tám hướng (±1000,0), (0,±1000), (±707,±707); crows (±15,0)




Behind caster

	

Field hôm nay; i=0..39: x=(2*(i%8)-7)/2, z=4+4*floor(i/8)/5; crows (±4,6)




Lone

	

Field hôm nay; một medium (18,-16)




Empty

	

Field hôm nay; không có quái

Dùng "sky" cho crows khi gọi spawnBeast. Ground dùng "A" hoặc "B" theo yêu cầu API, sau đó thay labels hợp lệ để xác nhận geometry independence.

Unit and integration assertions

Side counts: 0/0, 1/0, 1/1, 21/21 và 30/30. Test same-position ties, serial ties không được có vì serial phải unique, và late spawns giữ side sau khi di chuyển.

Mọi path bắt đầu tại caster, kết thúc pearl; samples nằm trong field; totalArc<=Lmax; passTicks thuộc F3–F42.

F0 hit cho ground gần, ground xa, only-flyer, lone và behind-caster; first hit ≤F2.

Sky collision trong F30–F50; nhiều overlapping capsules vẫn chỉ một corridor candidate cho mỗi beast.

Lotus full/half boundaries, petal clipping và 20-tick hit-gap.

Đổi gate labels không đổi geometry hash.

Hai runs cùng seed/input có world hashes giống nhau từng tick; sim không dùng float trig/sqrt.

Skill flag-off giữ nguyên baseline hashes và damage results.

Rotation và mirror

Xoay field, heart, caster và beast positions 90°. Sau khi đảo phép xoay, so sánh control points, samples và hit-volume intersections với integer rounding tolerance.

Mirror qua trục x: hoán đổi side 0/1, kiểm tra geometry sau inverse reflection. Dùng fixtures có số quái chẵn, không có median ties, và test points cách biên hit volumes ít nhất 0.05 m. Ties ngay trên split plane được kiểm tra riêng theo serial parity; không yêu cầu phép hoán đổi side bất khả thi tại điểm bất động của reflection.

Coverage

Để đo độc lập với damage:

Plain text
geometryCoverage =
    count(F0 damageable beasts whose frozen F0 position
          intersects at least one side-matched volume
          during F0..F71)
    /
    count(F0 damageable beasts)

Không chạy damage, không áp dụng budgets hoặc cooldown và không loại quái sau khi chúng lẽ ra bị giết. Dùng F0 positions cố định. Báo cáo thêm travelCoverage, tương tự nhưng chỉ tính F3–F71 để tránh F0 guided ray làm tăng giả tạo mức phủ đường rồng.

Targets thử nghiệm: clustered layouts ≥90%, open arena ≥80%, lone 100%, empty N/A. Đây là acceptance targets, không phải số liệu đã đo.

Bot acceptance

Trên map hiện tại, chạy ít nhất 92 casts ở mức 35–45 live:

Distinct victims p10–p90: mục tiêu 12–20.

Side-hit ratio 40/60–60/40 trong ≥90% casts.

Crow-hit rate ≥92%; first hit ≤F2.

geometryCoverage, travelCoverage, damage by part, F0 build cost và steady-state CPU ≤50 µs/tick/cast.

Ghi đầy đủ BALANCE.md: win, S, P, I, O, N, Q, typed share, key-1 share, key-2 share, auto-attack share.

10. View contract

Sim cung cấp castId, startTick, pearl, controls[2], samples[2], passTicks[2], trailLifetime=54, skyAnchors, finalPaths, roar F43–F50 và lotus F51–F71. View dùng interpolation để dựng hai dragon heads, body và trail theo samples đang active; sky tethers nối head với crow anchors. Renderer tự xử lý chuyển động và Fire art, không phản hồi float positions vào deterministic sim.

11. Risks và uncertainties

Rủi ro chính là hình học phủ được quái nhưng budget hết trước khi gây damage. Vì vậy phải tách geometryCoverage, travelCoverage và distinct damaged victims.

Số samples tăng theo kích thước sân; sparse density grid chỉ giải quyết số ô rỗng, không bảo đảm hiệu năng trên sân cực lớn. Cần benchmark F0 construction, collision bins và trường hợp 60 flyers, hai casts đồng thời. Bản đồ tương lai lớn hơn đáng kể có thể cần scale-specific tuning mà không thay đổi thuật toán hay phụ thuộc gates.

Kết quả first-hit giả định quái damageable thuộc một trong hai supported height bands và cast có positive effective damage. Fixed machinery không thể đánh quái ở khoảng cao không được hỗ trợ.

Cuối cùng, share 18–20% và bot win 75–90% phụ thuộc cả những skill khác. Không được coi chúng là kết quả đã chứng minh trước khi chạy bots.

## Run 3

Verdicts: FAIL, PASS, FAIL (dừng)

Page capture: ChatGPT run 3 (brief v3), verbatim page text

Chat URL: https://chatgpt.com/c/6aeacfc5-716c-83ec-bdb5-29661bc8c300
Captured: 2026-11-04T06:54:25.551Z
Units: 8



---

#### fallback-turn-0:0:user · USER (Claude)

Role: you are the game-systems analyst for a browser typing game, "Tu Tien Thu Ai" (a xianxia defence game where every attack comes from typed words). Analyse ONE candidate design for ONE skill, correct it, and return the corrected design. Write the prose in Vietnamese; keep every name, id, formula and pseudo-code in English. If you need clarifications, ask all of them in one message before you start; otherwise start directly.

WHY THIS BRIEF IS SHAPED THIS WAY
Two earlier runs asked for an open design with exact pseudo-code. Each answer grew new machinery (density grids, sweep grids, insertion heuristics, a 143 m path cap), and every self-review found new edge cases in it (FAIL three times in a row, twice). This run starts from a deliberately SIMPLE candidate written by the coordinator (Claude). Keep it simple: fix what is wrong, replace a part only when the replacement is clearly better and not more complex, and do not add grids, heuristics or damage rules. Code-level details (variable names, loop shapes, notation) belong to the coding ticket that the coordinator writes later; your job is a design that is correct, deterministic, map-agnostic and complete enough that its numbers can be implemented as written.

GOAL
The Sword key-2 skill "Twin Dragons, One Burning Pearl" (`twin-pearl`, 雙龍戲珠) becomes a FIELD-WIDE, MAP-AGNOSTIC area skill. The owner (04/11/2026) rejected the version in which each dragon runs up one lane to one of the two gates: "having the 2 dragons run up to the gates is not reasonable, because we are building skills to be shared; later maps will not only face 2 gates, so the skill must work on many maps instead of going to 2 gates; a field-wide area skill makes more sense." Keep two dragons, one burning pearl and the lotus climax. No gate count, lane, waypoint, flow field or sky-entry point may drive the shape.

FACTS
- Deterministic lockstep sim, 60 Hz, integer-only state; 1 m = 60,000 u; HP integers; per-mille ratios; helpers mulDiv (round half up), mulDivSym, isqrt, dist2, within, unitPm. No float trig or float sqrt. Same seed and inputs, same world hash. At most 60 live beasts, at most 2 casts alive at once.
- F0 = the tick the Cast resolves; Fn = F0+n. D58: the first hit by F2 (50 ms). Fast attack, slow decay; caster side first.
- Today's only map: field x -20..+20 m, z -18..+8 m; heart (formation centre) at (0;0); the player (the Cast's origin) at (0;+3). Ground gates at (-15;-18) and (+15;-18); crows enter at (+-20;-18) and fly straight to the heart 4 m high, 2 m/s; ground beasts walk to the heart edge (r 2 m) at 1.0-1.6 m/s. Peaks in waves 5-6: 25-44 live (max 52), about half per ground stream, 1-3 crows; streams are 2-3 m wide, groups 2-5 m apart. Tests can place beasts anywhere (spawnBeast with x, z) and can build a world on a synthetic stage with other field bounds; the sim cannot load another map yet.
- FIXED damage machinery (unchanged, only its numbers may change): kinds touch / corridor / lotus carry 15 / 45 / 40 % of the beast's key-2 damage (2.5 W = 225 HP at K0) times its side's falloff (100 %, -15 % per next distinct victim of that side, floor 40 %); lotus "half" region deals 50 %; at most one hit of each kind per beast per cast, at least 20 ticks apart; each side has budget parts touch, corridor, sky, lotus (today 2.5 W per side split 15/45/40, plus 0.8 W sky per side, times M_q and the seat bucket), spent first come; the whole cast is one area hit (a swarm cluster loses at most 60 % of its HP to it); the boss takes at most 1.5 W a cast; each tick one pass gathers each beast's first kind it may still take (touch, then corridor, then lotus) and strikes all candidates in one order (kind, distance to the heart, serial); ground volumes (0-1.5 m) hit only ground beasts, sky volumes (2.5-6 m) only flyers; a sky hit is kind corridor and spends the sky part. The cast resolves only when a damageable beast is alive.
- Old measurements (two-lane version, for scale): 17.2 distinct beasts hit per cast at 35-45 alive with the budget (31.5 without); key 2 = 41-50 % of match damage (canon cap 20 % per area skill); bots win 95-100 % with it, 0-40 % without it (all other skills' reach is too short). Budget sweep per side: 1.25 W gave 11.9 hit and wins 0-60 %; 2.0 W 15.2 and 45-100 %; 2.5 W 17.2 and 95-100 %.

CANDIDATE DESIGN (analyse and correct this)
C1. Snapshot at F0. Read once, before the F0 strike: field bounds, heart H, caster point C (the Cast's origin), and every live, damageable beast: serial, x, z, flyer (y within the sky band). Store in the cast record: the side of each snapshot serial, the frame (F, R), cut2, the pearl P, each dragon's route (control points), samples and pass ticks, the touch targets, the sky anchors. Beasts move as usual afterwards; volumes test live positions each tick.
C2. Frame and side split. F = unitPm(H - C) (caster to heart); if zero, F = unitPm(field centre - H); if zero, F = (0,-1000). R = (-F.z, F.x). For a point p: v(p) = (dot(p - H, R)) / 1000 (lateral), u(p) = (dot(p - H, F)) / 1000 (forward), integer division rounding half up. Sort the snapshot by (v, u, serial); the first ceil(n/2) are side 0, the rest side 1 (counts differ by at most one; ground and flyers together). cut2 = v(last of side 0) + v(first of side 1) when n >= 2; 2 v(B0) when n = 1; 0 when n = 0. A beast first seen after F0 gets side 0 if 2 v - cut2 < 0, side 1 if > 0, else serial parity, and keeps it for the cast.
C3. The pearl. G = the mean position of the snapshot's ground beasts (all beasts if no ground beast; H if none). P = H + 3/5 (G - H), then if |P - H| > 12 m scale it to 12 m, then clamp into the field shrunk by 2 m on every side. Empty field: P = H + 9 m along F, clamped the same way.
C4. Each dragon's route. For side s: anchors from its ground beasts by farthest-point sampling, at most K = 3: the first is the side's ground beast farthest from H; each next one maximises the smallest squared distance to {C, P, anchors already chosen}; ties by smaller serial; stop when K are chosen or the best smallest distance is under 3 m. The route is C, then the anchors in the order (of the at most 6 permutations) that gives the shortest polyline C -> ... -> P, ties by the lexicographic order of anchor indices, then P. If the route is longer than Lmax = 36 m, drop the last-chosen anchor and recompute; with no anchor the route is C -> W_s -> P, where W_s = H + 9 m along -R for side 0 and +R for side 1 (a wing loop, clamped like P), so an empty side still shows its dragon.
C5. Sampling and the body (today's code, reused on any polyline): samples every 0.5 m along the route with the S offset (amplitude 0.9 m, about 4 m half-waves per segment, sin approximated by 4f(1-f)), first bulge +1 for side 0 and -1 for side 1, each sample clamped into the field; pass[i] = 3 + arc_i x 39 / totalArc (the head runs F3-F42, at most 36 m in 39 ticks, about 55 m/s); the body is a ground capsule r 1.4 m round every sample with pass[i] <= t <= pass[i] + 54 (0.9 s trail). Kind corridor, part corridor.
C6. F0 strike and touches. F0: a ground disc r 4.5 m round H (64 m2, the old 8 x 8 m box's area), kind touch. F1: for each side, its snapshot beast nearest H (straight line; ties serial) that was not hit at F0; a disc r 2.2 m round that beast's position at F1, in that beast's own band (ground or sky), live F1-F2, kind touch, part touch. So whenever a damageable beast is alive at F0, a hit lands at F0 or F1 (exception, unchanged from today: a swarm beast the 60 % cluster cap leaves at 0 damage).
C7. Sky. F30-F50, for each side: a sky capsule r 2.5 m from the dragon's head sample (the last sample with pass <= min(t, 42)) to each sky anchor of that side (the snapshot flyers of that side, their F0 positions), plus a sky disc r 2.5 m round every active body sample. Kind corridor, part sky.
C8. Lotus. F51-F71 at P, ground only, r 9 m: full within r 4 m of P, inside the F0 disc, and within 2.2 m of each route's last 13 m before P (the petals, measured back along the route from P); half elsewhere within r 9 m.
C9. Frame map: F0 strike; F1-F2 touches; F3-F42 heads; F30-F50 sky; F43-F50 roar (no new volume); F51-F71 lotus; trail hits until at most F96; visuals until F300.
C10. Budget and share: keep the machinery; trial budget 2.0 W per side plus 0.8 W sky per side until the bot re-measures. The share target is the owner's decision: canon caps each area skill at 20 %, but without this skill the bots win only 0-40 %.

DELIVER
1. For each of C1-C10: correct as is, or the defect and the fix (keep fixes simple).
2. Walk-throughs with rough numbers: today's two-gate map at a peak (about 40 alive); a one-gate map (one stream from the top centre); a three-gate map (streams from the left edge, the top centre and the right edge); an open arena with foes on every side; foes only behind the caster; one lone foe; an empty field. For each: the side split, the two routes in words with rough lengths, and whether 12-20 distinct beasts are reachable at 35-45 alive.
3. The corrected full design (C1-C10 rewritten), at most about 1,800 words in all.
4. The test plan: synthetic layouts for each walk-through case (coordinates, counts, species), a mirror check and a rotation check (say exactly what must match and the tolerance), determinism and integer-only state, the flag-off golden check; bot measures on today's map: distinct beasts hit per cast at 35-45 alive (target 12-20, p10-p90), a map-agnostic coverage measure you define exactly, side balance, first hit by F2, crows hit, and the BALANCE.md metrics (win, S, P, I, O, N, Q, typed share, key-1 share, key-2 share, auto-attack share).
5. Your recommendation on the share target and the budget, and what else in the game must change; mark what is the owner's decision.
6. Risks and what you are not sure about.

(The page clipped this bubble to 9820 characters; the text above is the exact brief inserted into the composer and checked equal before sending.)

---

#### fallback-turn-0:2:assistant · CHATGPT

ChatGPT said:
Phân tích và thiết kế cuối cùng — twin-pearl

Kết luận: Giữ phương án chia đàn thú thành hai nhóm, mỗi rồng chọn tối đa ba điểm neo, cả hai hội tụ về một viên ngọc và kết thúc bằng hoa sen. Đây là phương án đơn giản, có tính quyết định và không phụ thuộc số cổng.

Tuy nhiên, cần sửa các vấn đề về giới hạn đường bay, chọn mục tiêu, số nguyên có dấu và ý nghĩa của vùng sát thương. Không cần thêm density grid, sweep grid, flow field hay quy tắc sát thương.

1. Đánh giá C1–C10

Mục

	

Đánh giá

	

Sửa đổi cần thiết




C1

	

Sửa nhẹ

	

Snapshot trước đòn F0; lưu dữ liệu cố định. Mục tiêu F1 chọn tại F1, không khóa trước từ F0.




C2

	

Sửa nhẹ

	

Dùng mulDivSym cho phép chiếu có dấu; giữ chia theo median, quy tắc serial và cut2.




C3

	

Sửa nhẹ

	

Giữ công thức pearl. Làm rõ làm tròn số nguyên và clamp khi một chiều sân nhỏ hơn 4 m.




C4

	

Lỗi quan trọng

	

Bỏ Lmax = 36 m và thao tác xóa anchor. Chúng làm mất khả năng bao phủ trên bản đồ rộng, dù đường bay hợp lệ.




C5

	

Sửa nhẹ

	

Giữ sampling 0.5 m, S-offset 0.9 m, thời gian F3–F42. Xác định chính xác half-wave, độ dài cung, điểm trùng và phép chia.




C6

	

Lỗi điều kiện bảo đảm

	

Giữ F0 disc. F1 chọn mục tiêu còn sống và hợp lệ tại F1. Bảo đảm sát thương chỉ khi mục tiêu còn sống và ngân sách/cap cho phép.




C7

	

Giữ, bổ sung

	

Sky anchors là vị trí F0; các sky volumes chỉ đánh flyers. Làm rõ head sample khi nhiều sample cùng pass tick.




C8

	

Sửa nhẹ

	

full region là hợp của ba điều kiện, không phải giao; luôn nằm trong outer lotus disc.




C9

	

Giữ

	

Cố định các mốc F0–F300; sát thương dừng F96, hình ảnh tồn tại đến F300.




C10

	

Giữ để thử nghiệm

	

2.0 W mỗi side là trial, không phải kết luận cân bằng. Canon 20% vẫn là giới hạn cần đạt.

Điểm quyết định: Lmax = 36 m không phù hợp với chính bộ tình huống bắt buộc. Với các fixture cụ thể dưới đây, độ dài polyline trước S-offset xấp xỉ:

Bản đồ hiện tại: 49 m mỗi rồng.

Một cổng: 31 m mỗi rồng.

Ba cổng: 63 m mỗi rồng.

Đấu trường mở: 60–68 m.

Thú ở sau caster: 38 m mỗi rồng.

Không nên khắc phục bằng một giới hạn lớn hơn. Độ dài tuyến ảnh hưởng tốc độ di chuyển đầu rồng, không được quyết định việc xóa mục tiêu.

2. Thiết kế hoàn chỉnh C1–C10
C1. Snapshot and cast state

Tại F0, trước khi gây sát thương, đọc đúng một lần:

fieldBounds, H, C, toàn bộ beasts đang sống và có thể nhận sát thương, gồm serial, x, z, y và phân loại ground/flyer.

Lưu trong cast:

F, R, cut2, sideBySerial, P, groundAnchors, skyAnchors, routeNodes, samples, passTicks, F1TouchDiscs.

Giữ nguyên snapshot trong suốt cast. Vị trí beast để xét va chạm và trạng thái HP luôn lấy từ sim tại tick hiện hành.

Beasts sinh sau F0 được gán side khi xuất hiện lần đầu trong cast; side không thay đổi.

C2. Frame and side assignment

Đặt:

Plain text
F = unitPm(H - C)
if F == (0, 0):
    F = unitPm(fieldCenter - H)
if F == (0, 0):
    F = (0, -1000)

R = (-F.z, F.x)

v(p) = mulDivSym(dot(p - H, R), 1, 1000)
u(p) = mulDivSym(dot(p - H, F), 1, 1000)

Sắp xếp snapshot theo (v, u, serial).

side 0: ceil(n/2) beasts đầu.

side 1: số còn lại.

cut2 = v(lastSide0) + v(firstSide1) nếu n >= 2.

cut2 = 2*v(single) nếu n == 1; bằng 0 nếu rỗng.

Beasts xuất hiện sau F0 dùng dấu của 2*v - cut2; nếu bằng 0 thì dùng serial parity.

Điều này chia cân bằng số lượng snapshot, kể cả khi toàn bộ thú xuất hiện từ một hướng.

C3. Pearl placement

Đặt G là trung bình vị trí ground beasts; nếu không có ground beast, dùng toàn bộ flyers.

Plain text
P = H + mulDivSym(G - H, 3, 5)

if distance(P, H) > 12m:
    P = H + 12m * unitPm(P - H) / 1000

Sau đó clamp từng tọa độ vào fieldBounds với inset 2 m.

Nếu chiều sân nhỏ hơn 4 m, clamp tọa độ tương ứng về trung điểm chiều đó.

Không có beast:

Plain text
P = clampInset(H + 9m * F / 1000)

Mọi phép trung bình, nhân tỷ lệ và chuẩn hóa đều dùng số nguyên.

C4. Dragon routes

Với mỗi side, chọn tối đa K = 3 ground anchors.

Anchor đầu tiên là ground beast xa H nhất.

Anchor tiếp theo tối đa hóa khoảng cách nhỏ nhất tới tập {C, P, selectedAnchors}.

Dừng khi đủ ba anchors hoặc khoảng cách tốt nhất nhỏ hơn 3 m.

Mọi trường hợp bằng nhau giải quyết bằng serial nhỏ hơn.

Chọn hoán vị anchors có tổng chiều dài C -> anchors -> P ngắn nhất. Tối đa sáu hoán vị; hòa thì dùng thứ tự selection indices.

Không giới hạn tổng chiều dài và không xóa anchor vì đường dài.

Nếu side không có ground anchor:

Plain text
W_0 = clampInset(H - 9m * R / 1000)
W_1 = clampInset(H + 9m * R / 1000)

route_0 = C -> W_0 -> P
route_1 = C -> W_1 -> P

Các control points trùng nhau được gộp; đường có tổng chiều dài 0 vẫn tạo một sample đứng yên tại C.

C5. Sampling, head and body

Giữ nguyên kiểu đường bay S.

Sample cách nhau tối đa 0.5 m trên từng đoạn control polyline, có sample tại endpoint.

Mỗi đoạn chia thành max(1, round(length / 4m)) half-waves.

Dùng 4*f*(1-f) với f từ 0 đến 1, tính bằng per-mille.

Amplitude 0.9 m theo pháp tuyến đoạn; dấu luân phiên theo half-wave, bắt đầu dương với side 0 và âm với side 1.

Clamp samples vào field bounds thực tế, không dùng inset 2 m.

Tính lại cumulative arc length từ samples bằng isqrt.

Plain text
pass[i] = 3 + mulDiv(39, cumulativeArc[i], totalArc)

Nếu totalArc == 0, toàn bộ samples dùng pass = 3.

Đầu rồng đi từ F3 đến F42 theo pass. Ground body có footprint hình tròn bán kính 1.4 m tại mỗi sample:

Plain text
pass[i] <= tick <= pass[i] + 54

Dùng corridor và ground band 0–1.5 m.

C6. Immediate strike and touch

F0: ground disc bán kính 4.5 m quanh H, kind touch.

F1: với mỗi side, chọn ground hoặc flyer còn sống, touch-eligible và chưa bị touch tại F0, gần H nhất; hòa theo serial.

Tạo disc bán kính 2.2 m tại vị trí F1 của mục tiêu, đúng height band của mục tiêu. Disc đứng yên và hoạt động F1–F2.

Cả F0 và F1 đều dùng touch part của side đã được gán cho beast.

Quy tắc D58: Trong bài kiểm thử cô lập, với ít nhất một mục tiêu damageable còn sống và touch budget cho phép sát thương dương, phải có hit chậm nhất cuối F2.

Không thể bảo đảm sát thương dương nếu mục tiêu chết trước F1 hoặc bị cap hiện hữu giới hạn về 0. Không thay đổi cap.

C7. Sky coverage

Từ F30 đến F50, mỗi dragon tạo:

Sky capsule bán kính 2.5 m nối current head sample với từng skyAnchor cùng side.

Sky disc bán kính 2.5 m quanh các active body samples.

current head sample là sample có chỉ số lớn nhất thỏa pass <= min(tick, 42).

Sky anchors là vị trí F0, không bám theo flyers.

Chỉ flyers trong height band 2.5–6 m có thể nhận hit từ sky volumes.

Damage kind vẫn là corridor, nhưng chi từ sky budget part.

C8. Lotus climax

Từ F51 đến F71, lotus xuất hiện tại P, chỉ đánh ground beasts.

Outer radius = 9 m.

Một ground beast nằm trong full region khi nằm trong outer radius và thỏa ít nhất một điều kiện:

Plain text
distance(beast, P) <= 4m
OR distance(beast, H) <= 4.5m
OR distance(beast, last13m(route_0)) <= 2.2m
OR distance(beast, last13m(route_1)) <= 2.2m

last13m được đo ngược theo sampled arc từ P; tuyến ngắn hơn 13 m sử dụng toàn bộ tuyến.

Phần còn lại bên trong outer radius là half region, nhận 50% lotus damage.

Không có quy tắc dựa vào cổng hoặc làn đường.

C9. Frame timeline

Frame

	

Hành động




F0

	

Cast release tại C; ground strike tại H




F1–F2

	

Targeted touch discs




F3–F42

	

Dragon heads và ground bodies




F30–F50

	

Sky coverage




F43–F50

	

Roar tại pearl, không thêm hit volume




F51–F71

	

Lotus climax




F72–F96

	

Ground trail damage còn hiệu lực




F97–F300

	

Visual decay, không gây damage

Renderer nhận routeNodes, samples, passTicks, P, side và frame hiện hành từ sim. Không tự tính lại đường bằng floating-point để quyết định sát thương.

C10. Damage and budget

Giữ toàn bộ machinery hiện tại:

Kind

	

Base damage

	

Budget part




touch

	

15% of 2.5 W

	

touch




corridor, ground

	

45% of 2.5 W

	

corridor




corridor, sky

	

45% of 2.5 W

	

sky




lotus, full

	

40% of 2.5 W

	

lotus




lotus, half

	

50% of full lotus

	

lotus

Trial:

Plain text
groundBudgetPerSide = 2.0 W
skyBudgetPerSide = 0.8 W

groundBudgetSplit = [15%, 45%, 40%]

Giữ M_q, seat bucket, falloff 100/85/70/55/40%, minimum re-hit interval 20 ticks, one-hit-per-kind, swarm-cluster cap 60%, boss cap 1.5 W và thứ tự (kind, distanceToHeart, serial).

Beast dùng side cố định của chính nó để tính budget và falloff; vùng của hai rồng có thể giao nhau nhưng không tạo thêm hit kind.

Một điều kiện cần kiểm chứng: ở 2.0 W, touch part chỉ có 0.3 W, thấp hơn nominal first touch 0.375 W. Bài thử phải xác nhận machinery hiện hữu vẫn thanh toán được sát thương dương từ budget còn lại. Nếu cơ chế hiện tại từ chối toàn bộ hit không đủ tiền, phải dùng 2.5 W làm baseline an toàn thay vì thay quy tắc chi budget.

3. Walk-through trên bảy tình huống

Các con số sau là ước lượng chiều dài control polyline cho fixtures của phần 4, chưa cộng độ cong S. Không phải kết quả bot.

Tình huống

	

Side split

	

Hai tuyến đường

	

Khả năng đạt 12–20




Hai cổng hiện tại, 40 beasts

	

20/20, chủ yếu chia theo x

	

Dragon 0 qua cụm trái, Dragon 1 qua cụm phải, cùng về P ≈ (0,-5.7); mỗi đường ~49 m

	

Có khả năng; phải đo actual hits




Một cổng trên giữa, 40

	

20/20 ngay trong cùng stream

	

Hai tuyến gần song song, đi dọc stream tới khoảng z=-17 rồi quay về pearl; ~31 m

	

Có khả năng, nhưng dễ trùng vùng sát thương




Ba cổng, 43

	

22/21; stream giữa chia giữa hai side

	

Một rồng nối trái–giữa, rồng còn lại nối phải–giữa; ~63 m mỗi đường

	

Có khả năng; Lmax cũ chắc chắn gây mất coverage




Arena bốn phía, 44

	

22/22

	

Hai tuyến đi qua các điểm neo ở nửa sân tương ứng, rồi hội tụ; ~60–68 m

	

Có khả năng, trường hợp khó nhất về phân tán




Chỉ sau caster, 40

	

20/20

	

Hai đường xòe ra hai bên phía z dương, quay về P ≈ (0,3.3); ~38 m

	

Có khả năng; F0/F1 đặc biệt hữu ích




Một beast tại (0,+7)

	

1/0

	

Dragon 0 ~6.8 m qua mục tiêu; Dragon 1 dùng wing loop ~19.4 m

	

Không áp dụng chỉ tiêu 12–20; mục tiêu phải trúng F1 nếu còn sống




Không có beast

	

0/0

	

Hai wing loops đối xứng dài ~22.2 m; P=(0,-9)

	

Không có Cast hợp lệ; chỉ chạy geometry preview

Một kiểm tra hình học gần đúng, giữ nguyên vị trí F0 của beasts và bỏ qua budget, cho thấy phần lớn mục tiêu trong các fixtures này nằm trong ít nhất một vùng đánh. Tuy nhiên, điều đó không chứng minh 12–20 actual distinct hits: budget, cooldown giữa các kind và thứ tự phân phối sát thương có thể làm số hit thấp hơn đáng kể.

4. Test plan
4.1. Synthetic fixtures

Dùng H=(0,0), C=(0,3), đơn vị tọa độ trong bảng là mét, và y=0 cho ground, y=4 cho crow. Các phép sinh tọa độ phân số được đổi sang integer u bằng quy tắc làm tròn đối xứng.

Fixture

	

Định nghĩa chính xác




two-gate

	

Bounds [-20,20] × [-18,8]. Ground: sideSign ∈ {-1,+1}, i=0..17, x=sideSign*(15+(i%3)-1), z=-17+15*i/17. 36 ground. Crows: (-19,-12), (-10,-8), (10,-8), (19,-12). Total 40.




one-gate

	

Cùng bounds. 38 ground, i=0..37, x=0.5*((i%5)-2), z=-17+2*floor(i/5). Crows (-2,-16), (2,-16). Total 40.




three-gate

	

Cùng bounds. 14 left ground: x=-18+0.75*(i%3), z=-14+4*floor(i/3); 14 right ground là ảnh gương; 12 top ground: x=0.8*((i%3)-1), z=-17+4*floor(i/3). Crows (-18,-14), (0,-16), (18,-14). Total 43.




open-arena

	

Bounds [-20,20] × [-20,20]. 40 ground: tám hướng [(10,0),(0,10),(-10,0),(0,-10),(7,7),(-7,7),(-7,-7),(7,-7)] / 10, năm bán kính [5,8,11,14,17]. Crows tại (±15,0) và (0,±15). Total 44.




behind-caster

	

Bounds hôm nay. 38 ground: i=0..37, x=-18+3*(i%13), z=4+1.5*floor(i/13). Crows (-17,7), (17,7). Total 40.




lone

	

Một ground beast tại (0,7).




empty

	

Không có beast; geometry preview only.

floor trong bảng chỉ là quy tắc tạo fixture; không sử dụng floating-point trong sim.

4.2. Geometric coverage

Định nghĩa:

Plain text
coverageStatic =
    snapshotBeastsInsideAnyActiveVolume /
    damageableSnapshotBeasts

Cách đo: đóng băng mọi beast tại vị trí F0, replay hit volumes F0–F96, bỏ qua damage budget, HP, swarm cap và cooldown. Với F1, chọn tâm touch disc trên các beast đóng băng chưa được F0 disc bao phủ.

Một beast được đếm một lần nếu vị trí và height band của nó giao ít nhất một volume.

Mục tiêu đề xuất: coverageStatic >= 75% trên từng synthetic fixture có 35–45 beasts. Đồng thời báo riêng ground coverage và flyer coverage. Đây là mục tiêu hình học cần kiểm chứng, không phải actual damage coverage.

4.3. Invariance and determinism

Mirror test: Dùng two-gate, phản chiếu x -> -x, giữ serial gắn với từng beast. Vì 40 beasts chia đều và không có lateral tie tại median:

side 0 và side 1 phải hoán đổi.

Đường bay, pearl, samples và volumes phải phản chiếu đúng.

Hit serials, hit frames, HP damage và tổng chi budget phải giống.

Tolerance: 0 u, 0 HP, 0 ticks.

Không áp dụng yêu cầu hoán đổi side tuyệt đối cho odd counts hoặc lateral ties tại median: quy tắc ceil(n/2) và serial có thể phá đối xứng phản chiếu trong những trường hợp đó.

Rotation test: Xoay toàn bộ bounds, C, H, beasts và velocities theo:

Plain text
T(x, z) = (-z, x)

Chạy với two-gate và three-gate.

Sau khi inverse-transform kết quả, yêu cầu hình học và hit events trùng chính xác, tolerance 0. Side labels phải giữ nguyên. So sánh event traces và trạng thái đã inverse-transform, không so sánh trực tiếp raw world hash của hai hệ tọa độ khác nhau.

Lockstep test: Cùng seed, inputs và rules phải có cùng world hash trên các lần chạy và môi trường JS được hỗ trợ. Kiểm tra mọi cast state là integer; không có Math.sin, floating-point sqrt hay phép chia không kiểm soát trong sim.

Flag-off golden: Với flag twin-pearl tắt, replay cùng seeds trên bản cũ và bản mới. Yêu cầu rulesHash, world hash từng tick, event trace và kết quả trận byte-identical. Bật flag thì trial table phải tham gia rulesHash như quy định hiện hữu.

4.4. Bot measurements

Chạy lại peak sweep và bot suite trên bản đồ hiện tại, tối thiểu cùng quy mô mẫu cũ 17 profiles × 20 seeds và khoảng 90+ casts ở 35–45 beasts. Báo:

Metric

	

Mục tiêu / yêu cầu




distinctHitsPerCast, 35–45 alive

	

p10–p90 trong khoảng 12–20




coverageStatic

	

≥75% mỗi synthetic peak fixture




sideBalance

	

Snapshot count lệch tối đa 1; đo cả actual hit-rate mỗi side




firstHitFrame

	

≤F2 trong isolated eligible tests




crowHitRate

	

Báo riêng 1, 2, 3 crows, và trường hợp tất cả cùng side; mục tiêu thử nghiệm ≥90% ở peak thực tế




lotusDamageShare

	

Báo full/half riêng, kiểm tra lotus thực sự gây damage




win, S, P, I, O, N, Q

	

Dùng định nghĩa và gates hiện hành trong BALANCE.md




Damage distribution

	

typedShare, key1Share, key2Share, autoAttackShare




Budget sensitivity

	

Chạy song song ground budget 1.25, 1.75, 2.0, 2.5 W mỗi side, giữ sky budget

sideBalance bổ sung tỷ lệ actualHitCount / snapshotSideCount cho từng side, không chỉ tỷ lệ hit tổng. Báo chênh lệch theo percentage points; thử ngưỡng 20 điểm phần trăm ở những fixture có hai side không rỗng.

5. Khuyến nghị về budget, damage share và hệ thống khác

Khuyến nghị triển khai: Giữ 2.0 W mỗi side làm trial đầu tiên, 0.8 W sky, không coi đây là cấu hình phát hành. Bước đầu tiên là kiểm tra F0/F1 positive-damage khi part budget nhỏ hơn nominal hit; nếu cơ chế hiện tại không hỗ trợ chi phần còn lại, dùng 2.5 W làm baseline để bảo đảm D58 mà không đổi damage machinery.

Quyết định của owner: Giữ canon key2Share <= 20%. Không âm thầm nâng giới hạn lên 40–50% chỉ vì bản cũ cần skill này để thắng.

Nhưng không thể đạt mục tiêu đó bằng cách giảm riêng ngân sách twin-pearl mà vẫn duy trì khả năng phòng thủ. Số liệu cũ đã cho thấy vấn đề:

2.0 W: khoảng 15.2 beasts hit nhưng key2Share vẫn rất cao.

2.5 W: 17.2 beasts hit và win 95–100%.

Không có dragon: win 0–40%, do các kỹ năng khác không đủ reach.

Vì vậy cần một pass cân bằng riêng biệt cho toàn bộ hệ thống tấn công:

Mở rộng hoặc cải thiện khả năng tiếp cận mục tiêu của key-1 và các kỹ năng khác, không sao chép field-wide reach sang mọi skill.

Đánh giá range và contribution của auto-attack để nó không bị key-2 thay thế hoàn toàn.

Chạy lại pacing, pressure và sức chịu đựng của waves sau khi sửa reach.

Chỉ sau đó điều chỉnh budget twin-pearl để đưa key2Share xuống ≤20% mà vẫn đạt win và các gates trong BALANCE.md.

Các thay đổi này không thuộc logic C1–C10. Phạm vi và mức điều chỉnh của chúng cần owner phê duyệt.

6. Rủi ro và các điểm chưa chắc chắn

Rủi ro

	

Kiểm chứng




Tuyến dài khiến đầu rồng di chuyển quá nhanh

	

Đo tốc độ cực đại theo stage; trước mắt giữ F3–F42, không cắt route




Hai rồng trùng nhau khi chỉ có một stream

	

Render hai đường và đo overlap; giữ S-offset đối dấu, chưa thêm heuristic




2.0 W gây hit zero nếu budget không thanh toán phần còn lại

	

Unit test một beast cho từng kind và budget part




Sky budget thiếu khi có 3 crows cùng side

	

Stress test riêng; chỉ thay số sky budget nếu bot xác nhận cần thiết




Lotus ít gây damage vì corridor đã dùng budget hoặc cooldown

	

Log candidate, accepted hit, rejected reason và remaining budget theo kind




Snapshot anchors trở nên cũ khi beasts di chuyển

	

So sánh coverageStatic với actual reach trên các bot seeds




Route samples quá nhiều trên stage rất lớn

	

Benchmark số samples, thời gian mỗi tick và giới hạn số nguyên an toàn; chưa thêm path cap tùy tiện




Mirror symmetry bị phá bởi tie hoặc odd count

	

Chỉ yêu cầu exact side swap trên fixtures không suy biến; kiểm thử các tie cases riêng




Coverage tốt nhưng key-2 vẫn thống trị trận

	

Đo share toàn trận sau khi sửa reach các kỹ năng khác

Không có bằng chứng đủ để khẳng định budget 2.0 W sẽ đạt đồng thời 12–20 hits, 90% crow hits và key2Share <= 20% trên hình học mới. Đó là ba kết quả cần đo, không được ghi thành kết quả đã đạt.

Quyết định cuối cùng: Chấp nhận thiết kế C1–C10 sau các sửa đổi trên, đặc biệt bỏ Lmax, giữ damage machinery và kiểm thử ngân sách hiện hữu. Chỉ chốt budget phát hành sau peak sweep và pass cân bằng reach toàn game.

---

#### fallback-turn-1:0:user · USER (Claude)

Review your latest full answer above against the brief, the facts and the constraints. Judge only what the brief asks of you: the damage machinery is fixed and given; code-level details belong to the coordinator's coding ticket; balance numbers that only the bot can measure are targets, not defects. It FAILS only for a real defect: a wrong fact, a step that would not work, a missing step the goal needs, a contradiction with the constraints or the owner's decisions, or a design rule whose result is ambiguous. Wording, style and optional extra ideas are not defects.
If it is correct and accurate, answer with exactly one line: VERDICT: PASS (you may add one line "Optional:" with ideas that do not change the verdict)
Otherwise answer: VERDICT: FAIL, then list each defect, then give the corrected FULL design (not a diff). If the full version does not fit in one message, stop at a section boundary, end with the line PART 1 OF N, and I will ask for the next part.

---

#### fallback-turn-1:2:assistant · CHATGPT

ChatGPT said:

VERDICT: FAIL

1. Các lỗi cần sửa

Bản trước đúng về hướng thiết kế tổng thể nhưng còn 4 lỗi thực sự cần khắc phục.

D1 — C5 chưa xác định duy nhất hình dạng đường bay. Quy tắc S-offset chưa quy định hướng pháp tuyến, cách chia đoạn thành samples và cách phân chia half-waves chính xác. Hai implementation hợp lệ theo mô tả cũ có thể tạo đường khác nhau, dẫn tới hit volumes và world hash khác nhau. Phải cố định các quy tắc hình học này.

D2 — C6/C10 chưa bảo đảm D58 với trial budget. Damage touch đầu tiên có nominal 0.375 W, nhưng touch part của ground budget 2.0 W chỉ có 0.300 W. Bản trước vừa yêu cầu hit trước F2 vừa cho phép một cấu hình mà khả năng thanh toán hit phụ thuộc vào cách xử lý budget chưa xác nhận. Không được sửa damage machinery để giải quyết việc này. Chọn 2.5 W làm baseline, giữ 2.0 W là thử nghiệm có điều kiện, và kiểm tra positive damage bằng machinery hiện hữu.

D3 — C1/C6 chưa khóa rõ thời điểm tạo F1 touch discs và tập mục tiêu. Bản trước liệt kê F1TouchDiscs trong dữ liệu được lưu tại F0 nhưng lại chọn mục tiêu tại F1, đồng thời chưa nói rõ có tính beasts mới sinh trong khoảng đó hay không. Phải lưu trạng thái chưa khởi tạo tại F0, chọn từ snapshot F0 còn sống tại F1, rồi cố định tâm disc.

D4 — Side-balance metric chưa nhất quán về quần thể. Bản trước lấy số beast của snapshot làm mẫu số nhưng có thể tính cả beast sinh sau F0 vào tử số. Điều này khiến hit rate có thể vượt 100% và làm sai phép so sánh. Phải chỉ đếm snapshot beasts trong cả tử số và mẫu số; báo riêng late spawns.

Không coi các mục tiêu coverage, số beast trúng đòn, win rate hay damage share chưa được bot kiểm chứng là lỗi. Các con số đó vẫn là test targets, không phải kết quả đã được chứng minh.

2. Corrected full design — twin-pearl
2.1. C1–C10
C1 — Snapshot

Tại F0, trước strike, đọc một lần fieldBounds, H, C và toàn bộ beasts đang sống, damageable, gồm serial, position, heightBand.

Lưu F, R, cut2, sideBySerial, P, anchors, routes, samples, passTicks, cùng trạng thái damage hiện hành. F1TouchDiscs chưa được tạo tại F0.

Beasts tiếp tục di chuyển bình thường. Mọi hit volume kiểm tra live positions.

Beasts mới xuất hiện sau snapshot được gán side khi xuất hiện lần đầu; không tham gia lựa chọn F1 targets hoặc anchors.

C2 — Frame and side split
Plain text
F = unitPm(H - C)

if F == (0, 0):
    F = unitPm(fieldCenter - H)

if F == (0, 0):
    F = (0, -1000)

R = (-F.z, F.x)

v(p) = mulDivSym(dot(p - H, R), 1, 1000)
u(p) = mulDivSym(dot(p - H, F), 1, 1000)

Sắp xếp snapshot theo (v, u, serial). side 0 nhận ceil(n/2) beasts đầu tiên; side 1 nhận phần còn lại. Ground và flyers cùng tham gia.

Plain text
if n >= 2:
    cut2 = v(lastSide0) + v(firstSide1)
else if n == 1:
    cut2 = 2 * v(singleBeast)
else:
    cut2 = 0

Beasts mới:

2*v < cut2: side 0.

2*v > cut2: side 1.

Bằng nhau: serial parity, chẵn vào side 0, lẻ vào side 1.

Side cố định suốt cast.

C3 — Pearl

G là mean position của ground beasts tại F0; nếu không có ground, dùng flyers; nếu không có beast, dùng fallback.

Plain text
P = H + 3/5 * (G - H)

Làm tròn đối xứng về integer u. Nếu distance(P,H) > 12m, scale vector về bán kính 12 m, sau đó clamp từng tọa độ vào field inset 2 m.

Nếu một chiều của field nhỏ hơn 4 m, giới hạn tọa độ chiều đó về midpoint.

Empty snapshot:

Plain text
P = clampInset(H + 9m * F / 1000)

Thứ tự scale rồi clamp là cố định; không chạy lặp lại.

C4 — Dragon routes

Mỗi side chọn tối đa ba ground anchors.

Anchor đầu tiên: beast xa H nhất, tie bằng serial nhỏ nhất.

Anchor tiếp theo: tối đa hóa khoảng cách nhỏ nhất tới {C, P, selectedAnchors}.

Dừng nếu khoảng cách tốt nhất nhỏ hơn 3 m hoặc đã có ba anchors.

Ties giải quyết bằng serial nhỏ nhất.

Duyệt tối đa sáu permutations; chọn polyline C -> anchors -> P có tổng Euclidean length nhỏ nhất, tính bằng integer isqrt, tie bằng lexicographic selection indices.

Không đặt Lmax; không xóa anchors vì đường dài.

Nếu side không có ground anchor:

Plain text
W_0 = clampInset(H - 9m * R / 1000)
W_1 = clampInset(H + 9m * R / 1000)

route_s = C -> W_s -> P

Gộp consecutive duplicate nodes. Trường hợp route có zero total length vẫn tạo một stationary sample.

C5 — Sampling and dragon body

Với mỗi segment A -> B:

Plain text
D = B - A
length = isqrt(dist2(A, B))
steps = max(1, ceil(length / 0.5m))
halfWaves = max(1, roundHalfUp(length / 4m))
N = unitPm(-D.z, D.x)

Tạo steps + 1 samples cách đều theo tỷ lệ j/steps, bằng integer symmetric rounding. Không nhân đôi sample chung của hai segments.

Đặt phase = halfWaves * j/steps. Phần nguyên xác định half-wave index, phần lẻ là f trong khoảng [0,1].

S-offset:

Plain text
shape(f) = 4*f*(1-f)

sign = (side == 0 ? +1 : -1)
       * (halfWaveIndex even ? +1 : -1)

offset = sign * 0.9m * shape(f) * N / 1000

Ở segment endpoints, offset bằng 0. Mọi phép tính dùng integer ratios, không floating-point trig. Clamp samples vào actual field bounds.

Tính lại cumulativeArc bằng integer distances giữa các samples sau offset và clamp.

Plain text
if totalArc > 0:
    pass[i] = 3 + mulDiv(39, cumulativeArc[i], totalArc)
else:
    pass[i] = 3

pass không giảm; sample đầu tại F3, sample cuối tại F42 nếu arc khác 0.

Ground body là các discs bán kính 1.4 m, ground band 0–1.5 m:

Plain text
pass[i] <= tick <= pass[i] + 54

Damage kind corridor. Không cần thêm sweep grid hoặc interpolation machinery.

C6 — F0 strike and F1 touches

F0: ground disc bán kính 4.5 m tại H, kind touch.

Tại F1, với mỗi side, tìm beast thuộc snapshot F0 còn sống, damageable, chưa nhận touch ở F0, gần H nhất theo live position F1; tie bằng serial nhỏ nhất.

Tạo disc bán kính 2.2 m tại live position F1, trong height band của beast được chọn. Tâm đứng yên; active F1–F2.

Chỉ chọn một target cho mỗi side. Nếu side không còn target hợp lệ, không tạo disc.

Baseline touch budget phải cho phép ít nhất một positive touch trong isolated eligible test. D58 yêu cầu first positive hit chậm nhất F2, ngoại trừ những trường hợp machinery cố định khiến mọi damage bằng 0 hoặc toàn bộ mục tiêu không còn damageable.

C7 — Sky volumes

F30–F50:

Current head là sample có index lớn nhất với pass <= min(tick,42).

Sky capsule bán kính 2.5 m nối head với từng sky anchor F0 của cùng side.

Sky discs bán kính 2.5 m tại active body samples.

Sky band 2.5–6 m, chỉ đánh flyers.

Kind corridor, chi từ sky budget part. Anchors không di chuyển theo crows.

C8 — Lotus

F51–F71, tại P, ground only, outer radius 9 m.

full region là giao của outer disc với hợp các vùng:

Plain text
disc(P, 4m)
OR disc(H, 4.5m)
OR capsule(last13m(route_0), 2.2m)
OR capsule(last13m(route_1), 2.2m)

last13m tính ngược từ P theo sampled arc. Nếu route ngắn hơn 13 m, lấy toàn bộ.

Phần còn lại của outer disc là half region, nhận 50% nominal lotus damage.

C9 — Timing

Frame

	

Event




F0

	

Caster release + ground strike




F1–F2

	

Touch discs




F3–F42

	

Dragon heads advance




F30–F50

	

Sky volumes




F43–F50

	

Roar, không thêm hit volume




F51–F71

	

Lotus




F72–F96

	

Ground trails còn damage




F97–F300

	

Visual decay only

Charge xảy ra trong lúc typing. Không thêm startup delay sau F0.

C10 — Damage and budgets

Giữ nguyên machinery và nominal damage:

touch = 15% * 2.5 W

corridor = 45% * 2.5 W

lotus = 40% * 2.5 W

lotusHalf = 50% * lotus

sky là corridor kind dùng riêng sky budget.

Falloff mỗi side: 100%, 85%, 70%, 55%, floor 40%.

Mỗi beast tối đa một hit mỗi kind, re-hit cách ít nhất 20 ticks.

Giữ cluster cap 60%, boss cap 1.5 W/cast, M_q, seat bucket, thứ tự (kind, distanceToHeart, serial) và quy tắc chi budget hiện hữu.

Chọn baseline:

Plain text
groundBudgetPerSide = 2.5 W
groundParts = [15%, 45%, 40%]
skyBudgetPerSide = 0.8 W

2.0 W chỉ là comparison trial; không chọn làm cấu hình cuối nếu D58 không đạt dưới machinery thực tế. Không thêm quy tắc partial payment hoặc thay đổi thứ tự xử lý damage.

3. Walk-throughs

Các độ dài là ước lượng control polyline cho fixtures dưới đây, trước S-offset. Chúng không phải kết quả đo damage.

Case

	

Side split

	

Routes và pearl

	

12–20 distinct hits




two-gate, 40

	

20/20

	

Mỗi rồng đi qua ba anchors của stream trái/phải, rồi quay về P≈(0,-5.7). Mỗi route ~47 m.

	

Reachable; đo bằng bot




one-gate, 40

	

20/20

	

Hai rồng đi dọc hai nửa của một stream hẹp, tới z≈-17 rồi trở về P≈(0,-6.2). ~31 m mỗi route.

	

Reachable; nguy cơ overlap




three-gate, 43

	

22/21

	

Side 0 nối cụm trái và giữa; side 1 nối cụm phải và giữa. P≈(0,-4.7). ~63 m mỗi route.

	

Reachable; chưa bảo đảm budget




open-arena, 44

	

22/22

	

Hai rồng phân chia theo lateral position, đi qua các điểm xa của nửa sân tương ứng và hội tụ tại H. ~57 m và ~69 m.

	

Reachable; thử thách lớn nhất




behind-caster, 40

	

20/20

	

Hai đường xòe sang trái/phải phía sau caster, rồi quay về P≈(-0.3,3.3). ~38 m mỗi route.

	

Reachable




lone, 1

	

1/0

	

Dragon 0: C -> (0,7) -> (0,4.2), ~6.8 m. Dragon 1 dùng wing loop ~19.4 m.

	

N/A; first hit by F2




empty, 0

	

0/0

	

Hai wing loops đối xứng, P=(0,-9), ~22.2 m mỗi route.

	

N/A; geometry preview only

Việc chia hai side theo median của vị trí beasts giúp các routes tự thích nghi với số hướng xuất hiện của địch. Tuy nhiên, đây vẫn là một cơ chế đi qua số lượng anchors hữu hạn, không bảo đảm chạm mọi điểm của mọi sân.

Mục tiêu 12–20 là số actual distinct beasts receiving positive damage, không phải số beasts nằm trong hit volumes.

4. Test plan
4.1. Synthetic layouts

Tất cả coordinates dưới đây tính bằng mét; chuyển sang integer u trước khi đưa vào sim.

Mặc định H=(0,0), C=(0,3), ground y=0, flyers y=4.

Dùng một species ground thông thường đã tồn tại trong game, không phải boss hoặc swarm đặc biệt. Flyers dùng Hoa Nha. Không tạo species ID mới chỉ để test.

Fixture

	

Bounds

	

Population




two-gate

	

x[-20,20], z[-18,8]

	

38 ground: sign ∈ {-1,+1}, i=0..18, x=sign*(15+(i%3)-1), z=-17+15*i/18. Hai crows: (-19,-12), (19,-12). Total 40.




one-gate

	

Như trên

	

38 ground: i=0..37, x=0.5*((i%5)-2), z=-17+2*floor(i/5). Hai crows: (-2,-16), (2,-16). Total 40.




three-gate

	

Như trên

	

14 left: x=-18+0.75*(i%3), z=-14+4*floor(i/3); 14 right là ảnh gương; 12 middle: x=0.8*((i%3)-1), z=-17+4*floor(i/3). Crows (-18,-14), (0,-16), (18,-14). Total 43.




open-arena

	

x[-20,20], z[-20,20]

	

40 ground: tám hướng (±1,0), (0,±1), (±0.7,±0.7), tại radius scales 5,8,11,14,17. Crows (±15,0), (0,±15). Total 44.




behind-caster

	

Bounds hiện tại

	

38 ground: i=0..37, x=-18+3*(i%13), z=4+1.5*floor(i/13). Hai crows (-17,7), (17,7). Total 40.




lone

	

Bounds hiện tại

	

Một ground beast (0,7).




empty

	

Bounds hiện tại

	

Không có beast; chỉ kiểm tra geometry generation.

Fixture open-arena cố ý sử dụng bốn crows để stress-test, nhiều hơn mức 1–3 crows thường gặp của bản đồ hiện tại.

Tất cả fixtures phải xác định serial ổn định theo thứ tự tạo beasts.

4.2. Static geometric coverage

Định nghĩa:

Plain text
coverageStatic =
    coveredSnapshotBeasts / totalSnapshotBeasts

Một snapshot beast được tính covered nếu vị trí F0 cố định của nó giao với ít nhất một hit volume trong F0–F96 và có height band hợp lệ.

Quy trình:

Freeze positions tại F0.

Replay geometry F0–F96.

Tạo F1 touches từ snapshot beasts chưa được F0 disc bao phủ.

Ignore HP, damage budget, swarm cap và re-hit interval.

Count distinct snapshot serials một lần.

Mục tiêu thử nghiệm: coverageStatic >= 75% cho mỗi fixture có 35–45 beasts.

Báo riêng groundCoverageStatic và flyerCoverageStatic.

Metric này đo khả năng bao phủ hình học, không dự đoán trực tiếp actual hits.

4.3. Mirror and rotation invariance

Mirror check: Dùng two-gate, biến đổi mọi tọa độ và velocity theo T(x,z)=(-x,z), giữ serial đi cùng beast.

Yêu cầu:

P và control geometry phản chiếu tương ứng.

side 0 và side 1 hoán đổi.

Sample positions sau inverse transform khớp chính xác.

Hit serial, frame, positive damage, HP và budget spending khớp.

Tolerance: 0 u, 0 HP, 0 ticks.

Chỉ yêu cầu exact side swap với fixture không có median ties và có số lượng side bằng nhau. Với odd counts hoặc ties tại median, canonical side assignment có thể không đối xứng; kiểm tra chúng theo deterministic rules thay vì áp đặt side swap.

Rotation check: Dùng two-gate và three-gate; xoay bounds, H, C, beasts và velocity 90°:

Plain text
T(x,z) = (-z,x)

Sau inverse transform, geometry và event traces phải khớp chính xác. Side labels giữ nguyên.

Không yêu cầu rotational invariance cho trường hợp hoàn toàn suy biến H=C=fieldCenter, vì fallback (0,-1000) cố định trong world coordinates.

4.4. Determinism and regression

Chạy cùng seed, inputs, rules trên các môi trường JS được hỗ trợ.

Yêu cầu:

Same world hash tại mọi tick.

Same cast record, route samples, pass ticks, hit events và budgets.

State chỉ chứa integers; mọi bình phương khoảng cách và phép nhân phải nằm trong safe integer range.

Không dùng floating-point trig hoặc sqrt trong sim.

flag=false: rulesHash, world hashes, event logs và match result byte-identical với baseline cũ.

flag=true: trial parameters được bao gồm trong rulesHash.

Unit tests riêng cho F0/F1 phải bao gồm một ground beast xa H, một flyer duy nhất, beasts chỉ phía sau caster, nhiều beasts trong F0 disc, và một mục tiêu nằm sát cluster cap.

Kiểm tra first positive hit ≤F2 cho tất cả eligible isolated cases. Log nguyên nhân khi machinery cố định khiến damage bằng 0.

4.5. Bot measurements

Chạy lại cùng bộ bot và seeds của benchmark cũ trên map hiện tại, đặc biệt các cast tại 35–45 alive.

Metric

	

Definition / target




distinctHitsPerCast

	

Positive-damage distinct serials; target p10 >= 12, p90 <= 20




coverageStatic

	

Target ≥75% trên từng fixture peak




sideBalance

	

Snapshot sizes lệch tối đa 1; đo actual hit rate mỗi side




sideHitRate

	

Snapshot serials hit trên mỗi side / snapshot serials của side đó




firstHitFrame

	

Positive damage chậm nhất F2 trong eligible tests




crowHitRate

	

Snapshot crows nhận positive damage trước F97 / eligible snapshot crows; mục tiêu peak ≥90%




lotusContribution

	

Damage từ full lotus và half lotus riêng




win, S, P, I, O, N, Q

	

Theo định nghĩa và gates hiện có trong BALANCE.md




typedShare

	

Damage từ typed skills / total match damage




key1Share

	

Theo mẫu số typed damage quy định hiện hữu




key2Share

	

Key-2 match damage / total match damage




autoAttackShare

	

Auto-attack damage / total match damage

Beasts sinh sau F0 không được cộng vào sideHitRate của snapshot; báo riêng lateSpawnHits.

So sánh ground budgets 1.25, 1.75, 2.0, 2.5 W, giữ sky budget 0.8 W. Mỗi cấu hình phải qua D58 trước khi được xét về balance.

Kiểm tra thêm runtime cost với tối đa 60 beasts và hai casts đồng thời, hướng tới ≤50 µs/tick/cast trong JS trên kích thước stage được hỗ trợ.

5. Share target, budget và các hệ thống cần thay đổi
Budget recommendation

Chọn groundBudgetPerSide = 2.5 W làm implementation baseline đầu tiên để tránh giả định về việc thanh toán touch damage.

Giữ skyBudgetPerSide = 0.8 W, vì cấu hình cũ đã ghi nhận crow hits với cùng mức này. Tuy nhiên vẫn phải xác nhận cơ chế budget hiện hữu cho sky kind bằng isolated tests.

Sau khi baseline đạt determinism, D58 và coverage, chạy sweep để xem 2.0 W có thể giảm damage share mà vẫn đáp ứng các gates hay không.

Không coi bất kỳ ngân sách nào là final trước khi có kết quả bot.

Owner decision — damage share

Giữ canon key2Share <= 20%, trừ khi owner chủ động thay đổi chuẩn cân bằng.

Dữ liệu cũ cho thấy không thể giải quyết vấn đề chỉ bằng cắt budget của twin-pearl. Kỹ năng này hiện là nguồn damage và reach chủ đạo, trong khi key-1 và auto-attack không tiếp cận đủ số enemies trước khi chúng tới heart.

Cần một balance pass riêng cho:

Key-1 reach: cải thiện khả năng đánh enemies ở xa để key-2 không trở thành lựa chọn bắt buộc.

Other skill reach: kiểm tra các kỹ năng cùng trường phái và nguyên tố, không chuyển toàn bộ chúng thành field-wide AoE.

Auto-attack reach/contribution: khôi phục vai trò hữu ích mà không làm mất sự ưu tiên của typed attacks.

Wave pacing and pressure: cân bằng lại sau khi tăng reach các hệ thống khác.

Chỉ điều chỉnh numbers của twin-pearl sau khi những hệ thống này được kiểm tra cùng nhau.

Owner cần phê duyệt: phạm vi thay đổi reach của các kỹ năng khác, canon 20% nếu có ngoại lệ, và final release budget.

6. Risks and unresolved questions

Risk

	

Validation




Route dài trên bản đồ lớn làm head travel quá nhanh

	

Đo tốc độ và tính đọc được của animation tại F3–F42




Fixed sample spacing tạo chi phí quá lớn trên stage rộng

	

Benchmark sample count, memory và 50 µs target; xác định giới hạn kích thước stage được hỗ trợ




Một stream khiến hai rồng overlap

	

Đo overlap của hit volumes; chưa cần thêm routing heuristic




Pearl lệch về một cụm quá xa

	

Kiểm tra synthetic layouts với phân bố rất bất đối xứng




Sky budget thiếu với nhiều crows cùng side

	

Đo actual crow hits và budget exhaustion




Lotus không tạo được meaningful damage vì cooldown hoặc budget

	

Log lotus candidates, accepted hits và rejected reasons




Static coverage cao nhưng actual hits thấp

	

So sánh coverageStatic và distinctHitsPerCast trên cùng snapshots




Geometry mới làm key-2 tiếp tục áp đảo

	

Đo match-wide share sau balance pass của các kỹ năng khác




Floating-point hoặc số nguyên vượt safe range

	

Determinism cross-runtime và integer-range assertions

Điểm chưa chắc chắn quan trọng nhất là budget exhaustion và actual damage distribution trên hình học mới. Các thông số hình học có thể triển khai và kiểm chứng độc lập; không có cơ sở để tuyên bố trước rằng chúng sẽ đạt đồng thời 12–20 actual hits, 90% crow hits, balanced wins và key-2 share ≤20%.

Final recommendation: Chấp nhận thiết kế chia median, ba anchors mỗi side, không giới hạn path length, hai dragon bodies và một lotus tại pearl. Triển khai baseline 2.5 W trước, giữ machinery hiện hữu, rồi chọn ngân sách phát hành bằng bot measurements.

---

#### fallback-turn-2:0:user · USER (Claude)

Review your latest full answer above (the corrected full design) against the brief, the facts and the constraints. Judge only what the brief asks of you: the damage machinery is fixed and given; code-level details belong to the coordinator's coding ticket; balance numbers that only the bot can measure are targets, not defects. It FAILS only for a real defect: a wrong fact, a step that would not work, a missing step the goal needs, a contradiction with the constraints or the owner's decisions, or a design rule whose result is ambiguous. Wording, style and optional extra ideas are not defects.
If it is correct and accurate, answer with exactly one line: VERDICT: PASS (you may add one line "Optional:" with ideas that do not change the verdict)
Otherwise answer: VERDICT: FAIL, then list each defect, then give the corrected FULL design (not a diff). If the full version does not fit in one message, stop at a section boundary, end with the line PART 1 OF N, and I will ask for the next part.

---

#### fallback-turn-2:2:assistant · CHATGPT

ChatGPT said:

VERDICT: PASS

---

#### fallback-turn-3:0:user · USER (Claude)

Review your latest full design above (the corrected full design two messages up) once more against the brief, the facts and the constraints. Judge only what the brief asks of you: the damage machinery is fixed and given; code-level details belong to the coordinator's coding ticket; balance numbers that only the bot can measure are targets, not defects. It FAILS only for a real defect: a wrong fact, a step that would not work, a missing step the goal needs, a contradiction with the constraints or the owner's decisions, or a design rule whose result is ambiguous. Wording, style and optional extra ideas are not defects.
If it is correct and accurate, answer with exactly one line: VERDICT: PASS (you may add one line "Optional:" with ideas that do not change the verdict)
Otherwise answer: VERDICT: FAIL, then list each defect, then give the corrected FULL design (not a diff). If the full version does not fit in one message, stop at a section boundary, end with the line PART 1 OF N, and I will ask for the next part.

---

#### fallback-turn-3:2:assistant · CHATGPT

ChatGPT said:

VERDICT: FAIL

1. Các lỗi thực sự

Sau khi đối chiếu lại với damage machinery cố định, thiết kế trước còn hai lỗi cần sửa.

D1 — C6 vi phạm quy tắc sky damage. Thiết kế dùng touch kind và touch budget cho F1 disc của flyer. Nhưng brief quy định rõ: mọi sky hit phải dùng corridor kind và chi từ sky budget. Vì vậy F1 disc của flyer không thể sử dụng cùng damage kind với ground touch.

Sửa: F1 ground disc giữ touch kind và touch budget; F1 sky disc sử dụng corridor kind và sky budget. Đây chỉ là sửa loại hit cho phù hợp với machinery có sẵn, không tạo damage rule mới.

D2 — Quy tắc chọn F1 target chưa loại trừ trường hợp không thể gây positive damage. Một beast gần H nhất có thể đã bị cluster cap chặn toàn bộ sát thương, trong khi beast khác cùng side vẫn có thể nhận sát thương. Nếu F1 luôn chọn beast gần nhất mà không kiểm tra khả năng nhận positive damage, Cast có thể không đạt D58 mặc dù còn mục tiêu hợp lệ.

Sửa: F1 chọn beast gần H nhất trong các snapshot beasts còn sống, chưa nhận kind tương ứng và có khả năng nhận positive damage theo machinery hiện hữu. Nếu không có ứng viên như vậy, không tạo F1 disc cho side đó. Không thay đổi cap hoặc cách tính damage.

Các mục tiêu về 12–20 distinct hits, coverage, tỷ lệ thắng và damage share vẫn là mục tiêu kiểm thử, không phải lỗi chỉ vì chưa có kết quả bot.

2. Corrected full design — Twin Dragons, One Burning Pearl

Skill: twin-pearl (雙龍戲珠), Sword key 2.

C1–C10: Final specification
C1 — Snapshot

Tại F0, trước strike, snapshot một lần fieldBounds, H, C và mọi beast đang sống, damageable, gồm serial, x, z, y, heightBand.

Lưu F, R, cut2, sideBySerial, P, groundAnchors, skyAnchors, routeNodes, samples, passTicks và trạng thái damage của cast.

F1Discs chưa khởi tạo tại F0; chúng được xác định một lần tại F1.

Beasts tiếp tục di chuyển. Mọi volume xét live positions ở tick hiện hành. Beasts mới sinh sau F0 được gán side cố định khi xuất hiện lần đầu; không tham gia chọn anchors hoặc F1 target.

C2 — Coordinate frame and side split
Plain text
F = unitPm(H - C)
if F == (0,0): F = unitPm(fieldCenter - H)
if F == (0,0): F = (0,-1000)

R = (-F.z, F.x)

v(p) = mulDivSym(dot(p-H, R), 1, 1000)
u(p) = mulDivSym(dot(p-H, F), 1, 1000)

Sort snapshot theo (v, u, serial).

side 0 nhận ceil(n/2) beasts đầu.

side 1 nhận số còn lại.

Ground và flyers cùng tham gia.

Plain text
if n >= 2:
    cut2 = v(lastSide0) + v(firstSide1)
else if n == 1:
    cut2 = 2*v(single)
else:
    cut2 = 0

Beasts sinh sau F0:

Plain text
2*v < cut2  -> side 0
2*v > cut2  -> side 1
2*v == cut2 -> side = serial % 2

Side không thay đổi trong cast.

C3 — Pearl placement

G là mean position của snapshot ground beasts. Nếu không có ground, dùng tất cả flyers.

Plain text
P = H + 3/5*(G-H)

Nếu distance(P,H)>12m, scale về bán kính 12 m theo vector P-H.

Sau đó clamp vào field inset 2 m. Nếu chiều field nhỏ hơn 4 m, giới hạn tọa độ chiều đó tại midpoint.

Empty snapshot:

Plain text
P = clampInset(H + 9m*F/1000)

Mọi phép tính và rounding dùng integer arithmetic. Scale và clamp chỉ thực hiện một lần theo đúng thứ tự.

C4 — Dragon routes

Mỗi side chọn tối đa K=3 ground anchors từ snapshot.

Anchor đầu là beast xa H nhất.

Anchor tiếp theo tối đa hóa minimum squared distance tới {C, P, selectedAnchors}.

Dừng nếu khoảng cách tốt nhất nhỏ hơn 3 m hoặc đủ ba anchors.

Tie bằng serial nhỏ nhất.

Duyệt tối đa sáu permutations. Chọn đường có tổng integer Euclidean length nhỏ nhất:

Plain text
C -> anchor[0] -> anchor[1] -> anchor[2] -> P

Tie bằng lexicographic selection indices.

Không có Lmax, không xóa anchor vì route dài.

Nếu side không có ground anchors:

Plain text
W_0 = clampInset(H - 9m*R/1000)
W_1 = clampInset(H + 9m*R/1000)

route_s = C -> W_s -> P

Gộp consecutive duplicate nodes. Route có zero length tạo một stationary sample.

C5 — Sampling and body

Với từng segment A -> B:

Plain text
length = isqrt(dist2(A,B))
steps = max(1, ceil(length/0.5m))
halfWaves = max(1, roundHalfUp(length/4m))
normal = unitPm(-(B.z-A.z), B.x-A.x)

Lấy steps+1 samples cách đều bằng integer interpolation, không nhân đôi shared endpoints.

Half-wave phase được phân chia chính xác bằng tỷ lệ halfWaves*j/steps. Với fractional phase f, áp dụng:

Plain text
shape = 4*f*(1-f)
sign = sideSign * alternatingHalfWaveSign
offset = sign * 0.9m * shape * normal/1000

sideSign dương cho side 0, âm cho side 1. Half-wave đầu tiên dương, sau đó đổi dấu luân phiên. Ở segment endpoints, offset bằng 0.

f, shape và offset tính bằng integer ratios; không dùng floating-point trigonometry.

Clamp samples vào actual field bounds.

Tính lại cumulative arc từ sampled polyline bằng isqrt:

Plain text
pass[i] = 3 + mulDiv(39, cumulativeArc[i], totalArc)

Nếu totalArc==0, mọi sample có pass=3.

Ground body gồm discs bán kính 1.4 m:

Plain text
pass[i] <= tick <= pass[i]+54

Ground band 0–1.5 m. Damage kind corridor, budget part corridor.

C6 — F0 strike and F1 discs

F0: Ground disc tại H, radius 4.5 m, kind touch, part touch.

F1: Với từng side, chọn snapshot beast gần H nhất theo live position F1, tie bằng serial nhỏ nhất, thỏa:

Vẫn sống và damageable.

Chưa nhận kind tương ứng trong cast.

Có thể nhận positive damage theo budget và caps hiện hữu.

Ground target tạo disc radius 2.2 m tại vị trí F1, ground band, kind touch, part touch.

Flyer target tạo disc radius 2.2 m tại vị trí F1, sky band, kind corridor, part sky.

Các discs tồn tại F1–F2, có tâm cố định. Nếu không có target hợp lệ, side đó không tạo disc.

Đây là volume sớm, không phải một loại damage mới. Flyer nhận corridor tại F1 sẽ không thể nhận thêm corridor trong cast.

Trong isolated eligible tests, first positive hit phải xảy ra chậm nhất cuối F2. Các trường hợp machinery hiện hữu thực sự chặn mọi positive damage phải được ghi rõ, không âm thầm coi là hit thành công.

C7 — Sky coverage

F30–F50:

Head sample là sample cuối cùng có pass <= min(tick,42).

Tạo sky capsule radius 2.5 m từ projected head position tới từng sky anchor F0 của side.

Tạo sky disc radius 2.5 m tại mọi active body sample.

Các capsule và discs là vùng theo mặt phẳng x,z, được xét trong sky band 2.5–6 m; không phải capsule 3D nối từ mặt đất lên flyer.

Chỉ flyers nhận damage.

Kind corridor, part sky.

Sky anchors cố định theo F0; không bám theo crows.

C8 — Lotus climax

F51–F71. Lotus nằm tại P, ground only.

Outer radius 9 m. Full damage khi beast nằm trong outer disc và trong ít nhất một vùng:

Plain text
disc(P,4m)
OR disc(H,4.5m)
OR capsule(last13m(route_0),2.2m)
OR capsule(last13m(route_1),2.2m)

last13m là phần cuối của sampled polyline, đo ngược từ P theo arc length, gồm phần segment tại đúng điểm cắt 13 m.

Nếu route ngắn hơn 13 m, dùng toàn bộ route.

Ngoài full region nhưng vẫn trong outer disc: half damage 50%.

Kind lotus, part lotus.

Không dựa vào cổng, làn đường hay waypoint.

C9 — Timeline

Frame

	

Event




F0

	

Caster release và strike tại H




F1–F2

	

Ground/sky early discs




F3–F42

	

Dragon heads advance




F30–F50

	

Sky coverage




F43–F50

	

Roar, không tạo damage volume mới




F51–F71

	

Lotus climax




F72–F96

	

Ground trails tiếp tục gây damage




F97–F300

	

Visual decay only

Caster-side release thể hiện ngay F0. Charge diễn ra trong lúc typing. Không thêm startup delay.

C10 — Fixed damage machinery and budget

Giữ nguyên:

Hit

	

Nominal damage

	

Budget part




Ground touch

	

15% * 2.5 W

	

touch




Ground corridor

	

45% * 2.5 W

	

corridor




Sky corridor

	

45% * 2.5 W

	

sky




Full lotus

	

40% * 2.5 W

	

lotus




Half lotus

	

50% * fullLotus

	

lotus

Giữ M_q, seat bucket, per-side falloff 100/85/70/55/40%, mỗi beast tối đa một hit mỗi kind, re-hit interval tối thiểu 20 ticks, swarm cap 60%, boss cap 1.5 W/cast và thứ tự strike (kind, distanceToHeart, serial).

Baseline đầu tiên:

Plain text
groundBudgetPerSide = 2.5 W
groundBudgetSplit = [15%,45%,40%]
skyBudgetPerSide = 0.8 W

2.0 W là comparison trial, không phải release default.

Không thêm partial-payment rule, đổi nominal damage hoặc thay đổi damage processing. Kiểm tra F1 sky positive damage với 0.8 W bằng machinery hiện hữu; dữ liệu crows của bản cũ là bằng chứng thực nghiệm hữu ích nhưng không thay thế isolated F1 test.

3. Walk-throughs

Các độ dài là ước lượng control-polyline length, không bao gồm S-offset. Chúng không phải kết quả đo damage.

Layout

	

Side split

	

Routes

	

12–20 distinct hits




two-gate, 40

	

20/20

	

Dragon 0 qua anchors stream trái, Dragon 1 qua stream phải; cùng về P≈(0,-5.7); khoảng 45–55 m mỗi route

	

Khả thi, cần bot xác nhận




one-gate, 40

	

20/20

	

Hai rồng đi qua hai nửa cùng stream giữa, rồi hội tụ tại P≈(0,-6.2); khoảng 30–35 m

	

Khả thi; nguy cơ overlap




three-gate, 43

	

22/21

	

Hai rồng nối anchors của stream trái/giữa và phải/giữa; P≈(0,-4.7); khoảng 55–70 m

	

Khả thi; cần đo actual coverage




open-arena, 44

	

22/22

	

Hai rồng bao quát các điểm neo phân tán trên nửa sân tương ứng, rồi về H; khoảng 55–75 m

	

Khả thi; khó nhất về khoảng cách




behind-caster, 40

	

20/20

	

Hai tuyến xòe qua các cụm phía z dương, rồi về P≈(-0.3,3.3); khoảng 35–45 m

	

Khả thi




lone, 1

	

1/0

	

Dragon 0 qua beast (0,7) rồi về P=(0,4.2), ~6.8 m. Dragon 1 wing loop ~19.4 m

	

Không áp dụng 12–20; phải đạt D58




empty, 0

	

0/0

	

Hai wing loops đối xứng, P=(0,-9), ~22.2 m mỗi route

	

Chỉ geometry preview

Tại peak 35–45 alive, 12–20 actual distinct hits là mục tiêu đo, không phải hệ quả chắc chắn của hình học.

4. Test plan
4.1. Synthetic fixtures

Đặt H=(0,0), C=(0,3), đơn vị mét; ground y=0, crows y=4. Dùng ground species thông thường của game và flyer species Hoa Nha. Serial được gán theo thứ tự tạo trong từng fixture.

Fixture

	

Bounds

	

Beasts




two-gate

	

[-20,20] × [-18,8]

	

38 ground: sign ∈ {-1,+1}, i=0..18, x=sign*(15+(i%3)-1), z=-17+15*i/18; 2 crows (-19,-12),(19,-12)




one-gate

	

Như trên

	

38 ground: i=0..37, x=0.5*((i%5)-2), z=-17+2*floor(i/5); 2 crows (-2,-16),(2,-16)




three-gate

	

Như trên

	

14 left: x=-18+0.75*(i%3), z=-14+4*floor(i/3); 14 right mirror; 12 middle: x=0.8*((i%3)-1), z=-17+4*floor(i/3); 3 crows (-18,-14),(0,-16),(18,-14)




open-arena

	

[-20,20] × [-20,20]

	

40 ground: tám hướng (±1,0),(0,±1),(±0.7,±0.7) nhân với 5,8,11,14,17; 4 crows (±15,0),(0,±15)




behind-caster

	

Bounds hiện tại

	

38 ground: i=0..37, x=-18+3*(i%13), z=4+1.5*floor(i/13); 2 crows (-17,7),(17,7)




lone

	

Bounds hiện tại

	

Một ground beast (0,7)




empty

	

Bounds hiện tại

	

Không có beast, geometry preview

Tất cả phép tạo tọa độ được lượng tử hóa thành integer u trước khi khởi tạo sim. open-arena cố ý có bốn crows để stress-test, dù wave hiện tại thường chỉ có 1–3.

4.2. Coverage metric

Định nghĩa:

Plain text
coverageStatic =
    coveredSnapshotBeasts / damageableSnapshotBeasts

Freeze tất cả beasts tại F0. Replay volumes F0–F96, gồm F1 discs được tạo từ snapshot cố định, bỏ qua HP, budget, caps và cooldown.

Một beast được tính covered một lần nếu có vị trí và height band giao với bất kỳ damage volume nào.

Mục tiêu đề xuất: coverageStatic >= 75% trên từng fixture 35–45 alive.

Báo riêng ground và sky coverage.

Đây là geometric reach metric, không phải actual damage metric.

4.3. Mirror and rotation

Mirror: Trên two-gate, biến đổi:

Plain text
T(x,z) = (-x,z)

Giữ serial gắn với beast; phản chiếu tất cả positions và velocities.

Với fixture có hai side bằng nhau, không có median ties:

Side labels phải hoán đổi.

Pearl và routes phải phản chiếu.

Samples sau inverse transform phải trùng.

Hit serials, hit ticks, HP damage và budget spending phải giống.

Tolerance: 0 u, 0 HP, 0 ticks.

Không yêu cầu hoán đổi side tuyệt đối ở các fixtures có odd counts hoặc median ties.

Rotation: Trên two-gate và three-gate:

Plain text
T(x,z) = (-z,x)

Xoay bounds, H, C, beasts và velocities. Sau inverse transform, geometry và hit-event traces phải khớp với tolerance 0.

Không yêu cầu rotation invariance đối với fallback suy biến H=C=fieldCenter, vì hướng (0,-1000) được cố định trong world coordinates.

4.4. Determinism, D58 and golden

Kiểm tra:

Same seed, inputs và rules → same world hash mọi tick.

Cast state chỉ có integers; không dùng float trig hoặc float sqrt.

Mọi phép tính nằm trong JS safe-integer range.

Tối đa 60 live beasts, hai concurrent casts.

flag=false: rulesHash, world hash, events và match results byte-identical với baseline cũ.

flag=true: trial data tham gia rulesHash.

Isolated D58 tests gồm:

Ground beast xa H.

Một flyer duy nhất.

Beasts phía sau caster.

Beasts trong F0 disc.

Trường hợp swarm cap chặn damage ở target gần nhất nhưng còn target khác hợp lệ.

Ground và flyer cùng side, cần chọn theo eligibility thực tế.

Trong eligible cases, first positive hit ≤F2. Log riêng trường hợp không còn target hoặc mọi positive damage bị machinery cố định chặn.

4.5. Bot measurements

Chạy cùng benchmark methodology cũ: 17 profiles × 20 seeds, peak sweeps tại 35–45 alive, đồng thời kiểm tra synthetic layouts.

Metric

	

Requirement




distinctHitsPerCast

	

Positive-damage distinct serials; target p10 ≥12, p90 ≤20




coverageStatic

	

Target ≥75% trên từng peak fixture




snapshotSideBalance

	

Chênh lệch snapshot count ≤1




sideHitRate

	

Snapshot serials nhận positive damage / snapshot serials của side; báo riêng mỗi side




lateSpawnHits

	

Báo riêng, không đưa vào snapshot side-hit rate




firstHitFrame

	

≤F2 trong eligible isolated tests




crowHitRate

	

Snapshot crows nhận positive damage trước F97 / eligible snapshot crows; target ≥90% peak




lotusContribution

	

Full và half lotus damage riêng




win, S, P, I, O, N, Q

	

Theo gates hiện hành của BALANCE.md




typedShare

	

Typed damage / total match damage




key1Share

	

Theo mẫu số typed damage hiện hành




key2Share

	

Key-2 damage / total match damage




autoAttackShare

	

Auto-attack damage / total match damage

Budget comparison: 1.25, 1.75, 2.0, 2.5 W ground per side, sky 0.8 W, giữ nguyên nominal damage và machinery.

Đo tick cost, số samples và memory usage; performance target ≤50 µs/tick/cast trong giới hạn sân được hỗ trợ.

5. Budget và damage share

Khuyến nghị: Bắt đầu với 2.5 W ground mỗi side và 0.8 W sky mỗi side. Giữ 2.0 W làm trial để kiểm tra khả năng giảm key-2 dominance.

Bắt buộc chạy isolated D58 tests, nhất là lone flyer sử dụng F1 sky corridor. Nếu sky budget hiện hữu không thể thanh toán positive damage, chỉ được điều chỉnh budget number, không đổi damage machinery.

Quyết định thuộc owner: Canon key2Share <= 20% tiếp tục có hiệu lực. Không tự ý nâng lên 40–50%.

Theo số liệu cũ, giảm riêng budget không giải quyết được tỷ lệ damage quá lớn của key-2 trong khi vẫn duy trì win rate. Cần một balance pass riêng cho:

Key-1 reach.

Reach và contribution của các typed skills khác.

Auto-attack reach và contribution.

Wave pacing, pressure và survivability sau các điều chỉnh reach.

Chạy lại toàn bộ metrics trước khi chốt release budget. Mức tăng reach cụ thể và bất kỳ ngoại lệ nào với canon 20% đều do owner quyết định.

6. Risks and uncertainties

Risk

	

Verification




Long routes khiến đầu rồng quá nhanh

	

Đo tốc độ và khả năng đọc hình ảnh tại F3–F42




Một stream khiến hai rồng overlap

	

Đo overlap của hit volumes; chưa thêm routing heuristic




F1 sky corridor tiêu thụ sky budget sớm

	

So sánh crow hits với và không có early sky target




F1 positive eligibility bị ảnh hưởng bởi shared cluster cap

	

Unit tests với nhiều target trong cùng cluster




Lotus bị corridor và cooldown chiếm ưu tiên

	

Log accepted/rejected hits theo kind và frame




Snapshot anchors trở nên cũ khi beasts di chuyển

	

So sánh static coverage với actual hit coverage




Stage rất lớn tạo nhiều samples hoặc integer overflow

	

Benchmark và safe-integer assertions




Geometry tốt nhưng key-2 vẫn áp đảo

	

Match-wide damage-share analysis sau reach balance

Kết luận: Phương án giữ hai rồng, một pearl, tối đa ba ground anchors mỗi side, median side split và lotus field-wide là phù hợp. Sau khi sửa F1 sky damage thành corridor/sky và lọc F1 target theo positive-damage eligibility, không cần thêm geometry grids, path caps, routing heuristics hay damage rules.

## Run 4

Verdicts: chưa có câu trả lời (anh dừng mọi việc lúc 14:02)

Chat URL: https://chatgpt.com/c/6aead710-5130-83ec-948c-2b59a263b966

#### fallback-turn-0:0:user · USER (Claude)

Role: you are the game-systems analyst for a browser typing game, "Tu Tien Thu Ai" (a xianxia defence game where every attack comes from typed words). Check ONE design for ONE skill for correctness, fix real defects, and return the corrected design. Write the prose in Vietnamese; keep every name, id, formula and pseudo-code in English. If you need clarifications, ask all of them in one message before you start; otherwise start directly.

WHY THIS BRIEF IS SHAPED THIS WAY
Three earlier runs did not reach two passing self-reviews in a row. The third started from a simple candidate and converged: its last review found only two defects (a flyer touched at F1 must take kind corridor from the sky part; the F1 target must be able to take positive damage), both fixed below. The coordinator (Claude) then made three changes of his own, marked [CLAUDE]. The design below is that converged version. Your scope is ONLY the design C1-C10: is each rule correct, deterministic, map-agnostic, consistent with the fixed machinery, and unambiguous in its result? Walk-throughs, the test plan and balance numbers are the coordinator's and are not part of this review. Keep it simple: fix only real defects, and add no grids, heuristics or damage rules.

GOAL
The Sword key-2 skill "Twin Dragons, One Burning Pearl" (`twin-pearl`, 雙龍戲珠) becomes a FIELD-WIDE, MAP-AGNOSTIC area skill. The owner (04/11/2026) rejected the version in which each dragon runs up one lane to one of the two gates: "having the 2 dragons run up to the gates is not reasonable, because we are building skills to be shared; later maps will not only face 2 gates, so the skill must work on many maps instead of going to 2 gates; a field-wide area skill makes more sense." Keep two dragons, one burning pearl and the lotus climax. No gate count, lane, waypoint, flow field or sky-entry point may drive the shape.

FACTS
- Deterministic lockstep sim, 60 Hz, integer-only state; 1 m = 60,000 u; HP integers; per-mille ratios; helpers mulDiv (round half up), mulDivSym, isqrt, dist2, within, unitPm. No float trig or float sqrt. Same seed and inputs, same world hash. At most 60 live beasts, at most 2 casts alive at once.
- F0 = the tick the Cast resolves; Fn = F0+n. D58: the first hit by F2 (50 ms). Fast attack, slow decay; caster side first.
- Today's only map: field x -20..+20 m, z -18..+8 m; heart (formation centre) at (0;0); the player (the Cast's origin) at (0;+3). Ground gates at (-15;-18) and (+15;-18); crows enter at (+-20;-18) and fly straight to the heart 4 m high, 2 m/s; ground beasts walk to the heart edge (r 2 m) at 1.0-1.6 m/s. Peaks: 25-44 live (max 52), about half per ground stream, 1-3 crows.
- FIXED damage machinery (unchanged, only its numbers may change): kinds touch / corridor / lotus carry 15 / 45 / 40 % of the beast's key-2 damage (2.5 W = 225 HP at K0) times its side's falloff (100 %, -15 % per next distinct victim of that side, floor 40 %); lotus "half" region deals 50 %; at most one hit of each kind per beast per cast, at least 20 ticks apart; each side has budget parts touch, corridor, sky, lotus (2.5 W per side split 15/45/40, plus 0.8 W sky per side, times M_q and the seat bucket), a hit takes min(its damage, what is left in its part), spent first come; the whole cast is one area hit (a swarm cluster loses at most 60 % of its HP to it); the boss takes at most 1.5 W a cast; each tick one pass gathers each beast's first kind it may still take (touch, then corridor, then lotus) and strikes all candidates in one order (kind, distance to the heart, serial); ground volumes (0-1.5 m) hit only ground beasts, sky volumes (2.5-6 m) only flyers; a sky hit is kind corridor and spends the sky part. The cast resolves only when a damageable beast is alive.

THE DESIGN TO CHECK
C1. Snapshot. At F0, before the F0 strike, read once: the field bounds, the heart H, the caster point C (the Cast's origin) and every live, damageable beast (serial, x, z, y; flyer = y inside the sky band). Store in the cast record: F, R, cut2, the side of each snapshot serial, P, the anchors, the route nodes, the samples and pass ticks, the sky anchors. The F1 discs are not made at F0; they are fixed once at F1. Beasts keep moving; every volume tests live positions at the current tick. A beast first seen after F0 gets a side once (C2) and takes no part in anchors or F1 targets.
C2. Frame and side split. F = unitPm(H - C); if zero, F = unitPm(field centre - H); if zero, F = (0,-1000). R = (-F.z, F.x). v(p) = mulDivSym(dot(p - H, R), 1, 1000); u(p) = mulDivSym(dot(p - H, F), 1, 1000). Sort the snapshot (ground and flyers together) by (v, u, serial); the first ceil(n/2) are side 0, the rest side 1. cut2 = v(last of side 0) + v(first of side 1) if n >= 2; 2 v(the one beast) if n = 1; 0 if n = 0. A later beast: side 0 if 2 v < cut2, side 1 if 2 v > cut2, else serial mod 2. A side never changes within the cast.
C3. Pearl. G = the mean position of the snapshot's ground beasts (of its flyers if it has no ground beast). P = H + 3/5 (G - H); if |P - H| > 12 m, scale P - H to 12 m; then clamp into the field shrunk by 2 m on every side (an axis shorter than 4 m clamps to its midpoint). Empty snapshot: P = H + 9 m along F, clamped the same way. Integer arithmetic; scale once, then clamp once.
C4. Routes. For each side, at most K = 3 anchors from its snapshot ground beasts by farthest-point sampling: the first is the one farthest from H; each next one maximises the smallest squared distance to {C, P, anchors chosen}; ties by smaller serial; stop at K or when the best smallest distance is under 3 m. Of the at most 6 orders, take the one with the shortest integer polyline length C -> anchors -> P (ties: lexicographic order of the anchors' selection indices). No length cap and no dropping of anchors. A side with no ground anchor routes C -> W_s -> P, W_0 = H - 9 m R and W_1 = H + 9 m R, clamped like P. Merge consecutive duplicate nodes; a zero-length route is one stationary sample.
C5. Samples and body. Per segment A -> B: length L = isqrt(dist2(A, B)); steps = max(1, ceil(L / step)); halfWaves = max(1, round half up(L / 4 m)); the normal is unitPm(-(B.z - A.z), B.x - A.x). steps + 1 evenly spaced samples by integer interpolation (a shared endpoint is not repeated). The phase runs halfWaves x j / steps; with f its fractional part, offset = sideSign x waveSign x 0.9 m x 4 f (1 - f), along the normal; sideSign +1 for side 0 and -1 for side 1; the first half-wave of each segment is positive and the sign alternates; the offset is 0 at segment ends; all ratios integer. Clamp each sample into the field bounds. Recompute the cumulative arc on the sampled polyline with isqrt. [CLAUDE] step = 0.5 m, raised to ceil(total control length / 256) when that is larger, so a route never has more than about 256 samples on a very large field. [CLAUDE] pass[i] = 3 + mulDiv(45, arc[i], totalArc) (the heads run F3-F48, 45 ticks instead of 39, because these routes are about 1.7 times longer than the old lane routes; a 45 m route moves at 60 m/s); pass = 3 for all if totalArc = 0. The body is a ground disc r 1.4 m round every sample with pass[i] <= t <= pass[i] + 54. Kind corridor, part corridor.
C6. F0 strike and F1 discs. F0: a ground disc r 4.5 m round H, kind touch, part touch. F1: for each side, the snapshot beast of that side nearest H by its live F1 position (ties: smaller serial) that is alive, damageable, has not yet taken the kind its disc would deal, and can take positive damage under the machinery (its part has budget left; the boss under his cap; its swarm cluster under the 60 % cap). A ground target gets a ground disc r 2.2 m at its F1 position, kind touch, part touch; a flyer gets a sky disc r 2.2 m at its F1 position, kind corridor, part sky. The discs keep their centres and live F1-F2. No eligible beast: no disc for that side. So with an eligible damageable beast alive at F0, the first positive hit lands by F1; a case where the fixed machinery blocks every positive hit is logged, not counted as a hit.
C7. Sky. [CLAUDE] F30-F56 (to the end of the roar): each side has, in the sky band, a capsule r 2.5 m (in the x-z plane) from its head point (the last sample with pass <= min(t, 48)) to each of its sky anchors (its snapshot flyers' F0 positions), and a disc r 2.5 m round every active body sample. Only flyers take it. Kind corridor, part sky.
C8. Lotus. [CLAUDE] F57-F77, at P, ground only, outer radius 9 m. Full inside the outer disc and within at least one of: disc(P, 4 m), disc(H, 4.5 m), and for each route the capsule r 2.2 m round its last 13 m of sampled polyline before P (measured back from P by arc length; the whole route if shorter). Half elsewhere inside the outer disc. Kind lotus, part lotus.
C9. Timeline. [CLAUDE] F0 strike at the caster side; F1-F2 discs; F3-F48 heads; F30-F56 sky; F49-F56 roar (no new volume); F57-F77 lotus; body trails hit until at most F102; F103-F300 visual decay only. Charge only while typing; no wait after F0.
C10. Machinery and budget. Keep the fixed machinery exactly. Baseline 2.5 W ground per side (15/45/40) and 0.8 W sky per side; 2.0 W per side is a comparison trial. The key-2 share target is the owner's decision.

DELIVER
1. For each of C1-C10: "correct" or the defect and its fix (keep fixes simple).
2. If any fix: the corrected full design C1-C10 (at most about 1,500 words). If none: say so.


(Đề bài trên là đúng văn bản đã chèn và so khớp trước khi gửi. Lúc anh dừng, ChatGPT còn đang nghĩ, chưa có chữ nào của câu trả lời; tab này sau đó bị đóng.)
## Bảng kiểm (Claude, 04/11/2026)

Các ý ChatGPT đưa ra là kỹ thuật dựa trên dữ kiện của đề bài, nên "nguồn" là mã của game, nguyên mẫu `proto.py` của Claude và các bản cổng số nguyên của giám khảo Claude (ngoài Git). Không lượt nào qua hai lần duyệt liên tiếp, nên mọi ý dưới đây chỉ là tham khảo; Claude tự kiểm từng ý.

| Ý | Lượt | Kiểm ở đâu | Kết quả | Ghi chú |
|---|---|---|---|---|
| Chia hai rồng theo tọa độ ngang quanh trục người chơi → Trận Tâm, lấy trung vị theo số con, `cut2` cho thú đến sau | 2 | Cổng số nguyên của các giám khảo (bảy bố cục, gương, xoay) | Đúng | Dùng ở §9.3 |
| Ảnh chụp một lần ở F0, khối trúng thử vị trí thật mỗi tick | 1–3 | `src/sim/twin-pearl.ts`, `cast.ts` | Đúng | Dùng ở §9.2 |
| Ngọc ở 3/5 đường tới tâm khối thú đất, kẹp 12 m và mép sân | 2 | `proto.py`, cổng số nguyên | Đúng | Dùng ở §9.4 |
| Quét trời bằng con nhộng từ đầu rồng tới neo trời ở vị trí F0 | 2 | Tính độ trôi của quạ (2 m/s: 1,87 m tới F56; quạ Cuồng ở Thử thách 2,73 m/s: 2,55 m) | Đúng với r 3 m; r 2,5 m sát giới hạn | Claude nâng lên r 3 m |
| Đo `coverageStatic`, test gương và xoay dung sai 0 | 3 | Cổng số nguyên của giám khảo | Đúng, sau khi `sPath` làm tròn đối xứng | Dùng ở §9.8, §9.12 D |
| Quạ chạm ở F1 phải là đòn hành lang lấy ngân sách trời | 3 (lần duyệt 3) | Luật sát thương cố định của đề bài, `hit()` | Đúng | Dùng ở §9.5, B.7 |
| Mục tiêu F1 phải nhận được sát thương dương | 3 (lần duyệt 3) | `combat.ts` `clusterLeft` (trần cụm làm tròn xuống) | Đúng | Dùng ở B.7 qua `areaClusterLeft` |
| Bỏ trần độ dài đường bay | 3 | `proto.py`: đường hai cổng 44–45 m; trần 36 m bỏ hết neo | Đúng | Dùng ở §9.4 |
| "Ngân sách 2,0 W không bảo đảm đòn F1" | 3 (lần duyệt 1) | `hit()` lấy `min(sát thương, phần còn lại)` | Sai | Đòn vẫn dương khi phần còn > 0 |
| Lưới mật độ 4 m, lưới quét 6 m, chèn điểm rẻ nhất | 2 | Ba lần duyệt của chính ChatGPT đều thấy lỗi biên mới | Bác | Quá phức tạp |
| Trần đường dài 3 × đường chéo sân (143 m) | 2 | 143 m trong 39 tick là khoảng 220 m/s | Bác | |
| Trần sát thương mỗi thú, ngân sách để dành cho hoa sen | 1 | Trái luật sát thương cố định | Bác | Lý do làm lượt 1 trượt mãi |
| Nửa sóng đầu của mỗi đoạn luôn dương | 3 | `sPath` hiện có nối dấu qua các đoạn và đã có test | Bác | Giữ `sPath` |
| Cắt cánh hoa sen trong đĩa 9 m | 3 | §3 A: cánh dài 13 m vươn quá 9 m | Bác | Giữ cánh 13 m |
| Thứ tự đánh vẫn theo `heartDistance` (ngầm) | 1–3 | `field.ts`: `heartDistance` đọc trường dòng chảy của cổng | Bác | Đổi sang `dist2` tới H |
