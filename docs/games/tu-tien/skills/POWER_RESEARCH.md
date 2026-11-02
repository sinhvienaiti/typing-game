# Nghiên cứu "uy lực" của chiêu (03/11/2026)

Lý do: anh chấm lab chiêu khoảng 6/10 (canon D58): chiêu phải chờ gồng, không có hiệu ứng màn hình, thiếu sự khủng bố của tu tiên, ít chiêu diện rộng, không có số sát thương, quái không phản ứng, không có âm thanh và tiếng hô.

- **Câu hỏi gửi ChatGPT** (Chat, thinking High, làm 5 phút 36 giây, có tra web): https://chatgpt.com/c/6ae8d7a8-cdfc-83ec-9522-f7cde2543fc9
- **Bản trả lời gốc** (tiếng Anh, có link nguồn): [`source/power-research-chatgpt-2026-11-03.md`](source/power-research-chatgpt-2026-11-03.md)
- **Tình trạng nguồn:** Claude chưa mở lại từng link. Số liệu của các game (khựng đòn của Street Fighter V, rung của GDC, số gộp của ZZZ) chỉ dùng làm điểm xuất phát, sẽ chỉnh trong lab.

## Điều rút ra từ nghiên cứu

1. **Chiêu cả sân phải có bốn trạng thái đọc được:** trời đổi, kiếm tụ, kiếm chọn từng con mồi, một nhát kết. Người chơi phải nhìn một con thú mà hiểu "sáu thanh kia đã chọn con này".
   - Học từ Tale of Immortal (mưa kiếm lớn dần), NARAKA (kiếm bay ưu tiên các mục tiêu khác nhau), Hàn Lập điều 72 thanh Thanh Trúc Phong Vân Kiếm, và Vampire Survivors (thấy từng con bị săn trước, rồi mới quét cả màn).
2. **Rung theo "trauma":** cường độ = trauma² dùng nhiễu mượt, không rung ngẫu nhiên. Khựng đòn chia bậc theo cỡ đòn. Đòn thường gần như không khựng, để dòng gõ không bị gãy.
   - Monster Hunter là lời cảnh báo: khựng quá mạnh thì người chơi kêu vướng, bỏ hẳn thì kêu đòn nhẹ bẫng.
3. **Thế giới phản ứng nhiều hơn camera.** Nên làm tối thế giới, chớp sáng ngắn, đổi bóng dáng của thú. Mờ toàn màn hình và cảnh cận che sân thì rất hạn chế.
   - Genshin và HSR bị chê vì cảnh cận và chớp sáng lặp lại gây mỏi mắt. Nên có thanh chỉnh độ rung và chớp (hướng dẫn trợ năng của Microsoft).
4. **Phản ứng của thú phải đổi bóng dáng**, không chỉ đổi lớp da: lóe viền 2–4 khung, vệt chém theo hướng, giật lùi nhẹ, rồi biến hình rõ khi chết.
   - Chỉ tinh anh mới bị choáng hoặc cắm kiếm. Thú Vương không bao giờ bị đẩy, chỉ giật thân trên.
   - Lấy từ DMC5: đòn thứ hai không khởi động lại phản ứng đang chạy.
5. **Số sát thương gộp theo đòn, không theo từng va chạm.**
   - Gộp mỗi mục tiêu trong 100–150 ms ("12.8K × 6"). Từ 5 thú trở lên trúng cùng lúc thì hiện một số tổng ở giữa cụm.
   - Chí mạng to 120–135 %. Số không được đè lên nhãn chữ.
   - Học cách gộp sát thương của ZZZ và số rút gọn của Diablo IV và Lost Ark.
6. **Tiếng hô ngắn thắng câu dài:** mỗi chiêu hay dùng cần 3 bản thu để khỏi nhàm. Âm thanh chia lớp: gọi, bay, chạm theo chất (thịt, đá, linh), chết. Tuyệt kỹ thêm lớp "thế giới đổi": nhạc lùi, lặng 40–60 ms trước nhát cuối, tiếng chuông dài.
   - Không phát 500 tiếng kiếm riêng. Gộp va chạm theo khoảng 30–50 ms, và chỉ 8–12 thanh gần người chơi có tiếng vụt qua.
