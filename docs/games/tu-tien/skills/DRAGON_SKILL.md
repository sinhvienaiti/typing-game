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

**Đo gì:** hộp xám của A · Song Long trong `games/immortality-cultivation` (HEAD `6e68958`: sim `e91a787`, lab `7ee98f0`, changelog `docs/changelog/2026-11-04-lab-twin-dragons-greybox.md`). Chiêu chỉ chạy khi header trận có cờ `swordKey2: "twin-pearl"`; mặc định tắt. Bài đo so nó với ô 2 hôm nay (Nhất Tuyến Xuyên Vân, đường thẳng 14 × 1,2 m) theo §2 luật 4 và [`BALANCE.md`](../../BALANCE.md), rồi thử hai biến thể số trong bộ nhớ làm chứng cứ. Không sửa file nào của game; canon và [`00-canon.md`](../00-canon.md) giữ nguyên; mọi số vẫn là số thử.

### 8.0 Kết luận

1. **Số thú khác nhau bị trúng: vượt xa đích.**
   - Khi có 35–45 thú trên hai đường, Song Long trúng 36,4 con mỗi lần tung (p10–p90: 32–41), tức 90 % số thú đang sống. Đích là 12–20; hôm nay 2,8.
   - Ở mức đông này không lần tung nào rơi vào 12–20. Đích chỉ đạt ở mức thưa: 15–24 thú trên hai đường, 53 % số lần tung.
2. **Phủ đường, quạ và đòn đầu: đạt.**
   - Phủ 100 % đường đi của cả hai cổng (hôm nay 3 % và 13 %).
   - Trúng 96 % số quạ đang bay (hôm nay 2 %).
   - Đòn đầu ở F0 hoặc F1 (0–17 ms; hôm nay 12 tick = 200 ms). Ngoại lệ 0,2 % số lần tung (§8.2), phần lớn khi trên sân chỉ còn Vương đang gầm.
3. **Trái/phải: đạt ở trung vị, chưa đều.** Trung vị 57,5/42,5 lúc 35–45 thú; 64 % số lần tung nằm trong 40/60–60/40 (hôm nay 2 %, vì đường thẳng chỉ trúng một bên). Phần lớn độ lệch theo chính triều thú: lúc đỉnh, cổng A đông hơn (54/46).
4. **Quá mạnh, mạnh hơn cả tuyệt kỹ.**
   - Mọi bot Mới → Nhanh thắng 95–100 % (dải Cân bằng 75–90 %).
   - Ô 2 chiếm 57–62 % sát thương cả trận; canon §7.3 cho mỗi chiêu vùng ≤ 20 %.
   - Lúc đông, mỗi lần tung ra 13,2 W hiệu dụng và hạ 21 con. Một lần tuyệt kỹ hôm nay chỉ ra trung bình 4,1 W. Ô 2 lại tung 5–7 lần mỗi phút.
   - Đây không phải "tuyệt kỹ thu nhỏ" mà là một tuyệt kỹ lặp lại mỗi 8 s.
5. **Nhưng nó sửa đúng chỗ gãy của [`SKILL_REACH.md`](SKILL_REACH.md):**
   - Áp lực P từ 67–75 % xuống 41–52 % (đích 15–35 %).
   - Quãng Q từ 72–82 % xuống 54–64 %, vào dải 50–70 %.
   - Đợt 2 (mở cổng thứ hai): thú lọt từ 10–18 % xuống 5–8 %; Trận Lực mất trong đợt từ 21–31 % xuống 4–9 %.
   - CB3 (ô 1 ≤ 30 % sát thương gõ) lần đầu đạt.
6. **Hai biến thể thử không đưa được về đích** (§8.6):
   - "Hẹp" (mọi khối trúng hẹp một nửa) vẫn trúng 29,4 con lúc đông, đường chỉ còn phủ 68 %, thắng vẫn 85–100 %.
   - "Ngân sách" (sàn giảm dần 40 % → 10 %) hạ còn 7,3 con mỗi lần tung, thắng 75–100 %, nhưng S tụt còn 9–45 % và ô 2 vẫn chiếm 43–52 % sát thương.
   - Bài học: phủ trọn hai đường thì trúng 72–94 % số thú đang sống, kể cả khi mọi khối hẹp đi một nửa. Sức mạnh phải hãm bằng ngân sách mỗi lần tung, không bằng bề rộng (câu hỏi ở §8.8).

### 8.1 Cách đo

- **Bot** (ngoài Git, `games/immortality-cultivation/tmp/skill-reach/`), chính bot của [`SKILL_REACH.md`](SKILL_REACH.md) §3.1, thêm phần chọn ô 2:
  - hồ sơ không hậu tố: ô 2 hôm nay;
  - `@twin-pearl`: Song Long (cờ header);
  - `@twin-pearl+narrow`, `@twin-pearl+budget`: hai biến thể số trong bộ nhớ (`key2-numbers.ts`, nạp trước sim).
- **Ghi từng lần tung ô 2** (`key2-measure.ts`, chỉ đọc world và sự kiện): số thú lúc tung theo cổng, thú khác nhau bị trúng, đòn, hạ, sát thương hiệu dụng và tiềm năng, phần thừa, trái/phải, quạ, đòn đầu, phần đường được phủ, sát thương theo từng phần của chiêu.
- **Kiểm bot không đổi sim:**
  - Với cờ tắt, 36 file kiểu golden (9 hồ sơ × 4 seed, 1.693 mốc băm world và local) trùng từng byte với `golden-after` của bước dựng.
  - 340 trận "hôm nay" trùng từng byte (kết quả, chỉ số, sổ sát thương) với lần đo SKILL_REACH ngày 03/11 (HEAD `c5267d0`). Vì vậy cột "hôm nay" dưới đây chính là số của SKILL_REACH §3.
