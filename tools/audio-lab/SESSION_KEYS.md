# Tiếng phím · phiên nghe `keys-1` (5 bàn phím, 29/10/2026)

Năm hồ sơ tiếng phím để người chơi chọn trong Settings: **Creamy, Thock, Clicky, Soft Dome, Classic Spring**. Mỗi hồ sơ có 10 tiếng phím (`key-01…key-10`) và 3 tiếng phím cách (`space-01…space-03`). Tất cả làm trong Audio Lab bằng Stable Audio 3 Small-SFX trên máy này: không gói tải về, không âm tổng hợp bằng mã.

Không có gì ở đây đã vào game. Tai anh là cổng cuối; theo `docs/games/SHARED_SYSTEMS_BAR.md` hệ này còn cần hai giám khảo độc lập chấm từ 9.

## Mở

```bash
bash tools/audio-lab/run.sh board --game keys --open      # hoặc: pnpm audio:board --game keys
```

Trang mở ở `http://127.0.0.1:3191` (bận thì 3192). Chọn phiên **`keys-1`**. Khoảng 15 phút. Nghe bằng **tai nghe**, giữ âm lượng máy cố định.

## Phiên có gì

Sáu mục:

| Mục | Nghe gì |
|---|---|
| `keys.creamy` … `keys.spring` (5 mục) | Mỗi bản là **một bộ 13 file** của bàn phím đó. Máy đưa bộ đứng đầu và bộ khác nhất; Soft Dome và Classic Spring có thêm một bộ dò lấy từ nửa dưới. Thock chỉ có một bộ (không bộ thứ hai nào đủ khác mà vẫn qua cổng): chấm sao, hoặc `0` nếu chưa đạt. Anh không biết bản nào là bản nào |
| `keys.compare` | Năm bàn phím cạnh nhau (bộ máy xếp đầu, câu gõ 60 WPM). Chấm sao cho từng bàn phím, ghi chú nếu hai bàn phím nghe giống nhau |

Bối cảnh của mỗi mục (phím `↑` `↓`):

| Bối cảnh | Là gì |
|---|---|
| **Gõ 60 WPM** (mở đầu) | Câu "the quick brown fox jumps over the lazy dog" gõ bằng bộ đó, đúng cách kit `typing-fx` sẽ phát: lấy biến thể theo vòng xáo trộn, không lặp liền, ±3 % tốc độ phát, ±8 % mức, phím 0,55, phím cách 0,6. Mọi bộ gõ cùng một nhịp: chỉ tiếng khác. Không cân độ to, nên bộ nào to hơn sẽ nghe ra |
| **Gõ 100 WPM** | Như trên, nhanh hơn |
| **Lặp 20 lần** | Bài mỏi tai: 20 lần, cách ~200 ms, ±50 cent, ±0,7 dB, không lặp hai bản gần nhất |
| **Một mình** | 13 file lần lượt: 10 phím rồi 3 phím cách |
| **Loa nhỏ** | Như "Một mình", lọc cao 200 Hz |

## Chấm

- `⇧1`…`⇧5`: sao cho bộ đang chọn. `V`: bộ tốt nhất. `0`: **không bộ nào đạt**.
- Nhãn hay dùng: `R` rè/lỗi (tiếng "AI", nhòe, xì), `S` sai chất liệu (không giống bàn phím đó), `E` rẻ tiền, `P` nhàm khi lặp, `C` chói, `D` đục, `M` chậm (phím phát trễ), `K` quá dài, `H` hay.
- `/` ghi chú (gõ tiếng Việt được), `Enter` lưu. Thẻ số đo của máy chỉ hiện sau khi chấm.
- Xin anh ghi một điểm 0–10 cho mỗi bàn phím trong ghi chú (mức 9 là "ngang bàn phím cao cấp thật, muốn bật").

## Sau khi anh chấm

```bash
bash tools/audio-lab/run.sh keys stage --from-ratings     # đưa bộ anh chọn vào staging; hồ sơ "không bộ nào đạt" bị rút ra
```

