# TU TIÊN TYPING — COMBAT, TỔ ĐỘI, TU LUYỆN VÀ CÂN BẰNG

**V2.2 · cập nhật 24/10/2026 · Di chuyển chuột/phím, đứng trận tùy chọn, Typing–Voice–Hybrid và đồ họa 2D có chiều sâu. Thiết kế đề xuất, chưa phải game đã triển khai.**

Tài liệu này bổ sung nghiên cứu Tale of Immortal và thay thế những đề xuất combat cũ mâu thuẫn với yêu cầu mới. V2.2 xác định di chuyển tự do và đồ họa 2D có chiều sâu là nền: dùng chuột hoặc phím trong và ngoài trận, đứng trận hoặc di chuyển tùy lựa chọn. Các nội dung khác gồm 5 cơ chế/phụ bản bổ sung để lựa chọn; solo–buff–pet–đội–bot; sức mạnh đầu/giữa/cuối; tu luyện chọn chữ; tự review và kiểm chứng.

**Ưu tiên khi có mâu thuẫn:** yêu cầu V2.2 về di chuyển, voice, lựa chọn đứng trận và hình ảnh 2D có hiệu lực trước những câu giới hạn di chuyển ở bản V2, master plan hoặc báo cáo cũ. Năm phương án phụ không phải điều kiện để được đi lại trong combat.

## 0. Những yêu cầu hiện tại

- Game học tiếng Anh, hỗ trợ Typing, Voice và Hybrid. Người chơi di chuyển tự do bằng bàn phím hoặc chuột, cả trong lẫn ngoài chiến đấu.
- Ô kỹ năng lớn, hiện từ tiếng Anh. Hoàn thành từ bằng kênh đang chọn kích hoạt đúng kỹ năng đó; nhận giọng nói cần luật xác nhận và độ trễ được kiểm riêng.
- Kỹ năng có cooldown; luôn có một hành động phù hợp vai trò để tiếp tục gõ.
- Có công kích nền tự động. Buff có thể cường hóa bản thân hoặc đồng đội; pet tự đánh và nhận lệnh.
- Có solo thuần, một người cùng bot, nhiều người và bot bù vị trí.
- Ưu tiên trận pháp 2–3 người; đại trận như Thất Tinh có 7 vị trí.
- Thủ hộ trận chống thú triều là một hoạt động. Ở trong trận có lợi thế, đi ra ngoài để đánh/chọn góc/nhặt đồ/khám phá cũng có giá trị; không bắt đứng cố định toàn trận.
- Nhân vật cận chiến/tầm xa có tầm đánh, hướng, chọn mục tiêu và khả năng thi triển khi di chuyển phù hợp.
- Học nguyên tắc vận hành từ game tham chiếu rồi tạo luật và bản sắc riêng.
- Tu luyện có chữ Minh, chữ thường và chữ Tâm ma với đặc tính khác nhau. Cần nhận diện, chọn nhanh, gõ chính xác; chữ Minh có thể hết hạn. Tránh gõ hoàn thành chữ Tâm ma.
- Lớp mạnh sớm và lớp phát triển muộn đều phải có hành trình hữu dụng.
- Nhân vật, quái, map và kỹ năng dùng hướng 2D/sprite; tạo chiều sâu bằng mỹ thuật, lớp, bóng, ánh sáng và VFX. Không mặc định runtime 3D cho đông quái.
- Không đưa xây thành, bang hội, đấu giá hoặc mô phỏng NPC phức tạp vào phạm vi này.

### 0.1. Trạng thái và giới hạn

“Đã xác định” là hướng người dùng nêu. “Đề xuất” là luật dự án để review. Mọi con số chưa có dữ liệu chơi thật đều là thông số thử.

Đã đọc nguồn giới thiệu chính thức, manual, tài liệu thiết kế và hướng dẫn được liệt kê cuối tài liệu. Không tuyên bố đã chơi hết hoặc xem toàn bộ video của từng game.

Ảnh người dùng gửi có tu sĩ thiền định và các cầu sáng xanh/trắng/đỏ. Ảnh tĩnh không đủ xác nhận toàn bộ luật, xác suất hay tốc độ của phiên bản đang minh họa. Các hướng dẫn Tale of Immortal năm 2021 được dùng như nguồn cộng đồng lịch sử, không làm cơ sở khẳng định thông số bản 2026.

Các phương án phụ bản/cơ chế bổ sung dưới đây **chờ người dùng chọn**. Di chuyển tự do bằng chuột/phím và quyền đứng trận/di chuyển đã được người dùng yêu cầu; không cần chờ chọn một trong 5 phương án mới được có chúng.

### 0.2. Những điểm đã sửa so với đề xuất trước

1. Di chuyển tự do bằng chuột/phím là nền combat, không chỉ là animation hoặc nhảy giữa vài điểm.
2. Tách đánh nền tự động khỏi gõ chọn kỹ năng.
3. Lớp buff/pet không bị ép mang hai ô đánh trực tiếp.
4. Tách pet nuôi lâu dài, triệu hồi tạm thời và bot đồng đội.
5. Cân bằng theo giai đoạn, nội dung, khả năng thao tác và đóng góp đội.
6. Tu luyện chọn lọc chữ có nhịp thời gian thực; không dừng thời gian khi người chơi bắt đầu gõ.
7. Không biến Tâm ma thành vật bắt buộc phải gõ để thanh lọc trong mode chọn chữ này.
8. Tách vị trí trong/ngoài trận với trạng thái đứng yên/đang di chuyển.
9. Thêm thu thập, khám phá vật phẩm ẩn, tầm đánh và quyền di chuyển của đồng đội.
10. Thêm luật đầu vào cho Voice và Hybrid, giữ một hành động chỉ được kích hoạt một lần.
11. Chốt hướng hình ảnh 2D có chiều sâu và phân bổ hiệu ứng theo ngân sách cảnh đông, không dùng số lượng hiệu ứng để thay chất lượng thiết kế.

## 1. Nền điều khiển — tự do di chuyển và chọn cách học

Nhân vật có tọa độ, tốc độ, hướng và collision trong arena. Người chơi được đi lại bằng phím hoặc chuột, đứng trận, áp sát, thả diều, đổi góc, lấy đồ và tìm bí mật. Auto attack và cơ chế khóa đích hỗ trợ thao tác; người chơi vẫn quyết định kỹ năng bằng tác vụ tiếng Anh.

### 1.1. Ba chế độ đầu vào

| Chế độ | Kích hoạt skill | Bàn phím di chuyển | Chuột |
|---|---|---|---|
| Typing | Gõ từ trên ô | Mũi tên luôn khả dụng khi game có focus; WASD qua trạng thái điều khiển riêng | Click điểm đến, tiếp tục gõ khi nhân vật đang đi |
| Voice | Nói từ trên ô, chốt khi nhận hợp lệ | WASD hoặc mũi tên, không chiếm chữ đang nhập | Di chuyển/chọn mục tiêu như bình thường |
| Hybrid | Luân phiên gõ và nói; mỗi từ có một kênh sở hữu | Như Typing lúc đang nhập, như Voice khi không mở nhập chữ | Vẫn di chuyển, không giành input của từ |

Đây là thiết kế hành vi, không khẳng định ASR đã được tích hợp. Hybrid không ghép nửa từ gõ với nửa từ nhận giọng nói. Người chơi có thể chọn kênh cho hành động kế; khi từ đã bắt đầu, kênh đó giữ quyền đến khi hoàn thành/hủy.

### 1.2. Giải xung đột WASD và chữ

Trong Typing, mặc định chữ cái là nội dung học. Nhấn A trong từ không làm nhân vật bước trái. Người muốn dùng WASD có thể chuyển rõ giữa hai trạng thái, ví dụ Tab có thể cấu hình:

- **Nhập từ:** chữ cái đi vào bài học; mũi tên/chuột vẫn di chuyển.
- **Di chuyển WASD:** chữ cái dành cho điều khiển, không bị ghi lỗi gõ. Phần từ dở được giữ.

Hiển thị trạng thái cạnh vùng nhập. Khi chuyển về nhập từ, thả trạng thái WASD đang giữ để tránh di chuyển kẹt. Không tự bật/tắt theo một khoảng im lặng khó đoán.

Mũi tên và click-to-move là hai cách tránh phải đổi trạng thái liên tục. Người chơi có thể click một điểm, đưa tay về gõ; nhân vật tiếp tục tới điểm đó. Việc vừa giữ mũi tên vừa gõ bằng hai tay là tùy chọn, không phải thao tác bắt buộc của mọi phụ bản.

### 1.3. Chuột và ưu tiên lệnh

Mapping thử: chuột phải trên đất để đi; chuột trái chọn mục tiêu/tương tác. Có thể đổi nút trong settings. Nhấp vào UI không truyền xuyên thành lệnh đi.

- Click-to-move tính đường quanh địa hình theo luật thông thường; không tự chọn đường né mọi đòn boss.
- Lệnh bàn phím mới ghi đè đường click đang chạy; thả phím dừng di chuyển bàn phím.
- Click mới thay điểm đến cũ; không xếp hàng dài nhiều đường ngầm.
- Điểm không tới được báo rõ, không khiến nhân vật đứng kẹt im lặng.
- Bấm vào mục tiêu có thể đặt soft target, không bỏ qua yêu cầu gõ/nói để dùng chiêu chủ động.
- Di chuyển/chọn đích không xóa từ đang nhập. Lệnh kỹ năng, lệnh đi và mục tiêu là các trạng thái tách biệt.
- Ô nhập chat, menu và trường nhập hệ thống lấy focus thì không tiếp tục bắt phím game; không chặn phím tắt hệ điều hành/trình duyệt tùy tiện.

### 1.4. Hợp đồng hành động và voice

- Một từ hoàn thành hợp lệ chốt một hành động có ID; animation không nhân thêm giao dịch.
- Từ lấy từ bài học và thay theo lịch; không dùng mã cố định như “attack/heal/left” cho mọi lần.
- Tên skill, icon và tác dụng tách rõ với từ đang luyện.
- Ô skill, thân pháp và lệnh cùng dùng một bộ phân giải. Không trùng toàn từ; tránh cặp tiền tố hoàn chỉnh gây cast nhầm.
- Khi đã khóa từ, lỗi gõ không tự chuyển sang ô khác. Ô hồi xong không giành input.
- Sửa bằng Backspace. Hủy toàn từ là thao tác có chủ đích, ví dụ Esc ngắn khi đang nhập; lúc không có từ thì Esc mở menu. Mapping này cần thử.
- Hủy/gõ lại không tạo damage, linh lực, mastery hay thưởng học.
- Skill/boss đổi phase không làm từ đang gõ biến thành một từ khác.
- Chiêu lớn nhận input tiếp theo ngay khi logic cho phép; không bắt ngồi chờ CGI.
- Kết quả ASR tạm thời không cast, tiêu mana hoặc khởi động cooldown. Chỉ kết quả được chấp nhận theo luật của phiên mới chốt.
- Kết quả giọng nói đến muộn không cast vào ô đã đổi từ, skill đang hồi hoặc hành động đã hoàn thành bằng gõ. Dùng danh tính từ/hành động, không chỉ so chuỗi chữ mới nhất.
- Nếu hai kênh gửi cùng một lần hoàn thành, chỉ chốt một lần. Đổi chế độ không giữ kết quả ASR cũ để bắn vào trận mới.
- Nhận sai hoặc độ tin cậy thấp cho phản hồi/retry; không tự trừ accuracy gõ. Nhận được từ không đồng nghĩa đã đánh giá phát âm chuẩn.
- Không tăng damage chỉ vì voice có thể nói từ ngắn nhanh hơn. Cùng cooldown, quota và nguyên tắc đầu tư; preset học và đo tốc độ của từng kênh tách rõ.

### 1.5. Đánh khi di chuyển: cận chiến và tầm xa

Cận chiến có tầm, cung đánh và hướng. Người chơi di chuyển áp sát hoặc vòng sườn, chọn soft target hoặc để ưu tiên tự động. Auto attack chỉ công kích mục tiêu hợp lệ trong tầm; không tự kéo nhân vật đi đuổi xa khi người chơi chưa chọn truy kích.

Tầm xa có thể đi và công kích, giữ cự ly, đổi góc bắn hoặc tìm đường nhìn. Tự ngắm là tùy chọn để Typing dùng được hai tay. Có thể chọn hướng bằng chuột/soft target; kỹ năng vẫn yêu cầu tác vụ học.

Chiêu có nhãn rõ:

| Nhóm | Khi nhân vật đi |
|---|---|
| Buff/hộ thân | Thường cast được khi đi; không bắt đứng mỗi lần gõ xong |
| Đạn/chiêu cơ động | Đi và cast theo hướng/đích hợp lệ |
| Đòn cận chiến nặng | Có thể cần dừng ngắn đã báo, đổi lại giá trị hợp lý |
| Vận công lớn | Có thời gian tụ lực rõ, người chơi chủ động chấp nhận |
| Trận/cơ quan đặt đất | Chọn điểm/cấu hình trước, có cách thu hồi/chuyển phù hợp |

Kiểm tầm lúc chốt cast theo luật chiêu. Nếu chiêu không có đích hợp lệ, không tiêu mana/CD như một lần tung thành công; giữ kết quả học, báo ngoài tầm rõ và cấp lại cơ hội nhập. Không cho hành động thất bại tạo tài nguyên hợp trận. Chiêu có thể đổi đích phải dùng quy tắc công khai, không ép người chơi gõ lại giữa từ chỉ vì quái vừa chết.

### 1.6. Trong trận pháp và đứng yên là hai trục

| Trạng thái | Lợi ích/đánh đổi đề xuất |
|---|---|
| Di chuyển trong vùng trận | Vẫn nhận hiệu ứng vùng, có thể né/đổi góc trong phạm vi |
| Đứng yên trong vùng trận | Có thể tích định tâm ngắn cho nhánh chuyên vận công; không phải mọi build đều cần |
| Ra ngoài trận | Chọn góc, tiếp cận địch/đồ/bí mật; mất dần phần bảo hộ/gia trì gắn với vùng |
| Quay lại trận | Khôi phục liên kết theo thời gian ngắn, không xóa toàn bộ tiến trình cá nhân |

Phần tăng lực của trận phải đủ đáng chọn nhưng không làm ra ngoài đồng nghĩa mất phần lớn sức mạnh. Khả năng cơ động, tránh damage và uptime công kích cũng là giá trị cần cân cùng damage bảng.

Có thể thử 1–2 giây đệm khi qua biên và một thời gian nạp lại ngắn; đây là thông số chưa chốt. Đi ra/vào không tạo buff mới cộng chồng, không cấp khiên đầy miễn phí mỗi bước. Một hiệu ứng giữ ID và giới hạn của nó.

Đứng trong trận không tăng accuracy tiếng Anh hoặc tự hoàn thành từ. Nếu có thưởng định tâm, đó là chỉ số RPG.

### 1.7. Nhặt đồ và tìm vật phẩm ẩn

- Tiền/nguyên liệu thường: tự hút trong bán kính gần; người chơi có thể chạy tới nhặt.
- Sau trận: gom phần đồ thường còn lại hoặc cho thu dọn thuận tiện, không bắt đi quanh nhặt từng đồng.
- Trang bị/rương/vật phẩm đặc biệt: đánh dấu dễ thấy, dùng tới gần/tương tác hoặc chọn nhặt theo luật rõ.
- Bí mật: lối phụ, điểm cảm ứng, linh vật ẩn hoặc rương chỉ lộ khi người chơi thăm dò/tới vùng phù hợp. Không yêu cầu tìm điểm ảnh cực nhỏ bằng chuột.
- Khám phá cho lựa chọn/thưởng thêm; mảnh ghép bắt buộc của lớp không bị giấu ở bí mật khó tìm duy nhất.
- Không làm đồ nhiệm vụ/trang bị chính biến mất trong vài giây để người thích đứng trận phải bỏ việc học. Thử thách nhặt thưởng nhanh là hoạt động tự chọn riêng.
- Pet nhặt hộ có thể lấy đồ thường đã lộ trong giới hạn; không tự mở mọi bí mật trên bản đồ.
- Đội dùng loot cá nhân hoặc quyền nhận rõ; người nói/gõ nhanh hoặc chạy tới trước không giành hết đồ của đồng đội.
- Nhặt cùng vật phẩm chỉ chốt một lần; bot không sinh thêm túi thưởng cho người sở hữu.

