# Tu Tiên Thủ Ải: 08. Phản biện tổng hợp (24/10/2026)

> **Vai:** người phản biện. Tìm chỗ hỏng trong đề xuất ghép từ 7 tệp `01`–`07`. Không viết lại thiết kế.
> **Đã đọc:** toàn văn `01`–`07`; Codex V2.2 §0, §1.9, §14, §26, §27; `docs/games/BALANCE.md` §4–§7; `docs/games/SPLIT_PLAN.md`; `games/dragon-hold/docs/changelog/2026-10-24-m0a-round2-gate.md`; `shared/voice/README.md`; `shared/vocabulary/topics/index.json`; trang giá và vòng đời Durable Objects của Cloudflare.
> **Mức:** **chặn** = phải chốt trước khi viết mã hoặc trước khi sản xuất hình · **lớn** = phải sửa trước MVP · **nhỏ** = sửa khi viết canon.
> **Nguồn:** `0x §y` là tệp phân tích; [Codex §x]; [repo: đường dẫn]; [web: url]; [video] là bản quay QCBH của chủ dự án.

## 1. Kết luận ngắn

1. **Chưa có nguồn chân lý.** Bảy tệp mô tả ba vòng chơi khác nhau, ba bản MVP khác nhau và bốn cách đánh số mốc. Cần một `00-canon.md` (giống `dragon-lane/00-canon.md`) trước khi viết mã. Không có tệp này thì mỗi làn agent sẽ cài một bản game riêng.
2. **Phạm vi không trôi về thế giới mở, nhưng trôi về "QCBH bỏ bản đồ".** Cộng các tệp lại có khoảng 20 hệ tiến trình chồng lên một game thủ ải, Sơn Môn có tới 12 điểm, và có 9 đến 14 loại tiền hay điểm.
3. **Chỗ hại việc học nặng nhất:** không có ngân sách từ mới chung. Có 5 luật khác nhau về chỗ đặt từ mới, và một tệp đặt từ mới lên chính ô tự cứu.
4. **Chế độ đội đang mâu thuẫn ở tầng kiến trúc.** `04` cho Durable Object chạy sim và quyết loot. `06` cấm việc này để vừa gói Free. `05` thiết kế thú và boss nhắm vào vị trí người chơi, điều mà kiến trúc của `06` không cho phép.
5. **Hướng hình 3D của `07` trái với yêu cầu chủ dự án đã nêu** ở [Codex §0]: 2D/sprite, không mặc định runtime 3D cho đông quái. Việc này phải hỏi anh, không tự chọn theo đề xuất.
6. **Trùng Rồng Giữ Ải ở mọi tầng ngoài trận.** Phần sim định chép từ đó còn trượt B1/B7. Typing ở đó cũng mới gánh 54 % sát thương. Thiết kế tu tiên lại thêm đánh nền và bỏ chữ trên quái thường, nên mục tiêu "gõ ≥ 55–60 %" càng khó đạt.

## 2. Bảng vấn đề

| # | Vấn đề | Mức | Nhóm |
|---|---|---|---|
| A1 | Vòng chơi, MVP và mốc mâu thuẫn giữa các tệp | **chặn** | Mâu thuẫn |
| D1 | Quyền sim và vị trí người chơi khi chơi đội: 04, 05, 06 loại trừ nhau | **chặn** | Đội, online |
| C1 | Từ mới: 5 luật, có luật đặt lên ô tự cứu, không có ngân sách chung | **chặn** | Học |
| E2 | Hình 3D runtime (07) trái yêu cầu 2D của chủ dự án | **chặn** (cho M0b) | Sản xuất |
| A2 | Tiền tệ vượt trần 3 | lớn | Mâu thuẫn |
| A3 | Thanh tài nguyên, số ô kỹ năng, ô đan | lớn | Mâu thuẫn |
| A4 | Gục, thua và phần thưởng giữ lại: 4 mô hình | lớn | Mâu thuẫn |
| B1 | Meta khoảng 20 hệ, Sơn Môn 12 điểm | lớn | Phình QCBH |
| C2 | Tĩnh tọa thưởng phản xạ, bắt trả tiền để học, Ngộ tính ngược chiều | lớn | Học |
| C3 | Trẻ em và người gõ chậm bị bỏ khỏi công thức và cổng | lớn | Học |
| C4 | Voice bị phạt sát thương; lịch Voice lệch nhau | lớn | Học |
| C5 | Cửa sổ báo đòn của Thú Vương mẫu sai theo chính công thức của nó | lớn | Học, cân bằng |
| D2 | Hạn mức Free: timer phá hibernation; số request lệch nhau | lớn | Đội, online |
| D3 | Nhịp k đội có 3 mô hình; hợp kích thành cuộc đua; vai đội có 4 trục | lớn | Đội |
| E1 | Tổng MVP vượt xa sức một người cộng agent | lớn | Sản xuất |
| F1 | Trùng Rồng Giữ Ải; chép sim đang trượt cổng | lớn | Trùng lặp |
| G1 | Thiếu onboarding; quá nhiều lựa chọn trước trận đầu | lớn | Thiếu |
| G2 | Thiếu IME tiếng Việt, va chạm phím tắt, tiếp cận | lớn | Thiếu |
| G3 | Preset lệch BALANCE; độ dài phiên vượt mốc nhắc nghỉ | lớn | Thiếu |
| G4 | Lưu, tài khoản và cầu học khác origin chưa chốt | lớn | Thiếu |
| A5 | Số hệ, công thức tăng sức, tên gọi, mã cổng | nhỏ | Mâu thuẫn |
| B2 | Còn sót chất QCBH | nhỏ | Phình QCBH |
| C6 | Độ Kiếp chặn tiến trình bằng từ yếu nhất; Tâm Ma tăng vì nợ ôn ở game khác | nhỏ | Học |
| D4 | Thưởng đội, chat trẻ em | nhỏ | Đội |
| G5 | Cố tình gõ chậm để hạ k và hạ ngưỡng Chớp | nhỏ | Thiếu |