- **Ma trận:** như SKILL_REACH §3: 17 hồ sơ × 20 seed, Cân bằng, bộ điều nhịp bật, Đứng yên. Bốn biến thể là 1.360 trận (2,5 phút trên 6 lõi).
- **Hai cách lấy lần tung:**
  - **Trận thật:** mọi lần bot tung ô 2. Với Song Long, sân thưa hẳn nên trong cả ma trận chỉ có 6 lần tung lúc 35–45 thú trên hai đường.
  - **Quét đỉnh** (`key2-dense.ts`): bot chơi trận cờ tắt; ở lúc đông nhất trên hai đường của mỗi đợt (≥ 15 con), dựng lại world từ replay, tung ô 2 đúng tick đó trong bản sao, rồi chạy tiếp 110 tick không lệnh nào. Mọi biến thể dùng cùng các world đó: 1.653–1.665 lần tung mỗi biến thể, trong đó 92 lần lúc 35–45 thú (78 lần ở đỉnh đợt 6). Đây là nguồn số chính cho §2 luật 4.
- **Định nghĩa:**
  - **Thú khác nhau bị trúng:** số con nhận ít nhất một đòn hiệu dụng của lần tung, kể cả con sinh ra sau khi tung (rồng còn ở cổng tới F96).
  - **Phủ đường:** phần đường đi của mỗi cổng (từ cổng tới mép Trận Tâm, mẫu 0,25 m) nằm trong một khối trúng trên đất của lần tung, ở bất kỳ tick nào.
  - **Trái/phải:** sát thương hiệu dụng lên thú cổng A (và quạ ở x < 0) so với cổng B; chỉ tính lần tung có thú ở cả hai đường.
  - **Trúng quạ:** phần quạ sống lúc tung bị trúng.
  - **Đòn đầu:** số tick từ F0 tới đòn hiệu dụng đầu tiên (1 tick = 16,7 ms).
  - **Thừa:** phần dư của các đòn kết liễu (đòn tiềm năng P × M_q × bucket × hệ số giảm dần, chưa tính trần cụm và ×1,5 phá thế, trừ máu còn), chia cho tổng sát thương tiềm năng của lần tung.

### 8.2 Tầm mỗi lần tung (§2 luật 4)

Quét đỉnh, lúc 35–45 thú trên hai đường; 92 lần tung mỗi cột (91 ở cột ngân sách).

| Chỉ số | Đích | Hôm nay (đường thẳng) | Song Long | Thử: hẹp | Thử: ngân sách |
|---|---|---|---|---|---|
| Thú trên hai đường lúc tung | ~40 | 38,2 | 38,2 | 38,2 | 38,3 |
| Thú khác nhau bị trúng (p10–p90) | 12–20 | 2,8 (1–5) | **36,4** (32–41) | 29,4 (19–38) | 38,2 (35–43) |
| Lần tung trong 12–20 | | 0 % | 0 % | 14 % | 0 % |
| Phần thú đang sống bị trúng | | 7 % | 90 % | 72 % | 94 % |
| Phủ đường cổng A / B | | 3 % / 13 % | 100 % / 100 % | 68 % / 68 % | 100 % / 100 % |
| Trái/phải, trung vị (p10–p90 phần trái) | 40/60–60/40 | một bên (0 hoặc 100 %) | 57,5/42,5 (46–65 %) | 59/41 (45–67 %) | 54/46 (43–67 %) |
| Lần tung trong 40/60–60/40 | | 2 % | 64 % | 53 % | 66 % |
| Trúng quạ | | 2 % | 96 % | 81 % | 96 % |
| Đòn đầu | ≤ 50 ms | 12 tick = 200 ms | F0 (89 %) hoặc F1: 0–17 ms | F0–F1 | F0–F1 |
| Hạ mỗi lần tung | | 2,4 | 21,3 | 17,1 | 7,3 |
| Sát thương hiệu dụng mỗi lần | | 1,1 W | 13,2 W | 10,5 W | 6,3 W |
| Thừa | | 71 % | 22 % | 24 % | 15 % |

**Theo mật độ** (quét đỉnh; số thú khác nhau bị trúng, trong ngoặc là phần lần tung rơi vào 12–20):

| Thú trên hai đường | Số lần tung | Hôm nay | Song Long | Hẹp | Ngân sách |
|---|---|---|---|---|---|
| 15–24 | 1.168 | 2,1 (0 %) | 19,7 (53 %) | 15,1 (82 %) | 20,4 (44 %) |
| 25–34 | 402 | 2,6 (0 %) | 26,7 (4 %) | 20,0 (53 %) | 27,7 (2 %) |
| 35–45 | 92 | 2,8 (0 %) | 36,4 (0 %) | 29,4 (14 %) | 38,2 (0 %) |

