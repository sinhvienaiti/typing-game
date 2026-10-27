# Lô 0a: phiên nghe đầu tiên của chủ dự án

Khoảng **20 phút**, 13 id (35 bản) trong 4 phiên ngắn. Đây là lần đầu tai của anh được ghi thành dữ liệu cho Audio Lab (mục 4.6, 7 và 12 của [`AUDIO_PIPELINE.md`](../../docs/games/AUDIO_PIPELINE.md)).

Mọi âm trong lô này làm từ thư viện CC0 (Kenney, VCSL, VSCO-2-CE), âm tổng hợp bằng mã và bộ phát mẫu Python. **Chưa có âm nào do Stable Audio 3 tạo**, vì mô hình đó còn chờ bước 0 của anh (mục 10.1). Không có gì ở đây được đưa vào game.

## Mở bằng một lệnh

Từ thư mục gốc `typing-game`:

```bash
pnpm audio:board --batch 0a --open
```

- Trình duyệt mở `http://127.0.0.1:3191/`. Nếu cổng 3191 đang bận, bảng dùng 3192 và in rõ địa chỉ trong terminal.
- Trang chạy hoàn toàn trên máy, không cần mạng, không gửi gì ra ngoài.
- Nghe xong thì bấm `Ctrl+C` trong terminal để tắt.

## Trước khi nghe

- Dùng **tai nghe** nếu có. Ở hộp đầu mỗi phiên, bấm `1` (tai nghe) hoặc `2` (loa).
- Chỉnh âm lượng máy cho dễ chịu ở id đầu tiên, rồi **giữ nguyên** đến hết.
- Mọi bản trong một id đã được cân cùng độ to, nên bản nào nghe "to hơn" không có lợi thế. Với cặp có đầu tiếng rất khác (cồng nở chậm, kẻng đanh), bảng cân theo cả độ to 100 ms đầu.
- Vài id phát nhỏ hơn mức chung (ví dụ `ui-move`, `hit.t1`) vì không được vượt đỉnh. Mô tả của id đó ghi rõ; anh đừng chỉnh âm lượng máy và đừng gắn "quá nhỏ" vì lý do này.
- Nhãn A, B, C xếp ngẫu nhiên. Tên file, nguồn, định dạng file và điểm máy bị giấu.
- **Thẻ ảnh và số đo chỉ mở khi anh chấm xong cả phiên**, không mở sau từng id: số đo của máy hiện giữa chừng sẽ dẫn tai ở các id sau. Chấm xong id cuối, bấm `⌫` để quay lại xem từng id.

## Nghe gì

Bốn phiên, mở theo thứ tự nào cũng được. Mỗi id khoảng 1,5 phút.

| Phiên | Id | Câu hỏi cho tai anh |
|---|---|---|
| **Tuyến Cuối** · hướng âm | `gun.xung` | Súng xung, phát 5 lần mỗi giây: bản nào ra "pháo thép nặng", bản nào nghe như đồ chơi? Nghe ở "Lặp 20 lần" |
| | `hit.t1` | Đạn trúng nhẹ: có ra tiếng keng trên vỏ thép không, hay giống tiếng vỗ tay, tiếng phím? |
| | `hit.t2` | Chí mạng: nặng hơn `hit.t1` rõ chưa, có cú thụi trầm không? |
| **Rồng Giữ Ải** · hướng âm | `fire.impact.a` | Cầu lửa trúng: có ra "phụt lửa trầm" không, hay chỉ là tiếng gõ? Lửa lách tách có thừa không? |
| | `trap.pine-bomb.trigger` | Bom Hạt Thông: nổ có lực không, hạt văng có nghe ra không? Thử thêm "Loa nhỏ" |
| | `wave.horn` | Tù và báo đợt, ba bản cùng một tiếng trống khung VCSL: hai kèn co Rê–La, trombone tenor trầm hơn một quãng tám, và kèn co trên trombone. Bản nào hợp rừng thần thoại? Cả ba đã qua chuỗi cuối (mono, 2,2 s) như bản sẽ vào game |
| **Lời Gọi** · hướng âm và nguồn nhạc cụ | `word-hit` | Nốt đàn tranh sau mỗi từ. Ba bản khác nhau ở **quãng tám** và **lối ngân**. Đây là câu hỏi mục 16 #4 (giữ C5–C6 hay hạ xuống C4–C5) |
| | `ui-pick` | Phách gỗ rồi chuông đồng nhỏ (VCSL Hand Chimes, không dùng chuông chùa). Ba bản khác nhau ở nốt chuông |
| | `ui-move` | Chạm rất nhẹ lên tre. Ba loại gỗ: loại nào ra "tre" nhất? |
| | `leak` | Báo quái lọt Lũy: **cồng hội làng** hay **kẻng sắt**? Đây là câu hỏi mục 16 #5 về nguồn cồng |
| **Hiệu chỉnh** · chỗ các lớp tai AI không đồng ý | `calib-1`, `calib-2`, `calib-3` | Mỗi id có một âm gốc và vài bản đã bị làm hỏng có chủ ý; tên id được làm trung tính để không lộ nguồn. Các lớp chấm của máy không thống nhất bản nào tốt nhất. Cứ chấm theo tai, không cần đoán bản nào bị hỏng |

## Cách chấm, chỉ bằng phím

