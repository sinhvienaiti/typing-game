
## 9. Song Long toàn sân, không phụ thuộc map (04/11/2026, chiều)

**Vì sao làm lại:** quyết định của anh lúc 11:50 (đầu tài liệu): chiêu dùng chung cho nhiều map, nên không được chạy về hai cổng; nó phải là chiêu diện rộng toàn sân. Giữ hai rồng, một viên ngọc và cao trào hoa sen. Mục này thay §3 A ở phần hình học và khung; luật sát thương của hộp xám (§8.6, `hit()`, ngân sách) giữ nguyên. Hộp xám hai hành lang (§8) chỉ còn là số đo để so.

### 9.0 Chốt

1. **Đầu vào chỉ có ba thứ:** khung sân (hình chữ nhật), Trận Tâm H và chỗ người ra chiêu C, và ảnh chụp mọi thú sống nhận được sát thương ở F0 (vị trí, độ cao). Không đọc nhãn cổng, đường đi, waypoint, trường dòng chảy hay điểm vào của quạ.
2. **Hai rồng chia đôi triều thú theo hướng ngang của người chơi:** trục F đi từ người chơi tới Trận Tâm, trục R vuông góc. Xếp thú theo tọa độ ngang, nửa trái cho rồng 0, nửa phải cho rồng 1; số thú hai bên lệch nhau tối đa 1 con.
3. **Mỗi rồng bay một vòng qua tối đa 3 "điểm neo" rồi về ngọc.** Điểm neo chọn bằng cách lấy điểm xa nhất (farthest-point sampling): con xa Trận Tâm nhất, rồi con xa nhất so với người chơi, ngọc và các neo đã chọn. Thứ tự bay là thứ tự ngắn nhất trong tối đa 6 cách. Rồng vẫn bay sóng chữ S như hộp xám, thân và vệt cháy như cũ.
4. **Ngọc** ở 3/5 đường từ Trận Tâm tới tâm khối thú đất, không quá 12 m, cách mép sân ít nhất 2 m. **Hoa sen** nở ở ngọc.
5. **Khung giữ tinh thần cũ, kéo dài 6 tick cho đường bay dài hơn:** F0 đòn ở Trận Tâm, F1–F2 hai đĩa F1 (đĩa đất hoặc đĩa trời), F3–F48 hai đầu rồng bay, F30–F56 đuôi quét quạ, F49–F56 nhịp gầm, F57–F77 hoa sen, vệt cháy trúng tới F102, hình tới F300.
6. **Luật sát thương giữ nguyên máy:** 3 loại đòn, 15/45/40 %, mỗi thú tối đa 3 đòn cách nhau ≥ 20 tick, mỗi bên một thang giảm dần và một ngân sách, cả lần tung là một đòn vùng (trần cụm 60 %), trần Vương 1,5 W, một thứ tự đánh mỗi tick. Đổi hai chỗ: bên của thú theo §9.3 (thay theo cổng), và "khoảng cách tới Trận Tâm" trong thứ tự đánh nay là đường chim bay, không theo trường dòng chảy. F1 thêm đĩa trời cho quạ (loại hành lang, phần trời).
7. **Ngân sách 2,0 W mỗi bên cộng 0,8 W trời** (anh duyệt 04/11, khoảng 19:40, §9.11): ô 2 là ngoại lệ có tên, chiếm ≤ 45 % sát thương cả trận lúc này; sau phần 2 của SKILL_REACH xuống ≤ 35 %, rồi thử 20 %. Bot quét lại 1,25–3,75 W mỗi bên để kiểm.

### 9.1 Cách làm và kết quả duyệt

**Đường đã dùng: ChatGPT bốn lượt, không lượt nào đạt hai PASS liên tiếp; Gemini không với tới; Claude tự phân tích và các giám khảo Claude độc lập duyệt** (luật bước 9 của `agent-orchestration`, anh thêm lúc 14:00).

| Lượt | Đề bài | Kết quả các lần tự duyệt | Vì sao dừng |
|---|---|---|---|
| ChatGPT 1 | Thiết kế mở, đủ cả sát thương | FAIL, FAIL, FAIL | Mỗi lần tự sửa lại thêm luật ngân sách mới (trần mỗi thú, ngân sách để dành), rồi lần sau thấy lỗi trong chính luật đó. Dừng theo luật 4 lượt |
| ChatGPT 2 | Chỉ hình học, luật sát thương cố định | FAIL, FAIL, FAIL | Lưới mật độ, lưới quét và chèn điểm rẻ nhất sinh lỗi biên mới mỗi lượt; đề ra trần đường dài 3 × đường chéo sân (143 m) |
| ChatGPT 3 | Sửa một bản đơn giản do Claude viết | FAIL, **PASS**, FAIL | Lượt 3 thấy hai lỗi thật (quạ chạm ở F1 phải là đòn hành lang lấy ngân sách trời; mục tiêu F1 phải nhận được sát thương dương). Đã sửa |
| ChatGPT 4 | Bản hội tụ của lượt 3 cộng ba sửa của Claude | Chưa có câu trả lời | Anh dừng mọi việc lúc 14:02; 14:06 chatgpt.com và gemini.google.com đều đã đăng xuất. Không đăng nhập |
| Gemini | Duyệt bản đã qua của ChatGPT | Không chạy | 4 Argon hết hạn mức tới 13:23; sau đó trình duyệt đăng xuất |
| Claude | Phân tích, nguyên mẫu hình học (`proto.py`, ngoài Git), viết §9 | Giám khảo Claude độc lập (mỗi lần một agent mới): FAIL, FAIL, PASS, PASS | Hai PASS liên tiếp ở lần 3 và 4 |

Bản ghi nguyên văn và bảng kiểm: [`source/dragon-fieldwide-chatgpt-2026-11-04.md`](source/dragon-fieldwide-chatgpt-2026-11-04.md), [`source/dragon-fieldwide-gemini-2026-11-04.md`](source/dragon-fieldwide-gemini-2026-11-04.md), [`source/dragon-fieldwide-critics-2026-11-04.md`](source/dragon-fieldwide-critics-2026-11-04.md).

**Bài học cho các lượt sau:** đề bài "thiết kế mở, đủ chi tiết để code theo" làm ChatGPT tự sinh máy móc mới và tự đánh trượt nó mãi. Đưa nó một bản đơn giản để sửa thì hội tụ sau 3 lượt.

### 9.2 Đầu vào và ảnh chụp F0

Đọc một lần ở F0, trước đòn F0:
- khung sân `stage.field` (minX, maxX, minZ, maxZ);
- Trận Tâm H (hôm nay là gốc tọa độ) và C = `cast.origin`;
- mọi thú `alive && !damageImmune`: serial, slot, x, z, y. Thú đất là thú ở dải đất (≤ 1,5 m), thú trời là thú ở dải trời (2,5–6 m).

Bản ghi của lần tung lưu (toàn số nguyên) H, F, R, `cut2`, P, bên của từng con, các cặp [slot, serial] của ảnh chụp và hình học dựng ra (nút, mẫu, `pass`, neo trời); vị trí F0 của thú chỉ dùng lúc dựng (công cụ đo tự ghi lại khi cần gọi `staticCoverage`). Sau F0 thú vẫn đi như thường; mọi khối trúng thử vị trí thật ở tick đang chạy. Chỉ hình học là cố định từ F0.

**Sân trống:** trong trận và trong lab, chiêu chỉ giải khi có thú nhận được sát thương, nên hình dạng sân trống chỉ gặp khi gọi thẳng hàm dựng hình học (test, công cụ): ngọc ở H + 9 m theo F, mỗi rồng bay một "vòng cánh" (§9.4); không có đòn.

### 9.3 Chia hai rồng

```text
F = unitPm(H − C);  if F = 0: F = unitPm(fieldCentre − H);  if F = 0: F = (0, −1000)
R = (−F.z, F.x)
v(p) = mulDivSym((p − H) · R, 1, 1000)        // ngang
u(p) = mulDivSym((p − H) · F, 1, 1000)        // dọc
sắp ảnh chụp (thú đất và trời chung) theo (v, u, serial) tăng dần
ceil(n/2) con đầu: bên 0; còn lại: bên 1
cut2 = v(con cuối bên 0) + v(con đầu bên 1)   khi n ≥ 2;   2·v(con duy nhất) khi n = 1;   0 khi n = 0
```

- **Thú không có trong ảnh chụp** (sinh sau F0, hay Vương vừa hết gầm): lấy bên ở lần đầu nó được xét đòn trong lần tung (`hit()` gọi `sideFor`, đúng chỗ hộp xám gọi `sideOf` hôm nay; kể cả khi phần ngân sách đã cạn): `2v < cut2` là bên 0, `2v > cut2` là bên 1, bằng nhau thì `serial % 2`. Đã có bên thì giữ tới hết lần tung.
- Hôm nay C = (0; 3), H = (0; 0): F = (0; −1000), R = (1000; 0), nên v = x: rồng 0 bên tây, rồng 1 bên đông, như hộp xám cũ, nhưng không cần biết cổng.

### 9.4 Ngọc, điểm neo và đường bay

**Ngọc P:**
```text
G = trung bình vị trí thú đất trong ảnh chụp (không có thú đất: mọi thú trong ảnh chụp)   // mulDivSym(tổng, 1, n)
P = H + mulDivSym(G − H, 600, 1000)                     // 3/5 đường
nếu |P − H| > 12 m: P = H + mulDivSym(P − H, 12 m, |P − H|)
kẹp P vào sân thu 2 m mỗi phía (trục ngắn hơn 4 m: lấy điểm giữa)
ảnh chụp rỗng: P = kẹp(H + 9 m · F / 1000)
```

