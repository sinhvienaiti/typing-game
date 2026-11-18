# Chiêu rồng (dragon skill): ba hướng cho anh chọn, 04/11/2026

**Quyết định mới của anh (04/11/2026, khoảng 11:50):** "tôi nghĩ việc 2 rồng chạy lên cổng là k hợp lý, vì chúng ta đang build skill cố gắng dùng chung, map sau này k phải chỉ có hướng về 2 cổng, nên skill phải áp dụng được ở nhiều map chứ k phải là đi về 2 cổng, nó nên dạng skill diện rộng toàn map thì hợp lý hơn".
- Song Long giữ ý hai rồng và một viên ngọc, nhưng phải là **chiêu diện rộng toàn sân, không phụ thuộc map**: không dựa vào số cổng hay hình đường đi của một map cụ thể.
- Hộp xám hiện tại (rồng chạy theo hai hành lang tới hai cổng, §8) chỉ còn là bằng chứng đo. Thiết kế lại ở §9 (04/11 tối: đã chốt, anh duyệt ba quyết định ở §9.11; mã sau cờ là phiếu Codex 271, đã merge, và phiếu bot 272).

**Trạng thái trước đó:** anh đã chọn **A · Twin Dragons, One Burning Pearl** (04/11/2026, sáng: "A · Song Long"). Bước tiếp theo là hộp xám trong lab và đo bằng bot (§6 bước 1). Số canon chưa đổi; B và C để lại cho bộ chiêu Thủy và phần tuyệt kỹ.

**Xem nhanh** (không vào Git):
- Bảng hình ba hướng: `games/immortality-cultivation/tmp/shots/dragon/directions-board.jpg` (3 hàng × 3 ảnh, có tên hướng).
- Từng ảnh, kèm prompt nguyên văn: `games/immortality-cultivation/art-src/lab/vfx/dragon/<direction-id>-c<k>.png` và `.prompt.txt`.

**Nghiên cứu nguyên văn và bảng kiểm nguồn:** [`source/dragon-skill-chatgpt.md`](source/dragon-skill-chatgpt.md) (ChatGPT, Chat, thinking High) và [`source/dragon-skill-gemini.md`](source/dragon-skill-gemini.md) (Gemini Argon, mức Cao). Mỗi bên hai lượt: cùng một đề bài, rồi nhận ý chính của bên kia để bổ sung.

**Việc anh giao (04/11):** khi bị chặn ở việc khác thì làm hiệu ứng hệ và chiêu thật đẹp, ví dụ một chiêu rồng lấy từ các chiêu rồng nổi tiếng của Trung Quốc; dùng ChatGPT và Gemini cùng tìm lời giải đạt chuẩn; ưu tiên Firefly hoặc Blender ở mọi chỗ chúng đẹp hơn mã ("luôn ưu tiên dùng blender hoặc fire[fly] nếu 2 thứ này làm tốt hơn bạn"); hình phải cuốn hút, rực rỡ, kiểu anime, donghua và thần thoại, không lấy cái thật làm đích.

**Luật áp dụng:** canon [`00-canon.md`](../00-canon.md) D56 (anime và thần thoại), D58 (ra chiêu tức thì, chiêu diện rộng, hiệu ứng màn hình theo bậc, cảnh cận tuyệt kỹ sau đòn đầu, tiếng hô), D59 (vũ khí cho hình, hệ cho chất); skill `game-vfx-production` (art trước, mã chỉ đặt và hoạt hình), `game-vfx-layered` (năm pha, phía người ra chiêu trước, đánh nhanh tắt chậm, mọi hình đều lấp lánh); [`SKILL_REACH.md`](SKILL_REACH.md) (tầm đánh hiện quá ngắn).

## 0. Tóm tắt

Ba hướng, cả ba đều phủ **cả hai cổng và cả hai đường trời** ngay từ khung đầu, thay vì nhắm một điểm như các chiêu hiện nay:

| | Hướng | Nguồn | Chỗ trong bộ chiêu | Hệ trình diễn | Cách thắng triều thú |
|---|---|---|---|---|---|
| **A** | **Twin Dragons, One Burning Pearl** (`twin-pearl`) | 雙龍戲珠, hai rồng đuổi ngọc | Kiếm, ô 2 | Hỏa | Mỗi con rồng "giữ" một cổng, chạy ngược dòng thú tới tận cổng, rồi cùng cắn ngọc ở chỗ hai đường gặp nhau: hoa sen lửa nở dọc cả hai đường |
| **B** | **Yinglong Carves the Rivers** (`yinglong-rivers`) | 應龍, rồng có cánh làm mưa, vạch đất chỉ đường sông cho Đại Vũ | Ô 4 của bộ chiêu hệ Thủy (hoặc ô 2 của Đao) | Thủy | Một con rồng có cánh vạch hai lòng sông dọc hai đường thú và hai dòng bụi nước trên trời; sông còn đọng, làm chậm và gây sát thương sau khi rồng đi |
| **C** | **Torch Dragon Opens Its Eye** (`torch-eye`) | 燭龍, rồng thân rắn mặt người, mở mắt là ngày, nhắm mắt là đêm | Tuyệt kỹ (ô 5), hệ Hỏa | Hỏa | Đêm sập xuống, con mắt dọc mở trên trời, năm vòng thân cào qua mọi đường, ấn mặt trời cháy khắp sân |

ChatGPT chọn dựng **A** trước; Gemini chọn **B**. Claude nghiêng về **A** (lý do ở §4). Câu hỏi cho anh ở §7.

## 1. Bài toán chiêu rồng phải giải

**Hình học sân** (canon §8.1, [`SKILL_REACH.md`](SKILL_REACH.md) §2.1):
- Sân Thanh Thạch Ải: x từ −20 tới +20, z từ −18 tới +8 (40 × 26 m). Trận Tâm ở (0; 0), người chơi đứng (0; +3).
- Cổng A (−15; −18) và cổng B (+15; −18), cách nhau 30 m. Hai đường đất chỉ gặp nhau trong khoảng 10 m quanh Trận Tâm. Quạ vào từ hai góc xa (±20; −18).
- Khoảng cách ngang: người chơi tới mỗi cổng 25,8 m; tới mỗi góc trời 29,0 m (ChatGPT tính, Claude tính lại).

**Vì sao thua hôm nay** (SKILL_REACH, đo trên bot):
- Thú đi 65 % quãng đường ngoài tầm ô 1.
- Ô 2 trúng trung bình 2,0 con mỗi lần, ô 4 trúng 4,6 con, tuyệt kỹ 3,9 con mỗi loạt. Lúc đỉnh đợt 5–6 có 25–44 thú sống (nhiều nhất 52).
- Gãy ngay khi mở cổng thứ hai, vì mỗi chiêu chỉ nhắm một điểm hoặc một hướng.

Vì vậy một chiêu rồng đẹp mà chỉ bay về một cụm thì không giải được lời anh. Ba hướng dưới đây được thiết kế từ đường đi của thú trước, rồi mới tới hình.

## 2. Luật chung cho cả ba hướng

Ghép từ hai trợ lý, Claude đã lọc:

1. **Phủ theo hành lang đường đi, không theo bán kính** (ChatGPT). Mỗi cổng có một phần chiêu "giữ" riêng, không bao giờ dồn hết vào cổng đông hơn. Quạ có khối trúng riêng trên cao (2,5–6 m); vết cháy dưới đất không trúng quạ.
2. **F0 đến F2: đòn ở người ra chiêu và "điểm chạm phóng" trên cả hai hành lang** (ChatGPT, Gemini cho số). Phím cuối là F0: lóe ở kiếm đạt đỉnh ngay khung đầu. Trong F1–F2, một sợi sáng mảnh nối từ kiếm tới đoạn có thú gần nhất của mỗi hành lang và gây khoảng 15 % sát thương. Đầu rồng không cần bay 26 m trong hai khung.
3. **Trúng lại và trần** (Gemini cho số): mỗi thú được trúng lại sau 18–24 tick, tối đa 3–4 lần mỗi lần tung. Vương có trần riêng theo mã lần tung, không bao giờ ăn đòn từ mọi mẫu của dải thân.
4. **Đo bằng bot, không ước bằng mắt** (ChatGPT): số thú khác nhau bị trúng mỗi lần (đích 12–20 khi có 40 thú trên hai đường, hôm nay 2–5), phần đường đi được phủ, tỉ lệ sát thương trái/phải (40/60 đến 60/40), tỉ lệ trúng quạ, thời gian tới đòn đầu ≤ 50 ms.
5. **Nhãn chữ thắng mọi xung đột** (cả hai): nhãn vẽ sau bloom và chỉnh màu; giảm hình phía sau nhãn, không bao giờ giảm nhãn; không có chớp hay bóng tối toàn màn hình phủ lên giao diện; khi hơn 35 thú thì cắt hạt phụ trước, giữ đầu rồng và lõi.
6. **Thân rồng chỉ hiện từng phần** (ChatGPT, Gemini đồng ý; theo cách Trần Dung giấu rồng trong mây ở Cửu Long đồ 1244): đầu và 20–30 % thân trước có vảy rõ; phần sau thành dải chất hệ, chìm vào khói, mây hoặc đá. Rồng trông dài hơn mà che ít hơn.
7. **Đường cong S nằm chủ yếu trên mặt đất** (Gemini, ChatGPT sửa số): thân gây sát thương ở cao 0,2–1,5 m, đầu lên 2–4 m ở nhịp gầm. Bóng dưới đất theo đúng độ cao và hướng sáng.
8. **Dáng theo "tam đình cửu tự" 三停九似** (Gemini, đã kiểm một phần): ba đoạn đầu tới vai, vai tới eo, eo tới đuôi, mỗi đoạn một độ cong khác; không bao giờ là ống đều bề. Sừng nai, râu dài, bờm, hàm rõ để đầu đọc được ở camera chơi.
9. **Mỗi hệ một bộ chất riêng** (ChatGPT; Claude bác ý "một mô phỏng tô lại màu cho mọi hệ" của Gemini): dùng chung đường đi, thời gian, khối trúng; không dùng chung hình. Lửa đổi màu ngọc không thành nước.
10. **Đánh nhanh, tắt chậm** (luật của anh): giữ đỉnh một lúc, rồi tắt bằng ăn mòn và nguội dần, không mờ đều. Đặt trần số mảnh còn lại để không phủ kín sân.

**Số trong tài liệu này là số thử.** Sát thương, hồi chiêu, vùng của canon §12 giữ nguyên tới khi anh chọn. Sau đó Claude chỉnh số và cân lại bằng bot theo `docs/games/BALANCE.md`, báo đủ chỉ số chứ không chỉ tỉ lệ thắng.

## 3. Ba hướng

Khung tính ở 60 Hz. F0 là phím đúng cuối cùng. Pha gồng chỉ hiện trong lúc gõ, không bao giờ bắt chờ sau F0.

### A · Twin Dragons, One Burning Pearl (`twin-pearl`)

**Một câu:** hai con rồng lửa bật ra từ hai bên lưỡi kiếm, mỗi con chạy ngược dòng thú tới một cổng, rồi cùng quay về cắn một viên ngọc lửa ở chỗ hai đường gặp nhau; ngọc vỡ thành hoa sen lửa có hai cánh dài chạy dọc hai đường.

**Nguồn:** 雙龍戲珠 (song long hí châu), họa tiết cung đình hai rồng đuổi ngọc lửa giữa mây. Đã kiểm: tấm cloisonné cuối Minh "Panel with dragons amid clouds" ở Metropolitan Museum (29.110.94), hai rồng đuổi ngọc lửa giữa mây. Họa tiết không quy định hai hành lang hay vụ nổ; đó là phần ta tự thiết kế.

**Chỗ trong canon:** Kiếm, ô 2 (chiêu diện rộng, hồi 8 s). Nó thay chiêu ô 2 "Thất Tinh Liệt Phong" trong [`SKILL_CATALOG_V2.md`](SKILL_CATALOG_V2.md) (bản nháp chưa duyệt). Không trùng Thương ô 2 (một nhát đâm quay về) hay Thương ô 4 (chín rồng tự săn): ở đây là đúng hai rồng, mỗi con giữ một cổng, và một cao trào chung. Theo D59, hệ khác đổi chất (Thủy: hai rồng ngọc đuổi một viên ngọc trăng).

| Pha | Khung | Việc |
|---|---|---|
| Gồng | trong lúc gõ | Mỗi chữ đúng thêm một vòng lửa quanh kiếm; hai lọn lửa xoắn ngược chiều nhau; một hạt ngọc nhỏ sáng dần trên chuôi; dưới chân mờ hiện ấn hai rồng. |
| Phóng (ở người ra chiêu) | F0–F2 | F0: lóe kiếm đạt đỉnh ngay khung đầu, nhát chém ở người ra chiêu, đòn giữ Trận Tâm 8 × 8 m ngay trước mặt. F1–F2: hai đầu rồng bật ra hai bên lưỡi; hai sợi sáng mảnh nối kiếm với điểm chạm trên mỗi hành lang (khoảng 15 % sát thương). |
| Bay | F3–F42 | Hai rồng tách đôi, mỗi con chạy ngược dòng một đường tới cổng (khoảng 26 m trong 40 khung) theo đường S trên mặt đất. Từ F30, đuôi vẩy cao quét góc trời (khối trúng cao 2,5–6 m). Ngọc bay thẳng tới điểm gặp (0; −9), theo đúng chỗ hai đường nhập trong lưới đường, rồi treo ở đó. Vệt lửa sau thân còn sát thương khoảng 0,9 s. |
| Trúng | F43–F64 | F43–F50 là nhịp gầm: hai đầu quay vào, chậm lại, há hàm; nhạc nền hạ 60–90 ms (không hạ tiếng gõ). F51 hai hàm khép vào ngọc: hoa sen lửa nở, mạnh nhất ở hai cánh dài dọc hai hành lang và ở vùng giữ Trận Tâm. Hoa sen trông rộng khoảng 18 m, nhưng sát thương đầy chỉ ở hai cánh. Khựng đòn 50 ms. |
| Dư âm | F65–F300 | Giữ đỉnh tới F80. Vệt lửa hình vảy trên hai đường và dấu hoa sen cháy nguội dần bằng ăn mòn (trắng vàng, son, than) tới F300 (5 s). Tàn lửa và sao lấp lánh thưa dần. |

**Tầm và triều thú:**
- Với tới 29 m (góc trời). Phủ trọn hai đường đất từ chỗ gặp nhau tới cổng, hai góc trời và vùng trước Trận Tâm.
- Mỗi thú tối đa 3 lần trúng (điểm chạm, hành lang, hoa sen), trúng lại sau 20 tick. Đề xuất chia sát thương: chạm 15 %, hành lang 45 %, hoa sen 40 % (giảm nửa ngoài hai cánh).
- Hai cổng được giữ cùng lúc ngay từ F2, nên cổng thứ hai không còn bị bỏ trống.

**Hào quang và lấp lánh:** sao bốn cánh ở mắt, đầu sừng và mặt ngọc (2–3 sao lóe lệch nhịp); vòng hào quang mảnh quanh ngọc chạy một điểm sáng; vảy lửa bong ra ở mép ngoài các khúc cua; bụi vàng li ti trong dư âm; lót khói tối rộng hơn thân 0,3–0,6 m để lửa không trắng xóa trên đá sáng.