## 3. Mâu thuẫn giữa các tệp

### A1 · Vòng chơi, MVP và mốc · **chặn**

- **Đơn vị chơi.** `01 §4.1`: một "Thú Triều" là một lượt 6 trận + Thú Vương, kéo dài 35–45 phút, có Doanh Trại, cả đường chính có 21 Thú Triều. `05 §4.9`: một chương là một ải gồm 8 trận, Đại Triều 10 đợt dài khoảng 12 phút. `03 §4.1`: một ải có 8–10 đợt, Cơ duyên chọn sau đợt 3/6/9. `07 §4.6`: một ải có 6 đợt + Thú vương, dài 7–9 phút. Cơ Duyên nằm ở ba chỗ khác nhau: trong ải (`03`), ở Doanh Trại (`01`), lúc nghỉ và để sau MVP (`05 §4.11`).
- **MVP.** `01 §4.12`: 6 Thú Triều × (4 trận + Thú Vương), tức khoảng 30 trận và 6 Thú Vương. `05 §4.11`: 1 ải, 1 Thú Vương, 1 lớp kiếm tu, chỉ solo. `03 §4.9`: 3 trường phái, solo + 2 bot. `07 §4.11`: 2 trường phái, solo + 1 bot. `02 §4.10`: 3 hệ người chơi Thủy/Mộc/Hỏa, trong khi trường phái Thổ-thể của `03` lại thuộc hệ Thổ mà `02` không mở cho người chơi ở MVP.
- **Mốc.** M1 nghĩa là "bot + Voice" ở `05`, "Độc tu + bot" ở `06`, "Tĩnh Tu + meta" ở `07`. Co-op online là M2 ở `05` và `07`, nhưng là M3 ở `06`.
- **Sửa:** viết `docs/games/tu-tien/00-canon.md` trước mọi mã: một bảng số, một từ điển thuật ngữ, một lộ trình mốc. Đề xuất lấy khung ít tốn nhất: **chương = 1 ải (05)**, trận thường ≤ 7 phút, Đại Triều cuối chương; **Cơ Duyên chỉ trong trận (03)**; bỏ "lượt 40 phút" của `01` ở v1 (xem G3). MVP lấy lát chơi của `07` (xem E1).

### A2 · Tiền tệ vượt trần 3 · lớn

- `04 §4.2` chốt ba tiền: Linh Sa, Văn Khí, Thú Hạch. `01 §4.10` chốt ba tiền khác: Linh Thạch, Thú Hạch (có bậc theo cảnh giới, tức nhiều tiền đội lốt một tiền), tu vi. `05 §4.10` thêm Trận Nguyên, Linh Thạch, Yêu Đan (theo họ, hệ, phẩm), Nguyên liệu vùng "cho Kỹ nghệ", Tàn trang công pháp, Tri Thức, Công Huân. `06 §4.7` thêm Hộ đạo điểm. `01 §5` thêm điểm Nhân Quả. `03 §4.7` thêm Thú hồn.
- Cộng lại có 9 đến 14 loại. `05` còn đưa kỹ nghệ trở lại, trong khi `01`, `02` và `04` đều đã bỏ.
- **Lỗi học:** `01 §4.4` thu **3 Thú Hạch mỗi phiên lĩnh ngộ**. Người học chậm cần thêm phiên (`01 §4.5`: người mới cần 2 phiên), nên phải trả nhiều tiền hơn để học cùng 6 từ.
- **Sửa:** chỉ giữ ba tiền của `04`. Tu vi là thanh kinh nghiệm, không gọi là tiền. Trận Nguyên gộp vào Linh Sa; Linh Thạch gộp vào Thú Hạch. Yêu Đan, Tàn trang, Thú hồn và "nguyên liệu" chỉ là **tên hình** của khoản đã ghi sổ (đúng luật `04 §4.4`). Công Huân, Hộ đạo, Nhân Quả chỉ là danh hiệu. Học không bao giờ tốn tiền.

### A3 · Thanh tài nguyên, ô kỹ năng, ô đan · lớn

- **Thanh.** `02 §4.2` giữ Linh lực (chiêu tốn 20–40) và thêm Định Tâm cho Tuyệt kỹ. `03 §4.3` bỏ Linh lực theo chiêu và dùng Chân nguyên. `05 §4.2` có Trận Ý. `07 §4.3` cho Thần thông "nạp khoảng 45 s". Nếu cộng hết, HUD có Sinh lực, Linh lực, Định Tâm hoặc Chân nguyên, Trận Ý, Trận Lực và thanh Thế của boss.
- **Ô có chữ.** `01 §4.2`: 4 ô ở K0. `03 §4.3`: 3 → 5 → 6. `05 §4.3`: 5 + Kết Ấn ngay ở MVP. `07`: 5, ô 6 mở ở cảnh giới 2. Hồi chiêu lệch nhau: Chiêu A 8–10 s (`03`) và 6 s (`07`); Hộ thân 10–15 s, 15 s và 20 s. Vì vậy bảng tải gõ của `03 §4.5` và `07 §4.3` không so được với nhau.
- **Đan.** `03`: 3 ô ở K0. `04 §4.5`: 2 ô, ô 3 mua bằng Văn Khí. `01`: ô 4 ở K2, ô 5 ở K5. `05 §2` dòng 2 lại **bỏ ô đan khỏi trận**, thay bằng cơ quan.
- **Sửa:** HUD v1 gồm Sinh lực, **một** thanh tuyệt kỹ (gộp Định Tâm, Chân nguyên và Thần thông) và Trận Lực chung. Bỏ Linh lực. Ô theo `03`. Đan 2 ô, ô 3 mở ở Thư Lâu. Phím xem G2.