**Điểm neo của mỗi bên** (chỉ thú đất của bên đó, tối đa 3):
```text
neo 1 = con xa H nhất (dist2; hòa: serial nhỏ)
neo k+1 = con chưa chọn có min dist2 tới {C, P, các neo đã chọn} lớn nhất (hòa: serial nhỏ)
dừng khi đủ 3, hoặc min dist2 lớn nhất < (3 m)²
```

**Đường của mỗi rồng:**
```text
có neo: thử mọi thứ tự neo (tối đa 6, sinh theo thứ tự từ điển của chỉ số chọn: [0,1,2], [0,2,1], [1,0,2], …),
        độ dài = Σ isqrt(dist2) của C → neo… → P; giữ thứ tự đầu tiên ngắn hơn hẳn
không neo: C → W → P, W = kẹp(H ∓ (mulDivSym(R.x, 9 m, 1000); mulDivSym(R.z, 9 m, 1000))): dấu − cho bên 0, + cho bên 1   // "vòng cánh"
bỏ nút trùng nút ngay trước; đoạn dài hơn 32 m chia đều thành ceil(L / 32 m) đoạn
không có trần độ dài, không bỏ neo vì đường dài
```

**Mẫu và thân** (dùng lại `sPath` của hộp xám, thêm tham số bước và làm tròn đối xứng, §9.12 B.4):
```text
step = max(0,5 m, ceil(tổng độ dài các đoạn nút / 256))     // tối đa 257 + số đoạn mẫu mỗi rồng, kể cả trên sân rất lớn
mẫu = sPath(nút, firstSide = +1 cho bên 0, −1 cho bên 1, step)   // biên độ 0,9 m, nửa sóng ≈ 4 m như hôm nay
kẹp từng mẫu vào khung sân; tính lại cung arc bằng isqrt trên các mẫu đã kẹp
pass[i] = 3 + mulDiv(arc[i], 45, arcTổng)   (arcTổng = 0: mọi pass = 3)       // đầu rồng F3 → F48
thân: đĩa r 1,4 m quanh mỗi mẫu i có pass[i] ≤ t ≤ pass[i] + 54, dải đất; loại hành lang, phần hành lang
đầu rồng ở tick t: mẫu cuối có pass ≤ min(t, 48)
```

- **Vì sao chia đoạn 32 m:** `mulDiv` chỉ đúng khi 2·a·b + c < 2^53 (`src/sim/fixed.ts`). Trong `sPath`, `mulDiv(4000·r, len − r, len²)` vượt ngưỡng đó khi một đoạn dài hơn khoảng 35 m.
- **Vì sao 45 tick thay 39:** đường hộp xám dựng thật dài khoảng 18–20 m (điểm gặp → cổng), đầu rồng bay khoảng 31 m/s theo sóng S; đường nút mới dài 2,2–2,5 lần (44–45 m trên sân hôm nay; theo sóng S thì 49–50 m). Kéo 6 tick giữ cao trào gần như cũ (hoa sen F57 thay F51); đầu rồng khoảng 67 m/s theo sóng S, anh xem trong lab (§9.11).
- **Vì sao bỏ trần độ dài:** neo đầu tiên là con xa nhất, nên trên sân hôm nay đường đã dài 44–45 m. Trần 36 m sẽ bỏ hết neo và rồng không bao giờ tới dòng thú xa (nguyên mẫu đã thử). Số mẫu có trần nhờ bước tự giãn.

### 9.5 Năm pha và khung (60 Hz, Fn = tick F0 + n)

| Pha | Khung | Khối trúng (sim) | Hình (view, không trúng) |
|---|---|---|---|
| Gồng | trong lúc gõ | — | Như §3 A: vòng lửa quanh kiếm theo từng chữ đúng, hạt ngọc sáng dần trên chuôi |
| Phóng (ở người ra chiêu) | F0 | Đĩa đất r 4,5 m quanh H (64 m², bằng hộp 8 × 8 m cũ). Loại chạm, phần chạm | Lóe kiếm đạt đỉnh ngay khung đầu, vòng sáng ở Trận Tâm |
| Phóng | F1–F2 | Mỗi bên một đĩa r 2,2 m, tâm cố định ở vị trí F1 của mục tiêu: con của bên đó gần H nhất (đường chim bay; hòa: serial nhỏ) trong ảnh chụp, còn sống, nhận được sát thương, chưa nhận loại đòn đĩa sẽ gây, và nhận được sát thương dương (phần ngân sách của nó còn, Vương còn dưới trần, cụm bầy còn dưới trần 60 %). Thú đất: đĩa đất, loại chạm, phần chạm. Thú trời: đĩa trời, loại hành lang, phần trời. Không có con hợp lệ: bên đó không có đĩa | Hai đầu rồng bật ra hai bên lưỡi; hai sợi sáng mảnh từ kiếm tới hai đĩa |
| Bay | F3–F48 | Thân và vệt của hai rồng (§9.4) | Hai rồng tách đôi, bay qua các neo theo đường S; ngọc bay thẳng từ kiếm tới P, tới nơi ở F48 |
| Bay | F30–F56 | Mỗi bên, trong dải trời: một "con nhộng" r 3 m (trên mặt x–z) từ đầu rồng của bên đó tới từng neo trời của bên đó (vị trí F0 của quạ trong ảnh chụp), và đĩa trời r 3 m quanh mỗi mẫu thân đang sống. Loại hành lang, phần trời | Đuôi rồng quất lên từng con quạ |
| Trúng | F49–F56 | Không khối mới (vệt và quét trời vẫn trúng) | Nhịp gầm: hai đầu đã kề ngọc (tới P ở F48), ngẩng lên, há hàm |
| Trúng | F57–F77 | Hoa sen ở P, dải đất. **Đầy** trong đĩa (P, 4 m), đĩa (H, 4,5 m), hoặc trong 2,2 m quanh 13 m mẫu cuối của mỗi đường (đo ngược từ P theo cung; đường ngắn hơn thì cả đường) — hai "cánh dài", có thể vươn ra ngoài 9 m như §3 A. **Nửa** ở phần còn lại trong r 9 m quanh P. Loại hoa sen, phần hoa sen | F57 hai hàm khép vào ngọc, hoa sen lửa nở; khựng đòn 50 ms |
| Dư âm | F78–F102 | Chỉ còn vệt thân (mẫu cuối qua lúc F48, cháy tới F102) | Hoa sen giữ đỉnh tới F86 (29 tick sau khi nở, như §3 A), rồi vệt và dấu bắt đầu nguội bằng ăn mòn |
| Dư âm | F103–F300 | Không | Tiếp tục nguội bằng ăn mòn: trắng vàng, son, than; tàn lửa và sao lấp lánh thưa dần |

- **Đòn đầu:** có thú hợp lệ ở F0 thì đòn dương đầu tiên ở F0 hoặc F1 (≤ 17 ms). Trường hợp luật cố định chặn mọi đòn dương (ví dụ thú bầy 1 máu, trần cụm làm tròn xuống 0, §8.2) được ghi lại, không tính là trúng.
- **Thời gian trúng của quạ:** quạ bay 2 m/s, tới F56 cách điểm neo F0 tối đa 1,9 m; quạ Cuồng ở mức Thử thách bay 2,73 m/s, tối đa 2,6 m. Con nhộng r 3 m giữ cả hai.
- **Tick gồng không đổi** (chỉ trong lúc gõ); không bao giờ chờ sau F0.

### 9.6 Khối trúng, trần và ngân sách

| Mục | Số | Ghi chú |
|---|---|---|
| Dải đất / dải trời | 0–1,5 m / 2,5–6 m | Như hộp xám. Thú ở giữa hai dải (1,5–2,5 m) không bị khối nào trúng |
| Loại và phần | chạm 15 %, hành lang 45 %, hoa sen 40 % của 2,5 W × hệ số giảm dần của bên; hoa sen nửa: 50 % | Không đổi |
| Mỗi thú mỗi lần tung | tối đa 3 đòn, mỗi loại 1, cách nhau ≥ 20 tick | Không đổi (`mayHit`) |
| Thang giảm dần | mỗi bên riêng: 100 %, −15 % mỗi con khác tiếp theo, sàn 40 % | Không đổi; "bên" nay là bên của §9.3 |
| Ngân sách mỗi bên | 2,0 W đất (chạm / hành lang / hoa sen 15/45/40) + 0,8 W trời, × M_q × bucket | Anh duyệt (§9.11); hộp xám cũ dùng 2,5 W. Quét lại ở §9.8 |
| Trần cụm bầy | cả lần tung là một đòn vùng: tối đa 60 % máu cụm | Không đổi |
| Trần Vương | 1,5 W mỗi mã lần tung | Không đổi |
| Thứ tự đánh mỗi tick | loại (chạm, hành lang, hoa sen), rồi dist2 tới H, rồi serial | **Đổi:** dist2 đường chim bay thay `heartDistance` (theo trường dòng chảy) |
| Thân rồng | r 1,4 m, vệt 54 tick | Không đổi |
| Đĩa F0 / đĩa F1 | r 4,5 m / r 2,2 m | Mới |
| Quét trời | r 3 m, F30–F56 | Đổi từ "góc trời → Trận Tâm" sang "đầu rồng → neo trời" |
| Hoa sen | r 9 m, lõi 4 m, cánh rộng 4,4 m dài 13 m, F57–F77 | Tâm ở ngọc, cánh theo đường của chính rồng |

### 9.7 Thử trên bảy bố cục (nguyên mẫu hình học, số thực, ngoài Git)

