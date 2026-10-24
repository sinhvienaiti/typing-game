# Tu Tiên Thủ Ải — 03. Kỹ năng và chiến đấu (24/10/2026)

> **Mảng:** kỹ năng, combat, đánh nền, đồ tiêu hao, trường phái, buff, pet, boss.
> **Đầu vào:** đề xuất Codex V2.2 (`TU_TIEN_TYPING_SYSTEMS_AND_5_COMBAT_OPTIONS_V2_2026-10-24.md`), video QCBH 4:20 của chủ dự án, thiết kế Rồng Giữ Ải, Tuyến Cuối, Lời Gọi, `shared/game-kit`.
> **Trạng thái:** phân tích và đề xuất. Mọi con số ghi "thử" là số khởi đầu, cần bot và chơi thật để chỉnh.
> **Đơn vị:** 1 W = máu một Tiểu yêu ở bậc ải đang chơi (cùng ý với `dragon-lane/DESIGN.md` §5.1). "E" là WPM riêng của người chơi.

## 1. Tóm tắt

- **Lõi combat cho thủ ải thú triều = Trận vị neo + đi lại trong vùng trận (bản rút gọn của phương án 1) + Phá thế phản chế cho tinh anh và Thú vương (phương án 3).** Ngự kiếm truy kích (2) và điều quân nhiều tuyến (5) thành ải đặc biệt sau MVP. Ngưng thời lập chiêu (4) bỏ khỏi thủ ải.
- **Đứng trận phải chơi được trọn vẹn.** Gõ cần hai tay trên phím chữ, nên đi lại là tùy chọn: chuột phải hoặc mũi tên, Voice dùng WASD. Thân pháp gõ bằng từ để lướt tới trận vị hoặc điểm đánh dấu mà tay không rời phím.
- **Hai tầng sức mạnh:** đánh nền tự động 15–25 %, kỹ năng gõ ≥ 60 %, phe phụ (trận, bẫy, pet) tối đa 35 %. Bot không gõ phải thua trước đợt 3.
- **Deck tăng theo cảnh giới: 3 → 5 → 6 ô có chữ.** Ô liên tục (hồi 0), 2 chiêu chính, 1 ô hộ thân hoặc thân pháp, 1 tuyệt kỹ (thanh Chân nguyên), 1 thần thông muộn. Tâm pháp là ô bị động, không chữ. Đan 3 ô dùng phím Alt, không gõ.
- **Quái thường không mang chữ.** Chỉ tinh anh và Thú vương mang chữ Ấn để phá thế. Trên màn tối đa 8 chữ sống; ô đang hồi thì ẩn chữ.
- **MVP 3 trường phái: Kiếm (S), Hỏa (F), Thổ-thể (F, hộ trận)**, đủ ba vai Tam Tài: chủ công, dọn bầy, giữ trận. Phù (hỗ trợ, bẫy) là trường phái 4 khi mở đội online. Ngự thú và pet để sau MVP. Không làm 24 trường phái.
- **Đội công bằng bằng cách chia cung ải:** mỗi người giữ một cung với nhịp k riêng. Mỗi người chỉ thấy chữ của mình. Hợp kích Tam Tài cần cả ba nhãn sáng, mỗi nhãn tính theo nhịp của chủ nhãn. Bot bù chỗ trống từ đầu trận.
- **Học từ QCBH:** kỹ năng là "sách" có loại ô riêng, có tầng luyện mở dần (video: 1/6, 220/300), có đồ tiêu hao giới hạn theo ô. Ta giữ nguyên tắc đó, bỏ việc bấm võ kỹ 0,2 s liên tục và bỏ Linh lực tiêu cho từng chiêu.

## 2. QCBH làm thế nào (chỉ phần có ích cho ta)

Ký hiệu nguồn: [video] = khung hình từ bản quay của chủ dự án (tên khung trong ngoặc); [web] = trang đã đọc; [trí nhớ] = chưa kiểm.

