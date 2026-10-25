# Lô 1c · Rồng Giữ Ải: phiên nghe `1c-dh-1`, `1c-dh-2` (âm theo hình dạng hành động, Q6)

Hai phiên, mỗi phiên dưới 20 phút: **`1c-dh-1`** khoảng 13 phút (4 id, 16 bản), **`1c-dh-2`** khoảng 10 phút (3 id, 11 bản). Thiết kế: [`Q6_REWRITE_2026-10-24.md`](Q6_REWRITE_2026-10-24.md) mục 7, 11, 12, 13 (13 là bản dựng lại sau phản biện, 26/10); luật của anh: [`DECISIONS.md`](DECISIONS.md) Q6. Báo cáo của máy (chỉ đọc sau khi chấm): `~/AudioLab/work/_batch1c/b1c/REPORT.md`.

Không có gì ở đây được đưa vào game. Mọi bản nằm trong `~/AudioLab`.

## Mở

```bash
pnpm audio:board --game dragon-hold --batch 1c --open
```

- Bảng hiện cả hai phiên. Nghe **`1c-dh-1`** trước (khạc lửa và ba cỡ cầu lửa trúng), rồi **`1c-dh-2`** (trúng nhiều quái, bom, tiếng tru). Nghỉ giữa hai phiên được.
- Mỗi phiên thêm **2 cặp mốc** lấy từ lô 0a, 0b (anh không cần biết cặp nào); hai phiên không lấy trùng cặp. Mỗi phiên tối đa 10 mục và 20 phút (kế hoạch mục 7).
- Thẻ ảnh và số đo của máy chỉ mở khi chấm xong cả phiên.
- Mệt thì dừng: bảng nhớ chỗ đang nghe, mở lại là làm tiếp.

## Nghe gì: bốn phần của Q6

Mỗi âm hành động phải có hình dạng của hành động. Rồng là sinh vật lớn: âm phải to xác, mạnh, vang.

| Phần | Nghe gì | Ví dụ ở phiên này |
|---|---|---|
| Tụ lực | Hít vào, khè họng, ngòi xì trước khi phát | Hỏa Long khè họng trước khi lửa bắt |
| Phát | Đầu tiếng có lực, không lề mề | Lửa bắt dưới áp lực rồi gầm; tiếng nổ của bom |
| Thân | Lửa cháy, lực đẩy, vật bay; có trọng lượng | Cầu lửa lao ra xa; than lách tách, mảnh văng |
| Đuôi | Vang trong không gian của bản đồ: thung lũng, rừng thông | Vang thấp, dài khoảng 0,6–1,2 s ở mức nhỏ |

- **Cấm:** "bụp", "thụp", puff, pop, bóng bay, đồ chơi, hoạt hình, retro; một tiếng trầm ngắn không có thân và đuôi.
- **Giọng đọc vẫn phải rõ** (Q6 luật 4): phần 1–4 kHz của âm phải nhường giọng đọc từ.
- Âm phát sau mỗi từ (khoảng 1,5 s một lần) phải có đuôi đủ thấp để nghe 20 từ liền không mệt. Đòn to (`fire.impact.c`) được đuôi dài và to hơn rõ.

Gắn nhãn theo Q6:

| Anh nghe thấy | Gắn |
|---|---|
| Một cú trầm rồi tắt, "bụp", "thụp" | `D` đục, cộng `Y` yếu/mỏng |
| Đồ chơi, hoạt hình, bóng bay, retro | `E` rẻ tiền hoặc `L` lạc thể loại |
| Lên chậm, lề mề, thiếu lực ở đầu tiếng | `M` chậm |
| Đuôi cụt, không có vang | Ghi chú (`/`): "đuôi cụt" |
| Che giọng đọc | `O` khó nghe tiếng đọc |
| Lách cách, rè, méo, tiếng "số" lạ | `R` rè/lỗi |

## Bối cảnh

