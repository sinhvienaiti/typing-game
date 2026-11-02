# Vũ khí: nghiên cứu và thiết kế (02/11/2026)

Chủ dự án, 02/11:
- Thanh kiếm trong 7 tranh hướng v1 "quá xấu, quá mức cơ bản, không có gì nổi bật".
- "mỗi khi thiết kế một thứ gì, bạn nên kêu chatgpt tham khảo các mẫu được nhiều người yêu thích… tránh copy nhưng phải có nét đẹp riêng".
- "hình ảnh, hiệu ứng, âm thanh, vfx, đều phải gửi tôi mẫu để tôi review".
- "chúng ta nên vẽ nhiều loại kiếm… khi thi triển, vũ khí sẽ là thứ phản ánh của kỹ năng… không chỉ tạo ra 1 cái kiếm, mà là nhiều loại vũ khí".

Nguồn: chat ChatGPT "Nghiên cứu thiết kế chiêu thức" (Chat mode, High), cùng chat với `CHATGPT_SKILL_RESEARCH.md`.

## 1. Nguyên tắc: vũ khí phản ánh chiêu

- Kiếm quang, đao quang, thương ảnh của mọi chiêu là bản sao của **chính món đang trang bị**: cùng bóng dáng, cùng rãnh sáng, màu nhấn theo hệ của món, tiếng riêng.
- Đổi vũ khí là đổi diện mạo và âm của cả bộ chiêu. Canon §14.5 đã cho pháp bảo đổi màu VFX và tiếng; ở đây mở rộng sang hình.
- Mỗi món thiết kế ba cấp ngay từ đầu: **hero** (đủ chi tiết, cận cảnh), **combat** 25–60 px (bóng dáng, hộ thủ chữ ký, một rãnh, đốc), **bản sao** ×150–500 (bóng lưỡi, một hình chuôi, một sống sáng, tách sáng tối). Nếu bản sao không còn nhận ra món gốc thì thiết kế gốc dựa quá nhiều vào chi tiết nhỏ.
- Trong code: `BladeSet` (lab) lấy geometry và màu nhấn từ món đang cầm, thay cho thanh jian tạm `jianGeometry()`.

## 2. Nghiên cứu kiếm (ChatGPT, có nguồn; Claude kiểm lại một phần)

Mười thanh ChatGPT chọn, mỗi thanh một bài học:

| Thanh | Nguồn | Bài học |
|---|---|---|
| Primordial Jade Cutter (Genshin, Liyue) | HoYoWiki; Claude kiểm: "ceremonial sword carved from pure jade" khớp | Một vật liệu kể cả câu chuyện; không chép lưỡi ngọc nguyên khối |
| Summit Shaper (Genshin) | HoYoWiki | Nhận diện bằng hình học: một hình chữ ký ở hộ thủ, một đường sáng trên lưỡi |
| Trấn Yêu Kiếm (Tiên Kiếm 3) | Baidu, mẫu 1:1 chính thức | Tiên kiếm không cần hộ thủ khổng lồ; sang nhờ tỷ lệ thanh thoát |
| Ma Kiếm (Tiên Kiếm 3) | Baidu | Chữ ký phải có ngay từ bóng dáng |
| Vọng Thư Kiếm (Tiên Kiếm 4) | Baidu, moegirl | Một câu thiết kế lạnh như trăng; Claude xác nhận vật liệu, **chưa xác nhận** chi tiết "không hộ thủ" |
| Thanh Trúc Phong Vân Kiếm (Phàm Nhân Tu Tiên) | Baidu, nhiều nguồn; Claude kiểm: 72 thanh, Kim Lôi Trúc, bản mệnh pháp bảo khớp | Một kiếm thành nhiều kiếm thành kiếm trận: đúng bài toán của ta |
| Thiên Gia (Tru Tiên) | Baidu Baike | Vũ khí là bản sắc của người cầm |
| Tru Tiên Cổ Kiếm (Tru Tiên) | Baidu Baike | Sang không phải là nhiều hoa văn |
| Thất Sát Kiếm (Đấu La) | Baidu | Ở 40 px, vài dấu sao lớn hơn năm mươi nét khắc |
| Đại La Kiếm Thai (Hoàn Mỹ Thế Giới) | Baidu | Chữ ký có thể nằm trên mặt lưỡi |