| Lớp | Công cụ | Ghi chú |
|---|---|---|
| Đầu rồng (một model, soi gương thành hai) | Ảnh nguồn 4 góc từ ChatGPT (Firefly yếu ở giữ một thiết kế qua nhiều góc), anh duyệt, rồi Tripo; Blender làm xương hàm và chuỗi râu | Trước đó dựng thử bằng `thuong-luong` của Wordwoven (thuồng luồng có râu, 28 xương, 20 đốt đuôi) theo luật dùng lại quái; bản xem gần cần ≥ 20.000 tam giác theo `MODEL_QUALITY.md`, nên bản cuối là model mới |
| 20–30 % thân trước có vảy | Blender Geometry Nodes rải vảy dọc đường cong, xuất thành dải lưới tư thế thẳng | Mã chỉ uốn dải theo đường đi (đường cong lưu trong một texture dữ liệu, ý của Gemini) |
| Thân lửa phía sau, bờm | Firefly Video: `aura-fire-ribbon` (dải lửa lặp theo x, gần vệt lửa Dragonhold anh thích) và `aura-fire-flame-sheath` đã làm đêm 04/11; thiếu thì Blender lửa chạy dọc đường cong | Dùng lại trước khi tạo mới |
| Ngọc lửa | Firefly Video: cầu lửa trắng vàng lặp trên nền đen; vòng `fire-halo-seal-loop` | |
| Hoa sen nổ | Firefly Video image-to-video như `fire-crescent-sweep` (khung đầu là hoa sen dựng từ lửa Firefly), hoặc Blender lửa nổ có lực xoáy | 3–5 ứng viên cùng lúc |
| Dấu trên đất | Bộ mặt nạ vẽ (ChatGPT hoặc Firefly Image), 4–8 biến thể, đóng kênh: hình, tuổi, vạch nóng, alpha | Vệt cháy hình vảy, dấu hoa sen |
| Lấp lánh | `glint-gold-twinkle-set`, `tip-star-glint`, `fire-gold-dust`, `fire-spark-spray` (Firefly, đã có) | |
| Mã | Đường đi theo hành lang, khối trúng, thời gian, ăn mòn, vòng mảnh | Không vẽ hình |

**Âm thanh** (Firefly sound effects, model Adobe, nhiều lớp, to và vang):
- F0: tiếng kiếm nứt sáng và một tiếng chuông đồng cao.
- F3: hai tiếng vút lửa chạy về trái và phải.
- F43: lặng; F47: hai tiếng gầm stereo.
- F51: tiếng chuông lớn kiểu Bồ Lao (con rồng kêu vang trên đỉnh chuông), một tiếng nổ trầm và đuôi vang núi khoảng 3 s.
- Dư âm: lửa lách tách lấp lánh.
- Tiếng hô gợi ý: 双龙——夺珠！

**Rủi ro:**
- Ba chủ thể (hai rồng và ngọc) tranh mắt nhau: hai đầu cùng cỡ, ngọc nhỏ cho tới cao trào.
- Hai thân dài che nhãn chữ ở giữa sân: thân đi sát đất, chìm từng đoạn, có mặt nạ giảm hình sau nhãn.
- Ô 2 thành tuyệt kỹ thu nhỏ: sát thương hoa sen chỉ đầy ở hai cánh.
- Hai rồng có thể giống hai viên đạn: nhịp gầm và cú cắn ngọc chung làm chúng thành một nghi lễ.

**Ảnh concept:**
- `twin-pearl-c1`: rõ nhất ý "mỗi rồng một đường", rồng là lửa trên lót đỏ thẫm.
- `twin-pearl-c2`: khoảnh khắc cắn ngọc và hoa sen lửa có hai cánh dài; rồng ở đây là thịt da hơn là lửa.
- `twin-pearl-c3`: yếu nhất; hai rồng đứng sát tường, không nằm trên đường thú.

### B · Yinglong Carves the Rivers (`yinglong-rivers`)

**Một câu:** một con rồng có cánh trồi lên giữa sân và gầm; đuôi nó vạch hai lòng sông ngược lên hai đường thú, cánh quét hai dòng bụi nước qua hai góc trời; sông trào rồi còn đọng, làm chậm và gây sát thương sau khi rồng đã đi.

**Nguồn:** 應龍 Ứng Long, đã kiểm ở bản gốc.
- Sơn Hải Kinh, Đại Hoang Bắc Kinh: "應龍已殺蚩尤，又殺夸父，乃去南方處之，故南方多雨" và "應龍畜水".
- Thiên Vấn (Sở Từ) hỏi "rồng có cánh vạch gì trên đất"; chú của Vương Dật nói Ứng Long vạch đất chỉ cho Đại Vũ chỗ đào kênh.
- Chi tiết "vạch bằng đuôi" là cách đọc của học giả hiện đại, không có trong bản gốc (Gemini lượt 1 nói như dữ kiện; Claude ghi lại).

**Chỗ trong canon:** đề xuất ô 4 của bộ chiêu hệ Thủy. [`SKILL_CATALOG_V2.md`](SKILL_CATALOG_V2.md) đã có "Vạn Triều Trục Thú" (dòng linh thủy uốn khắp sân đuổi thú); Ứng Long thành người chỉ huy các dòng đó. Không trùng tuyệt kỹ Thủy "Huyền Hải Khai Giới" (cả sân thành biển sâu): ở đây là giữ đường, không đổi cả thế giới. Nếu anh muốn chiêu đi theo vũ khí thì là ô 2 của Đao (ChatGPT). Gemini đề xuất ô 4 của Kiếm, nhưng chỗ đó là chiêu kiếm bay tự săn đúng như ví dụ của anh, nên Claude không đề xuất.

| Pha | Khung | Việc |
|---|---|---|
| Gồng | trong lúc gõ | Dưới chân hiện một "bản đồ sông" cổ, vạch thêm một nét theo mỗi chữ đúng; hai nét cánh nước sau lưng; giọt nước tụ ở mũi kiếm. |
| Phóng | F0–F2 | F0: chém xuống đất, lóe đạt đỉnh khung đầu, vòng sóng nhỏ ở chân. F1: hai dòng nước mảnh chạy từ điểm gặp ngược lên hai đường tới cổng như hai nét vạch sáng (đòn chạm đầu, khoảng 15 %). F2: Ứng Long trồi lên sau lưng người chơi. |
| Bay | F3–F40 | Rồng vòng lên trên giữa sân (0; −6), cánh xòe khoảng 16 m; phần đuôi chìm vào mây để ít che. Hai nét nước dày dần thành hai lòng sông rộng 3,5–4 m. |
| Trúng | F41–F75 | F41–F47 nhịp gầm. F48 đuôi đập xuống (0; −8): hai lòng sông trào sóng lần lượt từ gốc tới cổng (sóng chạy 26 m trong khoảng 18 khung). F48–F60 hai vòng bụi nước từ cánh quét hai góc trời. Khựng đòn 50 ms. |
| Dư âm | F76–F300 | Sông còn sát thương nhẹ tới khoảng F150, làm chậm 25–35 % trong 1,5–2 s (Vương giảm một nửa). Hình lòng sông giữ khoảng 4 s rồi khô dần từ mép: bọt trắng, xanh ngọc, đá ướt. Giọt nước lấp lánh. |

**Tầm và triều thú:**
- Với tới 29 m. Hai lòng sông khoảng 26 m × 3,5–4 m mỗi bên (≈ 190–210 m² trên đất), cộng hai vùng trời.
- Điểm mạnh riêng: thú đi sau vẫn phải lội qua sông. Đây là hướng duy nhất trong ba hướng giữ đường lâu sau khi rồng đã đi, đúng chỗ "65 % quãng đường ngoài tầm".
- Đề xuất chia sát thương: chạm 15 %, sóng trào 50 %, sông đọng 35 % (có trần).

**Hào quang và lấp lánh:** giọt nước hóa sao lấp lánh ở đỉnh vòng bụi nước; vành bọt trắng sắc theo bậc; ánh mảnh trên mép cánh; hạt sáng li ti trên lòng sông khi nguội. Lót xanh đen trong lòng sông để nước không nhạt trên đá sáng.

| Lớp | Công cụ | Ghi chú |
|---|---|---|
| Đầu, thân trước, cánh | Ảnh nguồn ChatGPT, anh duyệt, Tripo; Blender cho xương cánh | Cánh phải là lụa nước hay lông vũ kiểu Trung Hoa, không phải cánh dơi (xem rủi ro) |
| Thân nước phía sau | Firefly Video, dải nước lặp, nền trong suốt | Firefly Video tốt cho chuyển động nước mềm |
| Sóng trào và bọt | Blender mô phỏng nước (chỉ ở vài điểm va chạm) kết xuất thành flipbook; mặt nạ bọt vẽ | |
| Lòng sông | Mặt nạ vẽ đóng kênh (hình, hướng chảy, vạch bọt, alpha); mã cuộn theo hướng chảy | |
| Bụi nước, giọt | Firefly Video trên nền đen | |
| Lấp lánh | Bộ sao Firefly đã có, nhuộm bạc lam | |
| Mã | Đường đi, khối trúng, thời gian, cuộn theo hướng chảy, ăn mòn | |

**Âm thanh:**
- F0: đá nứt và nước dâng trầm; F2: tiếng vỗ cánh rộng.
- F41: tiếng gầm vang của rồng mưa.
- F48: hai tiếng sóng vỡ trái và phải, lệch nhau 80 ms.
- Dư âm: giọt nước như pha lê, nước rút.
- Tiếng hô gợi ý: 应龙——划江！

**Rủi ro:**
- Firefly cứ vẽ "rồng có cánh" thành rồng phương Tây cánh dơi. 2 trong 4 ảnh bị vậy; `yinglong-rivers-c3` (bản Hỏa) hỏng hẳn nên bị bỏ khỏi bảng. Ảnh nguồn thật phải ghi rõ cánh lụa nước hay cánh lông.
- Bốn dòng dễ thành lưới tia laser: rồng phải là chủ thể duy nhất; các dòng chảy theo đúng đường thú, không thẳng tắp.
- Nước trong mờ dễ nhạt trên đá sáng: lót tối trong lòng sông.
- Làm chậm 4 s quá mạnh cho một chiêu lặp lại: tách hình 4 s khỏi thời gian gây hiệu ứng ngắn hơn (ChatGPT).

**Ảnh concept:**
- `yinglong-rivers-c1`: rồng giữa sân, hai sông, hai vòng bụi nước tới góc trời; cánh vẫn hơi kiểu dơi.
- `yinglong-rivers-c2`: rõ nhất ý "sông chạy dọc đường thú" (hình chữ V qua cả hai đường); con rồng nhỏ, giống rồng phương Tây.
- `yinglong-rivers-c4`: rồng phương Đông thân rắn có cánh lông nước; đúng tinh thần Ứng Long nhất.

### C · Torch Dragon Opens Its Eye (`torch-eye`)

**Một câu:** phím cuối đánh ngay một nhát ấn khắp sân, rồi cảnh cận: một khe đỏ dọc trên trời mở thành con mắt của Chúc Long; game chạy lại thì sân chìm trong đêm, năm vòng thân rắn đỏ cào qua mọi đường, con mắt mở hết và ấn mặt trời cháy khắp mặt đá.

**Nguồn:** 燭龍 Chúc Long (Chúc Âm), đã kiểm ở bản gốc: Sơn Hải Kinh, Đại Hoang Bắc Kinh: "人面蛇身而赤，直目正乘，其暝乃晦，其視乃明…是燭九陰，是謂燭龍" (mặt người, thân rắn, đỏ, mắt dọc; nhắm là tối, mở là sáng). Hình cổ không phải rồng bốn chân có sừng, và không có chiêu "ấn bát quái"; ấn là phần ta tự thêm. Mặt người dễ thành rợn hay buồn cười, nên Gemini đề xuất mặt nạ vàng cổ có mắt dọc; Claude đồng ý.

**Chỗ trong canon:** tuyệt kỹ (ô 5), hệ Hỏa. Đề xuất gộp với tuyệt kỹ Hỏa "Nhất Tinh Phần Thiên" trong V2 (mọi lửa tắt, dồn về một ngôi sao rồi đốt cả trời): ngôi sao nhỏ đó thành con mắt dọc của Chúc Long. Không trùng tuyệt kỹ Thủy (linh thú dưới biển sâu): đây là con mắt trên trời và đêm hóa ngày.

| Pha | Khung | Việc |
|---|---|---|
| Gồng | trong lúc gõ | Mỗi chữ đúng làm thế giới tối thêm khoảng 5 % (nhãn chữ không đổi); khe đỏ dọc mờ hiện trên trời sau tường xa; vầng nhật thực sau lưng người chơi. |
| Phóng | F0 | Đòn đầu ngay: nhát kiếm ấn xuống, một vòng sáng mảnh lan khắp sân, mọi thú nhận khoảng 20 % sát thương và khựng; sân tối hẳn. Rồi sim và giờ gõ dừng cho cảnh cận khoảng 57 khung (0,95 s): khe dọc mở thành con mắt, gương mặt nạ vàng cổ hiện sau mây. Cảnh cận chỉ là thời gian điện ảnh, không phải khung trận. |
| Bay | F1–F45 sau khi chạy lại | Năm vòng thân rồng trồi từ khói và mây, cào qua: đường trái, đường phải, hai góc trời, vùng giữa; mỗi vòng một khối trúng riêng. Thân nhìn thấy dài khoảng 80 m chỉ là hình; chỉ năm vòng gây sát thương. |
| Trúng | F46–F80 | Đầu ngẩng sau tường xa, mắt mở hết: "bình minh", ánh đỏ vàng tràn sân; ấn mặt trời trên toàn mặt đá kích nổ, đòn cuối khoảng 60 % sát thương lên mọi thú trong sân (trần cụm 60 % như canon). Khựng 70 ms, chớp ≤ 3 khung, không chạm giao diện. |
| Dư âm | F81–F360 | Ánh sáng trở lại trong 2–3 s. Vết cháy hình vảy và ấn mặt trời nguội từ mép vào tâm. Tro vàng, sao lấp lánh rơi chậm. |

**Tầm và triều thú:** cả sân, cả trên trời (1.040 m², tới 29 m). Ba lượt trúng (vòng mở, năm vòng cào, ấn mặt trời), nhưng mỗi thú tối đa 3 lần. Đây là nút "cứu đợt" khi 44–52 thú tràn cả hai cổng, kể cả Vương.

**Hào quang và lấp lánh:** con mắt là điểm sáng nhất (lõi trắng mảnh, quầng ≤ 0,9); tia sáng mỏng từ mắt; sao lấp lánh dọc sống lưng ở các khúc cua; sợi lửa than trên vảy; tro vàng và sao bốn cánh rơi chậm trong dư âm. Đêm là lớp tối sẵn: lửa đỏ nổi mà không cần chói.

| Lớp | Công cụ | Ghi chú |
|---|---|---|
| Cảnh cận: mắt và mặt nạ | Hai ảnh Firefly Image hoặc ChatGPT khớp nhau (mắt nhắm, mắt mở) cộng chuyển động có giới hạn; chỉ dùng Firefly Video nếu một lượt thử giữ đúng thiết kế | Firefly Video với khung đầu và cuối chỉ neo đầu và cuối, không bảo đảm giữa clip (ChatGPT, đúng với trang Adobe). Không dùng Upscale Video vì nó chạy Topaz Astra, model đối tác |
| Thân rắn | Thử dựng bằng `thuong-luong` (thân rắn có râu, 20 đốt đuôi) đổi vật liệu; bản cuối là model mới từ ảnh nguồn đã duyệt | Không chân, như bản gốc |
| Lửa trên thân, sợi than | Firefly Video `aura-fire-ribbon`, `aura-fire-flame-sheath`; Blender lửa dọc đường cong nếu cần dày hơn | |
| Ấn mặt trời | Ảnh vẽ đối xứng (ChatGPT hoặc Firefly Image) cho hình ấn; nhiễu lửa cho kênh ăn mòn; đóng kênh | Ấn bát quái dễ thành "vòng phép lạc loài" (ChatGPT): vẽ như mặt trời có vảy rồng |
| Đêm | Mã: chỉnh màu ánh sáng thế giới | Được phép (chỉnh màu), nhãn chữ không bị ảnh hưởng |
| Lấp lánh, tro | Bộ sao và `fire-gold-dust` đã có | |

**Âm thanh:**
- Trong lúc gõ: nhịp trầm như tim đập, dày dần theo chữ.
- F0: tiếng ấn kiếm cộng chuông lớn.
- Cảnh cận: gần như im hẳn, rồi tiếng "rắc" sáng của con mắt mở và hợp xướng dâng.
- Sau khi chạy lại: năm tiếng cào lửa theo năm vòng.
- F46: tiếng gầm thần thú, bùm trầm, đuôi vang khoảng 3,5 s.
- Tiếng hô gợi ý: 烛龙开目——昼临！

