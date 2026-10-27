# Lô 1c · Tuyến Cuối: phiên nghe `1c-ts-1`, `1c-ts-2` (âm theo hình dạng hành động, Q6)

Hai phiên, mỗi phiên dưới 20 phút: **`1c-ts-1`** khoảng 13 phút (4 id, 16 bản), **`1c-ts-2`** khoảng 9 phút (3 id, 10 bản). Thiết kế: [`Q6_REWRITE_2026-10-24.md`](Q6_REWRITE_2026-10-24.md) mục 7, 11, 12, 13 (13 là bản dựng lại sau phản biện, 26/10); luật của anh: [`DECISIONS.md`](DECISIONS.md) Q6; bài thử súng liên thanh: [`BATCH1_BRIEF.md`](BATCH1_BRIEF.md) mục 3. Báo cáo của máy (chỉ đọc sau khi chấm): `~/AudioLab/work/_batch1c/b1c/REPORT.md`.

Không có gì ở đây được đưa vào game. Mọi bản nằm trong `~/AudioLab`.

## Mở

```bash
pnpm audio:board --game typing-survival --batch 1c --open
```

- Bảng hiện cả hai phiên. **`1c-ts-1`** trước: súng, vì mọi id khác nghe trên nền súng đang bắn, rồi ba bậc trúng. **`1c-ts-2`** sau: hạ quái, báo nguy.
- `1c-ts-1` thêm **2 cặp mốc** lấy từ lô 0a, 0b (anh không cần biết cặp nào). `1c-ts-2` không có cặp mốc: Tuyến Cuối chỉ có 5 cặp đã chấm; 3 cặp có một bản cũng nằm trong phiên 1c (nên không mù), 2 cặp còn lại đã ở `1c-ts-1`. Mỗi phiên tối đa 10 mục và 20 phút (kế hoạch mục 7).
- Thẻ ảnh và số đo của máy chỉ mở khi chấm xong cả phiên. Mệt thì dừng: bảng nhớ chỗ đang nghe.

## Nghe gì: bốn phần của Q6

Tuyến Cuối là hành lang thép. Súng và đòn to phải có trọng lượng; quái bầy nhỏ thì nhỏ.

| Phần | Nghe gì | Ví dụ ở phiên này |
|---|---|---|
| Tụ lực | Lên nòng, thép căng trước khi vỡ | Khóa nòng đóng trước phát súng |
| Phát | Đầu tiếng giòn, có lực | Tiếng nổ của phát súng; keng thép khi đạn trúng |
| Thân | Thép dày, lực đẩy; lớp trầm chỉ nằm dưới | Thân thép của bậc trúng; dầm ngân của đòn lớn |
| Đuôi | Vang hành lang thép, ngắn và thấp | Đạn trúng vang dọc hành lang; còi báo nguy dội lại |

- **Cấm:** "bụp", "thụp", puff, pop, đồ chơi, retro; một tiếng trầm ngắn không có thân và đuôi.
- Mã game phát **một tiếng** cho mỗi bậc trúng, mỗi phát súng, không ghép lớp. Vì vậy thân và đuôi phải nằm sẵn trong file.
- **Giọng đọc vẫn phải rõ** (Q6 luật 4) giữa tiếng súng 10 viên mỗi giây.

Gắn nhãn theo Q6:

| Anh nghe thấy | Gắn |
|---|---|
| Loạt súng rời từng phát, không liền | `J` ngắt quãng (nhãn quan trọng nhất của súng) |
| Một cú trầm rồi tắt, "bụp", "thụp" | `D` đục, cộng `Y` yếu/mỏng |
| Hai cú gõ sát nhau trong một tiếng trúng | Ghi chú (`/`): "gõ đúp" |
| Đồ chơi, retro | `E` rẻ tiền hoặc `L` lạc thể loại |
| Chói, mỏng khi nghe hàng trăm lần | `C` chói, `P` nhàm khi lặp |
| Che giọng đọc | `O` khó nghe tiếng đọc |
| Lách cách, rè, méo, tiếng "số" lạ | `R` rè/lỗi |

## Bối cảnh