- **Trận thật khớp quét đỉnh:** Song Long lúc 35–45 thú (6 lần) trúng 36,0 con, 90 % số đang sống; lúc 25–34 thú (170 lần) 27,6 con. Tính mọi lần tung của cả trận (phần lớn lúc thưa): hôm nay 1,9 con mỗi lần, Song Long 10,0, hẹp 8,1, ngân sách 10,5.
- **Đòn đầu trong trận thật:** Song Long F0 ở 21 %, F1 ở 78 % số lần tung. 36/14.765 lần (0,2 %) tới muộn, đã soi lại từng loại trên replay:
  - 32 lần trên sân chỉ còn một con; 31 lần trong đó là Vương đang gầm (miễn sát thương) ngay trong vùng giữ, nên đòn hiệu dụng đầu là hoa sen ở F51;
  - 1 lần chỉ còn quạ: không có điểm chạm trên đất, đòn đầu là đuôi quét trời ở F31;
  - 3 lần con gần Trận Tâm nhất là một Thạch Thử đứng một mình còn 1 máu: trần cụm 60 % làm tròn xuống 0, nên điểm chạm F1 ra 0 máu và đòn hiệu dụng đầu tới ở F16–F17.
- **Thú bầy còn 1 máu đứng một mình không chết vì đòn vùng** (luật có từ trước, không riêng Song Long): trần cụm là 60 % máu cả cụm làm tròn xuống, nên với 1 máu nó là 0. Chỉ đòn đơn mục tiêu (ô 1, Phi Kiếm) kết liễu được. Đây là việc kỹ thuật của luật sát thương, không cần anh quyết.
- **Lệch trái nhỏ do thứ tự tính:** mỗi tick, đường A được tính trước đường B, nên thú cổng A lấy các chỗ đầu của hệ số giảm dần.
  - Phần trái của sát thương trừ đi phần trái của số thú: +1 điểm trên mọi mật độ, +4 điểm lúc 35–45 thú, +5 điểm với biến thể ngân sách (giảm dần dốc hơn).
  - Đây là việc kỹ thuật, không cần anh quyết: xen kẽ hai đường theo khoảng cách tới Trận Tâm.

### 8.3 Sát thương theo phần của chiêu

Quét đỉnh, 35–45 thú. Mỗi ô: phần sát thương · số đòn mỗi lần tung · số con hạ mỗi lần tung.

| Phần | Khung | Song Long | Hẹp | Ngân sách |
|---|---|---|---|---|
| Đòn giữ 8 × 8 m trước Trận Tâm | F0 | 8,7 % · 6,1 · 2,1 | 6,7 % · 3,6 · 1,3 | 14,5 % · 6,3 · 1,8 |
| Điểm chạm trên hai đường | F1–F2 | 8,5 % · 6,5 · 0,6 | 11,3 % · 6,5 · 1,3 | 8,1 % · 6,5 · 0,4 |
| Thân và vệt trên đất | F3–F96 | 52,1 % · 20,3 · 12,4 | 54,9 % · 16,3 · 10,8 | 42,3 % · 21,7 · 1,2 |
| Đuôi quét trời | F30–F50 | 6,3 % · 1,7 · 0,1 | 6,7 % · 1,5 · 0,1 | 3,4 % · 1,7 · 0 |
| Hoa sen, phần đầy (hai cánh dài và vùng giữ) | F51–F71 | 19,4 % · 8,4 · 4,0 | 20,5 % · 7,1 · 3,7 | 26,2 % · 12,7 · 3,5 |
| Hoa sen, phần nửa (ngoài cánh) | F51–F71 | 5,0 % · 4,3 · 2,0 | không còn (r 4,5 m nằm trọn trong cánh và vùng giữ) | 5,4 % · 5,2 · 0,4 |

- **Chia thật so với thiết kế:** thiết kế chia chạm 15 %, hành lang 45 %, hoa sen 40 %. Đo được 17 / 58 / 24 %: hoa sen thiếu, vì khi nó nở ở F51 thân rồng đã hạ 12 con.
- **Thừa:** Song Long 22 %, so với 71 % của đường thẳng hôm nay. Đòn 2,5 W của đường thẳng rơi vào Thạch Thử 30 máu.

### 8.4 Các chỉ số của BALANCE.md

17 hồ sơ × 20 seed, Cân bằng, bộ điều nhịp bật. Cột như SKILL_REACH §3.4:
- "Gõ" là phần sát thương gõ (CB2 cần ≥ 55 %);
- "Ô 1/gõ" là phần ô 1 trong sát thương gõ (CB3 cần ≤ 30 %);
- "Ô 2/cả trận" là phần ô 2 trong mọi sát thương (canon §7.3 cho mỗi chiêu vùng ≤ 20 %);
- "Đánh nền" thì canon §7.3 đích 12–18 %;
- "Phút" là thời lượng trận, tính tới lúc thua.

Dải đích Cân bằng: Thắng 75–90 % · S trung vị 35–65 % · P 15–35 % · I ≤ 10 % · O ≤ 8 % · N 0,3–1 · Q trung vị 50–70 %.

**Hôm nay · Song Long** (mỗi ô: số hôm nay · số Song Long):