**Rủi ro:**
- Con rồng khổng lồ phủ kín sân: chỉ hiện từng vòng, đầu ở sau tường xa.
- Đêm làm khó đọc nhãn ở chỗ gần mắt và hào quang: nhãn vẽ sau, có nền riêng; mặt nạ giảm hình sau nhãn.
- Mặt người trên thân rắn có thể rợn: dùng mặt nạ vàng cổ, anh duyệt hướng mặt trước.
- Ấn trên sàn trông như sơ đồ phép: vẽ thành mặt trời vảy rồng.

**Ảnh concept:**
- `torch-eye-c1`: thân rắn ôm quanh cả sân như vòng lửa, ấn vàng ở Trận Tâm; đầu nhỏ, chưa thấy rõ mắt.
- `torch-eye-c2`: đầu khổng lồ sau tường xa, ánh đỏ tràn sân, hai vòng thân dọc hai mép.
- `torch-eye-c3`: rõ nhất. Con mắt dọc lửa trên trời, năm vòng cào qua sân, ấn mặt trời ở giữa, thú vẫn đọc được.

## 4. ChatGPT và Gemini góp gì, và Claude không đồng ý ở đâu

**ChatGPT góp:**
- Luật phủ theo hành lang, khối trúng riêng cho quạ, trần mỗi thú và trần Vương, và bộ chỉ số đo cho bot (§2.1, 2.3, 2.4).
- Điểm chạm phóng ở F0–F2 trên cả hai hành lang.
- Rồng lai: đầu có xương ổn định, phần đuôi là dải chất hệ; thân hiện từng phần như tranh Trần Dung; bốn khối (đầu, thân, chất hệ, dấu trên chiến trường).
- Không dùng clip Firefly cả con rồng bay làm asset hay làm đường đi; loại Upscale Video vì chạy Topaz Astra (đã kiểm).
- Nhãn chữ thắng mọi xung đột; mỗi hệ một bộ chất riêng.
- Lượt 2: sửa số của Gemini (ngọc ở (0; −9) thay vì (0; −12), hoa sen 18 m không tới góc trời, "72 %" không có căn cứ, instancing không tự làm hai rồng rẻ); nguồn Met 40747 cho song long hí châu; tự sửa chỗ nhầm tranh Trần Dung. Chọn A.

**Gemini góp:**
- Ý gốc của cả ba hướng cuối cùng: song long hí châu cho bài toán hai cổng, Ứng Long vạch sông để giữ đường, Chúc Long làm tuyệt kỹ đêm hóa ngày.
- Luật dựng cho camera 55°: đường S trên mặt đất, thân thấp dưới nhãn, sừng và râu phóng to; ngăn xếp độ sáng (lót tối, thân ≤ 0,85, viền 0,9, chỉ lõi mảnh trên 1).
- Đường cong trong texture dữ liệu để uốn lưới trên GPU; mặt nạ giảm hình sau nhãn; quy tắc 三停九似; mặt nạ vàng cổ cho Chúc Long; tiếng chuông kiểu Bồ Lao; khi hơn 35 thú thì cắt hạt phụ.
- Lượt 2: số cụ thể cho trúng lại (18–24 tick) và trần (3–4 lần), đòn chạm 15 %. Chọn B.

**Hai bên vênh nhau:**
- Dựng hướng nào trước (A hay B).
- Ứng Long ở ô 2 hay ô 4.
- Một mô phỏng tô màu cho mọi hệ (Gemini) hay mỗi hệ một bộ chất (ChatGPT).
- Râu dài 6–8 m (Gemini) hay thử 1–3 m trước (ChatGPT).
- Vòng lên xuống có bị dẹt ở 55° không (ChatGPT đúng: không dẹt hẳn).

**Claude không đồng ý:**
1. **Với Gemini:**
   - Cảnh cận trước đòn đầu (lượt 1) trái D58; lượt 2 đã sửa.
   - "Một mô phỏng tô lại màu cho mọi hệ": chỉ dùng chung đường đi, thời gian và khối trúng.
   - Con số "72 % sân, mỗi thú trúng hai lần" không có căn cứ.
   - Chọn B làm bản Hỏa đầu tiên: Ứng Long là rồng nước và mưa, bản Hỏa vừa lệch thần thoại vừa bị Firefly vẽ thành rồng phương Tây (`yinglong-rivers-c3`, đã bỏ).
   - Đặt B ở ô 4 của Kiếm: chỗ đó là chiêu kiếm bay tự săn của anh.
2. **Với ChatGPT:**
   - B ở ô 2 của Đao, hồi 8 s, với sông đọng làm chậm là quá mạnh. Claude để B ở ô 4 của hệ Thủy, nơi dòng nước đuổi thú vốn là ý của ô đó.
3. **Với cả hai:**
   - Đòn chạm phóng ở F1–F2 phải có sợi sáng nối về kiếm. Không có thì trông như nổ ngẫu nhiên ở xa.
   - Cả hai đều đề xuất Tripo hay Blender cho đầu rồng ngay. Theo luật của anh: tìm quái có sẵn trước (`thuong-luong` để dựng thử); ảnh nguồn phải đạt 8,5 và anh duyệt trước khi tạo model.

**Claude nghiêng về A,** vì:
- Đúng lab đang làm (Kiếm × Hỏa), và dùng lại được ngay các dải lửa, sao, vòng Firefly đã làm đêm 04/11.
- Hai cổng có rồng thật giữ cùng lúc, không phải dải hiệu ứng phụ.
- Ngọc cho một cao trào rõ, dễ đọc ở camera chơi.
- Ảnh `twin-pearl-c1` và `c2` là hai ảnh mạnh nhất trên bảng.

B nên là bản Thủy tiếp theo. C hợp làm tuyệt kỹ khi tới phần tuyệt kỹ.

## 5. Ảnh concept: cách làm và giới hạn

- **Công cụ:** Firefly web, Generate image, **Firefly Image 5** (model Adobe). Trang mở sẵn model đối tác Gemini 3.1; Claude đã đổi sang Firefly Image 5 trước ảnh đầu. 16:9; với ảnh tham chiếu, ảnh trả về 1360 × 768.
- **Giữ đúng camera chơi:** ảnh nhận diện `art-src/identity/thanh-thach-ai-55.png` (khung D48, 55°) được đưa vào ô Reference image. Thử không có tham chiếu thì Firefly hạ camera và phóng to nhân vật (ảnh thử đã xóa). Có tham chiếu thì cả 11 ảnh giữ đúng sân, hai cổng, triều thú và góc nhìn.
- **Số lượt:** 12 lượt, mỗi lượt một ảnh: 2 lượt thử camera và 10 ảnh concept. Giữ 9 ảnh; bỏ `yinglong-rivers-c3` (rồng phương Tây cánh dơi). Không mua credit, không chạm model đối tác, không đăng nhập, không bấm hộp đồng ý nào.
- **Lấy file:** bộ nhận cục bộ `127.0.0.1:8841` (form POST, trả 204 nên tab không rời trang); mỗi file đã so cỡ với blob. Đã tắt bộ nhận và máy chủ ảnh tham chiếu (8842) khi xong.
- **Giới hạn:**
  - Đây là ảnh concept để chọn hướng, **chưa chấm mù**, không phải art của game.
  - Firefly vẽ rồng đặc như sinh vật thật nhiều hơn "rồng làm bằng lửa hay nước", và hay vẽ cánh dơi khi được nói "có cánh".
  - Một ảnh đẹp có lửa ở cả hai cổng không chứng minh chiêu thật sự trúng cả hai cổng; tầm phải đo bằng bot (ChatGPT).

## 6. Sau khi anh chọn

1. **Hộp xám trước:** dựng đường đi và khối trúng của hướng được chọn trong lab (không hình), chạy bot ở 30–80 WPM, đo các chỉ số ở §2.4 trên trận đông nhất.
2. **Nghiên cứu hình và ứng viên:** ChatGPT và Gemini tìm các mẫu rồng được yêu thích; ảnh nguồn đầu rồng 4 góc cho anh duyệt; 3–5 ứng viên Firefly Video hoặc Blender cho mỗi lớp còn thiếu.
3. **Lab chiêu:** đủ năm pha, âm thanh, hiệu ứng màn hình theo bậc; gửi anh video và tấm khung; có bản chơi thử ở link cục bộ cố định.
4. **Chấm:** hai giám khảo mù ≥ 8,5 trong bản chơi, với thiết lập của người chơi. Đạt 7 thì gửi anh video demo rồi đi tiếp.

## 7. Câu hỏi cho anh

Anh chọn hướng nào để dựng trước: **A · Twin Dragons, One Burning Pearl** (Kiếm ô 2, Hỏa; Claude và ChatGPT đề xuất), **B · Yinglong Carves the Rivers** (ô 4 hệ Thủy; Gemini đề xuất), hay **C · Torch Dragon Opens Its Eye** (tuyệt kỹ Hỏa)? Nếu anh thích một ảnh cụ thể trên bảng hình, anh chỉ tên ảnh (ví dụ `twin-pearl-c1`), Claude sẽ lấy nó làm hướng hình.

## 8. Hộp xám: kết quả đo (04/11/2026)

**Đo gì:** hộp xám của A · Song Long trong `games/immortality-cultivation`.
- **Bản hiện tại** (sau review, 04/11 chiều): HEAD `033b3f4`.
  - Sim `68be1b8`: ngân sách mỗi bên, một trần cụm cho cả lần tung, hệ số giảm dần riêng mỗi bên, một thứ tự đánh cho cả hai đường.
  - Lab `4e0800f`.
  - Changelog `docs/changelog/2026-11-04-twin-pearl-review-fixes.md`.
- **Bản trước sửa:** HEAD `6e68958` (sim `e91a787`, lab `7ee98f0`). Số của nó được giữ ở cột "trước sửa" để so.

Chiêu chỉ chạy khi header trận có cờ `swordKey2: "twin-pearl"`; mặc định tắt, và trận mặc định giữ đúng từng byte như `1a78a82`. Bài đo so Song Long với ô 2 hôm nay (Nhất Tuyến Xuyên Vân, đường thẳng 14 × 1,2 m) theo §2 luật 4 và [`BALANCE.md`](../../BALANCE.md), rồi quét mức ngân sách làm chứng cứ cho anh. Canon và [`00-canon.md`](../00-canon.md) giữ nguyên; mọi số vẫn là số thử. Review và các sửa: §8.11.

### 8.0 Kết luận (sau sửa)

1. **Số thú khác nhau bị trúng: đạt đích nhờ ngân sách.**
   - Khi có 35–45 thú trên hai đường, Song Long trúng 17,2 con mỗi lần tung (p10–p90: 14–21); 80 % số lần tung nằm trong 12–20. Hôm nay: 2,8 con. Trước sửa: 36,4 con, 0 % trong đích.
   - Ở 25–34 thú: 14,4 con, 78 % trong đích. Ở 15–24 thú: 10,9 con, 42 %.
   - Không có trần số con. Ngân sách mỗi bên cạn trước khi rồng chạy hết đường.
2. **Phủ đường, quạ và đòn đầu: đạt, với một cái giá.**
   - Các khối trúng vẫn phủ trọn hai đường và hai góc trời (định nghĩa ở §8.1).
   - Lúc đông, sát thương thật chỉ tới 15,4 m (tây) và 20,2 m (đông) tính từ Trận Tâm (trung vị). Cổng cách 23,3 m. Chỉ 26 % số thú ở xa hơn 12 m bị trúng (chưa có ngân sách: 74 %).
   - Trúng 92 % số quạ đang bay (hôm nay 2 %).
   - Đòn đầu ở F0 hoặc F1 (0–17 ms; hôm nay 200 ms). Trong lab, phím → khung hiện ≤ 17–31 ms.
3. **Trái/phải: đạt.** Trung vị 50/50 lúc 35–45 thú; 92 % số lần tung nằm trong 40/60–60/40. Trước sửa: 57,5/42,5 và 64 %, vì đường A được lợi do thứ tự tính.
4. **Vẫn mạnh, dù đã giảm hơn một nửa.**
   - Lúc đông: 5,9 W hiệu dụng và 7,8 con hạ mỗi lần tung (trước sửa 13,2 W và 21,3 con). Một lần tuyệt kỹ hôm nay ra 4,1 W.
   - Ô 2 chiếm 41–50 % sát thương cả trận (trước sửa 57–62 %; canon §7.3 ≤ 20 %).
   - Mọi bot Mới → Nhanh thắng 95–100 % (dải Cân bằng 75–90 %); Trẻ em 5 %.
5. **Vẫn sửa đúng chỗ gãy của [`SKILL_REACH.md`](SKILL_REACH.md):**
   - Áp lực P từ 67–75 % xuống 49–60 % (đích 15–35 %).
   - Quãng Q từ 72–82 % xuống 68–71 %, sát mép trên của dải 50–70 %.
   - Đợt 2 (mở cổng thứ hai) với bot Chuẩn: thú lọt từ 14 % xuống 6,6 %, Trận Lực mất từ 30 % xuống 8,8 %.
6. **Quét ngân sách** (§8.6): không mức nào đưa ô 2 về ≤ 20 % mà vẫn giữ được tầm và tỉ lệ thắng. Tỉ lệ thắng có một "vách" giữa 1,25 và 2,5 W mỗi bên. Câu hỏi cho anh ở §8.8.

### 8.1 Cách đo

- **Bot** (ngoài Git, `games/immortality-cultivation/tmp/skill-reach/`): chính bot của [`SKILL_REACH.md`](SKILL_REACH.md) §3.1, thêm phần chọn ô 2.
  - Hồ sơ không hậu tố: ô 2 hôm nay.
  - `@twin-pearl`: Song Long (cờ header), với ngân sách mặc định 2,5 W mỗi bên.
  - `@twin-pearl+pool<N>`: chỉ đổi ngân sách mỗi bên thành N (W × 100) trong bộ nhớ (`key2-numbers.ts`, nạp trước sim). `+pool100000s100000` là "không giới hạn".
- **Ghi từng lần tung ô 2** (`key2-measure.ts`, chỉ đọc world và sự kiện): số thú lúc tung theo cổng, thú khác nhau bị trúng, đòn, hạ, sát thương hiệu dụng và tiềm năng, phần thừa, trái/phải, quạ, đòn đầu, phần đường được phủ, đòn xa nhất trên đất mỗi bên, phần thú xa bị trúng, sát thương theo từng phần của chiêu.
- **Kiểm cờ tắt:**
  - 9 hồ sơ × 4 seed với `BOT_HASHES=1`: 36/36 file trùng `golden-before` của bước dựng (chính là `1a78a82`) ở mọi trường bot cũ có ghi, gồm 1 693 mốc băm world và local.
  - 340 trận "hôm nay" của ma trận mới trùng lần đo sáng 04/11, nên cột "hôm nay" vẫn là số của SKILL_REACH §3.
  - Có thêm test ghim băm trong `tests/sim/twin-pearl.test.ts`.
- **Ma trận:** như SKILL_REACH §3: 17 hồ sơ × 20 seed, Cân bằng, bộ điều nhịp bật, Đứng yên. Chín biến thể (hôm nay, Song Long, không giới hạn, sáu mức quét) là 3 060 trận, 5 phút trên 6 lõi.
- **Hai cách lấy lần tung:**
  - **Trận thật:** mọi lần bot tung ô 2. Với Song Long sân thưa hơn, nên cả ma trận chỉ có 14 lần tung lúc 35–45 thú.
  - **Quét đỉnh** (`key2-dense.ts`): bot chơi trận cờ tắt. Ở lúc đông nhất trên hai đường của mỗi đợt (≥ 15 con), dựng lại world từ replay, tung ô 2 đúng tick đó trong bản sao, rồi chạy tiếp 110 tick không lệnh nào. Mọi biến thể dùng cùng các world đó: 1 665 lần tung mỗi biến thể, 92 lần lúc 35–45 thú. Đây là nguồn số chính cho §2 luật 4.
  - Sau review, bản sao bỏ các đòn đường thẳng ô 2 còn chờ của trận gốc trước khi tung, để chúng không bị tính cho lần tung đang đo (review thấy 5 lần như vậy).
