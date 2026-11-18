# Lô 1 · Lời Gọi: hai phiên nghe (S5, S6)

Khoảng **30 phút** cho cả hai phiên: S5 chừng 20 phút, S6 chừng 10 phút. Thiết kế: [`BATCH1_BRIEF.md`](BATCH1_BRIEF.md) mục 4.3, 4.4 và 7. Báo cáo của máy (chỉ đọc sau khi chấm): `~/AudioLab/work/_batch1/typing-defense/b1/REPORT.md`.

Không có gì ở đây được đưa vào game. Mọi bản nằm trong `~/AudioLab`.

## Mở

```bash
pnpm audio:board --game typing-defense --batch 1 --open
```

Hai phiên: **`1-td-s5`** (chuỗi từ và trận) và **`1-td-s6`** (báo nguy, lời gọi, UI). Mỗi phiên có thêm 4 cặp mốc lấy từ lô 0a, 0b (anh không cần biết cặp nào). Thẻ ảnh chỉ mở khi chấm xong cả phiên.

## Mới ở lô này

- **Bối cảnh "Trong trận thô"** (phím `↑` `↓`): mỗi bản được dựng sẵn trong một đoạn trận ngắn, qua bộ trộn giống mã âm hiện tại của Lời Gọi (bus typing có bộ nén, bus world, vang làng 0,8 s, bộ giới hạn master), có giọng đọc từ tiếng Anh của macOS. Các bản dựng của một id chỉ khác nhau ở đúng bản đang chấm. Bảng phát nguyên bản dựng, không lặp.
  - **Chuỗi từ** (11,6 s): gõ 7 từ, mỗi 1,5 s, có tiếng phím; nốt đàn tranh leo thang A3 (từ ẩu), C4, D4, F4 (Hoàn hảo, thêm chuông), G4, A4, C5 (Chớp: vuốt lên, thêm chuông); mỗi từ bắn một Phát Chữ; ba tháp cung, hai tháp pháo, Mực Câm tan, xu rơi. Tên, mực, xu phát theo cách đề xuất cho bước nối vào game: đều nhịp, không thành từng cụm rồi im.
  - **Cảnh đêm** (9 s): năm từ, hai tháp cung, lời gọi Chặt sáng hai lần, quái lọt Lũy hai lần (một lần giữa hai từ, một lần trùng một từ).
  - **Màn đầu** (4,2 s): lướt menu năm bước rồi chọn, hai lượt.
- **Nhãn "ngắt quãng"** (phím `J`): âm phát dày mà nghe rời từng tiếng.
- Lời Gọi hiện chỉ hạ nhạc khi đọc từ, không hạ tiếng hiệu ứng, nên trong "Trong trận thô" giọng đọc có lúc bị che. Đó là cách game đang trộn, không phải lỗi của bản. Nếu một bản làm giọng khó nghe hơn các bản khác, gắn **"khó nghe tiếng đọc"** (`O`).

## Nghe gì

| Phiên | Id | Bối cảnh mở đầu | Câu hỏi |
|---|---|---|---|
| **S5** | `word-hit` (3 bản) | Trong trận thô | Ba hướng của cùng thang 7 nốt đàn tranh (hạ một quãng tám như anh đã chọn): gảy như bản 0a, gảy mềm ấm, gảy có ánh dây thép trên cao. "Một mình" và "Lặp" chỉ phát nốt C4; nghe cả thang ở "Trong trận thô". Có ra đàn tranh Việt không? |
| | `word-hit-bell` (3) | Trong trận thô | Chuông khi Hoàn hảo, Chớp: hai nốt chuông tay nhỏ và một chuông ống. Có hợp làng tre không, có gợi chuông chùa hay chuông nhà thờ không? |
| | `wordshot-fire` (4) | Trong trận thô | Phát Chữ bay ra: vút nhanh, giấy, tre. Bản ghi sẵn nhãn "bị luật chặn" là tiếng vút lên chậm; chấm như mọi bản |
| | `arrow-fire` (3) | Trong trận thô | Tháp Cung bắn, tới 4 lần mỗi giây. Hai hướng: dây ngân, và bật dây trầm. Có gắt, có che giọng không? |
| | `ink-puff` (3) | Trong trận thô | Mực Câm tan, tới 8 lần mỗi giây. Hai hướng: túi giấy ướt bục, và phụt khói. Dày như trong trận có thành tiếng rè không? |
| | `blast` (3) | Trong trận thô | Tháp Pháo nổ: trống đầm và giấy tung. Một bản là âm Stable Audio 3 nguyên khối. Có ra trống taiko hay nổ lách tách không? Thử "Loa nhỏ" |
| | `coin` (2) | Trong trận thô | Đồng xu rơi: chuông ngân rất cao, hay chuông tắt nhanh? Có nhàm, có che giọng không? |
| **S6** | `leak` (4) | Một mình | Kẻng báo quái lọt Lũy, bản cuối. Một bản là bản 0a anh đã chấm 4/5. Bản cuối không được kém 4/5 |
| | `call-chop` (4) | Một mình | Lời gọi Chặt: gõ gỗ trầm, chắc vào thân tre. Nghe ra mõ chùa thì gắn **"sai chất liệu"** (`S`). Có bản nào nghe như gõ đúp không? |
| | `ui-move` (4) | Một mình | Chuyển mục: chạm rất nhẹ lên trống khe. Một bản là bản 0a anh đã chọn |
| | `ui-pick` (3) | Một mình | Chọn mục: phách gỗ rồi chuông tay A5. Chuông to, nhỏ hay như bản 0a? Văn hóa: chuông này có gợi chùa không? |

## Thiết bị

- Phiên **S5** nghe bằng **tai nghe** (hộp đầu phiên: phím `1`).
- Phiên **S6** nghe bằng **loa** (phím `2`), như người chơi trên laptop.
- Chỉnh âm lượng máy ở id đầu, giữ nguyên tới hết. Bối cảnh "Trong trận thô" của `ui-move`, `ui-pick` nhỏ hơn các id khác: UI vốn nhỏ hơn phím.
- Nghe thấy lỗi thì gắn **"rè/lỗi"** (`R`): dữ liệu này chỉnh bộ dò lỗi của máy.

## Sau phiên

Điểm ghi thêm vào `~/AudioLab/review/typing-defense/ratings.jsonl`. Claude chạy `bash tools/audio-lab/run.sh critic agreement` để đo bản hiệu chỉnh 1 trên dữ liệu mới, chốt bản gốc của từng id và làm lượt biến thể.