### A4 · Gục, thua và phần thưởng giữ lại · lớn

- **Gục.** `05 §4.3`: nằm 8 s rồi dậy, Trận Lực −5 %. `06 §4.5`: gục, đồng đội cứu bằng một từ bất kỳ, tự dậy sau 15 s. `01 §4.8`: Mệnh Đăng, 2 lần hồi sinh mỗi Thú Triều. `04 §4.5`: Hoàn Hồn Đan giá 150. Nếu hồi sinh miễn phí sau 8 s thì Mệnh Đăng và Hoàn Hồn Đan vô nghĩa.
- **Thua.** Phần thưởng giữ lại là 50 % (`01`, `05`), 30 % (`04`), 100 % thưởng các đợt đã qua (`06`), 0 % thưởng ải khi rút (`03`). Luật của `06` có lỗ: thưởng đợt nhân với thời gian có mặt, thua vẫn giữ 100 %, lại được bỏ phiếu thủ lại đợt. Người chơi có thể cày các đợt đầu rồi bỏ.
- **Sửa:** solo nằm 8 s; đội gục và cứu bằng từ bất kỳ. Bỏ Mệnh Đăng và Hoàn Hồn Đan. Thua giữ 50 % Thú Hạch. **Văn Khí và mọi kết quả học không bao giờ mất.** Đợt đã qua chỉ trả thưởng một lần cho mỗi bậc ải.

### A5 · Số liệu và tên gọi · nhỏ

- Khắc hệ: ±20 % (`05 §4.4`) so với ×1,30/×0,80 (`02 §4.3`). `05 §4.3`: chiêu gõ bỏ qua giáp **và kháng**. `02`: kháng hệ vẫn có tác dụng. `05` cho Phong Lang hệ Phong, trong khi `02` xếp Phong vào dị hệ sau MVP.
- `03 §4.5` có tâm pháp "Kiếm Tâm: +8 % chí mạng", trái luật không có chí mạng ngẫu nhiên của `02 §4.3`. Trần chất lượng từ ×1,15 (`03`) không chứa được Bạo kích 1,30–1,80 (`02`).
- Máu đội có 3 công thức: `02 §4.6` 1 + 0,8(n−1); `05 §5` ×1,7/×2,4/×5,0; `03 §5` solo ×0,45. Tăng sức theo cảnh giới có 2 công thức: g(K) = 1,12^K (`02 §4.7`) và R = 1 + 0,05(k−1) + 0,08·đại cảnh (`01 §4.2`). Đơn vị W có 3 định nghĩa (`03`, `05`, `02` dùng máu tuyệt đối).
- **Tên trùng:** "Định Tâm" là thanh ở `02`, nhưng là thưởng đứng yên ở `01` và `03`. `02` đổi thưởng đứng yên thành "Tĩnh tọa", trùng với mini-game tĩnh tọa của `01`. `07` gọi mini-game là Tĩnh Tu. Cảnh giới K4 là Hóa Thần ở `01` nhưng Kết Đan ở `03`. Mã cổng E1–E4 (`02`) trùng E1–E7 (`04`).
- **Sửa:** từ điển thuật ngữ và bảng số trong canon. Mã cổng có tiền tố theo mảng (EL-, EC-, CB-, NW-).

## 4. Phình về QCBH

### B1 · Meta khoảng 20 hệ chồng lên một game thủ ải · lớn

- Không tệp nào đề xuất thế giới mở. Nhưng cộng lại thì có: cảnh giới 21 kỳ, tu vi, Độ Kiếp 3 pha, Củng Cố, Đạo Ấn, công pháp (lĩnh ngộ, thuần thục, tham ngộ, thăng tầng), Khí Vận, Cơ Duyên (hai nơi), Hung Cát, Tâm Ma, Ngộ tính (`01`); Mệnh cách 3 dòng lúc tạo nhân vật, linh căn phẩm 1–5, đan tẩy linh căn (`02 §4.7`, Q5); tâm pháp, luyện 3 tầng (`03`); pháp bảo, Hộ Thân Y, Ngọc Bội, Thư Lâu 10 bậc, Đan Lô, Luyện Khí, Khí Linh, Bảng Truy Thú, Tàng Y Các (`04`); Phân thân, Hộ đạo (`06`).
- Sơn Môn có 7 điểm ở `01 §4.11` và 7 điểm **khác** ở `04 §4.9`. Gộp lại khoảng 12 điểm, vượt "luật cứng tối đa 7" của chính `01 §8`.
- Mệnh cách (`02`) và Khí Vận (`01`) cùng là bản sao của NTCM. Cả hai nhân chéo với Đạo Ấn, tâm pháp, Cơ Duyên và pháp bảo, tức 8 nguồn bổ trợ dồn vào bucket [Codex §21].
- Có 4 mô hình lớn lên của kỹ năng: thuần thục + tham ngộ (`01 §4.4`), Sơ/Tiểu/Đại thành (`03 §4.6`), dòng 1–6 (`07 §4.5`), dòng mở theo số từ đúng (`05 §6`).
- **Sửa:** v1 giữ tối đa **4 hệ lâu dài**: thanh cảnh giới, công pháp = bài học (một mô hình luyện duy nhất), pháp bảo cố định, Thư Lâu. Bỏ Mệnh cách, giữ Khí Vận nhưng chỉ dùng trong trận. **Gộp Độ Kiếp vào pha cuối của Thú Vương Đại Triều**, không làm thành một chế độ riêng. Sơn Môn v1 có 4 điểm: Trận Đài, Tĩnh Thất, Thư Lâu, Bảo Khí Lò.