Staging: `~/AudioLab/review/staging/keys/<hồ sơ>/` (`key-01.ogg … space-03.ogg`, `keys-manifest.json`, đúng chỗ kit đọc: `<base>/<id>/keys-manifest.json`), chỉ mục chung `~/AudioLab/review/staging/keys/keys-manifest.json`, master WAV và `SOURCES.json`, `licences.jsonl` ở `~/AudioLab/review/staging/keys/_art-src/<hồ sơ>/`. Hiện staging giữ bộ máy xếp đầu, trạng thái "candidate".

## Máy đã làm gì

| Hồ sơ | Nguồn bộ đầu | Ứng viên | Qua cổng (phím / cách) | Bộ đầu: audiobox PQ, khớp hồ sơ | Dài phím / cách |
|---|---|---|---|---|---|
| Creamy | đoạn gõ 10 s, prompt A (3 đoạn) | 81 bản tạo → 113 cú gõ | 38 / 13 | 7,43 · 0,90 | 116–180 / 213–225 ms |
| Thock | đoạn gõ A, B và cú đơn C (5 bản) | 81 → 91 | 26 / 28 | 7,80 · 0,81 | 129–180 / 90–258 ms |
| Clicky | đoạn gõ B (3 đoạn) | 108 → 182 | 49 / 24 | 7,77 · 0,94 | 112–148 / 127–258 ms |
| Soft Dome | đoạn gõ A, E (vòng 2) | 135 → 141 | 34 / 34 | 7,27 · 0,81 | 125–180 / 97–100 ms |
| Classic Spring | cú đơn C (10 bản) | 81 → 85 | 29 / 15 | 7,10 · 0,91 | 101–131 / 227–230 ms |

- **Tạo:** Stable Audio 3 Small-SFX, mỗi hồ sơ 4 prompt (A, B: đoạn gõ 10 s; C, D: một cú gõ 1 s), seed 101–124 cho cú đơn, 101–103 cho đoạn gõ. Vòng 2 (prompt E, F) cho Soft Dome và phím cách Clicky, vì vòng 1 ra tiếng phím cách Topre đục như tiếng thụp (98 % năng lượng dưới 800 Hz) và phím cách Clicky thiếu tiếng click. Prompt ở `keys/specs/<hồ sơ>.yaml`, đã qua lọc chữ cấm Q2, Q6.
- **Cắt cú gõ** (`keys/strokes.py`): mỗi cú là tiếng nhấn và tiếng nhả của chính nó; trước đó phải lặng, cách phím khác ít nhất 150 ms; bắt đầu 1 ms trước đầu tiếng (đầu tiếng ≤ 2 ms). Cú dài quá 180 ms (phím cách 260 ms) thì rút ngắn khoảng lặng giữa nhấn và nhả (thời gian giữ phím), không cắt tiếng.
- **Tai AI:** L1 (chặn), L1b, L2, L3 audiobox, L4 CLAP và AST, thẻ ảnh mù; rồi chọn bộ (`keys/pick.py`): cổng L1, lỗi mô hình L1b (xì, xoáy pha, nền nhiễu, rung cao độ, vạch lược) bị loại, đáy phím nhòe (> 6 ms) bị loại, tiếng chính đến muộn (> 15 ms) bị loại; điểm Q = khớp hồ sơ 0,35 + audiobox 0,25 + AST "Typing/Computer keyboard" 0,20 + điểm tổng của bộ chấm 0,20, trừ cờ L1b. Bộ 10 phím phải đều theo khoảng P10–P90 của 26 họ Kenney Impact (khoảng cách mel 0–50 ms, không bản sinh đôi, không bản lạc).
- **Độ to:** mọi file của cả năm hồ sơ về **−27 LUFS-M max** chỉ bằng tăng giảm mức (không nén), đỉnh thật ≤ −1,45 dBTP; OGG giải mã lệch tối đa 0,4 dB. Câu gõ 60 WPM của năm hồ sơ cùng −25,1 LUFS-I: đổi hồ sơ không nhảy âm lượng.
- **Định dạng:** master WAV 48 kHz 24-bit mono, bản chạy OGG Vorbis 48 kHz mono chất lượng 0,6 (5–9 KB mỗi file).