7. **Nhãn chữ là lớp riêng sau hậu kỳ:** không nhận bloom, mờ, tách màu, đổi phơi sáng hay chớp. Viền tối 2–3 px, nền tối 65–85 %. VFX dưới nhãn giảm 40–60 %.

## Hướng ChatGPT đề xuất và cách ta dùng

ChatGPT đưa ba hướng:
- **A, Thiên Hà Kiếm Lưu** (sông kiếm trên trời): thanh thoát, đậm chất tiên hiệp.
- **B, Liệp Sát Kiếm Trận** (trận săn đen đỏ): đáng sợ, nhưng nghiêng về ma đạo.
- **C, Tinh Hà Kiếm Vực** (chòm sao): rực rỡ, nhưng dễ ra kiểu gacha chung chung.

ChatGPT chọn **A, lấy thêm phản ứng thú dữ dội của B và cách gộp số của C**.

Claude theo hướng đó, với hai chỗ sửa theo anh:
- **Cảnh cận cho tuyệt kỹ** là cảnh cận thật, khoảng 1 s, dừng game lẫn giờ gõ (D58). ChatGPT khuyên chỉ có băng chữ ngắn.
- **Hiệu ứng màn hình mạnh hơn bảng của ChatGPT**, vì anh chê "không hề có hiệu ứng màn ảnh". Lấy mức giữa A và B, rồi chỉnh theo khung ảnh và ý anh.

| Bậc | Rung | Khựng | Chậm | Tối / chớp | Cảnh cận |
|---|---|---|---|---|---|
| Đánh thường | 3 px, tắt trong 90 ms | 14 ms, chỉ con thú trúng đòn | không | không chớp toàn màn; chớp tại chỗ trúng α 0,4 trong 70 ms, bán kính 130 px | không |
| Chiêu | 7 px, 200 ms; đẩy zoom 1,5 % ở nhát kết | 50 ms ở đòn chính, 67 ms ở nhát kết | 0,6× trong 140 ms ở nhát kết | lúc ra chiêu đèn thế giới giảm 22 % trong 300 ms (Ngự Kiếm Quyết thì không); chớp tại chỗ α 0,42, bán kính 190 px; nhát kết: chớp toàn màn α 0,3 trong 3 khung, mờ tỏa tâm 80 ms, viền màu 6 px | không |
| Tuyệt kỹ và chiêu cả sân | 16 px + nghiêng ≤ 0,35°, 350 ms; đẩy zoom 4 % | 50 ms mỗi đợt, 100 ms ở cao trào | 0,3× trong 280 ms | suốt chiêu (tuyệt kỹ: từ lúc vào cảnh cận) đèn thế giới còn 55 %, thế giới mất 60 % màu, viền tối quanh khung: độ sáng trung bình của sân giảm 35–50 %; cao trào: chớp α 0,42 trong 3 khung rồi trả nhanh về khung tối, mờ tỏa tâm 80 ms, viền màu 12 px | có, khoảng 1 s, dừng game và giờ gõ |

Sửa ở lượt 2 (03/11): hai giám khảo mù không thấy màn hình phản ứng ở tốc độ thật (độ sáng sân chỉ giảm từ 66 xuống 62, nhát kết thành sương sữa, đòn thường và Ngự Kiếm Quyết nhuộm xanh cả màn như bộ lọc), nên rung và khựng gần gấp đôi, tối bằng cách hạ đèn thế giới (VFX giữ nguyên độ sáng), chớp toàn màn chỉ ở nhát kết.

**Chiêu cả sân mẫu: Vạn Kiếm Triều Tông** (萬劍朝宗, Ten-Thousand Sword Convergence), dựng làm mẫu trong lab. Tên và ô chốt theo danh mục chiêu mới.

