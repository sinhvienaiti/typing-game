# Lô 1 · Tuyến Cuối: hai phiên nghe (S1, S4)

Khoảng **35 phút** cho cả hai phiên, mỗi phiên dưới 20 phút. Thiết kế: [`BATCH1_BRIEF.md`](BATCH1_BRIEF.md) mục 3, 4.1 và 7. Báo cáo của máy (chỉ đọc sau khi chấm): `~/AudioLab/work/_batch1/typing-survival/b1/REPORT.md`.

Không có gì ở đây được đưa vào game. Mọi bản nằm trong `~/AudioLab`.

## Mở

```bash
pnpm audio:board --game typing-survival --batch 1 --open
```

Hai phiên: **`1-ts-s1`** (súng và trúng) và **`1-ts-s4`** (hạ quái, nạp đạn, Tia, báo nguy). Mỗi phiên có thêm 4 cặp mốc lấy từ lô 0a, 0b (anh không cần biết cặp nào). Thẻ ảnh chỉ mở khi chấm xong cả phiên.

## Mới ở lô này

- **Bối cảnh "Liên thanh 3 s"** (phím `↑` `↓`, mở đầu ở hầu hết các id): một đoạn trận 3–4 s dựng sẵn qua bộ trộn giống game (mức bus, bộ nén, hạ tiếng khi đọc từ), có giọng đọc từ tiếng Anh của macOS. Súng Xung bắn 10 viên mỗi giây, mỗi viên trúng 150–300 ms sau, hai từ được gõ xong (nạp đạn, rồi giọng đọc), một đòn lớn, rồi ngừng bắn. Các bản dựng của một id chỉ khác nhau ở đúng bản đang chấm. Bảng phát nguyên bản dựng, không lặp.
  - Súng, nền, đuôi, các bậc trúng: cảnh súng bắn liên tục.
  - Hạ quái, nạp đạn: như trên, thêm quái bầy vỡ, một lính tinh nhuệ nổ, từ thứ hai gõ chuẩn.
  - Tia: Tia chạy 2,5 s, mỗi nhịp 0,1 s chích một lần.
  - Báo nguy (`hurt.breach`): bối cảnh "Trong trận thô", súng đang bắn thì tuyến bị phá.
- **Nhãn "ngắt quãng"** (phím `J`): âm phát dày mà nghe rời từng phát, không liền. Đây là nhãn quan trọng nhất của lô này, vì nó trả lời đúng ghi chú của anh ở lô 0a.

## Nghe gì

| Phiên | Id | Bối cảnh mở đầu | Câu hỏi |
|---|---|---|---|
| **S1** | `gun.xung` (4 bản) | Liên thanh 3 s | Mỗi bản là một bộ phát đơn (bộ nặng và bộ nhẹ xen nhau) phát mọi viên, có nền cơ khí và đuôi khi ngừng. Có nghe thành **một loạt liền, có lực** không, hay vẫn rời từng phát? Hai bản ghi sẵn "chỉ khác mức nền": cùng phát đơn, một bản nền nhỏ, một bản nền to; chọn nền rõ tới đâu. Một bản ghi "Cách game đang phát": bản 4/5 của anh ở lô 0a, phát đúng như game hôm nay |
| | `gun.xung.loop` (3) | Lặp (3 vòng) | Nền chạy suốt loạt bắn. Không được có nhịp riêng hay tiếng nổi lên. Một bản ghi sẵn cờ "dấu vòng lặp" của máy: nghe xem có nhận ra không |
| | `gun.xung.tail` (3) | Liên thanh 3 s | Khi ngừng bắn: có nghe như bị cắt không, có ra vang thép không, hay chỉ là tiếng xì, tiếng ầm? |
| | `hit.t1` (4) | Liên thanh 3 s | Đạn trúng vỏ thép, tới 10 lần mỗi giây. Sáng, gọn, không che tiếng súng. Giọng đọc từ có bị che không (nhãn "khó nghe tiếng đọc")? |
| | `hit.t2` (4) | Liên thanh 3 s | Chí mạng: nặng hơn hit.t1, có cú thụi trầm (đã ghép sẵn sub). Có "gõ đúp" không? |
| | `hit.sub` (2) | Một mình | Hai bản sub dưới cùng một tiếng chí mạng. Thử "Loa nhỏ" |
| | `hit.t4` (3) | Liên thanh 3 s | Đòn lớn đã ghép đủ lớp. To và dài hơn hit.t2 rõ chưa? Có ra thép dầm ngân không? |
| | `hit.tail` (2) | Một mình | Hai đuôi kim loại dưới cùng một cú đòn lớn. Hai bản rất gần nhau; không nghe ra khác biệt thì chấm bằng nhau |
| **S4** | `kill.swarm` (4) | Liên thanh 3 s | Bầy quái kim loại vỡ, hàng trăm lần mỗi trận. Hai hướng: vỡ khô, và vỡ có vang (sáng hơn nhiều). Có chói, có mỏng không? |
| | `kill.elite` (3) | Liên thanh 3 s | Lính tinh nhuệ nổ. Đuôi có bị cụt đột ngột không? |
| | `word.load` (3) | Liên thanh 3 s | Gõ xong một từ: "cạch-chắc". Giọng đọc ngay sau có rõ không? |
| | `word.perfect` (2) | Liên thanh 3 s | Từ gõ chuẩn: nạp đạn cộng tiếng rít và tia lửa. Một bản rít trầm nghe rõ, một bản rít cao rất mờ |
| | `gun.tia.pulse` (3) | Liên thanh 3 s | Tia điện chích mỗi 0,1 s. Hiện chưa có nền ù cho Tia, nên chắc chắn sẽ rời rạc: chấm chất tiếng chích; gắn "ngắt quãng" nếu anh muốn Tia có nền |
| | `hurt.breach` (3) | Trong trận thô | Báo nguy: cú đập thép, nổ trầm, còi hai nốt. Có đủ rõ để biết tuyến vừa bị phá không, hay quá đục? |

## Thiết bị

- Nghe **S1 bằng tai nghe** (hộp đầu phiên: phím `1`), rồi mở lại S1 bằng **loa** (`2`) chỉ cho `gun.xung`: lực của súng phải nghe được trên loa nhỏ.
- **S4 bằng tai nghe.**
- Chỉnh âm lượng máy ở id đầu, giữ nguyên tới hết.
- Nghe thấy lỗi thì gắn **"rè/lỗi"** (`R`): dữ liệu này chỉnh bộ dò lỗi của máy.

## Sau phiên

Điểm ghi thêm vào `~/AudioLab/review/typing-survival/ratings.jsonl`. Claude chạy `bash tools/audio-lab/run.sh critic agreement` để đo bản hiệu chỉnh 1 trên dữ liệu mới, chốt hướng súng (mức nền), bản gốc của từng id và làm lượt biến thể.