## Chỗ lệch kế hoạch (cần anh duyệt)

| Chỗ | Kế hoạch | Ở đây | Vì sao |
|---|---|---|---|
| Thời gian lên 10–90 % (§4.3.1) | Phím ≤ 3 ms | ≤ 10 ms | Phím ≤ 3 ms viết cho tiếng tick làm bằng mã. Cú gõ thật là ngón chạm keycap rồi mới chạm đáy: Creamy vòng 1 trung vị 5,5 ms, chỉ 3/113 cú dưới 3 ms. Đầu tiếng vẫn ≤ 2 ms; tiếng chính phải tới trong 15 ms; cú lên nhanh được xếp cao hơn |
| Mức chung (§4.3.3) | −20 LUFS-M max | −27 LUFS-M max | Cú gõ có crest 20–28 dB: chỉ bằng tăng mức, trung vị chỉ tới −25…−27 trước khi chạm −1 dBTP. Nén để lên −20 sẽ làm mềm tiếng click. Khi ghép vào game, mức phím của kit (0,55) có lẽ phải nâng; làn typing-feedback chỉnh |

## Máy nghi ngờ gì

- Tiếng do mô hình tạo có đáy phím mềm hơn bản thu thật: dải trên 2 kHz lên mất trung vị 3,5–4,5 ms (cổng loại trên 6 ms). Đây là lý do lớn nhất có thể làm hồ sơ chưa tới 9.
- Classic Spring: 10 cú đơn rất giống nhau (lệch trọng tâm phổ 78 cent, dưới P10 của Kenney): có thể "nhàm khi lặp".
- Thock: bộ đầu ghép 3 prompt (5 bản tạo), kém đều hơn các hồ sơ khác.
- Soft Dome: phím cách vẫn yếu (khớp hồ sơ 0,57); một file của bộ đầu bị cờ L1b "xì cao tần" khi kiểm lại master.
- Không có bản thu bàn phím thật nào trên máy để nghe mù xen kẽ. Đã gửi người điều phối danh sách bản thu CC0 thật (Freesound, Wikimedia Commons; `docs/games/THIRD_PARTY.md`), chờ anh đồng ý tải từng gói.

## Nếu anh chê một hồ sơ

1. Có bản thu CC0 thật được duyệt: cắt cú gõ bằng chính `keys/strokes.py`, chấm và chọn như trên, đưa vào phiên `keys-2` cạnh bản Audio Lab (nghe mù).
2. Không có: thêm prompt "slow typing, one key at a time" (đoạn 10 s, 12 seed) để có thêm cú gõ cùng một bàn phím, tối đa 3 vòng prompt (§5.5).
3. "Rè/lỗi", "nhòe": siết cổng đáy phím (≤ 3 ms) và loại mọi cờ L1b; "chói": hạ 3 dB ở 2,5–5 kHz; "đục": lọc cao 80–120 Hz (§5.4).
4. Sau 3 vòng vẫn chưa được: hồ sơ đó chỉ còn đường bản thu thật (CC0 hoặc anh tự thu bàn phím của anh), không phát hành ở mức 8.

## Lệnh

```bash
R="bash tools/audio-lab/run.sh keys"
$R generate --prompts C,D --seeds 101-124 --run r1      # rồi --prompts A,B --seeds 101-103
$R slice --run r1 --force
$R critic --run r1                                     # một mô hình nặng mỗi lúc (chờ làn khác)
$R pick --runs r1,r2
$R master [--choice creamy=distinct]
$R recheck && $R render && $R session [--force] && $R stage [--from-ratings]
bash tools/audio-lab/run.sh test tools/audio-lab/keys/tests
```