- **Liên thanh 3 s** (phím `↑` `↓`, mở đầu ở súng, bậc trúng, hạ quái): một đoạn trận 4 s qua bộ trộn giống game (mức bus, bộ nén từng bus, hạ tiếng khi đọc từ), có giọng đọc tiếng Anh của macOS. Súng Xung bắn 10 viên mỗi giây, mỗi viên trúng 150–300 ms sau, hai từ được gõ xong, một đòn lớn ở 2,3 s, rồi ngừng bắn. Các bản dựng của một id chỉ khác nhau ở đúng bản đang chấm.
  - Súng, bậc trúng: cảnh súng bắn liên tục, có nền cơ khí và đuôi khi ngừng.
  - Hạ quái: như trên, thêm quái bầy vỡ, một lính tinh nhuệ nổ ở 1,9 s, từ thứ hai gõ chuẩn.
  - Súng cố định ở mọi id khác là hướng 2 của lô 1 (bộ phát có số đo liên thanh tốt nhất của lô 1).
- **Trong trận thô** (báo nguy): súng đang bắn thì tuyến bị phá ở 1,2 s.
- **Lặp**: súng 30 lần cách 100 ms; `hit.t1` 20 lần cách 100 ms; quái bầy 20 lần cách 150 ms; `hit.t2` 8 lần cách 400 ms.
- **Một mình**, **Loa nhỏ**: như các lô trước.

## Từng id

| Phiên | Id | Số bản | Mở đầu | Câu hỏi |
|---|---|---|---|---|
| `1c-ts-1` | `gun.xung` | 4 | Liên thanh 3 s | Mỗi bản là một bộ phát (bộ nặng và bộ nhẹ xen nhau). Một bản là hướng 2 của lô 1 (khóa nòng, thân, đuôi ghép); hai bản là Stable Audio 3 nguyên khối của lô 1c (prompt I và K, bộ nhẹ là chính các bản đó phát nhỏ hơn 5 dB); một bản ghi "Cách game đang phát". Có nghe thành **một loạt liền, có lực** không, hay rời từng phát (`J`)? |
| `1c-ts-1` | `hit.t1` | 4 | Liên thanh 3 s | Đạn trúng vỏ thép, tới 10 lần mỗi giây: keng giòn, thân gọn, đuôi hành lang ngắn. Có che tiếng súng hay giọng đọc không? |
| `1c-ts-1` | `hit.t2` | 4 | Liên thanh 3 s | Chí mạng: nặng hơn `hit.t1`, lớp trầm chỉ ở dưới. Có "gõ đúp" không? |
| `1c-ts-1` | `hit.t4` | 4 | Liên thanh 3 s | Đòn lớn: dầm thép ngân dài dọc hành lang. To và dài hơn `hit.t2` rõ chưa? |
| `1c-ts-2` | `kill.swarm` | 3 | Liên thanh 3 s | Quái kim loại vỡ, hàng trăm lần mỗi trận. Hướng "vỡ có vang": bản Stable Audio 3 mới, và công thức của lô 1. Có chói, có mỏng, lặp có mệt không? |
| `1c-ts-2` | `kill.elite` | 3 | Liên thanh 3 s | Lính tinh nhuệ nổ: thép xé, nổ trầm có thân, tia điện, mảnh rơi. Đuôi có bị cụt đột ngột không? |
| `1c-ts-2` | `hurt.breach` | 4 | Trong trận thô | Báo nguy: nổ trầm có thân, thép rên, còi hai nốt, vang dội hành lang. Khác hẳn tiếng trúng, đủ rõ để biết tuyến vừa bị phá không? Còi có vào ngay trên tiếng nổ không? Một bản có nhãn "đuôi rút vừa thẻ": âm gốc còn kêu ở 960 ms, độ dài tối đa của thẻ, nên máy rút đuôi cho vừa; thấy đuôi cụt thì đó là bằng chứng thẻ quá ngắn |