Di chuyển ra ngoài có giá trị chiến thuật/khám phá; nhặt đồ thường vẫn thuận tiện để tránh biến game học thành việc dọn rác lặp lại.

### 1.8. Ngoài chiến đấu

Di chuyển WASD/mũi tên hoặc click-to-move bình thường. Tương tác NPC, cửa, tài nguyên bằng chuột hoặc phím có thể cấu hình. Khi mở chat/ô nhập, chữ cái thuộc trường nhập, không làm nhân vật đi.

Khám phá có thể mở tương tác typing/voice riêng; không bắt gõ một từ cho từng bước chân trên bản đồ.

### 1.9. Ngân sách chú ý và deck

Mốc thử là 4–6 ô skill lớn. Đi bộ/chạy bằng chuột/phím không chiếm ô skill. Thân pháp đặc biệt như lướt, bay ngắn, phản ảnh có thể là chiêu hoặc tiện ích theo luật riêng.

Ít nhất một ô là hành động liên tục và một ô có cách tự cứu. Một ô đổi chức năng theo phase chỉ cập nhật ở biên hành động an toàn; không thay nghĩa giữa từ.

Biến thể 4 skill + 2 lệnh chỉ dùng khi phụ bản điều quân cần và vẫn giữ bản sắc support/pet. Không bắt hy sinh hai kỹ năng chỉ để được đi trái/phải trong combat nền.

## 2. Nguồn tham chiếu và phần chắt lọc

| Game/nguồn | Nguyên tắc đã xác nhận | Phần dự án học |
|---|---|---|
| Into the Breach, tài liệu GDC của Matthew Davis [R01] | Đòn địch báo trước, ưu tiên khả năng đọc và lựa chọn | Người chơi biết nguy cơ trước khi chọn đáp án |
| Epistory, trang chính thức/Steam [R02] | Khám phá, combat và menu bằng bàn phím | Bàn phím có thể gánh cả hành trình |
| Typing of the Dead: Overkill, manual [R03] | Gõ để khóa mục tiêu, có co-op 2 người | Từ định tuyến hành động không cần chuột |
| Panzer Dragoon: Remake, giới thiệu phát hành [R04] | Các màn hành trình, địch nhiều hướng, khóa mục tiêu | Cảm giác chiến đấu khi đang hành tiến |
| Sekiro, hướng dẫn Activision [R05] | Tấn công và deflect gây áp lực Posture | Phá thế và phản công ngoài việc rút HP |
| Transistor, FAQ Supergiant/bài trải nghiệm trực tiếp PlayStation [R06–R07] | Kết hợp kế hoạch với hành động, xếp chuỗi trong Turn | Lập chiêu rồi thực thi liên hoàn |
| Bad North, mô tả nhà phát hành [R08] | Lệnh cấp đội, binh lính tự đi và đánh | Điều quân ở cấp quyết định |
| SUPERHOT, giới thiệu chính thức [R09] | Nhịp thời gian liên hệ với hành động | Cân nhắc đổi nhịp; không chọn thành phương án thứ sáu |
| Outshine, giới thiệu phát hành [R10] | Typing chiến đấu, kỹ năng, boss và điều khiển bàn phím | Tham chiếu thêm về nhịp typing hành động |

Không sao chép cốt truyện, UI, asset, tên kỹ năng đặc trưng hay toàn bộ vòng chơi của các game trên. Các luật tu tiên typing ở mục 3–7 là đề xuất của dự án; nguồn không chứng minh chúng đã hoạt động tốt.

## 3. Phương án 1 — Thân pháp cơ động và trận vị chiến thuật

**Cập nhật V2.2:** đi lại tự do bằng chuột/phím là nền đã xác định. Phương án này bổ sung thân pháp và các vị trí chiến thuật, không giới hạn người chơi vào vài điểm.

### 3.1. Không gian

Arena có địa hình đi được, góc đánh, chướng ngại và 3–5 điểm có giá trị như lôi trụ, bệ hộ pháp, vị trí cao hoặc đường vòng. Người chơi đi tới bằng phím/chuột. Skill thân pháp đặc biệt dùng gõ/nói nếu trang bị, chẳng hạn lướt qua khoảng hẹp hay tạo ảnh hộ; đi thường không tiêu ô skill.

### 3.2. Một chu kỳ

1. Boss báo vùng đông sắp bị sét quét.
2. Người chơi tự chạy ra khỏi vùng bằng phím/chuột, hoặc chọn một công cụ hộ pháp.
3. Có thể tới gần địch để cận chiến, vòng ra góc để đánh xuyên hoặc trở về vùng gia trì.
4. Vật phẩm/bí mật ở một nhánh phụ tạo thêm lựa chọn; không ép bỏ đòn phòng thủ để nhặt tiền thường.
5. Thân pháp đặc biệt cho cách tiếp cận/thoát khác, có chi phí và dấu hiệu rõ.

### 3.3. Luật công bằng

- Cảnh báo đủ cho cách giải dự kiến của preset. Không đồng thời bắt vừa chạy chính xác vừa gõ/nói một đáp án bắt buộc trong thời gian bất khả thi.
- Lối đi và vùng đánh nhìn được trên mặt đất; hình VFX giả độ cao không thay collision bí mật.
- Điểm đến không bị boss âm thầm chuyển vùng sau khi đã chốt đòn báo, trừ đòn truy đuổi có dấu hiệu riêng.
- Không mặc định miễn thương toàn đường lướt. Mọi lớp có công cụ sống sót nền.
- Không có tình huống chỉ đúng một lớp có thân pháp hiếm mới qua nội dung phổ thông.
- Không để click-to-move tự dự báo đòn tương lai và né hoàn hảo.

### 3.4. Đội, pet và thu thập

Không body-block đồng đội vô lý hoặc tranh một điểm đứng duy nhất. Pet theo chủ/giữ chốt theo cấu hình; trận/cơ quan có thu hồi/chuyển mạch, không mất cả build mỗi lần đổi chỗ. Nhặt đồ và quyền thưởng theo mục 1.7.

### 3.5. Phụ bản mẫu và ưu tiên

“Lôi Đài Tam Vị” trở thành arena di chuyển tự do với ba khu vực chiến thuật, không còn ba tọa độ bắt buộc. Có thể đứng trong bệ gia trì, chạy phá trụ mở sơ hở, lấy đường vòng hoặc thả diều.

**Ưu tiên thử:** trước hết kiểm di chuyển tự do + chọn skill + cận/tầm xa. Thân pháp/trận vị đặc biệt là lớp mở rộng cần review. Mốc 20–25% ký tự cho di chuyển của bản cũ không còn áp cho đi bộ/chạy bằng phím hoặc chuột.

## 4. Phương án 2 — Ngự kiếm hành tiến và truy kích

**Quyết định:** theo tuyến nào, xử lý mối nguy nào, khi nào bám boss hoặc đổi đường.

### 4.1. Cách điều khiển

Đây là biến thể phi hành riêng: nhân vật/đội có thể hành tiến trên phi kiếm, linh chu, tọa kỵ hay đài chiến. Người chơi đổi tuyến bằng phím/chuột; bản hỗ trợ có thể chọn đường bằng từ trên ô ngữ cảnh. Không dùng cơ chế hành tiến này để khóa di chuyển của combat nền.

Ở cửa rẽ, thể hiện các nhánh bằng không gian và UI rõ. Có thể chọn bằng phím/chuột hoặc lệnh gõ/nói ở preset hỗ trợ. Phá chướng ngại mở thêm đường, tạo đáp án cho lớp ít cơ động.

### 4.2. Trận mẫu

Đội bay vào hẻm núi; quái xuất hiện ở hai sườn. Một tuyến báo đá rơi, tuyến khác có hộ vệ mạnh. Người chơi đổi tuyến hoặc phá chướng ngại. Boss bay ngang, lộ bộ vị được định tuyến rõ cho chiêu phá giáp. Phá phong ấn để bám đuổi rồi vào điểm chiến đấu chốt.

Mỗi lần chọn tuyến phải đổi nguy cơ, cơ hội hoặc mục tiêu. Chỉ cuộn nền đẹp thì chưa tạo cơ chế mới.

### 4.3. Tương thích nhân vật

- Thể tu đứng trên linh chu/đài chiến; không phải mọi lớp đều biến thành kiếm sĩ.
- Linh thực, cơ quan và trận nhãn gắn với phương tiện hoặc theo chủ.
- Pet không tụt lại sau camera.
- HUD không xoay theo đường bay; camera tự ổn định, có giảm rung.
- Không đổi toàn bộ từ đang gõ khi camera chuyển cảnh.

### 4.4. Đội và bot

Mỗi người có tuyến riêng hoặc vai trên cùng phương tiện. Quyền chọn nhánh chung phải xác định trước: trưởng đội có báo trước hoặc quyết định ở checkpoint an toàn. Một người không tùy ý bẻ đường cả đội bằng một chữ giữa trận.

Bot bảo vệ sườn và xử lý mục tiêu phụ theo vai. Buff vẫn tác động hữu ích khi di chuyển.

**Đề xuất ưu tiên: vừa, phù hợp phụ bản đặc biệt.** Chi phí đường đi, camera và dựng màn cao hơn thủ trận. Chưa chốt thành combat mặc định.

## 5. Phương án 3 — Đấu pháp phá thế và phản chế

**Quyết định:** đọc ý định, chọn cách hóa giải, mở thời cơ phản công.

### 5.1. Hai mục tiêu

Boss có HP và thanh thế. Đánh đúng điểm yếu, phá niệm, giải ấn hoặc đỡ đòn đặc biệt làm thế tiến tới break. Break mở cửa sổ trấn áp/dồn sát thương; không mặc định giết ngay.

Người chơi tự chọn cự ly/vị trí bằng chuột hoặc phím. Chiêu phản/cận chiến có animation rõ; hoạt ảnh không tự kéo nhân vật vào vùng nguy hiểm trái lệnh đi.

### 5.2. Đọc đòn và đáp án

| Ý định | Một số cách giải |
|---|---|
| Đại đao tụ lực | Hộ pháp hoặc phá thế để ngắt |
| Bầy đạn | Màn chắn, tiêu đạn, phá nguồn niệm |
| Hấp thu linh lực | Giải ấn hoặc đổi nhóm chiêu |
| Khiên hồi máu/phản damage | Kiềm công pet, giữ đòn, giải khiên |
| Sơ hở sau đòn | Buff, hợp kích, chiêu dồn lực |

Gõ hộ pháp từ trước tạo thế thủ tồn tại đủ lâu để đón đòn. Không yêu cầu ký tự cuối trùng một cửa sổ parry nửa giây.

### 5.3. Giá trị của các vai

Thể tu đỡ, phù/âm giải hoặc phá niệm, DPS tận dụng sơ hở, ngự thú đổi lệnh hộ chủ/tập kích. Lớp ít burst có thể đóng góp thế qua cơ chế phù hợp, có quota rõ.

Mỗi đòn quan trọng có ít nhất hai hướng giải. Không để một ô hộ pháp là đáp án tốt nhất cho mọi đòn. Boss có kháng tạm sau break, tránh 7 người khóa vĩnh viễn.

**Đề xuất ưu tiên: cao.** Bổ sung vào boss của combat di chuyển tự do; người chơi có cả né vị trí và phản chế bằng skill.

## 6. Phương án 4 — Ngưng thời lập chiêu, tung liên hoàn

**Quyết định:** thứ tự hành động, đường tiếp cận và lượng hành động hữu hạn.

### 6.1. Vòng solo

1. Tích định tâm bằng typing và xử lý cơ chế.
2. Gõ ô Định Tâm để mở cửa sổ.
3. Thế giới combat dừng, người chơi gõ xếp tối đa 3 hành động trong ngân sách.
4. Có thể chọn đường/điểm bằng chuột hoặc phím để xếp di chuyển → phá giáp → tuyệt kỹ. Trong phase dừng, thao tác đi chỉ preview/xếp lệnh trong ngân sách, không cho nhân vật đi miễn phí khi thế giới đứng yên.
5. Xác nhận rõ bằng phím hoặc đủ số hành động đã chọn trước; không tự phóng chỉ vì ngừng gõ ngắn.
6. Nhân vật thực thi liên hoàn; khi logic cho phép, input trở về bộ ô thường.
7. Định tâm hồi trong thời gian combat thực, không dừng miễn phí liên tục.

### 6.2. Luật bắt buộc

- Địch, pet, DoT, hồi máu, cooldown, buff và timer phụ bản cùng dùng đồng hồ combat đang dừng.
- Thời gian học ngoài đời ghi nhận riêng.
- Xếp chiêu có cooldown phải giữ chỗ charge; không xếp 3 bản cùng chiêu khi chỉ có một lượt dùng.
- Hủy queue không nhân tài nguyên.
- Đích chết thì chuyển đích theo luật đã báo, không xóa từ đã gõ hoặc đổi chiêu sang tác dụng khác.
- Preview không hứa kết quả chắc chắn rồi âm thầm đổi luật lúc thực thi.

### 6.3. Co-op là biến thể riêng

Không cho một người dừng cả server tùy ý. Nếu chọn mode này cho đội, phụ bản mở phase lập kế hoạch chung; mỗi người xếp 1–2 hành động trong cửa sổ đủ rộng, bot điền việc của bot.

Người chưa xong dùng hành động an toàn đã chọn trước hoặc tiếp tục combat bình thường theo luật phụ bản; không giả vờ đã gõ xong từ. Không cần cả 7 người kết thúc đồng thời mới cho game chạy.

**Đề xuất ưu tiên: vừa, thử solo trước.** Hợp từ mới và combo nhưng có thể giảm nhịp gõ liên tục. Nên là mode ảo cảnh/luận kiếm trước khi cân nhắc thay combat nền.

## 7. Phương án 5 — Điều quân trên nhiều trận tuyến

**Quyết định:** cứu tuyến nào, đưa nhóm nào tới đâu, khi nào chuyển công–thủ.

### 7.1. Chiến trường và input

Có 2–3 chốt/tuyến dễ đọc. Đồng minh tự đi và đánh theo lệnh. Prototype 4 skill + 2 lệnh; mỗi lệnh gộp rõ nhóm sở hữu, hành động và đích, chẳng hạn “hộ vệ về chốt tây”. Gõ một từ tiếng Anh trên ô để thực hiện.

Nhân vật chính vẫn đi tự do bằng chuột/phím. Bộ lệnh gõ/nói điều phối nhóm giúp người đang học không cần kéo chọn từng đơn vị; có thể thêm chọn nhóm bằng chuột/phím tùy chọn. Trạng thái lệnh đang thực hiện luôn thấy được.

### 7.2. Chu kỳ mẫu

Địch giáp đổ sang trái, bầy nhỏ sang phải. Điều đội phá giáp giữ trái, dùng AoE xử lý phải. Pháp sư xuất hiện phía sau: chuyển đội cơ động đánh chặn. Giữ buff để hợp kích hay dùng khiên cứu chốt. Boss đổi hướng: rút đội về và tái phân công.

### 7.3. Giữ gọn và công bằng

- Quân phụ bản có ngân sách chung, cấp theo nội dung cho mọi lớp.
- Pet riêng của ngự thú không tự biến thành thêm ba đội quân miễn phí.
- Không thêm xây nhà, đào tài nguyên hoặc quản lý dân cư.
- Một lệnh giữ hiệu lực tới khi xong/được đổi có chủ đích.
- Không cùng lúc đòi ba từ cứu nguy ở ba tuyến.
- Có thể cho nhân vật trực tiếp tham chiến ở một tuyến, AI giữ phần còn lại.
- Đội người có quyền sở hữu nhóm rõ; người này không ghi đè lệnh nhóm người khác.

**Đề xuất ưu tiên: sau.** Hợp hỗ trợ/pet/trận tu, nhưng cần AI và UI tốt. Thử hai tuyến trước, chưa mở thẳng 3 tuyến/7 người.

## 8. Bảng lựa chọn năm cơ chế