`proto.py` dựng §9.3–9.4 bằng số thực trên các bố cục tổng hợp dưới đây, C = (0; 3), H = (0; 0): bên, ngọc và độ dài đường nút lấy từ nó; tốc đầu rồng tính theo cung của các mẫu sóng S (`sample()` của nó) chia 0,75 s (dòng in mặc định của script là độ dài đường nút chia 0,75 s). Cột "Trong tầm" lấy từ bản cổng số nguyên của giám khảo thiết kế (ngoài Git), có đủ cánh hoa sen, đĩa F1 và `sPath` nối dấu qua các đoạn: đó là phần thú ảnh chụp nằm trong ít nhất một khối trúng đúng dải ở bất kỳ tick nào, khi thú đứng yên (chưa tính ngân sách). Số con thật bị trúng do ngân sách quyết định (§8.6: khoảng 15 con ở 2,0 W mỗi bên, 17 con ở 2,5 W).

| Bố cục | Thú (đất + trời) | Hai bên | Ngọc | Đường nút rồng 0 / 1 (trước sóng S) | Tốc đầu rồng (theo cung sóng S, 45 tick) | Trong tầm |
|---|---|---|---|---|---|---|
| Hai cổng (hôm nay) | 38 + 2 | 20 / 20 | (0; −5,9) | 45,1 / 43,9 m: từ người chơi ra giữa dòng thú, lên tới cổng, rồi chéo về ngọc | 67 / 66 m/s | 40/40 |
| Một cổng (giữa mép trên) | 38 + 2 | 20 / 20 | (0; −6,2) | 32,0 / 31,9 m: hai rồng chạy hai nửa của cùng một dòng | 48 / 49 m/s | 40/40 |
| Ba cổng (mép trái, giữa mép trên, mép phải) | 39 + 3 | 21 / 21 | (0; −3,4) | 59,0 / 55,7 m: ra dòng bên, tới mép sân, vòng sang dòng giữa, về ngọc | 90 / 83 m/s | 42/42 |
| Đấu trường 40 × 40 m, thú tám hướng | 40 + 4 | 22 / 22 | (0; 0) | 56,9 / 68,8 m: mỗi rồng quét nửa vòng | 85 / 103 m/s | 35/44 |
| Chỉ sau lưng người chơi | 38 + 2 | 20 / 20 | (−0,3; 3,3) | 38,0 / 38,3 m | 57 / 58 m/s | 36/40 |
| Một thú đất | 1 | 1 / 0 | (0; −7,2) | 19,8 m / vòng cánh 21,0 m | 30 / 31 m/s | 1/1 |
| Một con quạ | 0 + 1 | 1 / 0 | (−6,0; −7,2) | vòng cánh 17,3 / 26,1 m; quạ trúng ở F1 qua đĩa trời | 25 / 38 m/s | 1/1 |
| Sân trống | 0 | 0 / 0 | (0; −9) | hai vòng cánh 22,2 m | 33 m/s | — |

Đọc bảng:
- Mọi bố cục có từ 35 thú trở lên đều có ≥ 79 % thú trong tầm (đấu trường 79,5 %), nên đích 12–20 con là việc của ngân sách, không phải của hình học.
- Đường dài nhất (đấu trường) cho đầu rồng 103 m/s. Đây là chỗ cần anh xem trong lab (§9.11).
- Bố cục một cổng: hai rồng chồng lên nhau trên một dòng. Chấp nhận được (mỗi rồng một nửa dòng, ngân sách riêng); thêm luật tách đường sẽ làm thuật toán phức tạp lại như ChatGPT lượt 2.

### 9.8 Đích đo và kế hoạch bot

**Đích** (quét đỉnh của §8.1, cùng bộ thế giới, 35–45 thú, ngân sách 2,0 W mỗi bên):

| Chỉ số | Định nghĩa | Đích |
|---|---|---|
| Thú khác nhau bị trúng | con nhận ≥ 1 đòn dương của lần tung | trung vị trong 12–20 và ≥ 70 % lần tung trong 12–20; báo thêm p10–p90 |
| **Trong tầm tĩnh** (`coverageStatic`, đo mới, không phụ thuộc map) | đóng băng thú ở vị trí F0, phát lại mọi khối F0–F102 (đĩa F1 lấy từ bản ghi lần tung sau t = 1, như `staticCoverage` ở §9.12 B.6), bỏ qua máu, ngân sách, trần và khoảng trúng lại; phần thú ảnh chụp nằm trong ≥ 1 khối đúng dải | trung vị ≥ 75 %; báo riêng đất và trời |
| Cân hai bên | số thú ảnh chụp hai bên lệch ≤ 1 (do dựng); sát thương hiệu dụng bên 0 / bên 1 khi mỗi bên có ≥ 5 thú trong ảnh chụp F0 | 40/60–60/40 ở ≥ 85 % lần tung |
| Đòn đầu | tick từ F0 tới đòn dương đầu tiên | F0 hoặc F1 ở mọi lần tung có thú hợp lệ; muộn hơn F2 dưới 0,1 % trong trận thật |
| Quạ | quạ ảnh chụp nhận đòn dương | ≥ 90 % |
| Tầm xa | trung vị đòn xa nhất tới H mỗi bên; phần thú > 12 m bị trúng | báo cáo, so với §8.2 |
| Phần theo loại đòn | như §8.3 | báo cáo |
| BALANCE.md | Thắng, S, P, I, O, N, Q, phần gõ, ô 1/gõ, ô 2/cả trận, đánh nền, phút, thua ở đợt; 17 hồ sơ × 20 seed | như §8.4, cột "hai hành lang" để so. Ô 2/cả trận ở bot Chuẩn ≤ 45 % (anh duyệt, §9.11) |
| Quét ngân sách | 1,25 / 1,75 / 2,0 / 2,5 / 3,75 W mỗi bên, trời 0,8 W | bảng như §8.6 |
| Hiệu năng | thời gian dựng hình học ở F0; µs mỗi tick mỗi lần tung, 60 thú | ≤ 0,2 ms; ≤ 50 µs |

**Bố cục tổng hợp** (cho test và cho một lệnh "quét bố cục" mới của bot). Đơn vị m, đổi sang u bằng `mToU` rồi làm tròn; thú đất y = 0, quạ y = 4 (`FIELD.flyHeightMm`); loài: Phong Lang cho thú đất, Hỏa Nha cho quạ; serial theo thứ tự tạo:

```text
stream(a, b, n):  k = 0…n−1, t = k/(n−1):  x = a.x + (b.x − a.x)·t + 0,5·((k mod 3) − 1),  z = a.z + (b.z − a.z)·t
hai cổng:   stream((−15; −17,5), (−1,8; −2,2), 19) + stream((15; −17,5), (1,8; −2,2), 19) + quạ (−19; −17), (19; −17)
một cổng:   k = 0…37: x = 0,6·((k mod 5) − 2), z = −17,5 + 15·floor(k/5)/7; quạ (−1,5; −16), (1,5; −16)
ba cổng:    stream((−19,5; −6), (−2,2; −1), 13) + stream((0; −17,5), (0; −2,2), 13) + stream((19,5; −6), (2,2; −1), 13) + quạ (−19; −17), (0; −17), (19; −17)
đấu trường: sân tổng hợp x, z ∈ [−20; 20]; theo đúng thứ tự hướng (1; 0), (−1; 0), (0; 1), (0; −1), (0,7; 0,7), (−0,7; 0,7), (0,7; −0,7), (−0,7; −0,7), mỗi hướng bán kính 5, 8, 11, 14, 17; rồi quạ (15; 0), (−15; 0), (0; 15), (0; −15)
sau lưng:   k = 0…37: x = −18 + 3·(k mod 13), z = 4 + 1,5·floor(k/13); quạ (−17; 7), (17; 7)
một thú:    Phong Lang ở (0; −12)          một quạ: Hỏa Nha ở (−10; −12)          sân trống: không thú
```

**Bot** (ngoài Git, `games/immortality-cultivation/tmp/skill-reach/`):
1. `key2-measure.ts`: bỏ phủ theo hành lang (`coverA`, `coverB`, `reachW/E` theo cổng), thay bằng `coverageStatic`, cân hai bên theo bên của lần tung, tầm xa theo bên.
2. Chạy lại ma trận và quét đỉnh của §8.10 với biến thể mới (`@twin-pearl` nay là bản toàn sân) và các mức quét ngân sách. Giữ số "hai hành lang" của §8 làm cột so.
3. Lệnh mới `key2-layouts.ts`: dựng từng bố cục trên, tung một lần với thú đứng yên (chỉ bước kỹ năng), in số con bị trúng, `coverageStatic`, đòn đầu, chia hai bên, độ dài đường và tốc đầu rồng.
4. Lab: Claude quay một video ở camera chơi cho anh xem (hai cổng và một bố cục khác), lưu ở `typing-game-review/captures/tu-tien/twin-pearl-fieldwide/` theo `review-folder`.

### 9.9 Hình (VFX): hệ quả, chưa làm art

Hai rồng vẫn là "đầu + thân + vệt" chạy dọc một đường đã tính sẵn, nên mọi lớp hình của §3 A còn dùng được: đầu có xương, 20–30 % thân trước có vảy, phần sau là dải lửa Firefly (`aura-fire-ribbon`, `aura-fire-flame-sheath`), ngọc, hoa sen, dấu cháy vẽ tay. Khác ở chỗ đường nay đổi mỗi lần tung, đường nút dài 17–70 m và đầu rồng bay 25–103 m/s, nên view cần từ sim: P, các nút đường và mẫu của từng rồng với `pass`, hai đĩa F1, các neo trời, khung pha (F0, F1, F3, F30, F49, F57, F77, F102) và nhịp vệt. View uốn dải thân theo các mẫu (đường cong trong texture dữ liệu như Gemini đề xuất ở §4), không tự tính đường. Đầu rồng theo hướng anh đã chọn, A · Solar Ember Regent (§9.11). Hình làm theo `game-vfx-production` (art trước, mã chỉ đặt và hoạt hình), sau khi anh duyệt bản hộp xám mới; vệt quá nhanh trên các đường dài nhất (cung S 63–77 m, đầu rồng 85–103 m/s) là rủi ro chính về đọc hình.

