# Bản đồ đẹp, sống, có chiến thuật và hợp lý: kế hoạch và triển khai cho ba game (28/10/2026)

**Đọc cho ai:** chủ dự án, và các agent làm bản đồ về sau.

**Quan hệ với tài liệu cũ:** tài liệu này **mở rộng** `docs/tools/MAP_FACTORY.md` (duyệt 27/10), không lặp lại nó. Kiến trúc lõi, MapSpec v0, quy tắc tất định, phiếu 025–033 vẫn như ở đó. Mục 2.10 ghi rõ giữ gì, đổi gì, bỏ gì.

**Nguồn:**
- Kiểm kê việc bản đồ ngày 28/10 (MAP_FACTORY, spike, mã Rồng, lõi `map-factory`, asset, ba game).
- Nghiên cứu cách làm bản đồ stylized và thiết kế màn TD (web, 28/10). Danh sách ở cuối.
- Phân tích chiến thuật từ mã sim của Rồng (`maps.ts`, `lanes.ts`, `words.ts`, `spawn.ts`, `movement.ts`, `combat.ts`, `policy.ts`) và số đo tính trên tọa độ thật.
- Phân tích ảnh: ảnh mẫu Haven Grove (nửa trên "BEFORE") cạnh spike `final2` và M0b, có số đo ảnh.
- Ba bản thiết kế cạnh tranh (luật + người chấm; bản đồ dựng tay; đồ thị mẫu) và hai giám khảo. Bản này lấy khung của bản "luật + người chấm", lấy cách sinh khung chơi của bản "đồ thị mẫu", lấy thứ tự bản thử của bản "dựng tay", và sửa mọi điểm yếu hai giám khảo nêu.

**Trạng thái:** đề xuất. Mọi quyết định ở đây là khuyến nghị của Claude theo ủy quyền 27/10. Chỉ một việc cần chủ dự án quyết về sau (nạp thêm credit Tripo trước các kit của lát M5, mục 5).

## Tóm tắt

**Trả lời chủ dự án: đúng, việc làm bản đồ chưa có kế hoạch triển khai.**
- MAP_FACTORY chỉ phủ 2 bản đồ (Rồng L2-cau, Lời Gọi w1-silverfall). Bước "Rồng vào game" ghi "khi rảnh", không ngày. 520 ải của Rồng là một dòng ở giai đoạn 5. Tuyến Cuối là việc tùy chọn ở giai đoạn 6.
- Spike chưa qua cổng: người dựng tự chấm 7,25, giám khảo độc lập chấm 6,75 (cổng 7). Khung hình +2,62 ms (cổng 2 ms).

**Kế hoạch cũ thiếu năm thứ:**
1. **Không ai thiết kế hay đo phần chơi.** Làn, ô, sông là đầu vào chỉ đọc. Nên kế hoạch không làm bản đồ "chiến thuật hơn" được. Đã có lỗi đo được: Đường Cầu gánh 58,2 % sức ép đợt 7; ô bẫy `cau-t1` nằm ngoài vòng chữ 26 m; ô nhà `h-se` không với tới đường nào trong 10 m; cầu không phải điểm nghẽn trong sim (mặt cầu 3,4 m rộng hơn làn 3 m) nhưng bot vẫn tính ×1,2.
2. **Không có luật "hợp lý".** Không luật nào nói vì sao đường cong, nước chảy về đâu, vách đứng đâu, lối mòn dẫn tới đâu. Sông của L2-cau còn hẹp dần về hạ lưu (8 → 4 m). Vách và 5 lối mòn của spike là hằng số gõ tay cho đúng một bản đồ.
3. **Chấm bằng mắt người dựng.** Không có số đo ảnh, không bộ mẫu hiệu chuẩn, không quy trình giám khảo.
4. **Không tính credit cho kit, không có lớp sự sống.** Kế hoạch cũ cần khoảng 96 + 22 model Tripo (3.500–7.000 credit) trong khi còn khoảng 1.100. Ngoài sông chảy và cây đung đưa, không gì chuyển động.
5. **Không có đường duyệt cho chủ dự án** khi số bản đồ lớn.

**Cách chọn, năm dòng:**
1. Mỗi bản đồ có hai phần tách hẳn, mỗi phần một mã băm: **khung chơi** (sim đọc, kiểm bằng bot) và **cảnh** (chỉ để nhìn, giữ golden).
2. Khung chơi sinh từ **đồ thị mẫu** (16 mẫu của Rồng); mỗi nút mang lý do (cổng có nguồn, khúc cong có vật gây cong, nước chảy từ cao xuống thấp). Lint chiến thuật loại seed xấu trước khi vẽ; bot 2 × 300 seed cho mỗi ải.
3. Cảnh dựng theo luật từ khung: ánh sáng trước, rồi vách, nước, bãi trống, lùm, lối mòn có đích, đồ dọc đường, sơn đất, sự sống. Luật không đạt thì cho **ghim tay** vật lớn, có ghi lại.
4. Chấm bằng **số đo ảnh** cộng **một giám khảo độc lập đã hiệu chuẩn**; chủ dự án quyết cuối.
5. Kit theo credit: bộ dùng chung nhuộm màu, 3–5 model chữ ký mỗi kit, ảnh 2D Codex trước.

**Bản thử: Rồng L2-cau, khoảng 3 tuần lịch, 4 chặng.**
- Chặng A (tuần đầu, không model mới): đưa spike vào game, sửa các nguyên nhân rẻ (đồng cỏ sọc, ánh sáng, mép đất, bố cục). Chủ dự án thấy bản đẹp hơn sau khoảng 4 ngày. Cổng: giám khảo ≥ 7,5.
- Chặng B: lõi tự suy khung cảnh từ đồ thị, thay hằng số tay; thử trên L2-cau lật gương, L2-l, L2-doi.
- Chặng C: kit Tripo đợt 3, Campfire Ring, lớp sự sống. Cổng ship: trung vị 12 ảnh ≥ 8.
- Chặng D (song song): thang ứng viên chiến thuật qua bot, kể cả làn dài hơn.
- Thời gian chủ dự án: khoảng 2 giờ (phần lớn là dựng Tripo). Credit: khoảng 270–360, chưa tính làm lại.

**Sau bản thử:** Rồng theo lát phát hành (C1 trước, mỗi lát một kit); Tuyến Cuối dựng lại sân Vành Chân Trời ngay sau bản thử; Lời Gọi có lint chiến thuật ngay ở bản 2D, phần cảnh làm khi bước 1C bắt đầu.

---

## 1. Các cách làm bản đồ và cách nào hợp với ta

Đánh giá: C = cao, V = vừa, T = thấp. Chi phí là ước của ta. Mã nguồn [Rx] ở cuối tài liệu.

| # | Cách | Cho gì | Rồng | Lời Gọi | Tuyến Cuối | Ta dùng? | Nguồn |
|---|---|---|---|---|---|---|---|
| 1 | Khung người làm + trang trí theo luật (Bad North, Townscaper, Kingdom Rush, Islanders) | Người giữ hình lớn và phần chơi; luật thêm chi tiết. Stålberg: hình lớn đoán được, chi tiết nhỏ đổi | C | C | C | **Có, là khung chính** | R1–R4, R33 |
| 2 | Spline cho đường, sông, lối mòn; đường đi chi phí thấp nhất | Đường cong mềm, bậc bề rộng, đồ đặt theo độ dài cung | C (lối mòn); V (làn: đổi làn là đổi cân bằng) | C | V | **Có** (lối mòn A*, `along.ts` 033) | R5–R7 |
| 3 | Nặn heightfield + sơn splat theo dốc | Đồi, bờ, vách | V (chỉ cao độ thấp) | V | T | Chỉ dấu cao độ có lý do; không nặn tay | R8 |
| 4 | Sơn đất theo trường khoảng cách (EDT, bẻ miền, texture bombing), nướng một lần | Đất mòn dưới cây có viền cỏ nhạt, mép lối mềm, sân mòn ở ngã ba | C | C | V (bẩn, cháy sàn) | **Có, lõi của vẻ đẹp ảnh mẫu** | R9–R11 |
| 5 | Rải nhiễu xanh (Poisson) | Lấp đều cỏ, hoa, sỏi | C | C | V | Có, nhưng chỉ trong mặt nạ, kèm cụm | R12, R13 |
| 6 | Rải theo cụm, lùm (cha–con, sinh thái) | Lùm cây một sắc chủ, cây lẻ, tầng dưới | C | C | T–V | **Có** | R14, R15 |
| 7 | Bảng luật theo biome, theo kit (HZD, Far Cry 5, Unreal PCG) | Một bộ luật ra nhiều bản đồ; nước trước, vách sau, cây sau cùng | C | C | V | **Có** (bảng luật mỗi kit) | R15–R17 |
| 8 | Bộ ô mô-đun (Skyrim) | Ít họa sĩ, nhiều màn | T–V | T–V | C (sàn, tường, ray) | Chỉ Tuyến Cuối | R18 |
| 9 | WFC | Ghép khớp cục bộ | T | T | V (chỉ khi có bộ ô) | **Không** | R19, MAP_FACTORY 5.1 |
| 10 | Đồ thị, ngữ pháp (Dormans, Unexplored) | Cấu trúc toàn cục trước, không gian sau | V | V | T | **Có, bản nhỏ**: đồ thị mẫu làn | R20, R21 |
| 11 | Ống nút kiểu Houdini | Lớp không phá hủy ở tầm AAA | T | T | T | Không (ý đã có trong L0–L7) | R16 |
| 12 | Sinh rồi thử theo số đo (search-based, Sentient Sketchbook) | Sinh N seed, chấm, giữ tốt nhất | C | C | V | **Có** | R22, R23 |
| 13 | AI chấm bằng LLM/VLM | Vòng sửa spec, chụp, chấm | C (làm QA) | C | C | **Có, với luật**: không tự chấm, có hiệu chuẩn, chủ dự án quyết | R24 |
| 14 | Trình sửa bản đồ trong trình duyệt (bảng bản đồ) | Người không lập trình chỉnh tay cầm, đổi seed, xem điểm | C | C | V | Có, ở bước triển khai | R25 |
| 15 | AI vẽ nền đất theo mặt nạ (ControlNet) | Nền vẽ tay dưới prop 3D | T (520 ải, 1–3 MB mỗi ải) | V | V (phông) | Không cho sân chơi; chỉ phông xa | R26 |
| 16 | Địa hình từ ràng buộc khoảng cách (Red Blob) | Cao độ, nước, độ ẩm suy từ khoảng cách | V | V | T | **Có**: luật "hợp lý" (lau sậy gần nước, đất khô xa nước) | R13 |
| 17 | Lớp sự sống (gió chung, chim, khói, nước) | Cảm giác sống | C | C | C | **Có** (lớp L8 mới) | R27 |

**Kết luận từ nghiên cứu:**
- Họ kiến trúc của MAP_FACTORY (spec + seed + sổ model, lõi số nguyên, L0–L7, không GLB cả bản đồ, không WFC) là đúng. Nghiên cứu không ủng hộ chuyển sang WFC, Houdini, nặn heightfield hay AI vẽ cả bản đồ.
- Hai thứ nghiên cứu cho thấy ta thiếu: **một đường thiết kế khung chơi có số đo chiến thuật** (độ dài, khúc cong, tách và nhập, điểm nghẽn, độ lộ của ô, báo trước, nhịp khái niệm theo màn) và **một người chấm không phải người dựng**. LLM chấm thiên vị bài của chính nó (Panickssery 2024); spike lặp lại đúng điều đó (7,25 so với 6,75).
- Luật TD đổi thành phép kiểm được (R28–R32):
  - ô cố định dễ thành câu đố một lời giải → đếm số cách đặt ô còn tốt;
  - một ô cạnh khúc quay 180° phủ đường hai lần → đo độ lộ và số lần phủ;
  - tách sớm rồi nhập thì chỉ ô ở điểm nghẽn phủ được cả hai → mẫu tách/nhập phải có ô chung;
  - cổng báo trước họ quái (rừng tối báo nhện);
  - mỗi màn một ý chính; có màn nghỉ;
  - môi trường đổi luật (PvZ: hồ, đêm, sương, mái) giống 8 kit chữ ký của Rồng;
  - lớp ưu tiên nhìn: giao diện > hiệu ứng > quân > cảnh (Riot); cảnh làm khung, không tranh chú ý.