### B2 · Còn sót chất QCBH · nhỏ

- `01 §4.6` cho Ngộ tính đổi vòng đời và tỉ lệ sinh mảnh, đúng như HUD "Ngộ tính · tỉ lệ sinh ngộ cầu · tốc độ cầu" [video 0:14–0:44]. "Niệm lực" là tên chỉ số riêng của QCBH [video 0:00]. Dùng "Linh Thạch" làm tiền chính cũng giống QCBH.
- **Sửa:** theo quy trình [Codex §20]. Tên chỉ số và tiền lấy từ canon riêng. Ngộ tính không điều khiển mini-game (xem C2).

## 5. Hại việc học

### C1 · Từ mới không có ngân sách chung · **chặn**

- **Năm luật khác nhau:** `05 §6` đặt 8 từ mới mỗi trận lên **ô Kiếm Khí (liên tục) và ô Hộ Thể (tự cứu)**. `03 §6` đặt từ mới chỉ lên Tuyệt kỹ và nói rõ ô cứu nguy không nhận từ khó. `07 §6.2` cấm từ mới trên ô hộ thân và Từ Khẩn, chỉ cho lên Chiêu B ở đợt 1–2. `04 §6` ghi "từ mới chỉ xuất hiện trên **thú chậm**", tức vẫn nghĩ theo mô hình chữ trên quái của Rồng. `06 §6` chỉ cho từ mới lúc đầu đợt và lúc nghỉ.
- **Không có trần chung.** `01 §6` cho tới 12 từ khẩu quyết mỗi lần về Sơn Môn. `05` thêm 8 từ mỗi trận, và một Thú Triều có 4–6 trận. `04` và `05` có thêm Học trước 8 từ. Một lượt 40 phút có thể gặp **50–60 từ mới**, so với `newMax: 6` mỗi ải ở `07 §4.2`.
- **Sửa (luật canon):** (1) trần từ mới **mỗi phiên chơi** do lõi học chung cấp, ví dụ ≤ 8 từ cho 20 phút, gồm cả tĩnh tọa và trận; (2) từ mới chỉ ở Học trước, Tĩnh Tu và một ô không gấp (Chiêu B); (3) ô liên tục, hộ thân, Ấn, Tẩy, Từ Khẩn, Linh Mạch, Bảo Hạp chỉ dùng từ đã thuộc hoặc đến hạn; (4) khi nợ ôn cao thì giảm từ mới (`01 §6`, Rồng 04 §7.2). Thêm cổng: trong replay, 0 lần từ mới xuất hiện trên ô gấp.

### C2 · Tĩnh tọa thưởng phản xạ hơn tiếng Anh · lớn

- Ở `01 §4.5`, Tạp Niệm là từ **đã thuộc**, được nhận ra bằng viền và biểu tượng ☼/✕. Né nó là phản xạ kiềm chế, không có nội dung tiếng Anh. Điểm phiên tính theo số Minh "bắt" được trong vòng đời, nên vẫn là gõ chép có đồng hồ.
- **Ngộ tính đi ngược chiều.** Ngộ tính = 50 + N70/25 (`01 §4.6`), và Minh sống lâu hơn khi Ngộ tính cao. Người mới, có ít từ thuộc nhất, lại nhận **vòng đời ngắn nhất** đúng lúc cần thời gian nhất.
- **Ghi sai do mơ hồ chủ đề.** `07 §4.5` sửa đúng hướng (chọn theo nghĩa), nhưng ghi `meaning-recall` **sai** khi người chơi gõ một Tâm ma không nhãn. Thuộc chủ đề nào không phải là hiểu nghĩa từ. Chủ đề lại mơ hồ: 101 chủ đề chỉ có 835 khóa từ khác nhau, phần lớn ở A1–A2 [repo: `shared/vocabulary/topics/index.json`]. (`01 §7` ghi 1.177 là sai.)
- **Sửa:** dùng bậc của `07`. Nhập Môn không bị thời gian ép (thẻ Khẩu Quyết của `01` là đủ). Gõ nhầm Tâm ma chỉ ghi "chọn nhầm", **không bao giờ** tạo sự kiện học âm. Ngộ tính chỉ thêm lựa chọn Tham ngộ hoặc dùng làm danh hiệu, không rút ngắn hay kéo dài đồng hồ. Không thu phí mỗi phiên.

### C3 · Trẻ em và người gõ chậm bị bỏ khỏi công thức · lớn

