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
