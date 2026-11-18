# Lô 0b vòng 2: nghe lại âm Stable Audio 3 sau buổi soát

Khoảng **15 phút**, 6 id (15 bản) trong 3 phiên ngắn. Đây là vòng 2 của bản thử Stable Audio 3 (mục 9 của [`AUDIO_PIPELINE.md`](../../docs/games/AUDIO_PIPELINE.md)). Vòng 1 nằm ở `~/AudioLab/review/batch-0b/`; anh không cần nghe lại vòng 1.

Không có gì ở đây được đưa vào game. Các bản chỉ nằm trong `~/AudioLab`.

## Mở bằng một lệnh

Từ thư mục gốc `typing-game`:

```bash
pnpm audio:board --batch 0b --open
```

- Trình duyệt mở `http://127.0.0.1:3191/` và liệt kê 3 phiên theo thứ tự **`0b-dh`, `0b-td`, `0b-ts`** (bảng xếp theo tên phiên). Nếu cổng 3191 đang bận (ví dụ bảng lô 0a còn mở), bảng dùng 3192 và in rõ địa chỉ trong terminal.
- Mở thẳng một phiên: thêm `?s=0b-dh` (hoặc `?s=0b-td`, `?s=0b-ts`) vào sau địa chỉ.
- Trang chạy hoàn toàn trên máy, không cần mạng.
- Nghe xong thì bấm `Ctrl+C` trong terminal để tắt.

## Vòng 2 đã sửa gì (để anh biết vì sao âm nghe khác vòng 1)

- **Không còn cắt vào giữa âm.** Máy tìm đầu tiếng thật cho mọi cửa sổ, kể cả cửa sổ đầu. Bản gõ hai lần, loạt đạn mà phát đầu quá ngắn, bản không có đầu tiếng thật bị loại kèm lý do, không đưa vào phiên.
- **Đuôi tắt dần theo hàm mũ**, không còn kiểu giữ nguyên rồi làm mờ ở 80 ms (lỗi của `hit.t1` vòng 1).
- **Tiếng tru giữ trọn**, kể cả đoạn lớn dần lúc đầu.
- **Ba công thức ghép lớp:** `hit.t1` (đầu tiếng Kenney, tiếng keng Stable Audio 3, thêm một lớp thân dày 200–800 Hz), `gun.xung` (tiếng cơ khí Kenney, thân Stable Audio 3, sub tổng hợp, chỉ một phát), `fire.impact.a` (đầu tiếng Kenney Impact, thân lửa Stable Audio 3, sub ngắn dưới 150 ms).
- **Prompt mới** ở ba chỗ buổi soát yêu cầu: rừng thông (nhấn lá kim và stereo, bỏ hẳn chữ "chim"), lời gọi Chặt (thêm 3 prompt kiểu gõ trầm, chắc), tiếng tru (tạo dài 2 s và 3 s để giữ trọn tiếng gọi).
- **Nền rừng:** các vạch "lược" cao tần của bộ giải mã đã được cắt về ngang nền.

### Sửa thêm sau buổi soát thứ hai (bản anh sắp nghe)