### 9.10 Ai góp gì, Claude không đồng ý ở đâu

**ChatGPT góp** (các lượt đều chưa qua, nên chỉ là ý tham khảo, Claude đã tự kiểm):
- Chia hai bên theo tọa độ ngang quanh trục người chơi → Trận Tâm, lấy trung vị, `cut2` cho thú đến sau (lượt 2). Dùng.
- Ảnh chụp một lần ở F0; quét trời bằng con nhộng từ đầu rồng tới neo trời (lượt 2). Dùng.
- Ngọc ở 3/5 đường tới tâm khối thú, kẹp 12 m và mép sân (lượt 2). Dùng.
- Đo `coverageStatic`, test gương và xoay với dung sai 0 (lượt 3). Dùng.
- Quạ được chạm ở F1 nhận đòn hành lang từ phần trời; mục tiêu F1 phải nhận được sát thương dương (lượt 3, lần duyệt 3). Dùng.
- Bỏ trần độ dài đường (lượt 3). Dùng; nguyên mẫu xác nhận trần 36 m làm mất neo.

**Claude không đồng ý với ChatGPT:**
- Lưới mật độ, lưới quét, chèn điểm rẻ nhất và trần 143 m (lượt 2): quá phức tạp và chính chúng làm các lần duyệt trượt.
- Trần mỗi thú và ngân sách để dành (lượt 1): trái luật sát thương cố định.
- "Ngân sách 2,0 W không bảo đảm đòn F1" (lượt 3): sai. Một đòn lấy `min(sát thương, phần còn lại)`, nên vẫn dương khi phần còn > 0. Khi viết, Claude giữ 2,5 W để so với §8; sau đó anh duyệt 2,0 W (§9.11).
- Cắt cánh hoa sen trong đĩa 9 m (lượt 3): giữ cánh dài 13 m như §3 A.
- "Nửa sóng đầu của mỗi đoạn luôn dương" (lượt 3): giữ đúng `sPath` đã có test (dấu nối tiếp qua các đoạn).
- Thứ tự đánh vẫn theo `heartDistance` (cả ba lượt ngầm giữ): đổi sang đường chim bay, vì `heartDistance` đọc trường dòng chảy của cổng.

**Claude thêm:** bước mẫu tự giãn (≤ 256 mẫu), chia đoạn 32 m để `mulDiv` không vượt 2^53, 45 tick bay, vòng cánh cho bên không có thú đất, nguyên mẫu `proto.py` cho bảng §9.7. Giám khảo lần 1 thêm: làm tròn đối xứng trong `sPath` (ảnh gương trùng tới 0 u), origin (0; 3) trong mọi test bố cục, con nhộng trời r 3 m cho quạ Cuồng, bước chuẩn bị cây Codex.

**Gemini:** không góp lượt này (§9.1).

**Giám khảo Claude độc lập:** bốn lần, mỗi lần một agent mới chưa viết bản này: FAIL, FAIL, PASS, PASS. Mọi lỗi của hai lần FAIL đã sửa (bản ghi nguyên văn và bảng kiểm: [`source/dragon-fieldwide-critics-2026-11-04.md`](source/dragon-fieldwide-critics-2026-11-04.md)).

### 9.11 Quyết định của anh (04/11/2026, khoảng 19:40)

Claude hỏi ba điều; anh chốt cả ba. Mục này thay câu 1 của §8.8.

1. **Phần sát thương của ô 2: duyệt đề xuất của Claude, ngoại lệ có tên cho chiêu biểu tượng này.**
   - Lúc này: ô 2 ≤ 45 % sát thương cả trận, ngân sách 2,0 W mỗi bên (§8.6 đo được 37–45 % ở 2,0 W khi tầm các chiêu khác chưa sửa; bot Mới → Nhanh thắng 45–100 %).
   - Sau phần 2 của SKILL_REACH (tầm ô 1, đánh nền, ô 4 và tuyệt kỹ; đo lại D_ref vì đợt đang tính theo 75 W/phút mà bot Chuẩn chỉ ra 43): ô 2 ≤ 35 %, đo lại; rồi thử về 20 % nếu tầm các chiêu khác cho phép.
   - Vì sao không giữ ngay 20 % của canon §7.3: hộp xám cũ chiếm 41–50 %, và quét §8.6 cho thấy không ngân sách nào về ≤ 20 % mà bot còn thắng; với ô 2 hôm nay (đường thẳng, 18–26 % sát thương) bot chỉ thắng 0–40 %, vì tầm mọi chiêu khác quá ngắn (SKILL_REACH).
   - Bot của phiếu 2 dùng các số này làm đích (§9.12 F).
2. **Tiếng hô bằng tiếng Anh,** theo luật chữ của game, ví dụ "Twin Dragons — Seize the Pearl!". Thay câu tiếng Trung gợi ý ở §3 A. Mọi chữ người chơi thấy trong các phiếu đều bằng tiếng Anh.
3. **Đầu rồng: hướng A, Solar Ember Regent** (đỏ vàng hoàng gia, sừng vàng, vòng hào quang, ngọc trong móng). Art làm ở bước riêng sau, theo `game-vfx-production` và `game-character-design`; không nằm trong các phiếu ở §9.12.

**Giữ mặc định, anh đổi được:** câu 2 của §8.8 vẫn đúng ở dạng không phụ thuộc map: ngân sách đánh theo thứ tự tới trước, nên lúc đông sát thương dừng gần Trận Tâm dù rồng vẫn bay tới thú xa nhất. Claude giữ đề xuất ở §8.8 (thú gần nguy hơn), đo bằng chỉ số "Tầm xa" ở §9.8.

**Anh xem khi có video lab (không phải quyết định bây giờ):** đầu rồng bay khoảng 67 m/s trên sân hôm nay và tới khoảng 103 m/s trên đường dài nhất (đấu trường). Nếu anh thấy quá nhanh, chỉ cần đổi số trong bảng: `heads.toTick` cùng `roar`, `sky.toTick`, `lotus` và `pearl.arriveTick` lùi theo (ví dụ đầu rồng bay 60 tick, hoa sen lùi tới F72).

### 9.12 Ticket Codex: lời giải đầy đủ

**Thợ:** Codex `gpt-6.1-sol`, effort `xhigh` (code và logic), một lane, **hai phiếu nối nhau**: phiếu 1 là A–E (nội dung, sim, lab, test); phiếu 2 là F (bot và số đo), giao sau khi Claude đã duyệt và merge phiếu 1. Sandbox `workspace-write`, thư mục làm việc là cây riêng `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-twin-fieldwide` trên nhánh `codex/twin-pearl-fieldwide` (không dùng `games/.wt-immortality-cultivation-codex`: cây đó đang giữ việc chưa duyệt của phiếu 258 và đã được phiếu 259 đặt chỗ). Mọi đường dẫn dưới đây tính từ thư mục đó. Báo cáo của Codex là tin nhắn cuối (`run.sh` lưu ở `.local/codex-runs/<id>/last.md`); Claude chép nó vào `docs/codex-queue/` của repo cha. Codex không commit; Claude chạy lại kiểm tra, đọc diff, rồi mới merge.

**Claude chuẩn bị trước khi giao** (Codex không tự làm):
1. `git -C /Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation worktree add ../.wt-ic-twin-fieldwide -b codex/twin-pearl-fieldwide main`, rồi `ln -s ../immortality-cultivation/node_modules /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-twin-fieldwide/node_modules` (liên kết như phiếu 255). Phiếu 2 dùng lại đúng cây và nhánh này sau khi Claude đã merge phiếu 1 (cây vẫn giữ bản chép `tmp/skill-reach/` của bước 2). Vì liên kết đó, mọi lệnh test và build ở E.1 dùng đúng dạng của báo cáo 255 (không ghi gì vào `node_modules` của cây chính).
2. Chép `tmp/skill-reach/` của cây chính vào cây mới (bot nhập `../../src/...` theo thư mục của chính nó, nên phải chạy bản trong cây mới).
3. Golden cờ tắt để so nằm ở đường tuyệt đối `/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/tmp/shots/dragon/greybox/golden-before/`.
4. Ghi hai phiếu ở `docs/codex-queue/` của repo cha. **Phiếu 1** `<n>-tt-twin-pearl-fieldwide.md`: dòng đầu "Thiết kế, chỉ đọc: `/Volumes/SS990TPRO/htdocs/typing-game/docs/games/tu-tien/skills/DRAGON_SKILL.md` §9.0–§9.11; mọi §9.x trong phiếu là của file này", rồi phần đầu §9.12 và A–E. **Phiếu 2** `<n+1>-tt-twin-pearl-fieldwide-bot.md`: cùng dòng đầu, phần đầu §9.12, B.1, B.3, B.6, dòng "Sân tổng hợp cho test" của D, và F. Trước khi chạy phiếu 2: `git -C /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-twin-fieldwide merge --ff-only main` để cây có đúng bản phiếu 1 đã merge. Chạy lần lượt (phiếu 2 sau khi phiếu 1 đã merge): `tools/codex-run/run.sh <n>-tt-twin-pearl-fieldwide docs/codex-queue/<n>-tt-twin-pearl-fieldwide.md games/.wt-ic-twin-fieldwide xhigh workspace-write`, và tương tự cho phiếu 2.