Tám nguyên tắc rút ra:
1. Một câu bóng dáng duy nhất.
2. Một vật liệu chủ (Thanh Phong: bạc lạnh), các vật liệu khác làm phụ.
3. Hộ thủ đọc được từ trên xuống, rộng 2–3 lần bản lưỡi, hình mây như ý, vòng ngọc, vai kiếm; không cánh chim hay sừng kiểu phương Tây.
4. Họa tiết quan trọng nằm trên mặt hướng lên camera.
5. VFX neo vào hình: rãnh có sẵn sáng lên, ánh sáng chạy trong rãnh, vệt sáng thoát từ rãnh.
6. Ba cấp chi tiết từ đầu (mục 1).
7. Kiếm tuệ là điểm nhấn chuyển động: hero có, 3 kiếm ngắn lại, 6 kiếm giảm mạnh, 150–500 bỏ.
8. Hoàng tộc đến từ tỷ lệ và tay nghề, không đến từ vàng (vàng kim là màu tiền).

## 3. Ba hướng Thanh Phong

| Hướng | Bóng dáng | Ghi chú |
|---|---|---|
| H1 Hạc Vân Miện | Hộ thủ cánh hạc rất rộng, đốc vòng ngọc bích, kiếm tuệ ngà và chàm | Đã vẽ (`art-src/weapons/` khi chép về). ChatGPT tự chấm chất cổ phong 6,5: cánh quá giống kiếm thiên thần phương Tây. Nếu giữ: thu hộ thủ 25–35 %, thành vai mây, một viên ngọc |
| H2 Bích Hoàn | Lưỡi bạc thẳng xuyên giữa một vòng ngọc bích dẹt có hai khuyết mây; đốc giọt ngọc; hai rãnh gió nhập lại ở mũi | ChatGPT đề xuất. Ở 25 px vòng ngọc vẫn đọc được; tốt nhất cho bầy 500 kiếm |
| H3 Vô Ngạc Lưu Vân | Gần như không hộ thủ, hai vai mây thấp, như một cây trâm ngọc dài | Nhẹ nhất cho bầy; gần Vọng Thư về nguyên lý nên phải khác về hình và màu |

Hình nhỏ ở góc tranh H1 không phải góc 55° từ trên xuống. Từ tranh sau, mỗi tấm có một hàng nhìn từ trên xuống 55° và một hàng thumbnail 40 px.

## 4. Nghiên cứu Đao và Thương (ChatGPT, có nguồn)

- **Đao:** Ẩm Tuyết Đao (Phong Vân), Viên Nguyệt Loan Đao (Cổ Long), Hổ Phách (Thần Binh Huyền Kỳ), Đồ Long Đao (Ỷ Thiên Đồ Long Ký), Cát Lộc Đao (Tiêu Thập Nhất Lang), Kinh Tịch, Thiên Nhận (Phong Vân).
- **Thương:** Hỏa Tiêm Thương (Phong Thần), Bạch Ngân Long Thương (Đấu La III), Bá Vương Thương (Thất Chủng Vũ Khí), Lượng Ngân Thương (truyền thống Triệu Vân), Trượng Bát Xà Mâu, Vortex Vanquisher, Calamity Queller, Primordial Jade Winged-Spear (Genshin).
- ChatGPT tự ghi rõ cái nào kiểm trên trang, cái nào là quan sát tranh chuyển thể. "Được yêu thích nhất" không có bảng xếp hạng chung đáng tin; danh sách là các thiết kế biểu tượng.

## 5. Ngôn ngữ chung của bộ

- **Vật liệu:** thép satin bạc lạnh (không gương chrome, không bẩn kiểu trung cổ), 5–15 % ngà sứ ở cổ, vai, hộ thủ, ngọc chỉ là một điểm nhấn (vòng, hạt, ấn), lụa chàm ở chuôi.
- **Rãnh sáng là hình thật trên model**, không phải vẽ emissive tùy ý. Kiếm: 1–2 rãnh dọc mặt lưỡi hướng lên camera. Đao: một rãnh rộng lệch về sống. Thương: một rãnh trên mũi và một nút ở cổ nối cán.
- **Hệ chỉ nằm trong rãnh**, một hai điểm khảm, vệt và lớp tiếng; vũ khí phải đẹp khi tắt VFX. Màu nhấn dùng đúng mã trong `SKILL_CATALOG.md` §1.
- **Sang nhờ tay nghề:** tỷ lệ thanh, chỗ chuyển tiếp gia công kỹ, khuyết mây, ngọc bích, ấn ở cổ, khảm ngà. Không cánh lớn, không vàng kiểu baroque, không chùm đá quý, không chữ Hán.
- **Tiếng ba lớp:** lớp họ (kiếm "shing" cao, đao "whum" trầm, thương "thuk" gọn), lớp món (ví dụ tiếng ngọc nhỏ của Clear Wind), lớp hệ. Đổi món phải đổi ít nhất lớp món và hình vệt.
- **Chiêu nhân bản món đang cầm:** Phi Kiếm là chính món; Ngự Kiếm 3 bản; Lạc Kiếm Trận 6; Thiên Hà Kiếm Vũ 150–500 bản giản lược. Đao quang giữ độ cong, sống, mũi, khuyết và rãnh; thương ảnh giữ mũi, cổ, rãnh và một đoạn cán.