| Phương án | Chủ động chính | Chuyển động có ý nghĩa | Solo/đội | Rủi ro |
|---|---|---|---|---|
| 1. Thân pháp/trận vị | Địa hình, tiếp cận, thoát và góc đánh | Đi tự do bằng chuột/phím, thêm chiêu thân pháp | Tốt / tránh kẹt và tranh chỗ | Cơ động vượt trội hoặc terrain khó đọc |
| 2. Ngự kiếm truy kích | Tuyến, nhánh, ưu tiên đích | Có, đổi đường và nguy cơ | Tốt / quyền chọn nhánh chung | Chỉ thay nền nếu ít lựa chọn |
| 3. Phá thế phản chế | Công–thủ và đáp án | Theo chiêu/cự ly | Tốt / vai bổ sung | Một đáp án tối ưu lặp mãi |
| 4. Lập chiêu liên hoàn | Thứ tự, ngân sách | Có nếu xếp thân pháp | Tốt / co-op phức tạp | Mất nhịp, lỗi đồng hồ |
| 5. Điều quân nhiều tuyến | Phân quân, cứu chốt | Ở cấp nhóm | Tốt / sở hữu rõ | Quá nhiều thông tin |

Nền đã xác định là di chuyển tự do + skill qua Typing/Voice/Hybrid + lợi thế vùng trận. Khuyến nghị kiểm nền với boss có 3 trước. Các cơ chế đặc biệt của 1, 2, 4, 5 vẫn là ứng viên; không cần chọn chúng mới được đi lại.

Một phụ bản có một cơ chế chính và tối đa một cơ chế phụ ở bản thử. Không dồn cả 5 vào cùng trận. Thủ hộ trận thú triều vẫn là một mode.

## 9. Đánh nền tự động và phần typing

### 9.1. Hai tầng sức mạnh

Đánh nền duy trì nhịp chiến trường. Gõ hoặc nói theo chế độ học quyết định skill, buff, lệnh pet, thân pháp đặc biệt, phá thế, giải ấn và hợp trận. Đi thường bằng chuột/phím. Tự ngắm không đồng nghĩa tự chọn chiêu mạnh thay người học.

Trong các ví dụ combat còn dùng từ “gõ”, đó là ví dụ của profile Typing; Voice/Hybrid đi qua cùng giao dịch skill theo mục 1.4. Tác vụ tu luyện chuyên luyện gõ ở mục 18 giữ profile riêng, không mặc định nhận giọng nói với cùng timer.

| Build | Đánh nền chưa được buff/lệnh, tỷ trọng output thử | Phần còn lại cần typing |
|---|---:|---|
| Công kích trực tiếp | 15–25% | Chiêu chủ động, combo, thần thông |
| Hỗ trợ solo | 20–30% | Self-buff pháp khí, cộng hưởng, đòn bổ sung |
| Ngự thú/khôi lỗi | 20–30% | Lệnh mạnh, buff, hợp kích, chiêu chủ |
| Thể tu/phản kích | Đủ dùng khi ít địch đánh mình | Tạo thế chủ động, đỡ đúng nguy cơ, phản chấn |

Đây là mục tiêu phân bổ để thử cùng preset, không phải số game tự ép về sau mỗi trận. Pet có thể gây phần lớn damage cuối trận; cần phân biệt lượng đánh nền và phần tăng thêm nhờ lệnh/buff.

Không tắt mọi auto attack khi người học dừng đọc vài giây. Nội dung quan trọng có quyết định chủ động để AFK không thành cách phát triển tốt nhất.

### 9.2. Deck theo vai

| Vai | Sáu ô minh họa |
|---|---|
| Công kích | 1 đòn gõ liên tục, 2 chiêu công/thiết lập, 1 khống chế, 1 hộ pháp, 1 thần thông |
| Buff | 1 dẫn linh liên tục, 2 buff khác vai, 1 hồi/giải, 1 hộ pháp, 1 thần thông |
| Pet | 1 lệnh liên tục, 1 hợp kích, 1 đổi vai/đánh dấu, 1 buff pet, 1 hộ chủ, 1 thần thông |
| Trận/cơ quan | 1 nạp lực liên tục, 2 điều khiển cấu trúc, 1 phát lực, 1 phòng thủ, 1 thần thông |

Đi thường không chiếm ô deck. Biến thể phụ bản có 4 skill + 2 lệnh chỉ áp khi cần điều quân/ngữ cảnh; không xóa công cụ tự cứu hoặc bản sắc lớp. Số ô không phải số kỹ năng nhân vật được học trong toàn game.

## 10. Các đường sức mạnh đầu–giữa–cuối game

### 10.1. Khác biệt cần tạo

Lớp mạnh sớm có chiêu nền hiệu quả ngay, ít setup, dọn địch đầu thuận lợi. Lớp muộn mở thêm liên kết, chuyển hóa tài nguyên, nhiều lựa chọn công–thủ hoặc phối hợp. Đỉnh muộn đi cùng điều kiện và đánh đổi.

“Yếu đầu” là cần chọn chiêu/đầu tư đúng hơn hoặc chưa có đỉnh phối hợp; vẫn có đủ công cụ chơi và vượt nội dung phổ thông. “Mạnh sớm” không có nghĩa đồ/kỹ năng ngừng phát triển cuối game.

### 10.2. Hồ sơ số để bắt đầu thử

K0–K6 là checkpoint đầu tư tương đương, không bắt buộc 7 cảnh giới. Giá trị là ngân sách hiệu quả solo mục tiêu so với bộ tham chiếu 100 ở cùng checkpoint. Đây không phải damage đo được, không gộp hồi đội thành DPS, không bảo đảm mọi matchup giống nhau.

| Hồ sơ | K0 | K1 | K2 | K3 | K4 | K5 | K6 | Đặc điểm |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| F — phát huy sớm | 110 | 109 | 106 | 103 | 100 | 98 | 97 | Dễ vào nhịp, ít setup, cuối vẫn hữu dụng |
| S — ổn định | 101 | 102 | 102 | 102 | 103 | 102 | 102 | Tiến đều, ít lệ thuộc một mảnh ghép |
| R — phát triển muộn | 92 | 94 | 97 | 101 | 105 | 109 | 112 | Liên kết mở dần, cần giữ điều kiện |
| H — lai linh hoạt | 96 | 98 | 100 | 102 | 104 | 106 | 108 | Tăng khả năng đổi vai/cấu hình |

Game không âm thầm kéo kết quả thực về bảng. Nếu test lệch, sửa kit/encounter/hệ số gây lệch. Bảng chỉ giúp đặt mục tiêu và tìm giả định vô lý.

### 10.3. Bảo vệ đầu game

- Trao đánh nền, hành động gõ liên tục, công cụ tự cứu trong bài giới thiệu lớp.
- Mảnh ghép thiết yếu có đường nhận chắc chắn qua tiến trình, không giấu sau rơi đồ hiếm.
- Lớp pet nhận pet chính ngay; lớp trận có trận nhỏ hoạt động khi solo.
- Thể tu tích thế cả khi chủ động đánh, không đứng chờ địch đánh mới có damage.
- Lớp khống chế có damage/phá thế thay thế trên boss kháng khống chế.
- Không tăng gấp đôi chi phí nuôi pet/cơ quan để “trả giá” cho sức mạnh cuối.
- Cho thử bộ cao trong phòng tập và đổi nhánh với chi phí hợp lý.
- Nếu support solo quá chậm, sửa self-buff/đòn nền/mục tiêu, không chỉ tăng thưởng để che vấn đề.

### 10.4. Giữ giá trị cuối cho lớp sớm

Địch đổi phase nhanh, mục tiêu khẩn cấp và các trận ngắn cho lớp ít setup lợi thế. Lớp muộn đạt đỉnh tốt hơn khi giữ được điều kiện; khả năng chuyển setup giữa phase có chi phí hợp lý.

Không thiết kế lớp muộn luôn hơn ở mọi mặt sau một mốc. Lớp sớm vẫn có nâng cấp và biến chiêu, không thành lựa chọn sai phải bỏ nhân vật.

### 10.5. Cân bằng đứng trận, cơ động, cận chiến và tầm xa

Đo hiệu quả thực theo thời gian được công kích, độ phủ mục tiêu, an toàn, setup và cơ chế phụ bản. Damage trên bảng không đủ kết luận.

Ví dụ giả định: đứng trận tăng 12% damage nhưng một tình huống chỉ có 75% uptime thì output quy đổi là 1,12 × 0,75 = 0,84. Nhánh cơ động không nhận buff đó nhưng giữ 90% uptime thì là 0,90. Ví dụ chỉ minh họa phép so, không phải số đã chốt hoặc kết quả playtest.

- Trong vùng trận vẫn di chuyển được; buff vùng và bonus đứng yên là hai hiệu ứng khác.
- Nhánh định tâm được lợi khi giữ chỗ, có công cụ chịu/giải áp lực; mất bonus không kéo theo mất cả kit.
- Nhánh cơ động có tiếp cận/thoát và đổi góc tốt, đổi lại một phần ngân sách damage/hộ thể theo build.
- Cận chiến cần giá trị tương xứng với thời gian vào tầm: đòn quét/phá thế, khả năng bảo hộ hoặc burst phù hợp. Không tự tăng mọi chỉ số chỉ vì tên “cận chiến”.
- Tầm xa có lợi về cự ly, nhưng đường nhìn, địch áp sát và nguy cơ vùng giữ chiến thuật; không chỉ tạo quái miễn nhiễm để phạt lớp này.
- Boss hỗ trợ cả né vị trí và một số giải pháp hộ pháp/phản chế phù hợp, để người thích đứng trận vẫn có đường chơi nội dung phổ thông.
- Voice có thể cho điều khiển di chuyển liên tục thuận hơn Typing; đo lợi thế đó cùng độ trễ/nhận sai. Không khẳng định ba kênh có cùng độ khó.
- Bảng cạnh tranh tách quy tắc/kênh/preset khi cần; phần thưởng tiến trình phổ thông không khóa vào việc phải chọn một kênh.
- Thưởng bí mật là lựa chọn thêm, vật liệu thiết yếu vẫn có đường rõ. Đồ thường thu dọn sau trận tránh chênh thu nhập chỉ do phải chạy nhặt.

### 10.6. Bot, pet và quyền rời trận

Bot có cấu hình theo chủ/giữ vùng/hỗ trợ nguy cấp, không tự bỏ cả trận để đuổi một đồng tiền. Khi người chơi ra ngoài, bot giữ vai đã phân; không được nhân thêm một bot vào vị trí của người vẫn đang tham gia.

Pet theo vị trí thực của chủ; nếu gặp đường hẹp, dùng cơ chế tái hợp hợp lệ được báo rõ. Không teleport gây hit ngoài tầm hoặc nhặt đồ xuyên tường. Cơ quan/trận đặt có chuyển mạch/thu hồi để thích nghi nhưng không di chuyển miễn phí vô hạn khi đang gây hiệu ứng.

## 11. Ma trận 24 trường phái để phát triển dài hạn

Các hồ sơ là đề xuất. Toàn bộ 24 hướng chưa được cân bằng hoặc cam kết sản xuất. Khi một hướng không tạo khác biệt đủ rõ, gộp thành nhánh của lớp khác thay vì giữ số lượng cho đẹp.

| Trường phái | Đường | Vòng chiến đấu riêng | Đầu game cần có | Đỉnh về sau / đánh đổi |
|---|---|---|---|---|
| Kiếm | S | Ghim → kiếm trận → thu kiếm | Kiếm đơn, cung chém, kiếm hộ | Hồi kiếm nhiều đường; tránh dồn nhầm đích |
| Đao | F | Chém quạt → tích thế → đòn nặng | AoE tốt, đỡ–phản dễ hiểu | Burst ngắn/kết liễu; tầm và độ phủ xa hạn chế |
| Thương | F | Xuyên hàng → mở giáp → liên kích | Đường đâm tự ngắm, quét gần | Phá giáp truyền sơ hở; địch phân tán giảm hiệu quả |
| Cung | F | Ưu tiên địch nguy hiểm → xuyên/rải tên | Đánh xa, bắn hạ đạn | Bắt mục tiêu tốt; cần xử lý bầy áp sát |
| Hỏa | F | Cháy vùng → lan → kích nổ | Có nổ trực tiếp để không phải chờ DoT | Lan bầy mạnh; chuyển phase nhanh giảm giá trị |
| Băng/thủy | S | Chậm → kết tinh → giữ/vỡ ấn | Đòn trực tiếp, giáp tinh | Đổi kiểm soát lấy burst; boss nhận phá thế thay đông cứng |
| Lôi | R | Điểm dẫn → mạng → lan/dồn | Liên lôi không cần đủ cột, lôi giáp | Nối mạng và xả boss; setup có độ trễ |
| Phong | S | Gom/đẩy → xuyên cụm → mở khoảng | Phong nhận đủ damage độc lập | Điều phối bầy/đạn; boss nặng ít bị dịch chuyển |
| Mộc/y | H | Gieo → nuôi → thu công hoặc hồi | Linh thực nền, self-buff và khiên | Cộng sinh/hồi hữu ích; burst tức thời thấp hơn |
| Thể/thổ | F | Tạo thế → đỡ → phản chấn | Chủ động nạp thế, kim thân | Đỡ nguy cơ, phá thế; công xa hạn chế |
| Phù | H | Đặt ấn → phối hai loại → dẫn phát | Một phù công và hộ phù | Gia trì/giải ấn hoặc nổ; cần phân phối dấu |
| Âm | R | Dẫn âm → buff → cộng hưởng | Pháp khí nền, self-buff, ô dẫn liên tục | Buff đội/hợp âm; focus đội giảm damage riêng |
| Ngự thú | R | Pet nền → lệnh → hợp kích | Pet chính và hộ chủ ngay | Bộ lệnh/tiến hóa; không nhân ngân sách theo số con |
| Đan | H | Dược tính → xúc tác → phản ứng | Đan công kích không cần thuộc recipe | Độc/dược hộ; chống độc không được vô hiệu cả kit |
| Khôi lỗi | R | Triển → đổi mô-đun → nạp/xả | Một cơ quan chính đánh và nhận lệnh | Pháo/thuẫn/ghép; phải theo được mode di chuyển |
| Trận | R | Nhãn → mạch → phát trận | Trận nhỏ solo, nạp lực có damage | Truyền lực/hình trận; cần phân phối công–thủ |
| Huyễn | H | Dụ bầy → kính ấn → phá ảnh | Đòn trực tiếp, boss nhận suy thế | Khống chế và bẫy; charm không áp tuyệt đối lên boss |
| Huyết | H | Xuất huyết → thu khí → công/thủ | Không bắt tự trừ HP để dùng bộ cơ bản | Duy trì/chuyển hóa; hồi và tài nguyên có trần |
| Hồn | R | Hit tạo hồn lực → ấn → dẫn | Boss đơn vẫn cho tích hồn lực | Hồn binh/hồn ấn; quota theo chủ |
| Ảnh | F | Dư ảnh → song kích → hội ảnh | Đòn trực tiếp và ảnh hộ | Burst ít setup; ảnh không lặp buff/ulti vô hạn |
| Tinh tú | R | Thắp điểm → tinh đồ → triệu tinh | Tinh châu và tinh mạc | Chọn hình đồ; tránh quá nhiều điểm phải đọc |
| Không gian | R | Định điểm → bẻ hướng/gom → trảm | Đòn cắt, hộ giới đơn giản | Liên kết đường đánh; không miễn thương thường trực |
| Thời gian | R | Lưu dư âm → tái hiện → đổi nhịp | Đòn trực tiếp, hộ pháp | Tái hiện một phần; không tự sao chép chính nó |
| Nhân quả | R | Đặt nhân → tích tác động → trả quả | Đòn trực tiếp và hộ duyên | Chuyển công/thủ theo ấn; không nhân theo mọi hit của đội |

### 11.1. Những lớp cần gộp nếu thử không khác biệt

Huyết/hồn/ảnh phải khác về nguồn tài nguyên, dạng đòn và cách phòng thủ. Tinh tú/trận phải khác về bố trí và chu kỳ. Không gian/thời gian/nhân quả cần đặc tả tác dụng rõ, không chỉ tên đẹp với cùng AoE.

Các nhánh không gian, thời gian và nhân quả nên mở sau khi nền ổn. Không dùng độ khó hiểu làm lý do biện hộ cho chỉ số quá mạnh.

### 11.2. Nhân vật và trường phái