| Thời điểm | Diễn biến |
|---|---|
| F0, phím cuối | 8 kiếm thật rời tay ngay tới thú gần |
| F1–20 | Thế giới tối dần (lượt 2: đèn thế giới còn 55 %, độ sáng sân giảm khoảng 45 %, lượt 1 chỉ 8 % nên không thấy); một vệt sông kiếm hiện chéo trên trời |
| F4–30 | 64 hạt kiếm bay lên; sông kiếm phủ gần 40 m, 320 kiếm ở High |
| F30–168 | Săn: mỗi 100 ms có 24–36 kiếm tách ra lao xuống. Kiếm được tái dùng nên thấy được 700–900 nhát |
| F168–192 | Kiếm còn lại bay lên, xoắn một vòng, xếp thành một nét chéo khổng lồ |
| F192 | Nhát kết quét cả sân. Sông kiếm thu về một điểm trên đầu anh hùng, kèm một tiếng chuông ngọc trầm |

Chọn mục tiêu có giữ chỗ:
- **Điểm ưu tiên** = mối nguy với cổng × 2 + tinh anh × 1,5 + độ gần × 0,8 + máu thấp × 0,5 − số kiếm đã giữ.
- **Số kiếm giữ mỗi con:** thú thường 2, tinh anh 4–6, Thú Vương 8–12.
- **Đổi mục tiêu:** con chết thì kiếm đổi đích ở tick sau; 15–20 % số kiếm cố ý chọn con khác gần đó.

## Việc tiếp theo

- **Dựng lớp uy lực dùng chung trong lab** (bất kể danh mục chiêu mới ra sao):
  - hiệu ứng màn hình theo bậc, cảnh cận tuyệt kỹ, phản ứng và cái chết của thú;
  - số sát thương gộp, ra chiêu tức thì;
  - móc âm theo sự kiện, mẫu Vạn Kiếm Triều Tông.
- **Danh mục chiêu mới:** nghiên cứu nguồn Trung Quốc song song ở ChatGPT và Gemini (Argon), xem [`SKILL_CATALOG_V2_RESEARCH.md`](SKILL_CATALOG_V2_RESEARCH.md) khi xong.
- **Âm thanh** (tiếng hiệu ứng và tiếng hô tiếng Trung) tạo trong Firefly, theo [`WEAPON_AUDIO.md`](WEAPON_AUDIO.md) và D58.

## Kết quả lượt 1 (03/11, khoảng 03:15)

Lượt 1 có 12 commit dựng (`3cd207d`…`193f15a`), changelog ở `docs/changelog/2026-11-03-lab-power-pass.md` của repo game. Sau đó một agent soát đối kháng tìm ra 7 lỗi thật và sửa cả 7 (`c05eea4`…`662eaa2`):
- NaN vào bloom ở Ultra;
- một đòn cũ giữ đòn mới thành 83 ms;
- bộ điều chỉnh độ phân giải hạ nhầm;
- nhát kết vượt bảng bậc;
- rung và tách màu sai tỉ lệ theo độ cao màn hình;
- kiếm xoay phụ thuộc tốc độ khung;
- tạo chuỗi mỗi đòn.

Đo lại: phím tới đòn 33 ms; High p95 phím 7 là 8,4 ms, K5 là 9,7 ms.

**Hai giám khảo mù: 5,8 và 5,5** (trần 8,5). Hai người cùng thấy:
- ở cận cảnh, tuyệt kỹ và chiêu cả sân ra khỏi khung;
- màn hình tối chưa đủ (độ sáng chỉ giảm từ 66 xuống 62), nhát kết là sương sữa;
- kiếm phím 7 thành "đống que sáng" một màu, không có thanh chủ;
- quái phản ứng ít, sau chiêu xoáy còn đứng trắng bệch như lỗi;
- số sát thương nhiều và rối, có số ra ngoài sân;
- cảnh cận đứng im như băng quảng cáo, tranh tả thực không khớp nhân vật tạm trên sân, chữ Hán đứng trước tên tiếng Anh.

**Lượt 2** (workflow `wf_38571378-1ef`) sửa đúng các điểm này, rồi soát đối kháng và cho hai giám khảo mới chấm. Theo luật ba lần thử: nếu tới lượt 3 vẫn không tăng rõ, Claude bàn hướng khác với ChatGPT trước lượt 4.