- `03 §4.7` dùng T ≥ 2 + 120/E với **E sàn 25**. Bot Trẻ em của BALANCE gõ 15 WPM [repo: `BALANCE.md` §6], và cổng B3 đòi bot này thắng ≥ 85 % ở Thư giãn. Không tệp nào chạy bot Trẻ em: `01` thử 25/35/60/90, `02 E3` thử 25/35/60, `07` thử 25/35/60.
- `07 §4.3` tính rằng ở 25 WPM, chỉ hồi chiêu đã chiếm hết giờ ("kín giờ"). Vậy mọi chữ bắt buộc thêm vào (Ấn, Tẩy, Kết Ấn, Thu Hồn, chữ khai mạch, cứu đồng đội) đều lấy chỗ của kỹ năng. Trần chữ sống là 8 (`03`, `07`), 9 (`05 §6`), 10 nếu cộng chữ Linh Mạch của `04`. Trong khi đó, M0a của Rồng chỉ đo được 1–3 chữ cùng lúc trên trình duyệt [repo: gate r2 "Còn mở" 8].
- **Sửa:** E sàn 15 trong preset Thư giãn. Thêm bot Trẻ em và Chậm chắc vào mọi cổng. Thư giãn tối đa 5 chữ sống. Mọi chữ bắt buộc phải có một đường giải không cần gõ (né, nấp, cơ quan).

### C4 · Voice bị phạt sát thương · lớn

- `03 §4.4` bước 5: kênh nói "luôn ×1,00, không có Nhanh", nên mất ×1,10 của từ Chuẩn và mất Chớp. Theo phép tính trong `02 §4.3`, như vậy là mất khoảng 10–15 % sát thương. `02 §6` lại cho Voice một hồ sơ Hội tâm riêng, nhắm khoảng 30 %. Độ trễ cộng thêm cho Voice có 4 con số: +1,5 s (`01`), +0,6–1,0 s (`05`), +1,0 s (`07`), theo hồ sơ C riêng (`06`).
- `05 §6` hứa Voice ở M1, trong khi `shared/voice` còn "no production decoder" [repo: `shared/voice/README.md`].
- **Sửa:** chất lượng từ tính theo hồ sơ **của từng kênh**, có cùng tỉ lệ Chớp mục tiêu. Đo một bảng độ trễ cho mỗi kênh. Voice chỉ làm khi có bộ giải mã (`07`: M3). Không hứa Voice cho chế độ đội trước khi đo được.

### C5 · Cửa sổ báo đòn của Thú Vương mẫu sai theo chính công thức · lớn

- Ở `05 §4.5`, Thiết Bối Xung nạp **3 s** ở 35 WPM, giải bằng một từ Ấn D3. Công thức của chính `05 §6` cho từ 5 chữ: (0,4 + 0,5 + 12·6/(35·0,86) + 0,2) × 1,6 ≈ **5,6 s**. Công thức của `03` cho 5,4 s. Bảng của `07` cho 5,8 s ở 25 WPM. Đường giải bằng gõ không kịp, nên đòn này thực chất chỉ giải được bằng chân, trái cổng C4 "đứng trận chơi được" của `03`.
- **Sửa:** một công thức báo trước duy nhất trong canon. Thêm test dữ liệu: mọi đòn có đáp án gõ phải có thời gian nạp ≥ T(E_preset, kênh).

### C6 · Độ Kiếp và Tâm Ma · nhỏ

- Độ Kiếp (`01 §4.3`) đặt cổng cảnh giới lên **từ yếu nhất** của người học, dưới áp lực thời gian, và số tâm ma tăng theo Tâm Ma. Tâm Ma lại tăng vì nợ ôn tính trên **mọi game của portal** (`01 §4.7`). Một em chơi Space nhiều sẽ thấy Độ Kiếp khó hơn mà không hiểu vì sao.
- **Sửa:** từ yếu luôn hiện nghĩa và IPA. Tối đa 3–4 tâm ma. Tâm Ma chỉ tính nợ ôn của các từ học trong game này. Trước Độ Kiếp có gợi ý Ôn Tâm, không phạt.

## 6. Đội và Cloudflare Free

### D1 · Quyền sim và vị trí người chơi · **chặn**

- `04 §5`: "Durable Object của phòng chạy mô phỏng có seed và quyết mọi lần rơi đồ. Client chỉ vẽ." `06 §4.6`: máy chủ **không** chạy sim; loot quay cục bộ theo seed. `06` tính rằng nếu DO chạy sim thì chỉ được khoảng 7 trận/ngày (dùng alarm) hoặc 144 trận/ngày (dùng setInterval).
- `06 §4.6` chỉ dùng được với một ràng buộc: thú chỉ nhắm cổng, nhãn, bot và điểm khiêu khích; vị trí người thật không vào sim. Nhưng `05 §4.4–4.5` có Phong Lang "vồ qua người chặn", Hỏa Nha "quấy người chơi", Vồ Xé "vào người chơi gần nhất" và cú húc hất người trong vạch. `03 §4.2` cho quái va chạm với người, còn Kim Cương Thân "kéo quái nhỏ trong 6 m". Tất cả đều cần vị trí người chơi trong sim chung.
- `06` muốn solo dùng **cùng luật** để nội dung làm một lần dùng được cho cả hai chế độ. Vì vậy quyết định này chặn cả việc thiết kế quái solo ngay từ bây giờ.
- **Sửa:** chốt mô hình của `06`: relay lockstep, loot cục bộ, tiến trình cục bộ (đây là PvE, gian lận chỉ hại chính người gian lận). Mọi đòn của thú nhắm vào nhãn, cổng, điểm khiêu khích hoặc một vùng đất có báo trước. Còn việc "có trúng mình không" thì máy của người đó tự tính. Viết lại các thú T02, T03, V01 cho đúng luật này. Bỏ "server kết toán" của `04` khỏi M2.