- Nguồn yếu: không đọc được bài nói gốc của Ironhide hay Ninja Kiwi; số Bloons lấy từ wiki cộng đồng; luật sân đấu (Tuyến Cuối) chỉ có ghi chú khóa học.

---

## 2. Giải pháp

### 2.1 Hai phần tách hẳn: khung chơi và cảnh

| | Khung chơi | Cảnh |
|---|---|---|
| Gồm | Bệ, làn (polyline, bề rộng, cầu, chỗ lội), cung bay, ô, vùng xây và vùng cấm; về sau vật mang chữ, hiểm họa, điểm sinh ngoài cổng, ô có hệ số | Ánh sáng, cao độ ngoài sân, nước (dáng, hướng chảy), vách, bãi trống, rừng mép, lùm, lối mòn, đồ dọc đường, sơn đất, sự sống |
| Ai đọc | Sim, bot, lint chiến thuật | Chỉ phần vẽ |
| Ở đâu | Nội dung game (`src/content/`) | `src/view/maps/<id>.map.json` của từng game (MapSpec v1); sim không import được |
| Sinh khi nào | Offline (`stages:gen`), khóa băm. Không bao giờ sinh lúc nạp | Khung cảnh offline (CLI), phần rải lúc nạp |
| Đổi thì | Bot 2 × 300 seed, đổi golden có chủ ý, có changelog | Golden sim giữ nguyên từng byte |
| Băm | `simHash` | `viewHash` và băm từng lớp |

**Tách băm (làm ngay).** Hôm nay bộ đọc 028 của Rồng băm cả `river` và `terrain`, dù sim không đọc chúng. Sửa logic sông (đổi hướng chảy) vì vậy trông như đổi luật chơi. Bộ đọc `dragon-hold@2` tách:
- `simHash`: bệ, làn đã biên dịch (u), bề rộng, đoạn cầu và lội, cung bay, ô;
- `viewHash`: sông, `terrain`, camera.

`river` vẫn ở MapDef (không dời, đỡ xáo `map.test` và 028). Cảnh được ghi đè hướng chảy của sông để nhìn.

**Cảnh giải thích khung, không đổi khung.** Cảnh đọc khung và thêm lý do cho từng hình dạng: vật gây cong trong mỗi khúc cong ≥ 15°, khe rừng sau mỗi cổng, đá lội trong đúng đoạn lội, mặt cầu khớp đoạn cầu. Một bản đồ "hợp lý" hơn mà khung không đổi.

### 2.2 Khung chơi và luật chiến thuật

#### Rồng: MapDef thêm trường khi kit cần

| Trường mới | Khi nào |
|---|---|
| `zones.build`, `zones.forbid` (04 §3.3); `role` của ô nhà (`lane`, `shared`, `dais`, `sky`) | Ngay, cùng lint |
| `padMods` (đồi +25 % tầm) | Kit hill-meadow |
| `objects`: vật mang chữ (Glow Mushroom, vách lở). Tối đa 1 sống, tính vào trần 16 chữ, chữ đầu duy nhất | violet-glade, red-canyon |
| `hazards` (lũ có đường vòng, dây leo, đoạn triều có chu kỳ, miệng nham, gió, sương) và `connectors` (đường nối giữa làn) | Kit của chúng |
| `spawns` ngoài cổng (phục kích đầm lầy, quái sông từ C8) | Kit của chúng |

Mỗi trường có hỗ trợ sim khi kit tới, qua cổng bot của làn Rồng.

**Điều kiện trước bản đồ thứ hai:** `data/waves.ts` phải tính `zoneDelayMs` từ MapDef được đưa vào, không import `MAP_L2_CAU`. `tests/content/map.test.ts` phải chạy qua mọi bản đồ trong `MAPS`.

#### Đồ thị mẫu (khung chơi của Rồng)

Mỗi mẫu trong 16 mẫu của 04 §3.1 thành một file `layouts/<mẫu>.graph.json` trong nội dung Rồng. Nút có tên và mang lý do:

| Loại nút | Trường chính | Luật đi kèm |
|---|---|---|
| `gate` | dải phương vị, bán kính 28–32 m, `source` (khe rừng, khe vực, cổng đổ, hang, bãi biển, khe sương), `telegraph` (họ quái) | Mỗi cổng là một lối mở có nguồn |
| `bend` | làn, dải vị trí, dải góc, bán kính ≥ 4 m, `cause` (lùm, tảng đá, ao, chân đồi, mỏm vách, bờ) | Cong ≥ 15° phải có vật gây cong trong 6 m |
| `choke` | `bridge`, `ford`, `narrows`, `arch`; dải vị trí, dải độ dài, tỉ lệ bề rộng | Điểm nghẽn phải thật (tỉ lệ < 1,0) |
| `split`, `merge` | dải vị trí, chênh nhánh | Hai nhánh tới điểm nhập cách nhau ≥ 3 s (02 §5.5) |
| `sky` | phương vị (cách cổng đất ≥ 40°), độ cao, vòng cuối 6–8 m, `roost` | Quái bay tới từ chỗ cao hoặc tối |
| `water` | sông, suối, ao, đầm; `from` cao `to` thấp; chỗ băng qua (id nút nghẽn); dải bề rộng | Nước chảy xuống, rộng dần về hạ lưu |
| `high-side` | phương vị theo mặt trời, cung 60–100°, vách (r 38–46 m, cao 6–9 m, 2–3 tầng) | Vách ở phía cao, hướng mặt về nắng |
| `open` | cung trống lớn nhất, 70–120° | Bãi cỏ yên |
| `landmark` | một mỗi làn (đặt tên làn), một mỗi góc phần tư | Mốc phải giúp định hướng |

**Sinh:**
1. Không xoay tự do. Hướng chỉ chọn từ dải phương vị cổng (±10°) và bản lật gương (x → −x). Camera mặc định giữ yaw 0; `lookM` tính theo luật khung (H10).
2. Đặt cổng, nghẽn, tách, nhập trong dải. Vẽ làn qua các nút thành đường cong bán kính ≥ 4 m, lấy mẫu polyline dây cung ≤ 1,5 m. Sim (`pointAt` tuyến tính) và mặt nạ làn của phần vẽ dùng chung polyline đó.
3. Sinh ô theo luật 03 và H5–H8.
4. Tính số đo, lint, dấu vân tay (fingerprint).
5. Mỗi (mẫu, kit, ô trong chương) sinh 64 seed; loại seed trượt luật cứng; xếp seed còn lại theo khoảng cách tới vector đích của mẫu cộng điểm khác biệt với 10 ải trước; lấy seed tốt nhất chạy bot. Trượt bot thì thử seed kế (tối đa 3), rồi chỉnh đe dọa ±10 % trong dữ liệu (04 §4.3). Không bao giờ sửa tay hình học.

Bộ sinh đồ thị chạy trong Node ở `stages:gen`, nằm trong `scripts/` của Rồng (không ship). Nó được dùng số thực, làm tròn ra cm; JSON đầu ra là sự thật và được khóa băm. Chạy lại trên cùng bản Node phải ra cùng byte. Cách này bỏ được yêu cầu "lượng giác bằng bảng tra" cho phần này (bớt phức tạp so với bản đồ thị gốc).

Ải dựng tay (ải 1, 10, 20 mỗi chương, 04 §11.3) được ghim cả làn và ô. L2-cau là ải ghim đầu tiên.

#### Luật cứng (lint chiến thuật `pnpm dh:map-lint`)

Lint gọi chính mã sim (`compileLanes`, `alongAtRadius`, `inWordZone`, hằng số `rules.ts`), nên không lệch khỏi sim.

| # | Luật | L2-cau hôm nay |
|---|---|---|
| H1 | Làn dài 24–36 m (01 §2.1, `map.test`); cổng ở r 28–32 m; kết thúc trên vòng 6 m | 24,59 / 25,29 m; cổng r 30,22 / 30,81 m. Đạt |
| H2 | Không đi ra xa bệ sau khi vào vòng 26 m (vòng chữ, `alongAtRadius` và chỗ dừng của quái bắn đều dựa vào nó), trừ khi mẫu khai báo ngoại lệ | Đạt |
| H3 | Hai làn cách nhau ≥ 8 m ngoài chỗ nhập; 0 chỗ cắt nhau | 9,15 m; 0. Đạt |
| H4 | Khoảng phương vị giữa các đầu làn ≥ 30° (vòng thẻ 12 chỗ) | 98°. Đạt |
| H5 | Ô bẫy: 3–5 mỗi làn, cách nhau 5–7 m, ≥ 8 m từ tâm, không trong đoạn lội, **r ≤ 25,5 m** (trong vòng 26 m ít nhất 0,5 m), trừ ô khai báo `hold` | `cau-t1` ở 4 m, r 26,32 m. **Trượt** (ngoại lệ đã biết của v1) |
| H6 | 2–3 điểm chặn mỗi làn | 2 / 2. Đạt |
| H7 | Mỗi ô nhà khai vai trò và đạt nó: `lane` ≥ 6 m làn trong 10 m; `shared` ≥ 4 m mỗi làn của hai làn trong 10 m; `dais` với tới bệ; `sky` với tới đầu cung bay. Bản đồ ≥ 2 làn có ≥ 1 ô `shared`. Không ô chết | `h-nw` là ô chung duy nhất (7,4 m Cầu, 6,1 m Suối). `h-se` 0 m làn trong 10 m: phải khai `dais` hoặc `sky` |
| H8 | Mỗi đầu cung bay có ≥ 1 ô trong tầm Net Launcher (10 m) | Chỉ `cau-t4` (9,4 m). Đạt, ghi phát hiện (đích mềm là 2) |
| H9 | Số ô so với vàng của ải trong G13b (15–35 %) | Bot đo |
| H10 | Đường bắn: tia từ Rồng (cao 2,5 m) tới từng điểm làn trong vùng chữ (mỗi 1 m), và từ ô nhà tới điểm làn trong tầm, không qua vật rắn cao > 1,2 m. Cổng, ô, vòng thẻ nằm trong khung mặc định trừ vùng HUD ở 1280×720 và 1920×1080 | Đạt với `lookM` [0, −4] |
| H11 | Hai nhánh tới chỗ nhập cách nhau ≥ 3 s, hoặc đợt quái so le | Không có |
| H12 | Nghẽn thật: thứ bot coi là nghẽn phải có tỉ lệ bề rộng < 1,0; `policy.ts` đọc tỉ lệ, không dùng hằng ×1,2 | Cầu 1,13 mà bot vẫn ×1,2. **Trượt** (ngoại lệ đã biết của v1) |

Định nghĩa H5 lấy theo vòng 26 m, không theo "vùng chữ của quái chậm nhất". T_a = 8 s × biên / k đổi theo hồ sơ người chơi, nên vùng chữ không cố định. Lint vẫn báo số mềm theo **hồ sơ tham chiếu** (k = 1, biên 1,219, T_a 9,75 s): E09 (2 m/s) vào vùng chữ ở 5,09 m dọc Đường Cầu.

**Số đo mềm** (báo, so dải của mẫu):