- **Định nghĩa:**
  - **Thú khác nhau bị trúng:** số con nhận ít nhất một đòn hiệu dụng của lần tung, kể cả con sinh ra sau khi tung (vệt rồng còn trúng tới F96).
  - **Phủ đường (hình học):** phần đường đi của mỗi cổng (từ cổng tới mép Trận Tâm, mẫu 0,25 m) nằm trong một khối trúng trên đất của lần tung, ở bất kỳ tick nào. Phép đo tính mọi khối, kể cả hộp giữ F0 và phần nửa của hoa sen. Riêng thân rồng chỉ phủ 66,7 % đường: đầu rồng xuất phát ở điểm gặp, nên không chạm 8,6 m cuối từ khúc quanh vào Trận Tâm. Hộp giữ và hoa sen phủ đoạn đó.
  - **Đòn xa nhất (mới):** khoảng cách tới Trận Tâm của đòn hiệu dụng xa nhất lên thú đất mỗi bên, trung vị qua các lần tung. Hai cổng cách 23,3 m.
  - **Thú xa bị trúng (mới):** trong số thú đất ở xa hơn 12 m lúc tung, phần nhận ít nhất một đòn.
  - **Trái/phải:** sát thương hiệu dụng lên bên tây (thú cổng A, quạ ở x < 0) so với bên đông; chỉ tính lần tung có thú ở cả hai đường.
  - **Trúng quạ:** phần quạ sống lúc tung bị trúng.
  - **Đòn đầu:** số tick từ F0 tới đòn hiệu dụng đầu tiên (1 tick = 16,7 ms).
  - **Thừa:** phần dư của các đòn kết liễu (đòn tiềm năng P × M_q × bucket × hệ số giảm dần, chưa tính trần cụm, ngân sách và ×1,5 phá thế, trừ máu còn), chia cho tổng sát thương tiềm năng của lần tung.
  - **Lần tung mỗi phút:** tính trên phút đánh (không tính giờ nghỉ và chuẩn bị). Tính trên cả trận thì Song Long 4,5 lần mỗi phút, hôm nay 3,9.

### 8.2 Tầm mỗi lần tung (§2 luật 4)

Quét đỉnh, lúc 35–45 thú trên hai đường; 92 lần tung mỗi cột.

| Chỉ số | Đích | Hôm nay (đường thẳng) | Trước sửa | Sau sửa, không giới hạn | **Song Long (sau sửa)** |
|---|---|---|---|---|---|
| Thú trên hai đường lúc tung | ~40 | 38,2 | 38,2 | 38,2 | 38,2 |
| Thú khác nhau bị trúng (p10–p90) | 12–20 | 2,8 (1–5) | 36,4 (32–41) | 31,5 (28–36) | **17,2 (14–21)** |
| Lần tung trong 12–20 | | 0 % | 0 % | 0 % | **80 %** |
| Phần thú đang sống bị trúng | | 7 % | 90 % | 77 % | 43 % |
| Phủ đường cổng A / B (hình học) | | 3 % / 13 % | 100 % / 100 % | 100 % / 100 % | 100 % / 100 % |
| Đòn xa nhất trên đất, tây / đông | | 5,4 / 2 m | | 22,9 / 22,0 m | 15,4 / 20,2 m |
| Thú xa hơn 12 m bị trúng | | 0 % | | 74 % | 26 % |
| Trái/phải, trung vị (p10–p90 phần trái) | 40/60–60/40 | một bên (0 hoặc 100 %) | 57,5/42,5 (46–65 %) | 58/42 (47–66 %) | **50/50 (43–57 %)** |
| Lần tung trong 40/60–60/40 | | 2 % | 64 % | 55 % | **92 %** |
| Trúng quạ | | 2 % | 96 % | 96 % | 92 % |
| Đòn đầu | ≤ 50 ms | 12 tick = 200 ms | F0 (89 %) hoặc F1 | F0 (82 lần) hoặc F1 (10 lần) | F0 (82 lần) hoặc F1 (10 lần): 0–17 ms |
| Hạ mỗi lần tung | | 2,4 | 21,3 | 15,0 | 7,8 |
| Sát thương hiệu dụng mỗi lần | | 1,1 W | 13,2 W | 11,8 W | 5,9 W |
| Thừa | | 71 % | 22 % | 17 % | 27 % |

**Theo mật độ** (quét đỉnh; số thú khác nhau bị trúng, trong ngoặc là phần lần tung rơi vào 12–20):

| Thú trên hai đường | Số lần tung | Hôm nay | Trước sửa | Song Long (sau sửa) |
|---|---|---|---|---|
| 15–24 | 1 168 | 2,1 (0 %) | 19,7 (53 %) | 10,9 (42 %) |
| 25–34 | 402 | 2,6 (0 %) | 26,7 (4 %) | 14,4 (78 %) |
| 35–45 | 92 | 2,8 (0 %) | 36,4 (0 %) | 17,2 (80 %) |

- **Trận thật khớp quét đỉnh:**
  - Lúc 35–45 thú (14 lần tung): 17,9 con, 44 % số đang sống.
  - Lúc 25–34 thú (282 lần): 15,3 con.
  - Tính mọi lần tung của cả trận (phần lớn lúc thưa): hôm nay 1,9 con mỗi lần, Song Long 6,7.
- **Đòn đầu trong trận thật:**
  - 15 374 lần tung: F0 ở 28 %, F1 ở 72 %.
  - 3 lần tới muộn (F31, F51, F51) và 1 lần không trúng (0,03 %).
  - Trước sửa có 36 lần tới muộn, phần lớn vì chiêu giải khi trên sân chỉ còn Vương đang gầm. Nay chiêu không giải trong trường hợp đó.
- **Trái/phải không còn lệch do thứ tự tính.** Mỗi bên có hệ số giảm dần và ngân sách riêng, và mỗi tick đánh theo một thứ tự chung cho cả hai đường. Có test: đám thú đối xứng gương nhận đòn đối xứng, sinh bên nào trước cũng vậy.
- **Thú bầy còn 1 máu đứng một mình không chết vì đòn vùng.** Đây là luật có từ trước trong `combat.ts`, không riêng Song Long: trần cụm là 60 % máu cả cụm làm tròn xuống, nên với 1 máu nó là 0. Chưa sửa, vì sửa sẽ đổi trận mặc định; sẽ làm riêng, kèm golden.

### 8.3 Sát thương theo phần của chiêu

Quét đỉnh, 35–45 thú. Mỗi ô: phần sát thương · số đòn mỗi lần tung · số con hạ mỗi lần tung.

| Phần | Khung | Trước sửa | Sau sửa, không giới hạn | Song Long (sau sửa) |
|---|---|---|---|---|
| Đòn giữ 8 × 8 m trước Trận Tâm | F0 | 8,7 % · 6,1 · 2,1 | 10,8 % · 5,8 · 2,8 | 10,1 % · 2,7 · 1,2 |
| Điểm chạm trên hai đường | F1–F2 | 8,5 % · 6,5 · 0,6 | 10,9 % · 6,3 · 1,4 | 3,5 % · 1,2 · 0,4 |
| Thân và vệt trên đất | F3–F96 | 52,1 % · 20,3 · 12,4 | 49,2 % · 16,6 · 8,4 | 41,0 % · 7,2 · 3,3 |
| Đuôi quét trời | F30–F50 | 6,3 % · 1,7 · 0,1 | 7,0 % · 1,7 · 0,1 | 12,0 % · 1,7 · 0,1 |
| Hoa sen, phần đầy (hai cánh dài và vùng giữ) | F51–F71 | 19,4 % · 8,4 · 4,0 | 19,9 % · 5,5 · 2,2 | 26,0 % · 5,0 · 2,3 |
| Hoa sen, phần nửa (ngoài cánh) | F51–F71 | 5,0 % · 4,3 · 2,0 | 2,2 % · 1,5 · 0,2 | 7,4 % · 2,4 · 0,4 |

- **Chia thật so với thiết kế:** thiết kế chia chạm 15 %, hành lang 45 %, hoa sen 40 %. Sau sửa đo được 14 / 53 / 33 % (trước sửa 17 / 58 / 24 %). Ngân sách giữ riêng phần của hoa sen, nên hoa sen không còn bị thân rồng "ăn" trước.
- **Đòn giữ F0 lấy gần hết phần "chạm"** của mỗi bên, vì nó đánh trước và vào đúng chỗ nguy nhất. Lúc đông, hai sợi sáng F1–F2 vì vậy gần như không còn sát thương. Đây là hệ quả của thứ tự tới trước; phần nhìn vẫn vẽ chúng.
- **Thừa:** Song Long 27 %, so với 71 % của đường thẳng hôm nay. Đòn 2,5 W của đường thẳng rơi vào Thạch Thử 30 máu.

### 8.4 Các chỉ số của BALANCE.md

17 hồ sơ × 20 seed, Cân bằng, bộ điều nhịp bật. Cột như SKILL_REACH §3.4:
- "Gõ" là phần sát thương gõ (CB2 cần ≥ 55 %);
- "Ô 1/gõ" là phần ô 1 trong sát thương gõ (CB3 cần ≤ 30 %);
- "Ô 2/cả trận" là phần ô 2 trong mọi sát thương (canon §7.3 cho mỗi chiêu vùng ≤ 20 %);
- "Đánh nền" thì canon §7.3 đích 12–18 %;
- "Phút" là thời lượng trận, tính tới lúc thua.

Dải đích Cân bằng: Thắng 75–90 % · S trung vị 35–65 % · P 15–35 % · I ≤ 10 % · O ≤ 8 % · N 0,3–1 · Q trung vị 50–70 %.

**Hôm nay · Song Long sau sửa** (mỗi ô: số hôm nay · số Song Long):

| Hồ sơ | Thắng | S | P | I | O | N | Q | Gõ | Ô 1/gõ | Ô 2/cả trận | Đánh nền | Phút | Thua ở đợt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 30 WPM 90 % | 0 · 100 % | 0 · 42 % | 74 · 55 % | 0,6 · 1,3 % | 0 · 0 % | 0 · 0,1 | 79 · 70 % | 80 · 84 % | 39 · 24 % | 23 · 47 % | 10,5 · 8 % | 8 · 12,7 | 4: 3 · 5: 16 · 6: 1 / — |
| 30 WPM 97 % | 5 · 100 % | 0 · 57 % | 71 · 50 % | 0,7 · 1,5 % | 0 · 0 % | 0,05 · 0 | 77 · 69 % | 81 · 85 % | 42 · 25 % | 21 · 48 % | 8,7 · 6,4 % | 9,1 · 11,9 | 4: 1 · 5: 7 · 6: 11 / — |
| 45 WPM 90 % | 0 · 100 % | 0 · 37 % | 71 · 56 % | 0,3 · 1,5 % | 0 · 0 % | 0 · 0,25 | 76 · 70 % | 82 · 85 % | 45 · 29 % | 20 · 45 % | 8 · 6,3 % | 7,7 · 10,9 | 5: 17 · 6: 3 / — |
| 45 WPM 97 % | 0 · 100 % | 0 · 47 % | 69 · 53 % | 0,4 · 1,6 % | 0 · 0 % | 0 · 0,2 | 75 · 68 % | 83 · 87 % | 48 · 29 % | 19 · 45 % | 6,6 · 5,2 % | 8,2 · 10,2 | 5: 7 · 6: 13 / — |
| 60 WPM 90 % | 0 · 100 % | 0 · 36 % | 72 · 60 % | 0,2 · 1,6 % | 0 · 0 % | 0 · 0,35 | 76 · 70 % | 84 · 86 % | 48 · 33 % | 20 · 41 % | 6,2 · 5,7 % | 7,1 · 9,6 | 5: 14 · 6: 6 / — |
| 60 WPM 97 % | 0 · 100 % | 0 · 49 % | 69 · 54 % | 0,6 · 1,6 % | 0 · 0 % | 0 · 0 | 73 · 68 % | 85 · 87 % | 51 · 33 % | 18 · 43 % | 5,2 · 4,4 % | 7,8 · 9,3 | 5: 7 · 6: 13 / — |
| 80 WPM 90 % | 0 · 100 % | 0 · 39 % | 70 · 58 % | 0,6 · 1,5 % | 0 · 0 % | 0 · 0,1 | 74 · 70 % | 84 · 87 % | 51 · 34 % | 19 · 41 % | 5,6 · 5,3 % | 7,5 · 9,4 | 5: 9 · 6: 11 / — |
| 80 WPM 97 % | 40 · 100 % | 0 · 52 % | 67 · 51 % | 1,2 · 2,1 % | 0 · 0 % | 0,4 · 0 | 72 · 68 % | 85 · 88 % | 52 · 35 % | 18 · 42 % | 5,1 · 3,9 % | 8,4 · 9,1 | 5: 3 · 6: 9 / — |
| Trẻ em (15 WPM 88 %) | 0 · 5 % | 0 · 0 % | 83 · 71 % | 0,2 · 0,3 % | 0 · 0 % | 0 · 0,05 | 95 · 81 % | 72 · 76 % | 22 · 13 % | 26 · 48 % | 20 · 15 % | 5,4 · 10,3 | 3: 15 · 4: 5 / 4: 3 · 5: 6 · 6: 10 |
| Mới (25 WPM 92 %) | 0 · 95 % | 0 · 46 % | 75 · 54 % | 0,4 · 1 % | 0 · 0 % | 0 · 0,1 | 82 · 71 % | 78 · 82 % | 37 · 21 % | 22 · 48 % | 12,1 · 9,2 % | 8,5 · 13,7 | 4: 5 · 5: 12 · 6: 3 / 6: 1 |
| Chậm chắc (25 WPM 99 %) | 0 · 100 % | 0 · 64 % | 71 · 49 % | 0,6 · 1,2 % | 0 · 0 % | 0 · 0 | 78 · 69 % | 80 · 85 % | 39 · 22 % | 22 · 49 % | 9,6 · 6,9 % | 9,9 · 12,6 | 5: 9 · 6: 11 / — |
| Chuẩn (35 WPM 95 %) | 0 · 100 % | 0 · 45 % | 72 · 55 % | 0,3 · 1,2 % | 0 · 0 % | 0 · 0,05 | 77 · 70 % | 81 · 85 % | 44 · 27 % | 20 · 46 % | 8,4 · 6,4 % | 8,5 · 11 | 5: 10 · 6: 10 / — |
| Khá (50 WPM 96 %) | 5 · 100 % | 0 · 54 % | 70 · 53 % | 0,6 · 2 % | 0 · 0 % | 0,05 · 0 | 75 · 68 % | 83 · 87 % | 48 · 28 % | 20 · 46 % | 6,3 · 5 % | 8,6 · 9,6 | 5: 2 · 6: 17 / — |
| Ẩu (50 WPM 85 %) | 0 · 100 % | 0 · 28 % | 73 · 60 % | 0,3 · 1,3 % | 0 · 0 % | 0 · 0,7 | 77 · 71 % | 82 · 85 % | 45 · 30 % | 21 · 43 % | 8,2 · 6,9 % | 7,5 · 10,8 | 4: 4 · 5: 10 · 6: 6 / — |
| Nhanh (70 WPM 97 %) | 10 · 100 % | 0 · 60 % | 68 · 51 % | 1,3 · 2,5 % | 0 · 0 % | 0,1 · 0 | 74 · 68 % | 85 · 88 % | 51 · 30 % | 19 · 45 % | 5,3 · 4,3 % | 8,4 · 9 | 5: 2 · 6: 16 / — |
| Không gõ | 0 · 0 % | 0 · 0 % | 82 · 82 % | 0 · 0 % | 0 · 0 % | 0 · 0 | 100 · 100 % | 0 · 0 % | — | 0 · 0 % | 74,8 · 74,8 % | 1 · 1 | 1: 20 / 1: 20 |
| Chỉ gõ (35 WPM 95 %, không mua) | 0 · 100 % | 0 · 45 % | 75 · 57 % | 0,5 · 1,5 % | 0 · 0 % | 0 · 0,1 | 79 · 70 % | 91 · 93 % | 42 · 26 % | 23 · 50 % | 9,5 · 6,9 % | 7,8 · 11,1 | 4: 2 · 5: 13 · 6: 5 / — |