Dữ liệu: `~/AudioLab/work/_keys/<hồ sơ>/r1|r2/` (`raw/`, `strokes/`, `critic/`), `pick.json`, `sets/<vai trò>/` (master, runtime, câu gõ, kiểm lại), `~/AudioLab/work/_keys/master.json`. Không có âm nào trong Git.

## Kết quả nghe của chủ dự án (29/10/2026, 14:15)

Chủ dự án nghe năm file 20 giây (bộ máy xếp đầu của mỗi hồ sơ) và **trả cả năm**: "âm nghe chán thật, xạn, nghe rất nhựa, cái clack nghe đúng kiểu nhựa lởm, bàn phím gõ âm hay phải theo phím nhôm chất lượng cao… xào xạc quá lởm".

Nhãn chê: nhựa, rẻ (clack nhựa), xạn và xào xạc (nhiễu, tiếng sột soạt), chán. Không hồ sơ nào được dùng. Hướng mới: bản thu thật của bàn phím **vỏ nhôm cao cấp** (custom, switch lube, keycap tốt), xử lý sạch nhiễu; tiếng do mô hình tạo chỉ còn là phương án phụ nếu bản thu thật chưa có.

## Bàn giao cho Codex (AU-keys, 29/10/2026)

Chủ dự án giao tiếng phím cho Codex. Làn AU-keys dừng ở đây; chưa tải gì về máy.

### Pipeline làm được gì

`bash tools/audio-lab/run.sh keys <bước>` (mã: `tools/audio-lab/keys/`, 7 test: `bash tools/audio-lab/run.sh test tools/audio-lab/keys/tests`):

| Bước | Việc |
|---|---|
| `generate [--profiles] [--prompts A,B,C,D] [--seeds] [--run]` | Stable Audio 3 từ prompt trong `keys/specs/<hồ sơ>.yaml` (A, B, E: đoạn gõ 10 s; C, D, F: cú đơn 1 s), lọc chữ cấm Q2, Q6, chờ mô hình nặng khác |
| `slice [--run] [--force]` | Đoạn thu → từng cú gõ (`keys/strokes.py`): nhấn + nhả của chính phím, cách phím khác ≥ 150 ms, đầu tiếng ≤ 2 ms, rút khoảng giữ phím khi quá 180 ms (cách 260 ms), đuôi mũ hàm mũ; `SOURCES.json`, sổ giấy phép, `<stem>.proc.json` |
| `critic [--run]` | Bộ chấm L1, L1b, L2, L3, L4, thẻ ảnh mù |
| `pick --runs r1,r2` | Cổng (L1, lỗi mô hình L1b, đáy phím nhòe > 6 ms, tiếng chính > 15 ms, không tới −27 LUFS-M chỉ bằng tăng mức), điểm Q, chọn bộ 10 + 3 đều theo khoảng Kenney Impact P10–P90 (`keys/pick.py`, `keys/family.py`) → `~/AudioLab/work/_keys/<hồ sơ>/pick.json` |
| `master [--choice hồ sơ=vai trò]` | −27 LUFS-M max cho mọi file, WAV 24-bit + OGG q0,6 → `sets/<vai trò>/` |
| `recheck`, `render`, `session`, `stage [--from-ratings]` | Kiểm lại L1 trên master; câu gõ 60/100 WPM như kit phát (`keys/phrases.py`); phiên Bảng Nghe `keys-1`; staging theo bố cục kit `<base>/<id>/keys-manifest.json` (có bản Python của `keyboardFiles()` kiểm manifest) |

Hiện **không có gì trong staging**: `~/AudioLab/review/staging/keys/keys-manifest.json` ghi "nothing staged" vì chủ dự án trả cả năm.

### Dữ liệu ở đâu