| Hệ | QCBH làm gì | Nguyên tắc rút ra | Ta dùng |
|---|---|---|---|
| Loại kỹ năng | Túi đồ lọc sách theo Võ kỹ/Linh kỹ, Tuyệt kỹ, Thân pháp, Tâm pháp, Thần thông, Kỹ nghệ [video t004]. Võ kỹ/linh kỹ ở chuột trái, kỹ năng đặc biệt ở chuột phải, thân pháp ở phím cách, tâm pháp bị động [web: kết quả tìm kiếm trích earlyguides.com, trang không mở được]. Tâm pháp bị động làm mạnh kỹ năng chủ động [web: en.wikipedia.org/wiki/Tale_of_Immortal]. Thần thông mở ở cảnh giới cao [trí nhớ] | Loại sách quyết định ô và cách dùng. Mỗi ô một vai rõ | Giữ phân loại, đổi cách kích hoạt sang gõ từ |
| Thanh chiến đấu | 4 ô kỹ năng và 1 ô tròn bên phải. Ô võ kỹ hiện hồi 0,0–0,2 s [video t160, t184] | Đòn chính gần như bấm giữ liên tục | Gõ không thể bắn 5 lần mỗi giây. Ta thay bằng đánh nền tự động và ô liên tục nạp băng |
| Một kỹ năng mẫu | Thân pháp cảnh Luyện Khí: hồi 20 s, tốn 25 Linh lực. Hóa 3 hồ lửa lao 400 đơn vị, gây 83 sát thương hỏa, rồi đưa người chơi tới con gần chuột nhất. Trang bị vào là được +33 di tốc, +11 hộ tâm. "Kỹ năng tu luyện 1/6", tiến độ 220/300; 6 dòng mở dần: chỉ số, giảm tiêu hao 1, thêm vùng lửa 14,36 s, +32 sát thương [video t120] | Kỹ năng lớn lên theo luyện tập; mỗi tầng thêm một dòng cụ thể, đọc được | Luyện công pháp 3 tầng (mục 4.6). Bỏ chỉ số bị động khi trang bị (thêm phức tạp, ít quyết định) |
| Tài nguyên | Sinh lực 810/916, Linh lực 213/253, Niệm lực 194/242 [video t004, t160] | Linh lực giới hạn tần suất chiêu | Ta đã có chi phí là thời gian gõ và hồi chiêu. Bỏ Linh lực theo chiêu; giữ một thanh Chân nguyên cho tuyệt kỹ |
| Đồ tiêu hao | 5 ô đạo cụ đưa vào trận, chỉ chứa đan dược và pháp bảo, mỗi ô tối đa 5 đan; tổng có hạn mức Niệm lực (99/242) [video t004]. Ô hiện số hồi sau khi dùng (17, 24, 18) [video t160, boss_14] | Mang theo có giới hạn, chọn trước trận | 3 ô đan, mỗi ô ≤ 3 lần mỗi ải, phím Alt |
| Rời trận | Nút "Trốn" (Esc) khi đang đánh; thành "Rời" khi đã sạch phòng [video t120, t140] | Luôn có đường thoát | Thủ ải không có nút trốn trong HUD; "Rút khỏi ải" nằm trong menu dừng (mục 5) |
| Cấu trúc trận | Phòng nối nhau, bản đồ nút góc phải, nút đỏ là boss, vòng âm dương là cửa [video t140, t184] | Nhịp đánh – dọn – đi tiếp | Không hợp thủ ải. Chỉ lấy ý "biết trước boss ở đâu" cho thanh đợt |
| Quái và phản hồi | Bầy xương cầm giáo, ma, dơi; số sát thương nhỏ (−51, −83), chữ "Bạo Kích"; phi kiếm có vệt sáng, nổ đỏ khi trúng [video t160, t184] | Số nhỏ, nhiều hit, vệt rõ | Gộp số nhỏ, giữ số chí mạng (Codex §26.7) |
| Boss | Boss thú to, máu 10.794; đá trụ trong sân làm chỗ che; nổ bụi lửa lớn [video boss_04–boss_27]. Khi máu còn khoảng 11 %, hiện vòng xanh và chữ "Nhấn phím E để hấp thụ yêu thú" [video boss_22, boss_27] | Boss có địa hình dùng được; kết boss có lựa chọn thưởng | Đá trụ thành Thạch Bích/vật che; "Phong ấn Thú vương" sau MVP (mục 4.7) |
| Đồng hành | Một sinh vật hồng đi theo nhân vật suốt trận [video t140–t184]. Có thể là linh thú, chưa chắc | Pet đi theo, không chiếm ô | Pet sau MVP (mục 4.9) |
| Chỉ số | Hội tâm/Hộ tâm, Bạo kích/Kháng bạo, Di tốc, Cước lực, Kháng công pháp/linh căn; thông thạo Đao, Thương, Kiếm, Quyền, Chưởng, Chỉ; linh căn Hỏa, Thủy, Lôi, Phong, Thổ, Mộc [video t004] | Thông thạo theo loại vũ khí và hệ | Mảng thuộc tính do phân tích khác lo; combat chỉ cần sát thương, phá thế, giảm sát thương, hồi chiêu, chí mạng |
| Định mệnh | Chọn tối đa 3 định mệnh lúc bắt đầu [web: wikipedia]. Người stream dự kiến bộ "thất tinh kiếm bộc, lôi lực từ xa, tiên thủ hậu công" [video t004] | Vài đặc tính đổi luật tạo ra build | Ta dùng Cơ duyên trong ải và tâm pháp (mục 4.6) |
| Góc nhìn, thể loại | Nhìn từ trên, nhập vai hành động trộn bullet hell [web: wikipedia] | Né đạn là kỹ năng tay | Không hợp người học gõ. Đòn báo trước phải giải được bằng kỹ năng gõ |
| Thú triều | Có sự kiện yêu thú tấn công vùng hoặc thành [trí nhớ, không xác nhận được qua web] | — | Không dựa vào. Luật thú triều là của ta |