**Thêm cho bot Chuẩn** (hôm nay → Song Long sau sửa):
- Đợt 2 (mở cổng thứ hai): thú lọt 14 % → 6,6 %; Trận Lực mất trong đợt 30 % → 8,8 %.
- Ô 2:
  - 5,0 → 5,6 lần mỗi phút đánh;
  - 8,5 → 21,4 W mỗi phút (canon ước ~18);
  - 1,9 → 6,5 con trúng và 1,6 → 3,6 con hạ mỗi lần tung.
- Phần sát thương cả trận của các chiêu vùng khác: ô 4 15,1 % → 10,0 %, tuyệt kỹ 10,7 % → 6,3 %.
- Mỗi lần tuyệt kỹ (mọi bot gõ): 4,1 → 2,9 W hiệu dụng, vì Song Long đã hạ trước nhiều con.
- Sức ra đòn tổng: 43,0 → 46,8 W mỗi phút đánh (D_ref thử 75).
- Thời gian sống trung bình của một thú (B4): 12,5 s → 10,1 s.

### 8.5 Cổng bot đo được

| Cổng | Hôm nay | Trước sửa | Song Long (sau sửa) |
|---|---|---|---|
| B1 cùng vùng cuốn (Mới → Nhanh) | trượt: thắng 0–10 %, S 0, P 68–75 % | trượt: thắng 95–100 %, P 41–52 % | trượt: thắng 95–100 %, S 28–64 %, P 49–60 % |
| B2 không quá dễ | đạt | đạt | đạt |
| B3, phần bot Mới (≥ 70 %) | trượt: 0 % | đạt: 95 % | đạt: 95 % |
| B4 chuẩn thắng ẩu | trượt: S 0 và 0 | đạt | đạt: S Chậm chắc 64 % > Ẩu 28 %; Chuẩn hạ thú 10,1 s < Ẩu 10,6 s |
| B5 Không gõ thua (Cân bằng) | đạt | đạt | đạt |
| B7, phần đo được | 1,9–2,0 bậc mỗi đợt | 1,2–1,9 | 1,5–2,0 |
| CB1 | đạt | đạt | đạt |
| CB2 phần gõ ≥ 55 % (Chuẩn) | đạt: 81 % | đạt: 88 % | đạt: 85 % |
| CB3 ô 1 ≤ 30 % sát thương gõ | trượt: 37–51 % | đạt: 14–21 % | trượt sát: 21–30 % (bot Nhanh 30,4 %) |
| CB9 Chuẩn 9–10,5 phút | không chấm (Chuẩn thua mọi seed) | trượt sát: 10,6 phút | trượt: 11,0 phút |
| HC2 ≤ 8 chữ sống | đạt (8) | đạt (8) | đạt (7) |
| §7.3 mỗi chiêu vùng ≤ 20 % (Chuẩn) | đạt sát: ô 2 19,9 % | trượt: 59,2 % | **trượt: 45,7 %** |
| §7.3 đánh nền 12–18 % (báo cáo) | 8,4 % | 5,0 % | 6,4 % |

- **B3:** chỉ chấm phần bot Mới; bot Trẻ em chạy ở Cân bằng, không ở Thư giãn như cổng yêu cầu.
- **B7:** mọi biến thể ≤ 2 bậc mỗi đợt, khoảng sinh 93–114 % (trong ±15 %). Thiếu lượt Chuẩn tắt nhịp, nên kit ghi "thiếu số".
- **Bot không đo được:** B6 (chưa có cặp chiến thuật Tốt/Kém), B8, HC1, HC3, HC8 (chưa có sự kiện học nháp), B9 (chưa có buổi chơi thử của người thật).

### 8.6 Quét ngân sách (chứng cứ, không phải đề xuất)

**Luật ngân sách** (`TWIN_PEARL.pool`, số thử):
- Mỗi bên (tây: thú cổng A và quạ ở x < 0; đông: cổng B và quạ ở x ≥ 0) có 2,5 W cho thú đất và vùng giữ, chia 15/45/40 như phần chạm, hành lang, hoa sen của mỗi con. Thêm 0,8 W cho đuôi quét trời của bên đó (máu một con Hỏa Nha).
- Ngân sách nhân M_q của Cast và bucket của ghế, như mọi đòn.
- Mỗi đòn lấy tối đa phần còn lại của bên và loại của nó, theo thứ tự tới trước. Phần nào hết thì lần tung đó không trúng thêm con nào bằng phần ấy.
- Mốc 2,5 W: mỗi rồng mang đúng sát thương ô 2 hôm nay lên con đầu tiên. Một con thú đơn độc mỗi bên vì vậy nhận đủ như ô 2 hôm nay.

**Quét:** mỗi mức đổi ngân sách mỗi bên, trời giữ 0,8 W; 17 hồ sơ × 20 seed mỗi mức.

| Mỗi bên | Trúng lúc 35–45 thú (trong 12–20) | W mỗi lần tung | Đòn xa nhất tây / đông | Mới → Nhanh thắng | Chuẩn: thắng · S · P · Q | Ô 2/cả trận (mọi bot gõ) |
|---|---|---|---|---|---|---|
| 1,25 W | 11,9 (58 %) | 3,4 | 13,1 / 13,1 m | 0–60 % | 0 · 0 · 67 · 73 % | 29–36 % |
| 1,5 W | 13,0 (67 %) | 3,9 | 13,4 / 13,6 m | 5–90 % | 40 · 0 · 65 · 72 % | 32–40 % |
| 1,75 W | 14,3 (84 %) | 4,4 | 14,4 / 13,6 m | 30–100 % | 90 · 10 · 63 · 71 % | 34–43 % |
| 2,0 W | 15,2 (84 %) | 4,9 | 14,9 / 16,0 m | 45–100 % | 95 · 21 · 60 · 71 % | 37–45 % |
| **2,5 W (mặc định)** | **17,2 (80 %)** | **5,9** | **15,4 / 20,2 m** | **95–100 %** | **100 · 45 · 55 · 70 %** | **41–50 %** |
| 3,75 W | 21,8 (35 %) | 8,1 | 17,7 / 21,4 m | 100 % | 100 · 57 · 49 · 67 % | 48–58 % |
| 5,0 W | 26,2 (2 %) | 9,7 | 19,8 / 21,8 m | 100 % | 100 · 57 · 47 · 67 % | 53–61 % |
| không giới hạn | 31,5 (0 %) | 11,8 | 22,9 / 22,0 m | 100 % | 100 · 62 · 46 · 65 % | 57–64 % |

**Đọc bảng:**
- **Tầm 12–20 đạt nhiều nhất ở 1,75–2,5 W** (80–84 % số lần tung).
- **Thắng có "vách":**
  - dưới 2,5 W nhiều bot thua lại; ở 1,25 W, Mới → Nhanh chỉ thắng 0–60 %, Chuẩn thua mọi seed;
  - từ 2,5 W trở lên, mọi bot Mới → Nhanh thắng 95–100 %, vượt dải 75–90 %.
- **Không mức nào đưa ô 2 về ≤ 20 %.** Ngay ở 1,25 W, khi bot đã thua lại, ô 2 vẫn chiếm 29–36 %.
- **P của Chuẩn vẫn 46–67 % ở mọi mức** (đích 15–35 %). Riêng ô 2 không cân được cả trận; phần còn lại là việc của nhịp sinh, Kết Giới và các ô khác (SKILL_REACH §5).
- **Đánh đổi của ngân sách:** càng nhỏ thì sát thương càng dừng gần Trận Tâm. Ở 2,5 W, lúc đông, rồng vẫn chạy tới cổng nhưng chỉ "cắn" thú trong khoảng 15–20 m đầu.

**Hai biến thể của bài đo sáng** (trên mã trước sửa, giữ để tham khảo):
- "Hẹp" (mọi khối hẹp một nửa) vẫn trúng 29,4 con và làm hỏng việc phủ đường (68 %).
- "Sàn 10 %" (từ con thứ 7 chỉ nhận 10 %) vẫn trúng 38 con, ô 2 vẫn 43–52 % sát thương.
- Cả hai cho cùng bài học: phải hãm bằng ngân sách mỗi lần tung, không bằng bề rộng. Bản sau sửa làm đúng như vậy.

### 8.7 Lab: tấm khung, clip và phím tới đòn đầu

**Tấm khung và clip ở camera chơi** (ngoài Git, trong `games/immortality-cultivation/tmp/shots/dragon/greybox/`; chụp trên mã trước sửa):
- `twin-pearl-greybox-play-1280x720-sheet.jpg`: bảy khung chụp ở 1280 × 720, mỗi ô nửa cỡ (tấm 1280 × 1440).
- `twin-pearl-greybox-play-1920x1080-sheet.jpg`: cùng bảy khung chụp ở 1920 × 1080 (tấm 1920 × 2160).
- `twin-pearl-greybox-play-1280-real-then-quarter.mp4`: 1280 × 720, 60 fps, 18,4 s. Từ F−20 tới F200 ở tốc độ thật (3,7 s), rồi chính đoạn đó ở 0,25× (14,7 s). Thấy cả hai đường và cả hai góc trời.
- Số và kịch bản chụp: `section8/capture-1280.json`, `section8/capture-1920.json`, `section8/capture-frames.mjs`.
- Khối trúng và khung không đổi sau sửa, nên tấm khung và clip vẫn đúng về hình học. Chỉ khác con nào bị trúng: nay ít con đổi màu hơn, nhất là gần cổng.

**Cách chụp:**
- Lab `skills-lab.html?key2=twin-pearl&fixed=1`. `fixed=1` là chế độ chụp từng bước của lab: không rAF, mỗi khung đúng một tick sim, nên F0 … F200 là tick thật. Không cờ nào khác: chất lượng mặc định High, tỉ lệ điểm ảnh không ghim.
- Camera chơi mặc định của lab: 55°, FOV 28°, cả sân; lab báo khoảng cách 53,51 m.
- Bảng phím của lab (góc trên trái, rộng 400 px) che đường A và cổng A ở khổ 1280. Lúc chụp, bảng này được ẩn bằng một dòng đổi style, không phải cờ URL. Băng tên pha ở trên và ô số của hộp xám ở góc dưới phải vẫn giữ.
- Triều: triều đông nhất lab dựng được, 44 thú đất trên hai đường và 4 quạ (lab tự bơm lại ở cổng). Chạy 200 tick cho triều trải ra, rồi bấm phím 2 ở tick 201.

**Bảy khung:**

| Khung | Thấy gì |
|---|---|
| F0 | Hộp giữ 8 × 8 m trước Trận Tâm lóe |
| F2 | Hai hộp chạm trên hai đường, hai sợi sáng nối từ kiếm |
| F20 | Hai đầu rồng đi được nửa đường, đường S và vệt sau thân hiện rõ trên cả hai đường |
| F42 | Hai đầu ở hai cổng; hai cột quét trời ở hai góc; ngọc treo ở điểm gặp (0; −9,25) |
| F51 | Hoa sen nở: hai cánh dài dọc hai đường, vùng giữ, đĩa r 9 m |
| F80 | Vệt gần cổng vẫn là khối trúng (khối cuối của sim ở F96); thú bị trúng lần 2 chuyển màu cam |
| F200 | Dư âm, chỉ có hình, không còn đòn |

**Phím tới đòn đầu, đo lại sau sửa** (`section8/` cũ dùng mốc "vẽ xong", review chỉ ra đó chỉ là lúc lệnh vẽ trả về):
- Kịch bản `review/latency-keys-v2.mjs`, kết quả `review/latency-v2.json`.
- Chrome không giao diện qua `heavy.sh --perf`, High, 1920 × 1080, khung rAF thật, phím thật qua CDP. 10 lần tung, có cả lần bấm đầu tiên của trang.
- Đòn đầu ở F0 cả 10 lần.
- **Phím → hiện ≤ 17,4–30,9 ms:** mốc thời gian của khung rAF kế tiếp sau khung có đòn đầu. Khung kia chắc chắn đã hiện lúc đó, nên đây là cận trên.
- **Phím → nộp:** 3,3–18,6 ms (lệnh vẽ trả về, cách đo cũ).
- Cùng lúc lab báo: 41–48 thú sống, 15–20 con khác nhau bị trúng, trái/phải 46/54 tới 52/48, ngân sách mỗi lần tung (594–640 máu) gần cạn.
- Việc hoãn tạo `AudioContext` tới sau khung của phím nay chỉ áp khi có `?key2=twin-pearl`. Các phiên lab khác mở âm thanh ngay trên phím, như trước. Trong Safari, ngữ cảnh âm thanh có thể bắt đầu ở trạng thái treo tới phím kế tiếp.

**Lưu ý khi xem:** ở 1280 × 720, nhãn chữ nhỏ nhưng đọc được. Ở F42, hai đầu rồng nằm sát mép xa của sân. Đây vẫn là hộp xám: hình trong mờ và nhãn, không có art.

### 8.8 Câu hỏi cho anh

1. **Ô 2 được chiếm bao nhiêu sát thương cả trận?**
   - Canon §7.3 cho mỗi chiêu vùng ≤ 20 %. Song Long sau sửa chiếm 41–50 %. Quét §8.6 cho thấy không mức ngân sách nào về ≤ 20 % mà bot còn thắng được.
   - Claude đề xuất cho chiêu biểu tượng của bộ Kiếm × Hỏa một trần riêng cao hơn 20 %, với ngân sách 2–2,5 W mỗi bên (ô 2 chiếm 41–46 % ở bot Chuẩn). Phần còn lại của cân bằng (P quá cao, thắng quá cao ở 2,5 W) làm bằng nhịp sinh và các ô khác theo BALANCE.md. Ngân sách thử giữ 2,5 W tới khi anh chọn.
   - Nếu anh giữ 20 % thì phải đổi thiết kế chứ không chỉ đổi số, ví dụ hồi chiêu dài hơn nhiều hoặc chỉ một rồng mỗi lần tung.
2. **Lúc đông, rồng có cần cắn tới tận cổng không?**
   - Với ngân sách, đích 12–20 thú và việc phủ hình học trọn hai đường cùng đạt. Nhưng lúc đông, sát thương dừng ở 15–20 m từ Trận Tâm; rồng vẫn chạy tới cổng.
   - Claude đề xuất giữ như vậy (thú gần Trận Tâm nguy hơn). Phần nhìn sẽ cho thấy rồng "hết sức": đầu và vệt nhạt dần khi bên đó cạn ngân sách.
   - Nếu anh muốn sát thương tới cổng thì phải chia ngân sách theo quãng đường thay vì tới trước, và chấp nhận mỗi con nhận ít hơn.

### 8.9 Giới hạn của bài đo

1. **Bot là bot đo của SKILL_REACH**, không phải làn 7. Mọi giới hạn ở SKILL_REACH §6 vẫn còn: không Backspace, mua theo thứ tự cố định, Đứng yên, không Học trước.
   - Với Song Long, bot coi mọi thú sống là "trong tầm" nên tung ô 2 ngay khi sẵn. Người thật có thể giữ chiêu chờ lúc đông; khi đó ngân sách giữ cho mỗi lần tung không mạnh hơn.
2. **"Thừa" đếm thiếu một chút:** đòn tiềm năng chưa tính ×1,5 phá thế. Đòn 0 sát thương (trần cụm hay ngân sách đã hết) không có sự kiện nên không thấy.
3. **Phần của chiêu** đọc từ sổ của sim cho mỗi lần tung (mỗi tick một loại đòn mỗi con). Trường hợp hiếm có đòn 0 sát thương xen vào thì loại đòn được đoán theo khung.
4. **Mẫu lúc 35–45 thú nhỏ:** quét đỉnh chỉ có 92 lần, 85 % từ đỉnh đợt 6. Chỉ các trận còn sống tới đó mới góp mẫu.
5. **Triều trong lab là triều riêng của lab** (đặt thú theo đường, đông nhất 44 + 4 quạ), không phải ảnh chụp đỉnh của bot.
6. **Sai số:** 20 seed mỗi hồ sơ, nên tỉ lệ thắng sai khoảng ±10 điểm %. Bot Trẻ em chạy ở Cân bằng.
7. **"Đòn xa nhất"** đo theo đường chim bay tới Trận Tâm, không theo quãng đường đi của thú.

### 8.10 Tái lập

Từ `games/immortality-cultivation`. Mọi file ở `tmp/skill-reach/`, ngoài Git.