| Hồ sơ | Thắng | S | P | I | O | N | Q | Gõ | Ô 1/gõ | Ô 2/cả trận | Đánh nền | Phút | Thua ở đợt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 30 WPM 90 % | 0 · 100 % | 0 · 38 % | 74 · 50 % | 0,6 · 1,3 % | 0 · 0 % | 0 · 0,25 | 79 · 61 % | 80 · 87 % | 39 · 16 % | 23 · 59 % | 10,5 · 6,3 % | 8,0 · 12,2 | 4: 3 · 5: 16 · 6: 1 / — |
| 30 WPM 97 % | 5 · 100 % | 0 · 47 % | 71 · 47 % | 0,7 · 1,5 % | 0 · 0 % | 0,05 · 0,05 | 77 · 59 % | 81 · 88 % | 42 · 18 % | 21 · 59 % | 8,7 · 5,1 % | 9,1 · 11,3 | 4: 1 · 5: 7 · 6: 11 / — |
| 45 WPM 90 % | 0 · 100 % | 0 · 36 % | 71 · 51 % | 0,3 · 1,9 % | 0 · 0 % | 0 · 0,15 | 76 · 60 % | 82 · 88 % | 45 · 20 % | 20 · 58 % | 8,0 · 5,2 % | 7,7 · 10,5 | 5: 17 · 6: 3 / — |
| 45 WPM 97 % | 0 · 100 % | 0 · 50 % | 69 · 46 % | 0,4 · 2,3 % | 0 · 0 % | 0 · 0 | 75 · 59 % | 83 · 89 % | 48 · 20 % | 19 · 60 % | 6,6 · 4,0 % | 8,2 · 9,8 | 5: 7 · 6: 13 / — |
| 60 WPM 90 % | 0 · 100 % | 0 · 43 % | 72 · 51 % | 0,2 · 2,5 % | 0 · 0 % | 0 · 0,10 | 76 · 60 % | 84 · 89 % | 48 · 23 % | 20 · 57 % | 6,2 · 4,4 % | 7,1 · 9,1 | 5: 14 · 6: 6 / — |
| 60 WPM 97 % | 0 · 100 % | 0 · 56 % | 69 · 44 % | 0,6 · 3,3 % | 0 · 0 % | 0 · 0 | 73 · 59 % | 85 · 90 % | 51 · 23 % | 18 · 59 % | 5,2 · 3,4 % | 7,8 · 8,7 | 5: 7 · 6: 13 / — |
| 80 WPM 90 % | 0 · 100 % | 0 · 39 % | 70 · 50 % | 0,6 · 2,9 % | 0 · 0 % | 0 · 0,15 | 74 · 59 % | 84 · 90 % | 50 · 24 % | 19 · 57 % | 5,6 · 3,9 % | 7,5 · 8,9 | 5: 9 · 6: 11 / — |
| 80 WPM 97 % | 40 · 100 % | 0 · 57 % | 67 · 42 % | 1,2 · 2,8 % | 0 · 0 % | 0,40 · 0 | 72 · 56 % | 85 · 91 % | 52 · 23 % | 18 · 59 % | 5,1 · 3,0 % | 8,4 · 8,6 | 5: 3 · 6: 9 / — |
| Trẻ em (15 WPM 88 %) | 0 · 5 % | 0 · 0 % | 83 · 63 % | 0,2 · 0,7 % | 0 · 0 % | 0 · 0 | 94 · 70 % | 72 · 81 % | 22 · 8 % | 26 · 62 % | 20,0 · 10,6 % | 5,4 · 9,7 | 3: 15 · 4: 5 / 4: 1 · 5: 10 · 6: 8 |
| Mới (25 WPM 92 %) | 0 · 95 % | 0 · 36 % | 74 · 52 % | 0,4 · 1,1 % | 0 · 0 % | 0 · 0,30 | 82 · 64 % | 78 · 86 % | 37 · 14 % | 22 · 60 % | 12,1 · 7,3 % | 8,5 · 13,1 | 4: 5 · 5: 12 · 6: 3 / 6: 1 |
| Chậm chắc (25 WPM 99 %) | 0 · 100 % | 0 · 48 % | 71 · 47 % | 0,6 · 1,6 % | 0 · 0 % | 0 · 0,05 | 78 · 59 % | 80 · 88 % | 39 · 16 % | 22 · 61 % | 9,6 · 5,6 % | 9,9 · 12,2 | 5: 9 · 6: 11 / — |
| Chuẩn (35 WPM 95 %) | 0 · 100 % | 0 · 42 % | 72 · 49 % | 0,3 · 1,8 % | 0 · 0 % | 0 · 0,10 | 76 · 61 % | 81 · 88 % | 44 · 19 % | 20 · 59 % | 8,4 · 5,0 % | 8,5 · 10,6 | 5: 10 · 6: 10 / — |
| Khá (50 WPM 96 %) | 5 · 100 % | 0 · 58 % | 70 · 45 % | 0,6 · 3,2 % | 0 · 0 % | 0,05 · 0 | 75 · 55 % | 83 · 90 % | 48 · 20 % | 20 · 61 % | 6,3 · 3,8 % | 8,6 · 9,1 | 5: 2 · 6: 17 / — |
| Ẩu (50 WPM 85 %) | 0 · 100 % | 0 · 35 % | 73 · 52 % | 0,3 · 1,9 % | 0,1 · 0 % | 0 · 0,25 | 77 · 61 % | 82 · 88 % | 45 · 20 % | 21 · 58 % | 8,2 · 5,3 % | 7,5 · 10,4 | 4: 4 · 5: 10 · 6: 6 / — |
| Nhanh (70 WPM 97 %) | 10 · 100 % | 0 · 64 % | 68 · 41 % | 1,3 · 3,9 % | 0 · 0 % | 0,10 · 0 | 74 · 54 % | 85 · 91 % | 51 · 21 % | 19 · 62 % | 5,3 · 3,1 % | 8,4 · 8,5 | 5: 2 · 6: 16 / — |
| Không gõ | 0 · 0 % | 0 · 0 % | 82 · 82 % | 0 · 0 % | 0 · 0 % | 0 · 0 | 100 · 100 % | 0 · 0 % | — | 0 · 0 % | 74,8 · 74,8 % | 1,0 · 1,0 | 1: 20 / 1: 20 |
| Chỉ gõ (35 WPM 95 %, không mua) | 0 · 100 % | 0 · 38 % | 75 · 50 % | 0,5 · 1,8 % | 0 · 0 % | 0 · 0,35 | 78 · 61 % | 90 · 95 % | 42 · 17 % | 23 · 65 % | 9,5 · 5,2 % | 7,8 · 10,9 | 4: 2 · 5: 13 · 6: 5 / — |