Một nhân vật có truyền thừa và một số hướng tương thích, không nhất thiết bị khóa vĩnh viễn vào một kiểu build. Nhân vật thần thoại có bộ dấu ấn riêng; thiết kế chi tiết từng nhân vật tiếp tục sau khi chọn nền combat. Trang phục thay diện mạo và VFX phù hợp, không thêm sức mạnh mua ngoài.

## 12. Buff, hồi phục và hỗ trợ

### 12.1. Chuyên môn

| Nhánh | Giá trị | Quyết định |
|---|---|---|
| Cường công | Tăng hiệu quả công kích | Dùng dọn bầy hay giữ lúc boss lộ sơ hở |
| Cộng hưởng | Cường hóa một số lượt skill | Dùng vào nhóm chiêu/người có lợi phù hợp |
| Hộ pháp | Khiên, giảm đòn, phản chế | Chặn đợt nào, giữ charge nào |
| Hồi | Khôi phục phần thực đã mất | Cứu người hay duy trì hộ trận |
| Giải | Cắt cơ chế suy yếu | Giải sớm hay chờ một đợt tích lớn |
| Tạo sơ hở | Suy giáp, phá niệm, trấn | Mở thời cơ cho cả đội |

Buff có hình ảnh tác động: kiếm đồng đội đổi cấu trúc khi gia trì, giáp xuất hiện khi chặn, mạch sáng nối trận nhãn. Không phủ sáng liên tục che chữ.

### 12.2. Hai focus của cùng nhân vật

**Tự Cường:** dành ngân sách cho self-buff và pháp khí/pet cá nhân.

**Đồng Tu:** dành nhiều ô/nhánh cho đội; damage riêng thấp hơn, giá trị phối hợp cao hơn.

Focus hiển thị trước trận và lưu theo loadout. Có thể dùng Tự Cường trong đội hoặc Đồng Tu cùng bot. Không âm thầm giảm chỉ số vì có người thứ hai tham gia. Đổi ở checkpoint, không đổi giữa animation để hưởng cả hai bộ.

### 12.3. Bộ sáu ô support mẫu

| Ô | Chiêu | Solo | Đội |
|---|---|---|---|
| 1 | Dẫn Âm/Dẫn Linh | Dùng liên tục, nạp và đánh bổ sung | Nạp cộng hưởng/hợp trận, vẫn có tác động |
| 2 | Cường Công Chú | Cường hóa pháp khí cá nhân | Buff công kích các thành viên hợp lệ |
| 3 | Linh Khí Cộng Hưởng | Tăng lực vài chiêu kế | Cường hóa lượt skill trong quota |
| 4 | Tịnh Tâm | Hồi/giải cho bản thân | Ưu tiên đồng đội nguy cấp |
| 5 | Linh Quang Hộ | Khiên cá nhân | Khiên theo liên kết trận |
| 6 | Sơn Hà Cộng Minh | Cao trào self-buff | Mở cửa sổ hợp kích của đội |

Chiêu thường thử CD 5–8 giây, hộ pháp 8–12, thần thông 24–36; thời lượng buff cần đủ vài hành động ở preset gõ. Các con số chưa phải cân bằng cuối.

### 12.4. Mục tiêu tự động hoặc chọn bằng chuột/phím

Buff đội dùng liên kết hợp lệ. Hồi đơn ưu tiên tỷ lệ HP, debuff và nguy cơ đã báo; không theo HP tuyệt đối khiến lớp nhiều máu hút mọi lần hồi. Ưu tiên có thể cấu hình trước trận.

Có thể chọn soft target bằng chuột/phím hoặc ưu tiên tự động. Không bắt click trước mỗi chiêu. Buff/heal có phạm vi/liên kết rõ; đi ra khỏi vùng xử lý theo thời lượng/đệm, không giật mất mọi hiệu ứng. Đích chết khi đang nhập: giữ từ và chuyển sang mục tiêu tương đương hợp lệ lúc cast.

### 12.5. Chồng buff và quota

1. Cùng buff ID: lấy mạnh nhất hoặc nối thời gian có trần.
2. Cùng nhóm công dụng: cộng trong bucket có giới hạn thử.
3. Damage, tốc đánh và CDR khác nhóm vẫn phải đo tổng tương tác.
4. Buff chủ sang pet đúng một lần.
5. Buff sinh buff, phản gây phản, pet gọi pet không tự đệ quy.
6. Hợp trận không tự nạp lại điều kiện của chính nó.

Không dùng một con số “tổng hỗ trợ” gộp tùy tiện damage, hồi và giải. Mỗi công dụng có phép đo; kiểm tra kết hợp trong encounter thật.

## 13. Pet được nuôi, triệu hồi phụ và khôi lỗi

### 13.1. Tiến trình pet

| Dữ liệu | Nội dung | Công bằng |
|---|---|---|
| Loài/hệ | Vai công, hộ, hỗ trợ; bộ đòn | Có lựa chọn khởi đầu đáp ứng kit |
| Cấp/cảnh giới | Nền sức mạnh | Theo tiến trình, không treo vô hạn |
| Tư chất | Tiềm năng/nhánh | Có đường cải thiện pet yêu thích |
| Kỹ năng | Auto, lệnh, hộ chủ, hợp kích | Số ô và ngân sách giới hạn |
| Khế ước | Phối hợp chủ–thú | Tăng qua hoạt động hợp lệ của người học |
| Tiến hóa | Hình thái và cơ chế | Vật liệu có đường nhận chắc chắn |
| Ngoại hình | Màu, trang sức, VFX | Tách mua sức mạnh |

Không phạt pet chết vĩnh viễn hoặc đói theo giờ khiến người học phải vào chăm. Nuôi có mục tiêu, không thành lịch việc nhà. Lai giống chỉ cân nhắc sau khi lệnh chiến đấu đã tốt.

### 13.2. Bộ lệnh mẫu

| Ô | Chiêu | Tác dụng |
|---|---|---|
| 1 | Hiệu Lệnh | Dùng liên tục, pet thực hiện một đòn lệnh |
| 2 | Tập Kích | Ưu tiên mục tiêu nguy hiểm/phá giáp |
| 3 | Linh Khế | Buff pet, tránh nhân hai lần từ chủ |
| 4 | Chuyển Thế | Đổi công/hộ/kiềm công theo cấu hình; có CD |
| 5 | Hộ Chủ | Chặn đợt và hỗ trợ sinh tồn |
| 6 | Vạn Linh Đồng Khế | Hợp kích mạnh chủ–thú |

Pet tự đánh khi không có lệnh mới. Lệnh thay ưu tiên hoặc tung hành động mạnh; không cần spam chỉ để pet hoạt động.

Boss phản damage phải có “kiềm công” thực sự: quy định đạn đã bay, DoT đang tồn tại, lệnh đã xếp được xử lý ra sao. Người chơi cần thấy trạng thái, không bị phạt bởi một auto không thể dừng.

Đổi vai công/hộ có thể có cooldown; quyền kiềm công an toàn không bị khóa theo cooldown đó. Có thể dùng chính sách pet dừng theo khiên phản đã được báo và một lệnh bàn phím riêng tùy chọn, không phát thưởng học cho lệnh một phím. Nếu yêu cầu gõ lệnh dừng trong phụ bản, cảnh báo phải đủ thời gian và ô dừng phải sẵn sàng. Đừng tạo bẫy do auto tiếp tục công khi người chơi đã chọn dừng.

### 13.3. Số lượng không nhân sức mạnh miễn phí

Prototype một pet chính; có thể mở hai pet chia vai. “Đàn thú” có thể là animation của một chiêu có tổng damage cố định.

Ví dụ ngân sách pet 70: một con nhận 70; hai con 35–35 hoặc 45–25 theo vai. Thêm con đổi độ phủ/lựa chọn, không tự thành 140.

On-hit, hút máu, tích ấn và hoàn linh lực có quota theo người sở hữu. Pet không phải thêm một thành viên để lấy thêm suất buff cố định hoặc loot.

### 13.4. Tương thích mode

| Mode | Pet/cơ quan/trận đặt |
|---|---|
| Thủ trận | Hộ chủ, ưu tiên rìa nguy hiểm |
| Di chuyển tự do/thân pháp | Theo chủ/giữ chốt; thu hồi/chuyển mạch, không mắc đường |
| Phi hành | Theo phương tiện, không bỏ lại sau camera |
| Đấu pháp | Kiềm công, tập kích sơ hở, có trạng thái rõ |
| Lập chiêu | Cùng đồng hồ thế giới; lệnh tốn ngân sách |
| Điều quân | Pet riêng tách khỏi quân chung phụ bản |

## 14. Solo, tổ đội và trận pháp

### 14.1. Ba hình thức

- Solo thuần: đường giải phù hợp một bộ kỹ năng.
- Một người + bot: đủ vị trí trận pháp.
- Nhiều người + bot bù: thường 2–3; 7 cho đại trận.

Bot lấp vị trí trước trận/checkpoint. Pet không lấp số người. Không tự sinh thêm bot giữa đợt để tăng lực.

### 14.2. Trận pháp

| Trận | Vị trí | Vai gợi ý | Phối hợp |
|---|---:|---|---|
| Lưỡng Nghi | 2 | Công + hộ/hỗ trợ, hoặc hai công có công cụ tự cứu | Chuyển công–thủ, phá ấn nối tiếp |
| Tam Tài | 3 | Chủ công, hộ trận, hỗ trợ/khống chế | Chia nguy cơ, nạp ba nhãn |
| Tứ Tượng | 4 | Bốn công năng tương thích | Luân phiên bảo hộ và mở sơ hở |
| Ngũ Hành | 5 | Năm nguồn tính chất của nội dung riêng | Chuyển hóa/khắc chế theo luật |
| Thất Tinh | 7 | Công đơn, dọn bầy, hộ, buff, hồi/giải, phá niệm, điều phối | Nhiệm vụ theo phase và đại hợp kích |

Vai là chức năng, không luôn là tên lớp. Một lớp đáp ứng 1–2 vai tùy deck nhưng không làm tất cả tối đa. Thuộc tính có thể đến từ kỹ năng/pháp bảo/bot theo luật đã báo, không khóa vào nhân vật hiếm.

### 14.3. Trận nhãn và sinh tồn

Một người/bot phụ trách một trận nhãn theo vai, đây là quyền đảm nhiệm chứ không phải tọa độ bị khóa. Nhân vật vẫn đi bằng chuột/phím. Trong vùng liên kết nhận gia trì; ra ngoài thì liên kết cá nhân giảm theo luật, không tự làm cả trận sập.

Mode cần có thể dùng HP cá nhân + một hộ trận chung. Khi một người đi nhặt đồ không sinh thêm bot miễn phí vào chỗ họ. Phase hợp kích có thể báo trước để người chơi quay về/tái liên kết; thiếu một người giảm mức hợp lực hoặc tạo đường cứu theo nội dung, không xóa vai của mọi người. Không thêm HP từng tường/cổng/công trình trong bản đầu.

Từ hoàn thành hợp lệ tạo đóng góp nạp trận. Support nạp bằng hiệu ứng hữu ích và ô liên tục, không lệ thuộc last-hit. Pet nhiều hit không nhân năng lượng hợp trận.

### 14.4. Hợp trận bất đồng bộ

Mỗi người có bài/từ riêng. Nạp qua giai đoạn đủ dài, không yêu cầu 7 người kết thúc cùng ký tự trong 0,5 giây.

Một nhãn chậm làm tích chậm/giảm mức phối hợp; không tự hủy hành động của cả đội. Cơ chế bắt buộc có đường cứu hộ hoặc nhịp học phù hợp.

Không dùng người nhanh nhất để âm thầm tăng áp lực cho cả đội. Lớp mạnh sớm giữ nhịp; lớp muộn setup vẫn cần có việc đóng góp ngay.

## 15. Bot hỗ trợ

Bot có lớp, deck, chỉ số và cooldown. AI biết giữ vai, đỡ đòn đã báo, giải trạng thái, dùng buff lúc hợp kích, kiềm công, nạp trận và tiếp quản nhiệm vụ.

- Không biết tương lai chưa báo hoặc phản ứng bằng 0 giây.
- Preset bot công khai về ưu tiên; thông số cần đo khi có runtime.
- Nội dung phổ thông cho một người + bot vượt được ở preset tương ứng.
- Khóa số vị trí/phiên bản encounter lúc vào. Người rớt mạng được bot thay không làm HP boss co giãn tùy ý.
- Bot không có túi loot riêng chuyển hết cho người thật.
- Bot không tạo mastery tiếng Anh, lịch sử từ thuộc hoặc accuracy của người học.
- Không cố tình làm bot ngu để ép tìm người.
- Nếu có bảng cạnh tranh, tách solo/đội bot/đội người và preset; không khóa vật liệu sức mạnh cốt lõi khỏi người solo.

Mất kết nối: giữ vị trí một khoảng chờ rõ rồi bot tiếp quản. Khi người quay lại, đổi điều khiển ở biên hành động; một nhân vật không được cast bằng cả bot lẫn người cùng lúc.

Đây là yêu cầu thiết kế tương lai, chưa có netcode được triển khai trong công việc này.

## 16. Quái, boss và áp lực hợp typing

| Vai quái | Bài toán | Nhiều đường giải |
|---|---|---|
| Bầy áp sát | Số đông/nhiều hướng | AoE, gom, giữ tuyến |
| Giáp dày | Đòn nhỏ kém hiệu quả | Phá giáp, sơ hở, DoT phù hợp |
| Niệm phép | Nguy cơ sau chuẩn bị | Ngắt, phá thế, hộ pháp |
| Bắn xa | Đạn và ưu tiên đích | Chắn, tiêu đạn, tập kích |
| Hỗ trợ địch | Hồi/khiên cho bầy | Đánh nguồn, giải ấn, dồn lực |
| Bộc phá | Nguy cơ tới gần | Đẩy, trói, phá trước, đỡ |
| Phản damage | Thời điểm ngừng công | Kiềm công, giải khiên, chuyển thủ |
| Chiếm chốt | Mục tiêu và không gian | Thân pháp, lệnh đội, phá nhãn |

Kháng nguyên tố làm đổi chiến thuật; tránh phụ bản vô hiệu toàn bộ lớp bằng miễn nhiễm tuyệt đối. Miễn nhiễm ngắn phải có dấu hiệu và cách giải.

### 16.1. Timer phản ứng

Quy đổi đơn giản: T_gõ (giây) = 12 × số ký tự / WPM chuẩn 5 ký tự.

Cửa sổ bắt buộc theo cách giải: né bằng đi thường cần thời gian đọc + đường thoát; phản bằng skill cần đọc + phần từ đang nhập + từ đáp án + animation + độ trễ kênh/đệm. Không lấy timer bấm một nút cho từ 7–10 ký tự; không cân Voice bằng giả định ASR tức thời.

Đòn nhanh có thể cho chuẩn bị thế bảo hộ hoặc tránh bằng vị trí đã báo đủ sớm. Preset dành cho người muốn đứng trận cần đường phòng thủ khả thi; phần thưởng đặc biệt có thể yêu cầu cơ động nhưng không khóa tiến trình nền. Trong đội tránh nhiều đáp án bắt buộc cho một người cùng lúc.

### 16.2. Hồ sơ boss cần có

Mỗi boss: áp lực thường, đòn báo, cơ chế hỗ trợ/giải, cửa sổ dồn lực, luật pet/DoT, bản solo/bot và bản đội. Tăng khó bằng biến thể có lý, không chỉ nhân HP.

Boss đổi từ truy kích sang đấu trường hoặc thủ trận sang phá nhãn chỉ sau khi cơ chế đã được dạy. Không cùng lúc ép đổi vị trí, giải ấn, chọn bộ vị và ra ba lệnh khẩn.

## 17. Hiểu học–luyện–tham ngộ trước khi biến đổi

Hướng dẫn cộng đồng Tale of Immortal năm 2021 mô tả học công pháp bằng thu cầu “ngộ”, phá cầu “ma”; luyện mở các dòng hiệu ứng; tham ngộ điều chỉnh dòng đã mở và có cách giữ lại một số giá trị. Một hướng dẫn Steam cập nhật năm 2025 cũng phân biệt mở dòng bằng kinh nghiệm với tham ngộ lại giá trị. [R11–R12]

Đây là ba nhu cầu: tiếp nhận kiến thức, luyện vận dụng, lựa chọn biến đổi. Không lấy mọi luật và số liệu cũ làm chuẩn phải chép.