| Việc | Lệnh |
|---|---|
| Ma trận (trận thật và quét đỉnh) | `KEY2_OUT=tmp/skill-reach/key2-fix ../../.local/bin/heavy.sh --cores=6 tmp/skill-reach/key2-matrix.sh line twin-pearl twin-pearl+pool100000s100000 twin-pearl+pool125 twin-pearl+pool150 twin-pearl+pool175 twin-pearl+pool200 twin-pearl+pool375 twin-pearl+pool500` (5 phút trên 6 lõi) |
| Gộp số → `tmp/skill-reach/key2-fix/numbers.json` và `aggregate.txt` | `KEY2_ROOT=tmp/skill-reach/key2-fix KEY2_VARIANTS="line twin-pearl …" node_modules/.bin/tsx tmp/skill-reach/key2-aggregate.ts` |
| Một trận lẻ | `node_modules/.bin/tsx tmp/skill-reach/bot.ts <thư mục> w45a97@twin-pearl 1 20` |
| Kiểm cờ tắt | 9 hồ sơ × seed 1–4 với `BOT_HASHES=1` vào `tmp/skill-reach/key2-review/golden-now/`, so với `tmp/shots/dragon/greybox/golden-before/`; test `tests/sim/twin-pearl.test.ts` có băm ghim |
| Đo phím tới đòn đầu | `vite --port 3241` trên cây sạch, rồi `URL=http://127.0.0.1:3241/skills-lab.html ../../.local/bin/heavy.sh --perf node src/kit/tools/cdp-run.mjs tmp/shots/dragon/greybox/review/latency-keys-v2.mjs --width=1920 --height=1080` |
| Chụp lab | như bản sáng: `section8/capture-frames.mjs` với `cdp-run.mjs` (§8.7) |

Bản số trước sửa vẫn ở `tmp/skill-reach/key2/numbers.json`. Khung chụp thô đã xóa; giữ hai tấm khung, clip và số.

### 8.11 Review 04/11 chiều: sửa gì, bác gì

Một review độc lập kiểm hộp xám, chạy lại bot ở `6e68958` và `1a78a82`, và thử đột biến trên bản sao. Từng mục đã được kiểm trên mã:

| # | Mục | Việc |
|---|---|---|
| 1 | Tầm 35,4 con, đích 12–20 | Đúng. Ngân sách (mục 2) đưa về 17,2 con, 80 % trong đích. Không thêm trần số con. |
| 2 | Không có ngân sách mỗi lần tung | Đúng. **Sửa:** ngân sách mỗi bên, chia theo phần (§8.6). |
| 3 | Trần cụm 60 % đặt lại ở mỗi khối, mỗi tick (cụm có thể mất 93,6 %) | Đúng. **Sửa:** cả lần tung là một đòn vùng. |
| 4 | Test không giữ luật (7 đột biến vẫn qua) | Đúng. **Sửa:** 27 test, có băm ghim của cờ tắt. 11 đột biến đều làm hỏng ít nhất một test. |
| 5 | Đường A được lợi do thứ tự tính | Đúng. **Sửa:** mỗi bên có hệ số giảm dần và ngân sách riêng; mỗi tick một thứ tự chung. |
| 6 | `rulesHash` không phủ bảng thử | Đúng. **Sửa:** chỉ khi header có cờ; không có cờ thì giá trị băm như cũ. |
| 7 | Chiêu giải khi chỉ còn Vương đang gầm | Đúng. **Sửa:** chỉ giải khi có thú nhận được sát thương; thú miễn sát thương không vào sổ. |
| 8 | Hiệu năng | Đúng, không phải vấn đề (5,3 µs mỗi tick). **Dọn** các chỗ rẻ. |
| 9 | Lab: hoãn âm thanh ở mọi phiên; mốc "vẽ" chưa phải lúc hiện | Đúng. **Sửa** cả hai (§8.7). |
| — | Thú bầy 1 máu không chết vì đòn vùng (`combat.ts`) | Đúng, nhưng **không sửa ở đây**: luật chung, sửa sẽ đổi trận mặc định. Làm riêng, kèm golden. |
| — | Đòn đường thẳng còn chờ bị tính vào lần tung đang đo (5 lần) | Đúng. **Sửa** trong công cụ đo (ngoài Git). |

**Đính chính các số của bản §8 trước:**
- "Phủ 100 % mỗi đường": chỉ đúng khi tính mọi khối; riêng thân rồng phủ 66,7 % (§8.1).
- "Khoảng 4 điểm lệch trái do thứ tự tính": review đo được 1–2 điểm ở đỉnh thật và 1,2–3,7 điểm ở đám thú đối xứng. Nay không còn lệch.
- "5–7 lần tung mỗi phút": là mỗi phút đánh; trên cả trận là 4,5 lần.
- "Đòn đầu muộn 0,2 %": nay 0,03 %, vì đã bỏ các lần tung chỉ có Vương đang gầm.
- "Phím tới đòn đầu 2,5–20 ms": là lúc lệnh vẽ trả về; lúc hiện là ≤ 17,4–30,9 ms (§8.7).
- "Một lần tuyệt kỹ ra 4,1 W": review chưa chạy lại; nay đã kiểm, đúng 4,1 W (hôm nay).

## 9. Song Long toàn sân, không phụ thuộc map (04/11/2026, chiều)

**Vì sao làm lại:** quyết định của anh lúc 11:50 (đầu tài liệu): chiêu dùng chung cho nhiều map, nên không được chạy về hai cổng; nó phải là chiêu diện rộng toàn sân. Giữ hai rồng, một viên ngọc và cao trào hoa sen. Mục này thay §3 A ở phần hình học và khung; luật sát thương của hộp xám (§8.6, `hit()`, cách chia và tiêu ngân sách) giữ nguyên; riêng mức ngân sách nay là 2,0 W mỗi bên cộng 0,8 W trời (§9.0 mục 7, §9.11). Hộp xám hai hành lang (§8) chỉ còn là số đo để so.

### 9.0 Chốt

1. **Đầu vào chỉ có ba thứ:** khung sân (hình chữ nhật), Trận Tâm H và chỗ người ra chiêu C, và ảnh chụp mọi thú sống nhận được sát thương ở F0 (vị trí, độ cao). Không đọc nhãn cổng, đường đi, waypoint, trường dòng chảy hay điểm vào của quạ.
2. **Hai rồng chia đôi triều thú theo hướng ngang của người chơi:** trục F đi từ người chơi tới Trận Tâm, trục R vuông góc. Xếp thú theo tọa độ ngang, nửa trái cho rồng 0, nửa phải cho rồng 1; số thú hai bên lệch nhau tối đa 1 con.
3. **Mỗi rồng bay một vòng qua tối đa 3 "điểm neo" rồi về ngọc.** Điểm neo chọn bằng cách lấy điểm xa nhất (farthest-point sampling): con xa Trận Tâm nhất, rồi con xa nhất so với người chơi, ngọc và các neo đã chọn. Thứ tự bay là thứ tự ngắn nhất trong tối đa 6 cách. Rồng vẫn bay sóng chữ S như hộp xám, thân và vệt cháy như cũ.
4. **Ngọc** ở 3/5 đường từ Trận Tâm tới tâm khối thú đất, không quá 12 m, cách mép sân ít nhất 2 m. **Hoa sen** nở ở ngọc.
5. **Khung giữ tinh thần cũ, kéo dài 6 tick cho đường bay dài hơn:** F0 đòn ở Trận Tâm, F1–F2 hai đĩa F1 (đĩa đất hoặc đĩa trời), F3–F48 hai đầu rồng bay, F30–F56 đuôi quét quạ, F49–F56 nhịp gầm, F57–F77 hoa sen, vệt cháy trúng tới F102, hình tới F300.
6. **Luật sát thương giữ nguyên máy:** 3 loại đòn, 15/45/40 %, mỗi thú tối đa 3 đòn cách nhau ≥ 20 tick, mỗi bên một thang giảm dần và một ngân sách, cả lần tung là một đòn vùng (trần cụm 60 %), trần Vương 1,5 W, một thứ tự đánh mỗi tick. Đổi hai chỗ: bên của thú theo §9.3 (thay theo cổng), và "khoảng cách tới Trận Tâm" trong thứ tự đánh nay là đường chim bay, không theo trường dòng chảy. F1 thêm đĩa trời cho quạ (loại hành lang, phần trời).
7. **Ngân sách 2,0 W mỗi bên cộng 0,8 W trời** (anh duyệt 04/11, khoảng 19:40, §9.11): ô 2 là ngoại lệ có tên, chiếm ≤ 45 % sát thương cả trận lúc này; sau phần 2 của SKILL_REACH xuống ≤ 35 %, rồi thử 20 %. Bot quét lại 1,25–3,75 W mỗi bên để kiểm.

### 9.1 Cách làm và kết quả duyệt

**Đường đã dùng: ChatGPT bốn lượt, không lượt nào đạt hai PASS liên tiếp; Gemini không nhận được bản nào đã qua để duyệt; Claude tự phân tích và các giám khảo Claude độc lập duyệt** (luật bước 9 của `agent-orchestration`, anh thêm lúc 14:00: ChatGPT hay Gemini không được làm chặn việc).

| Lượt | Đề bài | Kết quả các lần tự duyệt | Vì sao dừng |
|---|---|---|---|
| ChatGPT 1 | Thiết kế mở, đủ cả sát thương | FAIL, FAIL, FAIL | Mỗi lần tự sửa lại thêm luật ngân sách mới (trần mỗi thú, ngân sách để dành), rồi lần sau thấy lỗi trong chính luật đó. Dừng theo luật 4 lượt |
| ChatGPT 2 | Chỉ hình học, luật sát thương cố định | FAIL, FAIL, FAIL | Lưới mật độ, lưới quét và chèn điểm rẻ nhất sinh lỗi biên mới mỗi lượt; đề ra trần đường dài 3 × đường chéo sân (143 m) |
| ChatGPT 3 | Sửa một bản đơn giản do Claude viết | FAIL, **PASS**, FAIL | Lượt 3 thấy hai lỗi thật (quạ chạm ở F1 phải là đòn hành lang lấy ngân sách trời; mục tiêu F1 phải nhận được sát thương dương). Đã sửa |
| ChatGPT 4 | Bản hội tụ của lượt 3 cộng ba sửa của Claude | Chưa có câu trả lời | Anh dừng mọi việc lúc 14:02. Lúc 14:06 khung trình duyệt mở lại hiện trang chưa đăng nhập ở cả chatgpt.com và gemini.google.com; điều phối viên kiểm lại lúc 14:55 thì cả hai vẫn đăng nhập, nên báo "đăng xuất" chỉ đúng với phiên khung trình duyệt đó. Theo bước 9, Claude không chờ |
| Gemini | Duyệt bản đã qua của ChatGPT | Không chạy | ChatGPT chưa có bản nào qua hai lần liên tiếp để chuyển sang; 4 Argon hết hạn mức tới 13:23; sau 14:02 đi đường Claude |
| Claude | Phân tích, nguyên mẫu hình học (`proto.py`, ngoài Git), viết §9; giám khảo Claude độc lập, mỗi lần một agent mới chưa viết bản này | Cả §9 một lượt: FAIL, FAIL, FAIL (dừng, chia gói). Thiết kế §9.0–9.11: FAIL, PASS, PASS. Phiếu (§9.12) một lượt: FAIL, FAIL, FAIL (dừng, tách hai phiếu). Phiếu 1: FAIL, FAIL, PASS, PASS. Phiếu 2: lượt đầu FAIL, FAIL, FAIL (dừng; sửa rồi chạy lượt mới với giám khảo mới); lượt sau FAIL, FAIL, PASS, PASS | Thiết kế, phiếu 1 và phiếu 2 đều qua hai PASS liên tiếp trên đúng bản được giao |

Bản ghi nguyên văn và bảng kiểm: [`source/dragon-fieldwide-chatgpt-2026-11-04.md`](source/dragon-fieldwide-chatgpt-2026-11-04.md), [`source/dragon-fieldwide-gemini-2026-11-04.md`](source/dragon-fieldwide-gemini-2026-11-04.md), [`source/dragon-fieldwide-critics-2026-11-04.md`](source/dragon-fieldwide-critics-2026-11-04.md).

**Bài học cho các lượt sau:** đề bài "thiết kế mở, đủ chi tiết để code theo" làm ChatGPT tự sinh máy móc mới và tự đánh trượt nó mãi. Đưa nó một bản đơn giản để sửa thì hội tụ sau 3 lượt.

### 9.2 Đầu vào và ảnh chụp F0

Đọc một lần ở F0, trước đòn F0:
- khung sân `stage.field` (minX, maxX, minZ, maxZ);
- Trận Tâm H (hôm nay là gốc tọa độ) và C = `cast.origin`;
- mọi thú `alive && !damageImmune`: serial, slot, x, z, y. Thú đất là thú ở dải đất (≤ 1,5 m), thú trời là thú ở dải trời (2,5–6 m).

Bản ghi của lần tung lưu (toàn số nguyên) H, F, R, `cut2`, P, bên của từng con, các cặp [slot, serial] của ảnh chụp và hình học dựng ra (nút, mẫu, `pass`, neo trời); vị trí F0 của thú chỉ dùng lúc dựng (công cụ đo tự ghi lại khi cần gọi `staticCoverage`). Sau F0 thú vẫn đi như thường; mọi khối trúng thử vị trí thật ở tick đang chạy. Chỉ hình học là cố định từ F0.

**Điều kiện giải** (Claude chốt ngày 04/11 tối, sau lượt quét độc lập 271b; Codex sửa ở phiếu 271c): chiêu chỉ giải khi có ít nhất một thú sống, không miễn sát thương, và ở dải đất hoặc dải trời. Không có con nào như vậy (ví dụ chỉ còn thú ở giữa hai dải, 1,5–2,5 m) thì Cast được giữ như hôm nay, không tốn hồi chiêu 8 s.

**Sân trống:** trong trận và trong lab, chiêu chỉ giải theo điều kiện trên, nên hình dạng sân trống chỉ gặp khi gọi thẳng hàm dựng hình học (test, công cụ): ngọc ở H + 9 m theo F, mỗi rồng bay một "vòng cánh" (§9.4); không có đòn.

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
| Ngân sách mỗi bên | 2,0 W đất (chạm / hành lang / hoa sen 15/45/40) + 0,8 W trời, × M_q × bucket | Anh duyệt (§9.11); hộp xám cũ dùng 2,5 W. Mỗi phần (0,3 / 0,9 / 0,8 W) nhỏ hơn đòn đầu cùng loại (0,375 / 1,125 / 1,0 W), nên một con đơn độc mỗi bên nhận tối đa 2,0 W, 80 % ô 2 hôm nay (mốc "một con nhận đủ như ô 2 hôm nay" của §8.6 không còn). Quét lại ở §9.8 |
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

**Gemini:** không góp lượt này (§9.1; [`source/dragon-fieldwide-gemini-2026-11-04.md`](source/dragon-fieldwide-gemini-2026-11-04.md)).

**Giám khảo Claude độc lập:** 20 lần, mỗi lần một agent mới chưa viết bản này (đếm ở §9.1). Mọi lỗi của các lần FAIL đã sửa trước lần duyệt kế. Thiết kế, phiếu 1 (Codex 271, đã merge vào main của game ở `35f1b77`, gồm 271b và 271c) và phiếu 2 (Codex 272) đều qua hai PASS liên tiếp trên đúng bản giao cho Codex. Quyết định của anh lúc 19:40 được đưa vào sau khi phần thiết kế và phiếu 1 đã qua; hai lần duyệt cuối của phiếu 2 kiểm cả việc đưa các quyết định đó vào toàn §9. Các góp ý không chặn của giám khảo (để làm ở bước sau) ghi trong bản ghi: [`source/dragon-fieldwide-critics-2026-11-04.md`](source/dragon-fieldwide-critics-2026-11-04.md).

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