- **`gun.xung` đã dựng lại.** Bản v3 trước đó có tiếng nổ thứ hai khoảng 25 ms sau tiếng đầu: tiếng giòn của chính Stable Audio 3 còn nằm trong lớp thân. Nay lớp thân Stable Audio 3 qua lọc thông thấp 1,5 kHz, đúng vai "thân 120–800 Hz" của thẻ, nên dải cao chỉ còn tiếng khóa nòng Kenney. Cửa sổ thân bắt đầu 4 ms trước đỉnh thân. Bốn thân được chọn bằng cách dựng thử cả 24 bản thô, chỉ giữ thân không tạo đầu tiếng thứ hai. Thử lặp 20 phát (cách 200 ms, ±10 % nhịp, ±100 cent, ±2 dB): cả 4 biến thể đều chỉ có 1 đầu tiếng cao tần mỗi phát, 20/20 phát.
- **Máy có thêm phép đo "hai đầu tiếng"** cho mọi âm ngắn, kể cả master của công thức. Bản nào bị gắn cờ thì không vào phiên. Vì vậy `fire.impact.a` v3 bị thay bằng v4: v3 có một tiếng lách tách lớn 35 ms sau cú chạm.
- **Đầu tiếng phải có bằng chứng.** Bản bắt đầu ngay từ mẫu đầu của file chỉ được tin khi 1,5 ms đầu nhỏ hơn đỉnh ít nhất 30 dB, hoặc khi tiếng tách cao tần nằm trong 5 ms đầu. Không đạt thì gắn "đầu tiếng chưa xác minh" và không đưa vào phiên: 11/24 bản `hit.t1`, 5/41 bản `call-chop`, 10/24 bản `gun.xung`. Hai bản Stable Audio 3 của `hit.t1` ở lần chuẩn bị trước thuộc loại này nên đã bị thay.
- **Nền rừng:**
  - Hai kênh được cân theo từng 1/3 octave. Bản đứng đầu H s2004 trước đây nghiêng phải 5,9 dB, nay lệch 0,0 dB. 22/47 bản được cân; lệch lớn nhất là 9,4 dB trước khi cân, 0,3 dB sau khi cân.
  - Bản "gần như mono" nay được đo theo kênh bên so với kênh giữa (thấp hơn ≥ 10 dB là gần như mono), không chỉ theo tương quan.
  - Bộ dò dấu vòng lặp bắt thêm tiếng thụp trầm dưới 200 Hz và tiếng gần như có cao độ (như tiếng 3,93 kHz).
  - Phiên chỉ có bản stereo rộng (tương quan ≥ 0,3, kênh bên không quá thấp), cân kênh, và không có dấu vòng mà máy đo được. Bản dò cũ H s2001 gần như mono và có dấu vòng nên đã bị thay.
  - Máy chỉ đo được những dấu nó biết. Tai anh vẫn là phép thử cuối.

## Trước khi nghe

- Dùng **tai nghe** nếu có. Ở hộp đầu mỗi phiên, bấm `1` (tai nghe) hoặc `2` (loa).
- Nghe theo thứ tự bảng liệt kê: `0b-dh` → `0b-td` → `0b-ts`. Chỉnh âm lượng máy ở id đầu tiên của phiên `0b-dh` (nền rừng), rồi **giữ nguyên** đến hết cả ba phiên. Mọi bản trong một id đã được cân cùng độ to.
- Nhãn A, B, C xếp ngẫu nhiên. Tên file, nguồn và điểm máy bị giấu. **Thẻ ảnh chỉ mở khi anh chấm xong cả phiên.**
- **Hai id có nhãn ghi sẵn trên bản**, đó là chủ ý, không phải lộ thông tin:
  - `call-chop`: một bản ghi "Đối chứng có chủ ý: tiếng 'tốc' rỗng, cao (giống mõ?)".
  - `enemy.quadruped.howl`: cả hai bản ghi "Bị luật chặn: tiếng tru lớn dần chậm (> 30 ms)".
  Anh cứ chấm theo tai như mọi bản khác.

## Nghe gì

Theo đúng thứ tự bảng liệt kê:

| Phiên | Id | Câu hỏi cho tai anh |
|---|---|---|
| **0b-dh** · Rồng Giữ Ải | `amb.forest` (3 bản) | Gió qua rừng thông, vòng 6 s. **Nghe ít nhất 3 vòng (18 s) ở bối cảnh Lặp** (phím `↓`; "Một mình" chỉ phát một vòng). Bản nào ra **gió lùa qua lá kim** (xào xạc sáng), bản nào chỉ là **tiếng gió ù vào micro**, bản nào chỉ là **tiếng xì, nhiễu trắng**? Có tiếng chim, côn trùng, tiếng gõ, tiếng thụp không? Có nhận ra chỗ nối không? Có rộng, cân hai tai và dễ chịu không? Ba bản trải từ trầm, ù tới sáng, xì: máy nghe một bản là "lá xào xạc" lẫn "xe cộ", hai bản còn lại là "nhiễu trắng, nhiễu hồng" và "tiếng xì". Đây là chỗ anh chọn hướng, chưa có bản nào máy thấy thật sự đúng thẻ |
| | `enemy.quadruped.howl` (2 bản) | Thú bốn chân tru gọi bầy, **trọn một tiếng tru** (khoảng 1,1 s), phát cách nhau 1,5 s như trong game. Có rợn, hợp "rừng mục" không? Đoạn lớn dần lúc đầu có tự nhiên không, hay anh muốn tiếng tru vào nhanh hơn? Cuối tiếng tru có tiếng rít cao không (máy gắn cờ ở cả hai bản)? |
| | `fire.impact.a` (2 bản) | Cầu lửa trúng: **phụt lửa trầm, thân tròn, lách tách nhỏ**. Đầu tiếng có đủ "chạm" chưa (vòng 1 là tiếng phụt mềm không có đầu)? Phần trầm có kéo lê không? Có ra lửa không, hay chỉ là tiếng nổ, tiếng đập cửa? |
| **0b-td** · Lời Gọi | `call-chop` (3 bản) | Lời gọi Chặt: tài liệu game cần **gõ gỗ trầm, chắc vào thân tre**. Hai bản theo hướng đó, một bản là đối chứng tiếng "tốc" rỗng, cao. Bản nào nghe giống **mõ chùa** thì gắn **"sai chất liệu"** (luật văn hóa TK 22.1). Có nghe ra tre không? Để ý thêm: một trong hai bản gõ trầm có hai đầu tiếng sát nhau (cách khoảng 7 ms), có thể nghe như **"gõ đúp"**. Bản kia còn một họa âm khoảng 720 Hz, gần cao độ của tiếng "tốc". Nghe ra thì ghi chú (`/`) |
| **0b-ts** · Tuyến Cuối | `hit.t1` (3 bản) | Đạn trúng vỏ thép, phát 5 lần mỗi giây. Bản nào có **"keng" trên thép kèm chút thân nặng**, bản nào chỉ "tách" mỏng hay chói? Nghe ở bối cảnh Lặp: có mệt tai không? Đuôi có tắt tự nhiên không, hay bị cụt? Hai bản là công thức ghép lớp có thân (41–57 % năng lượng ở 200–800 Hz). Một bản là Stable Audio 3 nguyên bản, chỉ khoảng 5 % ở dải đó, đúng lỗi "thiếu thân" của vòng 1; bản này để đối chứng |
| | `gun.xung` (2 bản) | Pháo tự động, phát 5 lần mỗi giây. Có ra **pháo thép nặng, một phát gọn** (tiếng cơ khí, cú đấm trầm) không, hay nghe như tiếng gõ cửa? Còn nghe ra phát thứ hai trong một phát thì gắn "rè/lỗi" và ghi chú "hai phát". Máy (AST) không nhận ra âm này là tiếng súng, nên tai anh quyết định |

Nhãn quan trọng nhất ở lô này: **sai chất liệu** (nhất là `call-chop`), **rè/lỗi**, **yếu/mỏng**, **nhàm khi lặp** (nhất là `amb.forest`) và **chậm**.

## Cách chấm, chỉ bằng phím