**Thêm cho bot Chuẩn** (hôm nay → Song Long):
- Đợt 2 (mở cổng thứ hai): thú lọt 14 % → 6,7 %; Trận Lực mất trong đợt 30 % → 6,9 %.
- Ô 2: 5,0 → 5,6 lần mỗi phút đánh; 8,5 → 29,1 W mỗi phút (canon ước ~18); 1,9 → 9,8 con trúng và 1,6 → 5,7 con hạ mỗi lần tung.
- Phần sát thương cả trận của các chiêu vùng khác: ô 4 15,1 % → 6,9 %, tuyệt kỹ 10,7 % → 5,6 %. Song Long lấy chỗ của cả hai.
- Sức ra đòn tổng: 43,0 → 49,2 W mỗi phút đánh (D_ref thử 75).
- Thời gian sống trung bình của một thú (B4): 12,5 s → 8,4 s.

**Hai biến thể thử: hẹp · ngân sách** (mỗi ô: số hẹp · số ngân sách; định nghĩa ở §8.6):

| Hồ sơ | Thắng | S | P | I | O | N | Q | Gõ | Ô 1/gõ | Ô 2/cả trận | Đánh nền | Phút | Thua ở đợt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 30 WPM 90 % | 95 · 80 % | 28 · 22 % | 57 · 57 % | 1,4 · 1,0 % | 0 · 0 % | 0,55 · 0,55 | 66 · 69 % | 85 · 84 % | 23 · 23 % | 49 · 49 % | 8,2 · 7,7 % | 12,7 · 12,3 | 6: 1 / 5: 1 · 6: 3 |
| 30 WPM 97 % | 100 · 100 % | 40 · 34 % | 52 · 54 % | 1,7 · 1,0 % | 0 · 0 % | 0,15 · 0,30 | 64 · 67 % | 87 · 86 % | 24 · 24 % | 50 · 50 % | 6,4 · 6,3 % | 11,8 · 11,8 | — / — |
| 45 WPM 90 % | 100 · 90 % | 26 · 13 % | 56 · 59 % | 1,3 · 1,2 % | 0 · 0 % | 0,65 · 0,65 | 65 · 68 % | 86 · 86 % | 27 · 28 % | 48 · 46 % | 6,5 · 6,2 % | 10,7 · 10,6 | — / 6: 2 |
| 45 WPM 97 % | 100 · 100 % | 38 · 38 % | 53 · 54 % | 1,9 · 2,3 % | 0 · 0 % | 0,15 · 0,25 | 63 · 67 % | 88 · 87 % | 27 · 29 % | 49 · 46 % | 5,1 · 5,2 % | 10,1 · 10,0 | — / — |
| 60 WPM 90 % | 100 · 95 % | 37 · 31 % | 59 · 60 % | 1,9 · 1,7 % | 0 · 0 % | 0,10 · 0,30 | 65 · 68 % | 88 · 86 % | 30 · 31 % | 47 · 44 % | 5,4 · 5,5 % | 9,4 · 9,4 | — / 6: 1 |
| 60 WPM 97 % | 100 · 100 % | 48 · 43 % | 51 · 53 % | 2,2 · 2,2 % | 0 · 0 % | 0,05 · 0,10 | 61 · 66 % | 89 · 88 % | 30 · 32 % | 49 · 45 % | 4,2 · 4,3 % | 9,0 · 9,0 | — / — |
| 80 WPM 90 % | 100 · 100 % | 45 · 30 % | 55 · 58 % | 2,4 · 1,7 % | 0 · 0 % | 0 · 0,55 | 64 · 68 % | 88 · 87 % | 30 · 32 % | 47 · 43 % | 5,1 · 5,1 % | 9,2 · 9,2 | — / — |
| 80 WPM 97 % | 100 · 100 % | 44 · 45 % | 50 · 50 % | 2,2 · 2,8 % | 0 · 0 % | 0 · 0,05 | 60 · 66 % | 90 · 88 % | 30 · 33 % | 49 · 45 % | 3,8 · 3,9 % | 8,9 · 8,8 | — / — |
| Trẻ em (15 WPM 88 %) | 5 · 0 % | 0 · 0 % | 72 · 72 % | 0,5 · 0,4 % | 0 · 0 % | 0,05 · 0 | 76 · 80 % | 78 · 77 % | 13 · 13 % | 50 · 50 % | 13,6 · 13,9 % | 10,1 · 8,1 | 4: 2 · 5: 6 · 6: 11 / 4: 9 · 5: 7 · 6: 4 |
| Mới (25 WPM 92 %) | 85 · 75 % | 22 · 9 % | 58 · 58 % | 1,0 · 1,0 % | 0 · 0 % | 0,70 · 0,60 | 68 · 70 % | 83 · 83 % | 20 · 20 % | 49 · 49 % | 9,4 · 8,9 % | 13,8 · 13,1 | 6: 3 / 5: 1 · 6: 4 |
| Chậm chắc (25 WPM 99 %) | 100 · 100 % | 39 · 41 % | 51 · 52 % | 1,4 · 1,2 % | 0 · 0 % | 0 · 0,35 | 65 · 68 % | 86 · 86 % | 22 · 21 % | 50 · 52 % | 7,1 · 6,8 % | 12,8 · 12,5 | — / — |
| Chuẩn (35 WPM 95 %) | 100 · 90 % | 35 · 21 % | 55 · 58 % | 1,2 · 1,2 % | 0 · 0 % | 0,20 · 0,85 | 65 · 68 % | 86 · 86 % | 25 · 27 % | 49 · 46 % | 6,2 · 6,3 % | 11,0 · 10,9 | — / 6: 2 |
| Khá (50 WPM 96 %) | 100 · 100 % | 46 · 40 % | 51 · 54 % | 2,7 · 2,3 % | 0 · 0 % | 0,10 · 0,10 | 59 · 66 % | 88 · 87 % | 26 · 28 % | 51 · 46 % | 4,8 · 4,8 % | 9,5 · 9,5 | — / — |
| Ẩu (50 WPM 85 %) | 85 · 75 % | 20 · 9 % | 58 · 60 % | 1,3 · 1,0 % | 0 · 0 % | 0,75 · 0,65 | 65 · 70 % | 86 · 85 % | 26 · 28 % | 48 · 45 % | 6,5 · 6,5 % | 10,7 · 10,4 | 6: 3 / 6: 5 |
| Nhanh (70 WPM 97 %) | 100 · 100 % | 56 · 45 % | 48 · 51 % | 3,1 · 2,5 % | 0 · 0 % | 0 · 0 | 59 · 65 % | 90 · 88 % | 27 · 30 % | 52 · 47 % | 4,2 · 4,2 % | 8,8 · 8,8 | — / — |
| Không gõ | 0 · 0 % | 0 · 0 % | 82 · 82 % | 0 · 0 % | 0 · 0 % | 0 · 0 | 100 · 100 % | 0 · 0 % | — | 0 · 0 % | 74,8 · 74,8 % | 1,0 · 1,0 | 1: 20 / 1: 20 |
| Chỉ gõ (35 WPM 95 %, không mua) | 100 · 95 % | 33 · 27 % | 55 · 59 % | 1,8 · 0,9 % | 0 · 0 % | 0,40 · 0,75 | 65 · 70 % | 94 · 93 % | 23 · 25 % | 54 · 52 % | 6,4 · 6,6 % | 11,1 · 10,9 | — / 6: 1 |