**Được ghi:**
- `src/content/data/twin-pearl.ts` (chỉ phiếu 1)
- `src/sim/twin-pearl.ts` (chỉ phiếu 1)
- `src/sim/combat.ts` (chỉ thêm một hàm xuất, §B.7; chỉ phiếu 1)
- `tests/sim/twin-pearl.test.ts` (chỉ phiếu 1)
- `src/lab/twin-pearl-greybox.ts`, `src/lab/skills-main.ts` (chỉ phần hộp xám; chỉ phiếu 1)
- `tmp/skill-reach/**` (ngoài Git; chỉ phiếu 2)
- thư mục build tạm `/private/tmp/codex-twin-fieldwide-dist` (xóa sau khi kiểm; chỉ phiếu 1)

**Chữ:** mọi chữ người chơi thấy, và mọi nhãn mới trong lab, bằng tiếng Anh (luật chữ của game; §9.11).

**Luật chung của `run.sh`** cấm chạy build và bộ test của game và cấm sửa `src`, `tests`: phiếu này ghi đè luật đó, chỉ trong cây của Codex và chỉ cho các file ở danh sách "Được ghi" và các lệnh ở E và F.

**Cấm:**
- sửa canon, `rules.ts`, `school-kiem.ts`, `field.ts`, `spawn.ts`, `src/kit/**`, game khác;
- đổi bất kỳ hành vi nào khi cờ tắt;
- đổi `hit()`, `mayHit()`, `falloffPm()`, `postureOf()`, `twinPearlPool()` ngoài phần ghi ở dưới;
- số thực trong trạng thái sim; mở cổng mạng; commit.

#### A. Nội dung: `src/content/data/twin-pearl.ts`

Đổi `pool.sideW100` từ 250 thành **200** (2,0 W mỗi bên, anh duyệt, §9.11); `pool.skyW100` giữ 80. Giữ `SwordKey2`, `SWORD_KEY2_VARIANTS`, `id`, `name`, `sharesPct`, `maxHits`, `rehitTicks`, `bossCapW100`, `trailTicks`, `groundTopMm`. Thay phần hình học:

```ts
hold:   { tick: 0, radiusMm: 4500 },                       // F0 ground disc round the formation centre
touch:  { fromTick: 1, toTick: 2, radiusMm: 2200 },        // F1–F2 one disc per side, centre fixed at F1
pearl:  { pullPm: 600, maxMm: 12_000, insetMm: 2000, emptyMm: 9000, fromTick: 3, arriveTick: 48 },
anchors:{ max: 3, minGapMm: 3000 },
wingMm: 9000,
heads:  { fromTick: 3, toTick: 48, radiusMm: 1400, amplitudeMm: 900, halfWaveMm: 4000, sampleMm: 500, maxSamples: 256, maxSegmentMm: 32_000 },
sky:    { fromTick: 30, toTick: 56, radiusMm: 3000, bottomMm: 2500, topMm: 6000 },
roar:   { fromTick: 49, toTick: 56 },                      // view only
lotus:  { fromTick: 57, toTick: 77, radiusMm: 9000, coreMm: 4000, petalLengthMm: 13_000, petalHalfWidthMm: 2200, outsidePm: 500 },
```

Bỏ `meetFallbackMm` và hộp `hold.halfWidthMm/depthMm`, `touch.halfLengthMm/halfWidthMm`, `heads` cũ, `sky` cũ, `lotus` cũ. `TWIN_PEARL_END_TICK` vẫn là `max(heads.toTick + trailTicks, lotus.toTick, sky.toTick)` = 102. Sửa lời chú thích đầu file theo §9 (không còn hành lang hay cổng). `rulesHash` tự phủ bảng mới vì `matchRulesHash` đã đẩy `TWIN_PEARL` khi có cờ: không sửa `app.ts`.

#### B. Sim: `src/sim/twin-pearl.ts`

**B.1 Bỏ:** `TwinLane`, `TwinGeometry`, `TwinTouch`, `geometryCache`, `laneRoute`, `lastBend`, `buildLane`, `twinPearlGeometry`, `inHold` (hộp), `inTouch` (hộp), `routeDirection`, `pickTouches`, các hằng mô-đun đọc trường đã bỏ (`HOLD_HALF`, `HOLD_DEPTH`, `TOUCH_HALF_LEN`, `TOUCH_HALF_W`), `skyFront`, `inSky`, `inPetal` và `lotusRegion` bản theo hành lang, `sideOf` theo cổng.

**B.2 Giữ nguyên:** `TwinKind`, `KIND_BIT`, `KIND_ORDER`, các `POOL_*`, `TwinVictim`, `createTwinPearlState`, `swordKey2Of`, `falloffPm`, `postureOf`, `twinPearlPool`, `bookOf`, `mayHit`, `hit` (trừ dòng lấy bên, B.5), `stepTwinPearl`, phần `declare module`.

**B.3 Bản ghi lần tung** (`TwinPearlCast`, thêm, toàn số nguyên; giữ mọi trường cũ trừ `touch`):

```ts
readonly hx: number; readonly hz: number;            // H (u)
readonly fx: number; readonly fz: number;            // F (‰)
readonly rx: number; readonly rz: number;            // R (‰)
readonly cut2: number;
readonly px: number; readonly pz: number;            // the pearl P (u)
readonly sideSlot: number[];                         // by beast slot: 0 none, 1 side 0, 2 side 1 (grow with push(0), like bookAt: no holes)
readonly sideSerial: number[];                       // by beast slot: the serial the side belongs to
readonly dragons: readonly [TwinDragon, TwinDragon];
readonly disc: [TwinDisc, TwinDisc];                 // F1 discs, set at t = 1
readonly snapshot: number[];                         // [slot, serial] pairs of the F0 snapshot (F1 targets come only from it)

interface TwinDragon {
  readonly nodes: number[];                          // control points x0, z0, x1, z1 … (C, anchors…, P) after merging duplicates (before the long-segment split)
  readonly sx: number[]; readonly sz: number[];      // samples (u), clamped into the field
  readonly arc: number[];                            // cumulative arc on the clamped samples (u)
  readonly pass: number[];                           // tick offset the head passes each sample (3…48)
  readonly petalFrom: number;                        // first sample index with arc[last] − arc[i] ≤ petalLength
  readonly sky: number[];                            // sky anchors x, z … (this side's snapshot flyers at F0)
}
interface TwinDisc { on: number; x: number; z: number; sky: number }   // sky: 0 ground disc, 1 sky disc
```

**B.4 Dựng hình học ở F0** (xuất `buildCastGeometry(world, cast)` cho test và bot; gọi trong `resolveTwinPearl` trước khi đẩy bản ghi; trả các trường B.3):
1. **Ảnh chụp:** duyệt `world.beasts.list` theo thứ tự mảng: `alive && !damageImmune(world, beast)`.
2. **Trục và bên:**
   - F, R theo §9.3, cộng `+ 0` vào mỗi thành phần để không có −0 (ví dụ R = (−F.z + 0, F.x + 0)); "fieldCentre" = (mulDivSym(minX + maxX, 1, 2); mulDivSym(minZ + maxZ, 1, 2)) của `world.stage.field` đổi sang u.
   - Sắp bằng so sánh (v, u, serial). Ghi `sideSlot` và `sideSerial` cho từng con.
   - `cut2` như §9.3.
3. **Ngọc:** §9.4. Độ dài |P − H| = `isqrt(dist2)`. Kẹp: x vào [minX + inset; maxX − inset], nếu minX + inset > maxX − inset thì x = mulDivSym(minX + maxX, 1, 2); z tương tự.
4. **Neo:** §9.4, so bằng `dist2` (số nguyên, không căn).
5. **Thứ tự:**
   - Sinh hoán vị theo thứ tự từ điển; độ dài = Σ `isqrt(dist2)`; giữ hoán vị đầu tiên có độ dài nhỏ hơn hẳn.
   - Không neo: nút C, W, P (W kẹp như P).
   - Bỏ nút trùng nút trước. Lưu các nút này vào `nodes` (việc chia đoạn dài nằm trong `sampleRoute`, bước 6).
6. **Mẫu** (xuất `sampleRoute(nodes, sideSign, field)` trả `{ sx, sz, arc, pass, step }`, và `splitLong(nodes, maxSegU): number[]`; cả hai dùng cho test 4):
   - `sampleRoute` gọi `splitLong` trước: mỗi đoạn A → B dài L > `maxSegmentMm` thành k = ceil(L / maxSeg) đoạn, nút chèn ở A + mulDivSym(B − A, j, k), j = 1…k−1.
   - `sPath(nodes, side 0 ? +1 : −1, step)`: thêm tham số `step` (u) vào `sPath` hiện có, và đổi hai dòng độ lệch thành `x = bx + mulDivSym(-unit.z * off, 1, 1000)`, `z = bz + mulDivSym(unit.x * off, 1, 1000)` (làm tròn đối xứng theo dấu của tích, để ảnh gương trùng tới 0 u; bản cũ lệch 1 u ở các tích tận cùng …500). Không đổi gì khác.
   - `step = max(U(sampleMm), ceil(Σ độ dài đoạn / maxSamples))`.
   - Kẹp từng mẫu vào khung sân. Tính lại `arc`.
   - `pass[i] = heads.fromTick + mulDiv(arc[i], heads.toTick − heads.fromTick, arcTổng)` (arcTổng = 0: mọi `pass = fromTick`).
   - Nếu chỉ có 1 nút: một mẫu ở C, `arc = [0]`, `pass = [3]`.
7. **Cánh hoa sen:** `petalFrom` = chỉ số nhỏ nhất i có arc[last] − arc[i] ≤ petalLength.
8. **Neo trời:** các con ảnh chụp ở dải trời, theo bên của chúng, thứ tự ảnh chụp.

**H** là `heartPoint()` (gốc tọa độ hôm nay); không có trường nào khác giữ nó.