| # | Số đo | Dải đích | L2-cau |
|---|---|---|---|
| S1 | Độ quanh co L / (r_cổng − 6) | 1,05–1,35; mọi khúc ≥ 15° có vật gây cong | 1,015 / 1,019 (nan hoa thẳng); một khúc 21,2° ở chỗ lội |
| S2 | Thời gian tới bệ của quái S2; đi trước vùng chữ; bị chặn bởi T_a hay bởi vòng | S2 15–20 s (02 §1) | E09: trước vùng 2,5 / 2,9 s, tổng 12,3 / 12,6 s |
| S3 | Sàn Q (điểm vào vùng ÷ điểm dừng) | Báo; dự đoán Q (đích 50–70 %) | 0,21–0,23 |
| S4 | Độ phủ ô nhà (mét làn trong 6–16 m), ô chung, ô chết | ≥ 1 ô chung; ô ngoài gần chỗ tách, nhập, nghẽn | Xem H7 |
| S5 | Độ lộ ô nhà với chỗ đứng của quái bắn (E11 12 m, E01 10 m) | Báo | 5 ô lộ với E11; `h-se` lộ với E01 |
| S6 | Lộ kỹ năng vùng: số làn trong một nón Phun Lửa 60° tại 12 m; trong đĩa Thiên Hỏa 4 m | Theo mẫu; D23 ≤ 15 % đo bằng bot | 0 |
| S7 | Phần diện tích bẫy nằm trong vùng chữ của E09 (hồ sơ tham chiếu) | Báo | `cau-t1` ngoài |
| S8 | Ô với tới đầu cung bay | 2 | 1 |
| S9 | Mốc đặt tên làn, thấy được ở khung mặc định | 1 mỗi làn | Cầu: đạt |
| S10 | Vector độ khó: số mặt trận (đầu làn trong một nón 60°; số ô 10 m tối thiểu để phủ mọi làn), thời gian S2 ngắn nhất và độ lệch giữa làn, đòn bẩy (bẫy trong vòng mỗi làn, ô chung, nghẽn, chậm, chặn), độ hội tụ, cung bay và tầm với, dấu của hiểm họa kit | Theo mẫu | Mốc gốc |

**Vector độ khó và hệ số mẫu.** Thứ tự giả thuyết: L1-thang < L1-s < L1-xoan; L2-tach < L2-l ≈ L2-cau < L2-doi; L3-lech, L3-quat < L3-t < L3-y; L4-haicap < L4-thap, L4-x < L4-chongchong < L4-vong. Mỗi mẫu × cơ chế kit được đo một lần bằng bộ đợt chuẩn hóa đe dọa trên 2 × 300 seed, ra **hệ số mẫu** (Δthắng, ΔS, ΔP, ΔI, ΔQ so với L2-cau). `stages:gen` chỉnh đe dọa trong ±10 % để G21 (đường cong ±15 %) giữ. Bản đồ không được tăng tải gõ (04 §0.5); nó đổi cách chia chú ý và đòn bẩy phòng thủ. Ghép mẫu khó với cơ chế kit dễ chịu, hoặc ngược lại; lần đầu của một mẫu tính là ý mới của ải đó (04 §5.6).

**Bot vẫn chạy cho từng ải.** Một ải là 2 họ × 300 seed × 5 bot = 3.000 lượt, khoảng 10–11 phút trên 10 nhân (canon §8: khoảng 2,1 giây CPU một lượt). Một chương 20 ải khoảng 3,5 giờ, chạy qua đêm. Hệ số mẫu chỉ để chỉnh đe dọa, không thay bot từng ải.

**Ba mẫu không vừa 24–36 m:** L1-xoan ("xoắn nửa vòng quanh bệ" dài khoảng 61 m), L4-vong, L1-s dài. Đề xuất ghi vào canon (báo chủ dự án, không hỏi):
- L1-xoan thành móc 90–120° quanh đồi hoặc lùm, ≤ 36 m;
- L4-vong: một làn đi cung ≤ 120°, các làn kia hướng tâm;
- L1-s: biên độ ≤ 4 m trong 36 m.

**Mâu thuẫn canon cần chốt sau khi đo:** dải làn 24–36 m (01 §2.1, `map.test`) hay 24–40 m (02 §1, art-pipeline §5). Giữ 24–36 m tới khi ứng viên v2c (làn 27–29,5 m) cho số I↔Q. Ô nhà: giữ vòng 7–10 m và 14–20 m của 03; bỏ "ô nhà cách đường 2–6 m" của art-pipeline §5 (vai trò ô ở H7 thay nó).

#### Lời Gọi và Tuyến Cuối

- **Lời Gọi:** khung chơi đã có trong sim (tuyến, đất xây, nước, cầu, mỏ, 36 cây luật). Lint đọc bản trích 028:
  - trường phủ: mét tuyến trong 9 m và 12 m của từng chỗ xây (chỗ 12 m tốt nhất phủ 42 m; 77 chỗ ở 9 m và 277 chỗ ở 12 m phủ cả hai nhánh ≥ 4 m);
  - đoạn chết: boss đi khoảng 50 s không tháp nào với tới (BUILD_1B §4.2); đích ≤ 15 s;
  - người đi bộ chỉ qua sông ở cầu; độ lộ của mỏ dưới đường bay; nhà quan trọng cách nhau 15–35 m.
  - Rainbow Hill (2, −21) là điểm tựa tự nhiên: tháp 12 m phủ 28 m, với +10 % phủ 36,5 m. Đồi và nền Watchtower cần có trong sim: đề xuất cho làn Lời Gọi, qua bot của nó.
- **Tuyến Cuối:** khung chơi là `FieldPreset` (hành lang, hai đầu, đoàn xe băng ngang, trạm giữa): dải cổng, khe sinh (RIFT z 13–17), vạch NEAR (z ≤ 7), DRAIN (16 m), hiểm họa §4.0b. Vật cản nào cũng đổi flow field, nên là luật chơi, qua bot. Số đo: thời gian từ cổng tới tầm bắn của từng quái (mìn 2,6 m/s: từ 40 m tới 10 m mất 11,5 s), độ sâu khe sinh so với tầm súng, độ dàn ngang so với nón Tán 9 m và cột của Ray.

### 2.3 Luật hợp lý (phép kiểm `checks/logic.ts`)