### 8.5 Cổng bot đo được

| Cổng | Hôm nay | Song Long | Thử: hẹp | Thử: ngân sách |
|---|---|---|---|---|
| B1 cùng vùng cuốn (Mới → Nhanh) | trượt: thắng 0–10 %, S 0, P 68–75 % | trượt: thắng 95–100 %, P 41–52 % | trượt: thắng 85–100 %, S 20–56 %, P 48–58 % | trượt: thắng 75–100 %, S 9–45 %, P 51–60 % |
| B2 không quá dễ | đạt | đạt | đạt | đạt |
| B3, phần bot Mới (≥ 70 %) | trượt: 0 % | đạt: 95 % | đạt: 85 % | đạt: 75 % |
| B4 chuẩn thắng ẩu | trượt: S 0 và 0 | đạt: S 48 > 35 %, hạ 8,4 < 8,5 s | đạt | đạt |
| B5 Không gõ thua (Cân bằng) | đạt | đạt | đạt | đạt |
| B7, phần đo được | 1,9–2,0 bậc mỗi đợt | 1,2–1,9 | 1,4–2,0 | 1,4–2,0 |
| CB1 | đạt | đạt | đạt | đạt |
| CB2 phần gõ ≥ 55 % (Chuẩn) | đạt: 81 % | đạt: 88 % | đạt: 86 % | đạt: 86 % |
| CB3 ô 1 ≤ 30 % sát thương gõ | trượt: 37–51 % | **đạt: 14–21 %** | đạt: 20–27 % | đạt: 20–30 % |
| CB9 Chuẩn 9–10,5 phút | không chấm (Chuẩn thua mọi seed) | trượt sát: 10,6 phút | trượt: 11,0 | trượt: 11,0 (trận thắng) |
| HC2 ≤ 8 chữ sống | đạt (8) | đạt (8) | đạt (8) | đạt (7) |
| §7.3 mỗi chiêu vùng ≤ 20 % (Chuẩn) | đạt sát: ô 2 19,9 % | **trượt: 59,2 %** | trượt: 48,6 % | trượt: 46,2 % |
| §7.3 đánh nền 12–18 % (báo cáo) | 8,4 % | 5,0 % | 6,2 % | 6,3 % |

- **B3:** chỉ chấm phần bot Mới; bot Trẻ em chạy ở Cân bằng, không ở Thư giãn như cổng yêu cầu.
- **B7:** mọi biến thể ≤ 2 bậc mỗi đợt, khoảng sinh 93–114 % (trong ±15 %). Thiếu lượt Chuẩn tắt nhịp, nên kit ghi "thiếu số".
- **Bot không đo được:** B6 (chưa có cặp chiến thuật Tốt/Kém), B8, HC1, HC3, HC8 (chưa có sự kiện học nháp), B9 (chưa có buổi chơi thử của người thật).

### 8.6 Hai biến thể số trong bộ nhớ (chứng cứ, không phải đề xuất)

