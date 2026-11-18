# Việc: tiếng hô kỹ năng bằng Firefly Generate Speech (05/11)

**Mục tiêu.** Làm 4 câu hô, mỗi câu 3 take, trước khi tài khoản Firefly hết hạn (khoảng 23:00 ngày 05/11).

**Đã chốt.** Anh duyệt cả bốn câu (`DECISIONS.md`, 05/11 01:05):

| id | Câu | Dùng cho |
|---|---|---|
| `callout-k1` | Sword Qi, Strike! | phím 1 |
| `callout-dash` | Flash Step! | lướt |
| `callout-ult` | Milky-Way Sword Rain! | tối thượng |
| `callout-twin` | Twin Dragons, Seize the Pearl! | Song Long |

**Cách làm**
- **Công cụ:** Firefly Generate Speech, model `tts-model-firefly-dnt`. Đây là giọng của Adobe, không phải đối tác.
- **Giọng:** Brittney (anh chọn), cao độ High, tốc độ 1.1x. Nếu trang có mục cảm xúc hay nhấn giọng, chọn kiểu mạnh mẽ, hào hùng.
- **Tab:** chỉ dùng **tab-2** (`firefly.adobe.com`). **Không chạm tab-3**, vì bộ chạy video đang làm việc ở đó.
- **Lưu file:**
  - nơi lưu: `games/immortality-cultivation/art-src/lab/firefly-sprint-2026-11-05/callouts/<id>/take<N>.<đuôi gốc>`;
  - kèm `take<N>.prompt.txt` ghi câu, giọng, cài đặt, giờ tạo và credit nếu trang có hiện;
  - cách gửi file ra: dùng lại máy nhận local của hàng âm (`typing-game-review/captures/tu-tien/firefly-sprint-sound/tools/`, cổng 8791) hoặc một bản sao của nó. Không ghi đè media.
- **Gặp hộp đăng nhập, trả tiền, điều khoản hay đồng ý:** dừng ngay và báo. Không bấm gì trong hộp đó.

**Số nghiệm thu.**
- Đủ 12 file, mỗi file đọc đúng câu của mình. Kiểm bằng độ dài, mức âm và chuyển giọng nói thành chữ nếu có công cụ local; agent không nghe được.
- Ghi credit mỗi lần tạo.

**Giới hạn.** Tối đa khoảng 60 bước. Trả về tối đa 10 dòng.

## Nhật ký
- 01:04 Máy nhận riêng `typing-game-review/captures/tu-tien/firefly-sprint-callouts/tools/callout-recv.py` chạy ở cổng 8792 (bản sao của máy nhận hàng âm, chỉ nhận tên `callout-*`, không ghi đè).
- 01:07 Trang Generate Speech ở tab-2: model Firefly Speech (Adobe), giọng Brittney (voiceId v150), tốc độ 1.1x, cao độ High (pitch_shift 1, thang -3..3). Trang không có mục cảm xúc hay nhấn giọng (chỉ có chèn khoảng lặng và mẹo). Mỗi lần tạo: 1 credit (bảng giá `text_to_speech_v2`), ra 1 file WAV 48 kHz mono.
- 01:07 `callout-k1/take1.wav` đã lưu (2,00 s, 1 credit).
- 01:09 `callout-k1/take2.wav`, `take3.wav` đã lưu (mỗi file 2,00 s, 1 credit; ba take khác nhau theo md5). Muốn tạo lại cùng câu phải sửa chữ rồi trả lại để nút Generate Again sáng.
- 01:12 `callout-dash/take1..3.wav` đã lưu (mỗi file 1,55 s, 1 credit). Một lần bấm hụt ô chữ nên không tạo, không mất credit.
- 01:14 `callout-ult/take1..3.wav` đã lưu (mỗi file 2,03 s, 1 credit).
- 01:16 `callout-twin/take1..3.wav` đã lưu (mỗi file 2,45 s, 1 credit).
- 01:17 Kiểm 12 file: đủ 12 WAV 48 kHz mono + 12 `take<N>.prompt.txt`; 12 md5 khác nhau; câu gửi đi trong request khớp đúng id; đỉnh -5,3 đến -8,9 dBFS, trung bình -18,8 đến -24,7 dB; tiếng nói dài khoảng 0,85 s (dash), 1,25 s (k1), 1,5 s (ult), 1,9 s (twin), hợp với số âm tiết; các take cùng câu có độ dài file bằng nhau (Firefly cố định độ dài theo chữ). Máy không có công cụ chuyển giọng nói thành chữ (không có whisper), nên chưa kiểm được lời đọc; cần người nghe. Tổng 12 credit, không gặp hộp đăng nhập, trả tiền hay điều khoản. Đã tắt máy nhận cổng 8792 (chạy lại: `/usr/bin/python3 -I callout-recv.py` trong thư mục tools).

## Đợt 2 (05/11 tối, chờ anh duyệt câu): tuyệt kỹ hệ, cột trụ, nhát cuối vũ khí
Giọng Brittney như đợt 1, mỗi câu 3 take, 1 credit mỗi take.

| id | Câu | Dùng cho |
|---|---|---|
| `callout-ult-metal` | Heavenly Geng, Every Edge Strike! | tuyệt kỹ Kim |
| `callout-ult-wood` | Primordial Tree, Descend! | tuyệt kỹ Mộc |
| `callout-ult-water` | Profound Sea, Open! | tuyệt kỹ Thủy |
| `callout-ult-fire` | One Spark, Burn the Heavens! | tuyệt kỹ Hỏa |
| `callout-ult-earth` | Ten Thousand Peaks, Rise! | tuyệt kỹ Thổ |
| `callout-ult-thunder` | Nine Heavens, Thunder Edict! | tuyệt kỹ Lôi |
| `callout-ult-wind` | Firmament, Become the Storm! | tuyệt kỹ Phong |
| `callout-ult-ice` | Cold Heaven, Be Still. | tuyệt kỹ Băng (giọng lặng) |
| `callout-ult-dark` | Endless Night, Devour! | tuyệt kỹ Ám |
| `callout-ult-light` | Heaven's Light, Judge Them! | tuyệt kỹ Quang |
| `callout-ult-poison` | Myriad Venoms, Bloom! | tuyệt kỹ Độc |
| `callout-ult-blood` | Blood Moon, Rise! | tuyệt kỹ Huyết |
| `callout-ult-void` | Void, Shatter the Realm! | tuyệt kỹ Không gian |
| `callout-ult-star` | Nine Stars, Fall! | tuyệt kỹ Tinh tú |
| `callout-pillar-thunder` | Thunder Pillar, Strike! | cột sét |
| `callout-pillar-light` | Light of Judgement! | cột sáng |
| `callout-pillar-meteor` | Meteor, Fall! | thiên thạch lửa |
| `callout-edict` | Myriad Edges, Heed the Edict! | Kiếm phím 7 |
| `callout-sabre-final` | Heaven-Tilting Sever! | nhát cuối Đao |
| `callout-spear-final` | One Spear, Seal the Gate! | nhát cuối Thương |
