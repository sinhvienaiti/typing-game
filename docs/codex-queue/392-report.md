# Phiếu 392 — Lối chơi gõ chữ trước, bố cục UI/UX sau

## Tóm tắt cho owner

Khuyên dùng **gõ từ để chọn kỹ năng ở một dải cố định, kết hợp Ấn trên địch đặc biệt; mua và đặt cơ quan bằng phím lệnh lúc nghỉ**. Giữ quái thường không mang chữ. Đây là nền luật đang có, phù hợp với thú triều đông và ngân sách học. Danh sách là các lựa chọn song song, không phải hàng đợi bắt buộc gõ từ trái sang phải. Chưa nên đưa cụm từ vào tuyệt kỹ hiện tại: thời gian gõ dài hơn, cần đổi hợp đồng Cast và cân bằng, nhưng chưa giải quyết được việc che sân.

Chọn **phương án A: dải gõ thấp, HUD gọn, mỗi lần chỉ một chế độ**. Khi đánh chỉ hiện thông tin quyết định hành động; cửa hàng đóng; Học trước và Thẻ Ôn chỉ hiện khi trận dừng. Khi học, ẩn cửa hàng và thanh kỹ năng. Khi đặt trụ, thu ngăn cửa hàng để thấy cả sáu ô đất. Bản đồ, đường đi và vị trí công trình giữ nguyên.

Trong ảnh owner, khung UI phủ khoảng **34,5% khung game**, nhưng tập trung tới **79,3% một vùng giữa–dưới được định nghĩa rõ trong báo cáo**. Đây là số đo hình chữ nhật trên ảnh, không phải toàn bộ sân bị che. A có ngân sách thiết kế khoảng **15,4–16,6% khi đánh**, **20,1% khi mua**, **23,0% khi học**; chưa phải kết quả chạy game.

Chưa sửa code, chưa tạo media, chưa chạy build/test. Không kết nối được browser host để đo DOM ở hai độ phân giải. Sandbox chặn ghi thư mục review ngoài repo; toàn bộ sơ đồ ASCII và nội dung ABOUT được giữ ngay trong báo cáo để bàn giao.

## 0. Phạm vi, bằng chứng và mức chắc chắn

- Ngày đọc: **16/11/2026**, một làn Codex; phiếu đã có `Phản biện: PASS (Sonnet, vòng 3)`. Đây là nghiên cứu theo yêu cầu trực tiếp của owner, không phải vé triển khai hay phán quyết chấp nhận mỹ thuật.
- Đã mở ảnh của owner: `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-16/tu-tien/ui-layout-research/owner-screenshot-current-ui.webp`. Không gửi ảnh này hoặc ảnh bên thứ ba vào công cụ tạo ảnh.
- Đã đối chiếu `00-canon.md` §§4–6, 8–10, 12–14, 17, 21, 24–25; `M0A_PLAN.md`; `DANH_GIA_2026-10-24.md`; các phân tích `03-ky-nang-chien-dau.md`, `04-vat-pham-kinh-te-shop.md`, `05-che-do-chong-thu-trieu.md`, `07-hoc-tieng-anh-my-thuat-am-thanh-san-xuat.md`. Các phân tích cũ có số và hướng mỹ thuật đã bị canon thay; chỉ dùng để hiểu lý do, không phục hồi luật cũ.
- Đã đọc các presenter HUD, Bàn Quyết, Học trước, khung học, Thẻ Ôn, cửa hàng, đợt, các vùng màn hình; router phím; phần nối app; luật chữ, nhắm đích và vị trí ô cơ quan trong source hiện tại.
- **Quan sát ảnh:** bằng chứng trực tiếp của đúng ảnh được giao. **Đọc code:** xác nhận điều kiện và công thức, chưa xác nhận cảm nhận khi chơi. **Dự phóng:** quy đổi hình học từ ảnh sang hai kích thước. **Đề xuất:** số ngân sách và hành vi chưa được dựng.
- Web truy cập được; nguồn ở §3 đã tra ngày 16/11. Browser automation trả `The browser access host is unavailable`; không có số đo DOM trực tiếp tại 1280×720 hoặc 1920×1080 trong phiên này. Không mở server hay chạy build/test để lấy số thay thế.
- Source mới `src/content/data/stage-m0a.ts` có ghi phiếu 387a: hành lang uốn, hai cổng cùng miệng vào. Một số mô tả cũ còn nói hai hướng vào độc lập. Báo cáo **không suy bố cục từ bản đồ cũ**, không đổi bản đồ hay camera để bù UI.

## 1. Lối chơi gõ chữ — quyết định chính

### 1.1 Người chơi hiện đang gõ gì để làm gì?

Nguồn luật: [`00-canon.md`](../games/tu-tien/00-canon.md) §§5, 6, 8.3, 9.3, 12.1, 14.3, 17. Source dưới đây viết tương đối từ `games/immortality-cultivation/`.

| Việc | Đầu vào và hiệu quả hiện tại | Nhắm đích, phản hồi và ý nghĩa học |
|---|---|---|
| Đánh nền | Tự động; không gõ mỗi phát | Theo mục tiêu mềm hoặc địch hợp lệ gần Trận Tâm trong tầm. Không sinh sự kiện học |
| Ô 1, đòn liên tục | Gõ hết một từ quen 3–5 chữ → nạp một băng 3 kiếm | Từ chọn **hành động**, không chọn một con quái theo tên. Ưu tiên mục tiêu mềm hoặc địch gần Trận Tâm trong tầm |
| Ô 2, chiêu chính | Từ 4–7 chữ đang học/đến hạn → chiêu đường thẳng, hồi 8 s | Mục tiêu mềm hoặc cụm gần Trận Tâm; gặp lại từ mới sau lần đầu, không dùng làm nơi giới thiệu từ mới |
| Ô 3, hộ thân/thân pháp | Từ quen 3–5 chữ → khiên tại vị trí tung, hoặc lướt theo loadout | Cách tự cứu bằng từ dễ; không thêm phím chữ để dùng chiêu |
| Ô 4, chiêu phụ | Từ 4–7 chữ → vùng kiếm tại con trỏ hoặc cụm đông nhất; hồi 12 s | Là ô duy nhất nhận từ mới trong đợt 1–2; lần mới có nghĩa và IPA theo luật |
| Ô 5, tuyệt kỹ | Đầy Chân Nguyên mới có từ sống 5–8 chữ; gõ xong → tuyệt kỹ, dùng thanh | Hiện tại vẫn là **một từ**, không phải câu; từ đến hạn/yếu, không phải từ mới |
| Ấn / Tẩy | Gõ từ trên tinh anh, tướng, Vương để xử lý Ấn; gõ Tẩy để lấy lại nhãn bị chiếm | Tác vụ khẩn, chỉ từ quen/đến hạn theo luật. Có chủ thể rõ; khác với quái thường |
| Đan, phù | `1/2/3` hoặc đường chuột của điều khiển tương ứng; hồi chung 8 s | Không gõ tên món; không thưởng học. Presenter Bàn Quyết hiện chỉ vẽ ô, cần kiểm chứng đường click thực tế trước khi dựa vào nó |
| Mua, đặt, nâng, bán | Lúc chuẩn bị/nghỉ: Backquote mở chế độ shop; mũi tên, Enter, `=`, `-` | Không gõ từ để mua hoặc kích hoạt trụ. Cơ quan đã đặt tự đánh; không bắt gõ thêm cho từng lần trụ bắn |
| Học trước | Xem từ + IPA + nghĩa Việt, nghe, gõ lại một lần | Tùy chọn, không giới hạn giờ; sao chép có gợi ý, luôn `hintUsed: true`; không coi là đã nhớ nghĩa |
| Thẻ Ôn | Tối đa 3 câu lúc nghỉ: nghe rồi gõ, nhìn nghĩa rồi gõ, hoặc chọn nghĩa bằng `1/2/3` | Lúc thẻ mở, số thuộc câu hỏi; đồng hồ nghỉ dừng. Ẩn chữ chiến đấu tránh lộ đáp án |

Các bất biến quan trọng từ code và canon:

1. **Một từ hoàn thành → một Cast**, chữ cuối chốt tự động; không cần Enter để bắn. Nếu không có đích hợp lệ, giữ tối đa 3 s rồi có thể hết hiệu lực; không tự tiêu hồi chiêu khi hết hiệu lực. Không hứa với người chơi rằng mọi từ đúng đều trúng quái.
2. Chữ đầu của các từ sống khác nhau, không có quan hệ tiền tố hoặc quá giống nhau; gõ chữ đầu khóa lựa chọn. Từ không đổi khi đang gõ dở. Backspace lùi chữ, Esc nhả khóa. Giữ nguyên lịch sử lỗi khi nhả khóa theo `sim/words.ts`.
3. Tối đa `min(trần preset, A−3)` từ sống: thường ≤8, Relaxed/Learning ≤5. Đây là trần **toàn bộ** 5 ô + Ấn + Tẩy, không phải 8 từ ở dải rồi thêm nhãn tùy ý ngoài sân.
4. Bàn Quyết chỉ sống từ báo đợt đến hết đợt và pha Vương; mờ khi chuẩn bị/nghỉ/gục. Trong đợt hiện **nhiều lựa chọn kỹ năng**, không phải một bài chép tuyến tính.
5. Ngân sách ≤8 từ mới trong cửa sổ trượt 20 phút, dùng chung Học trước/Tĩnh Tu/ô 4. Từ mới của trận phải gặp ≥3 lần, cách nhau ≥45 s, trước đợt 4. Khi nợ ôn nhiều, allowance còn có thể thấp hơn. UI thu gọn không được làm mất lịch gặp lại.