| # | Luật |
|---|---|
| LG1 | **Cổng có nguồn.** Mỗi cổng đất nằm ở khe rừng (rộng ≥ bề rộng làn + 6 m), khe vực, cổng đổ, hang hay bãi biển; vệt đường đi tiếp ≥ 16 m vào vành ngoài. Cung bay đến từ chỗ cao hoặc tối trên phương vị không có cổng đất trong 40°. Trang trí cổng báo họ quái (thảm rêu cho Yêu Rêu, cỏ giẫm và vết cào cho Thú Mục), không máu, không xác (05) |
| LG2 | **Khúc cong có lý do.** Mỗi khúc ≥ 15° có vật gây cong ở phía trong, trong 6 m. Không cong giữa bãi trống |
| LG3 | **Nước chảy xuống.** Từ phía cao sang phía thấp; bề rộng không giảm về hạ lưu, trừ khi đổ vào ao hoặc đầm. Cầu vuông góc dòng (±20°) ở chỗ hẹp sâu; chỗ lội ở đoạn nông rộng. Ao ở chỗ trũng, có dòng vào hoặc ra; lau sậy ở bờ nước chậm |
| LG4 | **Vách ở phía cao**, ngoài sân (r ≥ 36 m), mặt hướng nắng (pháp tuyến · mặt trời ≥ 0,3), không nằm giữa bệ và điểm làn trong vùng chữ, có bãi đá vụn dưới chân |
| LG5 | **Lối mòn có đích**: cầu tàu ở ao, đầu cầu, bãi đá chân vách, bếp lửa, khe rừng có vệt đường. Không dừng ở ô (spike §6.3). Trong 14 m quanh một làn, lối mòn lệch hướng làn ≥ 25°. Sân ngã ba chỉ ở chỗ ≥ 3 lối gặp |
| LG6 | **Vùng của Rồng.** Đèn, rào dày gần bệ, thưa dần về cổng. Bệ đọc là chỗ cao được giữ (viền đá; có thể nâng phần nhìn ≤ 0,4 m). Lùm mọc ở các nêm giữa hai làn |
| LG7 | **Mốc khớp sim.** Mặt cầu = đoạn cầu + 0,5 m mỗi đầu; đá lội trong đoạn lội. Hiểm họa hiện trước khi tác dụng (vết lũ, đá lỏng trên vách lở, dải cát ướt, miệng nham cháy xém, bọt nước) |
| LG8 | **Màu.** Màu tín hiệu (#FF4A4A, #FFB020, #FFC83A, #7FF5E0) không gần làn. Tán tím, lam và tán ấm cách làn và ô ≥ 9 m (05 §2.2). Bụi cách vàng Héo #C8D24A ΔE2000 ≥ 20. Không để lỗ hình ô trong decor |

### 2.4 Luật nhìn (rút từ ảnh mẫu)

Số đo ảnh (thu về 384×216): ảnh mẫu / spike mặc định / M0b.

| Số đo | Ảnh mẫu | Spike | M0b |
|---|---|---|---|
| Luma trung bình | 0,522 | 0,422 | 0,395 |
| Cỏ sáng (hue 65–160°, s > 0,3, luma > 0,45) | 41,7 % | 20,6 % | 26,1 % |
| Luma trung vị của cỏ sáng | 0,640 | 0,544 | 0,545 |
| Rất tối (V < 0,22) | 4,6 % | 10,3 % | 9,9 % |
| Xanh két tối (hue 170–235°, luma < 0,3) | 3,0 % | 13,2 % | 18,7 % |
| Điểm ấm đỏ cam | 1,1 % | 0,1 % | 0 % |
| Độ rối chi tiết (trung bình \|L − mờ 5×5\|) | 0,0445 | 0,0585 | 0,0406 |
| Tương phản mảng lớn (độ lệch chuẩn sau mờ 25×25) | 0,126 | 0,111 | — |

Đọc: spike thêm nhiễu nhỏ nhưng mất các mảng sáng lớn. Ảnh mẫu là "mảng sáng lớn, yên; chi tiết nhỏ chỉ ở mép".

| # | Luật | Tham số | Loại sửa |
|---|---|---|---|
| V1 | Bãi trống một phía | Cung trống lớn nhất trong r 9–28 m: không lùm, ≤ 1 lối mòn băng qua, 1–3 cây lẻ. ≥ 40 % vành r 9–30 m (trừ làn) không cây, không decal. Bãi trống ≥ 25 % điểm ảnh của khung mặc định | luật |
| V2 | Đồng cỏ sáng và yên | Bỏ dải "stroke" bị phân bậc trong bãi trống (spike `paint.ts` L367, L407–410; `terrain.ts` L921–922 ở `main`): một mảng nhiễu mềm 20–30 m, ±4–5 % luma, trọng số stroke ≤ 0,08 (đang 0,26). Tông sẫm chỉ dưới bóng tán và sàn rừng | shader |
| V3 | Quầng hai tông | Đất mòn → viền tối 0,15–0,25 m (tối hơn cỏ 25–35 %) → quầng cỏ nhạt khoảng 1 m → đồng. Đĩa đất là 2–3 elip chồng, nhiễu bán kính ≤ ±25 %, 3–5 thùy, lệch 0,3–0,5 R về phía khuất nắng. Bỏ chấm lá đỏ (đọc như máu) | luật + shader |
| V4 | Lùm | ≤ 7 lùm trong sân; cách nhau ≥ 8 m; ≥ 70 % một loài; 1–2 điểm nhấn; 1–2 lùm neo (R 7–9 m) nhập vào rừng mép | luật |
| V5 | Nhịp mật độ | Ba bậc: lùm dày, cây lẻ trên đĩa đất (cách nhau 6–10 m, chỉ ở dải chuyển tiếp), bãi trống | luật |
| V6 | Rừng mép | Một vịnh mỗi 60–90° (sâu 6–10 m, chứa một cây hoặc một lùm nhỏ), 2–3 mũi, nhiễu mép ±4 m, khe ở mọi cổng. Ngọn cây sáng, không thành tường xanh két | luật |
| V7 | Điểm ấm | Cây tán ấm 5–10 % số cây, 6–10 cây trong khung mặc định, cách nhau ≥ 12 m, cách làn và ô ≥ 9 m, ở ngã ba và mặt ngoài lùm. Hue 10–30°, S ≤ 0,70, V ≤ 0,70, ΔE2000 ≥ 20 với ba màu tín hiệu. Hợp canon: 04 §2.3 cho "lá thu đỏ để xa đường". Thử trước bằng **nhuộm cây tán tròn có sẵn** (0 credit) | luật + kit |
| V8 | Bậc đường | Làn 2,6–3 m (sim). Lối chính 1,4–1,6 m, phủ khoảng 95 %, không dải cỏ giữa. Lối nhánh 0,9 m, có dải cỏ | shader + luật |
| V9 | Đồ dọc đường | Lantern Post mỗi 9–12 m trên lối chính, đổi bên, cách mép 0,9 m, cách ô ≥ 4,6 m, cách làn ≥ 2,2 m. Rail Fence 2–4 đoạn ở khúc cong và đầu cầu. Dọc làn chỉ cọc thấp ≤ 1,2 m | kit + `along.ts` |
| V10 | Vách | 3 tầng khoảng 3 m, mặt trên sáng (bỏ sọc mỗi 1,8 m). Cliff Rock xếp mặt vách. Bãi 10–20 đá nhạt 0,8–2 m trên nền đất. Không tảng tròn rêu "như trứng" trên mặt vách | địa hình + kit |
| V11 | Nước | Hue 205–215, giữa sâu hơn, tách khỏi màu rừng. Reed Clump ở bờ chậm, Wooden Jetty ở cuối một lối mòn, lá súng | shader + kit |
| V12 | Tiêu điểm | Bệ có viền (đá hoặc vòng cỏ sẫm). Ba tiêu điểm phụ (ao, vách, mốc), mỗi cái ≥ 80 % trong khung mặc định ở 16:9 và 1280×720. Một mốc có ích mỗi góc phần tư, vì camera xoay tự do | luật |
| V13 | Sạch hue | Thông về hue 120–150, ngọn sáng hơn. Sỏi thành cụm 2–4 viên xám vừa, không chuỗi trắng | shader + luật |
| V14 | Decal | Gom ở mép (vai lối, rìa lùm, bờ nước). Decal ở bãi trống ≤ 30 % lưới hôm nay. Grass Tuft và Wildflower Clump là cụm 3D thưa, dày dần về mép | luật + kit |
| V15 | Thứ bậc độ sáng | Độ sáng và độ bão hòa của cảnh dưới quái, thẻ chữ, hiệu ứng. Không tiêu điểm sáng dưới vùng HUD | phép kiểm |
| V16 | Biến thể, Hắc Vụ | Chỉ đổi sắc, LUT, sương, hạt, 2–4 ô đất (04 §2.3); không đổi bố cục. Hắc Vụ là lớp tham số phủ lên cùng cảnh | preset |

### 2.5 Ánh sáng và lớp sự sống

**Ánh sáng** là một khối trong MapSpec, theo biến thể kit:
- Mặt trời chiếu ngang camera mặc định: phương vị từ Đông (75–115°) hoặc Tây (245–285°), cao 45–55°. **Mỗi ải chọn một phía** theo seed, nên phía cao và vách đổi bên giữa các ải.
- Màu đất của đèn bán cầu chuyển từ tím #6f5d80 (`stage.ts` L204) sang xám xanh khoảng #6d7a5a; bóng lam lạnh, không tím.
- Sương bắt đầu ngoài r 50 m (hôm nay #b6c0d4 phủ góc trên phải khung).
- Quái và tín hiệu dùng chung mặt trời, nên mỗi lần đổi chạy lại `dh-crowd` và `dh-telegraphs`.
- Mặt vách thẳng đứng có pháp tuyến · mặt trời tối đa bằng cos(độ cao): 0,64 ở 50°. Vì vậy luật là ≥ 0,3, thường đạt 0,5–0,6.

**Lớp sự sống L8** (thủ tục, của ta, instanced; ≤ 0,15 ms, ≤ 3 draw call):

| Món | Thông số |
|---|---|
| Đàn chim | 2–3 đàn, mỗi đàn 3–6 con, cứ 15–30 s, cao 12–18 m, chỉ băng qua phần ba ngoài của khung |
| Bóng mây | Nhiễu chiếu xuống đất 40–60 m, −6 tới −8 % luma, trôi 1–2 m/s; tắt ở Low |
| Bướm, đom đóm | 10–20 ở mép bãi cỏ (bướm ban ngày, đom đóm lúc chạng vạng) |
| Khói | Từ đích lối mòn (Campfire Ring) |
| Lá rơi | 0–2 cùng lúc từ cây tán ấm |
| Gió | Một trường gió chung cho cỏ, bụi, cây |
| Gợn ao, đèn chập chờn | Shader; đèn chỉ ở biến thể chạng vạng |

Luật: không thứ gì động thấp hơn 8 m trên vùng chữ hay trên thẻ chữ; chạy nửa nhịp trong đỉnh đợt và khi đánh boss; cài đặt giảm chuyển động tắt chim, bướm, lá. Chim, bướm là sprite 2D (Codex vẽ), chuyển động là của ta. Chấm sự sống trên dải 10 s (20 khung), không trên ảnh tĩnh.

### 2.6 Địa hình

- **Trong sân** (Rồng): sim phẳng. Phần nhìn cao ≤ 1,6 m, dốc ≤ 1:6, làn san phẳng với dốc ≤ 3 %, không vách hay bậc trong sân (trượt H10 và khó đọc ở bốn hướng). Trần chiều cao cây gần bệ giữ min(8; 3,6 + 0,26(r − 10)) m của spike.
- **Ngoài sân:** phía cao mang cao độ và vách; vành ngoài thoải dần về phía thấp và chỗ nước thoát.
- **Trường từ ràng buộc (L1):** cao độ tăng về phía cao; độ ẩm = khoảng cách tới nước; độ mòn = khoảng cách tới bệ, lối, sân. Chúng quyết cỏ tươi mát và lau sậy gần nước, đất khô xa nước và ở sân, đĩa đất dưới cây.
- **Cao độ có luật chơi** (đồi +25 % tầm của hill-meadow, Rainbow Hill +10 % của Lời Gọi) là trường của sim (`padMods`, vùng của Lời Gọi), có bot. Phần nhìn chỉ đắp một gò 1–1,5 m dưới ô đó.
- **Góc 75° nhìn gần thẳng xuống** (tán thành đốm): sửa bằng kit (thân cây lộ, tán khác dáng), không chặn góc.

### 2.7 Kit và credit

**Credit:** còn khoảng 1.100 credit web; 30–60 credit một model; 3D nhận từ 7 điểm, nên tính khoảng 25 % làm lại. Kế hoạch 04 §12.1 (12 model Tripo mỗi kit, 96 + 22) bị bỏ.

**Cách làm kit mới:**
1. **Bộ dùng chung** từ pine-river, nhuộm theo kit bằng sắc và LUT: cây, đá, bụi, cộng 8 món đợt 3 (Lantern Post, Rail Fence, Cliff Rock A và B, Grass Tuft, Wildflower Clump, Reed Clump, Wooden Jetty), Campfire Ring. Ví dụ: Cliff Rock nhuộm đỏ cho red-canyon, sẫm cho volcano; Reed Clump và Wooden Jetty cho mire và rock-coast.
2. **Ảnh 2D của Codex trước** (rẻ, nhận từ 8): 8 ô đất và 4 tấm decal mỗi kit, phông xa, sprite sự sống, billboard cho món nhỏ ở xa, **một ảnh mẫu của chính kit** để đặt dải số đo ảnh.
3. **Tripo chỉ cho 3–5 món chữ ký mỗi kit** (vật mang chữ, một mốc, một loài cây).
4. **Kiểm sổ 025 trước khi tiêu credit.** Dùng lại bằng cách nhập vào media của chính game (`prepare-models --import`), không đọc chéo lúc chạy: mốc Lời Gọi đợt 2 (cầu gỗ, chòi canh) cho hill-meadow; model sci-fi của Space cho Tuyến Cuối.
5. **Metadata kit** trong `registry/kits/<kit>.json`: `role`, `nominalHeightCm`, `footprintCm`, `clearanceCm`, `hueClass`, `castsShadow`, `tintable`, `lodClass`, `maxTris`; cấp kit: bảng màu, `captureBands` (dải số đo ảnh), ánh sáng mặc định, tham số bố cục (hẻm có vách hai bên, bờ biển, mảng nước đầm). Có `check-kit`.

| Nhu cầu | Món | Credit | Còn lại (ước) |
|---|---|---|---|
| Rồng pine-river đợt 3 (ảnh Codex 046; Claude chấm trước) | 8 | khoảng 240 | khoảng 860 |
| Rồng bản thử: Campfire Ring (đích lối mòn, nguồn khói) | 1 | 30–60 | khoảng 800–830 |
| Rồng bản thử: Maple Tree, chỉ khi nhuộm cây có sẵn < 8 điểm | 0–1 | 0–60 | khoảng 740–830 |
| Dự phòng làm lại cho bản thử | 2–3 | 60–90 | khoảng 650–770 |
| Tuyến Cuối: món còn thiếu sau khi kiểm sổ Space | 0–4 | 0–200 | khoảng 450–770 |
| Rồng violet-glade (C3): Glow Mushroom, Glade Arch, Crystal Rock | 3 | 90–180 | khoảng 270–680 |
| Rồng hill-meadow (C4): 2–3 món sau khi nhập mốc Lời Gọi | 2–3 | 60–180 | khoảng 90–620 |
| Lời Gọi 1C (12 mốc Tripo đợt 2 đã có) | 0–2 | 0–100 | |

Các kit mire, rainforest, red-canyon, rock-coast, volcano cần 15–20 món (450–1.200 credit) cộng khoảng 3 món héo dùng chung cho Hắc Vụ (90–180). **Quyết định của chủ dự án trước lát M5:** nạp thêm khoảng 1.000–1.500 credit web, hoặc giảm còn 2 món chữ ký mỗi kit. Không chặn việc tới lúc đó.

### 2.8 Công cụ

| Công cụ | Ở đâu | Ai |
|---|---|---|
| Lõi `shared/game-kit/map`: giữ hash, seeds, raster, edt, along, spec; thêm `siting.ts` (vách theo nắng, ao với hệ số khung, bãi trống, vịnh rừng, khe cổng, vật gây cong), `paths.ts` (A* số nguyên trên lưới 50 cm, làm mượt, bậc, sân ngã ba, đích), `frame.ts` (khung camera trên mặt đất), `checks/{logic,composition}.ts`; sau bản thử: `scatter.ts` (030 viết lại), `paint.ts` (mặt nạ), `life.ts` | repo cha, kit sync vào game | Codex, Claude duyệt |
| CLI `tools/map-factory/cli.mjs`: `validate`, `skeleton` (giải phần `auto` của khung cảnh, ghi ra `out/`), `check`, `guide` (guide.svg), `look` (số đo ảnh, đọc PNG bằng `node:zlib`), `check-kit`, về sau `diff` | repo cha | Codex |
| Bộ đọc `dragon-hold@2` (tách băm) | repo cha | Codex |
| Rồng: `scripts/maps/lint-map.ts` (`pnpm dh:map-lint`), `scripts/maps/graph/` (đồ thị, sinh, ô, quét seed), `prepare-ground`, `prepare-decals`, kịch bản `dh-map-shots` và `dh-map-bench` | repo Rồng | Codex (script), Claude (kịch bản trình duyệt) |
| Phần vẽ Rồng: đọc `L2-cau.map.json`; sơn đất nướng vào render target; đồ dọc đường; sự sống; bậc chất lượng | repo Rồng | Claude |
| Trang so sánh riêng tư (Artifact): ảnh mẫu, M0b, spike, bản mới, 12 góc, AFTER, nheo mắt, 720p, dải sự sống, số đo, guide.svg, ô ghi chú cho từng ảnh | claude.ai, riêng tư | Claude |
| Bảng bản đồ (dev, `?view=mapboard`): guide và hình thật cạnh nhau, khung chơi khóa, tay cầm cảnh, đổi seed cảnh, chọn biến thể, điểm số, ghim ghi chú, nút duyệt | repo từng game, chỉ dev | Claude, ở bước triển khai R1 |

**Bộ giám khảo** (Claude giữ):
- Thang 13 điểm con: bố cục, gom độ sáng, đồng yên, mép, thứ bậc tiêu điểm, điểm màu, nhịp mật độ, khung, cao độ, sáng tối, nhịp lối và đồ, nước, sự sống; cộng điểm chung và đạt/trượt "đọc được khi đang chơi" ở ảnh AFTER.
- Mẫu hiệu chuẩn: nửa trên ảnh mẫu = 10; M0b mặc định ≈ 4,75; spike `final2` mặc định ≈ 6,75. Giám khảo lệch quá 0,75 ở mẫu nào thì bỏ, chạy lại.
- Giám khảo là subagent mới, chỉ thấy thang, mẫu hiệu chuẩn và ảnh; không thấy ghi chú của người dựng. Một giám khảo luôn có; người thứ hai chỉ khi điểm nằm trong ±0,5 quanh cổng.
- **Từ điển góp ý** đổi lời chủ dự án thành tham số: "tối quá" → độ phơi sáng, nền đồng cỏ, mật độ rừng mép; "rối" → decal bãi trống, số lùm, biên độ mảng; "rừng như tường" → vịnh, nhiễu mép; "trống" → cây lẻ, điểm ấm, sự sống; "đường không rõ" → bề rộng lối, tương phản viền; "thiếu sức sống" → số chim, bướm, khói; "dời ao" → ghim ao.

### 2.9 Cổng chất lượng

| Cổng | Ngưỡng |
|---|---|
| Q1 Tất định | `build`/`skeleton` hai lần cùng byte; golden sim của Rồng không đổi với mọi việc cảnh; `pnpm check` đạt |
| Q2 Chiến thuật | H1–H12 đạt (ngoại lệ đã biết của bản ghim ghi rõ); số mềm được báo. Việc khung chơi cần thêm G1–G16, B1–B9, D23 trên 2 họ × 300 seed: cổng đã đạt không được trượt; cổng đang trượt (B1, B7) không tệ hơn quá nhiễu |
| Q3 Hợp lý | LG1–LG8: 0 lỗi |
| Q4 Bố cục (nhìn từ trên) | ≥ 40 % vành r 9–30 m trống; cung trống ≥ 70°, chiếu lên khung mặc định ≥ 25 % điểm ảnh; ≤ 7 lùm trong sân, cách nhau ≥ 8 m; 3 tiêu điểm phụ ≥ 80 % trong khung; 1 mốc mỗi góc phần tư |
| Q5 Số đo ảnh (pine-river; khung mặc định 1080p và 720p) | Luma trung bình ≥ 0,48; cỏ sáng ≥ 35 %, trung vị luma ≥ 0,60, hue 86–96°; đồng sáng (hue 65–160°, s > 0,3, luma > 0,5) ≥ 30 % (ảnh mẫu 40,1 %, spike 16,1 %); rất tối ≤ 6 %; xanh két tối ≤ 6 %; tím ≤ 1 %; điểm ấm 0,5–2 % (khi đã có cây ấm); độ rối ≤ 0,050; tương phản mảng lớn ≥ 0,12. Hiệu chuẩn: ảnh mẫu đạt mọi dòng; M0b và spike trượt ≥ 3 dòng. Kit khác dùng `captureBands` của chính nó |
| Q6 Đọc được | `dh-crowd`: 0 khung có quái bị che ≥ 40 %, che lớn nhất ≤ 35 %; `dh-telegraphs` đạt; tương phản quái với nền không kém M0b quá 10 %; không tiêu điểm dưới vùng HUD; thẻ chữ giữ ≥ 7:1 |
| Q7 Hiệu năng | Rồng High 1080p, 220 quái có xương: tổng ≤ 8 ms trung bình, ≤ 12 ms p95; chênh so với đất trống ≤ 2,0 ms trung bình, ≤ 3,0 ms p95; ≤ +30 draw call; prop ≤ 550 k tam giác ở lượt chính; chênh ≤ +0,8 M tam giác mọi lượt; nạp (rải + nướng) ≤ 300 ms; Medium chênh ≤ 1,5 ms, Low ≤ 1,0 ms (tạm); Firefox đo một lần |
| Q8 Giám khảo | Xem cổng từng chặng ở 3.4 |
| Q9 Chủ dự án | Mỗi kit một lần (`artApproved`, 04 §11.3), mỗi mẫu một lần (guide + một lượt chơi), mỗi chương một tờ ghép; mọi bản đồ của bản thử |

**Chia ngân sách khung hình** (so với đất trống 4,61 ms), cộng 1,7 ms, chừa 0,3 ms:

| Phần | Ngân sách |
|---|---|
| Sơn đất đã nướng | 0,4 ms |
| Prop instanced (cây, đá, đèn, rào, cỏ) | 0,75 ms |
| Vòng impostor | 0,1 ms |
| Nước và ao | 0,2 ms |
| Bóng thêm (chỉ cây > 3 m trong 40 m; cỏ không đổ bóng) | 0,1 ms |
| Sự sống | 0,15 ms |

Khung cảnh (định vị, đường lối) tính offline, nên lúc nạp chỉ còn rải và nướng. Spike đo: mặt nạ 76 ms, rải 13 ms; nướng ước ≤ 120 ms.

**Số đo ảnh không là golden cứng trong Git.** Chúng phụ thuộc GPU và driver. Lưu làm số báo kèm mã máy; cổng chỉ áp trên máy tham chiếu (M4), máy khác dùng dung sai theo lớp máy.

### 2.10 Giữ, đổi, bỏ trong MAP_FACTORY

**Giữ:**
- lõi số nguyên (027–029, 031, 033), sổ 025, bộ đọc 028;
- sinh lúc nạp, không GLB cả bản đồ, Blender chỉ cho từng model;
- L0 chỉ đọc đối với phần cảnh;
- từ spike: shader dải EDT, decal bombing, `impostor.ts`, ao trong `water.ts`, hai kịch bản (đổi tên `dh-map-shots`, `dh-map-bench`);
- `mapNotes` của `report.ts` tới khi lint phủ hết.

**Đổi:**
- Thêm **khung chơi có đồ thị mẫu và lint** phía trước L0 (giai đoạn 5 cũ thành R1–R4 có phiếu).
- MapSpec v0 → v1: thêm `gameplay {adapter, commit, simHash, viewHash}`, `brief`, `lighting`, `scene` (mỗi vật lớn là `auto` hoặc ghim), `layers.life`, `critics`, `approved`.
- Spec gốc nằm trong repo game (`src/view/maps/`); `tools/map-factory/maps/` chỉ giữ mẫu test.
- 030 viết lại thành rải theo cụm và trong mặt nạ; 032 thu lại thành `skeleton` và `check`.
- Giai đoạn 3 "khi rảnh" thành bản thử có ngày (mục 3).
- Cổng 5 "12 ảnh ≥ 8" viết lại: khung mặc định và 4 hướng ở 55° ≥ 8, trung vị 12 ảnh ≥ 8, không ảnh nào < 7.
- Tuyến Cuối từ giai đoạn 6 tùy chọn vào triển khai.
- Loại trừ Maple Tree của phiếu 046 bỏ, thay bằng luật V7.
- Trần "2 M tam giác mọi lượt" (M0b đã duyệt ở 3,09 M, spike 2,53 M) thay bằng trần chênh của bản đồ; đề xuất ghi vào 05 §8, số tổng chỉ báo.

**Bỏ:**
- gộp nhánh spike nguyên khối (chép từng phần qua bản thử);
- hằng số tay toàn cục của spike (đường vách, 5 hướng lối mòn) khi chặng B đạt; `hash2` số thực; tải `/art-src` ở dev;
- mục 5 của MVP "lõi tái hiện spike số thực" (thay bằng ngang bằng theo số đo ảnh);
- 12 model Tripo mỗi kit;
- nền vẽ sẵn của Lời Gọi §22.9 cho sân chơi (chỉ giữ cho phông xa);
- người dựng tự chấm làm cổng;
- stroke phân bậc trong đồng cỏ, màu đất tím của đèn bán cầu, sương trong khung;
- TopoTopo, WFC, xuất GLB, lớp MCP (giữ nguyên NO-GO).

---

## 3. Bản thử một bản đồ Rồng: L2-cau

### 3.1 Vì sao L2-cau

- Là bản đồ duy nhất chơi được: có đợt quái, golden, cổng bot, ải M0, kit thật.
- Có điểm trước để so: M0b khoảng 4,5–5; spike 6,75 (giám khảo độc lập). Có số hiệu năng gốc: đất trống 4,61 ms; spike 7,23 ms trung bình, 8,6 ms p95.
- Có nhiều loại nút nhất: 2 cổng, cầu, chỗ lội, sông, cung bay, vách, ao, 6 ô nhà.
- Có lỗi chiến thuật đã biết, để thử xem lint có tìm ra không.
- Là mẫu của C2, nên định hình các lát phát hành đầu.

Không chọn L1-thang (chưa có dữ liệu, quá đơn giản để chứng minh gì) hay w1-silverfall (Lời Gọi chưa có 3D). Bản đồ mới hoàn toàn sẽ kéo theo đợt quái mới và bot trước khi chứng minh được gì về vẻ ngoài.

### 3.2 Câu chuyện của L2-cau mới (brief)

Khung chơi giữ nguyên ở chặng A–C (`simHash` không đổi).

- **Mặt trời từ Đông**: phương vị khoảng 95° (chỉnh trong 80–110° bằng `dh-crowd` và giám khảo), cao 50°. Bóng đổ sang trái màn hình như ảnh mẫu.
- **Phía cao là phía Tây.** Vách nhạt 3 tầng ở r 38–46 m, khoảng phương vị 215–300°; phần nào có pháp tuyến · mặt trời < 0,3 thì cắt. Vách đóng khung mép trái khung hình.
- **Khe vực ở khoảng 240–260°**, nơi Đường Suối (cổng ở 257°) và dòng suối đi qua. Suối khởi từ một thác nhỏ ở chân vách. Đây là nguồn của cổng Suối (LG1).
- **Sông chảy ngược trong phần nhìn** (dữ liệu không đổi): suối 4 m sinh ra ở khe vực phía Tây Nam, qua chỗ lội (hẹp, nông: lội được là hợp lý), rộng tới 8 m dưới Cầu (sâu: cần cầu), rồi ra Đông Bắc. Bề rộng thành không giảm về hạ lưu; `widthsM` giữ nguyên, chỉ đổi hướng chảy của shader.
- **Cổng Cầu** (khoảng 16°): khe rừng có khúc gỗ đổ bên vệ đường, vệt đường đi tiếp 16 m. **Cổng trời** (khoảng 74°): một cây thông chết cao trên mũi rừng làm chỗ đậu.
- **Bãi trống Đông và Đông Nam** (khoảng 95–200°, r 9–28 m): đồng cỏ sáng. Ao ở mép xa, trong khung (ứng viên khoảng (19, 7): r 20,2 m, phương vị 110°; lint kiểm lại khoảng cách tới ô và cung bay), có Wooden Jetty và Reed Clump. Một lối chính có đèn từ sân bệ ra cầu tàu.
- **Lùm neo** ở nêm Tây Bắc bên kia sông và ở chân vách. Cây tán ấm ở ngã ba và mặt ngoài lùm, cách làn và ô ≥ 9 m.
- **Lối mòn có đích:** sân bệ → cầu tàu ở ao (lối chính); sân bệ → bãi đá chân vách phía Tây Nam (lối chính); ao → Campfire Ring ở vịnh rừng Đông Nam (lối nhánh, có khói); đầu cầu bờ Bắc → chỗ câu cá (lối nhánh). Rail Fence ở đầu cầu.
- **Rừng mép** có vịnh mỗi 60–90° và khe ở mọi cổng. **Sân bệ** có viền đá.

### 3.3 Các chặng

| Chặng | Việc | Ai | Ngày (ước) |
|---|---|---|---|
| 0 Nền (song song, từ 29/10) | Claude chấm 8 ảnh đợt 3, đưa danh sách Tripo; gộp lõi `map-factory` (027–033) vào nhánh làm việc; tạo worktree; xếp phiếu; ghi thuật toán vào phiếu. Codex: ảnh trước (Campfire Ring, Woodpile, Maple Tree dự phòng, sprite sự sống, ô cỏ yên, tờ decal mép và cổng), rồi mã (sửa kit sync, tách băm, đo ảnh, đợt quái theo bản đồ, cột báo cáo theo làn và ô, `prepare-ground`) | Claude, Codex | 29/10–31/10 |
| A Thấy đẹp hơn (không model mới) | Worktree `games/.wt-dh-mappilot`, nhánh `map-pilot` từ `main` 02fe9c7 (`src/view` giống hệt gốc spike 3f3390d). A1: chép commit spike, dời hằng số tay và vị trí ao, lùm vào `src/view/maps/L2-cau.map.json` (cảnh ghim); ngang bằng số đo ảnh với spike `final2` ±0,01. A2: sửa rẻ (đồng cỏ, ánh sáng, viền và thùy, decal gom mép, hue, viền bệ, sỏi xám) và bố cục 3.2 (ghim tay), cây ấm bằng nhuộm (bật/tắt A/B). A3: nướng sơn đất vào render target; đo; trang so sánh số 1; giám khảo | Claude | 31/10–04/11 |
| B Luật thay tay | Đồ thị L2-cau (ghim khung), L2-l, L2-doi; lõi giải `auto` (vách, ao, bãi trống, vịnh, khe cổng, vật gây cong, lối mòn tới đích); phần vẽ đọc khung cảnh từ CLI. Bản suy ra chỉ thay bản ghim khi bằng hoặc hơn về số đo ảnh, 0 lỗi hợp lý, giám khảo không thấp hơn A quá 0,25. Thử tổng quát | Codex (lõi, đồ thị), Claude (thuật toán, nối, chấm) | 03/11–12/11 |
| C Kit và sự sống | Xử lý GLB của chủ dự án (Blender `--kind props`, `prepare-models`, metadata); đặt đồ theo luật; sự sống; bậc Medium, Low; Firefox; `dh-map-shots` (12 góc, 720p, nheo mắt, AFTER với mọi ô đã xây và quái đợt 7 có thẻ, dải 10 s); giám khảo; trang so sánh số 2; chủ dự án duyệt và chơi; gộp vào `main` của Rồng, changelog | Claude, chủ dự án | khi có model; đích 10/11–17/11 |
| D Chiến thuật (song song với C) | Lint tái hiện lỗi đã biết; thang ứng viên qua bot; kiểm dự đoán | Claude, máy | 06/11–14/11 |

**Thang ứng viên chiến thuật** (mỗi bước chạy cùng bản gốc trên 2 × 300 seed; chỉ giữ khi mọi cổng đạt trên cả hai họ; golden đổi có chủ ý, có changelog):
- **v2a, chỉ ô:** dời `cau-t1` từ 4 m sang 5 m dọc làn (r 25,35 m, trong vòng 26 m; cách `cau-t2` 5 m); khai vai trò mọi ô nhà và dời `h-se` về một vai trò nó đạt (ô chung hoặc ô làn Suối); thêm một ô với tới đầu cung bay.
- **v2b:** v2a + mặt cầu hẹp hơn làn (2,6 m, tỉ lệ 0,87: nghẽn thật); `policy.ts` đọc tỉ lệ thay hằng ×1,2.
- **v2c:** v2b + khúc cong có vật gây cong, làn dài khoảng 27–29,5 m (trong dải 24–36 m). Đây là phép thử đòn bẩy I↔Q: L2-cau ở sát 24 m, quái S2 tới bệ trong 12,3 s so với 15–20 s của 02 §1.
- Bước nào làm gãy cổng thì chia đôi thay đổi để tìm nguyên nhân; không giữ được thì giữ v1 và ghi lý do.

**Kiểm dự đoán:** mỗi kết quả bot có một số tĩnh dự đoán chiều thay đổi:

| Kết quả bot | Số tĩnh dự đoán |
|---|---|
| I (thời gian rảnh) | Đi trước vùng chữ (S2) |
| Q | Sàn Q (S3) |
| Tỉ phần sức ép theo làn ở đợt 7 (hôm nay Cầu 58,2 %) | Đòn bẩy mỗi làn (bẫy trong vòng, ô phủ, nghẽn) |
| Số nhịp Herb Hut theo ô | Mét làn trong 7 m của ô |
| Độ dàn dùng ô | Độ dàn phủ của ô |

### 3.4 Cổng nghiệm thu

**Cổng A (cuối chặng A, không model mới):**
- `simHash`, `tests/golden/m0.json` không đổi; `pnpm check` đạt.
- Số đo ảnh Q5 đạt mọi dòng ở khung mặc định 1080p và 720p (điểm ấm tính khi bật cây nhuộm).
- Giám khảo độc lập: trung vị 12 ảnh ≥ 7,5, không ảnh nào < 6,5.
- Q6 đạt. Q7: chênh ≤ 2,0 ms trung bình và ≤ 3,0 ms p95 sau khi nướng sơn đất.
- Q3 (hợp lý) chỉ báo, chưa chặn (cảnh còn ghim tay).

**Cổng B (luật thay tay):**
- Bản suy ra ≥ bản ghim A về mọi dòng Q5 (dung sai 0,005), Q3 0 lỗi, Q4 đạt, giám khảo không thấp hơn A quá 0,25.
- **Thử tổng quát**, không thêm tọa độ tay hay hằng số luật:
  - L2-cau lật gương (x → −x; mặt trời, vách, bãi trống lật theo): Q3–Q5 đạt, giám khảo khung mặc định ≥ 7,5;
  - L2-cau với 3 seed cảnh khác: Q3–Q5 đạt;
  - L2-l và L2-doi: 64 seed mỗi mẫu, ≤ 1 s mỗi seed trong Node, ≥ 50 % seed đạt luật cứng; seed tốt nhất được dựng cảnh trong hộp cát dev ≤ 300 ms, Q3 đạt, Q5 đạt hoặc ghi rõ dòng trượt.
- Luật không đạt sau 2 vòng: được ghim vật lớn đó, ghi là "ngoại lệ ghim" kèm lý do. Nhưng tổng quát vẫn phải đạt thì cách làm mới được coi là đúng.

**Cổng C (ship):**
- Giám khảo độc lập (đã hiệu chuẩn): khung mặc định và 4 hướng ở 55° mỗi ảnh ≥ 8; trung vị 12 ảnh ≥ 8; không ảnh nào < 7; AFTER ≥ 7,5; sự sống ≥ 7 trên dải 10 s.
- Q1–Q7 đạt; Q7 ở High, Medium, Low, và một lượt Firefox (hoặc ghi rõ "chưa đo").
- Chủ dự án xem trang so sánh, chơi 10 đợt, nói "đạt".

**Cổng D (chiến thuật):**
- Lint trên L2-cau v1 tái hiện, sai số ±0,05 m, ±1°, ±0,1 s: độ dài 24,59 / 25,29 m; cổng r 30,22 / 30,81 m; độ quanh co 1,015 / 1,019; khúc Suối 21,2°; vào vòng ở 4,35 / 4,95 m; khoảng cách làn nhỏ nhất 9,15 m; phương vị đầu làn 4° / 266°; và năm phát hiện: `h-se` không với tới làn nào trong 10 m; `h-nw` là ô chung duy nhất; `cau-t1` ở r 26,32 ngoài vòng; tỉ lệ cầu 1,13 (không nghẽn) trong khi bot tính ×1,2; chỉ `cau-t4` (9,4 m) cho Net Launcher với tới đầu cung bay.
- Thời gian đi trước vùng chữ của lint bằng đúng `zoneDelayMs` của `waves.ts` cho mọi làn × quái, và khớp thời gian rảnh "approach" của `anatomy.ts` trong ±10 %.
- Dự đoán đúng chiều ≥ 12 trên 15 phép so (5 kết quả × 3 ứng viên). Trượt thì số tĩnh chỉ dùng để lọc, mọi bản đồ vẫn qua bot đầy đủ (chi phí không đổi).
- Giữ ứng viên là tùy chọn; chạy hết thang và ghi số là bắt buộc.

**GO cho triển khai** = A + B + C + phần kiểm dự đoán và tái hiện của D.

### 3.5 Không đạt thì sao

| Tình huống | Làm gì |
|---|---|
| Số đo ảnh đạt mà giám khảo < 8 | Kit là giới hạn: thêm ≤ 2 món Tripo, chấm lại một lần |
| Số đo ảnh trượt | Sửa luật bố cục, tối đa 2 vòng, áp cho mọi bản đồ của kit, không vá riêng một bản đồ |
| Vẫn < 8 sau đó | Đưa chủ dự án một lựa chọn: nhận 7,5 để triển khai, hoặc chi thêm cho kit |
| Hiệu năng trượt | Giảm mật độ rải theo bậc; cắt bóng phụ; giảm sự sống |
| Tổng quát trượt | Sửa lược đồ đồ thị và luật trước khi triển khai |
| Dự đoán trượt | Giữ đồ thị cho hợp lý và cảnh; số tĩnh chỉ lọc; bot đầy đủ cho mọi ải |

### 3.6 Thời gian

- Agent: Claude khoảng 10–12 ngày làm việc; Codex 34 phiếu dưới một giờ (6 ảnh, 28 mã; khoảng 6–7 cửa sổ hạn mức). Danh sách ở `TICKETS.md`.
- Lịch: khoảng 3 tuần, xong khoảng 17/11 nếu chủ dự án dựng model trước 08/11.
- Chủ dự án: khoảng 2 giờ (Tripo khoảng 80 phút; trang so sánh số 1 khoảng 10 phút, không bắt buộc; trang số 2 và chơi 10 đợt khoảng 30 phút).

---

## 4. Triển khai sau bản thử

### 4.1 Rồng theo chương và kit

**Điều kiện trước (khoảng 2–3 ngày, làm trong bản thử hoặc ngay sau):**
- chuyển phần rải và mặt nạ sơn đất của bản thử (đang số thực trong phần vẽ) sang lõi số nguyên, một lần, lấy đầu ra bản thử làm mẫu; ngang bằng theo số đo ảnh;
- `stages:gen`, `stages:validate` (có lint chiến thuật và hợp lý), dấu vân tay và luật khác biệt;
- `cli diff`: liệt kê các bản đồ đã duyệt có băm lớp đổi khi luật hay kit đổi; chủ dự án chỉ xem tờ của các bản đó;
- bảng bản đồ v1 (khung chơi khóa, chọn seed và biến thể, ghim ghi chú, điểm số, nút duyệt).

| Đợt | Lát (04 §12.3) | Bản đồ | Cần | Cổng | Ngày (ước) |
|---|---|---|---|---|---|
| R1 | M2, C1 (20 ải) | L1-thang, L1-s, L1-xoan (móc) trên pine-river xuân | Dữ liệu C1 của làn Rồng (file chương, đợt); hiệu chuẩn mẫu; phép thử độ nhạy: 3 seed mỗi mẫu trên 2 × 300, kết quả cổng lệch ≤ ±3 điểm | Mỗi ải: Q1–Q6 tự động, bot 2 × 300. Giám khảo: khung mặc định của ải dựng tay (1, 10, 20), 1 trên 10 ải còn lại chọn ngẫu nhiên, và mọi ải trượt số đo ảnh. Chủ dự án: mỗi mẫu một lần (guide + một lượt chơi), tờ ghép 20 ải | 18/11–05/12 |
| R2 | M3, C2–C3 | L2-doi, L2-l, L2-tach, L2-cau (họ seed) trên pine-river hè; kit violet-glade | Biến thể hè (sắc, LUT, ô; không model); violet-glade: ảnh mẫu kit, ô, decal, `captureBands`, 3 món Tripo; Glow Mushroom là vật mang chữ (trường `objects`, bot) | Kit `artApproved` (3 góc × 4 hướng); như R1 | tháng 12 |
| R3 | M4, C4–C6 | hill-meadow (ô đồi +25 % trong sim), mire, rainforest | `padMods`, `hazards`, `spawns`; nhập mốc Lời Gọi cho hill-meadow | Như trên; cơ chế chữ ký qua bot | tháng 1–2/2027 |
| R4 | M5 trở đi | red-canyon, rock-coast, volcano; 3 và 4 làn (G10 đọc được ở 4 làn); lớp Hắc Vụ | Quyết định nạp credit | Như trên | theo lát |

- **Chi phí mỗi ải:** khoảng 1 giây sinh, khoảng 10–11 phút bot, vài phút agent đọc báo cáo. Toàn 520 ải khoảng 90 giờ máy, chạy qua đêm theo lát.
- **Chi phí mỗi mẫu:** khoảng nửa ngày Claude (đồ thị, xem hiệu chuẩn) cộng khoảng 11 phút bot mỗi cơ chế kit.
- **Chi phí mỗi kit:** khoảng 2–3 ngày Claude, ảnh Codex, 25–35 phút Tripo và 10 phút duyệt của chủ dự án.
- **Khác biệt:** dấu vân tay (phương vị cổng, phương vị bãi trống, phía mặt trời, loại nước, bộ mốc) cách 10 ải trước ≥ ngưỡng; ≤ 3 ải liền cùng mẫu (04 §3.2); hai ải trong chương khác nhau ở ≥ 2 trong {mẫu, phía mặt trời, bãi trống ±45°, loại nước, mốc chính}.
- **Spec trong Git:** mỗi ải 1–2 KB JSON, khoảng 1 MB cho 520 ải. Không media.

### 4.2 Lời Gọi (w1-silverfall)

**Ngay, còn 2D (rẻ):**
- Lint chiến thuật TD (`tools/map-factory/lint/td.mjs`) trên bản trích 028; lớp nhiệt độ phủ trong `debug-2d` khi làn Lời Gọi rảnh.
- Bí danh `td-sandbox` ↔ `w1-silverfall` trong bộ đọc; không đổi id sim ngoài lượt đặt tên.
- Đề xuất cho làn Lời Gọi (qua bot của nó): nền Rainbow Hill +10 % tầm, nền Watchtower, đoạn chết của boss ≤ 15 s.
- Ghi vào §22.9 rằng "ảnh nền vẽ sẵn rồi vẽ luật đè lên" bị thay bằng Map Factory cho sân chơi; ảnh vẽ chỉ còn cho phông xa.
- Sửa MAP_FACTORY §6.5: 12 GLB mốc Tripo đợt 2 đã có trong `art-src/3d/landmarks` (cau-go, choi-canh-doi, vach-thac-bac…).
- Codex: 6 ô đất đồng cỏ, 2 tấm decal.

**Ở bước 1C (3D):**
- Cùng luật cảnh (V, LG). Ảnh mẫu Haven Grove còn hợp Lời Gọi hơn, vì đây là game xây làng.
- Cảnh bằng billboard 2D của bộ `meadow` (60 file) theo ngân sách §23.10 (High 1.500 vật lớn + 4.000 cỏ, ≤ 6 draw call) cộng các mốc Tripo đã có.
- **Cảnh phản ứng khi người chơi xây:** sơn lại một ô 16 × 16 m của render target quanh nhà mới (≤ 4 ms, chia qua nhiều khung): đất mòn và quầng; một lối mòn nhánh từ cửa nhà ra đường gần nhất theo A* của lưới xây (chỉ để nhìn); decor trong nền nhà bị dọn (`clearOnBuild`).
- Cổng: Q1, Q3–Q8 với ngân sách §25.12 của Lời Gọi; golden luật không đổi.
- Bản đồ 2–3, Đồi Chè, bản đồ neon: viết brief sau khi bản đồ 1 đạt; bản đồ neon cần ảnh mẫu riêng.
- Ngày: 1C chưa lên lịch; phần bản đồ khoảng 1,5 ngày cộng bộ dựng billboard (việc của 1C, 3–4 ngày).

### 4.3 Tuyến Cuối

**Trước mọi việc sân:** làn Tuyến Cuối sửa việc đọc chéo model của Space. `vite.config.ts` (L13–24) phục vụ `/assets/space-typing/models/` từ thư mục Space ở dev và qua alias nginx khi chơi, "không bao giờ chép vào dist" (AGENTS.md L98). Như vậy game không deploy một mình được. Món kit bản đồ mới phải nhập vào media của chính Tuyến Cuối.

**Cách làm: dải set-piece.**
- Sân chơi 24 × 40 m (mã `FIELD` gateZ 40 là sự thật; sửa "khoảng 60 m" ở SURVIVAL_MODE_PLAN §4.1 và "60 bản đồ" ở §4.0) **giữ trống**: không vật gì trong |x| ≤ 12, z 2,4–40, trừ vật cản đã qua bot.
- Trang trí ở dải bên (x 12–22): mô-đun dọc z (lan can, máng ống, ăng-ten, chồng hàng, đoạn vỡ mở ra không gian), cổng vòm ở đầu xa, lõi trạm hay đường ray đoàn xe khi `FieldPreset` yêu cầu.
- Sàn: sơn bẩn, vết cháy, mòn tấm theo dải EDT; sọc cảnh báo quanh khe sinh và hiểm họa.
- Phông thị sai 2–3 lớp mỗi họ quái (tinh vân, vành đai thiên thạch, trạm vỡ), ảnh Codex, cộng shader hố đen sẵn có.
- Sự sống: mảnh vụn trôi, tàu xa bay qua, đèn hiệu nháy, tia lửa từ ống vỡ.
- Mẫu sân (`FieldPreset`): hành lang, hai đầu, đoàn xe băng ngang, trạm giữa. 60 chương = khoảng 5–6 sân × mẫu mục tiêu × phông × vị trí hiểm họa × seed.
- **Câu hỏi luật "không model dựng bằng mã":** sàn, tường, ray, ống hiện dựng bằng mã. Khuyến nghị cho làn Tuyến Cuối: tính chúng là bề mặt cấu trúc như đất và đường; mọi vật rời phải là model hoặc billboard. Báo chủ dự án, không chặn.
- **Ảnh mẫu:** chưa có cho sci-fi. Codex vẽ 2 ảnh ý tưởng; chủ dự án chọn một (5 phút); dải số đo ảnh hiệu chuẩn theo ảnh đó so với sân hôm nay.
- **Thứ tự:** sửa đọc chéo → ảnh mẫu → dựng lại Vành Chân Trời (chỉ phần nhìn, golden giữ) → mỗi mẫu mục tiêu một sân → phông theo họ quái.
- **Ngày:** sân đầu khoảng 5–7 ngày, ngay sau bản thử Rồng (khoảng 18/11–28/11), song song R1 vì khác repo và làn.

### 4.4 Lịch thô

| Thời gian | Việc |
|---|---|
| 29/10–31/10 | Chặng 0: chấm ảnh đợt 3, gộp lõi, worktree, ảnh Codex, phiếu mã nền |
| 31/10–04/11 | Chặng A; trang so sánh số 1 (khoảng 04/11) |
| 03/11–12/11 | Chặng B (Codex lõi và đồ thị song song) |
| khi có model, đích 10/11–17/11 | Chặng C; chủ dự án duyệt và chơi |
| 06/11–14/11 | Chặng D (bot) |
| khoảng 17/11 | GO/NO-GO triển khai |
| tháng 11 | Lời Gọi: lint TD, bí danh, sửa tài liệu, ảnh ô đất |
| 18/11–28/11 | Tuyến Cuối sân đầu |
| 18/11–05/12 | Rồng R1 (C1), cùng dữ liệu M2 của làn Rồng |
| tháng 12 trở đi | Rồng R2; mỗi lát một kit |
| khi 1C bắt đầu | Lời Gọi bản đồ 1 trong 3D |

Ngày là ước, phụ thuộc hạn mức Codex, lúc làn Rồng rảnh, và lúc chủ dự án dựng model.

---

## 5. Việc của chủ dự án

| Khi nào | Việc | Thời gian | Credit |
|---|---|---|---|
| Sau khi Claude chấm xong (khoảng 30/10) | Dựng 8 món đợt 3 trên web Tripo (Lantern Post, Rail Fence, Cliff Rock A, Cliff Rock B, Grass Tuft, Wildflower Clump, Reed Clump, Wooden Jetty) | khoảng 60 phút | khoảng 240 |
| Sau khi ảnh Codex đạt | Dựng Campfire Ring | khoảng 10 phút | 30–60 |
| Chỉ khi cây nhuộm < 8 điểm | Dựng Maple Tree | khoảng 10 phút | 0–60 |
| Khoảng 04/11 (không bắt buộc) | Xem trang so sánh số 1, ghi chú | 10 phút | 0 |
| Khoảng 14–17/11 | Xem trang so sánh số 2, chơi 10 đợt L2-cau, nói "đạt" hoặc ghi chú bằng lời của mình | 30 phút | 0 |
| Sau bản thử | Chọn ảnh mẫu sci-fi cho Tuyến Cuối | 5 phút | 0 |
| Sau bản thử | Dựng món Tuyến Cuối còn thiếu sau khi kiểm sổ Space | 0–40 phút | 0–200 |
| Mỗi mẫu bố cục mới | Xem guide, chơi một lượt | khoảng 10 phút | 0 |
| Mỗi chương | Duyệt tờ ghép 20 ải | khoảng 10 phút | 0 |
| Mỗi kit mới | Dựng 3–5 món chữ ký; duyệt kit (3 góc × 4 hướng) | khoảng 40 phút | 90–180 |
| Trước lát M5 | **Quyết định:** nạp thêm khoảng 1.000–1.500 credit, hay 2 món chữ ký mỗi kit | 5 phút | — |

Mọi việc khác theo khuyến nghị của Claude; cổng nào gãy thì báo.

**Báo chủ dự án, không hỏi** (ghi trong changelog và canon):
- dải làn giữ 24–36 m tới khi v2c cho số; vai trò ô nhà thay "2–6 m từ đường";
- L1-xoan thành móc ≤ 36 m, L4-vong một làn đi cung ≤ 120°, L1-s biên độ ≤ 4 m;
- cây tán ấm cho phép ≥ 9 m từ làn (04 §2.3), thử nhuộm trước;
- trần tam giác tính theo phần chênh của bản đồ;
- Tuyến Cuối: sân 24 × 40 m theo mã; bề mặt cấu trúc dựng bằng mã (khuyến nghị cho làn đó);
- nền vẽ sẵn của Lời Gọi §22.9 chỉ còn cho phông xa;
- tên món mới bằng tiếng Anh (Campfire Ring, Glow Mushroom…); tên làn có sẵn ("Đường Cầu", "Đường Suối") chỉ đổi trong lượt đặt tên của Rồng.

---

## 6. Rủi ro

| Rủi ro | Cách giảm |
|---|---|
| Luật tự định vị ra cảnh chung chung như spike | Bản ghim tay ở chặng A là mức sàn; bản suy ra chỉ thay khi bằng hoặc hơn; ghim vật lớn là lối thoát có ghi lại |
| Luật khớp riêng L2-cau | Thử tổng quát: lật gương, 3 seed, L2-l, L2-doi; sửa luật, không sửa bản đồ |
| Giám khảo nhiễu, tự thiên vị, lệch gu chủ dự án | Người dựng không chấm; mẫu hiệu chuẩn có luật bỏ; số đo ảnh; chủ dự án quyết cuối |
| Mặt trời ngang hay đồng sáng hơn làm quái, tín hiệu khó đọc | Q6 (`dh-crowd`, `dh-telegraphs`, tương phản quái với nền) trước mọi lần gộp |
| Hiệu năng vượt khi thêm đồ và sự sống | Nướng sơn đất trước; ngân sách từng phần chừa 0,3 ms; khung cảnh offline; bậc Medium, Low; Firefox |
| Cây ấm lẫn với màu tín hiệu | Dải hue, S, V; ΔE2000 ≥ 20; ≥ 9 m từ làn; ảnh AFTER có thẻ và hiệu ứng |
| Lantern Post trang trí lẫn với Firefly Lamp có luật (kit sương) | Dáng và màu khác; kiểm khi kit sương tới |
| Số tĩnh không dự đoán được bot | Bot vẫn là sự thật cho mọi ải; số tĩnh chỉ lọc |
| Giờ máy bot (khoảng 90 giờ cho 520 ải) | Chạy qua đêm theo lát; bản thử đo số thật |
| Đợt quái gắn một bản đồ | Đợt quái theo bản đồ trước bản đồ thứ hai |
| Hết credit | Bộ dùng chung, nhuộm, billboard, dùng lại từ sổ; quyết định nạp trước M5 |
| Ảnh Codex tự chấm quá cao | Claude chấm trước khi chủ dự án tiêu credit; tối đa 3 lượt |
| Tích hợp (nhánh lõi chưa gộp, lỗi kit sync, nhiều worktree) | Chặng 0 làm trước; mỗi thư mục một người ghi; Claude duyệt và commit |
| Số đo ảnh lệch theo máy | Báo kèm mã máy; cổng trên máy tham chiếu |
| Tuyến Cuối đọc chéo Space | Phiếu riêng cho làn đó trước việc sân; món kit chỉ nhập vào media của chính game |
| Bảng bản đồ lan phạm vi | Bản thử chỉ dùng trang so sánh; bảng v1 ở R1, khung chơi khóa |

---

## Nguồn (truy cập 28/10/2026)

**Cách làm bản đồ**
- [R1] T. Thompson, "How Townscaper Works", Game Developer, 06/04/2022. https://www.gamedeveloper.com/game-platforms/how-townscaper-works-a-story-four-games-in-the-making
- [R2] N. Rueda, phỏng vấn Á. Azofra (Ironhide), ENTER.CO, 25/02/2014. https://www.enter.co/especiales/videojuegos/la-ciencia-y-el-arte-detras-de-un-buen-tower-defense-entrevista/
- [R3] O. Stålberg, Everything Procedural 2018. https://80.lv/articles/using-wave-function-collapse-algorithm-for-dioramas
- [R4] "Strategic minimalism behind indie hit Islanders", 14/06/2019. https://wnhub.io/news/analytics/item-2245
- [R5] Galin, Peytavie, Maréchal, Guérin, "Procedural Generation of Roads", CGF 29(2), 2010. https://perso.liris.cnrs.fr/egalin/Articles/2010-roads.pdf
- [R6] Emilien và cộng sự, "Procedural Generation of Villages on Arbitrary Terrains", Visual Computer 2012. https://hal.archives-ouvertes.fr/hal-00694525
- [R7] Diễn đàn Unity về đường theo spline (2024–2026). https://discussions.unity.com/t/road-system-for-unity-based-on-the-current-spline-package-and-the-terrain-system/1664437
- [R8] Diễn đàn three.js 2018–19 https://discourse.threejs.org/t/how-to-create-a-multiple-textured-terrain/5069 ; https://github.com/nickfallon/textureSplat ; https://github.com/TokisanGames/Terrain3D/blob/main/doc/docs/shader_design.md
- [R9] Felzenszwalb, Huttenlocher, "Distance Transforms of Sampled Functions", Theory of Computing 8(19), 2012. https://theoryofcomputing.org/articles/v008a019/
- [R10] I. Quilez, domain warping. https://iquilezles.org/articles/warp
- [R11] Glanville, "Texture Bombing", GPU Gems ch. 20, 2004. https://developer.nvidia.com/gpugems/gpugems/part-iii-materials/chapter-20-texture-bombing
- [R12] Bridson, SIGGRAPH 2007 sketch. https://www.cs.ubc.ca/~rbridson/docs/bridson-siggraph07-poissondisk.pdf
- [R13] Red Blob Games, polygon map generation. https://www.redblobgames.com/maps/polygon-map-generation/
- [R14] Lane, Prusinkiewicz, Graphics Interface 2002. https://www.algorithmicbotany.org/papers/eco.gi2002.html
- [R15] J. van Muijden, GDC 2017 (Horizon Zero Dawn). https://www.guerrilla-games.com/read/gpu-based-procedural-placement-in-horizon-zero-dawn
- [R16] E. Carrier, "Procedural World Generation of Far Cry 5", GDC 2018. https://gdcvault.com/play/1025557/ ; https://blog.playstation.com/2018/03/22/the-procedural-world-generation-of-far-cry-5/
- [R17] Epic, PCG framework. https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-framework-in-unreal-engine
- [R18] Burgess, Purkeypile, "Skyrim's Modular Approach to Level Design", GDC 2013. https://www.gamedeveloper.com/design/skyrim-s-modular-approach-to-level-design
- [R19] Boris the Brave, "WFC tips and tricks" (cập nhật 28/02/2025). https://boristhebrave.com/2020/02/08/wave-function-collapse-tips-and-tricks
- [R20] J. Dormans, PCG Workshop 2010. https://www.pcgworkshop.com/archive/dormans2010adventures.pdf
- [R21] Boris the Brave, "Dungeon Generation in Unexplored". https://www.boristhebrave.com/2021/04/10/dungeon-generation-in-unexplored/
- [R22] Togelius, Yannakakis, Stanley, Browne, IEEE TCIAIG 3(3), 2011. https://course.ccs.neu.edu/cs5150f13/readings/togelius_sbpcg.pdf
- [R23] Liapis, Yannakakis, Togelius, "Sentient Sketchbook", 2013. https://www.antoniosliapis.com/projects/project_sentient_sketchbook.php
- [R24] Duan và cộng sự 2025 https://arxiv.org/abs/2501.13964 ; Panickssery và cộng sự, NeurIPS 2024 https://arxiv.org/abs/2404.13076 ; Earle và cộng sự (ScriptDoctor) 2025 https://arxiv.org/abs/2506.06524 ; SimWorlds 2026 https://arxiv.org/pdf/2607.01766 ; Word2World https://themoonlight.io/review/word2world-generating-stories-and-worlds-through-large-language-models
- [R25] LDtk 1.2 https://deepnight.itch.io/ldtk/devlog/471310/ldtk-120-is-out-happy-new-year ; Three.js Level Creator https://defacci.itch.io/threejs-level-creator/devlog/1458096/threejs-level-creator-first-release ; Triplex https://learnwithjason.dev/3d-in-react-with-triplex-a-visual-editor-for-react-three-fiber
- [R26] Zhang, Rao, Agrawala, ControlNet, ICCV 2023. https://arxiv.org/abs/2302.05543
- [R27] B. Rockenbeck, GDC 2021 (gió của Ghost of Tsushima). https://gdcvault.com/play/1027124/Blowing-from-the-West-Simulating

**Thiết kế màn TD, làn, sân**
- [R28] T. Phan, "Tower Defense Game Rules (Part 1)", Game Developer, 27/04/2017. https://www.gamedeveloper.com/design/tower-defense-game-rules-part-1-
- [R29] Bloons wiki, Map difficulty (wiki cộng đồng). https://www.bloonswiki.com/Map_difficulty
- [R30] D. Harlow, "Kingdom Rush – the wonderful campaign level design", Game Developer, 25/10/2013. https://www.gamedeveloper.com/design/kingdom-rush---the-wonderful-campaign-level-design
- [R31] Plants vs. Zombies, Wikipedia. https://en.wikipedia.org/wiki/Plants_vs._Zombies_(video_game)
- [R32] Riot, cập nhật Summoner's Rift 06/2014 và "Defining the Rift's Visual Style" (bản đăng lại). https://www.surrenderat20.net/2014/06/update-to-summoners-rift-headed-to-pbe.html ; https://www.surrenderat20.net/2014/11/red-post-collection-defining-rifts.html?m=1
- [R33] Phỏng vấn Bad North, Nintendo UK, 04/2018. https://www.nintendo.co.uk/News/2018/April/Interview-Taking-on-hordes-of-invading-Vikings-in-Bad-North-1368315.html
- [R34] The Level Design Book (blockout, composition). https://book.leveldesignbook.com/process/blockout
- [R35] Nghiên cứu năm yếu tố của Lynch trong A Short Hike và Sable. https://cs.wellesley.edu/~pmwh/mvmap/papers/open_world_elements/open_world_elements.html

**Trong repo**
- `docs/tools/MAP_FACTORY.md` (§1.1, §3, §4.2, §6, §8.3, §8.5, §9, §11); `docs/tools/map-factory/spike-l2-cau.md` (§3, §5, §6, §7, §8); `docs/codex-queue/046-dh-set-dressing-2d.md`
- Rồng: `src/content/data/{maps,stages,waves}.ts`, `src/content/{types,rules}.ts`, `src/sim/{lanes,words,spawn,movement,combat}.ts`, `src/view/{terrain,scatter,water,paths,stage}.ts` (stage.ts L201 camera 30°, L204 màu đất bán cầu), `scripts/balance/{report,meter,anatomy,policy}.ts`, `tests/content/map.test.ts`, `docs/changelog/2026-10-26-review-fix.md`, `2026-10-26-b1b7-names.md`, `2026-10-27-owner-decisions.md`
- Spike: `games/.wt-dh-mapspike` nhánh `map-spike` (`src/view/{layout,paint,impostor}.ts`; `paint.ts` L367, L407–410), ảnh `tmp/shots/mapspike/final2/`
- `docs/games/dragon-lane/`: 00-canon §4.4, §7, §8; 01 §2.1, §3.2; 02 §1, §5.5; 03 §8; 04 §2, §3, §4.3, §5.6, §11, §12; 05 §2, §2.2, §4.3, §8; `research/art-pipeline.md` §2, §5, §9
- `docs/games/BALANCE.md` §3, §7, §9
- Lời Gọi: `docs/td/TYPING_DEFENSE_DESIGN.md` §22.9, §23.10, §25.12, §26.1; `BUILD_1B.md` §4; `src/content/{slice-1a,rules}.ts`; `art-src/3d/landmarks/SOURCES.json`
- Tuyến Cuối: `docs/SURVIVAL_MODE_PLAN.md` §4.0, §4.0b, §4.1; `BUILD_S1.md` §1.1, §5.2; `src/content/{rules,stage-rules}.ts`; `src/view/scene.ts`; `vite.config.ts` L13–24; `AGENTS.md` L98
- Ảnh: `tmp/map-studio/owner-reference-haven-grove.webp`, `now-rong-giu-ai-m0b.png`; script đo ảnh của Claude ngày 28/10 (`stats.mjs`, `stats2.mjs`, `stats3.mjs`, chép vào phiếu MF-C04)