### 17.1. Năm tiến trình khác nhau

| Tiến trình | Đo gì? | Nguồn |
|---|---|---|
| Tu vi | Tiến độ cảnh giới RPG | Nội dung chiến đấu/học hợp lệ |
| Tư chất | Phát triển một hướng công pháp | Mốc rèn luyện và tài nguyên mục tiêu |
| Ngộ tính nhân vật | Quyền lựa chọn/hiệu quả tham ngộ trong RPG | Hoạt động và tiến trình có trần |
| Thành thạo công pháp | Mức luyện một kỹ năng RPG | Dùng hợp lệ, phòng tập, bài công pháp |
| Mức thuộc tiếng Anh | Nhớ từ, hiểu nghĩa, ôn lại | Bằng chứng người học tự thực hiện |

Ngộ tính cao không tự chứng minh biết tiếng Anh. Gõ lại chữ hiện sẵn là luyện gõ/tiếp xúc; bài nhớ nghĩa cần tác vụ hồi tưởng phù hợp. Kết quả RPG và kết quả học được báo riêng.

## 18. Tu luyện chọn chữ — nhanh, chính xác, không loạn

**Đây là profile tu luyện chuyên chọn và gõ chữ.** Nhân vật thiền định trong hoạt động này không có nghĩa bị khóa di chuyển ở combat. Ba loại chữ có luật riêng; người chơi phải chọn đúng mục tiêu và hoàn thành đúng hạn. Không dừng thời gian khi bắt đầu gõ. Không dùng thanh lọc làm cách bỏ qua toàn bộ việc tránh Tâm ma.

“Chữ Minh” ở đây là nhóm mảnh từ mang tính minh ngộ, không bắt mọi mục tiêu chỉ hiện chữ “Minh”. Nội dung để gõ vẫn là từ/cụm tiếng Anh của bài học.

### 18.1. Đặc tính của ba loại chữ

| Loại | Hoàn thành đúng hạn | Để hết hạn | Vai trò |
|---|---|---|---|
| **Minh** | Tăng minh điểm/tiến độ bài, có cơ hội đạt mốc lựa chọn đã công bố | Mất cơ hội nhận của mảnh đó, ghi một lần bỏ lỡ | Mục tiêu giá trị, tạo áp lực ưu tiên |
| **Thường** | Tăng tiến độ ổn định/khí lực ở mức thấp hơn | Thường không gây phạt trực tiếp | Giữ nhịp, lựa chọn khi Minh chưa phù hợp |
| **Tâm ma** | Gây bất ổn/tâm ma theo mức đã báo | Trôi đi không phạt trong mode này | Mục tiêu phải tránh gõ hoàn thành |

Mức thưởng/hậu quả được giới thiệu trước. Tâm ma không bí mật giả thành Minh hoặc đổi loại giữa từ ở bản nền. Nếu sau này có biến thể nhận diện khó hơn, cần dạy riêng và kiểm khả năng đọc.

Gõ đúng tiếng Anh của Tâm ma có thể là **đúng thao tác gõ nhưng sai lựa chọn đối tượng**. Màn kết quả tách hai việc này; không sửa nghĩa của từ hoặc nói từ đó là từ tiếng Anh sai.

### 18.2. Hai lớp kỹ năng của người chơi

1. Nhận diện và chọn: thấy trạng thái, ước lượng còn đủ thời gian không, ưu tiên Minh thay vì Tâm ma.
2. Thực hiện: gõ nhanh, chính xác, sửa lỗi trong thời gian còn lại.

Người gõ rất nhanh nhưng lao vào Tâm ma phải chịu hậu quả. Người chính xác nhưng chọn quá chậm có thể bỏ lỡ Minh. Để đạt kết quả tốt cần cả hai.

### 18.3. Bố cục tránh rối

Prototype dùng 3–4 điểm đọc quanh nhân vật thiền định, phân bố theo cung rộng. Từ xuất hiện trong ô/mảnh đủ lớn; vùng nhập chính ổn định ở một chỗ quen thuộc. Không rải hàng chục chữ bay chồng lên nhau.

- Mỗi điểm chỉ có một từ đang hoạt động.
- Khoảng trống giữa từ dựa trên kích thước từ dài nhất của dải bài, không chỉ vị trí tâm.
- Không để đường bay của hai từ cắt nhau lúc cả hai còn nhận input.
- Không cho từ đi sau thân nhân vật, hiệu ứng hoặc bảng chỉ số.
- Tối đa một lớp nguy cơ/nhãn phụ trên mỗi mảnh; không bày nhiều con số li ti.
- Màu + hình viền + icon/nhãn nhận diện. Không dựa riêng vào đỏ/xanh.
- Hình Tâm ma có dấu cảnh báo tĩnh dễ đọc; Minh có dấu sáng riêng. Hiệu ứng chỉ hỗ trợ nhận diện.
- Vị trí khởi đầu có cân bằng vùng nhìn; không dồn toàn Minh vào góc dễ đọc và Tâm ma ra ngoài rìa mãi.

### 18.4. Xuất hiện, chuyển động và thời gian tồn tại

Một mảnh có ba giai đoạn:

1. **Đi vào:** chuyển động ngắn tới điểm đọc, giới thiệu trạng thái. Không tính vào thời gian phản ứng hữu ích nếu chữ chưa đọc được.
2. **Hoạt động:** nhận gõ, đồng hồ rõ; có trôi nhẹ trong vùng nhưng chữ giữ hướng và kích thước ổn định.
3. **Rời đi:** hết hạn hoặc hoàn thành; tan khỏi vùng. Trạng thái kết quả chốt theo đồng hồ logic.

Thời hạn bắt đầu khi từ đã đọc được và nhận input. Hoạt ảnh xuất hiện không được ăn mất phần lớn thời gian. Cần thông báo gần hết hạn bằng viền/thanh thời gian, không nhấp nháy gây khó nhìn.

Chữ Minh có nhịp xuất hiện đáng chú ý, thời gian hữu hạn. Tâm ma có thể tồn tại lâu hơn để buộc người chơi tiếp tục chọn lọc thay vì gõ mọi từ trên màn hình. Chữ thường lấp nhịp nhưng không chiếm hết chú ý.

### 18.5. Ngân sách xuất hiện ban đầu để thử

Các mốc sau giả sử dải từ khoảng 4–7 ký tự. Cần đo lại theo từ vựng, WPM và lỗi thực; không gắn cứng vào cảnh giới.

| Preset | Từ đồng thời | Minh đồng thời | Tâm ma đồng thời | Thời gian Minh đọc được để xử lý, thử |
|---|---:|---:|---:|---|
| Làm quen | 2–3 | 1 | 0–1, sau hướng dẫn | 6–9 giây |
| Tiêu chuẩn | 3–4 | 1, đôi khi 2 | Tối đa 1 trước | 4–7 giây |
| Thử thách | Khoảng 4 trước | 1–2 | 1–2 nếu vẫn đọc được | 3–5 giây |

Không giảm thời gian và tăng mật độ/độ dài/di chuyển cùng một lúc. Muốn tăng độ khó phải biết trục nào đang tăng.

Điểm xuất phát cho một mục tiêu có thể là: thời gian nhận diện + thời gian gõ theo dải độ dài + phần đệm. Độ khó nhanh đến từ đệm ngắn hơn và lựa chọn sát nhau hơn trong phạm vi thử nghiệm, không từ che chữ.

### 18.6. Điều phối để nhanh mà không bất khả thi

- Lệch thời điểm xuất hiện và hết hạn của các chữ Minh. Không buộc hoàn thành hai từ trong một cửa sổ chỉ đủ một từ.
- Có thể có nhiều Minh để người chơi phải chọn, nhưng ngưỡng qua bài không yêu cầu thu tất cả.
- Kịch bản phát sinh cần biết ngân sách ký tự và số cơ hội có thể đạt; không tạo lượt chỉ có Tâm ma rồi chấm người học kém.
- Có một nhịp tăng áp lực rồi một khoảng thở ngắn; tránh mật độ tối đa suốt phiên.
- Không cho bỏ/đổi từ vô hạn để săn từ ngắn; đổi có quy tắc và lịch bài học vẫn giữ.
- Độ dài và độ quen của từ không tiết lộ hoàn toàn loại chữ. Tâm ma không phải lúc nào cũng từ dài nhất để người chơi bỏ qua nhãn.
- Seed và log giúp tái hiện một lượt bị đánh giá là bất công.

### 18.7. Chọn bằng từ, tránh gõ nhầm do tiền tố

Tất cả ba loại tham gia bộ nhận từ. Nếu chỉ cho Minh nhận input thì việc tránh Tâm ma mất ý nghĩa.

Ưu tiên phân biệt sớm tiền tố giữa các loại, đặc biệt Minh/Tâm ma. Không dùng cặp một từ là tiền tố hoàn chỉnh của từ khác. Nếu pool không đủ, giảm số ứng viên hoặc đổi từ bằng bộ lập lịch, không sửa chính tả tiếng Anh để tạo mã.

Khi tiền tố còn trùng, highlight các ứng viên; không tự chốt vào Tâm ma trước khi người chơi phân biệt được. Một khi đã khóa từ, gõ sai không nhảy sang mảnh khác.

Ở bản thử, hậu quả Tâm ma chốt khi hoàn thành từ, để người chơi có thể nhận ra chọn sai và hủy với chi phí thời gian. Nhãn mục tiêu đang nhập phải nổi rõ; không ẩn tới ký tự cuối.

### 18.8. Minh hết hạn khi người chơi đang gõ

Đồng hồ không dừng. Khi hết hạn, mảnh rời thế giới và mất quyền nhận thưởng đúng hạn.

Phần từ đang nhập có thể giữ ở vùng nhập dưới dạng “đã quá hạn” để người học kết thúc hoặc chủ động hủy. Gõ xong vẫn ghi thao tác học phù hợp nhưng không nhận minh điểm của mảnh đã hết hạn.

Trong lúc xử lý từ quá hạn:

- Không tự chuyển ký tự còn lại sang từ mới.
- Không tự chọn Tâm ma vừa xuất hiện.
- Không tự biến một từ thành từ khác.
- Có phản hồi ngắn “quá hạn”, không bật modal ngắt nhịp.
- Khi hoàn thành/hủy, trở về chọn mục tiêu mới.

Đây là phương án input cần thử. Có thể chọn xóa input sau một ranh giới xác nhận rõ, nhưng không được xóa giữa dòng rồi để ký tự đang gõ vô tình kích hoạt đối tượng khác.

### 18.9. Chấm kết quả

| Chỉ số | Định nghĩa |
|---|---|
| Chính xác gõ | Ký tự đúng/sai theo chính sách học |
| Chọn lọc | Minh/thường được chọn, Tâm ma hoàn thành nhầm |
| Đúng hạn | Mảnh hoàn tất trước deadline, mảnh bỏ lỡ |
| Hiệu quả tu luyện | Tiến độ/khí lực/minh điểm và bất ổn của phiên |
| Kết quả nhớ từ | Chỉ ghi nếu có tác vụ kiểm tra nhớ phù hợp |

Không trộn việc bỏ lỡ Minh vào accuracy ký tự. Không cho một lần gõ Tâm ma xóa toàn bộ lịch sử học.

Điểm RPG thử có thể dùng các trọng số khác nhau cho Minh/thường, phạt Tâm ma theo bất ổn và giữ tiến độ một phần. Chỉ chốt số sau khi biết tỷ lệ cơ hội đạt được; không tự đặt ngưỡng 100% thu Minh.

Chữ thường giữ nhịp và cho tiến độ nền, nhưng không thay hoàn toàn nguồn minh điểm của chữ Minh. Các mốc tham ngộ cao cần lượng Minh khả thi của preset; spam toàn chữ thường không trở thành đường tối ưu để bỏ qua chọn lọc. Phiên chưa đạt mốc cao vẫn giữ phần học/tiến độ nền, tránh bắt người mới làm lại trắng.

### 18.10. Tăng ngộ tính, học công pháp và tỷ lệ thành công

Minh điểm chủ yếu là điểm của phiên. Chạm mốc giúp tiến bài, nhận tài nguyên tham ngộ hoặc tiến tới một mốc ngộ tính có trần. Không mỗi từ lại tăng ngộ tính vĩnh viễn vô hạn.

Ngộ tính RPG có thể mở thêm lựa chọn nhánh/giữ kết quả hoặc giảm hậu quả bất ổn trong giới hạn. Nó không tự gõ hộ, tự thu Minh, biến từ chưa biết thành đã thuộc hay làm Tâm ma vô hại hoàn toàn.

Học kỹ năng nền ưu tiên tích tiến độ chắc chắn. Nếu dùng xác suất cho phần thưởng phụ/đột phá, hiển thị rõ giới hạn và bảo đảm tiến độ; không bắt người học gõ tốt rồi vẫn mất sách hiếm bởi một lần tung số.

### 18.11. Phiên minh họa

Một phiên 60–90 giây để thử:

1. Nhịp đầu một Minh + một thường; dạy chọn và deadline.
2. Tâm ma xuất hiện cùng nhãn rõ, tồn tại qua vài lựa chọn.
3. Minh thứ hai xuất hiện lệch nhịp: người chơi quyết định bỏ thường để kịp Minh hay hoàn tất từ sắp xong.
4. Một đoạn tăng áp lực ngắn, sau đó giảm mật độ.
5. Kết phiên: báo gõ, chọn lọc, đúng hạn và tiến độ riêng; mở một lựa chọn công pháp khi đủ mốc.

Không ép minigame dài ở mọi lần tăng chỉ số. Dùng cho học công pháp/mốc tham ngộ và thử thách tự chọn, xen đường ôn ngắn.

### 18.12. Pause, mất focus và công bằng thời gian

Chế độ học có thể cho tạm dừng rõ ràng; không tiếp tục làm chữ hết hạn âm thầm khi người chơi ra khỏi tab. Màn pause che vùng lựa chọn và tạm ngừng đồng hồ, khi trở lại có đếm nhịp an toàn. Không cho xem từ trong pause rồi bấm tiếp để hưởng thành tích tốc độ như một lượt không pause.

Nếu có xếp hạng tốc độ, đánh dấu lượt đã pause hoặc dùng quy tắc riêng công khai. Quyền tạm dừng buổi học vẫn giữ. “Không dừng khi bắt đầu gõ” khác với thao tác tạm dừng có chủ đích của toàn phiên.

## 19. Những hoạt động tu luyện khác

Đây là ngoài combat, không phải thêm cơ chế chiến đấu thứ sáu.

| Hoạt động | Thao tác và quyết định | Kết quả RPG | Điểm khác |
|---|---|---|---|
| Dẫn khí nhập mạch | Gõ chuỗi ngắn, chọn tuyến công/thủ trước đoạn | Tư chất/nhánh | Chọn đường, dùng khí hữu hạn |
| Thiên thư tái cấu | Đọc ví dụ, gõ theo tác vụ đã học, chọn biến thể | Mở biến chiêu | Ghép cấu trúc công pháp |
| Linh thú đồng tâm | Gõ lệnh/từ phù hợp bài tình huống | Khế ước, lệnh mới | Phối hợp chủ–thú |
| Đột phá tâm cảnh | Ôn nhóm từ qua các pha, tích nhiều phiên | Mốc cảnh giới | Giữ tiến độ, không một lần tốc độ quyết định hết |
| Tham ngộ biến chiêu | Ôn rồi chọn giữ/đổi tác dụng đã preview | Nhánh hoặc dòng kỹ năng | Đánh đổi rõ, không reroll vô định |
| Phòng luyện | Thử deck và thay một nhánh, quan sát tác dụng | Hiểu combo, mastery RPG có giới hạn | Phản hồi thay vì áp lực thất bại |

### 19.1. Ngôn ngữ phải đúng

Nếu yêu cầu nhớ nghĩa, dùng dữ liệu kiểm chứng và ngữ cảnh xử lý đa nghĩa. Không chấm một nghĩa đúng thành sai vì câu không chỉ rõ. Nếu chỉ gõ lại từ, ghi là luyện gõ/tiếp xúc.

IPA, nghĩa Việt và phát âm phù hợp lúc giới thiệu/ôn có gợi ý. Trong bài hồi tưởng, mở gợi ý bằng thao tác rõ, ghi đúng mức hỗ trợ và không làm nhục người học.