Cả hai đổi đối tượng số trong tiến trình bot, trước khi sim đọc chúng; không file nào của game đổi. Hai biến thể này là hai lần thử duy nhất, chọn trước khi chạy, mỗi lần một đòn bẩy:

| Biến thể | Đổi gì | Giữ nguyên |
|---|---|---|
| **Hẹp** (`+narrow`) | Mọi khối trúng hẹp một nửa: bán kính thân rồng 1,4 → 0,7 m; nửa rộng điểm chạm 2,2 → 1,1 m; nửa rộng cánh sen 2,2 → 1,1 m; bán kính quét trời 2,5 → 1,25 m; bán kính hoa sen 9 → 4,5 m; vùng giữ 8 × 8 → 4 × 8 m | Chiều dài, đường S, vệt 0,9 s, khung, sát thương |
| **Ngân sách** (`+budget`) | Sàn giảm dần của ô 2 40 % → 10 %: từ con thứ 7 bị trúng trở đi, mỗi con chỉ nhận 10 % thay vì 40 % | Hình học, khung, chia 15/45/40 |

**Đọc kết quả:**
- **Hẹp:**
  - Lúc 35–45 thú vẫn trúng 29,4 con (72 % số đang sống); chỉ 14 % số lần tung vào 12–20.
  - Phủ đường tụt còn 68 %: đường S lệch 0,9 m, lớn hơn bán kính 0,7 m, nên chừa khe giữa đường. Quạ trúng còn 81 %.
  - Thắng 85–100 %, ô 2 vẫn 47–52 % sát thương cả trận.
  - Hẹp đi không đổi được sức mạnh, mà làm hỏng lời hứa "giữ trọn hai đường".
- **Ngân sách:**
  - Vẫn trúng 38 con, nhưng mỗi lần tung chỉ hạ 7,3 con (từ 21,3) và ra 6,3 W (từ 13,2).
  - Thắng: Mới 75 %, Chuẩn 90 %, Ẩu 75 %, các bot khác 80–100 % (trừ Trẻ em 0 %).
  - S tụt còn 9–45 %, nhiều bot dưới dải 35 %. Ô 2 vẫn 43–52 % sát thương cả trận.
  - Giảm sàn đưa tỉ lệ thắng gần dải, nhưng ô 2 vẫn gánh gần nửa trận, và trận trở nên sát nút ở bot chậm.
- **Cả ba bản Song Long:**
  - P vẫn 41–60 %, trên dải 15–35 %.
  - Đánh nền chỉ còn 3–9 % (Mới → Nhanh).
  - Ô 4 và tuyệt kỹ mất chỗ: mỗi chiêu còn 4–12 % sát thương cả trận.

### 8.7 Lab: tấm khung và clip ở camera chơi

**File** (ngoài Git, trong `games/immortality-cultivation/tmp/shots/dragon/greybox/`):
- `twin-pearl-greybox-play-1280x720-sheet.jpg`: bảy khung chụp ở 1280 × 720, mỗi ô nửa cỡ (tấm 1280 × 1440).
- `twin-pearl-greybox-play-1920x1080-sheet.jpg`: cùng bảy khung chụp ở 1920 × 1080 (tấm 1920 × 2160).
- `twin-pearl-greybox-play-1280-real-then-quarter.mp4`: 1280 × 720, 60 fps, 18,4 s. Từ F−20 tới F200 ở tốc độ thật (3,7 s), rồi chính đoạn đó ở 0,25× (14,7 s). Thấy cả hai đường và cả hai góc trời.
- Số và kịch bản chụp: `section8/capture-1280.json`, `section8/capture-1920.json`, `section8/capture-frames.mjs`.

**Cách chụp:**
- Lab `skills-lab.html?key2=twin-pearl&fixed=1`. `fixed=1` là chế độ chụp từng bước của lab: không rAF, mỗi khung đúng một tick sim, nên F0 … F200 là tick thật. Không cờ nào khác: chất lượng mặc định High, tỉ lệ điểm ảnh không ghim.
- Camera chơi mặc định của lab: 55°, FOV 28°, cả sân; lab báo khoảng cách 53,51 m.
- Bảng phím của lab (góc trên trái, rộng 400 px) che đường A và cổng A ở khổ 1280. Lúc chụp, bảng này được ẩn bằng một dòng đổi style, không phải cờ URL. Băng tên pha ở trên và ô số của hộp xám ở góc dưới phải vẫn giữ.
- Triều: triều đông nhất lab dựng được, 44 thú đất trên hai đường và 4 quạ (lab tự bơm lại ở cổng). Chạy 200 tick cho triều trải ra, rồi bấm phím 2 ở tick 201.
- Hai khổ chụp ra cùng một kết quả sim (tất định): 43 con khác nhau, 77 đòn, hạ 16, trái/phải 45/55, quạ 4/4, đòn đầu F0.

**Bảy khung:**

| Khung | Thấy gì |
|---|---|
| F0 | Hộp giữ 8 × 8 m trước Trận Tâm lóe; 17 con trúng ngay khung đầu |
| F2 | Hai hộp chạm trên hai đường, hai sợi sáng nối từ kiếm; 26 con đã trúng |
| F20 | Hai đầu rồng đi được nửa đường, đường S và vệt sau thân hiện rõ trên cả hai đường |
| F42 | Hai đầu ở hai cổng; hai cột quét trời ở hai góc; ngọc treo ở điểm gặp (0; −9,25) |
| F51 | Hoa sen nở: hai cánh dài dọc hai đường, vùng giữ, đĩa r 9 m |
| F80 | Vệt gần cổng vẫn đang trúng (đòn cuối của sim ở F96); thú bị trúng lần 2 chuyển màu cam |
| F200 | Dư âm, chỉ có hình, không còn đòn |