Nguồn web: [Wikipedia: Tale of Immortal](https://en.wikipedia.org/wiki/Tale_of_Immortal), [kosgames: Techniques Guide](https://kosgames.com/tale-of-immortal-techniques-guide-5889/) (chỉ xác nhận tâm pháp có ô theo chỉ số, tuyệt kỹ có thời lượng cố định), kết quả tìm kiếm trích [earlyguides.com](https://earlyguides.com/tale-of-immortal) (bố cục ô; trang trả 404 khi mở).

**Không chép:** tên kỹ năng, tên boss, bố cục cuộn giấy, khung HUD, nét vẽ thủy mặc của QCBH. Mọi tên dưới đây là tên tạm của dự án.

## 3. Codex V2.2 nói gì, ta giữ / sửa / bỏ

| § | Codex đề xuất | Quyết định | Lý do |
|---|---|---|---|
| §1, §1.1–1.3 | Đi tự do bằng chuột/phím là nền; WASD qua trạng thái Tab | **Sửa:** neo trận vị, đi lại trong vùng trận và tiền tuyến ngắn. MVP: chuột phải và mũi tên; chế độ WASD (Tab) sau MVP. Voice dùng WASD | Thủ ải không cần arena rộng. Bắt rời tay khỏi hàng phím chữ làm giảm cả gõ lẫn học |
| §1.4 | Hợp đồng hành động: một từ một giao dịch có ID, ASR chỉ chốt kết quả cuối, không cast hai lần | **Giữ nguyên** | Đúng và cần cho mạng (mục 5) |
| §1.5 | 5 nhãn cast khi di chuyển | **Rút còn 3:** cast khi đi; dừng ngắn có báo (≤ 0,4 s); đặt đất. Không có "vận công lớn" ở MVP | Ít nhãn, dễ đọc |
| §1.6 | Trong trận và đứng yên là hai trục | **Giữ**, số thử ở mục 4.2 | Không bắt đứng; đứng có lợi nhỏ |
| §1.7 | Nhặt đồ, bí mật | **Sửa:** đồ thường tự hút trong vùng trận; vật đặc biệt rơi ở tiền tuyến là lý do xuất trận ngắn | Không biến combat thành dọn rác |
| §1.9, §9.2 | 4–6 ô lớn, deck theo vai | **Giữ, chốt 3 → 5 → 6 ô có chữ theo cảnh giới** | Người mới ít chữ hơn; ô tăng cùng năng lực |
| §3 (PA1) | Thân pháp và trận vị trên arena tự do | **Lõi, bản rút gọn:** 3 trận vị cố định trên bản đồ ải, thân pháp gõ để lướt giữa chúng | Hợp thể loại thủ ải, rẻ |
| §4 (PA2) | Ngự kiếm hành tiến, truy kích | **Ải đặc biệt sau MVP:** "Truy Thú Vương" cuối chương | Camera, đường bay, dựng màn đắt; không phải thủ ải |
| §5 (PA3) | Phá thế phản chế: thanh Thế, đọc đòn, nhiều đáp án | **Lõi cho tinh anh và Thú vương** | Cho boss chiều sâu mà không cần né đạn |
| §6 (PA4) | Ngưng thời lập chiêu | **Bỏ khỏi thủ ải.** Có thể thành ảo cảnh solo nếu sau này cần | Dừng thế giới hỏng nhịp đội và nhịp gõ liên tục; lỗi đồng hồ nhiều |
| §7 (PA5) | Điều quân nhiều tuyến | **Sau MVP:** ải 2–3 cổng và chế độ đội; MVP chỉ 1 ải, 2 đường đất, 1 đường trời | Cần AI, UI tốt; đội 7 người tự nhiên thành nhiều tuyến |
| §8 | Một cơ chế chính, tối đa một phụ mỗi ải | **Giữ** | Chống quá tải |
| §9.1 | Đánh nền 15–25 % cho lớp công | **Giữ, thêm trần:** gõ ≥ 60 %, phe phụ ≤ 35 %; cổng bot không gõ | Khớp trụ cột "gõ là sức mạnh" của Rồng Giữ Ải và cổng B5 ở `BALANCE.md` |
| §10 | Hồ sơ F/S/R/H, K0–K6 | **Giữ làm mục tiêu**, nhưng gắn theo build (tâm pháp, nhánh luyện), không chỉ theo trường phái | MVP chỉ 3 trường phái vẫn thử được cả F và R |
| §11 | 24 trường phái | **Bỏ khỏi phạm vi.** MVP 3, thêm 1 khi mở đội; mỗi trường phái mới phải qua cổng khác biệt | 24 bộ VFX, âm, cân bằng là quá sức |
| §12 | Buff, hồi, chồng buff, Tự Cường/Đồng Tu | **Giữ luật chồng buff §12.5.** Tự Cường/Đồng Tu đi cùng trường phái Phù | MVP chỉ có khiên và giảm sát thương của Thổ-thể |
| §13 | Pet nuôi, lệnh, ngân sách pet 70 | **Sau MVP**, đi cùng Ngự thú. Giữ ngân sách §13.3 | Pet cần AI, model, hoạt ảnh |
| §14–15 | Solo, bot, trận pháp 2–7 | **Giữ, thêm luật cung ải** (mục 5) | Chống người nhanh gánh cả đội |
| §16 | Bảng vai quái, timer phản ứng | **Giữ, chốt công thức** báo trước ở mục 4.7 | Đã khớp bảng §23.2 |
| §21–22 | Trần chỉ số, công bằng gõ | **Giữ** (giảm hồi chiêu tối đa 30 %, chất lượng từ có trần) | — |
| §26.6 | Kỹ năng hoàn chỉnh 7 bước | **Giữ, thêm luật âm** Q6 ở `tools/audio-lab/DECISIONS.md` | Chủ dự án chê tiếng "bụp", tiếng đồ chơi |

## 4. Đề xuất cho game chống ải thú triều

### 4.1 Một ải nhìn từ combat

```text
Tĩnh tọa trước trận (xem đợt, chọn deck, chọn đan, xem trước 8 từ mới)
→ [ Báo đợt 5 s → Thú triều 40–60 s → Nghỉ 15 s (đổi đan; Cơ duyên sau đợt 3, 6, 9) ] × 8–10
→ Lặng 10 s → Thú vương (2–3 pha) → Kết ải (thưởng, điểm luyện, sổ từ)
Thua: Hộ trận chung về 0, hoặc mọi người cùng ngã. Ngã cá nhân: hồi lại sau 8 s ở trận vị (thử).
```

### 4.2 Không gian và di chuyển

```text
  Bãi thú triều  →  2 đường đất + 1 đường trời
        │                │
  Tiền tuyến (8–12 m trước trận): xuất trận được; gia trì giữ 1,5 s rồi tắt
  Vùng trận (bán kính ~6 m): 3 trận vị Trái · Giữa · Phải
  Trận bàn ở cổng ải: thanh Hộ trận chung
```

| Trạng thái | Luật (số thử) |
|---|---|
| Trong vùng trận | Gia trì: +10 % sát thương, −10 % sát thương nhận. Đi lại tự do, không mất gia trì |
| Đứng yên ≥ 1,5 s trong vùng | Chỉ tâm pháp loại "định tâm" mới có thêm lợi. Không đổi độ chính xác, không tự hoàn thành từ |
| Ở tiền tuyến | Gia trì giữ 1,5 s rồi tắt; nối lại sau 1 s khi quay về. Được nhặt vật đặc biệt, đánh cận chiến sâu, chặn đường |
| Quái chạm trận bàn | Trừ Hộ trận theo loại quái (Tiểu yêu 1 %, tinh anh 4 %, thử) |
| Đồng đội | Không chặn thân nhau; quái chặn người chơi theo va chạm thường |

- **Điều khiển Typing:** a–z chỉ để gõ. Chuột phải lên đất là đi tới (đường đi theo lưới, `games/typing-defense/src/sim/nav`). Mũi tên đi trực tiếp. Không có WASD ở MVP.
- **Voice:** WASD và mũi tên đều đi, vì chữ cái không dùng để gõ.
- **Thân pháp bằng từ:** gõ xong là lướt tới điểm chuột đang rê, không rê thì tới trận vị kế theo chiều kim đồng hồ. Tay không rời hàng phím.
- **Luật cân bằng:** mọi đòn báo trước đều có ít nhất một cách giải bằng kỹ năng gõ, đứng tại chỗ. Bot "đứng yên" phải đạt cùng dải thắng với bot "cơ động" (cổng C4, mục 4.10).

### 4.3 Deck và các ô

| Ô | Vai | Hồi (thử) | Loại từ trên ô | Mở ở |
|---|---|---|---|---|
| — | **Đánh nền** tự động, không chữ | Theo trường phái | — | K0 |
| 1 | **Liên tục:** mỗi từ nạp một băng chiêu nhỏ | 0 s; từ mới hiện ngay khi gõ xong | Đã thuộc hoặc ôn, 3–5 chữ | K0 |
| 2 | **Chiêu chính A** | 8–10 s | Đang học, 4–7 chữ | K0 |
| 3 | **Hộ thân hoặc thân pháp** (chọn một trước trận) | 10–15 s | Đã thuộc, 3–5 chữ (ô cứu nguy không nhận từ khó) | K0 |
| 4 | **Chiêu chính B** | 10–14 s | Đang học, 4–7 chữ | K1 |
| 5 | **Tuyệt kỹ**, chỉ hiện chữ khi Chân nguyên đầy | Thanh 100 | Từ mới của ải, đã xem trước | K1 |
| 6 | **Thần thông** | 1 lần mỗi đợt hoặc 75 s | 6–9 chữ hoặc cụm 2 từ | K4 |
| Bị động | **Tâm pháp** 1 ô (K0), 2 ô (K2) | — | Không chữ | K0 |
| Phím | **Đan** 3 ô, Alt + 1/2/3, mỗi ô ≤ 3 lần mỗi ải, hồi chung 8 s | — | Không chữ, không thưởng học | K0 |

- **Chân nguyên:** +5 mỗi từ Chuẩn, +3 mỗi từ có lỗi, +2 mỗi chữ Ấn. Đầy sau ~20–25 từ, tức khoảng 55–70 s ở 35 WPM (thử). Tuyệt kỹ dùng hết thanh.
- **Chữ sống tối đa 8:** 5 ô (6 từ K4) + ≤ 2 chữ Ấn + ≤ 1 chữ sự kiện. Phải nằm trong ngân sách kit `N_max = min(16; A − 3)` (`dragon-lane/00-canon.md` §5). Ô đang hồi thì ẩn chữ, chỉ hiện vòng đếm. Thường chỉ 2–4 chữ cùng sống.
- Số ô không phải số kỹ năng học được. Ngoài trận người chơi có thể học nhiều sách, mỗi trận mang 5–6.

### 4.4 Gõ một từ thì chiêu chạy thế nào

1. **Hiện chữ:** ô sẵn sàng nhận một từ từ bộ từ của ải. Chữ đầu không trùng với chữ sống khác của chính người đó (`shared/game-kit/typing/letters.ts`, tầng 2 khi thiếu chữ cái). Không hai từ có khoảng cách sửa ≤ 1 cùng sống.
2. **Khóa:** phím đầu khóa mềm ô đó. Gõ đúng 1 chữ rồi phím kế là chữ đầu của ô khác thì đổi khóa, không tính lỗi (`typing/router.ts`). Backspace xóa một chữ, Esc nhả khóa.
3. **Chốt:** chữ cuối đúng tạo một giao dịch `Cast{actor, slot, actionId, wordId, tick, channel, quality}`. Chỉ một lần. Animation không nhân giao dịch.
4. **Đích:** theo luật đích của chiêu (gần cổng nhất, cụm dày nhất, nguy nhất, bản thân, đồng đội). Nếu chuột đang rê trên bãi thì lấy điểm đó, như Rồng Giữ Ải 01 §2.4. Không có đích hợp lệ thì ô giữ trạng thái "đã gõ" 3 s chờ đích, không tốn hồi chiêu (Codex §1.5).
5. **Chất lượng từ (thử):** Chuẩn (0 lỗi) ×1,10 hiệu lực và +1 điểm luyện; Nhanh (≤ 0,7 thời gian dự kiến theo E riêng) +1 Chân nguyên; Ẩu (≥ 2 lỗi) ×0,80. Trần ×1,15. Kênh nói: luôn ×1,00, không có Nhanh. Bảng xếp hạng tách theo kênh.
6. **Hồi chiêu** bắt đầu khi chiêu tung. Hồi xong thì ô nhận **từ mới**. Từ không bao giờ đổi khi người chơi đang gõ dở.
7. **Ô liên tục theo mô hình băng đạn của Tuyến Cuối** (`games/typing-survival/src/sim/weapons.ts`): mỗi từ nạp 1 băng, chờ tối đa 2 băng, băng tự xả trong 1,5–2,5 s. Gõ đều thì sát thương đều; ngừng gõ thì chỉ còn đánh nền.
8. **Hủy, gõ lại** không tạo sát thương, Chân nguyên, điểm luyện hay sự kiện học.

### 4.5 Ba trường phái MVP (tên tạm, số thử)

| Ô | **Kiếm tu** (S, chủ công, đơn mục tiêu và xuyên hàng) | **Hỏa tu** (F, dọn bầy) | **Thổ-thể tu** (F, giữ trận, phá thế, cận chiến) |
|---|---|---|---|
| Đánh nền | 1 phi kiếm mỗi 1,2 s, 0,12 W, tầm 10 m, nhắm quái gần cổng nhất | 1 hỏa cầu mỗi 1,5 s, nổ bán kính 1,5 m, 0,08 W mỗi con | 1 quyền mỗi 1,0 s, cung 120° bán kính 2,5 m, 0,15 W, Phá thế 2 |
| 1 Liên tục | **Ngự Kiếm Quyết:** nạp 3 phi kiếm, xả trong 1,5 s, mỗi kiếm 0,4 W, xuyên thêm 1 con (50 %) | **Xích Viêm Châm:** 1 hỏa châu nổ bán kính 2 m, 0,6 W mỗi con (≤ 6 con), gắn Bén Lửa 3 s | **Chấn Địa Quyền:** sóng nón 60°, 4 m, 0,7 W, đẩy lùi quái nhỏ 1 m, Phá thế 8 |
| 2 Chiêu A | **Nhất Tuyến Xuyên Vân** (9 s): đường 14 × 1,2 m, 2,0 W con đầu, −15 % mỗi con sau (sàn 40 %), Phá thế 20 | **Viêm Tuyến** (10 s): vệt lửa 8 × 2 m ngang đường, 5 s, 0,3 W/s mỗi con, trần 8 W | **Phá Sơn Chưởng** (9 s): dừng 0,4 s có báo, 3,0 W đơn mục tiêu, Phá thế 35 |
| 3 Hộ thân | **Hồi Kiếm Hộ Thân** (14 s): 5 s, chặn 3 đòn hoặc đạn nhắm mình hay đồng đội trong 2 m | **Hỏa Tráo** (15 s): vòng lửa bán kính 3 m trong 4 s, đẩy lùi quái nhỏ 1,5 m, 0,2 W/s | **Kim Cương Thân** (14 s): 5 s, −50 % sát thương nhận, kéo quái nhỏ trong 6 m, nhận thay 30 % sát thương của đồng đội trong 4 m |
| 4 Chiêu B | **Lạc Kiếm Trận** (12 s): ghim vùng bán kính 3 m trong 5 s, 0,35 W/s mỗi con, chậm 20 %, trần 6 W | **Bạo Viêm** (12 s): kích nổ mọi quái đang Bén Lửa trong 10 m, 1,2 W mỗi con (≤ 10 con) | **Thạch Bích** (12 s): tường 5 m chắn đường 6 s, máu 6 W; quái phải phá hoặc vòng |
| 5 Tuyệt kỹ | **Thiên Hà Kiếm Vũ:** 3 đợt trong 2 s, vùng bán kính 6 m, tổng 10 W chia đều (≤ 2,5 W mỗi con), Phá thế 40 | **Xích Diễm Phần Nguyên:** biển lửa 10 × 6 m trong 6 s, 0,5 W/s, quái nhỏ lùi 1 s | **Sơn Hà Trấn:** nện đất bán kính 7 m, tổng 4 W, choáng quái nhỏ 2 s (khống chế giảm dần), Hộ trận +10 % |
| Tâm pháp mẫu | **Kiếm Tâm** (S): từ Chuẩn cho băng kế +8 % chí mạng · **Tích Kiếm** (R): −8 % ở đợt 1, +3 % mỗi đợt sống qua, trần +24 % | **Hỏa Mạch** (F): +15 % sát thương lửa ở đợt 1–3, giảm dần còn +5 % ở đợt 8 | **Hậu Thổ** (định tâm): đứng yên ≥ 1,5 s trong vùng trận thì −15 % sát thương nhận |

- **Thân pháp dùng chung (thay ô 3):** **Lưu Vân Bộ** (10 s): lướt 5 m tới điểm chuột hoặc trận vị kế. Không miễn thương, chỉ không bị đẩy trong 0,3 s.
- **Trần vùng:** mỗi chiêu vùng ≤ 15 % tổng sát thương cả ải; một đòn vùng gây ≤ 60 % máu một cụm bầy (`BALANCE.md` §9.1). Khống chế cứng ≤ 35 % thời gian sống của quái.
- **Trường phái 4 (mốc đội online): Phù tu (H).** Đặt phù ấn lên đường (bẫy nổ, trói), dán phù lên đồng đội (khiên, cường công), giải ấn trên trận bàn. Kèm Tự Cường/Đồng Tu (Codex §12.2).
- **Kiểm thử ngân sách:** ở 35 WPM, ~22,7 từ mỗi phút (`dragon-lane/DESIGN.md` §5.2), chia khoảng 10 từ ô 1, 8 từ ô 2 và 4, 3 từ ô 3, 1 tuyệt kỹ. Ô liên tục ~1,0–1,3 W mỗi từ quy đơn mục tiêu; đánh nền ~0,10 W/s, khoảng 20 % đầu ra. Đây là số thử để bot đo, không phải kết quả.

### 4.6 Sức mạnh đầu – giữa – cuối

**Trong một ải (Cơ duyên):** sau đợt 3, 6, 9 chọn 1 trong 3. Mỗi trường phái 8 Cơ duyên riêng và 8 chung, gồm biến chiêu (Ngự Kiếm xuyên thêm 1), chỉ số (−10 % hồi ô 2) hoặc tâm pháp tạm. Học từ Long Ấn của Rồng Giữ Ải, không mang ra ngoài ải.

**Ngoài ải (cảnh giới, khớp K0–K6 của Codex §10.2):**

| Mốc | Tên gợi ý (tên chung của thể loại) | Combat mở thêm |
|---|---|---|
| K0 | Luyện Khí sơ kỳ | Đánh nền, ô 1–3, 1 tâm pháp, 3 đan |
| K1 | Luyện Khí hậu kỳ | Ô 4, tuyệt kỹ |
| K2–K3 | Trúc Cơ | Tâm pháp ô 2, tầng luyện 2, đổi thân pháp |
| K4–K5 | Kết Đan | Thần thông (ô 6), tầng luyện 3 với chọn nhánh |
| K6 | Nguyên Anh | Hợp kích nâng cao, đại trận 7 vị |

**Luyện công pháp (học từ "1/6" trong video, rút còn 3 tầng):** Sơ thành → Tiểu thành → Đại thành. Điểm luyện đến từ dùng chiêu bằng từ Chuẩn (trần 40 điểm mỗi chiêu mỗi ải, chống cày) và từ hoạt động tu luyện (mảng khác). Tầng 2 cho một dòng hiệu lực. Tầng 3 chọn nhánh **F** (mạnh ngay, ví dụ hồi −15 %) hoặc **R** (tích theo đợt, ví dụ +4 % mỗi đợt, trần +28 %). Nhờ vậy cùng một trường phái đi được đường F, S hoặc R, và MVP 3 trường phái vẫn thử được bảng F/S/R/H. Đổi nhánh ở Tĩnh tọa với chi phí nhỏ (Codex §10.3).

### 4.7 Thú triều, tinh anh, Thú vương

| Quái (vai theo Codex §16) | Mang chữ? | Đáp án chính |
|---|---|---|
| Bầy Tiểu yêu, nhiều hướng | Không | Đánh nền, ô liên tục, chiêu vùng |
| Thú giáp dày | Không | Chiêu đơn mạnh (Xuyên Vân, Phá Sơn), Bạo Viêm |
| Thú bay bắn xa | Không | Đánh nền ưu tiên quái bay; hộ thân chặn đạn |
| Thú bộc phá lao vào trận | Không; có vòng báo đỏ | Đẩy lùi, Thạch Bích, giết trước |
| Yêu tướng (tinh anh) | **1 chữ Ấn** khi lộ | Gõ Ấn hoặc chiêu có Phá thế; vỡ thế thì dồn lực |
| Thú vương | **Cụm Ấn** 2 chữ mỗi lần, theo pha | Phá thế, hộ thân, Thạch Bích, dồn lực khi vỡ |

- **Thanh Thế (thử):** Yêu tướng 100, Thú vương 300 mỗi pha. Chữ Ấn −25, chiêu có nhãn Phá thế −8 đến −40, đánh nền Thổ-thể −2. Về 0 thì **vỡ thế 6 s**: không ra đòn, nhận +50 % sát thương. Sau mỗi lần vỡ, lần kế cần ×1,5 Thế (tránh khóa boss mãi, Codex §5.3).
- **Thời gian báo trước** cho đòn cần đáp án gõ: `T ≥ 2 + 120 / E` giây (E sàn 25). Ra 6,8 s ở 25 WPM; 5,4 s ở 35; 4,0 s ở 60. Khớp bảng Codex §23.2 (đọc 1 s, 4 chữ đang dở, 6 chữ đáp án, đệm 1 s). Đòn né bằng chân: ≥ 2 s cộng thời gian đi ra khỏi vùng ở di tốc thường.
- **Mỗi đòn lớn có ≥ 2 đáp án.** Ví dụ Thú vương "Xích Nham Lang Vương" (tên tạm):
  - *Gầm trấn* (vùng quanh trận): hộ thân, hoặc ra tiền tuyến.
  - *Xung phong* (đường thẳng vào trận bàn): Thạch Bích, phá thế bằng Ấn, hoặc né.
  - *Triệu bầy* (2 cụm Tiểu yêu ở hai đường): chiêu vùng, tuyệt kỹ.
  - *Giáp nham* (khiên −70 % sát thương): Cụm Ấn hoặc Bạo Viêm.
  - Mỗi pha chỉ thêm một cơ chế mới; không ép đổi chỗ, gõ Ấn và chọn đáp án cùng lúc (Codex §16.2).
- **Phong ấn Thú vương (học từ cảnh "hấp thụ yêu thú" trong video):** khi Thú vương < 10 % máu, mở cửa sổ 8 s; gõ 2 chữ Phong ấn thì nhận Thú hồn (vật liệu pet, đan) thay một phần thưởng thường. Bỏ qua thì hạ bình thường. **Sau MVP**, đi cùng pet.

### 4.8 Dữ liệu kỹ năng (khung, dựa trên `DuelActionDefinition` của Space)

```ts
type SkillDef = {
  id: string; school: "kiem" | "hoa" | "tho" | "phu";
  slot: "nen" | "lienTuc" | "chieu" | "hoThan" | "thanPhap" | "tuyetKy" | "thanThong" | "tamPhap";
  wordBand: "known-3-5" | "learning-4-7" | "new" | "long-6-9" | "none";
  cooldownS: number;            // 0 for lienTuc; tuyetKy uses gauge
  castMode: "move" | "brief-root" | "ground";   // §1.5 reduced to 3 labels
  rootS?: number;               // brief-root only, <= 0.4
  target: "gateNearest" | "densest" | "threat" | "hover" | "self" | "ally" | "lane";
  shape: { kind: "line" | "cone" | "circle" | "chain" | "wall" | "zone"; r?: number; len?: number; w?: number; arcDeg?: number };
  damageW: number;              // per target, at quality x1.00
  totalCapW?: number;           // area skills
  posture?: number;             // Phá thế
  tags: ("aoe" | "cc" | "shield" | "posture" | "pierce" | "push")[];
  mastery: [MasteryLine, MasteryLine, { f: MasteryLine; r: MasteryLine }];
  quota?: { perTargetPerS?: number };          // §12.5, §21
};
```

Dữ liệu ở `content/`, sim thuần TS tất định như ba game hiện có. Không chuỗi từ nào nằm trong sim; sim chỉ giữ `wordId` (`typing/decks.ts`).

### 4.9 MVP và sau MVP

| MVP (bản thử dọc, solo + 2 bot) | Sau MVP |
|---|---|
| 1 ải, 2 đường đất + 1 đường trời, 3 trận vị, 8 đợt, 1 Thú vương 3 pha | Ải 2–3 cổng (PA5), Truy Thú Vương (PA2) |
| Kiếm, Hỏa, Thổ-thể: mỗi trường phái đánh nền + 4 chiêu + 1 tuyệt kỹ + 2 tâm pháp | Phù (mốc đội online), Ngự thú + pet (§13), Lôi (R) |
| Lưu Vân Bộ; 3 loại đan | Thân pháp thứ 2, pháp bảo trong ô đạo cụ |
| Cơ duyên 8 chung + 4 mỗi trường phái | Đủ 8 mỗi trường phái |
| Phá thế, chữ Ấn, Cụm Ấn | Phong ấn Thú vương, thần thông |
| Luyện công pháp tầng 1–2 | Tầng 3 chọn nhánh F/R |
| Typing; giao dịch Cast sẵn cho Voice | Voice, Hybrid |
| Bot đồng đội theo vai | Co-op online 2–3, Thất Tinh 7 |

### 4.10 Cổng bot cho mảng combat (thêm vào B1–B9 của `BALANCE.md`)

| Cổng | Ngưỡng |
|---|---|
| C1 Gõ là chính | Bot Không gõ thua trước đợt 3; phần sát thương ngoài gõ ≤ 40 % với bot Chuẩn |
| C2 Không chiêu nào quét sạch | Mỗi chiêu vùng ≤ 15 % tổng sát thương ải |
| C3 Ba trường phái ngang nhau | Tỉ lệ thắng của bot Chuẩn với từng trường phái chênh ≤ 8 điểm % |
| C4 Đứng trận chơi được | Bot đứng yên và bot cơ động cùng E: chênh thắng ≤ 10 điểm % |
| C5 Đội công bằng | Solo + 2 bot và đội 3 bot cùng preset: chênh thắng ≤ 5 điểm % |
| C6 Không cast đôi | Replay: mỗi `wordId` hoàn thành ra đúng một `Cast` |
| C7 Không ngộp | Ngộp O ≤ 8 % ở Cân bằng khi có 8 chữ sống |

## 5. Solo và đội

| Hình thức | Luật |
|---|---|
| **Solo thuần** | 3 trận vị, một người. Ải dùng bản "1 vị": mật độ ×0,45, Thú vương máu ×0,45 (thử). Tâm pháp Tự Cường được ưu tiên |
| **Solo + 2 bot (mặc định)** | Bản "3 vị". Bot lấp chỗ trước trận, không sinh thêm giữa đợt (Codex §14.1). Bot chọn trường phái bù vai còn thiếu |
| **Đội 2–3 người (+ bot)** | Bản "3 vị". Người thật chọn trận vị; bot lấp chỗ trống |
| **Thất Tinh 7 vị (mở rộng)** | 3 cổng × 2 vị + 1 trận nhãn chính ở giữa; mỗi cổng là một tuyến (PA5). Chỉ làm khi bản 3 vị đã qua cổng |

**Luật công bằng trong đội:**

- **Mỗi người chỉ thấy chữ của mình.** Ngân sách chữ và chữ đầu duy nhất tính riêng từng người. Kỹ năng của đồng đội hiện bằng icon và VFX gọn (Codex §26.9).
- **Cung ải:** mỗi trận vị giữ một cung (Trái, Giữa, Phải). Quái của cung sinh theo nhịp k của người giữ, `k = clamp(C(E_eff)/C_ref; 0,75; 1,30)` (`BALANCE.md` §4.1). Người chậm nhận ít quái hơn trong cung của mình; người nhanh không làm cả đội khó lên. Tối đa 15 % quái đi lạc sang cung bên cạnh.
- **Phiên bản ải khóa lúc vào.** Máu Thú vương theo số vị (3), không theo số người thật. Người rớt mạng: giữ chỗ 10 s, rồi bot tiếp quản; trả quyền điều khiển ở biên hành động, không bao giờ cả bot lẫn người cùng cast.
- **Hợp kích Tam Tài:** mỗi trận vị có một nhãn. Nhãn sáng khi chủ nhãn gõ đủ `8 × k` từ Chuẩn kể từ lần hợp kích trước, nên người chậm cần ít từ hơn. Đủ 3 nhãn thì mỗi người thấy một chữ hợp kích riêng; người đầu tiên gõ xong chốt cho cả đội. 2/3 nhãn thì hiệu lực 60 %. Thử: 15 W chia trên vùng, Phá thế 60, Hộ trận +10 %. Pet và đánh nền không nạp nhãn.
- **Buff đội:** cùng ID lấy mạnh nhất; khiên có trần theo người (Codex §12.5, §21).
- **Thưởng:** loot cá nhân; thưởng phổ thông theo hoàn thành và đóng góp hợp lệ (sát thương, khiên đã đỡ, phá thế, nhãn), không theo last-hit (Codex §22.3). Bot không có túi thưởng, không tạo sự kiện học.
- **Rút khỏi ải:** một người rút thì bot thế chỗ, người đó giữ điểm học đã có, không nhận thưởng ải. Cả đội bỏ ải cần 2/3 phiếu.
- **Preset chốt trước trận.** Mỗi người có bộ từ riêng trong dải công khai (Codex §22.2). Bảng xếp hạng tách solo, đội bot, đội người, và tách kênh Typing/Voice.
- **Mạng (ghi nhận để mảng online quyết):** sim tất định nên chỉ cần chuyển lệnh `Move`, `Cast`, `UseItem` có tick qua một phòng Durable Object làm trạm chuyển, không chạy sim trên server, để vừa gói Cloudflare Free. Voice chốt kết quả ở máy người chơi rồi mới gửi `Cast`. Có thể tham khảo `games/space-typing/src/duel/{protocol,network-client,authority}.ts`.

## 6. Gắn với học tiếng Anh

| Nguồn chữ | Loại từ | Độ dài | Khi nào hiện |
|---|---|---|---|
| Ô 1 liên tục | Đã thuộc, đến hạn ôn | 3–5 chữ (E < 25: 3–4) | Luôn có; đổi mỗi lần gõ xong |
| Ô 2, 4 chiêu chính | Đang học | 4–7 chữ theo E (bảng 01 §3.4 của Rồng Giữ Ải) | Khi hồi xong |
| Ô 3 hộ thân, thân pháp | Đã thuộc | 3–5 chữ | Khi hồi xong; không bao giờ nhận từ mới |
| Ô 5 tuyệt kỹ | Từ mới của ải (8 từ, đã xem ở Tĩnh tọa) | Theo từ | Khi Chân nguyên đầy; IPA và nghĩa hiện cạnh ô |
| Ô 6 thần thông | Từ dài hoặc cụm 2 từ của chủ đề | 6–9 chữ | 1 lần mỗi đợt |
| Chữ Ấn | Đến hạn ôn; từ C3: Hỏi nghĩa (thấy nghĩa Việt, gõ tiếng Anh) | 4–6 chữ | Khi tinh anh lộ, theo pha boss |

**Tránh quá tải:**

- Tối đa 8 chữ sống; chỉ một loại chữ đặc biệt mới tại một lúc (`dragon-lane/00-canon.md` §5).
- Khi có đòn báo trước cần đáp án gõ, không sinh từ mới trên ô 2, 4, 5 cho tới khi đòn qua.
- Khung học (IPA, nghĩa, nút nghe) là DOM cố định cạnh thanh kỹ năng, hiện từ vừa tung. Không rung, không bị VFX che (Codex §26.9).
- Nghĩa ẩn dần theo số lần nhớ đúng, không theo số lần gõ chép (Rồng Giữ Ải 01 §6.3).
- Mỗi từ mỗi ải ghi đúng một sự kiện học có chấm, qua `shared/game-kit/learning`. Từ gõ bởi bot, pet, đánh nền không tạo sự kiện.

**Typing, Voice, Hybrid:**

- Typing: như mục 4.4. Chỉ từ không lỗi mới tính đúng trong sự kiện học.
- Voice: nói từ trên ô. Kết quả tạm chỉ tô sáng ô, không cast. Kết quả cuối khớp `wordId` đang sống mới cast. Kết quả đến muộn cho ô đã đổi từ thì bỏ. Không có Nhanh; ×1,00. Âm thanh game và phát âm mẫu không được tự kích hoạt kỹ năng (Codex §26.10).
- Hybrid: mỗi từ thuộc một kênh từ phím hoặc âm đầu tiên tới khi xong hoặc hủy. Hai kênh cùng hoàn thành thì chỉ chốt một.

## 7. Tái sử dụng và chi phí

| Phần | Lấy từ | Việc phải làm | Chi phí |
|---|---|---|---|
| Bộ từ, chữ đầu, khóa mềm, chấm từ, nhịp | `shared/game-kit/typing/{decks,letters,router,scorer,tempo,budget,session}.ts` | Thêm nguồn chữ "ô kỹ năng" vào ngân sách | S |
| Hồ sơ năng lực, FlowMeter, bộ điều nhịp, bot gõ giống người, cổng | `shared/game-kit/balance/*`, `docs/games/BALANCE.md` | Nhịp k theo từng cung; bot theo vai | S–M |
| Mô hình "từ nạp băng, súng tự xả", chất lượng Chuẩn/Nhanh | `games/typing-survival/src/sim/weapons.ts`, `src/content/guns.ts` | Viết lại thành ô liên tục 3 trường phái | S |
| Đợt, sinh quái, trạng thái, hào quang tướng, boss pha, ngân sách chữ | `games/dragon-hold/src/sim/{waves,spawn,director,status,auras,boss,words}.ts`, `dragon-lane/00-canon.md` §4–5 | Dùng sim; đổi đường thành cung ải; thêm thanh Thế | M |
| Tìm đường cho click-to-move, bot, pet | `games/typing-defense/src/sim/nav/{grid,astar}.ts` | Lưới vùng trận và tiền tuyến | S |
| Khung dữ liệu hành động, hồi chiêu, bot, giao thức phòng | `games/space-typing/src/duel/{actions,cooldowns,bots,protocol,network-client,authority}.ts`, `games/space-typing/cloud/src/*` | `SkillDef` mục 4.8; phòng co-op | M (dữ liệu) · L (mạng) |
| Phản hồi trúng đòn, số sát thương, dừng hình | `shared/game-kit/feedback/{numbers,hitstop,tiers,reaction}.ts` | Hồ sơ "tu tiên"; gộp số nhỏ | S |
| Sự kiện học | `shared/game-kit/learning/*` | gameId mới | S |
| Nhận giọng nói | `shared/game-kit/speech/*`, runtime Voice của Space | Giao dịch Cast theo `wordId` | M |
| Âm | `docs/games/AUDIO_PIPELINE.md`, `tools/audio-lab/DECISIONS.md` Q6 | ~40 tiếng ghi âm CC0 cho MVP: kiếm rít, lửa gầm có vang, đất nện nặng; không "bụp" | M |
| VFX 2D theo 7 bước | Codex §26.5–26.6 | ~18 kỹ năng MVP, sprite sheet, cap hạt | L |

**Ước lượng toàn mảng:** MVP solo + bot ≈ M–L (sim và bot M, VFX và âm L). Co-op online 2–3 người: L. Thất Tinh: L.

## 8. Rủi ro và câu hỏi cho chủ dự án

**Rủi ro chính**

| Rủi ro | Giảm bằng |
|---|---|
| Rời tay khỏi phím chữ để đi lại làm hỏng nhịp gõ | Đứng trận chơi được trọn vẹn (cổng C4); thân pháp bằng từ; Voice dùng WASD |
| Gõ ô kỹ năng thành gõ chép, không học | Từ đổi theo lịch; ô liên tục dùng từ ôn; từ mới chỉ ở tuyệt kỹ, có xem trước; nghĩa ẩn dần |
| Chiêu vùng quét sạch thú triều, hết căng | Trần 15 % mỗi chiêu, 60 % mỗi cụm; cổng C2 |
| Đánh nền quá mạnh nên treo máy vẫn thắng | Cổng C1; đánh nền ≤ 25 % |
| Trong đội, người nhanh gánh, người chậm thấy thừa | Cung ải với nhịp k riêng; nhãn hợp kích theo k; mỗi người chỉ thấy chữ mình |
| Màn đông (hàng trăm quái, 3 người cùng tuyệt kỹ) khó đọc | Ưu tiên đòn của mình và nguy cơ nhắm mình; VFX đồng đội gọn; vùng chữ không bị che (Codex §26.9) |
| Phạm vi phình theo QCBH | MVP 3 trường phái; mỗi trường phái mới phải qua cổng C3 và có VFX, âm riêng trước khi nhận |

**Câu hỏi (mỗi câu có phương án đề xuất)**

| # | Câu hỏi | Đề xuất |
|---|---|---|
| 1 | Lõi combat là trận vị neo + phá thế phản chế; PA2, PA5 là ải đặc biệt sau MVP; bỏ PA4 khỏi thủ ải? | Có |
| 2 | Quái thường không mang chữ; chỉ tinh anh và Thú vương mang chữ Ấn? | Có. Giữ chữ cho ô kỹ năng, tránh ngộp khi có hàng trăm quái |
| 3 | Mặc định đứng trận; đi lại bằng chuột phải và mũi tên trong vùng trận và tiền tuyến; WASD (Tab) để sau? | Có |
| 4 | Bỏ Linh lực tiêu theo từng chiêu; chỉ có hồi chiêu và thanh Chân nguyên cho tuyệt kỹ? | Có. Chi phí thật của chiêu là thời gian gõ |
| 5 | MVP 3 trường phái Kiếm, Hỏa, Thổ-thể; Phù khi mở đội online; Ngự thú và pet sau? | Có |
| 6 | Deck 3 ô có chữ ở K0, 5 ô ở K1, 6 ô ở K4? | Có |
| 7 | Đội: MVP là solo + 2 bot; online 2–3 người ở mốc sau; Thất Tinh là mở rộng cuối? | Có |
| 8 | Đan dùng Alt + 1/2/3, không gõ, không thưởng học? | Có. Đồ cứu nguy không nên bắt gõ |
| 9 | Từ trên ô đổi mỗi lần hồi xong (ô liên tục đổi sau mỗi từ), không cố định cả ải? | Có |
| 10 | Luyện công pháp 3 tầng, điểm từ dùng chiêu bằng từ Chuẩn (có trần) và từ tu luyện? | Có |
| 11 | Thêm "Phong ấn Thú vương" lấy Thú hồn (ý từ cảnh hấp thụ yêu thú trong video)? | Có, nhưng sau MVP, cùng lúc với pet |
| 12 | Cung ải: quái mỗi cung sinh theo nhịp của người giữ cung đó? | Có. Đây là luật công bằng chính của chế độ đội |
