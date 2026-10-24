# Lô 1 · Rồng Giữ Ải: hai phiên nghe (S2, S3)

Khoảng **35–40 phút** cho cả hai phiên, mỗi phiên dưới 20 phút. Thiết kế: [`BATCH1_BRIEF.md`](BATCH1_BRIEF.md) mục 4.2, 4.4 và 7. Báo cáo của máy (chỉ đọc sau khi chấm): `~/AudioLab/work/_batch1/dragon-hold/b1/REPORT.md`.

Không có gì ở đây được đưa vào game. Mọi bản nằm trong `~/AudioLab`.

## Mở

```bash
pnpm audio:board --game dragon-hold --batch 1 --open
```

Hai phiên: **`1-dh-s2`** (trận đánh) và **`1-dh-s3`** (nền và tù và). Mỗi phiên có thêm 4 cặp mốc lấy từ lô 0a, 0b (anh không cần biết cặp nào). Thẻ ảnh chỉ mở khi chấm xong cả phiên.

## Mới ở lô này

- **Bối cảnh "Trong trận thô"** (phím `↑` `↓`): mỗi bản được dựng sẵn trong một đoạn trận ngắn, qua bộ trộn giống game (mức bus, hạ tiếng khi đọc từ, vang rừng, bộ giới hạn), có giọng đọc từ tiếng Anh của macOS. Bản dựng của một id chỉ khác nhau ở đúng bản đang chấm. Bảng phát nguyên bản dựng, không lặp.
  - Trận đánh: gõ xong một từ mỗi 1,5 s → Hỏa Long khạc lửa cùng lúc với giọng đọc → cầu lửa rơi 0,6 s sau (lượt a, b, đòn to c).
  - Tiếng tru: bầy thú kéo tới, tru hai lần, vài từ có cầu lửa.
  - Bom Hạt Thông: bầy lạo xạo, bốn từ, bom nổ hai lần.
  - Nền và tù và: 18 s, nền rừng ba vòng, suối, tù và báo đợt, bầy và thú kéo vào, tù và tướng, rồi bốn từ có cầu lửa.
- **Nhãn mới "ngắt quãng"** (phím `J`): âm phát dày mà nghe rời từng phát, không liền.

## Nghe gì

| Phiên | Id | Bối cảnh mở đầu | Câu hỏi |
|---|---|---|---|
| **S2** | `fire.cast` (3 bản) | Trong trận thô | Hai hướng: phụt lửa tròn, và khạc có hơi thở. Có nghe ra rồng khạc lửa không? Giọng đọc từ có bị che không (nhãn "khó nghe tiếng đọc")? |
| | `fire.impact.a` (3) | Trong trận thô | Âm gốc của họ cầu lửa: phụt trầm, thân tròn, lách tách nhỏ. Lặp 20 lần có mệt không? |
| | `fire.impact.b` (2) | Trong trận thô | Tối hơn .a, lách tách khô. Cùng họ mà phân biệt được không? |
| | `fire.impact.c` (2) | Trong trận thô | Đòn to: dài và nặng hơn .a rõ, không có tiếng nổ thứ hai |
| | `enemy.quadruped.howl` (4) | Trong trận thô | Trọn một tiếng tru. Các bản ghi sẵn nhãn "bị luật chặn" là chủ ý; chấm như mọi bản. Cuối tiếng tru có tiếng rít không? |
| | `trap.pine-bomb.trigger` (3) | Một mình | Nổ trầm, hạt văng. Thử "Loa nhỏ" |
| **S3** | `amb.forest` (4) | Lặp (3 vòng) | Gió qua rừng thông. Nghe đủ 3 vòng: mệt tai không, nhận ra chỗ nối hay một đoạn dâng lên lặp lại không? Một bản có thêm lớp ù trầm nhỏ |
| | `amb.river` (3) | Lặp | Suối: có tiếng bong bóng nào có cao độ lặp lại mỗi vòng không? |
| | `enemy.swarm.march` (3) | Lặp | Bầy lạo xạo: đều hay thành từng đợt? |
| | `enemy.quadruped.march` (4) | Lặp | Vó thú: nhịp có đều qua chỗ nối không, có "vó đôi" ở chỗ nối không? |
| | `wave.horn` (3) | Một mình | Cùng hai kèn co Rê–La, khác hình câu |
| | `general.g01.horn` (3) | Một mình | Trầm hơn tù và báo đợt, mở dần, gỗ và rêu, đáng sợ |

## Thiết bị

- Nghe cả hai phiên bằng **tai nghe** (hộp đầu phiên: phím `1`). Rồi nếu còn thời gian, mở lại S2 bằng loa (`2`) chỉ cho `fire.cast` và `trap.pine-bomb.trigger`.
- Chỉnh âm lượng máy ở id đầu, giữ nguyên tới hết.
- Nghe thấy lỗi thì gắn **"rè/lỗi"** (`R`): dữ liệu này chỉnh bộ dò lỗi của máy.

## Sau phiên

Điểm ghi thêm vào `~/AudioLab/review/dragon-hold/ratings.jsonl`. Claude chạy `bash tools/audio-lab/run.sh critic agreement` để đo bản hiệu chỉnh 1 trên dữ liệu mới, chốt bản gốc của từng id và làm lượt biến thể.