- Prompt J của súng không có trong phiên: 6/6 bản kêu ngay từ mẫu đầu (đầu tiếng chưa xác minh), 5 bản còn bị luật đầu tiếng chặn.
- `hurt.breach` prompt D không có bản nguyên khối trong phiên: 6/6 bản còn to tới sát 960 ms, không còn chỗ cho đuôi (sửa sau phản biện, Q6_REWRITE 13.2).
- **Vì sao hai phiên** (sửa sau phản biện): một phiên 7 id, 26 bản và 3 cặp mốc mất khoảng 20–25 phút, vượt giới hạn 20 phút của kế hoạch.
- Nhiều bản trúng, hạ quái của lô 1c cũng kêu ngay từ mẫu đầu và không được đưa vào phiên (`kill.elite` 21/24, `hit.t2` 15/22, `hit.t1` 14/23; Q6_REWRITE 11.3 #3). Vì vậy `kill.elite` chủ yếu là công thức.

## Cặp mốc (đo độ nhất quán)

- 2 cặp mốc từ lô 0a, 0b được chèn vào `1c-ts-1` khi anh mở phiên lần đầu. Bảng không cho biết mục nào là cặp mốc.
- Vài id có lẫn bản anh đã chấm ở lô trước, hoặc bản cũng nằm trong phiên S1, S4 của lô 1. Phiên không ghi là bản nào.
- Bản "Cách game đang phát" của súng (0a v2, anh chấm 4/5) mang nhãn, nên **không** dùng để đo độ nhất quán; cặp 0a của súng có bản này cũng không được chọn làm cặp mốc.
- Hai thứ này cho máy đo anh có chấm lại giống lần trước không (mục 4.6 bước 6).

## Thiết bị

- Nghe cả phiên bằng **tai nghe** (hộp đầu phiên: phím `1`).
- Rồi mở lại `1c-ts-1` bằng **loa** (`2`), chỉ cho `gun.xung`: lực của súng phải nghe được trên loa nhỏ.
- Chỉnh âm lượng máy ở id đầu, giữ nguyên tới hết.
- Nghe thấy lỗi thì gắn **"rè/lỗi"** (`R`). Chưa lượt chấm nào có nhãn này; nó là dữ liệu duy nhất để chỉnh bộ dò lỗi của máy (L1b).

## Còn chờ điểm của lô 1

| Phiên lô 1 | Id | Lô 1c thay chưa | Còn cần chấm vì |
|---|---|---|---|
| `1-ts-s1` (chưa chấm) | `gun.xung` | Thêm I, K nguyên khối; hướng 1 và 3 chỉ có ở S1 | Chọn hướng súng và mức nền (16 hay 11 dB) |
| `1-ts-s1` (chưa chấm) | `hit.t1`, `hit.t2`, `hit.t4` | Có: sinh lại theo Q6 | Chỉ còn để đo máy (`critic agreement --batch 1`) |
| `1-ts-s1` (chưa chấm) | `gun.xung.loop`, `gun.xung.tail`, `hit.sub`, `hit.tail` | Không | Chỉ có ở S1. Bản dựng 1c dùng bản máy xếp đầu cho nền và đuôi súng |
| `1-ts-s4` (chưa chấm) | `kill.swarm`, `kill.elite`, `hurt.breach` | Có: sinh lại theo Q6 | Chỉ còn để đo máy |
| `1-ts-s4` (chưa chấm) | `word.load`, `word.perfect`, `gun.tia.pulse` | Không | Chỉ có ở S4 |

**Thứ tự đề xuất:** `1c-ts-1`, `1c-ts-2`, rồi S1 (nền, đuôi súng, mức nền), rồi S4.

## Sau phiên

- Điểm ghi thêm vào `~/AudioLab/review/typing-survival/ratings.jsonl`.
- Claude chạy `bash tools/audio-lab/run.sh critic agreement --batch 1c` để đo bản hiệu chỉnh 1 trên dữ liệu mới, rồi chốt hướng súng, bản gốc của từng id và làm lượt biến thể.
- `hit.t4` nay đạt −20,1 LUFS-M sau khi thân được cân mức (trước −22,9; Q6_REWRITE 13.1), gần như không cần bù `gainDb`.
- Bản dựng trong bối cảnh và số đo: `~/AudioLab/work/_batch1c/b1c/typing-survival/context/`.