**B.5 Bên của thú khi vào sổ** (thay `sideOf(beast)` trong `hit()`): `sideFor(cast, beast)`:
- `sideSlot[slot] ≠ 0` và `sideSerial[slot] = serial`: lấy bên đã lưu.
- Ngược lại: v = mulDivSym((x − hx)·rx + (z − hz)·rz, 1, 1000); bên 0 nếu 2v < cut2, bên 1 nếu 2v > cut2, ngược lại `serial % 2`. Ghi lại vào `sideSlot` và `sideSerial`.

**B.6 Khối trúng** (hàm thuần, xuất ra cho test, lab và bot):
- `inHoldDisc(cast, x, z)`: `within(x, z, hx, hz, hold.r)`.
- `inDisc(disc, x, z)`: `disc.on && within(x, z, disc.x, disc.z, touch.r)`.
- `liveSamples(dragon, t, out)`: như hôm nay, trên `dragon.pass`.
- `inSpan(dragon, first, last, x, z, r)`: thêm tham số bán kính.
- `headIndex(dragon, t)`: mẫu cuối có `pass ≤ min(t, heads.toTick)`.
- `inSkyReach(cast, x, z, t)`: t ∈ [30; 56] và có ít nhất một rồng thỏa một trong hai:
  - `distSegment2(x, z, head, anchor) ≤ (3 m)²` với một neo trời của rồng đó;
  - `inSpan(dragon, span, 3 m)`.
- `distSegment2`: chiếu nguyên như `inPetal` cũ. `along` dùng `floor(dot / len)` và kẹp vào [0; len]; điểm gần nhất bằng `mulDivSym`. Đoạn dài 0 (đầu rồng trùng neo): khoảng cách tới điểm đó.
- `inBody(dragon, x, z, t)`: viết lại trên `liveSamples` và `inSpan` với r 1,4 m. `inGroundBand`, `inSkyBand` giữ nguyên.
- `staticCoverage(cast, points)`: nhận vị trí F0 của các thú ảnh chụp (x, z, y), trả số con nằm trong ít nhất một khối đúng dải ở một tick nào đó F0–F102, bỏ qua máu, ngân sách, trần và khoảng trúng lại; đĩa F1 lấy từ bản ghi (sau t = 1). Dùng cho test và bot.
- `lotusRegion(cast, x, z)`:
  - 2 (đầy) nếu một trong các điều: `within(P, coreMm)`, `inHoldDisc`, hoặc trong `petalHalfWidth` của một đoạn [k; k+1] với k ≥ max(0, petalFrom − 1) của một rồng (đoạn đầu có thể vươn quá 13 m tối đa một bước mẫu: chấp nhận);
  - 1 (nửa) nếu không đầy nhưng `within(P, radiusMm)`;
  - 0 nếu không.
- `volumesAt(cast, x, y, z, t)`: bit như hôm nay (1 đĩa F0, 2 đĩa F1 đất hay trời theo dải của đĩa, 4 thân, 8 trời F30–F56, 16 hoa sen đầy, 32 hoa sen nửa), nay nhận `cast` thay `geo`.

**B.7 Đĩa F1** (`pickDiscs(world, cast)` ở t = 1):
- Với mỗi bên s, duyệt các cặp của `snapshot` có bên s; lấy con bằng `beastByRef(world, { slot, serial })` (`src/sim/combat.ts`; thêm `beastByRef` vào dòng import từ `./combat`), bỏ cặp trả `null` (đã chết hoặc slot đã dùng lại).
- Một con hợp lệ khi:
  - sống, `!damageImmune`;
  - ở dải đất (loại chạm, phần chạm) hoặc dải trời (loại hành lang, phần trời);
  - `mayHit(cast, beast, loại, 1)`;
  - `cast.pool[s·4 + phần] > 0`;
  - không phải Vương, hoặc `bossDealt < bossCap`;
  - nếu thuộc cụm bầy: `areaClusterLeft(world, cast.area, cluster) > 0`.
- Chọn con hợp lệ có dist2 tới H nhỏ nhất (hòa: serial nhỏ). Đặt `disc[s] = { on: 1, x, z, sky }` theo dải của nó.
- **`combat.ts`:** xuất thêm `areaClusterLeft(world, area, cluster)`. Nó trả `area.left[at]` nếu cụm đã có, ngược lại `floor(hp cụm × clusterCapPct / 100)`, **không** đẩy vào `area` (cùng công thức `clusterLeft`). Không đổi gì khác.

**B.8 Mỗi tick** (`stepCast`, thay phần gom ứng viên; giữ cách gom một lượt rồi sắp):
```text
geo đọc từ cast; t = world.tick − startTick
t = 1: pickDiscs
với mỗi thú sống, !damageImmune:
  g = inGroundBand(y), s = inSkyBand(y)
  nếu g và ((t = 0 và inHoldDisc) hoặc (1 ≤ t ≤ 2 và một đĩa F1 đất chứa nó)) và mayHit(chạm)      → chạm, POOL_TOUCH
  ngược lại nếu s và 1 ≤ t ≤ 2 và một đĩa F1 trời chứa nó và mayHit(hành lang)                       → hành lang, POOL_SKY
  ngược lại nếu g và thân một rồng đang sống chứa nó (r 1,4 m) và mayHit(hành lang)                   → hành lang, POOL_CORRIDOR
  ngược lại nếu s và inSkyReach và mayHit(hành lang)                                                   → hành lang, POOL_SKY
  ngược lại nếu g và 57 ≤ t ≤ 77 và lotusRegion ≠ 0 và mayHit(hoa sen)                                 → hoa sen, POOL_LOTUS, nửa nếu vùng = 1
  d = dist2(x, z, hx, hz)                                                                              // thay heartDistance
sắp (KIND_ORDER, d, serial); đánh lần lượt bằng hit() như hôm nay
```
Thoát sớm khi không khối nào sống ở tick t (như hôm nay). Bên của thú trong `hit()` lấy từ `sideFor` (B.5).

**B.9 `resolveTwinPearl`:** điều kiện giải không đổi (có thú nhận được sát thương). Gọi `buildCastGeometry` rồi đẩy bản ghi. Ngân sách vẫn từ `twinPearlPool`.

**Số khung trong mã:** mọi tick ở B.6–B.8 (1–2, 30–56, 48, 57–77, 102) đọc từ `TWIN_PEARL` (`touch`, `sky`, `heads`, `lotus`, `TWIN_PEARL_END_TICK`); không viết số tick trần trong mã, để đổi khung chỉ là đổi bảng (§9.11).

**B.10 Dọn chú thích đầu file** theo §9: không còn hành lang, cổng, góc trời, điểm gặp.

#### C. Lab: `src/lab/twin-pearl-greybox.ts`, `skills-main.ts`

- **Triều thú của lab** (bỏ mọi chỗ dùng `twinPearlGeometry`, `skyFront`, `TwinGeometry`, `along()` theo hành lang):
  - khi dựng lại (R) và lúc mở: đổ bố cục hai cổng của §9.8;
  - phím `L`: đổ bố cục kế tiếp: hai cổng, một cổng, ba cổng, vòng quanh (tám hướng × bán kính 5, 8, 11, 14, 17 m theo thứ tự §9.8, bỏ những điểm ngoài sân hôm nay), sau lưng; lab bỏ thêm những điểm rơi vào ô bị chặn (hai Trận Trụ, kể cả khoảng đệm), vì trong lab thú đi lại;
  - **bỏ hẳn** `refill()` và phần tự bơm cũ ở đầu mỗi `stepWorld()`; phím `N` đổ lại bố cục đang chọn;
  - thú đất đổ bằng `spawnBeast` với nhãn cổng "A" (nhãn không ảnh hưởng hình học); quạ luôn với nhãn "sky" ở y = 4 m;
  - phím `V` thả Vương ở `gatePoint(stage, "A")`;
  - thú đi như thường; bấm phím 2 ngay sau `L` hoặc `N` để tung lúc bố cục còn nguyên. Không sửa sim để giữ thú đứng yên.
- **Vẽ từ bản ghi lần tung đang sống:**
  - đĩa F0, hai đĩa F1 (đất hay trời) và hai sợi sáng từ kiếm;
  - nút và mẫu của hai rồng, đầu rồng ở `headIndex`, vệt theo `liveSamples`. Lưới instanced của thân đủ cho mọi mẫu: tối thiểu 320 thực thể mỗi rồng (`maxSamples` + 1 + số đoạn), hoặc vẽ từ `range.last` lùi về khi vượt;
  - con nhộng trời tới từng neo trời;
  - ngọc bay từ kiếm tới P trong F3–F48;
  - hoa sen: đĩa lõi, cánh và vòng 9 m.
- **Băng tên pha** theo khung mới. **Ô số:** tây/đông thay bằng bên 0 / bên 1 lấy từ `cast.book[].side`; thêm `coverageStatic` của lần tung: ghi vị trí F0 của các thú ảnh chụp ngay sau lệnh `stepWorld()` chạy F0 trong `cast()`, rồi tính một lần khi lần tung tới t ≥ 1 (không tính mỗi khung).
- Thêm `L` vào danh sách nút của bảng, như `N` và `V`.
- Không đổi gì khi không có `?key2=twin-pearl`.

#### D. Test: `tests/sim/twin-pearl.test.ts` (viết lại phần hình học; giữ phần luật sát thương)

