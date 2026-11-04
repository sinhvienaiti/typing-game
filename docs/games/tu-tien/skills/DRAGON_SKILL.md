# Chiêu rồng (dragon skill): ba hướng cho anh chọn, 04/11/2026

**Trạng thái:** anh đã chọn **A · Twin Dragons, One Burning Pearl** (04/11/2026, sáng: "A · Song Long"). Bước tiếp theo là hộp xám trong lab và đo bằng bot (§6 bước 1). Số canon chưa đổi; B và C để lại cho bộ chiêu Thủy và phần tuyệt kỹ.

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