| Phím | Việc |
|---|---|
| `Space` | Phát hoặc dừng bản đang chọn |
| `1`, `2`, `3` | Chọn bản A, B, C và phát |
| `←` `→` | Chọn bản trước hoặc sau, không phát |
| `⇧1` … `⇧5` | Cho 1–5 sao bản đang chọn (3 sao: dùng được nếu sửa nhẹ) |
| `V` | Đánh dấu bản tốt nhất |
| `0` | Không bản nào đạt |
| `H` `G` `C` `D` `R` `Y` `K` `T` `N` `M` `S` `L` `P` `E` `O` | Nhãn: hay, hợp game, chói, đục, rè/lỗi, yếu/mỏng, quá dài, quá to, quá nhỏ, chậm, sai chất liệu, lạc thể loại, nhàm khi lặp, rẻ tiền, khó nghe tiếng đọc |
| `↑` `↓` | Đổi bối cảnh: Một mình, Lặp (đúng nhịp chơi), Loa nhỏ |
| `/` | Ghi chú ngắn (`Enter` lưu, `Esc` thoát) |
| `Enter` | Lưu. `Enter` lần nữa sang id tiếp |
| `⌫` | Quay lại id trước |
| `?` | Bảng phím |

## Mất bao lâu

- 15 bản. Nghe mỗi bản ở bối cảnh mặc định mất khoảng 4 phút, riêng nền rừng 3 bản × 3 vòng là gần 1 phút. Cộng thời gian so và chấm: khoảng **15 phút**.
- Dừng giữa chừng được. Mở lại bằng đúng lệnh trên, bảng làm tiếp từ chỗ đã dừng.

## Điểm của anh quyết định gì

Mỗi lần lưu thêm một dòng vào `~/AudioLab/review/<game>/ratings.jsonl` (chỉ ghi thêm). Sau phiên, Claude đọc file điểm và:

1. **Chốt có dùng tiếp Stable Audio 3 không (mục 9).** Điều kiện: ít nhất 3/6 id có một bản anh chấm từ 3 sao. Đạt thì Stable Audio 3 là nguồn chính cho lửa, nổ, nền và quái ở lô 1; không đạt thì các nhóm đó quay về công thức Kenney, tổng hợp và bộ phát mẫu.
2. **Chốt hướng công thức** cho `hit.t1`, `gun.xung`, `fire.impact.a`: bản ghép lớp được từ 3 sao thì công thức đó thành mẫu cho cả họ âm (`hit.t2`, `hit.t4`, `fire.impact.b`, `fire.impact.c`…) ở lô 1.
3. **`call-chop` và luật văn hóa:** bản nào bị gắn "sai chất liệu" thì prompt đó bị cấm cho mọi lời gọi. Nếu anh lại thích bản đối chứng hơn và không thấy giống mõ, Claude ghi thành một câu hỏi để anh duyệt; thẻ spec không tự đổi.
4. **`amb.forest`:** chọn hướng prompt cho mọi nền rừng (trầm, ù như vòng này hay sáng, xào xạc), và cho biết dấu lặp nào anh nghe ra để chỉnh bộ dò "dấu vòng lặp".
5. **Luật đầu tiếng sinh vật (≤ 30 ms):** nếu anh chấm tiếng tru nguyên vẹn từ 3 sao, Claude soạn đề xuất nới luật cho tiếng gọi dài (ví dụ đo đầu tiếng của tiếng tru theo lớp tách, hoặc cho phép lớn dần đến 150 ms). **Luật chỉ đổi khi anh duyệt**; kế hoạch chưa bị sửa.
6. **So tai anh với máy:** ở `hit.t1` và `amb.forest` có một bản máy xếp thấp (anh không biết là bản nào). Nếu anh chấm nó cao, máy đang xếp sai ở id đó và trọng số các lớp chấm được chỉnh lại (mục 4.6).

## Nếu có trục trặc

- **Không nghe thấy gì:** bấm chuột vào trang một lần, rồi kiểm âm lượng máy.
- **Kiểm file phiên:** `pnpm audio:board check`.
- Phiên được tạo lại bằng `bash tools/audio-lab/run.sh batch0b session --force`. Không có `--force` thì lệnh từ chối ghi đè. Điểm đã chấm không bị xóa, nhưng đừng tạo lại khi đang chấm dở.