Giữ, sửa cho khung mới:
- cờ tắt: header không có `swordKey2`, ô 2 vẫn là đường thẳng, **các băm ghim của `1a78a82` giữ nguyên**;
- `rulesHash` phủ bảng chỉ khi có cờ;
- 3 đòn mỗi thú, mỗi loại 1, cách ≥ 20 tick; phần 15/45/40;
- hệ số giảm dần mỗi bên, sàn 40 %; ngân sách mỗi bên và mỗi phần (nay 2,0 W mỗi bên chia 15/45/40, cộng 0,8 W trời), không phần nào vượt;
- một trần cụm cho cả lần tung; trần Vương theo mã lần tung; chia Thế 3/9/8;
- chỉ giải khi có thú nhận được sát thương; tất định và không số thực (`hashedFloats`).

Thêm (bố cục ở §9.8; thú đứng yên: chỉ gọi `stepSkills` qua `advance`, trừ khi test ghi khác; **mọi lần tung dùng `castOf(world, 2, { origin: at(0, 3) })`**, trừ phần kẹp của test 2 và C xoay của test 9, vì `castOf` mặc định đặt origin ở Trận Tâm):

| # | Test | Kiểm |
|---|---|---|
| 1 | Bên theo trục ngang | Hai cổng: 20/20, mọi con x < 0 bên 0. n = 0, 1, 2 cho đúng `cut2`. Thú đến sau theo `cut2`, hòa theo `serial % 2`, giữ bên tới hết lần tung |
| 2 | Ngọc | Hai cổng: P cách (0; −5,9) ≤ 0,15 m. Mười Phong Lang quanh (−15; −16) (tâm khối cách H khoảng 22 m): \|P − H\| = 12 m ± 2 u. Sân trống (gọi `buildCastGeometry` trực tiếp, origin (0; 3)): P = (0; −9). Kẹp mép: sân trống, `buildCastGeometry(world, castOf(world, 2, { origin: at(0, −3) }))` trên THANH_THACH_AI cho F = (0; 1000) và P = (0; 6 m) (9 m kẹp về maxZ − 2 m) |
| 3 | Neo và đường | Hai cổng: mỗi rồng 3 neo (5 nút: C, 3 neo, P); con xa H nhất của mỗi bên là một nút. Σ isqrt các đoạn nút (C → neo → P, trước sóng S) 45,1 / 43,9 m ± 1 m (nguyên mẫu); `arc` cuối 50,3 / 49,2 m ± 1 m. Đường bắt đầu ở C, kết thúc ở P. Một thú: rồng không có thú đất bay vòng cánh qua H ± 9 m·R |
| 4 | Mẫu | Mọi mẫu trong khung sân. `pass` không giảm, đầu 3, cuối 48. Số mẫu ≤ 257 + số đoạn (sau khi chia). `splitLong` biến một đoạn nút 40 m thành 2 đoạn, mỗi đoạn ≤ `maxSegmentMm` (u). Gọi thẳng `sampleRoute` với một danh sách nút dài ≥ 200 m (đường gấp khúc) trong khung 60 × 60 m (−30 000…30 000 mm): bước > 0,5 m và số mẫu ≤ 257 + số đoạn. (Không dựng world trên sân lớn hơn khoảng 64 × 63,5 m: `field.ts` từ chối từ 16 384 ô) |
| 5 | Đĩa F0 và F1 | Con trong r 4,5 m quanh H nhận chạm ở F0. Với `cast.pool.fill(10 ** 9)` ngay sau khi giải (như các test đám đông hiện có): mỗi bên, con gần H nhất ngoài đĩa F0 nhận chạm ở F1. Không bơm ngân sách, bố cục hai cổng **bỏ hai quạ**: bên có con bị chạm ở F0 đã cạn phần chạm, nên `disc[s].on === 0`. Cùng bố cục **có quạ**: đĩa của bên đó là đĩa trời ở quạ của bên đó (`disc[s].sky === 1`), quạ nhận hành lang từ phần trời ở F1. Con gần nhất bị trần cụm chặn (cụm 1 máu): bỏ qua, chọn con kế |
| 6 | Thân, trời, hoa sen theo khung | Chạy với `cast.pool.fill(10 ** 9)` sau khi giải, để quạ không là mục tiêu F1. Con trên đường rồng nhận hành lang khi đầu qua và tới 54 tick sau. Quạ không nằm trên đường nhận hành lang qua con nhộng, đúng ở F30 (nó nằm ở đầu con nhộng của chính nó). Thú đất dưới con nhộng không bị trời trúng. Hoa sen đầy trong lõi, đĩa H và cánh; nửa trong 9 m quanh P; không gì ngoài 9 m quanh P trừ cánh và đĩa H r 4,5 m. Không đòn nào sau F102 |
| 7 | Bảy bố cục | Mỗi bố cục có thú: đòn dương đầu tiên ở F0 hoặc F1. `coverageStatic` ≥ 95 % (hai cổng, ba cổng), ≥ 85 % (một cổng, sau lưng), ≥ 75 % (đấu trường). Số con bị trúng ≤ tổng con và mọi phần ngân sách ≥ 0. Sân trống: dựng hình học không lỗi, không đòn |
| 8 | Gương | Hai cổng lật x → −x, giữ serial; C = (0; 3) không đổi: bên 0 ↔ 1. Mọi đòn (serial, tick, loại, máu) trùng, dung sai 0. Nút, mẫu và `pass` là ảnh gương, dung sai 0 u |
| 9 | Xoay | Đấu trường trên sân 40 × 40 m, xoay 90° (x, z) → (−z + 0, x) (cộng `+ 0` để không có −0, như test gương hiện có), cả C: (0; 3) thành (−3; 0). Mọi đòn trùng, dung sai 0. Mẫu xoay đúng, dung sai 0 u |
| 10 | Không đọc cổng | Cùng vị trí, đổi nhãn cổng A ↔ B của mọi thú đất: mọi đòn trùng |
| 11 | Tất định | Hai lần chạy một seed, có thú di chuyển và hai lần tung chồng nhau: cùng băm mỗi tick. Bản ghi lần tung chỉ có số nguyên |
| 12 | Hiệu năng (khói) | 60 thú, hai lần tung chồng nhau, 102 tick, chạy nóng máy 3 lần trước: in thời gian dựng hình học và µs mỗi tick mỗi lần tung. Chỉ làm hỏng test khi trung vị vượt 4 lần đích (0,8 ms; 200 µs) |

**Sân tổng hợp cho test:** `{ ...THANH_THACH_AI, id: "test-arena", field: { ...THANH_THACH_AI.field, minXMm: −20_000, maxXMm: 20_000, minZMm: −20_000, maxZMm: 20_000, mechSlots: [], pillars: [] } }` qua `makeWorld({ stage })`. Kiểm trước rằng `createWorld` chạy được với nó; nếu không, dừng và ghi vào báo cáo, không sửa `field.ts`.

#### E. Kiểm của phiếu 1 (Codex chạy, Claude chạy lại)

1. `VITEST_MAX_THREADS=4 node node_modules/vitest/vitest.mjs run --no-cache --configLoader runner --maxWorkers 4` xanh, gồm test băm ghim cờ tắt `1a78a82`. `node node_modules/typescript/bin/tsc --noEmit -p .` xanh. Build không ghi vào cây: `IC_VITE_CACHE_DIR=/private/tmp/codex-twin-fieldwide-dist/.vite-cache node node_modules/vite/bin/vite.js build --outDir /private/tmp/codex-twin-fieldwide-dist --configLoader runner` xanh (như phiếu 255), rồi xóa thư mục đó. `node src/kit/verify-kit.mjs` xanh.
2. Hiệu năng (test 12, 60 thú, sau 3 lần chạy nóng máy): đạt nếu trung vị dựng hình học ≤ 0,2 ms và trung vị ≤ 50 µs mỗi tick mỗi lần tung; trượt thì báo số, không tối ưu bằng cách đổi luật.
3. Phiếu 1 không chạy bot: sau phiếu 1, các script ở `tmp/skill-reach/` còn nhập tên đã bỏ; phiếu 2 sửa chúng.
4. `grep -n "heartDistance" src/sim/twin-pearl.ts` không ra gì, kể cả trong chú thích (thứ tự đánh dùng `dist2` tới H, §9.6; đừng chép chú thích `// thay heartDistance` của B.8 vào mã).
5. **Báo cáo:** file đã đổi, kết quả từng lệnh, số của test 12, mọi chỗ làm khác phiếu và lý do.

#### F. Phiếu 2: bot và số đo (`tmp/skill-reach/`, ngoài Git)

**Phạm vi:** phiếu 2 chỉ ghi `tmp/skill-reach/**`; không sửa `src/`, `tests/` hay số trong `src/content/data/twin-pearl.ts`. Cần đổi sim thì dừng và ghi vào báo cáo. Sim là bản phiếu 1 đã merge (B.1, B.3, B.6 và sân tổng hợp của D có trong phiếu này).

**Cách chạy mọi script** (CLI `tsx` bị sandbox chặn với `listen EPERM`, như phiếu 195, 223): `TSX_DISABLE_CACHE=1 node --import=tsx tmp/skill-reach/<script>.ts …`. Thay hai chỗ `node_modules/.bin/tsx` trong `key2-matrix.sh` bằng đúng dạng đó. Mọi kết quả mới ghi vào `tmp/skill-reach/key2-fieldwide/`; không ghi vào `key2/`, `key2-fix/`, `key2-review/` (đó là nguồn của các cột so ở §8).