Kho luyện vẫn từ chương trình tiếng Anh của nền tảng, không chỉ tên skill hoặc danh từ tu tiên.

### 19.2. Không biến tu luyện thành checklist

Dùng chung dữ liệu từ và lịch ôn. Một số hoạt động là lựa chọn thay thế để đạt mục tiêu, không bắt làm hết mỗi ngày. Không tạo thêm sáu loại tiền và shop chỉ để phục vụ sáu minigame.

## 20. Quy trình tạo bản sắc riêng

Mỗi hệ thống cần trả lời:

1. Nhu cầu người chơi là gì?
2. Lựa chọn hấp dẫn ở game tham chiếu là gì?
3. Khi hai tay đang gõ, lựa chọn đó còn hoạt động không?
4. Dự án thay luật, phần thưởng hoặc cấu trúc quyết định ở đâu?
5. Việc học tiếng Anh có vai trò thật nào?
6. Bỏ tên tu tiên/VFX đi, cơ chế vẫn có đặc điểm riêng nào?

| Nguyên tắc tham chiếu | Thiết kế riêng |
|---|---|
| Thu/ngăn vật thể khi học | Ba nhóm từ, deadline, chọn lọc, input chống chuyển nhầm, lịch ôn |
| Luyện mở hiệu ứng | Bài ứng dụng và lựa chọn biến chiêu công/thủ |
| Một chỉ số ngộ tính | Quyền chọn tham ngộ; tách bằng chứng biết tiếng Anh |
| Đội đánh boss | Trận nhãn, từ cá nhân, nạp bất đồng bộ, bot bù |
| Né bằng vị trí | Thân pháp gõ chọn điểm, timer theo chi phí nhập |
| Pet tự đánh | Khế ước, lệnh, ngân sách sở hữu và tương thích nhiều mode |

Tạo riêng mỹ thuật, hoạt ảnh, âm thanh, bố cục, truyện và nhân vật hư cấu. Nhân vật thần thoại truyền thống cũng dùng diễn giải hình ảnh riêng; không lấy tạo hình đặc trưng từ sản phẩm hiện đại.

Đây là quy trình khác biệt hóa sản phẩm, không phải bảo đảm pháp lý về bản quyền. Tài liệu không dùng việc “đổi màu/đổi tên” làm bằng chứng đủ khác.

## 21. Giới hạn chỉ số và tương tác

| Hệ | Luật thử | Ngăn lỗi |
|---|---|---|
| Damage | Tách bucket nền/kỹ năng/mục tiêu/buff; đo tổng tương tác | Mọi % nhân chéo vô hạn |
| Cooldown | Tổng giảm thử tối đa 30%, skill thường có sàn riêng | Hộ pháp/ulti về gần 0 CD |
| Tốc đánh auto | Trần và quota proc theo chủ | Nhiều pet sinh vô hạn hit phụ |
| Chí mạng | Trần xác suất/hệ số theo giai đoạn, đo đầu tư tương đương | Một đường đồ thành đáp án duy nhất |
| Giảm damage | Ghép theo bucket rõ, không bất tử thường trực | Hộ + hồi không thể thua |
| Khiên | Trần theo đối tượng, luật làm mới/ưu tiên | Tích khiên vô hạn trước boss |
| Hút máu | Damage hợp lệ và quota chung chủ–pet | Multi-hit sinh hồi vượt ngân sách |
| Khống chế | Boss phá thế, kháng tạm sau break | Khóa boss mãi |
| Tái hiện | Danh sách cho phép, hệ số giảm, không tự lặp | Sao chép ulti/hoàn CD đệ quy |
| Hợp trận | Quota nguồn và ngân sách encounter | Skill trận tự nạp lại chính nó |

Các trần là quy tắc dữ liệu công khai, không kéo ngầm theo việc người chơi mạnh lên. Các nhóm khác nhau vẫn phải kiểm tương tác chéo; giới hạn từng nhóm riêng chưa đủ.

### 21.1. Trang bị

Mỗi nhánh có ít nhất hai hướng đồ khả thi để thử. Đồ hỗ trợ tăng hiệu quả bảo hộ/giải, không chỉ damage. Đồ pet tác động trong phần ngân sách pet, không cộng lại toàn bộ công kích chủ đã buff.

Bộ cơ bản có đường nhận chắc chắn. Nội dung phổ thông không yêu cầu roll hoàn hảo. Ngoại trang/VFX tách sức mạnh. Tu vi/cảnh giới không tự nâng mức thuộc từ.

## 22. Công bằng typing và phần thưởng

### 22.1. Chi phí từ

Từ 4 và 9 ký tự có chi phí khác nhau. Không gắn cố định từ dài vào lớp muộn rồi coi đó là “cân bằng”. Bộ từ các ô có phân bố chi phí phù hợp preset; ô phòng thủ không luôn nhận từ khó nhất.

Hành động liên tục có thể tích năng lượng theo ký tự hợp lệ của từ đã hoàn thành, có cap và không đếm xóa gõ lại. Hệ số bù effort cần thử; không tự nhân mọi buff theo độ dài từ.

Tu luyện chọn chữ có deadline phụ thuộc dải độ dài và preset. Cùng seed không có nghĩa cùng độ khó nếu thay toàn bộ từ 4 ký tự bằng 10 ký tự.

### 22.2. Preset

Tách độ khó ngôn ngữ và độ khó RPG. Người mới có mật độ/nguy cơ phù hợp. Trong đội, chốt preset trước trận, từ cá nhân nằm trong dải công khai.

Nếu có cạnh tranh, dùng quy tắc/bộ từ tương đương và tách preset. Không so trực tiếp bài từ mới của người 25 WPM với từ thuộc sẵn của người 90 WPM.

Bot, pet và auto attack không tạo accuracy hoặc lịch sử nhớ từ thay người học. Nhận giọng nói và chính xác gõ là hai chỉ số khác; ASR nhận ra từ không tự chứng minh phát âm đạt chuẩn.

Voice/Hybrid cần thử riêng độ trễ, tiếng ồn và kết quả tới muộn. Nếu đưa voice vào tu luyện Minh–Tâm ma, dùng profile thời hạn/phản hồi riêng; không phạt tâm ma chỉ vì kết quả nhận tạm hoặc không chắc. Các lượt có kênh/preset khác nhau không xếp thẳng chung một bảng tốc độ.

### 22.3. Đóng góp support

Ghi damage trực tiếp, damage tăng thêm hợp lệ nhờ buff, khiên thực sự tiêu thụ, hồi HP đã mất, giải trạng thái hữu ích, phá niệm và nhiệm vụ trận.

Thưởng phổ thông dựa hoàn thành và tham gia hữu ích, tránh last-hit. Không tính hồi khi đầy máu, khiên hết hạn chưa dùng, buff trùng ID không có tác dụng như đóng góp mới.

Muốn ước lượng damage tăng nhờ buff trên một hit, giữ nguyên roll crit/trạng thái rồi tính có và không có buff. Đây là cách phân bổ credit sự kiện; không chứng minh toàn bộ trận thiếu người buff sẽ diễn ra giống thế.

## 23. Mô hình phân tích đã chạy

Mô hình Python ở phụ lục từ V2 kiểm đường tăng trưởng, chồng buff, số pet, cooldown và chi phí gõ. V2.2 giữ kết quả này làm tham chiếu cũ; chưa mô phỏng di chuyển tự do, uptime cận/tầm xa, loot, voice hoặc rendering 2D. Không có game runtime, AI địch, collision, mạng hay dữ liệu người chơi; không thể kết luận cân bằng/vui hoặc FPS.

### 23.1. Ví dụ sai và cách sửa

Giả sử support gây 100 damage như lớp công, mỗi support lại nhân cả đội 20%. Đội 7 support đạt 700 × 1,2^7 = 2.508,23, gấp 3,58 lần đội 7 công không buff. Đây là thiết kế thử cố tình sai để kiểm lỗi, không phải dữ liệu game tham chiếu.

Mô hình sửa: lớp công 100 damage; support focus đội 75 trước aura; mỗi họ buff công 10%, cùng họ lấy mạnh nhất, tổng tối đa 18%. Chỉ có hai họ mẫu trong mô hình. Áp một lần lên tổng output sở hữu.

Focus solo dùng ngân sách Tự Cường riêng; không lấy 75 làm chỉ số bắt buộc cho support solo. Các hệ số này chỉ phục vụ phép kiểm một trục damage, không phải chốt trần mọi loại buff của game.

| Vị trí | Toàn công | Một support | Cao nhất trong mô hình | Số support tại điểm đó | Tăng so toàn công |
|---|---:|---:|---:|---:|---:|
| 2 | 200 | 192.50 | 200.00 | 0 | 0.00% |
| 3 | 300 | 302.50 | 302.50 | 1 | 0.83% |
| 4 | 400 | 412.50 | 413.00 | 2 | 3.25% |
| 5 | 500 | 522.50 | 531.00 | 2 | 6.20% |
| 7 | 700 | 742.50 | 767.00 | 2 | 9.57% |

Trong mô hình damage này, đội 2 toàn công đánh mạnh hơn đội 2 có support. Mô hình chưa tính sống sót, giải đòn và thời gian công kích được duy trì. Không suy ra support không hữu dụng ở đội 2; phải thử encounter thật.

Đội 7 có hai support trùng họ đạt 715; hai họ khác nhau đạt 767. Đội toàn support đạt 619,5. Hiện tượng áp đảo do nhân aura đã được loại khỏi công thức mẫu; điều đó không chứng minh 10%/18% là mức cân bằng đúng.

### 23.2. Những phép kiểm khác

- Ngân sách pet 70 chia cho 1/2/3/4 con rồi buff 18% một lần: đều 82,6.
- CD 8 giây với trần giảm 30% còn 5,6; nhập thêm 100% giảm không đưa nó về 0.
- Các hồ sơ có sàn/trần, có giao nhau; lớp sớm còn 97 cuối, lớp muộn đầu là 92 trong bảng mục tiêu.
- Bộ sáu từ minh họa không trùng toàn từ và không có tiền tố hoàn chỉnh.

| WPM | Cửa sổ mẫu tối thiểu |
|---|---:|
| 25 | 6.80 giây |
| 40 | 5.00 giây |
| 60 | 4.00 giây |
| 90 | 3.33 giây |

Cửa sổ mẫu gồm đọc 1 giây + 4 ký tự đang dở + 6 ký tự phản ứng + đệm 1 giây. Chưa tính nhớ từ mới, lỗi, animation hoặc mạng, vì vậy không dùng làm timer chung.

### 23.3. Kiểm lịch chữ Minh

Lịch thử bốn chữ 5/6/5/7 ký tự, xuất hiện tại giây 0/3/6/9, hết hạn tại 6/10/13/17. Tính 25 WPM và 0,6 giây chọn mỗi chữ, không lỗi: có một thứ tự hoàn thành kịp cả bốn.

Lịch thử khác: hai chữ 7 ký tự cùng xuất hiện ở giây 0, cùng hết hạn giây 5. Với 40 WPM và 0,6 giây chọn mỗi chữ, hoàn thành lần lượt tại 2,7 và 5,4 giây. Không thể đòi lấy cả hai trong giả định đó.

Kết luận thiết kế là phải kiểm cơ hội và ngưỡng qua bài; không yêu cầu mọi Minh đều được thu. Thuật toán thử là một lịch chọn sớm theo deadline trong các ví dụ, không là bộ chứng minh khả thi tối ưu cho mọi lịch phức tạp.

Đã qua 38 điều kiện nhất quán trong mô hình. Đây không phải 38 test của một game đã hoàn thiện.

Một số điều kiện chỉ xác nhận công thức thực hiện đúng giả định. Chưa kiểm được input hết hạn, độ đọc UI hay AI vì chưa triển khai runtime.

## 24. Tự review và các sửa đổi

| Mã | Vấn đề | Mức | Sửa trong V2 | Còn cần |
|---|---|---|---|---|
| RV01 | Đứng trận bắt buộc hoặc chỉ được nhảy điểm | Cao | Đi tự do chuột/phím là nền; 5 phương án là mở rộng | Prototype di chuyển/range |
| RV02 | Chỉ đổi quả cầu thành chữ | Cao | Ba trạng thái, deadline, chọn lọc, học tách RPG | Test lựa chọn và học |
| RV03 | Support solo thiếu damage/việc gõ | Cao | Tự Cường, pháp khí nền, ô liên tục | Đo vượt ải |
| RV04 | Aura nhân theo số support | Nghiêm trọng | ID/bucket, quota và chia ngân sách | Encounter sống sót và tương tác |
| RV05 | Mỗi pet có toàn bộ damage/quota | Nghiêm trọng | Ngân sách theo chủ | AI/collision |
| RV06 | Buff chủ và pet nhận hai lần | Nghiêm trọng | Một pipeline kế thừa | Test runtime |
| RV07 | Lớp muộn thiếu nửa kit quá lâu | Cao | Kit nền, mảnh ghép chắc chắn | Test người mới |
| RV08 | Lớp sớm hết giá trị cuối | Cao | Giữ ít setup/burst và nâng cấp | Test endgame |
| RV09 | Đi thường chiếm mất ô skill | Cao | Chuột/phím di chuyển tách deck; chỉ thân pháp/lệnh đặc biệt dùng ô | Đo deck theo vai |
| RV10 | Parry nhanh hơn thời gian gõ | Nghiêm trọng | Báo sớm, thế thủ có thời lượng | Lỗi gõ/mạng thực |
| RV11 | Nhãn trận khóa người tại tọa độ hoặc tranh chỗ | Cao | Nhãn là vai, đi lại tự do; liên kết vùng có luật | Multiplayer/bot |
| RV12 | Một người dừng cả đội | Nghiêm trọng | Solo pause, đội phase chung riêng | Đồng bộ thời gian |
| RV13 | Pause nhưng pet/CD tiếp tục | Nghiêm trọng | Cùng đồng hồ combat | Runtime |
| RV14 | Support thua credit vì ít last-hit | Cao | Credit hữu ích/thưởng hoàn thành | Chống đếm trùng |
| RV15 | Bot tạo mastery/nhân loot | Cao | Tách danh tính và thưởng | Runtime |
| RV16 | Đang gõ làm Minh không hết hạn | Cao | Đồng hồ tiếp tục chạy | Test đúng hạn |
| RV17 | Chữ hết hạn làm ký tự rơi sang Tâm ma | Nghiêm trọng | Giữ input quá hạn/hủy có chủ đích | State machine nhập thực |
| RV18 | Tất cả loại nhận input trừ Tâm ma | Cao | Tâm ma vẫn có thể bị chọn/gõ nhầm | Test chọn lọc |
| RV19 | Hai Minh hết hạn cùng lúc, ngưỡng bắt lấy cả | Cao | Lệch lịch và kiểm ngưỡng khả thi | Scheduler nhiều seed |
| RV20 | Rối chữ do chồng, bay sau FX | Cao | Vùng đọc, giới hạn số, font/spacing | Màn hình/layout thật |
| RV21 | Tâm ma bị ghi thành tiếng Anh sai | Cao | Tách gõ, chọn lọc và deadline | Test hiểu phản hồi |
| RV22 | Ngộ tính tự biến thành biết từ | Cao | Năm tiến trình tách riêng | Dữ liệu học |
| RV23 | Cơ quan/trận vô dụng khi map di chuyển | Cao | Theo chủ/phương tiện, chuyển mạch | Test từng kit |
| RV24 | Dồn cả 5 cơ chế vào một trận | Cao | Một chính + tối đa một phụ ở bản thử | Playtest |
| RV25 | Bảng số đẹp được gọi là cân bằng | Cao | Ghi giả định/giới hạn; kiểm dữ liệu thật | Chưa thể xác nhận |
| RV26 | Spam chữ thường thay hết Minh | Cao | Tách tiến độ nền và mốc minh điểm khả thi | Test chiến lược chọn chữ |
| RV27 | Đổi vai pet đang CD khiến không thể kiềm công | Cao | Quyền dừng an toàn tách CD đổi vai | Boss phản damage |
| RV28 | Pause xem từ để lấy thành tích tốc độ | Vừa | Che vùng đọc, đánh dấu pause, giữ quyền nghỉ học | Quy tắc phiên/xếp hạng |
| RV29 | Thêm di chuyển làm mất bản sắc support/pet | Cao | Đi thường không lấy ô; pet/trận theo chủ/chuyển mạch | Prototype từng lớp |
| RV30 | WASD vừa nhập chữ vừa đi | Nghiêm trọng | Trạng thái rõ, mũi tên/chuột thay thế, giữ từ dở | Input thực |
| RV31 | Voice và gõ cùng cast một chiêu | Nghiêm trọng | Kênh sở hữu, ID hành động, bỏ kết quả cũ/partial | ASR/Hybrid |
| RV32 | Ra/vào trận farm khiên/buff | Cao | ID liên tục, đệm/decay có cap, không nạp miễn phí | Test biên vùng |
| RV33 | Đứng trận mất đồ, người chạy giành hết loot | Cao | Hút gần, thu dọn đồ thường, loot cá nhân, bí mật tự chọn | Reward/playtest |
| RV34 | Cận chiến mất cast ngoài tầm, ranged thả diều vượt trội | Cao | Range/đường nhìn rõ, không tiêu sai, đo uptime và boss | Encounter thực |
| RV35 | Giả định 2D tự động nhẹ | Cao | Đo alpha/filter/texture/frame time, ngân sách theo cảnh | Profiler |
| RV36 | VFX giả 3D che vùng đánh thật | Cao | Neo mặt đất, depth, telegraph tách hình trang trí | Visual/collision |
| RV37 | TTS/BGM bị nhận thành câu trả lời | Nghiêm trọng | Phân nguồn/kênh, điều phối mic và test âm thanh thực | Voice runtime |