**Trạng thái (04/11/2026, tối):**
- Phiếu 1 giao cho Codex là phiếu 271 (bản §9 giao kèm: `docs/codex-queue/271/section9-design.md`), cùng 271b (lượt quét độc lập 200 bố cục ngẫu nhiên) và 271c (điều kiện giải theo dải, §9.2). Đã merge vào main của game ở `35f1b77`: 960/960 test, tsc sạch.
- Phiếu 2 là phiếu 272 (`docs/codex-queue/272-tt-twin-pearl-fieldwide-bot.md`, bản §9 giao kèm: `docs/codex-queue/272/section9-design.md`), chạy sau phiếu 273b.
- Sau bản giao phiếu 271, phần phiếu 1 dưới đây còn đổi ba chỗ: chú thích JSDoc của `pool` theo 2,0 W (A), các test ngân sách 2,0 W (D), và điều kiện giải theo dải (B.9, đã làm ở 271c). Hai chỗ đầu là việc kiểm lại sau phiếu 271.

**Thợ:** Codex `gpt-6.1-sol`, effort `xhigh` (code và logic), một lane, **hai phiếu nối nhau**: phiếu 1 là A–E (nội dung, sim, lab, test); phiếu 2 là F (bot và số đo), giao sau khi Claude đã duyệt và merge phiếu 1. Sandbox `workspace-write`, thư mục làm việc là cây riêng `/Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-twin-fieldwide` trên nhánh `codex/twin-pearl-fieldwide` (không dùng `games/.wt-immortality-cultivation-codex`: cây đó dành cho phiếu 259). Mọi đường dẫn dưới đây tính từ thư mục đó. Báo cáo của Codex là tin nhắn cuối (`run.sh` lưu ở `.local/codex-runs/<id>/last.md`); Claude chép nó vào `docs/codex-queue/` của repo cha. Codex không commit; Claude chạy lại kiểm tra, đọc diff, rồi mới merge.

**Claude chuẩn bị trước khi giao** (Codex không tự làm):
1. `git -C /Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation worktree add ../.wt-ic-twin-fieldwide -b codex/twin-pearl-fieldwide main`, rồi `ln -s ../immortality-cultivation/node_modules /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-twin-fieldwide/node_modules` (liên kết như phiếu 255). Phiếu 2 dùng lại đúng cây và nhánh này sau khi Claude đã merge phiếu 1 (cây vẫn giữ bản chép `tmp/skill-reach/` của bước 2). Vì liên kết đó, mọi lệnh test và build ở E.1 dùng đúng dạng của báo cáo 255 (không ghi gì vào `node_modules` của cây chính).
2. Chép `tmp/skill-reach/` của cây chính vào cây mới (bot nhập `../../src/...` theo thư mục của chính nó, nên phải chạy bản trong cây mới).
3. Golden cờ tắt để so nằm ở đường tuyệt đối `/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/tmp/shots/dragon/greybox/golden-before/`.
4. Ghi hai phiếu ở `docs/codex-queue/` của repo cha. **Phiếu 1** `<n>-tt-twin-pearl-fieldwide.md`: dòng đầu "Thiết kế, chỉ đọc: `/Volumes/SS990TPRO/htdocs/typing-game/docs/games/tu-tien/skills/DRAGON_SKILL.md` §9.0–§9.11; mọi §9.x trong phiếu là của file này", rồi phần đầu §9.12 và A–E. **Phiếu 2** `<n+1>-tt-twin-pearl-fieldwide-bot.md`: cùng dòng đầu nhưng "§9.0–§9.11 và §8", phần đầu §9.12, B.1, B.3, dòng tiêu đề của B.4 (`buildCastGeometry`), B.6, dòng đầu của B.7 (`pickDiscs` ở t = 1), dòng "Sân tổng hợp cho test" của D, và F. Trước khi chạy phiếu 2: `git -C /Volumes/SS990TPRO/htdocs/typing-game/games/.wt-ic-twin-fieldwide merge --ff-only main` để cây có đúng bản phiếu 1 đã merge. Chạy lần lượt (phiếu 2 sau khi phiếu 1 đã merge): `tools/codex-run/run.sh <n>-tt-twin-pearl-fieldwide docs/codex-queue/<n>-tt-twin-pearl-fieldwide.md games/.wt-ic-twin-fieldwide xhigh workspace-write`, và tương tự cho phiếu 2.

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

Đổi `pool.sideW100` từ 250 thành **200** (2,0 W mỗi bên, anh duyệt, §9.11); `pool.skyW100` giữ 80. Viết lại chú thích JSDoc của `pool` theo 2,0 W mỗi bên (anh, 04/11): một con đơn độc mỗi bên nhận tối đa 2,0 W. Giữ `SwordKey2`, `SWORD_KEY2_VARIANTS`, `id`, `name`, `sharesPct`, `maxHits`, `rehitTicks`, `bossCapW100`, `trailTicks`, `groundTopMm`. Thay phần hình học:

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

**B.9 `resolveTwinPearl`:** điều kiện giải: có ít nhất một thú sống, `!damageImmune`, ở dải đất hoặc dải trời (§9.2; phiếu 271c); không có thì trả `false`, Cast được giữ. Gọi `buildCastGeometry` rồi đẩy bản ghi. Ngân sách vẫn từ `twinPearlPool`.

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
- hệ số giảm dần mỗi bên, sàn 40 %; ngân sách mỗi bên và mỗi phần (nay 2,0 W mỗi bên chia 15/45/40, cộng 0,8 W trời), không phần nào vượt. Với 2,0 W, các phần nhỏ hơn đòn đầu cùng loại, nên: test phần 15/45/40 bơm ngân sách (`cast.pool.fill(10 ** 9)` ngay sau khi giải) để 15/45/40 % của 2,5 W rơi đúng như cũ; thêm một ca một con đơn độc không bơm, chờ [27, 81, 72] máu (chạm, hành lang, hoa sen) ở chất lượng của test hiện có; test ngân sách đổi tên thành 2,0 W và ghim các phần [27, 81, 72, 72]; chú thích máu trong test Thế đổi thành 27 / 108 / 180;
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
     - đọc ngay lúc bắt đầu ghi lần tung (`start()`: trong quét đỉnh là ngay sau `resolveCast`, trong trận là sau tick F0; trong trận vị trí có thể lệch vài cm vì một số bước sau kỹ năng cũng dời thú, chỉ ảnh hưởng số phủ của trận thật, không có ngưỡng), trước khi `sideFor` có thể ghi đè `sideSlot` cho một slot dùng lại: số thú ảnh chụp mỗi bên, tách đất và trời (đếm `snapshot` theo `sideSlot` và dải độ cao); số quạ mỗi bên;
     - vị trí F0 (x, z, y) của các thú ảnh chụp lúc tung; khi lần tung đã qua t = 1 (sau tick có `pickDiscs`), gọi `staticCoverage` mỗi lần tung hai lần, một lần với các điểm đất và một lần với các điểm trời; số chung là tổng hai số đó, chia cho mọi thú ảnh chụp (kể cả thú ở giữa hai dải);
     - số con bị trúng và sát thương mỗi bên, theo `cast.book[].side`; số thú ảnh chụp ở dải trời nhận ≥ 1 đòn dương (cho số quạ bị trúng; không dùng `crowsHit` cũ theo nhãn cổng);
     - tầm xa mỗi bên: đòn hiệu dụng xa nhất lên thú ở dải đất (≤ 1,5 m) tới H, như §8.1; và số thú đất ảnh chụp ở xa H hơn 12 m, số trong đó bị trúng;
     - phần theo loại đòn (đĩa F0, đĩa F1 đất, đĩa F1 trời, thân, trời, hoa sen đầy, hoa sen nửa): sát thương, số đòn, số con hạ. Mỗi sự kiện `hit` của lần tung xếp vào một phần theo tick so với F0, dải độ cao của thú và loại đòn vừa thêm vào `book` của nó (`kinds`): t = 0 là đĩa F0; t = 1–2, chạm là đĩa F1 đất, hành lang ở dải trời là đĩa F1 trời; hành lang ở dải đất là thân; hành lang ở dải trời từ t = 30 là trời; hoa sen đầy hay nửa theo `lotusRegion(cast, x, z)` ở vị trí lúc trúng;
     - `firstHit` (tick từ F0 tới đòn dương đầu tiên; −1 nếu không có) và, khi −1, lý do theo luật: xét các thú trong `book` của lần tung không nhận đòn dương nào; có con thuộc cụm bầy là `clusterCap`; có Vương là `bossCap`; ngược lại, nếu phần ngân sách tương ứng bằng 0 là `budget`; còn lại là `other`;
   - bộ ghi chỉ đọc: không gọi `sideFor`, `pickDiscs` hay hàm nào ghi vào bản ghi lần tung; vị trí ảnh chụp đọc từ `world.beasts.list[slot]` có kiểm `serial` (không dùng `beastByRef`, vì nó trả `null` cho con chết ngay ở F0, làm mất con đó khỏi số phủ và số đất/trời);
   - tên các phần mới bằng tiếng Anh: `f0Disc`, `f1Ground`, `f1Sky`, `body`, `sky`, `lotusFull`, `lotusHalf`;
   - sau bước này `key2-measure.ts` không còn nhập tên nào đã bỏ.
2. `key2-numbers.ts`: bỏ biến thể "narrow" (nó ghi vào các trường đã bỏ `touch.halfWidthMm`, `hold.halfWidthMm`). `+pool<N>` giữ nguyên (đổi `pool.sideW100` thành N trong bộ nhớ). Sửa luôn danh sách biến thể mặc định trong `key2-matrix.sh` và các dòng hướng dẫn trong `bot.ts`, `key2-dense.ts` còn nhắc `+narrow`.
3. `key2-aggregate.ts`, cho nhóm 35–45 và in như §8.2–8.6:
   - nhóm "35–45 thú" theo **thú đất trong ảnh chụp** (như §8.2; nhóm này quyết định đạt/trượt), in thêm nhóm theo mọi thú trong ảnh chụp để tham khảo;
   - số con bị trúng (trung vị, p10–p90, phần lần tung trong 12–20), `coverageStatic` (chung, đất, trời);
   - cân hai bên: chỉ tính lần tung mà mỗi bên có ≥ 5 thú trong ảnh chụp F0;
   - quạ bị trúng = số quạ ảnh chụp (dải trời) nhận ≥ 1 đòn dương chia số quạ ảnh chụp, tách theo phần (`f1Sky` hay `sky`), in riêng cho các lần tung có ≥ 2 quạ ở cùng một bên (đĩa F1 có thể tiêu hết ngân sách trời của bên đó cho con quạ đầu);
   - tầm xa: trung vị đòn xa nhất mỗi bên, phần thú đất > 12 m bị trúng (như §8.2);
   - phần theo loại đòn: % sát thương, đòn và hạ mỗi lần tung (như §8.3); thêm vào danh sách `PARTS` cố định của `key2-aggregate.ts` mọi phần mới (đĩa F0, đĩa F1 đất, đĩa F1 trời, thân, trời, hoa sen đầy, hoa sen nửa), để không phần nào bị bỏ sót khi in;
   - đòn đầu trong trận thật: số lần tung, số lần `firstHit > 2`, và danh sách riêng các lần `firstHit = −1` kèm lý do;
   - khối "canon" in thêm dòng ô 2/cả trận ≤ 45 % ở bot Chuẩn (đích anh duyệt) cạnh dòng ≤ 20 % cũ;
   - cột so: đọc thêm `tmp/skill-reach/key2-fix/numbers.json` (các biến thể `line`, `twin-pearl` là hai hành lang 2,5 W, `twin-pearl+pool200` là hai hành lang 2,0 W) và in cạnh số mới; không cần chạy lại các biến thể đó.
4. `key2-layouts.ts` mới (theo §9.8 bot bước 3):
   - dựng từng bố cục của §9.8 theo đúng thứ tự tạo; đấu trường trên sân tổng hợp `{ ...THANH_THACH_AI, id: "test-arena", field: { ...THANH_THACH_AI.field, minXMm: −20_000, maxXMm: 20_000, minZMm: −20_000, maxZMm: 20_000, mechSlots: [], pillars: [] } }`; thế giới có cờ dựng như `twinWorld` trong `tests/sim/twin-pearl.test.ts`;
   - tung một lần với origin (0; 3), chỉ bước kỹ năng; sân trống gọi thẳng `buildCastGeometry`;
   - in: hai bên, P, độ dài đường nút, cung cuối, tốc đầu rồng (cung cuối chia (`heads.toTick` − `heads.fromTick`) / 60 s), `coverageStatic` (dạng số con / tổng), số con bị trúng, đòn đầu, chia hai bên.
5. Một script so cờ tắt nhỏ trong `tmp/skill-reach/` (kiểm 1 dưới đây).
6. **Cast không giải** (§9.2: không có thú nào ở dải đất hay dải trời): không phải một lần tung. Trong trận, bot giữ hành vi của game (Cast được giữ, không tốn hồi chiêu), `key2-measure.ts` không mở bản ghi lần tung nào, và mỗi trận ghi hai số: `key2Held` (số sự kiện `cast` của ô 2 có `state` "held") và `key2Fizzled` (số sự kiện `cast` của ô 2 có `state` "fizzled"). Trong quét đỉnh (`key2-dense.ts`), khi `resolveCast` trả `false` thì bỏ mẫu đó và lưu số "không giải" vào JSON đầu ra (trường `unresolved`). `key2-aggregate.ts` in, theo từng biến thể, tổng `key2Held`, tổng `key2Fizzled` của trận thật và tổng `unresolved` của quét đỉnh trong `aggregate.txt`; các số này không vào mẫu số của các chỉ số theo lần tung.

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
   - đòn đầu F0 hoặc F1 ở mọi lần tung có đòn dương; lần `firstHit = −1` liệt kê riêng kèm lý do, như kiểm 4;
   - quạ ≥ 90 % (in riêng nhóm ≥ 2 quạ một bên);
   - cân hai bên 40/60–60/40 ở ≥ 85 % lần tung đủ điều kiện.
4. **Trận thật, biến thể `twin-pearl`, mọi lần tung:** số lần `firstHit > 2` < 0,1 % số lần có đòn dương; các lần `firstHit = −1` đếm và liệt kê riêng kèm lý do, không gộp vào tỉ lệ này.
5. **Phần của ô 2 (anh duyệt, §9.11):** ô 2/cả trận ở bot Chuẩn (hồ sơ `standard`, 20 seed) ≤ 45 % với `twin-pearl` (2,0 W). In ô 2/cả trận của mọi bot.
6. **Báo cáo** (không có ngưỡng): ma trận 17 hồ sơ × 20 seed và quét ngân sách 1,25 / 1,75 / 2,0 / 2,5 / 3,75 W, bảng như §8.2–8.6 (tầm, phần theo loại đòn, BALANCE.md, cổng bot, quét) với cột "hai hành lang" để so.
7. Nếu một ngưỡng ở 1–5 trượt: ghi số và các lần tung trượt vào báo cáo; không đổi số trong `data/twin-pearl.ts` hay luật §9 để cho khớp.

#### G. Sau hai phiếu (việc của Claude)

- Từ lúc merge phiếu 1 tới lúc chép bot về sau phiếu 2, bot ở cây chính (`tmp/skill-reach/`) còn nhập các tên đã bỏ nên không chạy được: báo các agent khác (HANDOFF) đừng chạy bot ở cây chính trong khoảng đó.
- Duyệt diff và chạy lại E (phiếu 1) và các lệnh, phép kiểm của F (phiếu 2). Không commit liên kết `node_modules` của cây (nó hiện là file chưa theo dõi).
- **Mốc của `tmp/skill-reach/`:** phiếu 1 không ghi vào `tmp/skill-reach/` của cây Codex, nên tới lúc giao phiếu 2 bản đó vẫn đúng như lúc chép ở bước chuẩn bị 2. Trước khi giao phiếu 2: so `tmp/skill-reach/` của cây chính với bản đó bằng `diff -rq` (bỏ các thư mục kết quả); file nào khác thì chép bản của cây chính vào cây Codex; rồi lưu `shasum -a 256` các file `*.ts`, `*.sh` của cây chính làm mốc. Sau khi duyệt phiếu 2: dò mọi file khác nhau giữa hai bản bằng `diff -rq`; file nào ở cây chính khác mốc thì gộp bằng tay; còn lại chép về `games/immortality-cultivation/tmp/skill-reach/`, cùng thư mục `key2-fieldwide/`; chạy thử một trận từ cây chính (`TSX_DISABLE_CACHE=1 node --import=tsx tmp/skill-reach/bot.ts <thư mục tạm> w45a97@twin-pearl 1 1`) trước khi gỡ cây. §9.13 ghi lệnh tái lập chạy từ cây chính.
- Quay video lab (hai cổng và một bố cục khác) ở `typing-game-review/captures/tu-tien/twin-pearl-fieldwide/`, gửi anh. Thư mục đó có `ABOUT.md` ghi rằng số đo của bot nằm ở `games/immortality-cultivation/tmp/skill-reach/key2-fieldwide/` (cùng chỗ với các số §8, để script so được).
- Ghi số đo vào một §9.13 mới của tài liệu này.
- Báo anh số đo mới so với đích anh đã duyệt ở §9.11 (ô 2/cả trận ở bot Chuẩn ≤ 45 % với 2,0 W mỗi bên), gửi kèm video lab để anh xem tốc đầu rồng (§9.11, "Anh xem khi có video lab"); chỉ hỏi anh nếu một đích của F trượt.
- Âm thanh của §3 A dời theo khung mới khi làm âm: lặng ở F49, hai tiếng gầm ở F53, chuông lớn ở F57. Tiếng hô bằng tiếng Anh (§9.11), ví dụ "Twin Dragons — Seize the Pearl!".
- Viết changelog `games/immortality-cultivation/docs/changelog/<ngày>-twin-pearl-fieldwide.md` (mục nào làm, số đo, những gì chưa làm).