**Sửa script:**
1. `key2-measure.ts` (theo §9.8 bot bước 1):
   - bỏ phủ theo hành lang (`laneRoutes`, `coverage()`, `coverA/B`) và mọi chỗ nhập hay gọi các tên đã bỏ ở B.1: `TwinLane`, `TwinGeometry`, `TwinTouch`, `laneRoute`, `twinPearlGeometry`, `inHold`, `inTouch`, `skyFront`, `inSky`, `inPetal`, `sideOf`; `lotusRegion` nay nhận `cast` (B.6);
   - trận "line" (cờ tắt) cũng bỏ `coverA/B`, không thay, và giữ mọi trường cũ khác (cả `reachW/E`);
   - trận có cờ, mỗi lần tung, ghi thêm:
     - số thú ảnh chụp mỗi bên, tách đất và trời (đếm `snapshot` theo `sideSlot` và dải độ cao); số quạ mỗi bên;
     - vị trí F0 (x, z, y) của các thú ảnh chụp lúc tung; khi lần tung đã qua t = 1 (sau tick có `pickDiscs`), gọi `staticCoverage` một lần, tách đất và trời; mẫu số của số chung là mọi thú ảnh chụp, kể cả thú ở giữa hai dải;
     - số con bị trúng và sát thương mỗi bên, theo `cast.book[].side`;
     - tầm xa mỗi bên: đòn hiệu dụng xa nhất lên thú ở dải đất (≤ 1,5 m) tới H, như §8.1; và số thú đất ảnh chụp ở xa H hơn 12 m, số trong đó bị trúng;
     - phần theo loại đòn (đĩa F0, đĩa F1 đất, đĩa F1 trời, thân, trời, hoa sen đầy, hoa sen nửa): sát thương, số đòn, số con hạ;
     - `firstHit` (tick từ F0 tới đòn dương đầu tiên; −1 nếu không có) và, khi −1, lý do (trần cụm, Vương chạm trần, ngân sách cạn, khác);
   - sau bước này `key2-measure.ts` không còn nhập tên nào đã bỏ.
2. `key2-numbers.ts`: bỏ biến thể "narrow" (nó ghi vào các trường đã bỏ `touch.halfWidthMm`, `hold.halfWidthMm`). `+pool<N>` giữ nguyên (đổi `pool.sideW100` thành N trong bộ nhớ).
3. `key2-aggregate.ts`, cho nhóm 35–45 và in như §8.2–8.6:
   - nhóm "35–45 thú" theo **thú đất trong ảnh chụp** (như §8.2; nhóm này quyết định đạt/trượt), in thêm nhóm theo mọi thú trong ảnh chụp để tham khảo;
   - số con bị trúng (trung vị, p10–p90, phần lần tung trong 12–20), `coverageStatic` (chung, đất, trời);
   - cân hai bên: chỉ tính lần tung mà mỗi bên có ≥ 5 thú trong ảnh chụp F0;
   - quạ bị trúng, in riêng cho các lần tung có ≥ 2 quạ ở cùng một bên (đĩa F1 có thể tiêu hết ngân sách trời của bên đó cho con quạ đầu);
   - tầm xa: trung vị đòn xa nhất mỗi bên, phần thú đất > 12 m bị trúng (như §8.2);
   - phần theo loại đòn: % sát thương, đòn và hạ mỗi lần tung (như §8.3);
   - đòn đầu trong trận thật: số lần tung, số lần `firstHit > 2`, và danh sách riêng các lần `firstHit = −1` kèm lý do.
4. `key2-layouts.ts` mới (theo §9.8 bot bước 3):
   - dựng từng bố cục của §9.8 theo đúng thứ tự tạo; đấu trường trên sân tổng hợp `{ ...THANH_THACH_AI, id: "test-arena", field: { ...THANH_THACH_AI.field, minXMm: −20_000, maxXMm: 20_000, minZMm: −20_000, maxZMm: 20_000, mechSlots: [], pillars: [] } }`; thế giới có cờ dựng như `twinWorld` trong `tests/sim/twin-pearl.test.ts`;
   - tung một lần với origin (0; 3), chỉ bước kỹ năng; sân trống gọi thẳng `buildCastGeometry`;
   - in: hai bên, P, độ dài đường nút, cung cuối, tốc đầu rồng (cung cuối chia (`heads.toTick` − `heads.fromTick`) / 60 s), `coverageStatic`, số con bị trúng, đòn đầu, chia hai bên.
5. Một script so cờ tắt nhỏ trong `tmp/skill-reach/` (kiểm 1 dưới đây).

**Lệnh** (từ thư mục làm việc):
```text
# cờ tắt: 9 hồ sơ × seed 1–4
mkdir -p tmp/skill-reach/key2-fieldwide/golden-now
for p in w30a97 w45a97 w60a97 w80a97 w45a90 standard novice fast no-type; do
  BOT_HASHES=1 TSX_DISABLE_CACHE=1 node --import=tsx tmp/skill-reach/bot.ts tmp/skill-reach/key2-fieldwide/golden-now $p 1 4 > tmp/skill-reach/key2-fieldwide/golden-now/$p.log 2>&1
done
# bố cục
TSX_DISABLE_CACHE=1 node --import=tsx tmp/skill-reach/key2-layouts.ts > tmp/skill-reach/key2-fieldwide/layouts.txt
# ma trận và quét đỉnh: 2,0 W (mặc định mới) và các mức quét
KEY2_OUT=tmp/skill-reach/key2-fieldwide bash tmp/skill-reach/key2-matrix.sh twin-pearl twin-pearl+pool125 twin-pearl+pool175 twin-pearl+pool250 twin-pearl+pool375
KEY2_ROOT=tmp/skill-reach/key2-fieldwide KEY2_VARIANTS="twin-pearl twin-pearl+pool125 twin-pearl+pool175 twin-pearl+pool250 twin-pearl+pool375" TSX_DISABLE_CACHE=1 node --import=tsx tmp/skill-reach/key2-aggregate.ts > tmp/skill-reach/key2-fieldwide/aggregate.txt
```
Cột so "hai hành lang" (2,0 W là `twin-pearl+pool200`, 2,5 W là `twin-pearl`) và "hôm nay" lấy từ `tmp/skill-reach/key2-fix/numbers.json` (bản chép ở bước chuẩn bị) và các bảng §8; không chạy lại biến thể "line" (cờ tắt không đổi).

**Kiểm và số phải đạt:**
1. **Cờ tắt:** với mỗi file JSON trong `/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/tmp/shots/dragon/greybox/golden-before/`, mọi trường có trong đó, ở mọi tầng (cả trong `waves[]`), bằng hệt trường cùng đường dẫn ở file cùng tên trong `golden-now`; bỏ qua khóa chỉ có ở `golden-now` (như `key2*`, `pace`, `lanePeak*`) và file `.log`, như §8.1. In số file khớp (đích 36/36).
2. **Bố cục:** `layouts.txt` khớp bảng §9.7 trong ± 1 m (độ dài các đoạn nút) và ± 1 con (trong tầm).
3. **Quét đỉnh, biến thể `twin-pearl` (2,0 W mỗi bên), nhóm 35–45 thú đất:**
   - số con bị trúng: trung vị trong 12–20 và ≥ 70 % lần tung trong 12–20 (in thêm p10–p90);
   - `coverageStatic` trung vị ≥ 75 %;
   - đòn đầu F0 hoặc F1;
   - quạ ≥ 90 % (in riêng nhóm ≥ 2 quạ một bên);
   - cân hai bên 40/60–60/40 ở ≥ 85 % lần tung đủ điều kiện.
4. **Trận thật, biến thể `twin-pearl`, mọi lần tung:** số lần `firstHit > 2` < 0,1 % số lần có đòn dương; các lần `firstHit = −1` đếm và liệt kê riêng kèm lý do, không gộp vào tỉ lệ này.
5. **Phần của ô 2 (anh duyệt, §9.11):** ô 2/cả trận ở bot Chuẩn ≤ 45 % với `twin-pearl` (2,0 W). In ô 2/cả trận của mọi bot.
6. **Báo cáo** (không có ngưỡng): ma trận 17 hồ sơ × 20 seed và quét ngân sách 1,25 / 1,75 / 2,0 / 2,5 / 3,75 W, bảng như §8.2–8.6 (tầm, phần theo loại đòn, BALANCE.md, cổng bot, quét) với cột "hai hành lang" để so.
7. Nếu một ngưỡng ở 1–5 trượt: ghi số và các lần tung trượt vào báo cáo; không đổi số trong `data/twin-pearl.ts` hay luật §9 để cho khớp.

#### G. Sau hai phiếu (việc của Claude)

- Duyệt diff và chạy lại E (phiếu 1) và các lệnh, phép kiểm của F (phiếu 2). Không commit liên kết `node_modules` của cây (nó hiện là file chưa theo dõi).
- Sau khi duyệt phiếu 2: kiểm bản `tmp/skill-reach/` của cây chính chưa đổi kể từ bước chuẩn bị 2, rồi chép các script đã sửa (`key2-measure.ts`, `key2-numbers.ts`, `key2-aggregate.ts`, `key2-matrix.sh`, `key2-layouts.ts`, script so cờ tắt) và thư mục `key2-fieldwide/` về `games/immortality-cultivation/tmp/skill-reach/`; chạy thử một trận từ cây chính (`TSX_DISABLE_CACHE=1 node --import=tsx tmp/skill-reach/bot.ts <thư mục tạm> w45a97@twin-pearl 1 1`) trước khi gỡ cây. §9.13 ghi lệnh tái lập chạy từ cây chính.
- Quay video lab (hai cổng và một bố cục khác) ở `typing-game-review/captures/tu-tien/twin-pearl-fieldwide/`, gửi anh.
- Ghi số đo vào một §9.13 mới của tài liệu này.
- Hỏi anh câu §9.11 với số mới.
- Âm thanh của §3 A dời theo khung mới khi làm âm: lặng ở F49, hai tiếng gầm ở F53, chuông lớn ở F57. Tiếng hô bằng tiếng Anh (§9.11), ví dụ "Twin Dragons — Seize the Pearl!".
- Viết changelog `games/immortality-cultivation/docs/changelog/<ngày>-twin-pearl-fieldwide.md` (mục nào làm, số đo, những gì chưa làm).