**Lưu ý khi xem:**
- Dòng "key → drawn" trong ô số không có nghĩa ở chế độ chụp từng bước (nó đo thời gian giữa hai lệnh CDP). Độ trễ thật lấy từ `latency.json` của bước dựng: 2,5–20 ms qua 16 lần bấm thật.
- Ở 1280 × 720, nhãn chữ nhỏ nhưng đọc được. Ở F42, hai đầu rồng nằm sát mép xa của sân.
- Đây vẫn là hộp xám: hình trong mờ và nhãn, không có art.

### 8.8 Câu hỏi cho anh

1. **Giữ đích nào: "phủ trọn hai đường tới tận cổng" hay "12–20 thú khi có 40 thú"?**
   - Hai đích này không đạt cùng lúc được: rồng chạy hết đường thì trúng 72–94 % số thú đang sống, kể cả khi mọi khối hẹp đi một nửa.
   - Claude đề xuất giữ phủ trọn hai đường, bỏ đích 12–20, và hãm sức bằng ngân sách mỗi lần tung. Phủ trọn là chỗ trả lời câu "phạm vi quá bé" của anh, và P, Q, đợt 2 đều tốt lên nhờ nó.
   - Nếu anh muốn giữ 12–20 thì phải đổi thiết kế (ví dụ mỗi rồng chỉ cắn N con đầu đường), không chỉ đổi số.
2. **Ô 2 được chiếm bao nhiêu sát thương cả trận?**
   - Canon §7.3 cho mỗi chiêu vùng ≤ 20 %. Song Long đang 57–62 %; hạ sàn giảm dần còn 10 % vẫn 43–52 %.
   - Muốn về 20 % thì cần một trần tổng mỗi lần tung, như trần 4 W của ô 4. Đó là luật mới trong sim, không chỉ là số.
   - Anh giữ 20 %, hay cho chiêu rồng (chiêu biểu tượng của bộ Kiếm × Hỏa) một trần riêng cao hơn, ví dụ ≤ 35 %?

### 8.9 Giới hạn của bài đo

1. **Bot là bot đo của SKILL_REACH**, không phải làn 7. Mọi giới hạn ở SKILL_REACH §6 vẫn còn: không Backspace, mua theo thứ tự cố định, Đứng yên, không Học trước.
   - Với Song Long, bot coi mọi thú sống là "trong tầm" nên tung ô 2 ngay khi sẵn, 5–7 lần mỗi phút. Người thật có thể giữ chiêu chờ lúc đông, khi đó mỗi lần tung còn mạnh hơn.
2. **"Thừa" đếm thiếu một chút:** đòn tiềm năng chưa tính ×1,5 phá thế. Đòn 0 sát thương (trần cụm đã hết) không có sự kiện nên không thấy.
3. **Phần của chiêu** đọc từ sổ của sim cho mỗi lần tung (mỗi tick một loại đòn mỗi con). Trường hợp hiếm có đòn 0 sát thương xen vào thì loại đòn được đoán theo khung.
4. **Mẫu lúc 35–45 thú nhỏ:** quét đỉnh chỉ có 92 lần, 85 % từ đỉnh đợt 6. Chỉ các trận còn sống tới đó mới góp mẫu.
5. **Triều trong lab là triều riêng của lab** (đặt thú theo đường, đông nhất 44 + 4 quạ), không phải ảnh chụp đỉnh của bot.
6. **Sai số:** 20 seed mỗi hồ sơ, nên tỉ lệ thắng sai khoảng ±10 điểm %. Bot Trẻ em chạy ở Cân bằng.

### 8.10 Tái lập

Từ `games/immortality-cultivation`. Mọi file ở `tmp/skill-reach/`, ngoài Git; bản bot trước bài này giữ ở `tmp/skill-reach/bot.before-key2-measure.ts`.

| Việc | Lệnh |
|---|---|
| Ma trận 4 biến thể (trận thật và quét đỉnh) | `../../.local/bin/heavy.sh --cores=6 tmp/skill-reach/key2-matrix.sh` |
| Gộp số → `tmp/skill-reach/key2/numbers.json` | `node_modules/.bin/tsx tmp/skill-reach/key2-aggregate.ts` |
| Một trận lẻ | `node_modules/.bin/tsx tmp/skill-reach/bot.ts <thư mục> w45a97@twin-pearl 1 20` |
| Kiểm cờ tắt so với golden của bước dựng | `BOT_HASHES=1` với 9 hồ sơ × seed 1–4, so `tail` với `tmp/shots/dragon/greybox/golden-after/` (đã lưu ở `tmp/skill-reach/key2/golden-check/`) |
| Chụp lab | `vite` cổng 3231 trên cây sạch, rồi `URL=http://127.0.0.1:3231/skills-lab.html OUT_DIR=… CLIP=1 ../../.local/bin/heavy.sh --gpu node src/kit/tools/cdp-run.mjs tmp/shots/dragon/greybox/section8/capture-frames.mjs --width=1280 --height=720`; ghép tấm và clip bằng ffmpeg (xstack, hai đoạn 60 fps và 15 fps) |

Khung chụp thô đã xóa; giữ hai tấm khung, clip và số.