Code đối chiếu chính: `app/input-router.ts`, `app/app.ts`, `sim/words.ts`, `sim/cast.ts`, `sim/targeting.ts`, `typing/slots.ts`, `typing/new-word-ledger.ts`, `ui/ban-quyet.ts`, `ui/learn-ahead.ts`, `ui/review-card.ts`, `ui/shop-mode.ts`.

### 1.2 So sánh bốn mô hình

Đây là đánh giá thiết kế của Codex, không phải kết quả thử nghiệm người chơi. “Hợp học từ” xét cả chính tả, nghĩa, phát âm, gặp lại và quyền đưa từ mới vào tình huống khẩn.

| Mô hình | Cách hiện chữ và chọn đích | Tải nhận thức | Học từ vựng Anh | Chi phí, điểm yếu với Tu Tiên |
|---|---|---|---|---|
| **M1 — từ trên từng quái** | Nhãn bám quái; chữ đầu khóa con tương ứng; tô phần đã gõ ngay tại nhãn | Liên kết mắt–đích rõ khi ít quái. Khi đông: tìm từ, đọc chữ chuyển động, phân biệt lớp và theo dõi nguy hiểm đồng thời | Tốt cho chính tả; nghĩa/IPA đi theo nhãn sẽ làm nhãn lớn. Quái chết sớm làm nhịp gặp lại phụ thuộc chiến đấu | Với 60 địch, không thể mọi con cùng có từ mà vẫn giữ trần 5–8 và chữ đầu khác nhau. Chỉ gắn từ cho một nhóm nhỏ sẽ thành một thiết kế khác, cần luật chọn nhóm và địch chưa có chữ. Không chọn làm nền |
| **M2 — cụm/câu cho chiêu và tuyệt kỹ** | Một ô cố định hiện cụm 2–3 từ hoặc câu; phải chọn hành động trước/nhờ tiền tố; có tiến độ theo từ | Ít vị trí đọc nhưng giữ bộ đệm dài, dễ quên đang gõ đến đâu; chuyển từ phòng thủ sang chiêu lớn chậm hơn | Có tiềm năng học cụm trong ngữ cảnh nếu nội dung, nghĩa và bài kiểm nhớ được soạn thật; lặp mã chiêu cố định chỉ luyện thuộc mã | Đổi tokenizer, dấu cách, lỗi, hủy, Cast và học theo nhiều `wordId`; thêm thời gian phải cân bằng. Canon chỉ để cụm 2 từ cho ô 6 sau MVP. Không đưa vào ô 5 ở lượt UI này |
| **M3 — hàng đợi từ ở dải cố định** | Một từ hiện tại lớn, 2–3 từ kế mờ; gõ xong tự đánh đích ưu tiên | Ít tìm kiếm nhất, thuận gõ đều; nhưng mắt ở đáy và quyền chọn kỹ năng bị giảm nếu bắt đi theo hàng | Dễ điều phối từ mới/gặp lại. Vẫn chủ yếu sao chép nếu luôn thấy đáp án, chưa chứng minh nhớ nghĩa | Nếu chỉ một hàng bắt buộc, người chơi có thể phải gõ đòn khác trước khi đến khiên. Nếu cho chọn nhánh thì thực chất đã trở thành bảng lựa chọn. Không dùng hàng đợi bắt buộc |
| **M4 — kết hợp có giới hạn** | Dải cố định chứa các từ của kỹ năng có thể chọn ngay bằng chữ đầu; Ấn/Tẩy có liên kết trên sân; shop và học là chế độ riêng | Ít chữ chuyển động; vẫn chọn được đánh/khiên/vùng/tuyệt kỹ. Còn chi phí đảo mắt giữa dải và địch, cần đo thật | Giữ ngân sách, lịch gặp lại, nghĩa/IPA theo mức thuộc; dành kiểm nhớ và nghe cho lúc nghỉ | Gần source nhất. Phải làm rõ “từ chọn chiêu, đích chọn riêng”; tránh biến thanh kỹ năng thành một bảng tên dài. **Khuyên dùng** |

Ví dụ thời gian thuần gõ, theo quy ước WPM = 5 ký tự: ở 35 WPM, 5 ký tự ≈1,71 s; cụm 12 ký tự ≈4,11 s; câu 40 ký tự ≈13,71 s, chưa kể đọc/sửa. Độ dài tăng không tự tạo chiều sâu chiến thuật. Ở 25 WPM, từ 5 ký tự đã khoảng 2,4 s; không bắt người này hoàn tất câu dài để tự cứu.

Biến thể “quái thường gõ từ, kỹ năng gõ cụm, mua lúc nghỉ” đã được cân nhắc: liên kết trực tiếp rất hấp dẫn, nhưng cộng dồn tải của M1 và M2; đổi cả luật nhắm đích, tốc độ ra chiêu và ngân sách chữ. Có thể là một prototype gameplay riêng nếu owner muốn đổi nền game, không phải giải pháp thu gọn HUD lần này.

### 1.3 Mô hình khuyên dùng: bảng lựa chọn từ, không phải hàng đợi cưỡng bức

**Trong chiến đấu, người chơi quyết định “dùng chiêu gì, vào đâu” rồi gõ một từ để thực hiện.** Thứ tự gợi ý có thể có, nhưng không khóa mất những lựa chọn khác.

- Mỗi ô có icon art của chiêu, một nhãn vai ngắn bằng tiếng Anh và từ đang sống. Chữ đầu được nhấn rõ. Nhãn vai tách khỏi từ: ví dụ `Strike` phía trên `stone`, không yêu cầu gõ `Strike stone`. Các tên ví dụ là nhãn nghiên cứu, chưa phải bản dịch chính thức của kỹ năng.
- Mọi từ có thể kích ngay đều nhìn thấy, kể cả Ấn/Tẩy trong ngân sách. Khi bắt đầu gõ, chỉ tăng nổi từ đang khóa; các từ khác vẫn ở vị trí ổn định và còn đọc được. Không thu mọi ô khác thành icon vô chữ, không bắt nhớ từ ẩn.
- Hồi chiêu là vòng/số nhỏ; từ kế mờ không có gạch chân chữ đầu và không nhận phím. Cần khác biệt bằng hình/trạng thái, không chỉ giảm opacity để người mới đoán.
- Đích tự chọn dùng luật hiện có; click trái đặt mục tiêu mềm là tùy chọn. Chỉ báo đích đặt lên chủ thể/viền vùng đánh. Không thêm nhãn từ lên toàn bộ bầy để giải thích đích.
- Ô đất dùng con trỏ trong sân hoặc cụm đông theo luật. **Rủi ro phải giải quyết khi dựng:** con trỏ để lại trên sân từ trước có thể khiến người chơi bàn phím bắn vào chỗ cũ. Cần chỉ báo `Aim: cursor` / `Aim: auto` rõ và kiểm tra hành vi hiện tại; thay quy tắc con trỏ phải là quyết định riêng, không lén đổi trong CSS.
- Ấn trên địch đặc biệt được nối bằng dấu chọn/đường liên kết rất gọn với mục từ ở dải. Có thể hiện bản sao nhãn trên chủ thể khi cần định vị; cùng `wordId` và khóa, không phải thêm một từ sống. Nhãn không nhảy khi đang gõ; nếu hết chỗ trên sân, dải vẫn đọc được.
- Một dòng nghĩa/IPA cho **từ đang gõ** tích hợp vào dải khi luật `hint` cho phép; bỏ khung học thứ hai nổi phía trên. Giữ việc sao chép có gợi ý khác với bài nhớ nghĩa. Không cho tooltip nghĩa xuất hiện ngầm mà bản ghi vẫn báo `hintUsed: false`.
- Ô 4 tiếp tục nhận từ mới ở tải phù hợp, không chuyển từ mới sang khiên hoặc Ấn. Không dồn mọi từ mới sang trước trận vì sẽ làm việc học thành bước cản bắt buộc và làm đổi lịch phân phối hiện tại.