- Khoảng 600 cú gõ ứng viên: `~/AudioLab/work/_keys/<hồ sơ>/r1|r2/strokes/` (WAV 24-bit, `_strokes.json`, `<stem>.proc.json`), bản thô `raw/` (589 bản tạo), kết quả chấm `critic/`.
- Năm bộ bị trả (và các bộ khác nhất, bộ dò): `~/AudioLab/work/_keys/<hồ sơ>/sets/top|distinct|probe/` (`masters/`, `runtime/`, `phrase-60wpm.wav`, `phrase-100wpm.wav`, `critic/`); tóm tắt `~/AudioLab/work/_keys/master.json`. Khoảng 900 MB, xóa được.
- Phiên nghe: `~/AudioLab/review/keys/sessions/keys-1.json`.

### Bản thu thật đã tìm (chưa tải; giấy phép kiểm tại trang nguồn ngày 29/10)

Freesound bắt buộc đăng nhập để tải; Wikimedia Commons thì không. Không trang Freesound nào hiện "tùy chọn AI".

| Hồ sơ đề xuất | Bản thu | URL | Giấy phép | Định dạng, dung lượng | Bàn phím, switch |
|---|---|---|---|---|---|
| Creamy Linear, Marbly | Techrul, "Typing on a rainy 75" | https://freesound.org/people/Techrul/sounds/815614/ | CC0 1.0 | MP3 204 kbps 48 kHz stereo, 58 s, 1,4 MB | Rainy 75 (vỏ nhôm); tag creamy, thocky; switch, plate không ghi |
| Deep Thock | Reina0613, "Mechanical keyboard typing sounds" | https://freesound.org/people/Reina0613/sounds/709460/ | CC0 1.0 | WAV 24-bit 48 kHz stereo, 48 s, 13,3 MB | ikki68 Aurora custom, WS Brown tactile lube tay, Zoom H8; vỏ, plate không ghi |
| Deep Thock | grcekh, "Keyboard Typing 4/5/9/10 (WhiteFox, Mechanical)" | https://freesound.org/people/grcekh/sounds/546167/ (gói https://freesound.org/people/grcekh/packs/30755/) | CC0 1.0 | MP3 320 kbps 44,1 kHz, 2:49, 6,5 MB (546167) | WhiteFox (vỏ nhôm), Hako Violet tactile, Yeti Nano, không hậu kỳ; cuối clip có phím gõ rời |
| Clean Clack | Seth_Makes_Sounds, "Typing On Keyboard (cherry mx browns)" | https://freesound.org/people/Seth_Makes_Sounds/sounds/618064/ | CC0 1.0 | WAV 24-bit 44,1 kHz stereo, 1:10, 17,8 MB | Cherry MX Brown, AT2035; bàn phím không ghi |
| Clean Clack | tofu_delivery, "Custom Mechanical Keyboard" | https://freesound.org/people/tofu_delivery/sounds/588650/ | CC0 1.0 | WAV 16-bit 44,1 kHz stereo, 47 s, 7,9 MB | custom, AT2035; bàn phím, switch không ghi |
| Soft Dome | grcekh, "Keyboard Typing 1/2/3/6/7 (HHKB, Topre)" | https://freesound.org/people/grcekh/sounds/546033/ | CC0 1.0 | MP3 152 kbps 48 kHz, 3:16, 3,6 MB (546033) | HHKB Pro Hybrid Topre 45g (vỏ nhựa), Yeti Nano; chưa tìm được Topre vỏ nhôm có giấy phép rõ |
| Thock (dự phòng) | aliyahb, "Thocky Keyboard Typing" | https://freesound.org/people/aliyahb/sounds/869164/ | CC0 1.0 | M4A 131 kbps mono, 33 s, 530 KB | không ghi |
| Clicky (nếu còn giữ) | SamsterBirdies, "Typing on a keyboard" | https://freesound.org/people/SamsterBirdies/sounds/489424/ | CC0 1.0 | FLAC 24-bit 44,1 kHz, 1:35, 13,3 MB | Cherry MX Blue, BOYA BY-M1 |
| Classic Spring (nếu còn giữ) | Raymangold22, "Typing - Model M 1986.ogg" | https://commons.wikimedia.org/wiki/File:Typing_-_Model_M_1986.ogg | CC0 1.0 | Ogg Vorbis 112 kbps, 12 s, 165 KB | IBM Model M 1986 (cũng có Model F 1984, cùng tác giả, CC0) |