- **Trong trận thô** (phím `↑` `↓`, mở đầu ở mọi id): mỗi bản được dựng sẵn trong một đoạn trận, qua bộ trộn giống game (mức bus, hạ tiếng khi đọc từ, vang rừng, bộ giới hạn), có giọng đọc tiếng Anh của macOS. Các bản dựng của một id chỉ khác nhau ở đúng bản đang chấm.
  - **Chuỗi khạc lửa** (9,6 s), cho họ lửa: gõ xong một từ mỗi 1,5 s; Hỏa Long khạc lửa cùng lúc với giọng đọc; cầu lửa rơi 0,6 s sau, theo lượt a, b, và đòn to c ở từ thứ 3 và thứ 6.
    - Tiếng khạc nay dài 600–900 ms (lô 1: 340 ms), nên đuôi của nó còn vang khi cầu lửa rơi. Game cũng phát như vậy.
    - Từ thứ 2 và thứ 5 trúng 3 và 4 quái, nên có thêm `impact.multi` chồng lên tiếng trúng, ở mức của game.
  - **Bầy thú** (8 s), cho tiếng tru: vó thú kéo tới, tru hai lần, ba từ có cầu lửa.
  - **Bẫy** (7 s), cho bom: bầy lạo xạo, bốn từ, bom nổ hai lần.
  - Nền là bản rừng thông anh đã chấm 4/5 (lô 0b).
- **Lặp 8 lần**: họ lửa phát mỗi 1,5 s, đúng nhịp sau mỗi từ. Đây là chỗ kiểm đuôi thấp. Tiếng tru: 4 lần.
- **Một mình**: nghe đủ bốn phần, nhất là đuôi.
- **Loa nhỏ**: như laptop.

## Từng id

| Phiên | Id | Số bản | Mở đầu | Câu hỏi |
|---|---|---|---|---|
| `1c-dh-1` | `fire.cast` | 4 | Trong trận thô | Có đủ bốn phần không: khè họng, lửa bắt và gầm, cầu lửa lao xa, đuôi thung lũng? Bản nào nghe ra rồng lớn, mạnh, vang? Giọng đọc có bị che không? Bốn bản thuộc ba hướng khác nhau của thẻ. Hai bản có nhãn "đuôi rút vừa thẻ" |
| `1c-dh-1` | `fire.impact.a` | 4 | Trong trận thô | Lửa bùng có thân, hay "một cục rơi xuống"? "Lặp" mỗi 1,5 s có mệt không (`P`)? |
| `1c-dh-1` | `fire.impact.b` | 4 | Trong trận thô | Tối hơn .a, than nổ khô. Cùng họ mà phân biệt được không? Một bản có nhãn "bị luật chặn" |
| `1c-dh-1` | `fire.impact.c` | 4 | Trong trận thô | Đòn to: dài và nặng hơn .a rõ chưa? Có tiếng nổ thứ hai không? Một bản có nhãn "bị luật chặn" |
| `1c-dh-2` | `impact.multi` | 3 | Trong trận thô | Âm mới, chưa có ở lô 1: một từ trúng nhiều quái. Có nghe ra lửa bùng nhiều chỗ không, có lấn tiếng trúng thường không? Cả 3 bản có nhãn "bị luật chặn"; 2 bản có thêm "đuôi rút vừa thẻ" |
| `1c-dh-2` | `trap.pine-bomb.trigger` | 4 | Trong trận thô | Nổ trầm có thân, hay "thụp"? Hạt, dăm văng, vang rừng thông? Một bản có nhãn. Thử "Loa nhỏ" |
| `1c-dh-2` | `enemy.quadruped.howl` | 4 | Trong trận thô | Trọn một tiếng tru, dâng lên rồi hạ, vang rừng mục xa? Cuối tiếng tru có tiếng rít cao không? Cả 4 bản có nhãn |

- **Vì sao hai phiên** (sửa sau phản biện): một phiên 7 id, 26 bản và 3 cặp mốc mất khoảng 20–25 phút, vượt giới hạn 20 phút của kế hoạch.
- **Hướng F của `fire.cast` không có trong phiên:** 5/6 bản gầm còn to tới sát 900 ms, độ dài tối đa của thẻ, nên không còn chỗ cho đuôi; bản thứ sáu không có đầu tiếng thật. Hướng H chỉ còn 1/6 bản vì cùng lý do.

## Bản có nhãn