| Phím | Việc |
|---|---|
| `Space` | Phát hoặc dừng bản đang chọn |
| `1`, `2`, `3` | Chọn bản A, B, C và phát |
| `←` `→` | Chọn bản trước hoặc sau, **không phát** (tiện khi đang ở bối cảnh Lặp, khỏi nghe lại cả vòng) |
| `⇧1` … `⇧5` | Cho 1–5 sao bản đang chọn |
| `V` | Đánh dấu bản tốt nhất (không bấm thì bản nhiều sao nhất được chọn) |
| `0` | Không bản nào đạt |
| `H` `G` `C` `D` `R` `Y` `K` `T` `N` `M` `S` `L` `P` `E` `O` | Nhãn: hay, hợp game, chói, đục, rè/lỗi, yếu/mỏng, quá dài, quá to, quá nhỏ, chậm, sai chất liệu, lạc thể loại, nhàm khi lặp, rẻ tiền, khó nghe tiếng đọc |
| `↑` `↓` | Đổi bối cảnh: Một mình, Lặp (đúng nhịp chơi: 20 lần, hoặc 8 lần với âm phát thưa như `word-hit`, `leak`, `wave.horn`), Loa nhỏ (lọc cao 200 Hz) |
| `/` | Ghi chú ngắn (gõ tiếng Việt được, `Enter` để lưu, `Esc` để thoát ô ghi chú) |
| `Enter` | Lưu. `Enter` lần nữa sang id tiếp |
| `⇧Enter` | Sang id tiếp mà không lưu |
| `⌫` | Quay lại id trước |
| `I` | Phóng to thẻ ảnh và xem đủ số đo (khi thẻ đã mở) |
| `Esc` | Dừng phát, đóng cửa sổ |
| `?` | Bảng phím |

Nhãn quan trọng nhất ở lô này là **rè/lỗi**, **yếu/mỏng**, **sai chất liệu** và **lạc thể loại**: chúng chỉnh trực tiếp bộ dò lỗi và cách máy xếp hạng.

## Mất bao lâu

- 13 id, 35 bản, mỗi id khoảng 1,5 phút: tổng khoảng 20 phút. Riêng phần âm thanh, nghe mỗi bản một lần ở bối cảnh mặc định mất khoảng 5 phút; nghe cả Lặp lẫn Một mình mất khoảng 7 phút. Phần còn lại là thời gian so và chấm.
- Mỗi phiên có đồng hồ và giới hạn 20 phút để tai không mỏi.
- Dừng giữa chừng được. Mở lại bằng đúng lệnh trên, bảng làm tiếp từ chỗ đã dừng.

## Điểm của anh đi đâu, dùng làm gì

- Mỗi lần lưu thêm một dòng vào `~/AudioLab/review/<game>/ratings.jsonl` (`dragon-hold`, `typing-defense`, `typing-survival`, và `_calib` cho phiên hiệu chỉnh). File chỉ ghi thêm, không sửa dòng cũ. Nó nằm ngoài repo; người điều phối chép sang `games/<game>/art-src/audio/review/ratings.jsonl` khi được ghi vào game (mục 11).
- Vai trò của từng bản (bản máy xếp đầu, bản khác nhất, bản dò máy xếp thấp) chỉ ghi trong file, không hiện trên trang.
- Sau phiên, Claude đọc file điểm và:
  1. **Chốt hướng âm** cho từng game: gốc prompt và công thức của lô 1 (mục 5.2).
  2. **Ghi hai quyết định** cần anh duyệt: quãng tám của `word-hit` và nguồn cồng/kẻng của `leak` (mục 16 #4, #5).
  3. **So tai anh với máy.** Ở lô 0, audiobox (L3) chấm bản "mỏng" cao nhất ở 6/8 nhóm của bộ hiệu chỉnh, còn luật đo (L2) chọn bản gốc ở 6/8 nhóm. Ba id `calib-*` của phiên chính chỉ là ba chỗ hai lớp bất đồng, được chọn có chủ đích, nên **không đủ để quyết trọng số audiobox**. Quyết định đó cần cả 8 nhóm của phần thêm `0a-them` (bên dưới). Khi đã có, nếu anh chọn bản gốc thì audiobox giữ trọng số thấp; nếu không, luật đo được chỉnh lại (mục 4.5, 4.6).
  4. **Chỉnh bộ dò lỗi L1b** bằng các nhãn "rè/lỗi".
  5. Âm anh chấm từ 4 sao và chọn là bản tốt nhất trở thành **âm tham chiếu** đầu tiên cho lớp L5.

## Phần thêm (khoảng 10–15 phút, cần cho quyết định trọng số audiobox)

Bộ hiệu chỉnh đầy đủ của kế hoạch (mục 4.6, lô 0a): 8 âm gốc, mỗi âm kèm 3 bản làm hỏng (clip, đục, mỏng), và 8 âm Kenney đứng riêng. Thẻ ảnh cũng chỉ mở khi chấm xong phiên. Mở khi có thời gian:

```bash
pnpm audio:board --batch 0a-them --open
```

## Nếu có trục trặc

- **Không nghe thấy gì:** bấm chuột vào trang một lần (trình duyệt cần một thao tác để bật âm), rồi kiểm âm lượng máy.
- **Báo cổng bận:** bảng tự dùng 3192; mở địa chỉ được in trong terminal.
- **Kiểm file phiên:** `pnpm audio:board check`.
- Phiên được tạo lại bằng `pnpm audio:batch0 session --run batch0-2026-10-23-r2 --force`. Không có `--force` thì lệnh từ chối ghi đè phiên đã có. Điểm đã chấm không bị xóa, nhưng phiên mới có thể khác thứ tự; đừng tạo lại khi đang chấm dở.