- Đã xét, không nên dùng: Commons "Typing on Keychron V1 Ultra (Red Linear Switch).wav" (vỏ nhựa, thu bằng mic MacBook, giấy phép ghi lệch CC BY 4.0 và CC BY-SA 4.0); bàn phím gaming và laptop trên Freesound; Monkeytype, Bucklespring, keyboardsounds (GPL); gói Mechvibes, wayclick, keebsound (không có giấy phép rõ cho file âm); Sonniss (không phải CC0/CC-BY); OpenGameArt "Keyboard Soundpack #1" (Cherry KC 1000 màng cao su).
- Khoảng trống: Freesound CC0 gần như không có bản thu đặt tên rõ một bàn phím nhôm cao cấp (Keychron Q, Mode, custom 65 %) với switch, plate, keycap. Không tìm thấy bản nào cho "Marbly" (plate POM) và Topre vỏ nhôm. Đường chắc nhất cho mức 9: chủ dự án tự thu một bàn phím nhôm thật bằng mic gần (bản ghi của chủ dự án là nguồn sạch giấy phép nhất, kế hoạch §3.1 hạng 4), hoặc thu từ người quen có giấy đồng ý (§10.4).
- Freesound trả HTTP 429 khi tìm nhiều; tìm tiếp nên giãn cách.

### Chuỗi làm sạch đã viết (`keys/clean.py`, có test)

`clean_take(x, sr, params)` trước khi cắt cú gõ:

1. lọc cao 60 Hz, bậc 4, pha không (tiếng ù bàn, máy lạnh);
2. cổng phổ: phổ nhiễu là trung bình STFT của 15 % khung lặng nhất (giữa các cú gõ), bin dưới nhiễu + 6 dB bị hạ 24 dB, mặt nạ làm mượt theo thời gian và tần số, chỉ hạ chứ không nâng (không tạo tiếng vọng trước);
3. bỏ tiếng tách chỉ khi là lỗi: gai ≤ 3 mẫu, cách đầu tiếng của cú gõ trên 6 ms, nội suy lại; đầu tiếng của cú gõ (vẫn còn kêu 2–6 ms sau) không bao giờ bị sửa;
4. EQ theo hồ sơ: nâng nhẹ 250 Hz (+2 dB, Q 0,8) cho tiếng "thock" chắc, hạ 6 kHz (−2,5 dB) cho bớt xạn; cấm nâng dải 4–8 kHz.

Sau khi cắt: `stroke_gate` (bộ giãn xuống, ngưỡng −48 dB so với đỉnh cú gõ, tối đa 30 dB) để không còn tiếng phòng dưới và sau tiếng nhấn, tiếng nhả. Báo cáo ghi nền nhiễu và tiếng xì 4–8 kHz trong khung lặng trước và sau.

**Chưa nối vào pipeline:** cần một bước `ingest` đọc bản thu đã tải (WAV, FLAC; MP3 tùy bản libsndfile), chạy `clean_take`, ghi thành bản thô dạng `audiolab.keys.take/1` (nguồn, tác giả, URL, giấy phép CC0) để `slice` cắt như bản tạo, áp `stroke_gate` cho mỗi cú gõ, rồi ghi `docs/games/THIRD_PARTY.md` và sổ giấy phép. `slice` hiện chỉ đọc hồ sơ Stable Audio 3 (`gen/sa3.read_record`).

### Năm hồ sơ đề xuất (người điều phối, 29/10)

Creamy Linear (linear lube, keycap PBT), Deep Thock (tactile, plate đồng thau hoặc PC), Marbly (plate POM, linear), Clean Clack (ABS doubleshot dày trên vỏ nhôm, sáng mà chắc), Soft Dome (Topre trên vỏ nhôm). Kit `typing-fx` đang dùng id `creamy, thock, clicky, dome, spring` (`KEYBOARD_PROFILES` trong `audio.ts`); đổi id thì làn typing-feedback sửa theo.