- **"Bị luật chặn":** cổng vệ sinh của máy đòi âm va chạm lên tới đỉnh trong 10 ms. Âm có phần tụ lực theo Q6 (lửa bùng dần, ngòi trước tiếng nổ, nhiều quả cầu lửa) lên chậm hơn, nên bị chặn.
- Tiếng tru bị luật "sinh vật lên ≤ 30 ms" chặn, như ở lô 1. Q3 đã quyết nới tới 150 ms; cổng L1 chưa đổi vì §4.3.1 của kế hoạch chưa sửa (việc của người điều phối).
- **"Đuôi rút vừa thẻ":** âm gốc còn kêu (trên −30 dB) ở độ dài tối đa của thẻ, nên máy rút đuôi cho vừa. Nếu bản này hay mà anh thấy đuôi cụt, đó là bằng chứng thẻ quá ngắn (làn Specs), không phải bản không có đuôi.
- **Anh chấm các bản này như mọi bản.** Nếu bản có nhãn được chấm ngang hoặc cao hơn, đó là bằng chứng để sửa luật hay thẻ (mục 4.3.1 của kế hoạch, làn Specs), không phải để bỏ bản.

## Cặp mốc (đo độ nhất quán)

- 2 cặp mốc từ lô 0a, 0b được chèn vào mỗi phiên khi anh mở phiên lần đầu. Bảng không cho biết mục nào là cặp mốc. Cặp nào có bản cũng nằm trong phiên lô 1c thì không được chọn.
- Một id có lẫn một bản anh đã chấm ở lô trước. Phiên không ghi là id nào, bản nào.
- Hai thứ này cho máy đo anh có chấm lại giống lần trước không (mục 4.6 bước 6). Lô 0a, 0b chưa có số đo này.

## Thiết bị

- Nghe cả phiên bằng **tai nghe** (hộp đầu phiên: phím `1`). Mọi lượt chấm trước đều bằng loa; thân dưới 150 Hz và đuôi vang nhỏ chỉ nghe rõ bằng tai nghe.
- Nếu còn sức: mở lại bằng **loa** (`2`), chỉ cho `fire.cast` (`1c-dh-1`) và bom (`1c-dh-2`).
- Chỉnh âm lượng máy ở id đầu, giữ nguyên tới hết.
- Nghe thấy lỗi thì gắn **"rè/lỗi"** (`R`). Chưa lượt chấm nào có nhãn này; nó là dữ liệu duy nhất để chỉnh bộ dò lỗi của máy (L1b).

## Còn chờ điểm của lô 1

| Phiên lô 1 | Id | Lô 1c thay chưa | Còn cần chấm vì |
|---|---|---|---|
| `1-dh-s2` (chưa chấm) | `fire.cast`, `fire.impact.a`, `.b`, `.c`, `enemy.quadruped.howl`, `trap.pine-bomb.trigger` | Có: cả 6 id sinh lại theo Q6 | Chỉ còn để đo máy (`critic agreement --batch 1`) và để thử luật đuôi Q6 trên bản "phụt tròn" (DECISIONS Q6, bước kiểm 2–3). Không còn chọn hướng |
| `1-dh-s3` (chưa chấm) | `amb.forest`, `amb.river`, `enemy.swarm.march`, `enemy.quadruped.march`, `wave.horn`, `general.g01.horn` | Không | Nền và tù và chỉ có ở S3. Bản dựng 1c dùng bản máy xếp đầu của S3 cho suối, bầy, vó thú |

**Thứ tự đề xuất:** `1c-dh-1`, `1c-dh-2`, rồi S3. S2 để sau cùng, nếu anh còn thời gian.

## Sau phiên

- Điểm ghi thêm vào `~/AudioLab/review/dragon-hold/ratings.jsonl`.
- Claude chạy `bash tools/audio-lab/run.sh critic agreement --batch 1c` để đo bản hiệu chỉnh 1 trên dữ liệu mới, và thử luật L2 Q6 đề xuất (có và không có `owner-v2`).
- Rồi chốt bản gốc của từng id, làm lượt biến thể, bù mức to bằng `gainDb` khi đưa vào game: chỉ còn bom (−24,4 LUFS-M). `fire.impact.a`, `.b` nay đạt −20 sau khi thân được cân mức (Q6_REWRITE 13.1).
- Bản dựng trong bối cảnh và số đo: `~/AudioLab/work/_batch1c/b1c/dragon-hold/context/`.