**Vì sao vẫn phải có học lúc nghỉ:** nghiên cứu của Karpicke & Roediger dùng từ vựng ngoại ngữ cho thấy lợi ích của truy hồi lặp lại đối với ghi nhớ lâu dài. Suy ra cho thiết kế này: gõ chép lúc đánh cần được bổ sung bằng nghe/nhớ nghĩa lúc an toàn; không dùng WPM làm bằng chứng đã học nghĩa. Đây không phải thử nghiệm hiệu quả học của Tu Tiên. [Bài nghiên cứu, Science 2008](https://pubmed.ncbi.nlm.nih.gov/18276894/).

### 1.4 Luồng một đợt từ đầu đến cuối

Ví dụ từ và vị trí sau đây chỉ minh họa luồng, không sửa bộ từ hoặc thứ tự cấp từ của game.

1. **Trước trận:** chọn tốc độ theo flow có sẵn. Vào trạng thái `Prepare`, xem một tóm tắt đợt. Nút `Learn words` là tùy chọn. Chọn học → chỉ thẻ học + chỉ báo `Learning · battle paused`, sân tĩnh phía sau; shop, thẻ đợt chi tiết và thanh chiến đấu ẩn. Nghe, gõ lại, sửa lỗi; xong trở về `Prepare`. Không bắt đi hết 8 từ mới được chơi.
2. **Chuẩn bị bố trí:** Backquote hoặc `Shop` mở ngăn hàng. Mũi tên chọn món/ô, Enter mua/đặt. Lúc xác nhận điểm đặt, ngăn thu còn dòng món + giá + `Enter: place` để thấy các ô trên **bản đồ hiện tại**. `=`/`-` vẫn xác nhận hai lần cho nâng/bán. Esc quay lại chuẩn bị. Chỉ một chủ thể nhận phím.
3. **Bắt đầu:** khi không bảng mở, Enter theo điều kiện hiện tại bắt đầu; đóng mọi bề mặt mua/học trước khi chuyển sang báo đợt 5 s. Trong lúc báo đợt, dải chữ sống theo canon, không tạo một luật chờ mới riêng cho UI.
4. **Trong đợt:** thấy bầy đến, chọn từ của đòn liên tục và gõ; chữ cuối phát một Cast. Nhìn chỉ báo đích và phản ứng trên sân. Cần chiêu vùng → chọn từ ô 4; cần khiên → Esc nhả từ dở nếu có rồi gõ từ ô 3. Không phải gõ hết một hàng mới được phòng thủ. Nếu xuất hiện Ấn/Tẩy, chỉ tăng nổi tác vụ khẩn, giữ trần chữ sống.
5. **Đầy tuyệt kỹ:** ô 5 chuyển trạng thái rõ bằng icon/viền và từ quen có thể gõ; không mở popup hay cut-in chữ để ép đọc. Người chơi quyết định lúc tung. Đan/phù dùng `1/2/3` nếu cần.
6. **Kết đợt thật sự:** không dựa vào đồng hồ về 0; chờ mọi toán của đợt đã sinh và hết địch theo luật. Trước Vương có đoạn lặng 8 s nhưng có thể còn địch cũ: vẫn dùng HUD chiến đấu, **không tự mở học hay shop**.
7. **Nghỉ giữa đợt:** chuyển sang `Break`; các từ chiến đấu mất quyền nhận phím. Hiện thời gian nghỉ và hai lựa chọn `Shop` / `Review`, không tự chồng cả hai. Nếu chọn ôn, tối đa 3 câu, ẩn đáp án chiến đấu, dừng đồng hồ; xong trở lại nghỉ. Shop cũng giữ chế độ riêng. Tiếp đợt theo timer/preset hiện hành; không tự thống nhất Enter cho mọi preset nếu chưa được duyệt đổi luật. Để đường bàn phím đầy đủ, đề xuất thêm **`4` = `Learn words` trong Prepare, `4` = `Review` trong Break**, chỉ khi tác vụ còn khả dụng; ngoài hai mode này không có tác dụng. Đây là phím mới cần duyệt, chưa có trong router hiện tại; không dùng `L` hoặc `R`.

Thay đổi UX cần owner duyệt rõ: hiện app tự mở Học trước khi có từ và hẹn mở Thẻ Ôn lúc nghỉ. Đề xuất chuyển sang lời mời có thể chọn/bỏ qua trong `Prepare`/`Break`; **chưa triển khai**. Không giảm allowance, bỏ phần thưởng học hay làm mất cơ hội ôn khi bỏ popup.

### 1.5 Phân quyền phím và chuyển chế độ

Giữ `event.code` cho lệnh; không lấy WASD, QWER, B/S/R làm phím tắt. Phím chữ a–z thuộc việc gõ. Tab không bị chiếm làm lệnh chiến đấu; vẫn cần đường focus cho người dùng bàn phím và công nghệ hỗ trợ khi dựng.

| Chế độ | a–z | Backspace / Enter | Esc | Mũi tên / số / Backquote |
|---|---|---|---|---|
| `Combat`, có từ khóa | Chỉ từ đang khóa; chữ cuối tự tung | Backspace lùi; Enter không bắn hoặc mua | Nhả khóa, không mở menu cùng nhịp | Mũi tên đi; 1/2/3 dùng đồ; Backquote không mở shop |
| `Combat`, chưa khóa | Chữ đầu chọn một từ sống | Backspace không bán đồ; Enter không có hành động chuẩn bị | Mở pause | Như trên |
| `Prepare` / `Break`, không bảng | Không tung chiêu; chữ bị bỏ theo luật | Enter chỉ theo điều kiện phase/preset | Mở pause | Backquote mở shop; **4 mở học/ôn (đề xuất mới)**; mũi tên vẫn đi theo source, không kiêm chọn menu |
| `Shop` | Không mua bằng chữ; không lọt về sim | Enter mua/đặt; Backspace không bán | Đóng shop, trả về nghỉ | ←→ món; ↑↓ ô; `=`/`-` nâng/bán xác nhận hai lần; 1/2/3 không dùng đan; Backquote đóng |
| `Learning` / `Review` | Vào ô trả lời | Xóa/sửa; Enter nộp nếu loại câu cần | Học trước: bỏ từ, Esc hai lần trong 600 ms đóng; Thẻ Ôn: Esc đóng ngay. Phải hiện hướng dẫn đúng | 1/2/3 chỉ chọn đáp án khi câu hỏi loại đó; không dùng đồ; 4 không mở tác vụ khác; Backquote không mở shop |
| `Pause` / `Settings` / `Sound` | Không lọt xuống chiến đấu | Theo panel đang focus | Đóng/trở lại một cấp | Không dùng đồ và không đi |

Quy tắc router cho bản dựng sau: **một mode chủ động, một nơi nhận phím, một lần nhấn chỉ tạo một tác dụng**. Mở mode dừng di chuyển và lưu/nhả khóa theo hợp đồng hiện hành; không làm mất im lặng từ đang gõ. Trở về đúng mode cha. Nút `Listen` và các nút panel có thứ tự Tab chuẩn; khi nút có focus, Enter/Space kích đúng nút, không đồng thời nộp câu hỏi ở router toàn cục. IME đang composition không cast/nộp bài/mở menu; Cmd/Ctrl shortcut của hệ điều hành giữ nguyên. Khi bật nguồn nhập tiếng Việt, báo bằng tiếng Anh cách chuyển sang ABC trên Mac; không tự sửa thành độ khó thấp hơn.

## 2. Kiểm kê UI hiện tại và đo mức che

### 2.1 Điều đang xảy ra, không gộp nhầm mọi phase

`app/app.ts` tạo HUD, Bàn Quyết, shop strip, shop mode và học cùng một match. `learnAhead.open(...)` tự chạy khi có từ học trước. `pausedNow()` dừng trận khi Học trước/Thẻ Ôn mở; **dừng sim không đồng nghĩa ẩn presenter khác**. `shop-strip.ts:164` chỉ xét phase có thể mua và shop mode chưa mở; không xét Học trước/Thẻ Ôn. Vì vậy ảnh chuẩn bị có học ở giữa và cửa hàng phía sau là tương thích với source.

Thẻ đợt **không thường trực trong wave đang đánh**: `wave-card.ts:125` chỉ trả thẻ ở prep/warning/break/lull. Shop strip cũng chỉ có prep/break. Không kết luận “lúc đánh luôn có cả cửa hàng lẫn Học trước” từ ảnh tĩnh này. Khi chiến đấu, nguy cơ khác là dải kỹ năng dài, khung học trùng nội dung phía trên, Ấn thêm vào dải và thông báo.

### 2.2 Công thức kích thước từ source

`uiScale(W,H) = clamp(0,8; min(W/1600,H/900); 1,2)` trong `src/kit/ui/tokens.ts`. Vì vậy hai viewport 16:9 cần xét có `u=0,8` và `u=1,2`. Kích thước px tuyến tính theo u cho cùng phần trăm, **trừ** chữ có `min/max/clamp`, wrap, border cố định và nội dung thay đổi.

Bảng dưới là **vùng dành chỗ do `screen-zones.ts` khai báo**, không phải diện tích nền panel đã render. `x,y,w,h` tính bằng CSS px, text scale 100%.

| Vùng khai báo | 1280×720: x,y,w,h | 1920×1080: x,y,w,h | w% × h% xấp xỉ | Lưu ý |
|---|---|---|---|---|
| `hud` | 10,518,240,96 | 14,778,360,144 | 18,75 × 13,33 | Góc trái dưới phía trên dải chữ; chiều cao thực theo nội dung |
| `top` | 464,8,352,74 | 696,12,528,110 | 27,50 × 10,28 / 10,19 | Giữa trên; chứa Trận Lực và có thể thêm Thế |
| `notices` | 432,92,416,61 | 648,136,624,91 | 32,50 × 8,47 / 8,43 | Chỉ là hình học keepout; notices thật được append trong `.ic-hud__top`, không là panel độc lập ở tọa độ này |
| `card` | 998,10,272,184 | 1498,14,408,276 | 21,25 × 25,56 | Chỗ dự phòng; thẻ thật tự cao và có thể chuyển góc |
| `shop` | 260,489,760,125 | 388,735,1144,187 | 59,38/59,58 × 17,36/17,31 | Vùng hình học không bằng CSS box: dải thật shrink/wrap theo nội dung |
| `quyet` | 0,624,1280,96 | 0,936,1920,144 | 100 × 13,33 | Band dành cho camera ở đáy, không phải panel nền kín cả chiều ngang |

Kích thước `shop` trên được tính đúng thứ tự làm tròn của hàm, không lấy screenshot thay. CSS `max-width` của shop gần 59,5% màn, nhưng **không có width cố định**; không được dùng 980u như chiều rộng thực ở cả hai độ phân giải.

### 2.3 Từng thành phần: kích thước thực suy từ ảnh, điều kiện hiện, chặn đầu vào

Ảnh có cả giao diện ứng dụng bên ngoài game. Khung game lấy gần `(102,84) → (1777,1027)`, cỡ **1675×943**. Tọa độ dưới đây so với khung đó, bỏ nền ứng dụng bên ngoài. Các con số có dấu `≈` là đo tay biên panel trên ảnh và **dự phóng đồng dạng**, không phải hai ảnh chụp mới ở 720p/1080p. Sai số biên khoảng vài pixel ảnh; wrap có thể làm kết quả thật khác.

| Thành phần / vị trí | w% × h%; diện tích khung | 1280×720: w×h dự phóng | 1920×1080: w×h dự phóng | Lúc hiện, quyền đầu vào |
|---|---|---|---|---|
| **Học trước**, x≈32,54%, y≈30,75% | ≈34,99 × 38,49; 13,47% | ≈448×277 | ≈672×416 | Prep, app tự mở khi có từ; `pointer-events:auto` trong card, không có veil toàn màn. Router lấy chữ/Enter/Esc; sim dừng |
| **Cửa hàng chuột**, x≈25,01%, y≈66,17% | ≈50,03 × 19,19; 9,60% | ≈640×138 | ≈961×207 | Prep/break khi shop mode chưa mở; card và nút nhận chuột. Không tự sở hữu phím khi chỉ là strip, nên học vẫn giữ phím nếu mở |
| **Bàn Quyết + 3 ô đồ**, x≈17,13%, y≈88,23% | ≈65,79 × 10,39; 6,84% | ≈842×75 | ≈1263×112 | Luôn có presenter; từ chiến đấu dim ngoài phase sống. `pointer-events:auto` trên nền; có thể chặn click lên sân dưới box. Ô đồ của `ban-quyet.ts` là div, không thấy click handler tại presenter này |
| **Trận Lực**, x≈36,30%, y≈1,17% | ≈27,40 × 5,62; 1,54% | ≈351×40 | ≈526×61 | HUD match; không lấy chuột/phím. Thế thêm hàng khi có đối tượng phù hợp, không có trong ảnh |
| **Sinh lực + Chân Nguyên**, x≈0,72%, y≈78,90% | ≈18,87 × 6,47; 1,22% | ≈241×47 | ≈362×70 | Góc trái dưới; HUD cập nhật cả lúc thẻ học mở; pointer none; không giữ phím |
| **Linh Sa**, x≈0,72%, y≈75,19% | ≈8,06 × 3,18; 0,26% | ≈103×23 | ≈155×34 | Chip trên Sinh lực, cập nhật khi ví đổi; pointer none. Tiền còn lặp trong shop |
| **Thẻ đợt**, x≈77,97%, y≈72,85% trong ảnh | ≈21,31 × 12,51; 2,67% | ≈273×90 | ≈409×135 | Prep/warning/break/lull; không giữ chuột/phím. Hàm đặt chọn góc phải trên, phải dưới hoặc trái trên để tránh đường/ô/panel; vị trí không cố định tuyệt đối |

Những thành phần cần kiểm kê thêm nhưng không thấy trong ảnh trên:

| Thành phần | Kích thước / vị trí từ source ở 720p → 1080p | Khi hiện và chặn đầu vào |
|---|---|---|
| Khung học khi chiến đấu `.ic-learn` | Rộng 352→528 px (**27,5% W**), cao tối thiểu 57,6→86,4 px (**8% H**), cách đáy 120→180 px (**16,67% H**), giữa ngang; cao auto khi có IPA/nghĩa/recent | Khi khóa từ hoặc giữ thẻ vừa gõ: từ mới 2,5 s, từ khác 0,8 s khi có hint. Nền pointer none; nút nghe pointer auto. Ẩn lúc Học trước/Thẻ Ôn. Chiếm thêm vùng sân trên dải, lặp từ đang có ở Bàn Quyết |
| Ô Ấn / Tẩy | Chèn vào `.ic-bq__extras`; mỗi ô min 102,4→153,6 px (**8% W**) trước khi nội dung làm rộng hơn; chiều cao auto | Có Ấn/Tẩy hợp lệ. Chia cùng router và trần chữ với kỹ năng. Tăng bề ngang dải; `max-width` của cha không bảo đảm các con flex không tràn |
| Tên và chữ kỹ năng | Ô thường min 102,4→153,6 px, đồ min 73,6→110,4 px; từ **28→32 px** ở 100% (không giảm theo cùng tỉ lệ u) | Nhãn tiếng Việt dài `white-space:nowrap`; tên, từ, trạng thái có thể ép rộng. Không thể suy chiều ngang thật chỉ bằng cộng min-width |
| Thế / thông báo | Cột trên rộng 352→528 px; Thế và mỗi notice cao auto. Vùng notices dự phòng ở bảng §2.2 không là số đo DOM | Thế chọn Vương trước, rồi mục tiêu mềm có Thế, rồi tinh anh/tướng phù hợp. Thông báo theo event. Pointer none; thêm chiều cao, không có modal |
| Shop mode bằng phím | Cùng CSS `.ic-shop`, cao auto theo hàng và thông báo, max-width gần 59,5% W; không có kích thước DOM để báo chính xác | Backquote ở prep/break, strip ẩn. Lấy mọi phím qua router; chữ bị bỏ; mũi tên không đi; Enter mua/đặt, nâng/bán cần hai lần |
| 6 ô cơ quan trên sân | Không là panel DOM: 2 dải đất 4×2 m, 4 vòng trụ bán kính 0,8 m, chiếu theo camera; **không có % px cố định** | Dấu ô chỉ hiện prep/break. `stage.ts` vẽ và highlight theo shop cursor. Không tự bắt keyboard; hàng nút chọn ô nằm trong shop. Tọa độ thế giới không đủ suy px nếu thiếu ma trận camera |
| Thẻ Ôn | Dùng `.ic-lpanel`: width min(92vw,560u) = 448→672 px (**35% W**); height auto theo câu nghe/nhớ nghĩa/3 lựa chọn | Mở ở break theo lịch app, chờ shop mode đóng; giữ phím, pause sim; card pointer auto. Nguy cơ strip phía sau còn hiện giống Học trước |
| Pause/settings | Veil 100% màn; panel rộng min(460u,W−32)=368→552 px (**28,75% W**), cao auto | Esc khi không khóa; veil chặn chuột, activePanel giữ phím, dừng sim. Không tính veil này như một HUD chơi thường trực |
| Kết quả / Sổ Từ | Panel rộng min(760u,W−32)=608→912 px (**47,5% W**), max-height H−quyetBand−32; nội dung cuộn | Sau trận; không có combat cần quan sát. Không đưa vào tổng HUD của ảnh chuẩn bị |
| Banner IME | Giữa trên, rộng tối đa min(92vw,760u)=608→912 px (**47,5% W**); cao auto | Khi phát hiện IME; click để ẩn, không giữ phím. Có thể đè thanh Trận Lực; phải có vị trí riêng trong layout mới |

Không tìm thấy hai nút Settings/Sound thường trực được dựng trong các presenter HUD vừa đọc; menu Esc có cài đặt, còn `createSoundHooks` là móc âm chứ không phải nút Sound. Cần kiểm chứng ở host hoàn chỉnh; phương án mới dành chỗ cho **cả hai nút art** theo luật repo, không coi Esc là thay thế nút nhìn thấy.

### 2.4 Tỉ lệ che: cách tính có thể kiểm lại

**Quy ước:** một nền panel bán trong suốt vẫn tính toàn bộ hình chữ nhật của nó vào diện tích che hình học, vì nó làm giảm khả năng đọc sân. Đây không phải alpha-weighted opacity hay đo nhận thức. Hình bo góc vẫn dùng bounding box; phần chồng chỉ tính một lần.

```text
Khung V = 1675 × 943 = 1.579.525 px².
Các box (x,y,w,h) trong hệ tọa độ ảnh gốc 2000 × 1103:
  Trận Lực : 710,  95,  459,  53
  Học trước: 647, 374,  586, 363
  Shop     : 521, 708,  838, 181
  Sinh lực : 114, 828,  316,  61
  Linh Sa  : 114, 793,  135,  30
  Đợt      :1408, 771,  357, 118
  Bàn Quyết: 389, 916, 1102,  98
Tổng từng box = 562.171 px².
Chồng Học trước ∩ Shop = 586 × 29 = 16.994 px².
Hợp = 545.177 px²; hợp / V = 34,515% ≈ 34,5%.
```

**Hai mẫu số khác nhau cần phân biệt:**

- Nếu “sân” là toàn bộ khung game phía sau UI: **34,5%**. 1280×720 dự phóng khoảng **318.093 px²** bị phủ; 1920×1080 khoảng **715.708 px²**. Không đổi phần trăm chỉ vì tăng độ phân giải.
- Nếu “sân” là view khả dụng sau khi trừ band đáy 120/900 =13,33% theo source: cắt các box theo phần trên band, hợp / vùng còn lại ≈ **31,9%** trong ảnh. Cách này loại nền Bàn Quyết nằm ngoài vùng camera tránh, không cộng band rồi đếm lại.
- Vùng kiểm tra chiến thuật **R = x25–75%, y30–85% của khung V** có khoảng **79,3%** bị các box phủ. R được chọn để kiểm tra nơi Học trước và shop đang chồng nhau quanh phần giữa–dưới; **không phải** mask địa hình hay toàn hành lang. Số này giải thích điểm tập trung che, không thay thế số toàn sân.

Mức che chính xác của **đường đi, cổng, Trận Tâm, sáu ô đặt và telegraph** chưa đo được: cần polygon chiếu từ host thật rồi tính giao với union UI. Không dùng hình chữ nhật R làm bằng chứng “79% bản đồ bị che”. Cũng chưa có ảnh combat để báo tổng thực khi Vương, 2 Ấn và Tẩy cùng hiện; không lấy ảnh prep làm mẫu combat.

### 2.5 Nguyên nhân ưu tiên xử lý

1. **Thiếu chính sách hiển thị theo mode:** học lấy phím và pause, nhưng cửa hàng/HUD vẫn chiếm thị giác phía sau.
2. **Nhiều chỗ hiện cùng dữ kiện:** từ ở ô chiêu rồi lặp trong khung học; tiền ở HUD và shop; thanh Chân Nguyên ở HUD và trạng thái ô 5. Có thể giữ dữ liệu mà bỏ nền/lặp không cần thiết.
3. **Thanh không thực sự có ngân sách bề ngang:** 5 ô, extra và 3 ô đồ ghép flex; chữ tiếng Việt dài nowrap và font từ có sàn 28 px. Tăng viewport không tự chữa quá tải.
4. **Chọn “chỗ ít xấu nhất” không tạo ra chỗ trống:** `chooseSpot` tìm trong ba góc, khi không góc nào sạch sẽ chọn chi phí thấp nhất. Thẻ đợt di chuyển không bảo đảm không che bất kỳ đường/ô nào.
5. **Cần coi chữ là hành động chiến đấu:** bỏ hết chữ thành icon làm khó gõ; đưa chữ lên mọi quái làm sân đầy. Cần giảm nội dung phụ và số panel, giữ chữ có thể dùng ngay.

## 3. Nghiên cứu tham chiếu: nguyên tắc, không chép ảnh

Chỉ dùng nội dung nguồn; không tải ảnh thương mại vào bộ tham chiếu hoặc công cụ tạo ảnh. Các bài học áp dụng cho Tu Tiên là **suy luận của báo cáo**, không phải nguồn xác nhận game này sẽ dễ chơi hơn.

| Tham chiếu | Điều kiểm chứng được và giới hạn | Nguyên tắc áp dụng |
|---|---|---|
| **The Typing of the Dead: Overkill** | Manual SEGA tr.6–9: từ trước địch; chữ đầu khóa đích; phần đã gõ đổi sắc; có cách hủy khóa. Không đánh đồng luật bản thường với Hardcore về khoảng trắng/lỗi. [Manual chính thức](https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/246580/manuals/TOTDO_STEAM_MANUAL_ENG.PDF?t=1763675367) | Vị trí chữ phải giải thích được hành động và đích; tiến độ nằm ngay nơi đọc. Không suy rằng cách này chịu được hàng chục quái cùng mang chữ |
| **Epistory** | Designer David Bailly mô tả ưu tiên địch theo tốc độ/khoảng cách và lựa chọn magic; trận có giai đoạn đứng chiến đấu. [Phân tích của designer](https://david-bailly.com/portfolio/typing-games-how-and-why/7/). Nhà phát hành xác nhận điều khiển bằng bàn phím và độ khó thích ứng. [Trang game](https://store.steampowered.com/app/398850/Epistory__Typing_Chronicles/) | Giữ quyền chọn từ có ý nghĩa; bớt yêu cầu thao tác đồng thời. Không ép người chơi Tu Tiên vừa chạy liên tục vừa đọc nhiều bảng |
| **Nanotale** | Cùng designer mô tả chữ trên đối tượng, ghép effect/shape/modifier, thêm di chuyển và slow motion khi di chuyển để giảm chia chú ý. [Nguồn designer](https://david-bailly.com/portfolio/typing-games-how-and-why/7/) | Cụm từ có giá trị khi mỗi thành tố thay chiến thuật. Không chỉ nối dài từ để làm tuyệt kỹ trông lớn; không nhập cơ chế slow motion vào Tu Tiên nếu chưa duyệt đổi luật |
| **ZType** | Đã xác minh nguồn tác giả, game gốc và cảm hứng typing shooter. [PhobosLab](https://phoboslab.org/log/2011/01/z-type), [game gốc](https://zty.pe/). **Từ trí nhớ, chưa kiểm chứng trực tiếp trong lượt này:** nhãn từ đi với tàu địch và gõ chọn đích; web đọc không lấy được trạng thái canvas | Dùng như giả thuyết so sánh nhãn gắn địch; không dùng làm bằng chứng mật độ nhãn, font, % HUD hay độ dễ học |
| **Kingdom Rush** | Trang do Ironhide đăng hướng dẫn xây tháp đánh địch, tiền từ hạ địch, phím riêng cho spell và hủy lựa chọn. [Hướng dẫn nhà phát triển](https://www.kongregate.com/en/games/ironhidegames/kingdom-rush?permalink=kingdom-rush&set_locale=true&uploaded_by=ironhidegames). **Từ trí nhớ, chưa kiểm chứng bố cục trực tiếp:** menu tròn quanh ô xây | Mua/xây là tác vụ lựa chọn có thể hủy; menu chỉ cần hiện khi thao tác. Không sao chép phím chữ `P` vào typing game; không khẳng định popup quanh trụ luôn thoáng |
| **Bloons TD 6** | FAQ ghim của `samninjakiwi [developer]` liệt kê các phím chọn tháp, nâng đường, bán, start và pause; bài ngày 18/12/2018, không bảo đảm mapping của mọi bản hiện nay. [FAQ nhà phát triển](https://steamcommunity.com/app/960090/discussions/0/3561682880014875212/). **Từ trí nhớ, chưa kiểm chứng bố cục bản hiện tại:** dải tháp cạnh màn | Tách thao tác xây khỏi nhìn đường; nút trên màn có đường phím. Không mang Q–Y/A–G hay Space fast-forward sang Tu Tiên vì xung đột typing/nhịp |
| **Defense Grid: The Awakening** | Manual: tài nguyên ở trái trên; chọn ô đất → menu xây xuất hiện bên trái; chọn tháp → Upgrade. [Manual do trang game dẫn](https://store.steampowered.com/manual/18500), §§5–6 | Thông tin tổng gọn ở biên; thao tác chi tiết hiện sau lựa chọn. Chọn ô cần xem rõ ô đất chứ không chỉ đọc danh sách ô trong shop |
| **MOBA: League of Legends** | Riot nêu khả năng, đồ, tài nguyên và nơi truy cập shop; QWER dùng cho abilities. [Hướng dẫn Riot](https://www.leagueoflegends.com/en-gb/how-to-play/). **Từ trí nhớ, chưa kiểm chứng vị trí HUD của client hiện tại:** cụm kỹ năng phía dưới | Nhóm thông tin theo tần suất quyết định; quan sát battlefield là chính. Không áp QWER vào đây, không lấy minimap/hàng đồ MOBA làm lý do tăng panel |
| **ARPG / diegetic HUD** | Phân tích gốc của Marcus Andrews mô tả HUD trên trang phục/hologram của Dead Space, đồng thời đặt vấn đề lợi ích chức năng và UI kết hợp. [Game UI Discoveries](https://www.gamedeveloper.com/design/game-ui-discoveries-what-players-want) | Dấu chọn/vùng đích có thể nằm trong sân; chữ gõ vẫn có thể ở DOM ổn định. “Trong thế giới” không tự có nghĩa “đọc tốt”, không biến cả bài học thành vật thể 3D |

Nguyên tắc HUD có nguồn:

- **Phân lớp thông tin và cho xem chi tiết theo yêu cầu:** các lựa chọn cần nhận biết được; không buộc nhớ phím/ý nghĩa icon chỉ để dùng chức năng thường xuyên. [NN/g, Recognition and Recall](https://www.nngroup.com/articles/recognition-and-recall/). Suy luận áp dụng: từ sống luôn hiện; mô tả chiêu dài, lịch đợt và danh mục hàng chỉ khi cần.
- **Kích thước chữ và scaling độc lập với việc làm HUD gọn:** Microsoft nêu ngưỡng chữ PC/VR và khả năng phóng chữ, gồm chữ trong icon. [XAG 101](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/101). Giữ từ 28–32 px theo canon; không hạ chữ để đạt % che đẹp trên giấy.
- **Tương phản phải đúng trên mọi nền:** chữ và tín hiệu quan trọng cần tương phản đủ với nền thay đổi; màu không được là tín hiệu duy nhất. [XAG 102](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/102). Dùng miếng nền cục bộ cho chữ, không làm cả HUD mờ đến khó đọc.
- **Vùng an toàn:** tài liệu GDC 2004 giải thích safe region vì TV overscan; các con số console cũ không phải yêu cầu PC hiện tại. [Cross Platform UI Development](https://media.gdcvault.com/gdc04/slides/cross_platform_user_int.pdf), tr.5–6. Khoảng biên 2% dưới đây là lựa chọn thiết kế PC, còn vùng cấm đè là cổng/đường/Trận Tâm/telegraph thực tế, không phải chỉ một viền ngoài.

Kết luận nghiên cứu áp dụng: tách đọc để đánh, xem chi tiết, mua và kiểm nhớ thành các trạng thái rõ; dùng một nơi ổn định cho chữ thường và chỉ báo gắn sân cho quan hệ đích. Không có nguồn nào ở trên chứng minh “HUD dưới X% thì tự dễ chơi”; các ngưỡng sau là ngân sách để kiểm chứng.

## 4. Ba phương án phục vụ cùng mô hình M4

### 4.1 Quy ước chung và cách tính ngân sách

Các sơ đồ là **khung dây chữ**, không phải art/UI shipping. Khung quy chiếu 16:9, tọa độ chuẩn hóa `x,y,w,h` theo phần trăm viewport; bảng tọa độ mới là kích thước chính xác, ASCII chỉ mô tả vị trí. Tất cả giữ bản đồ hiện có phía sau; không cắt đường hay dựng lại map.

Diện tích một box = `w×h/100` phần trăm toàn màn. Ngân sách cộng các box không chồng; nếu nhãn trên sân có chồng thì lấy union, không cộng hai lần. Các % là **trần dự kiến cho bounding box UI** ở text scale 100%; không bao gồm cơ thể quái, VFX, damage number như thể đó là panel HUD. Chưa phải số đo sau dựng.

Ba phương án đều có:

- Bộ status nhỏ tổng **2,7%**: trái trên `(2,2,22,5)` =1,1%; giữa trên `(40,2,20,3)` =0,6%; phải trên `(78,2,20,5)` =1,0%, gồm đợt, Settings và Sound. Các giá trị sống vẫn nhìn thấy; chỉ mở mô tả dài khi cần. Mờ bớt khung trang trí lúc ổn định, không ẩn hoặc giảm tương phản chữ thiết yếu.
- Tối đa hai nhãn liên kết Ấn trên sân, mỗi box không quá `(12,5)` =0,6%; tổng **1,2%**. Tẩy có mục riêng trong dải; chỉ báo vị trí gọn, không thêm một thẻ lớn.
- Chỉ một mode học/shop/combat. Học chỉ khi dừng; shop chỉ prep/break. Không phủ một veil tối toàn sân khi mục đích là để còn xem cảnh tĩnh.
- Chế độ học dùng một chip mode `(40,2,20,3)` =0,6%, ẩn bộ status 2,7%. Shop giữ status 2,7%, dấu số của sáu ô xây có ngân sách tổng 0,6%; không còn dải combat phía sau.
- Dòng `stone · đá` trong vùng học là ngoại lệ tiếng Việt hợp lệ. Nút, nhãn mode, trạng thái và tên vật phẩm đều tiếng Anh. Icon phải lấy art thật đã được duyệt khi triển khai; chữ trong sơ đồ chỉ là chú thích.

### 4.2 A — Dải gõ thấp, ngăn hàng bên cạnh, thẻ học độc lập — khuyên dùng

```text
 A / COMBAT                         khung quy chiếu 1600 × 900
+--------------------------------------------------------------------+
| [Health / Energy]          [Core]       [Wave 2/6] [Settings] [Sound] |
|                                                                    |
|                    GIỮ NGUYÊN BẢN ĐỒ HIỆN CÓ                       |
|                                                                    |
|             địch thường: không nhãn từ                              |
|                   [seal word]                                      |
|                       |                                            |
|                địch đặc biệt được liên kết                          |
|                                                                    |
|                                                                    |
|                 vùng chiến đấu / báo đòn                            |
|                                                                    |
|                                                                    |
|                         hero / Core                                |
|                                                                    |
|                                                                    |
| [Strike: stone] [Line: ...] [Guard: ...] [Field: ...] [Ultimate: ...] |
| [seal / cleanse khi có] [nghĩa + IPA của từ khóa]      [1] [2] [3]   |
+--------------------------------------------------------------------+
 Shop: ngăn 24% W bên phải/trái; đóng dải gõ; thu ngăn lúc đặt ô.
 Learn: thẻ giữa 40% W × 56% H; ẩn shop, dải gõ và HUD chiến đấu.
```

| Trạng thái | Hình học thêm vào bộ chung | Diện tích dự kiến |
|---|---|---:|
| Đánh thường, đủ Ấn | Dải `(2,86,96,12)` =11,52%; status 2,7%; nhãn Ấn ≤1,2% | **≤15,42% toàn màn** |
| Đánh cao điểm | Thêm bar Thế `(40,6,20,3)` =0,6%; tối đa một thông báo `(40,10,20,3)` =0,6% | **≤16,62%** |
| Mua sắm | Ngăn `(74,10,24,70)` =16,8%; status 2,7%; số ô ≤0,6% | **≤20,10%** |
| Học / ôn | Card `(30,22,40,56)` =22,4%; chip mode 0,6%; các phần khác ẩn | **≤23,00%** |

**Khi nhìn quái và gõ:** dải nằm sát vùng thấp nơi giao chiến gần Trận Tâm; từ khóa, phần đã gõ, nghĩa/IPA gom một vùng. Dùng dấu chọn trên đích để nối hành động, không thêm khung học nổi trên sân. Không thể hứa mắt tuyệt đối không rời quái; khi địch còn ở đầu xa, vẫn phải liếc dải. Mục tiêu là một quãng nhìn ngắn và dự đoán được, không phải đọc chữ đang chạy quanh.

**Dải chứa đủ lựa chọn:** phần kỹ năng có 5 ô ổn định; phần ngoại lệ Ấn/Tẩy có chỗ dự trù; đồ 1/2/3 thu gọn sang phải. Từ sống không bị ẩn vì có ô hồi chiêu. Thu tên dài thành nhãn vai ngắn + art, tooltip đầy đủ lúc pause/chuột; không yêu cầu hover để biết từ nào được gõ. Giữ chữ ≥28 px ở 720p và tới 32 px ở 1080p, một dòng hint chỉ dành cho từ đang khóa. Cần kiểm wrap bằng từ dài 8 chữ, hai Ấn và Tẩy; nếu không đủ phải tăng band/reflow, không thu chữ nhỏ.

**Shop:** cửa hàng không mở sẵn trong mọi lúc nghỉ. Mở bằng Backquote hoặc nút; cùng một shop cho chuột và phím, không hai bề mặt song song. Ngăn đặt bên không che ô đang chọn; không nhảy bên khi người chơi đang mua. Bước đặt thu còn nhãn nhỏ để thấy toàn bộ ô. Toàn bộ thao tác dùng bảng phím §1.5; chữ không lọt sang chiêu. Đồng hồ nghỉ dừng khi shop mode hoạt động; cần giữ đúng lệnh `shop-open`/`shop-close` hiện hành.

**Học:** làm trước trận hoặc chọn `Review` lúc nghỉ. Nếu card giữa che đúng Core thì không gây mất địch đang chạy vì sim đã dừng, và chỉ một card hiện. Người muốn xem map đóng/bỏ qua được. Thẻ học không tự chen vào chiến đấu, đoạn lặng trước Vương hay lúc gõ dở.

**Đánh đổi:** band 12% H dành riêng cho chữ; để giữ nguyên map/camera hiện tại, tiếp tục cơ chế view inset đã có, chưa nới viewport/crop bản đồ. Khi triển khai, trước tiên cho nội dung mới nằm trong band đang có 13,33% thay vì thu inset về 12% ngay; khác biệt 1,33 điểm phần trăm là phần dự phòng, không phải đất mới được map vẽ thêm. “Thấy đầy đủ” phải xác minh cổng/địch/ô, không suy từ việc UI nhỏ hơn.

### 4.3 B — Bảng từ một cạnh và một dòng gõ thấp

```text
 B / COMBAT                         khung quy chiếu 1600 × 900
+--------------------------------------------------------------------+
| [Health / Energy]          [Core]       [Wave 2/6] [Settings] [Sound] |
|                                                                    |
| [Strike word]                                                      |
| [Line word  ]          GIỮ NGUYÊN BẢN ĐỒ                            |
| [Guard word ]                                                      |
| [Field word ]                                                      |
| [Ultimate   ]                         [seal word]                  |
| [Seal A     ]                              |                       |
| [Seal B     ]                          special foe                 |
| [Cleanse    ]                                                      |
|                                                                    |
|                                                                    |
|                           hero / Core                              |
|                                                                    |
|                                                                    |
|                       [word being typed / hint]                     |
|                                                                    |
|                                                                    |
+--------------------------------------------------------------------+
 Shop: thay bảng từ bằng ngăn 26% W; không giữ cả hai bảng.
 Learn: thẻ giữa 44% W × 58% H; các bảng khác đóng.
```

| Trạng thái | Hình học | Diện tích dự kiến |
|---|---|---:|
| Đánh | Cạnh `(2,14,18,68)` =12,24%; dòng khóa `(36.5,88,27,7)` =1,89%; status 2,7%; Ấn ≤1,2% | **≤18,03%** |
| Mua | Ngăn `(72,10,26,78)` =20,28%; status + số ô =3,3% | **≤23,58%** |
| Học | Card `(28,21,44,58)` =25,52%; chip mode 0,6% | **≤26,12%** |

Từ nằm cố định ở cạnh và dòng đang gõ gần vùng hero. Chiêu hồi không lấy chỗ của từ sống; đủ tối đa 8 hàng. Học trước chỉ prep, ôn chỉ break, shop thay hẳn bảng từ. Sử dụng đúng các phím ở §1.5; mũi tên chỉ chọn hàng khi **mode shop/học** đã lấy quyền, không dùng mũi tên đổi chiêu trong combat vì sẽ lấy mất di chuyển.

Ưu: bề ngang từ dư hơn, có thể đọc tên vai bên icon; nhiều hàng dễ scan theo cột. Nhược: mắt phải đi cạnh → sân → dòng thấp; một dải rộng 18% W có thể che cổng/sky route hay ô cơ quan của map hiện có. Chuyển map vào vùng 82% còn lại sẽ là đổi framing, **không đề xuất ở phiếu này**. Phương án chỉ dùng nếu đo polygon cho thấy cạnh đặt bảng thực sự không mang thông tin cần nhìn. Không chọn làm mặc định.

### 4.4 C — Bảng từ gần vùng giao chiến, mua tại ô đang chọn

```text
 C / COMBAT                         khung quy chiếu 1600 × 900
+--------------------------------------------------------------------+
| [Health / Energy]          [Core]       [Wave 2/6] [Settings] [Sound] |
|                                                                    |
|                    GIỮ NGUYÊN BẢN ĐỒ                               |
|                                                                    |
|                            enemy tide                              |
|                                                                    |
|                       [seal word]                                  |
|                                                                    |
|                                                                    |
|                         hero / Core                                |
|                  +---------------------------+                     |
|                  | Strike / Line / Guard     |                     |
|                  | Field / Ultimate / hint   |                     |
|                  +---------------------------+                     |
|                  [Seal A / Seal B / Cleanse]                        |
|                                                                    |
|                                                      [1] [2] [3]   |
|                                                                    |
+--------------------------------------------------------------------+
 Shop: popover 24% W × 38% H cạnh ô chọn; thu nhỏ khi xác nhận đặt.
 Learn: ngăn 28% W × 76% H ở cạnh; combat và shop ẩn.
```

| Trạng thái | Hình học | Diện tích dự kiến |
|---|---|---:|
| Đánh | Bảng `(31,54,38,24)` =9,12%; extra `(31,80,38,8)` =3,04%; đồ `(83,92,15,6)` =0,9%; status 2,7%; Ấn ≤1,2% | **≤16,96%** |
| Mua | Một popover 24×38 =9,12%; status 2,7%; số ô 0,6% | **≤12,42%**, chưa tính nếu phải nới để đủ hàng |
| Học | Ngăn 28×76 =21,28%; chip mode 0,6% | **≤21,88%** |

Ưu: từ gần hero/cụm giao chiến, popover mua ít diện tích tổng. Bảng từ là vị trí cố định trong một đợt, không đuổi theo hero hoặc con trỏ từng frame. Học trước/ôn chuyển sang ngăn cạnh lúc dừng, shop chỉ khi chọn ô. Keyboard dùng §1.5; mở shop từ Backquote chọn ô bằng ↑↓, không đòi click trụ; Esc hủy/lùi, Enter đặt.

Nhược quyết định: tổng % nhìn đẹp nhưng bảng có nguy cơ nằm ngay trên Core, địch sát đích và telegraph — đúng vùng owner cần quan sát. Dịch bảng để né đòn khi đang gõ lại phá ổn định đọc. Popover có thể che ô kế bên, sáu món thật + thông tin nâng/bán có thể vượt box 24×38. Không khuyên dùng cho toàn bộ kỹ năng; chỉ có thể mượn nguyên tắc “chi tiết theo ô chọn” cho shop của A. Không giảm map, đổi đường hoặc dời công trình để làm C hợp thức.

### 4.5 Bảng quyết định

| Tiêu chí | A: dải thấp | B: cạnh | C: gần giao chiến |
|---|---|---|---|
| Giữ mọi từ sống dễ thấy | Có, cần kiểm width cực hạn | Có, cần kiểm height/reflow | Có, cần kiểm hai hàng + hint |
| Liên kết từ → chiêu → đích | Dải ổn định + chỉ báo sân | Phải đảo mắt xa hơn | Gần nhưng có thể đè đích |
| Rủi ro che vùng quyết định | Thấp nhất nếu tận dụng band hiện có | Cổng/sky/ô ở cạnh | Cao quanh Core |
| Gần kiến trúc hiện tại | Cao | Trung bình | Thấp hơn |
| Combat / shop / learn (% V, 100%) | **15,42–16,62 / 20,10 / 23,00** | 18,03 / 23,58 / 26,12 | 16,96 / 12,42 / 21,88 |
| Khuyến nghị | **Dựng để owner thử trước** | Dự phòng nếu đo cạnh trống thật | Không chọn mặc định |

Các % toàn màn **không bằng % đất có giá trị bị che**. Riêng A, nếu dải được đặt ngoài vùng camera như cơ chế band sẵn có, phần panel phủ bên trong view còn lại là khoảng `(2,7+1,2)/86,67 = 4,5%`, cao điểm khoảng **5,9%**. Đây vẫn là dự kiến; chưa đo giao với hành lang. Shop/learn là sân tĩnh, không thể so % của chúng như một cảnh combat đang chạy.

## 5. Phương án chốt để tham khảo triển khai và rủi ro

**Codex khuyên A + mô hình M4**, chưa thay canon hay coi đã được owner duyệt. Giữ sự lựa chọn của 5 kỹ năng, các giới hạn học và Ấn hiện có; sửa cách xuất hiện, thứ bậc và lặp nội dung. Đây là mức thay đổi giải quyết đúng ảnh bị chê mà không cần tạo nền gameplay mới.

Các rủi ro và cách phân xử cụ thể:

| Rủi ro | Cách xử lý/kiểm chứng ở phiếu dựng sau |
|---|---|
| Nhãn vai ngắn làm người mới không biết skill nào | Mỗi ô có art riêng + tên vai ổn định + từ; dạy bằng một tình huống trước đợt. Tooltip đầy đủ có đường bàn phím khi pause; không chỉ icon |
| 8 từ sống + đồ + chữ 150% không vừa band | Reflow tối đa hai hàng, mở band lên khoảng 18–20% khi cần; không cắt từ, không giấu Ấn khẩn, không làm font dưới sàn. Ngân sách A 15,4–16,6% **không áp** cho chữ phóng. Tính lại vùng che riêng và kiểm map không bị crop |
| Từ gõ xong mà không thấy đòn vì `held/fizzled` | Trạng thái `Waiting for target` / phản hồi hết hiệu lực nằm cùng ô, không mở popup. Không báo đã gây damage nếu chỉ hoàn tất từ |
| Shop nhìn được nhưng che mất ô cần đặt | Chỉ một ngăn, có bước thu khi đặt; kiểm cả 6 ô, mỗi loại, bằng phím và chuột. Không dựa vào `chooseSpot` như bảo đảm không che |
| Gợi ý nghĩa lộ làm sai kết quả học | Cùng một nguồn `hint` cho vẽ UI và event; chỉ tính recall khi đúng loại tác vụ và không gợi ý. Không đổi 3 lần gặp thành 3 lần nhớ |
| Tự mở Học trước/Ôn khiến người chơi thấy bị ngắt | Đề xuất lời mời chủ động + lựa chọn rõ; việc thay auto-open cần ghi quyết định, giữ tùy chọn học và phần thưởng. Không khóa học vào timer 20 s |
| Dải gõ vẫn kéo mắt xa đầu hành lang | Đo hành vi nhìn/nhận biết, thử người gõ chậm; dùng tiến độ ở đúng dải và chỉ báo đích. Không thêm bản sao từ lớn bám quái thường |
| UI nhỏ, nhưng chữ tiếng Việt dài làm tràn | Làm pass tiếng Anh của bề mặt liên quan theo phiếu riêng/duyệt phạm vi; giữ nghĩa Việt trong học. Chuỗi hiện tại cần đổi gồm `HỌC TRƯỚC`, `Cửa hàng`, `Đợt`, `Sinh lực`, `Chân Nguyên`, `Nâng`, `Bán`, `Trống`, `Chờ đích`, `MỚI`, hướng dẫn phím và tên kỹ năng/vật phẩm. Proper name được giữ theo quy tắc |
| Source đang thay bởi làn khác | Đọc lại phase, keymap, camera projection, bố trí ô và checksum trước khi viết code; không làm theo số đo cũ như đã cố định |

## 6. Danh sách việc dựng — chưa thực hiện

1. **Chốt hợp đồng bằng một quyết định:** M4; không từ trên quái thường; một từ/chiêu hiện tại; không cụm/câu trong ô 5. Xác nhận lời mời học thay auto-open, mode shop/học loại trừ nhau và ngân sách font/diện tích. Không cần chờ art mới để xác nhận luồng.
2. **Đo baseline thật:** tại 1280×720 và 1920×1080 CSS px, DPR được ghi riêng, không chỉ kích thước file ảnh. Text 100/125/150%, phase prep+learn, break+review, shop+place, combat thường, combat Vương+2 Ấn+Tẩy theo trần hợp lệ, pause. Lấy `getBoundingClientRect`, visible state, pointer-events, polygon sân và owner ảnh/video mới; không mở URL flags để chấm acceptance.
3. **Một bộ điều khiển mode cho presentation và input:** combat/prepare/break/shop/learning/review/pause. Ẩn đúng presenter phía sau; phục hồi focus; timer solo dừng đúng lý do; không chỉnh sim damage hay thời điểm Cast để chữa UI.
4. **Dựng dải A trong band hiện có:** 5 vị trí kỹ năng ổn định, chỗ Ấn/Tẩy dự trù, đồ gọn, nghĩa/IPA tích hợp, hồi chiêu/held rõ. Loại khung học trùng, giảm nhãn phụ, giữ tất cả từ sống đọc được.
5. **Gom shop thành một bề mặt:** phím và chuột chung state; chọn món → ô → đặt, bước thu ngăn; nâng/bán giữ xác nhận; một dòng ví. Giữ sáu vị trí trên map.
6. **Dựng học/ôn trong mode riêng:** một card, không shop/skillbar phía sau, nút `Listen`, `Skip`, `Done`/hướng dẫn Esc đúng hành vi. Học trước gợi ý, Ôn giữ kiểm nhớ/nghe, không lộ từ ngoài card.
7. **HUD rút gọn và ngôn ngữ:** trạng thái thiết yếu ở biên, chi tiết đợt chỉ prep/break, cảnh báo một dòng có ưu tiên. Settings và Sound có nút art dùng kit đúng hợp đồng. Không dùng emoji/CSS shape làm icon sản phẩm; không mở một hướng art mới trong vé wiring.
8. **Kiểm tra hợp đồng và phím sau thay đổi:** một chữ cuối chỉ một Cast; composition không cast/submit; Esc lần đầu nhả khóa; 1/2/3 không dùng đồ khi làm câu hỏi; shop không đi/đánh; Cmd shortcut không bị nuốt; focus trở lại không tự tung chiêu. Kiểm timer và `hintUsed`/allowance/lịch gặp lại. Phiếu này không chạy các test đó.
9. **Kiểm UX với người thật trước khi nhận:** người chưa biết game giải thích được “gõ gì để làm gì”; thực hiện đánh/khiên/đổi đích/mua/đặt/học mà không phải đoán mode. Nhận ra địch đến Core và telegraph trong lúc gõ. So với baseline cùng kịch bản, không tăng lỗi gõ/thời gian xử lý nguy hiểm. Nếu không có eye tracking, gọi kết quả là nhận biết/phản ứng, không giả số đo mắt.
10. **Cổng bàn giao:** tại 100%, A union panel ≤17% V khi đánh cao điểm (đã gồm nhãn và thông báo dự kiến); học/shop chỉ khi dừng và không chồng nhau; không HUD phủ polygon Core/cổng/ô đặt/telegraph cần thao tác, trừ đúng nhãn chủ thể không che cue. Chữ lớn có budget riêng và không mất nội dung. Quay before/after để owner thấy; hai judge mù ≥8,5 trên host thật, bar 9 nếu thay bộ typing feedback dùng chung. Owner duyệt cuối. Hiện **chưa có PASS UX/visual**.

## 7. Tệp bàn giao, phần chưa làm và cách hoàn tất thư mục review

Đã tạo: **`docs/codex-queue/392-report.md`** — toàn bộ kết quả nghiên cứu, bảng đo, ba khung dây ASCII, luồng và backlog triển khai. Không tạo ảnh/video, không sửa game/docs Tu Tiên, không build/test, không đổi nhánh, commit hay thao tác Git bị cấm. Không gọi assistant bên ngoài hay mở thêm làn.

**Chưa thể ghi đúng đích:** thử tạo `ABOUT.md` tại thư mục dưới đây trả `PermissionError: [Errno 1] Operation not permitted`; thư mục review nằm ngoài writable roots. Không dùng symlink hay công cụ khác để vượt sandbox. Không thay thế ảnh gốc. Cần phiên có quyền ghi thư mục đó để chép ba sơ đồ tại §§4.2–4.4 ra ba file Markdown sau; nội dung và thông số đã có sẵn, không cần nghiên cứu lại:

```text
/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-16/tu-tien/ui-layout-research/
  392-layout-a.md   ← §4.1 + §4.2 (khung dây, các mode, diện tích)
  392-layout-b.md   ← §4.1 + §4.3
  392-layout-c.md   ← §4.1 + §4.4
  ABOUT.md          ← nội dung bên dưới
```

Nội dung `ABOUT.md` chờ ghi:

```yaml
purpose: Nghiên cứu lối chơi gõ chữ và ba bố cục UI/UX 16:9 cho phiếu 392; giữ nguyên bản đồ.
made-by: Codex, 16/11/2026
doc: /Volumes/SS990TPRO/htdocs/typing-game/docs/codex-queue/392-report.md
delete-when: Owner đã chọn bố cục và phiếu triển khai đã giữ lại sơ đồ cần dùng; giữ ảnh gốc do owner cung cấp.
```

Chưa chạy `node scripts/review-index.mjs`: không có tệp review nào ghi thành công; chỉ mục cũng ở ngoài vùng được phép ghi của phiên này. Khi hoàn tất chép trong phiên có quyền và phạm vi phù hợp, chạy script để dựng lại index theo luật thư mục review. Không có raw frame do phiếu này tạo nên không có gì để prune.

Owner cần xem trước: **§1.2–1.5** để quyết định lối chơi và chế độ, rồi **§4.2** cho bố cục A. Điểm cần quyết định là chấp thuận nền M4 và cách mời học/ôn; chưa phải duyệt art hoặc duyệt đổi bản đồ.

## Phụ lục: mốc source để phiên dựng đối chiếu lại

Các hash SHA-256 rút gọn được đọc trong phiên nghiên cứu; chỉ nhận diện snapshot, không dùng để khóa làn khác.

| Source từ `games/immortality-cultivation/` | Hash 12 ký tự |
|---|---|
| `src/ui/ban-quyet.ts` | `1bce2a7091c8` |
| `src/ui/learn-ahead.ts` | `f938f1ba55de` |
| `src/ui/learning-frame.ts` | `96567f1a661b` |
| `src/ui/hud.ts` | `ed1f96f646c8` |
| `src/ui/wave-card.ts` | `2aeb5fe32a12` |
| `src/ui/shop-strip.ts` | `792917e3a280` |
| `src/ui/shop-mode.ts` | `b1e7ef245d90` |
| `src/ui/screen-zones.ts` | `fe5e66c2dbd6` |
| `src/ui/styles/game-css.ts` | `7535634e7bf1` |
| `src/app/app.ts` | `c8e6d448d331` |
| `src/app/input-router.ts` | `6e68035b6eb7` |
| `src/content/rules.ts` | `e4fb3582ea12` |
| `src/content/data/stage-m0a.ts` | `e4e34b10c46b` |