## 6. Đợt 1: 10 món

Tên tiếng Anh là tên người chơi đọc; tên Hán Việt chỉ để ghi chú.

| Món | Hệ | Dấu nhận diện ở 40 px | Chiêu phản ánh |
|---|---|---|---|
| Clear Wind (Thanh Phong), kiếm chữ ký | Kim | Lưỡi thẳng xuyên vòng ngọc bích rỗng | Mọi kiếm quang có vòng O và hai rãnh nhập một ở mũi; tiếng thép kèm tiếng ngọc |
| Winter Vein (Hàn Mạch) | Băng | Hai vai lục giác thấp như mảng băng chẻ | Rãnh tách ba vết rạn gần mũi; trúng để lại vết nứt ngắn |
| Thunder Seal (Lôi Ấn) | Lôi | Hộ thủ chữ X bẹt và một ấn hình thoi | Nút X chớp theo nhịp; ba tiếng điện khác nhau khi ba kiếm bay |
| Verdant Branch (Bích Chi) | Mộc | Lưỡi hình lá, hộ thủ chữ Y lệch | Bầy kiếm như đàn lá kim loại; vệt đôi khi rẽ nhánh |
| Ember Crest (Diệm Phong), đao | Hỏa | Đao bản vừa, một gai lửa ở sống | Đao quang có gai lửa ở sống, vệt cam đỏ |
| Mountain Verdict (Trấn Nhạc), đao | Thổ | Đao nặng, sống ba bậc như sườn núi | Đao quang thành khối ép dày ba bậc, tiếng đá dưới tiếng thép |
| Tidal Crescent (Triều Nguyệt), đao | Thủy | Đao dài cong nông, không quá 20° | Cung nước nông dài, không thành vòng trăng |
| Sky Thread (Thiên Ty), thương | Phong | Mũi lá dài có khe giọt nước rỗng | Thương ảnh giữ khe giọt nước, vệt gió mảnh |
| Resonant Fang (Ngân Minh), thương | Kim | Mũi thoi dài, cổ bát giác rỗng | Mỗi lần trúng một tiếng kim loại ngân |
| Storm Pin (Lôi Châm), thương | Lôi | Mũi rất dài có khe sét một nét | Hàng loạt châm thương có tia ziczac ở lõi |

Rủi ro gần thiết kế có sẵn (ChatGPT tự review, Claude đồng ý): Thunder Seal với bộ Geo của Genshin nếu hộ thủ thành khối to; Mountain Verdict với Đồ Long Đao nếu đen và thô; Tidal Crescent với Viên Nguyệt Loan Đao nếu cong quá; Sky Thread với Primordial Jade Winged-Spear nếu hai vây nở thành cánh. Mỗi rủi ro có luật cứng trong bản vẽ.

Mỗi họ vẽ một tấm (hàng anh hùng ba phần tư, hàng cùng món ở góc 55° từ trên, Claude tự thu 40 px xám để kiểm), gửi chủ dự án duyệt, chấm mù hai giám khảo ở 8,5.

## 7. Câu hỏi canon (chờ chủ dự án)

- Canon §14.5 và D32 hiện chỉ có **một ô Pháp Bảo Bản Mệnh, món cố định**, không độ hiếm; D05 giới hạn 4 hệ lâu dài.
- Đề xuất của Claude: vũ khí nằm trong chính ô đó, nên không thêm hệ mới. Người chơi có nhiều món mỗi họ và chọn một món trước trận. Chỉ số giữ trong dải của pháp bảo hiện tại và trần 25 % (§14.6). Khác biệt chủ yếu là hình, màu, tiếng và hệ.
- Cách có vũ khí, số món ở MVP, hệ của món có đổi hệ sát thương hay không (D23 hiện: hệ người chơi = hệ trường phái) để chủ dự án chốt.