### 9.13 Kết quả bot (phiếu 272)

**Báo cáo đầy đủ của Codex:** `games/.wt-ic-twin-fieldwide/tmp/skill-reach/key2-fieldwide/report.md` (ngoài Git; cùng thư mục có `aggregate.txt`, `numbers.json`, `failures.json`). Theo §9.12 G, thư mục `key2-fieldwide/` sẽ được chép về `games/immortality-cultivation/tmp/skill-reach/`. Mã game: main `35f1b77` (phiếu 271, 271b, 271c), ngân sách mặc định 2,0 W mỗi bên cộng 0,8 W trời.

**Đạt** (quét đỉnh, 92 lần tung lúc 35–45 thú đất, trừ khi ghi khác):
- Cờ tắt: 36/36 file khớp `golden-before`. Bố cục: 8/8 khớp bảng §9.7.
- Thú khác nhau bị trúng: trung vị 14 (p10–p90 11–17), 83,7 % số lần tung trong 12–20.
- `coverageStatic` trung vị 97,4 % (đất 97,3 %, trời 100 %).
- Đòn đầu: F0 62 lần, F1 30 lần. Trận thật: 0 trên 13 315 lần có đòn dương tới muộn hơn F2; 2 lần không có đòn dương (`book` rỗng, lý do `other`).
- Quạ: 159/166 = 95,8 %.

**Trượt:**
- Cân hai bên: 69/92 = 75 % số lần tung nằm trong 40/60–60/40 (đích ≥ 85 %). Hai hành lang cũ chia theo cổng nên con số cũ (92,4 %) không cùng định nghĩa.
- Ô 2/cả trận ở bot Chuẩn: 45,99 % trung bình 20 seed (trần anh duyệt 45 %).

**Thắng thua:** bot Chuẩn chỉ thắng 15 % (hai hành lang: 95 % ở 2,0 W, 100 % ở 2,5 W). Cổng B1 trượt: Mới 0 %, Chậm chắc 5 %, Chuẩn 15 %, Khá 50 %, Ẩu 0 %, Nhanh 85 %; áp lực P 61–66 %.

**Tầm và phần đòn:**
- Đòn đất xa nhất tới H (trung vị): bên 0 14,95 m, bên 1 11,60 m. Thú đất ở xa hơn 12 m bị trúng: 13,2 % (hai hành lang 2,0 W: 20,1 %).
- Phần sát thương: thân 43,6 %, hoa sen đầy 19,7 %, đĩa F1 trời 9,5 %, quét trời 7,7 %, đĩa F0 7,6 %, đĩa F1 đất 6,1 %, hoa sen nửa 5,8 %.

**Quét ngân sách** (mỗi bên; thú bị trúng trung vị · cân hai bên · Chuẩn thắng · ô 2/cả trận ở Chuẩn):

| Mỗi bên | Bị trúng | Cân hai bên | Chuẩn thắng | Ô 2/cả trận |
|---|---|---|---|---|
| 1,25 W | 11 | 47,8 % | 0 % | 37,5 % |
| 1,75 W | 13 | 78,3 % | 5 % | 43,7 % |
| **2,0 W (mặc định)** | **14** | **75 %** | **15 %** | **46,0 %** |
| 2,5 W | 15 | 72,8 % | 45 % | 47,6 % |
| 3,75 W | 19 | 81,5 % | 95 % | 54,1 % |

Mục này chỉ ghi số. Việc chỉnh cân bằng (ngân sách, cách chia hai bên, phần sửa tầm của SKILL_REACH) do Claude điều phối chốt ở bước sau.

## 10. Bầy rồng khí (05/11/2026): sim tự vạch đường, chạm là trúng, nổ ngọc cả sân

**Anh duyệt (05/11 16:00):** "rồng lướt qua quái nào thì gây sát thương quái đó, và khi rồng tới ngọc, sẽ gây ra 1 vụ nổ mạnh cả map". Hình rồng khí giữ như lab (`claude/dragon-swarm-lab`), không vẽ lại (15:35). Nguồn thiết kế: ChatGPT (Chat, High, tự duyệt 2 PASS), nguyên văn `docs/games/tu-tien/source/key2-qi-swarm-chatgpt-2026-11-05.md`; đọc mã: `docs/work/consult/key2-qi-swarm-wiring-study.md`. Claude chốt; chỗ Claude khác ChatGPT ghi **[Claude]**.

### 10.1 Bất biến
- 5 rồng, 5 vùng, 1 ngọc. Sim vạch đường, view chỉ vẽ đúng đường sim gửi (không tự tìm đích, không làm trơn lại, không đổi đường).
- Chỉ thân rồng thật chạm mới gây sát thương; mỗi quái **một** đòn chạm mỗi lần tung (con rồng chạm đầu tiên giữ đòn). Mỗi quái tối đa 3 đòn mỗi lần tung: sóng thả, chạm, nổ ngọc.
- Luật không phụ thuộc map: chỉ dùng biên sân, người ra chiêu, vị trí và mật độ quái. Toàn số nguyên, không float, không lượng giác lúc chạy, không ngẫu nhiên, không duyệt không thứ tự.
- Giữ hồi chiêu 8 s, chờ tung 3 s, trần boss, trần cụm 60 %.

### 10.2 Vạch đường (số nguyên)
- **Vùng:** chia sân thành 5 dải bằng nhau theo trục dài (bằng nhau thì trục X), biên nửa mở, dải cuối gồm biên max. Rồng i giữ dải i. Vùng chỉ quyết chọn đích; rồng bay qua vùng khác vẫn chạm được.
- **Chọn đám quái:** chụp quái đủ điều kiện (đất, trời, boss) ở F0; mỗi vùng chia ô 4 m; điểm = đất + trời + 2 × boss; xếp điểm giảm, rồi chi phí đường tăng, rồi tọa độ ô; lấy tối đa 2 đám tách rời mỗi rồng; đích lái = medoid vị trí quái của đám (hòa thì theo id quái).
- **Ngọc P:** cùng tỉ lệ với 271 nhưng không dùng điểm tim của map: H = medoid của ô 4 m điểm cao nhất toàn sân, G = trọng tâm quái đất (không có thì mọi quái); đi từ H về G 3/5 quãng, tối đa 12 m; kẹp trong sân lùi 2 m; trong 60 m quanh người ra chiêu; sân hẹp hơn 4 m thì lấy tâm sân.
- **Lái:** tọa độ nguyên (cm hay `u` của sim), bước 0,25 m, 4096 hướng lượng tử, rẽ tối đa 36 đơn vị hướng mỗi bước (bán kính ≥ 4,5 m), dài tối đa 75 m, tối đa 301 mẫu. Thử [2 đích, 1 đích, không đích] tới khi đường hợp lệ (trong sân, đúng bán kính, ≤ 75 m, tới kịp). Bảng hướng có phiên bản; phép nhân chia qua `mulDiv` hay số nguyên rộng có kiểm.
- **[Claude] Đường cong cuối:** làm trơn B-spline bậc hai (như lab, phiếu 289) rồi **nướng thành mẫu nguyên**; kiểm lại bán kính sau làm trơn, sai thì giữ đường lái. Mẫu nướng là nguồn duy nhất cho cả va chạm và hình.
- **[Claude] Đường xoắn khóa theo quỹ đạo:** xoắn ngang 1,8 m, nâng 0,8 m, bước sóng 15 m, pha theo độ dài đường (không trôi theo thời gian, khác lab `drift 0.1`). Thân rồng vì vậy luôn nằm trên **đường xoắn cố định** = đường nướng + độ lệch xoắn tại mỗi mẫu (tính bằng bảng sin nguyên). Sim lưu đường xoắn này; view vẽ thân bám đúng nó.
- **Độ cao:** đám đất bay thấp, đám trời bay ở độ cao của đám; nội suy dọc bằng số nguyên; độ cao không tới được thì bỏ đích. Bán kính 4,5 m chỉ tính theo mặt ngang.
- **Trường hợp biên:** 1–2 quái: rồng liên quan nhắm chúng, rồng khác tuần tra vùng mình; mọi quái một vùng: một rồng dồn vào đó, bốn rồng tuần tra, nổ ngọc vẫn trúng hết; vùng trống: bay cảnh về ngọc, không bịa sát thương; chỉ quái trời: mật độ trời quyết đường; quái tới muộn: không vạch lại, vẫn trúng chạm thật và nổ; quái chết trước khi chạm: không trúng; không quái đủ điều kiện: giữ luật chờ tung như cũ.

### 10.3 Nhịp (tick sau khi giải chiêu, 60 tick = 1 s) **[Claude: nhanh hơn bản ChatGPT 6,5 s]**
- F0 giải chiêu, chốt đường, phát sự kiện đường. F1 sóng thả. Thả rồng F2, F8, F14, F20, F26.
- Bay tới lúc lao: đầu rồng i vào ngọc ở F180 + 12i (F180…F228). Tốc độ rồng = độ dài đường tới điểm 2 m trước ngọc / thời gian có; kẹp 13–20 m/s (gần mức 1,3× anh chọn); nhanh hơn 20 thì bỏ bớt đích; chậm hơn 13 thì chèn điểm lái trên vòng 6 m quanh ngọc, mỗi 90° (phiếu 293). Trong 7,8 m cuối, rồng lặn thẳng vào ngọc với bán kính rẽ giảm dần như lab; kiểm bán kính 4,4 m chỉ ở các mẫu cách ngọc hơn 8 m.
- Sau khi đầu vào ngọc, thân rút vào ngọc dọc đường trong 30 tick; va chạm vẫn tính trên phần thân còn hiện.
- **Nổ ngọc F260** (4,33 s). Dư âm tới F300. **Hết F300 (5 s)**, còn 180 tick trước hồi chiêu.

### 10.4 Sát thương (số khởi điểm, bot chốt)
| Kênh | Khởi điểm | Thời điểm | Khoảng quét |
|---|---|---|---|
| Sóng thả | quỹ chung 0,5 W, bán kính **6 m** [Claude: 4,5 → 6] | F1 | 0,3–0,7 W |
| Chạm thân | **0,15 W** mỗi quái, một lần mỗi tung [Claude: 0,08 → 0,15] | khi chạm | 0,10–0,20 W |
| Nổ ngọc | quỹ chung **2,5 W** [Claude: 3,0 → 2,5] | F260 | 2,0–3,5 W |
- **[Claude] Va chạm chạm:** quái trúng khi khoảng cách tới **đoạn đường xoắn mà thân đang chiếm** (từ độ dài đuôi tới độ dài đầu ở tick đó) ≤ 0,85 m + hurtbox. Đầu đi ≤ 0,35 m mỗi tick < bán kính nên không lọt qua; không cần quét 41 trạm thân. Lưới ô cho pha rộng; thứ tự: tick, rồng, id quái.
- **[Claude] Đòn đầu:** sóng thả 6 m ở F1. Không quái nào trong 6 m thì đích đầu của rồng 0 là đám quái gần người ra chiêu nhất (bất kể vùng), để đòn chạm đầu tới sớm nhất; hình và âm vẫn phát ngay ở F0–F1. Không bịa đòn từ xa.
- **Nổ ngọc:** chụp mọi quái sống trong sân ở F260; q = khoảng cách tới ngọc / khoảng cách từ ngọc tới biên sân theo cùng tia, thang 0–1000; trọng số w = 1000 − ⌊400q/1000⌋ (ngọc 1000, biên 600); quỹ = max(round(2,5 W), N); mỗi quái giữ 1 đơn vị, phần còn lại chia theo trọng số, dư lớn nhất, hòa theo id.
- **Trần:** quái thường tối đa 2,5 W mỗi tung, boss 1,5 W; cả 3 kênh chung một danh tính đòn diện rộng cho trần cụm 60 %; không chia lại phần bị trần cắt; đo sát thương thật sau trần, không tính dư máu.
- **Nhận cân bằng:** phím 2 ≤ 45 % sát thương của bot Chuẩn; bot Chuẩn thắng rõ hơn 15 %; ghi theo lần tung: độ dài đường, số đám phủ, tick đòn đầu, số quái bị chạm, sát thương từng kênh, phần bị trần cắt. Nếu phím 2 vẫn lấn át mà bot Chuẩn vẫn thua thì sửa các chiêu khác hay cách bot dùng, không bắt riêng chiêu này gánh.

### 10.5 Sự kiện sim → view
- `skill-fx` giai đoạn mới ở F0, gói `SwarmCastV1`: castId, seat, slot, castTick; người ra chiêu, ngọc, biên sân (nguyên); 5 mảng mẫu đường xoắn đã nướng (số nguyên, xếp cố định); tick thả, tick lao; thời gian rút; phiên bản hình học và tham số xoắn; checksum. Trần 24 KiB.
- Giai đoạn `swarm-burst` (F260) và `swarm-end` (F300). Sự kiện `hit` thêm `castId`, `phase` (release/touch/burst) và `dragon` (chỉ số, khi chạm).
- Phiên bản người vạch đường, bảng hướng, va chạm, sát thương, lược đồ sự kiện vào rulesHash của biến thể; biến thể vẫn sau cờ header, cờ tắt thì băm replay không đổi.

### 10.6 View (phiếu sau)
- Presenter `src/view/skills/qi-dragon-swarm.ts` (từ module lab): đồng hồ = tick thế giới (dừng khi tạm dừng), vẽ thân theo đúng đường xoắn sim gửi, nội suy giữa hai tick; pool 2 bầy cho tung chồng; làm ấm trong `newMatch`; giảm chuyển động theo canon §24.
- Tầng: High 5 rồng + tối đa 3 lượt depth prepass (≤ 8 lượt vẽ skinned); Medium 5 rồng một lượt, không prepass; Low 5 dải/bóng 2D theo đường chiếu, ngọc và nổ màn hình, không skinned, không bloom, giữ đúng nhịp và chỗ.
- Model và texture: bản High/Medium của phiếu 292 qua manifest `public/assets/immortality-cultivation/`.

### 10.7 Thứ tự làm và cổng
1. Phiếu 293 (sim A): biến thể `swarm` sau cờ, mô-đun hình học nguyên, vùng, đám, ngọc, lái, nướng, đường xoắn, sự kiện `SwarmCastV1`; test tất định và biên. Cờ tắt: băm replay không đổi.
2. Phiếu 294 (sim B): ba kênh sát thương, va chạm trên đường xoắn, trần, sự kiện `hit` mở rộng, giai đoạn nổ/hết; test bảo toàn quỹ, thứ tự, trần.
3. Phiếu 295: bot đo cân bằng (khung 272) cho biến thể mới, quét quỹ.
4. Phiếu 296: presenter view + tầng + lab chạy từ sim thật; video cho anh.
5. Sau khi anh duyệt và cân bằng đạt: bật biến thể cho bản chơi (header, rulesHash, quyết định tương thích replay: cần anh duyệt).