### D2 · Hạn mức Free · lớn

- Theo trang giá, thời gian chạy không bị tính khi object rảnh và đủ điều kiện ngủ đông [web: https://developers.cloudflare.com/durable-objects/platform/pricing/]. Điều kiện là không có `setTimeout` hay `setInterval` nào đang chờ [web: https://developers.cloudflare.com/durable-objects/concepts/durable-object-lifecycle/]. Ước tính khoảng 200 request mỗi trận của `06` vì vậy đúng **chỉ khi DO hoàn toàn không có timer**.
- `05 §5` lại "gom 10 lần mỗi giây, gửi lại", tức cần timer. Khi đó DO thức suốt trận: 720 s × 0,125 GB ≈ 90 GB-s mỗi trận, tức khoảng 144 trận/ngày cho **cả tài khoản**, dùng chung với Space. Chính `06` cũng có timer ẩn: giữ ghế 10 s, nhắc AFK sau 45 s và 75 s.
- **Sửa:** DO không có timer. Rớt mạng bắt bằng sự kiện `webSocketClose`, đóng dấu tick rồi phát lại. Thời gian chờ 10 s và luật AFK chạy **trong sim tất định**, ví dụ bot nhận ghế ở tick T + 600. Heartbeat dùng tự trả lời ping của runtime. Cổng N4 đo cả GB-s trên Dashboard, không chỉ đếm request.

### D3 · Công bằng tốc độ trong đội · lớn

- **Nhịp k có 3 mô hình:** k theo từng cung hoặc ghế (`03 §5`, `06 §4.3`), k lấy trung vị đội, kẹp trong [0,85; 1,15] (`05 §5`), k theo tổng sức cả đội (`07 §5`). Với đội 2 người, trung vị chính là trung bình, nên người nhanh làm cả đội khó lên, trái [Codex §14.4].
- **Hợp kích:** `03 §5` cho "người đầu tiên gõ xong chốt cho cả đội", tức người nhanh luôn thắng cuộc đua. `05 §5` dùng 40 % + 20 % cho mỗi người gõ xong. `06 §4.1` để ghế Trận kích.
- **Vai có 4 trục:** trường phái (`03`), nhãn Công/Thủ/Dưỡng (`05`), vai ghế Công/Hộ/Trận/Ngự thú (`06`), hệ trong chuỗi sinh (`02 §5`). `06` nói vai Hộ và Trận hợp người gõ chậm, nhưng không MVP nào có lớp nhân vật làm được hai vai đó.
- **Sửa:** k theo ghế (`06`). Hợp Trận bất đồng bộ theo `05`. Một trục vai duy nhất: vai ghế gắn với một nhãn; trường phái cung cấp bộ chiêu cho vai; hệ **không** là vai. Có ít nhất một lớp Hộ hoặc Trận trước khi mở đội người thật.

### D4 · Thưởng đội và chat · nhỏ

- `06 §4.4` cho đội người thật +10 % thưởng. `04 §5` ghi "đội chỉ có thêm danh hiệu, ngoại trang". Một em học một mình, không có bạn chơi cùng, sẽ thiệt. `06 §6` mở chat ở nghỉ giữa đợt, trong khi `07 §5` ghi "MVP không có chat chữ".
- **Sửa:** thưởng đội chỉ là danh hiệu. Không có chat tự do ở v1, chỉ có câu soạn sẵn.

## 7. Sản xuất

### E1 · Tổng MVP vượt sức · lớn

- Mỗi tệp chỉ ước phần của mình. Cộng các MVP lại: 30 trận và 6 Thú Vương (`01`); 3 trường phái × (đánh nền + 4 chiêu + tuyệt kỹ + 2 tâm pháp), mỗi chiêu cần VFX và âm (`03`); vòng ngũ hành, ấn, phản ứng (`02`); Thư Lâu 10 bậc, Bảo Khí Lò, 8 đồ tiêu hao, pháp bảo 3 ô × 2 món × số trường phái (`04`); 10 đợt, 5 họ thú, 4 cơ quan (`05`); sim sẵn cho lockstep, ghế, bot (`06`). Riêng lát chơi của `07` đã cần 7–9 tuần với 4–6 làn agent song song và khoảng 13–20 giờ Tripo của chủ dự án.
- Cùng lúc đó, Rồng Giữ Ải đã có kế hoạch khoảng 216 model Tripo và khoảng 750 ảnh Codex [repo: `docs/games/dragon-lane/04-stages-maps-progression.md` dòng 18]. M0a của Rồng còn chờ anh chơi thử để chấm B9. Giờ của chủ dự án (Tripo, nghe âm, chơi thử) là nút thắt chung của mọi game.
- **Sửa:** MVP = lát của `07`: 1 ải, 6 đợt + Thú Vương, **1 trường phái** (Kiếm), solo + 1 bot, chỉ Typing, hộp xám trước. Ở MVP, hệ chỉ là biểu tượng điểm yếu của thú, chưa có ấn và phản ứng. Tĩnh Tu làm bản thử riêng cỡ S–M để đo giá trị học. Mọi phần khác ghi "sau" trong canon.

### E2 · Hình 3D runtime trái yêu cầu của chủ dự án · **chặn** (cho M0b)

- [Codex §0] liệt kê "Nhân vật, quái, map và kỹ năng dùng hướng 2D/sprite… Không mặc định runtime 3D cho đông quái" trong mục **yêu cầu hiện tại**. [Codex §0.1] ghi rằng "đã xác định" là hướng người dùng nêu. `07 §4.7` đề xuất phương án A (GLB chạy trên Three.js 3D). Trong khi đó `01 §7`, `04 §7` và `05 §7.1` đều giả định 2D.
- Lý lẽ của `07` có cơ sở: không có họa sĩ hoạt hình 2D, chủ dự án chê chuyển động cứng, và repo đã có sẵn instancing. Nhưng đám đông có xương **chưa đo** (M0a: "bench có xương vẫn chờ GLB" [repo: gate r2]).
- **Sửa:** hộp xám M0a không cần hình nên không bị chặn. Trước M0b, đưa anh **một** lựa chọn có bằng chứng: cùng một cảnh dựng theo A và B, có ảnh và đoạn chuyển động 10 s, có số bench 300 quái ở bậc Low. Ghi rõ rằng phương án A đổi một yêu cầu anh đã nêu. Không áp luật "làm theo đề xuất" cho điểm này.

### E3 · Luật âm thanh lệch nhau · nhỏ

- `01 §4.5` và `05 §4.5` ghi "chỉ dùng tiếng thu thật CC0". `07 §4.9` dùng thêm audio-lab Stable Audio 3, đúng với DECISIONS Q1 hiện hành (cho phép từ 23/10, có Bảng Nghe). **Sửa:** canon dẫn tới `tools/audio-lab/DECISIONS.md` Q1 và Q6, không chép lại luật.

## 8. Trùng Rồng Giữ Ải

### F1 · Trùng khung và chép sim đang trượt cổng · lớn

- Phần ngoài trận gần như đổi tên một-một: Linh Sa / Văn Khí / Thú Hạch = Vàng / Tri Thức / Vảy Rồng (`04 §1`); Thư Lâu = Thư Viện; Cơ Duyên = Long Ấn; Hung Cát = Lời Thề; Huyết Phù / Giáp Phù = Tim Rồng / Vảy Cứng; Ngọc Bội = Ngọc Chữ; cơ quan = bẫy; Trận Phường = cửa hàng giữa đợt. Học trước, Thẻ Ôn, Sổ Từ cũng giống hệt. Portal sẽ có hai game "giữ ải theo đợt + cửa hàng + bẫy + ba tiền", cộng Lời Gọi và Tuyến Cuối cũng là thủ.
- M0a của Rồng còn trượt B1 và B7 vì Nhàn I (bot Chuẩn 20,5 %, bot Nhanh 35,7 %). Typing ở đó gây 54,1 % sát thương, dưới mức 65–80 % mà DESIGN đặt ra [repo: gate r2, "Cần anh quyết" 1–2]. Thiết kế tu tiên thêm đánh nền, cơ quan và Hợp Trận, lại bỏ chữ trên quái thường, nên tỉ lệ gõ ≥ 55–60 % càng khó đạt.
- `05 §4.7` nói "ô luôn có từ" là cách **sửa** Nhàn I. Thật ra đó chỉ là **đổi thước đo**: thời gian nhàn biến thành thời gian gõ lặp từ 3–5 chữ đã thuộc ở ô liên tục. `07 §4.3` tính người 60 WPM dư khoảng 23 từ mỗi phút cho việc này.
- **Sửa:** (1) ghi rõ trong canon ba điểm khác Rồng: nhân vật tự đi, gõ trên thanh kỹ năng, chơi đội; ngoài ba điểm đó thì chép luật của Rồng, có header `// Source:`, không thiết kế lại. (2) Không chép `director`, `pace` và `waves` trước khi Rồng chốt cách sửa Nhàn I; hoặc chép kèm một vé nợ đồng bộ. (3) Định nghĩa lại I cho game có thanh kỹ năng, ví dụ "nhàn quyết định": chỉ còn ô liên tục dùng được và không có đích ưu tiên. Thêm cổng "ô liên tục ≤ 30 % sát thương gõ". (4) Tuyến Cuối đã có mô hình nạp băng; ô liên tục chép từ đó, ghi nguồn.

## 9. Phần còn thiếu

### G1 · Onboarding · lớn

- Không tệp nào mô tả 10 phút đầu. Nếu cộng lại, người mới phải qua: chọn 3 Mệnh cách và linh căn (`02`), chọn trường phái, chọn Khí Vận (`01`), Học trước (`04`, `05`), Hành Nang (`04`), và còn phải hiểu Trận Lực, Kết Giới, nhãn, Trận Ý. Hồ sơ gõ ban đầu (`SkillProfile`) chưa có dữ liệu, nhưng k, độ dài từ và ngưỡng Chớp đều dựa vào nó.
- **Sửa:** trận đầu bắt đầu trong ≤ 60 s, không có lựa chọn build. 3 trận dạy (`05 §4.9`), mỗi trận một ý mới. Đợt đầu dùng để đo tốc gõ. Mọi lựa chọn build mở dần từ trận 4.

### G2 · IME tiếng Việt, phím tắt, tiếp cận · lớn

- Không tệp nào nhắc **bộ gõ tiếng Việt** (Unikey, EVKey ở chế độ Telex hay VNI). Đây là lỗi thường gặp nhất với người chơi Việt Nam. Kit đã có xử lý composition [repo: `shared/game-kit/typing/session.ts`, `config.ts`, `input/keys.ts`] và repo có skill `typing-input-ime`.
- **Phím va chạm:** Alt+1/2/3 cho đan (`03`, `04`) gõ ra ký tự đặc biệt khi bấm Option+số trên Mac, và đổi tab trong Chrome trên Linux. F1–F6 cho truyền âm (`06`), mà F1 mở trợ giúp của trình duyệt. Tab dùng để bật WASD nhưng cũng chuyển focus. Esc vừa nhả khóa chữ (kit) vừa mở menu dừng.
- **Tiếp cận:** không ai nhắc giảm chuyển động (máy chủ dự án đang bật reduced-motion). Lôi Kiếp có sét chớp, cần kiểm nhấp nháy. Ấn Nghe cần phụ đề. Chỉ có `02` nhắc tới mù màu.
- **Sửa:** dò IME khi vào trận và báo rõ cách tắt. Đan dùng phím số **không kèm phím phụ**, vì từ chỉ gồm a–z. Theo `prefers-reduced-motion`. Trần chớp sáng. Mọi tín hiệu âm có kèm hình.

### G3 · Preset, độ dài phiên, đối tượng · lớn

- BALANCE dùng các mức Thư giãn / Cân bằng / Thử thách / Học. Tĩnh tọa dùng Làm quen / Tiêu chuẩn / Thử thách (`01`). Nghỉ đợt dùng Dễ / Thường / Khó (`04`).
- Một lượt Thú Triều dài 35–45 phút (`01 §4.1`), trong khi `04 §4.10` nhắc nghỉ sau 30 phút (20 phút với trẻ em). Đại Triều 10 đợt dài khoảng 12 phút ở 35 WPM, và khoảng 15 phút ở 25 WPM vì k giãn đợt (`05 §4.8`).
- Chưa ai xác định đối tượng chính: trẻ em hay thiếu niên. Chủ đề tâm ma, độ kiếp, sét đánh cần kiểm giọng điệu cho hồ sơ trẻ em.
- **Sửa:** dùng đúng tên preset của BALANCE. Trận ≤ 7 phút ở Thư giãn. Lưu ở mỗi trận. Không có phiên bắt buộc dài hơn mốc nhắc nghỉ.

### G4 · Lưu và cầu học · lớn

- `01 §5` lưu cục bộ, sau này đồng bộ qua Worker tài khoản (D1). `04 §7` dùng giao dịch ví của Space. `06` Q3 dùng danh tính khách và Worker riêng `tu-tien-coop`. Ngộ tính (N70) và nợ ôn cần lõi học chung, nhưng mỗi game chạy trên một host riêng (`dragon.`, `td.`, `survival.` [repo: SPLIT_PLAN §1]) và chỉ đọc được lõi học qua cầu của portal. Chạy riêng ở cổng 3008 thì Ngộ tính đứng yên ở 50.
- **Sửa:** v1 lưu cục bộ, có số phiên bản bản lưu và đường chuyển đổi. Mọi phần thưởng từ học phải chạy được khi không có portal (dùng dữ liệu cục bộ của game). Đăng ký `gameId` và origin trong `games.json` ngay ở bước dựng khung.

### G5 · Cố tình gõ chậm · nhỏ

- Nhịp k theo ghế (`06`) và ngưỡng Chớp theo nhịp riêng (`02`) đều đọc từ hồ sơ. Người chơi có thể cố tình gõ chậm vài trận để hạ kỳ vọng, rồi được thú sinh thưa hơn và Chớp nhiều hơn.
- **Sửa:** hồ sơ dùng phân vị bền trên nhiều phiên, có trần đổi mỗi phiên, và ngưỡng Chớp có sàn. Bảng xếp hạng tắt bộ điều nhịp (đã có trong BALANCE §4.2).

## 10. Việc cần làm trước khi viết mã

1. Viết `docs/games/tu-tien/00-canon.md`: từ điển thuật ngữ, bảng số, vòng chơi (chương = 1 ải), MVP = lát một trường phái, lộ trình mốc duy nhất. Mọi tệp `01`–`07` trỏ về đây khi có mâu thuẫn.
2. Chốt luật học C1 (ngân sách từ mới theo phiên, ô gấp chỉ dùng từ đã thuộc) và C5 (một công thức báo trước, có test dữ liệu).
3. Chốt D1 và D2: relay không timer; thú không nhắm vị trí người thật; viết lại T02, T03, V01.
4. Hỏi anh E2 bằng ảnh và số bench, không tự quyết.
5. Chờ Rồng chốt cách sửa Nhàn I, hoặc ghi vé nợ đồng bộ, trước khi chép `director`, `pace`, `waves`.

**Câu hỏi cho chủ dự án** (anh không trả lời thì làm theo đề xuất, trừ câu 1):

| # | Câu hỏi | Đề xuất |
|---|---|---|
| 1 | Giữ 2D/sprite như yêu cầu ở Codex §0, hay đổi sang "nhìn 2D, chạy 3D GLB"? | Quyết sau buổi A/B có bench; trước đó chỉ làm hộp xám |
| 2 | Tu tiên là game thứ năm (repo riêng) hay chờ Rồng qua cổng M0a? | Viết canon và làm bản thử Tĩnh Tu ngay; khung repo và sim chờ Rồng chốt cách sửa Nhàn I |
| 3 | Đối tượng chính: trẻ em hay thiếu niên trở lên? | Thiếu niên trở lên là mặc định; hồ sơ trẻ em dùng Thư giãn, không chat, giọng điệu nhẹ |
| 4 | Gộp Độ Kiếp vào Thú Vương cuối chương? | Có |
| 5 | Thú không đuổi người thật, để chơi đội được trên gói Free? | Có |