### 24.1. Các đánh đổi chưa chốt

- Di chuyển chuột/phím đã là nền. Cần giảm việc đổi tay/trạng thái khi Typing; Voice có lợi thế điều khiển liên tục nên phải đo riêng.
- Hành tiến tạo không gian đẹp nhưng cần quyết định tuyến thật.
- Phá thế cần nhiều đường giải, tránh một skill phản xử lý mọi thứ.
- Lập chiêu có chiều sâu nhưng thay đổi nhịp typing liên tục.
- Điều quân hợp support/pet nhưng dễ quá tải.
- Tâm ma phải nhận ra được nhưng không quá tách biệt để lựa chọn thành tự động.
- Lớp muộn cần đỉnh đủ hấp dẫn, vẫn không áp đảo mọi nội dung. Bảng 92–112 chỉ là điểm thử.

## 25. Kế hoạch kiểm chứng

### 25.1. Ma trận nội dung

| Trục | Mẫu |
|---|---|
| Phát triển | K0/K1/K3/K5/K6, cùng công sức và đồ tương đương |
| Vai | Công sớm, công setup, buff, hồi/hộ, pet |
| Hình thức | Solo thuần, người + bot, đội 2/3; 7 sau |
| Lối chơi | Đứng trong trận, chạy trong trận, ra ngoài, quay lại; cận/tầm xa |
| Đầu vào | Typing, Voice, Hybrid; chuột, mũi tên, WASD và đổi focus |
| Ngôn ngữ | Từ quen, từ mới, từ đến hạn; tách khi so |
| Gõ | Chậm/vừa/nhanh, có lỗi tự nhiên |
| Encounter | Bầy, giáp, niệm, boss, phản damage, đổi phase |
| Mode | Thủ trận và từng cơ chế được người dùng chọn |
| Tu luyện | Ba loại chữ, nhiều lịch, input quá hạn, ranh giới timer |
| Thiết bị | Màn hình, font, bàn phím/layout, mic và cấu hình mục tiêu |
| Hình ảnh | Scene 2D, depth, VFX/đồ rơi dày, nhiều người và các quality |

### 25.2. Chỉ số

1. Qua ải, thời gian, nguyên nhân thua.
2. Damage hữu dụng, overkill, setup và chuyển đích.
3. Hồi/hộ/giải hữu ích, cơ chế và thời gian sống thêm.
4. Thời gian gõ/nói, đổi tay/đổi trạng thái, đi lại, nhặt đồ và bị buộc chờ.
5. Cast nhầm, mất ký tự, đổi từ/ý nghĩa giữa lúc gõ.
6. Kết quả học thực, mức gợi ý, lịch ôn sau.
7. Pet/bot mắc đường, bỏ lệnh, dùng sai buff.
8. Minh bỏ lỡ do quyết định/gõ chậm hay do bị che/không đủ cơ hội.
9. Chọn Tâm ma do đọc sai, không nhìn nhãn, hay lỗi bộ phân giải.
10. Người chơi có hiểu lựa chọn của mình làm thay đổi kết quả không.

### 25.3. Cửa kiểm đề xuất

- Mọi lớp có đường vượt nội dung phổ thông; thiếu công cụ bắt buộc là lỗi thiết kế.
- Chênh thời gian kéo dài khoảng trên 15–20% giữa build cùng vai/đầu tư cần điều tra cùng an toàn và độ khó thao tác; không tự nerf theo một chỉ số.
- Không có đoạn toàn bộ ô đều khóa buộc chờ.
- Tốc độ ngôn ngữ và áp lực RPG được công bố, không tăng ngầm giữa trận.
- Tu luyện không yêu cầu lịch hành động vượt ngân sách ký tự của preset để đạt kết quả cơ bản.
- Chữ không chồng, nhảy hay bị che; đúng/sai/loại/đúng hạn phân biệt được.
- Tâm ma không ép đọc hoặc nhập nội dung sai ngôn ngữ; độ nguy hiểm thuộc luật RPG.
- Hỗ trợ không bắt buộc một lớp cụ thể cho mọi đội; các lớp có cách thay thế chức năng.
- Số ally/pet/VFX tăng không làm mất input.

### 25.4. Ca lạm dụng và ranh giới

Buff trùng ID; nhiều bucket; buff + tốc đánh + CDR; toàn support; toàn pet; pet + hút máu; hoàn CD + tái hiện; đội 7; spam từ dễ; hủy/gõ lại; pre-buff; đổi focus; bot tiếp quản lúc đang nhập; lag khi cast; boss chết giữa queue; pause khi DoT tick; đổi mode lúc cơ quan đã đặt.

Tu luyện: Minh hết hạn sát ký tự cuối; khác biệt thời điểm hiển thị/logic; trùng tiền tố khác loại; Tâm ma xuất hiện khi từ cũ quá hạn; hai Minh cùng deadline; đổi font/zoom; mất focus tab; nhấn giữ phím; gõ dấu hoặc layout ngoài dải hỗ trợ.

Di chuyển/voice/2D: giữ WASD rồi chuyển nhập; click UI xuyên nền; đi và cast ngoài tầm; quay lại trận liên tiếp; nhặt cùng đồ bằng người/pet; ASR trễ sau đổi mode; cùng từ qua hai kênh; TTS lọt mic; foreground che điểm đến; 7 người ulti và nhiều nhãn loot; hạ quality không đổi hit logic.

## 26. Mỹ thuật 2D có chiều sâu, kỹ năng và hiệu năng

### 26.1. Hướng hình ảnh đã xác định

Dùng nền, nhân vật, quái, pet, đồ rơi và kỹ năng theo hướng 2D. “2D có chiều sâu” hoặc “2.5D” trong tài liệu chỉ cách trình bày lớp/khối/ánh sáng; không mặc định phải dùng cảnh và nhân vật 3D trong runtime.

Ảnh U02 người dùng gửi cho thấy kiếm vàng có đường vòng lớn, vùng băng dưới đất, xoáy gió và vật phẩm rơi cùng nhiều kẻ địch. Đây là tham chiếu về cảm giác và bố cục. Một ảnh không xác nhận chính xác engine, shader hoặc toàn bộ cách sản xuất asset của game tham chiếu.

Mục tiêu riêng của dự án: hình tu tiên có khối, skill khác biệt, đường tác động rõ, nhiều quái nhưng vùng chữ học luôn sạch.

### 26.2. Góc nhìn, map và độ sâu

Camera trên chéo 3/4 cố định để thấy mặt đất và dáng nhân vật; thử độ nghiêng/zoom bằng scene mẫu. Không cần camera xoay tự do. Di chuyển chuột/phím dùng cùng mặt phẳng gameplay 2D.

| Lớp | Cách làm đề xuất | Điều cần kiểm |
|---|---|---|
| Nền xa | Tranh nền/parallax nhẹ ngoài vùng tương tác | Không làm người học chóng mặt |
| Mặt đất | Tile hoặc mảnh nền có phối cảnh vẽ sẵn | Điểm đến, tường và collision đúng hình |
| Bóng | Bóng tiếp xúc và bóng bay đơn giản | Nhân vật/đạn có cảm giác chạm đất/độ cao |
| Nhân vật, quái | Sprite/animation 2D, sắp lớp theo chân | Đi sau cây/đá đúng; không bị che khi cần đọc |
| Chiêu sát đất | Vòng elip, vết nứt, băng/rễ/trận văn | Vùng tác động thật đọc được |
| Chiêu trên cao | Độ lệch hình so với điểm mặt đất, bóng và lớp trước–sau | Không gây hiểu nhầm hitbox |
| Foreground | Ít vật che phía trước, giảm alpha khi che người | Không giấu nhân vật, loot quan trọng hoặc cảnh báo |
| HUD | Tách camera, chữ/IPA/nghĩa ổn định | Không quay, rung hoặc mờ theo VFX |

Nền đẹp vẫn cần dữ liệu đi được/collision riêng. Không coi toàn bộ bức tranh là mặt phẳng có thể click tới mọi điểm.

### 26.3. Nhân vật và animation 2D

Bản thử đối chiếu 4 hướng chính với 8 hướng cho nhân vật chủ, chọn theo chất lượng nhìn và chi phí asset. Quái thường có thể dùng ít hướng hơn nếu vẫn đọc được hướng công kích; boss có animation riêng đủ báo đòn.

Không xoay cả hình người nằm nghiêng như một tấm bìa chỉ để quay mặt 360 độ. Vũ khí/VFX có thể xoay theo góc, thân người chuyển sprite/pose thích hợp. Hướng đánh và hitbox không giả vờ khớp khi hình thực tế chỉ quay sai.

Hai hướng sản xuất có thể thử: spritesheet vẽ frame và rig 2D với các bộ phận. Không bắt mọi asset dùng cùng kỹ thuật. Trang phục nhiều bộ cần đo chi phí đồng bộ pose; ghép bộ phận không được làm áo/tóc/vũ khí lệch khi chạy/cast. Lật trái–phải chỉ khi thiết kế cho phép, tránh đảo sai chi tiết bất đối xứng.

Các trạng thái nền: đứng, chạy, cast ngắn, cast nặng, nhận đòn, bị phá thế, thắng/thua. Auto attack dùng chuyển động gọn không che nhịp skill chính.

### 26.4. Tạo ảo giác khối bằng 2D

- Vẽ sáng/tối và mặt vật thể nhất quán, không chỉ thêm glow.
- Vòng kiếm/trận chia phần sau lưng và trước người; xoay quỹ đạo elip tạo cảm giác bao quanh.
- Kiếm/linh châu bay có bóng/điểm neo mặt đất, biến thiên scale có kiểm soát theo quỹ đạo giả độ sâu.
- Vết chém có lõi rõ, đường đi, độ rộng và điểm kết thúc; quỹ đạo cong có gia tốc để thấy lực.
- Va chạm phát sáng cục bộ, vỡ mảnh/rạn giáp và phản ứng quái đúng thời điểm.
- Hỏa có lõi/tàn, băng có mặt tinh thể/vỡ, lôi có nhánh/xung, mộc có nảy/siết/nở. Không chỉ đổi màu một sprite.
- Ánh sáng 2D/normal map có thể thử chọn lọc cho hero/boss/đòn lớn; không cần mọi con quái có đèn và bóng động riêng. Tài liệu Godot mô tả khả năng tăng cảm giác sâu bằng ánh sáng/bóng 2D; đây là nguồn nguyên tắc, chưa chọn Godot làm engine. [R14]

Không làm hình tăng độ cao mà người chơi không còn biết vùng nào bị đánh trên đất. Cảnh báo và damage dùng dữ liệu gameplay 2D có thẩm quyền.

### 26.5. Ngữ pháp VFX theo trường phái

| Hệ | Hình dạng/nhịp đặc trưng | Cảm giác va chạm |
|---|---|---|
| Kiếm | Phi kiếm, đường thẳng, cung sạch, thu hồi | Xuyên/cắt, điểm lóe gọn |
| Đao/thương | Cung nặng hoặc tuyến đâm, vệt có quán tính | Chấn lực, phá giáp theo hướng |
| Hỏa | Tụ lõi, cuộn lửa, bùng theo đợt, tàn bay | Nổ có nhịp, đẩy và cháy |
| Băng/thủy | Kết tinh, dòng chảy, vòng elip, vỡ mặt | Rạn, vỡ hoặc cuốn |
| Lôi | Nút dẫn, nhánh nhanh, xung ngắn | Giòn, rung cục bộ |
| Mộc/y | Hạt, rễ, dây, hoa nở | Sinh trưởng, siết và hộ sinh |
| Thể/thổ | Khối, nứt, bụi và sóng nền | Nặng, bám mặt đất |
| Phù/âm/trận | Mực/ấn, sóng, đường mạch có cấu trúc | Khóa, giải, cộng hưởng |
| Pet/khôi lỗi | Silhouette, vồ/bắn, khớp chuyển động | Đòn có nguồn dễ nhận biết |

Bảng là chữ ký hình ảnh, không giới hạn chỉ chín nhóm. Các trường phái nâng cao phải có cấu trúc hình riêng trước khi sản xuất hàng loạt.

### 26.6. Một kỹ năng hoàn chỉnh

1. Chuẩn bị ngắn: pose/tụ sáng cho biết chiêu đã nhận.
2. Hình chính: kiếm, linh ảnh, luồng hoặc vùng có silhouette.
3. Đường đi: vệt và vật dẫn, không phủ cả màn.
4. Va chạm: lóe/nứt/nổ rõ tại đúng đích.
5. Phản ứng: quái giật, khựng, vỡ giáp hoặc ngã theo gameplay.
6. Dư âm: tàn/hoa/băng/mảnh ngắn có cap.
7. Âm thanh/số damage: xác nhận lực mà không lấn phát âm.

Ví dụ Vạn Kiếm: kiếm mở phần sau nhân vật → từng lớp lao qua không gian → ba đợt hội vào vùng đích → một điểm kết thúc mạnh → kiếm/tàn thu gọn. Không cần mỗi kiếm là model 3D hoặc collider riêng. Số hit/damage được xác định bằng luật skill, số kiếm phụ trong VFX có thể giảm theo quality.

Đại trận/ultimate không khóa input để chiếu phim. CGI/cut-in nếu có là hình/animation 2D ngắn có tùy chọn giảm; không là yêu cầu video nặng cho mọi lần cast.

### 26.7. Hiệu năng: 2D vẫn cần đo

Tài liệu PixiJS khuyến nghị spritesheet và lưu ý chi phí filter, mask, thay blend mode, cập nhật text. Điều này củng cố việc đặt ngân sách render; chưa phải quyết định chọn framework và không chứng minh FPS của dự án. [R13]

Ngân sách cần theo dõi riêng: số đối tượng logic, số đối tượng vẽ, diện tích trong suốt chồng nhau, số texture đang resident, draw call, CPU/GPU frame time và độ trễ input/voice.

Một atlas 4096 × 4096 giả sử RGBA8 không nén cần 64 MiB cho một ảnh gốc, chưa mipmap/buffer phụ. Đây là phép tính theo định dạng giả định, không là dung lượng tải PNG hoặc bộ nhớ của mọi thiết bị. Không mặc định làm atlas càng lớn càng nhẹ.

Biện pháp đề xuất:

- Tái dùng texture/atlas và object pool cho đạn/hạt/số damage; không tạo/hủy hàng loạt mỗi đợt.
- Tải asset theo vùng/đội/ngoại trang đang dùng, không nạp toàn roster và mọi skin.
- VFX trang trí tách khỏi projectile/hit logic; một nghìn hạt không thành một nghìn vật thể vật lý.
- Hạn chế filter toàn màn hình; dùng vùng nhỏ, hiệu ứng được vẽ sẵn và số đèn/bóng động có cap.
- Giảm lớp alpha khổng lồ chồng nhau, nhất là 7 người cùng ulti.
- Nhóm đối tượng khi giữ được thứ tự trước–sau; không phá depth để giảm draw call.
- Gộp damage nhỏ theo mục tiêu/khoảng ngắn; giữ crit/hit quan trọng rõ. Font số và font học có thể dùng pipeline khác.
- Chữ học cần đủ glyph Việt/IPA, không giảm độ nét để bù VFX.
- Culling/LOD và tần suất AI được chọn qua profiler; không giả định một tối ưu phù hợp mọi nút thắt.
- Không giảm kết quả damage hoặc tốc độ học khi hạ quality hình ảnh.

### 26.8. Quality và stress test

Mục tiêu thử desktop ban đầu: 60 FPS ở 1080p tương ứng khoảng 16,7 ms/frame; chưa phải cam kết đạt trên mọi máy.

Test theo bậc 1/3/7 người, khoảng 50/100/200/300 quái và nhiều cấp VFX, ghi riêng số thật và số trang trí. Đẩy từng trục để tìm nút thắt, không tuyên bố tổ hợp tối đa đã được hỗ trợ. Thử cả voice đang chạy và cảnh nhiều đồ rơi/nhãn.

High/Ultra không dùng blur toàn cảnh để che chất lượng. Giảm tải bằng mật độ hạt phụ, tàn, đèn, độ dài dư ảnh và VFX đồng đội; vùng chữ và dấu nguy hiểm vẫn rõ. Quality thấp giữ silhouette chính, hit confirm và cơ chế đọc được.

Ghi frame time, spike, bộ nhớ sau nhiều lần đổi scene, input-to-cast, voice-to-cast và cảm giác đọc. Model cân bằng ở mục 23 không kiểm rendering.

### 26.9. Đội đông và ưu tiên thông tin

Đòn bản thân và nguy cơ đang nhắm vào mình ưu tiên. Đồng đội có bản VFX gọn, vẫn thấy buff/giải/hợp trận quan trọng. Không bày 42 ô skill trên màn của một người.

Dùng dấu nguồn/loại thay vì mỗi aura một vòng sáng dày. Hiển thị rương/loot đặc biệt dễ đọc giữa skill. Bóng/foreground không che chữ hoặc pointer điểm đến.

Tu luyện vẫn dùng vùng đọc ổn định, ký hiệu loại và hoạt ảnh có nhịp. Camera, rung và flash của combat không lọt vào lớp chữ.

### 26.10. Âm thanh

BGM có âm lượng riêng, không ducking theo phát âm. Hô chiêu và tiếng pet có cap lặp. Voice cần tránh tiếng game bị nhận thành lời người chơi; chọn cấu hình microphone/đầu vào và thử tiếng loa/tai nghe thực tế, không khẳng định đã giải bằng thiết kế.

Phát âm của bài học không tự kích hoạt skill qua mic. Kết quả TTS/âm thanh hệ thống không được ghi là câu trả lời của người học; cần điều phối kênh âm thanh/nhận và kiểm trên runtime.

### 26.11. Bộ mẫu trước khi sản xuất hàng loạt

Một nhân vật chạy/cast 2D, hai loại quái, một boss, một nền có vật che và đồ rơi, ba skill khác hình: kiếm, hỏa, băng/lôi; có buff/pet mẫu. Kiểm depth, hướng đánh, điểm nhặt, chữ và hiệu năng trước.

Sau đó mới nhân rộng hướng nhìn, costume và số skill. Chưa cần tạo ảnh hoặc model mới trong lần cập nhật tài liệu này.


## 27. Trình tự phát triển đề xuất

| Bước | Đầu ra | Cửa kiểm |
|---|---|---|
| P0 | Ghi nền mới và đánh dấu 5 cơ chế mở rộng | Không ép chọn một phương án để được di chuyển |
| P1 | Đi chuột/phím, range, đánh nền, skill, nhặt đồ, vùng trận | Không xung đột chữ/đi, đứng/chạy đều có đường chơi |
| P2 | Typing/Voice/Hybrid qua cùng giao dịch | Không double cast, từ cũ/partial, TTS tự kích |
| P3 | Scene 2D có chiều sâu và ba vai công/support/pet | Đọc rõ, animation/range khớp, FPS được đo |
| P4 | Tam Tài với bot, đứng/ra/vào trận và loot cá nhân | Không nhân buff/loot, vai không khóa tọa độ |
| P5 | Tu luyện Minh–thường–Tâm ma và một cơ chế đặc biệt đã chọn | Deadline công bằng, không loạn, profile voice tách nếu có |
| P6 | Co-op người thật | Đồng bộ vị trí/skill/loot, quyền lệnh và mất kết nối |
| P7 | Thất Tinh, thêm lớp/mode | Dữ liệu cân bằng, đọc, ASR và scene đông |

Không đợi multiplayer hoàn chỉnh mới thử buff/pet: solo và bot kiểm sớm. Kiểm chuột/phím, Voice, đứng trận/di chuyển và một scene 2D mẫu trước khi sản xuất hàng trăm asset.

## 28. Điểm dành cho vòng review tiếp theo

Nền đã được người dùng yêu cầu: chuột/phím di chuyển tự do, đứng trận có lợi nhưng tùy chọn, Typing/Voice/Hybrid, cận/tầm xa và thu thập/khám phá; đồ họa 2D có chiều sâu. Năm phương án đặc biệt tiếp tục để review, không khóa nền đã xác định. Các hướng buff/pet/solo/đội/bot và tu luyện nhanh–chuẩn được giữ.

Chưa cần tải video dài. Nếu muốn khảo sát sát một minigame cụ thể, một đoạn ngắn thấy bắt đầu, thao tác, hết hạn và kết quả sẽ giúp phân biệt luật quan sát với đề xuất.

## 29. Nguồn

| Mã | Nguồn | Phạm vi |
|---|---|---|
| R01 | [Matthew Davis — Into the Breach Design Postmortem, GDC 2019](https://media.gdcvault.com/gdc2019/presentations/Into%20the%20Breach%20Postmortem%20Final.pdf) | Tài liệu của nhà phát triển: báo đòn, khả năng đọc, ràng buộc thiết kế |
| R02 | [Epistory chính thức](https://epistorygame.com/) và [Steam](https://store.steampowered.com/app/398850/Epistory__Typing_Chronicles/?l=english) | Điều khiển bàn phím; không suy diễn mapping cụ thể |
| R03 | [Typing of the Dead: Overkill — manual](https://cdn.akamai.steamstatic.com/steam/apps/246580/manuals/TOTDO_STEAM_MANUAL_ENG.PDF?t=1603130707) | Gõ khóa đích/co-op. Manual có cả phần House of the Dead dùng chuột, không trộn hai phần |
| R04 | [Panzer Dragoon: Remake — Steam](https://store.steampowered.com/app/1178880/Panzer_Dragoon_Remake/?l=english) | Màn hành trình, địch nhiều hướng, khóa đích; chọn tuyến bằng từ là sáng tạo dự án |
| R05 | [Activision — Sekiro Game Mechanics](https://support.activision.com/sekiro/articles/sekiro-shadows-die-twice-game-mechanics) | Posture, tấn công/deflect/phản; không lấy timer phản xạ cho typing |
| R06 | [Supergiant — Transistor FAQ](https://www.supergiantgames.com/blog/transistor-faq/) | Kết hợp kế hoạch với hành động |
| R07 | [PlayStation — trải nghiệm trực tiếp Transistor tại PAX 2013](https://blog.playstation.com/2013/09/04/hands-on-with-transistor-on-ps4/) | Turn, xếp chuỗi, ngân sách và nhịp hồi; bài về demo, không lấy số làm bản cuối |
| R08 | [Bad North — Steam, mô tả nhà phát hành](https://store.steampowered.com/app/688420/Bad_North_Jotunn_Edition/?l=english) | Lệnh cấp đội, lính tự đi và giao chiến |
| R09 | [SUPERHOT — Steam](https://store.steampowered.com/app/322500/SUPERHOT/?l=english) | Nhịp thời gian theo hành động; không khẳng định đứng yên time scale bằng 0 |
| R10 | [Outshine — Steam](https://store.steampowered.com/app/1288410/Outshine/) | Typing, kỹ năng/boss, bàn phím; không suy diễn cách né cụ thể |
| R11 | [GamerSky — hệ kỹ năng Tale of Immortal, 01/02/2021](https://www.gamersky.com/handbook/202101/1359456_9.shtml) | Nguồn cộng đồng cũ, dẫn yjyj98879/Ali213; cầu ngộ/ma và học–luyện–tham ngộ |
| R12 | [Steam — Short Mind Skill Guide, The Guy, cập nhật 25/04/2025](https://steamcommunity.com/sharedfiles/filedetails/?id=3165878972) | Người chơi trực tiếp mô tả mở dòng/tham ngộ; không phải tài liệu chính thức đầy đủ |
| R13 | [PixiJS — Performance Tips](https://pixijs.com/8.x/guides/concepts/performance-tips) | Tài liệu kỹ thuật chính thức, atlas/filter/mask/blend/text; không là benchmark game này |
| R14 | [Godot — 2D lights and shadows](https://docs.godotengine.org/en/stable/tutorials/2d/2d_lights_and_shadows.html) | Nguyên tắc độ sâu 2D; không chốt engine |
| U01 | Ảnh người dùng gửi: image(20261024-080931).png | Minh họa tu luyện, không suy toàn bộ luật từ ảnh |
| U02 | Ảnh người dùng gửi: image(20261024-095035).png | Tham chiếu hình skill, quái và đồ rơi; không suy engine/shader |

Không dùng thống kê class của game khác để khẳng định cân bằng cho dự án. Mọi bảng số V2 là giả thuyết có kiểm tra nhất quán; V2.2 chưa bổ sung benchmark runtime cho di chuyển/Voice/2D.

## 30. Phụ lục tái lập mô hình

Python tiêu chuẩn, không thư viện ngoài. Đây là phép kiểm thiết kế, không phải code triển khai game.

~~~python
"""Analytical design probes, not a game simulation or playtest."""
from itertools import product
from collections import Counter
import json

CURVES = {
    "F": [110, 109, 106, 103, 100, 98, 97],
    "S": [101, 102, 102, 102, 103, 102, 102],
    "R": [92, 94, 97, 101, 105, 109, 112],
    "H": [96, 98, 100, 102, 104, 106, 108],
}

def typing_seconds(chars, wpm):
    return 12.0 * chars / wpm

def response_window(wpm, remaining=4, defense=6, read_time=1.0, margin=1.0):
    return read_time + typing_seconds(remaining + defense, wpm) + margin

def corrected_team(n, supports, families=None):
    # One player owns all pets. They are not extra party members here.
    assert 0 <= supports <= n
    if families is None:
        families = ["A" if i % 2 == 0 else "B" for i in range(supports)]
    assert len(families) == supports
    strongest = {f: .10 for f in families}
    amp = min(.18, sum(strongest.values()))
    raw = (n-supports) * 100.0 + supports * 75.0
    return raw * (1+amp)

def broken_team(n, supports):
    # Deliberately flawed proposal: full personal DPS AND multiplying auras.
    return n * 100.0 * 1.20 ** supports

def pet_output(total_budget, count, team_amp=.18):
    assert count >= 1
    per_pet = total_budget / count
    return count * per_pet * (1+team_amp)

def cooldown(base, reduction):
    assert base > 0
    return max(2.0, base * (1-min(.30, max(0.0, reduction))))

def earliest_deadline_trace(tokens, wpm, choose_time=.6):
    """Non-preemptive words, ideal typing; lower-bound design probe only."""
    pending=list(tokens)
    t=0.0
    trace=[]
    while pending:
        available=[x for x in pending if x["appears"]<=t]
        if not available:
            t=min(x["appears"] for x in pending)
            available=[x for x in pending if x["appears"]<=t]
        token=min(available,key=lambda x:x["expires"])
        t+=choose_time+typing_seconds(token["chars"],wpm)
        trace.append({"id":token["id"],"finished":round(t,3),"expires":token["expires"],"in_time":t<=token["expires"]})
        pending.remove(token)
    return trace

def run():
    checks = []
    def check(name, condition):
        assert condition, name
        checks.append(name)

    for name, curve in CURVES.items():
        check("curve_floor_"+name, min(curve) >= 92)
        check("curve_ceiling_"+name, max(curve) <= 112)
    check("fast_still_viable_late", CURVES["F"][-1] >= 95)
    check("late_growth_not_required_at_start", CURVES["R"][0] >= 90)
    check("actual_crossover", CURVES["F"][0] > CURVES["R"][0] and CURVES["F"][-1] < CURVES["R"][-1])

    teams=[]
    for n in (2,3,4,5,7):
        values=[corrected_team(n,k) for k in range(n+1)]
        best=max(range(n+1), key=lambda k: values[k])
        teams.append({"slots":n,"no_support":n*100,"one_support":round(values[1],2),"best_support_count_in_this_model":best,"best_output":round(values[best],2),"all_support":round(values[n],2),"best_gain_percent":round((values[best]/(n*100)-1)*100,2)})
        check(f"all_support_not_dominant_n{n}", best < n)
        check(f"team_amp_bounded_n{n}", max(values)/(n*100) <= 1.10)

    duplicate=corrected_team(7,2,["A","A"])
    diverse=corrected_team(7,2,["A","B"])
    check("duplicate_buff_not_stacking", duplicate < diverse)
    check("duplicate_assignment_symmetric", corrected_team(7,2,["B","A"]) == diverse)
    pet_values=[pet_output(70,c) for c in (1,2,3,4)]
    check("pet_count_does_not_multiply_budget", max(pet_values)-min(pet_values)<1e-9)
    check("pet_buff_once", abs(pet_values[0]-82.6)<1e-9)
    for cdr in (0,.1,.3,.6,1.0):
        check("cooldown_positive_"+str(cdr), cooldown(8,cdr)>=2)
    check("cooldown_cap", cooldown(8,1.0)==cooldown(8,.3))

    windows=[{"wpm":w,"seconds":round(response_window(w),2)} for w in (25,40,60,90)]
    check("slower_typing_needs_longer_warning", windows[0]["seconds"] > windows[-1]["seconds"])
    check("half_second_parry_invalid_for_typing", typing_seconds(6,60)>.5)
    # Six-card candidate set includes skill + move/order cards together.
    words=["river","stone","bloom","quiet","shelter","thunder"]
    check("words_unique", len(words)==len(set(words)))
    check("no_complete_prefix_collision", not any(a!=b and b.startswith(a) for a,b in product(words, repeat=2)))
    # Simultaneous avoidable threats: require at most one new typed response.
    movement_cost=typing_seconds(6,40)
    emergency_cost=typing_seconds(6,40)
    check("two_words_need_more_than_one_word", movement_cost+emergency_cost>movement_cost)
    green=[{"id":"M1","appears":0,"expires":6,"chars":5},{"id":"M2","appears":3,"expires":10,"chars":6},{"id":"M3","appears":6,"expires":13,"chars":5},{"id":"M4","appears":9,"expires":17,"chars":7}]
    good_trace=earliest_deadline_trace(green,25)
    impossible=[{"id":"M1","appears":0,"expires":5,"chars":7},{"id":"M2","appears":0,"expires":5,"chars":7}]
    bad_trace=earliest_deadline_trace(impossible,40)
    check("staggered_green_schedule_feasible_without_errors",all(x["in_time"] for x in good_trace))
    check("detect_infeasible_simultaneous_green_schedule",not all(x["in_time"] for x in bad_trace))
    result={"model":"analytical assumptions only; no enemy AI, networking, player data or finished game","checks_passed":len(checks),"checks":checks,"curves":CURVES,"team_sweep":teams,"seven_all_support_broken":round(broken_team(7,7),2),"seven_all_support_corrected":round(corrected_team(7,7),2),"seven_two_duplicate_support":round(duplicate,2),"seven_two_diverse_support":round(diverse,2),"pet_budget_70_after_18_percent_amp":pet_values,"response_windows":windows,"eight_second_cooldown_at_cap":cooldown(8,1.0),"cultivation_feasible_25wpm":good_trace,"cultivation_infeasible_40wpm":bad_trace}
    return result

if __name__ == "__main__":
    print(json.dumps(run(),ensure_ascii=False,indent=2))
~~~



