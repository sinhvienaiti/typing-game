# Phiếu 392b — Góc nhìn độc lập về lối chơi gõ chữ

## Tóm tắt

Khuyên giữ **mỗi từ hoàn thành kích hoạt đúng kỹ năng trong ô đã chọn**, nhưng luân phiên từ theo hồ sơ học; không cố định cả trận một từ cho một chiêu. Đây đã là nền của game hiện tại. Điểm còn thiếu có thể là cảm giác chủ động chọn thời điểm, không nhất thiết là thiếu thao tác.

Chuỗi 3–5 từ tạo nghi thức tung tuyệt kỹ, nhưng làm người gõ chậm chờ lâu, khó đổi sang tự vệ và dễ biến ôn từ thành chép danh sách. Không khuyên dùng cho chiêu thường hoặc chiêu cứu nguy.

Vạch chạy tạo cao trào rõ, đồng thời buộc người chơi chuyển từ đọc–gõ sang nhìn–canh. Áp sau mọi từ sẽ cắt nhịp luyện gõ và cạnh tranh chú ý với báo đòn. Chỉ nên **thử cho tuyệt kỹ, có thể tắt**, không làm thao tác bắt buộc để được tung chiêu đã gõ đúng.

Phương án lai ưu tiên thử: gõ một từ để chuẩn bị tuyệt kỹ, tiếp tục đánh bằng các từ khác, rồi ấn **Space khi tự chọn thời điểm**; chưa cần vùng Perfect/Great/Miss. So với bản có vạch chạy, cách này giúp xác định owner thích quyền chọn thời điểm hay thích thử thách phản xạ.

Đây là phân tích độc lập với phiếu 392, dựa trên mã nguồn và canon. Nhận định UX: **từ trí nhớ, chưa kiểm chứng**. Không dùng web, không sửa game, chưa làm lab.

## 1. Cơ sở hiện tại: game đang yêu cầu gõ gì?

Đọc ngày 16/11/2026; không đọc `392-report.md`. Nguồn cục bộ bên dưới là bằng chứng về luật, không phải bằng chứng rằng trải nghiệm đã hay hoặc dễ dùng. Mã đang được các agent khác chỉnh; báo cáo phản ánh phần đã đọc trong lượt này.

| Việc | Luật canon và phần mã đã đối chiếu |
| --- | --- |
| Đánh quái thường | Có đánh nền tự động. Quái thường không mang từ. Người chơi gõ từ trên Bàn Quyết để dùng chiêu mạnh hơn; không phải tìm chữ trên từng con. |
| Chọn chiêu | Bàn Quyết có 5 ô kỹ năng. Chữ đầu chọn/khóa mềm từ trong ô; các từ sống khác chữ đầu, không là tiền tố của nhau. Gõ xong từ tạo Cast cho đúng ô đó. Không cần gõ tên kỹ năng, bấm phím số chọn chiêu hay Enter xác nhận từ. |
| Ô 1 | Từ 3–5 chữ, đã thuộc/đến hạn/từ nền; mỗi từ nạp băng 3 kiếm, không hồi chiêu, tối đa 2 băng chờ. Đây khác đánh nền tự động. |
| Ô 2 | Từ 4–7 chữ, đang học/đến hạn, hoặc từ mới đã gặp trong trận; chiêu chính, hồi 8 giây. |
| Ô 3 | Từ quen 3–5 chữ; hộ thân hồi 15 giây hoặc thân pháp hồi 8 giây, chọn trước trận. |
| Ô 4 | Từ 4–7 chữ; vùng đánh/chậm, hồi 12 giây. Là ô duy nhất nhận từ mới trong trận, chỉ đợt 1–2 và còn ngân sách. |
| Ô 5 | Khi Chân Nguyên đạt 100 mới có từ 5–8 chữ, ưu tiên từ đến hạn/yếu. Một từ hoàn thành tung tuyệt kỹ; dùng hết thanh khi giải quyết Cast thành công. |
| Ấn và chữ khẩn | Là các từ riêng để xử lý mối đe dọa. Không nhận từ mới; cùng chia trần chữ sống. Cân bằng/Thử thách tối đa 8, Thư giãn/Học tối đa 5, còn bị giới hạn bởi bộ từ. |
| Nhắm chiêu | Có mục tiêu mềm; chiêu đất lấy con trỏ trên sân, nếu không thì chọn cụm đông nhất theo luật. Bàn phím thuần vẫn phải chơi được. |
| Gõ xong nhưng chưa có đích | Cast `held` tối đa 3 giây, chưa tốn hồi; sau đó `fizzled`. Đây là chờ đích tự động, chưa phải chủ động giữ chiêu chờ Space. |
| Chất lượng | Đã có Chớp/Hoàn hảo/Tốt/Vừa/Ẩu. Chớp xét tốc độ so với hồ sơ của chính người chơi, không có chí mạng ngẫu nhiên. |
| Học | Từ trong ô thay đổi theo bộ từ, loại ô và hồ sơ. Ngân sách từ mới tối đa 8/20 phút; mỗi từ mới cần gặp lại theo lịch. Một sự kiện học có chấm cho mỗi từ mỗi trận; gõ lại không đồng nghĩa thêm một lần nhớ nghĩa. |

Các điểm kiểm trực tiếp:

- [Canon §5–6](../games/tu-tien/00-canon.md): bảng phím, một từ/một Cast, phân ô, trần chữ, loại từ, chất lượng và Chân Nguyên; §9.3, §12.1: đánh nền và chiêu Kiếm; §17: học và gặp lại.
- [Nhập phím](../../games/immortality-cultivation/src/app/input-router.ts), nhất là `onKeyDown`; [bảng phím](../../games/immortality-cultivation/src/content/rules.ts), `KEYS`: mặc định chưa có hành động Space tung chiêu. Các phím số 1/2/3 dùng đan, phù.
- [Xử lý từ](../../games/immortality-cultivation/src/sim/words.ts), `typeKey` và `complete`: chữ cuối phát `word-complete`, chấm từ rồi tạo Cast; [Cast](../../games/immortality-cultivation/src/sim/cast.ts): giải quyết, giữ và hủy khi hết hạn.
- [Kỹ năng](../../games/immortality-cultivation/src/sim/skills.ts), `resolveCast`, `resolveUltimate`; [Chân Nguyên](../../games/immortality-cultivation/src/sim/chan-nguyen.ts); [dữ liệu trường phái](../../games/immortality-cultivation/src/content/data/school-kiem.ts).
- [Quy tắc từ từng ô](../../games/immortality-cultivation/src/typing/slots.ts), [chấm chất lượng](../../games/immortality-cultivation/src/typing/grading.ts), [nhịp theo người chơi](../../games/immortality-cultivation/src/sim/pace.ts).
- [Bàn Quyết](../../games/immortality-cultivation/src/ui/ban-quyet.ts): DOM cố định dưới màn, tên chiêu tách khỏi từ; [khung học](../../games/immortality-cultivation/src/ui/learning-frame.ts): từ đang gõ, nghĩa/IPA theo cờ gợi ý, phía trên Bàn Quyết.

**Phân biệt cần giữ:** “mỗi kỹ năng cần một từ” đã có; “mỗi kỹ năng luôn là cùng một từ” chưa phải luật hiện tại. Mã còn nhánh thử ô 2 `twin-pearl`, chỉ bật khi đầu trận yêu cầu; không coi nhánh thử đó là luật mặc định. Một số nhãn UI trong mã đã đọc vẫn là tiếng Việt; báo cáo chỉ đề xuất chữ người chơi đọc bằng tiếng Anh, không thực hiện lượt chuyển ngôn ngữ.

## 2. Cùng một thao tác, thời gian khác nhau rất lớn

Ước lượng sau dùng quy ước tính **5 ký tự = 1 WPM**, mỗi từ dài 5 chữ; chuỗi có Space giữa các từ. Công thức `t = 60 × số phím / (5 × WPM)`. Đây là phép tính tải nhập đơn giản, **không phải dự báo từ công thức E_eff của game**, chưa tính đọc, tìm ô, nghĩ nghĩa, sửa sai hoặc nhìn sân.

| Tốc độ | Một từ: 5 phím | Ba từ: 17 phím | Năm từ: 29 phím |
| --- | ---: | ---: | ---: |
| 15 WPM | 4,00 giây | 13,60 giây | 23,20 giây |
| 30 WPM | 2,00 giây | 6,80 giây | 11,60 giây |
| 60 WPM | 1,00 giây | 3,40 giây | 5,80 giây |
| 90 WPM | 0,67 giây | 2,27 giây | 3,87 giây |

Nếu thêm trung bình 0,8 giây chờ canh sau **mỗi từ**, riêng phần chờ chiếm khoảng 17%/29%/44%/55% chu kỳ ở bốn tốc độ trên. Người gõ nhanh chịu trần thông lượng rõ; người gõ chậm vẫn phải chịu thêm một bài phản xạ sau thời gian chuẩn bị dài. Không suy ra người chậm phản xạ kém: tốc độ gõ, trình độ tiếng Anh và khả năng canh nhịp là ba biến khác nhau.

Game đã điều nhịp theo hồ sơ nhưng `k` chỉ trong 0,75–1,30. Không thể mặc định bộ điều nhịp hiện tại sẽ bù được chuỗi dài gấp 3–5 lần, thời gian chờ canh, hoặc việc người chơi tạm không dùng được kỹ năng cứu nguy.

## 3. A — Một từ cho một kỹ năng cụ thể

### Một lần tung và nơi hiển thị

Ví dụ minh họa, không phải từ đang được cấp trong game: ô chiêu hiển thị tên **“Sword Wave”** và từ **`river`**. Người chơi:

1. Nhìn ô chiêu cần dùng, kiểm tra sẵn sàng và tình hình sân.
2. Gõ `r` để khóa ô, rồi `i v e r`.
3. Chữ `r` cuối hoàn thành từ, tạo Cast; không thêm Space. Khi có đích hợp lệ, chiêu phát theo thời gian của nó.
4. Ô hồi và xem trước từ tiếp theo; lỗi được sửa theo luật nhập, Esc nhả từ theo luật hiện tại.

Từ nằm trong ô cố định dưới sân; chỉ từ đang gõ được nhắc lớn ở khung học. Nghĩa tiếng Việt và IPA chỉ xuất hiện trong phần học theo preset. Không đưa thêm nhãn từ lên quái.

### Ưu, nhược và học từ

**Ưu:** phản hồi trực tiếp “mình hoàn thành từ → mình làm được việc”; chuyển sang hộ thân hoặc Ấn tương đối nhanh. Tên chiêu và vị trí ô ổn định giúp học thao tác dù từ đổi. Dải 15–30 WPM vẫn có phản hồi sau từng từ; 60–90 WPM còn việc chọn chiêu, mục tiêu và thời điểm, thay vì chỉ đua số ký tự.

**Hai biến thể có giá khác nhau:**

- **Một từ cố định cho mỗi chiêu:** dễ thuộc cách gọi và tạo liên tưởng, nhưng rất nhanh thành năm mật khẩu. Lặp nhiều `fire` có thể luyện chính tả `fire`; không chứng minh hiểu nghĩa, và có thể khiến người chơi né ô từ dài để tối ưu sát thương. Hai từ cùng chữ đầu cũng xung đột bộ định tuyến hiện tại.
- **Một từ đang được cấp cho mỗi chiêu:** giữ phân phối từ theo hồ sơ và lịch ôn. Đổi lại phải nhìn lại ô trước khi gõ; từ như `river` dùng để gọi kiếm không tự dạy nghĩa “river”. Từ học và tên chiêu phải khác kiểu chữ, không làm người chơi tưởng phải gõ tên chiêu.

Với người gõ chậm, vấn đề lớn là vừa tìm ô vừa giải nghĩa; nên giữ từ cứu nguy quen/ngắn và từ mới ở ô có thời gian học. Với người nhanh, tránh chỉ cấp từ ngắn nhất và để ô 1 lấn mọi lựa chọn. Nguyên tắc phù hợp là **vai trò chiêu cố định, từ ôn luân phiên**, có gợi ý nghĩa và ôn nhớ riêng; không khóa từ theo chủ đề nguyên tố nếu điều đó phá hồ sơ học.

**Rủi ro:** chọn ô bằng chữ đầu có thể dẫn tới gõ nhầm chiêu khi từ đổi; nhìn năm ô cùng lúc có tải thị giác; phản hồi hình/âm yếu vẫn khiến thao tác đúng cảm thấy nhạt. Thêm phím không tự chữa được ba vấn đề đó. A là lựa chọn ít thay luật nhất, nhưng chưa có bằng chứng chơi thử trong phiếu này.

## 4. B — Chuỗi 3–5 từ mới tung chiêu

### Một lần tung và nơi hiển thị

Ví dụ chuỗi ba từ đã quen **`river stone light`**, chỉ minh họa thao tác, không phải câu tiếng Anh tự nhiên:

1. Chọn chuỗi bằng chữ đầu của từ đang hiện trong ô tuyệt kỹ.
2. Gõ `r i v e r`, ấn **Space** để chuyển từ.
3. Gõ `s t o n e`, ấn **Space**.
4. Gõ `l i g h t`; chữ cuối tung một tuyệt kỹ. Không có Space cuối để tránh trùng vai trò với C.

Khung nhập nằm tại Bàn Quyết, hiển thị từ hiện tại, từ kế tiếp mờ và **“2/3”**; danh sách đã hoàn thành thu lại. Không bày đủ năm từ lớn ngang sân hoặc thành cột che góc nhìn. Backspace sửa từ hiện tại; lỗi không xóa cả chuỗi. Phải cho phép tạm dừng chuỗi ở ranh giới từ để dùng hộ thân/Ấn rồi quay lại; nếu chỉ cho hủy toàn bộ thì chi phí thoát quá cao.

### Ưu, nhược và học từ

**Ưu:** tăng cảm giác nghi thức, chuẩn bị sức mạnh lớn; tập chuyển từ và gõ liên tục. Có thể dùng cụm/câu ngắn tự nhiên nếu mục tiêu là luyện cụm từ, với nội dung đã được kiểm tra nghĩa và độ khó.

**Nhược:** chuỗi liền 3–5 từ bắt người chơi hoãn phản hồi chiến đấu lâu. Ở 15–30 WPM, bảng trên cho 6,8–23,2 giây ngay cả trước đọc/sửa sai; đó là khoảng cam kết lớn cho một hành động trong trận đang chạy. Ở 60–90 WPM, chuỗi ngắn dễ trở thành một mật khẩu dài; thách thức không còn tương đương giữa hai nhóm. Rút hồi chiêu hoặc tăng sát thương đơn thuần chưa bù được rủi ro không kịp tự cứu.

**Học:** thêm từ không tự tăng học. Danh sách rời luyện chép/chính tả; cụm tự nhiên mới có cơ hội luyện cách kết hợp từ. Không biến ngẫu nhiên các từ đến hạn thành câu vô nghĩa rồi gọi đó là học ngữ cảnh. Chuỗi nên dùng từ đã gặp, không đưa 3–5 từ mới vào tuyệt kỹ. Mỗi từ đã gõ vẫn cần được ghi nhận dù người chơi bỏ chuỗi; hoàn thành chuỗi không tự được đánh dấu “nhớ nghĩa”.

**Rủi ro luật:** hiện một từ hoàn thành là một Cast. B cần quy định lại quan hệ giữa từng từ, một lần tung cuối, Chân Nguyên và sự kiện học. Nếu mỗi từ vừa nạp Chân Nguyên vừa nhận đủ sức tuyệt kỹ cuối, có thể thưởng kép; nếu không có tác dụng gì cho tới cuối, dễ tạo cảm giác công sức bị giữ làm con tin. Chuỗi có tiến độ riêng cũng thêm một tài nguyên vào HUD.

**Đánh giá:** không khuyên thay các ô thường, hộ thân hoặc Ấn bằng B. Nếu owner thích nghi thức, chỉ thử chuỗi **3 từ quen cho tuyệt kỹ trong lab**; chưa bắt đầu với 5. Cụm 2 từ cho một loại chiêu sau MVP đã có trong canon, nhưng không phải bằng chứng chuỗi 5 từ sẽ phù hợp.

## 5. C — Gõ xong rồi canh vạch, ấn Space

### Một lần tung và nơi hiển thị

1. Người chơi gõ từ hoặc hoàn thành chuỗi; chữ cuối chuyển trạng thái sang **“Ready”**, chưa tung chiêu.
2. Có khoảng báo trước ngắn để chuyển chú ý; con trỏ chạy một lần trên thanh.
3. Người chơi ấn **Space** khi con trỏ vào vùng đích; hiển thị **“Perfect”**, **“Great”** hoặc **“Miss”**.
4. Tung một lần theo kết quả; hết thời gian cũng có kết quả xác định. Space không được kích lại chiêu.

Chỉ **một thanh canh** ở ngay vùng nhập đang dùng dưới sân, thay phần trạng thái của ô hoặc khung tập trung đã dành chỗ. Tên chiêu, từ đã gõ và “Press Space” vẫn thấy. Dùng biên vùng và chữ ngoài màu; không bắn thanh chạy lên giữa sân, không thêm thanh cho từng kỹ năng. Không thu nhỏ chữ 28–32 px để lấy chỗ. Bố cục phải kiểm ở cỡ chữ 125/150% trước khi kết luận “gọn”.

### Giá trị và chi phí

**Ưu:** có đỉnh căng thẳng ngắn, động tác kết thúc rõ, phân biệt được chuẩn bị và phóng chiêu. Người gõ chậm vẫn có thể đạt Perfect nếu cửa sổ canh không phụ thuộc tốc độ gõ. Nếu nhịp ăn khớp tín hiệu nhìn/nghe, kết quả dễ cảm thấy do mình điều khiển.

**Nhược:** sau mỗi từ, tay và mắt phải đổi nhiệm vụ. Đây là thử phản xạ thị giác sau gõ; nếu không gắn pha với nhạc, không nên gọi là cơ chế theo nhạc. Gắn vào nhạc lại thêm vấn đề người chơi hoàn thành từ ở pha bất kỳ: chờ nhịp kế làm độ trễ tung chiêu biến thiên.

Khi đông quái, người chơi phải ưu tiên giữa thanh, báo đòn, mục tiêu và từ tiếp theo. Hộ thân hoàn thành nhưng còn phải chờ thanh có thể khiến họ nhận đòn ngay trong lúc đã làm đúng phần gõ. Ngược lại, người nhanh bị chờ sau quá nhiều từ. Cấm gõ trong thanh sẽ giảm luyện tập; cho gõ tự do lại làm hai tác vụ tranh nhau và khó đọc kết quả. Vì vậy không dùng C cho mọi kỹ năng, đặc biệt không cho ô tự vệ và chữ khẩn.

**Học:** thao tác canh không có nội dung từ vựng. Nó có thể tạo động lực nhưng cũng kéo chú ý khỏi nghĩa/IPA đúng lúc vừa học xong. Kết quả Space phải là `timingGrade` riêng; tuyệt đối không biến Miss thành gõ sai, không giảm điểm nhớ từ, không cộng thời gian canh vào WPM hoặc hồ sơ Chớp.

### Công bằng và sức mạnh

Không suy WPM thấp thành cửa sổ rộng hoặc WPM cao thành cửa sổ hẹp. Nếu cần hỗ trợ, dùng lựa chọn nhịp riêng; không bắt người đang học tiếng Anh vượt thêm bài phản xạ để được sức mạnh tối thiểu. Cần hỗ trợ đổi phím và phương án không theo dõi chuyển động.

Bản **Miss mất toàn bộ tuyệt kỹ và thanh tài nguyên** có kịch tính nhưng mức phạt quá lớn so với mục tiêu học: sau thời gian tích thanh và gõ, một lần Space trượt xóa cả hành động. Không khuyên dùng. Bản đáng thử là Perfect/Great thêm thưởng nhỏ, Miss hoặc không ấn vẫn tung ở sức cơ bản. Ví dụ lab: `1,10 / 1,05 / 1,00` cho hệ số canh riêng, **chỉ là số thử**, chưa phải cân bằng. Tuy nhiên, nếu cộng lên M_q đang có, Chớp ×1,25 có thể thành ×1,375; phải đo lại. “Thưởng nhỏ” vẫn có thể thành bắt buộc trong thực tế nếu trận được cân quanh người luôn Perfect.

Với một thanh chạy 1,2 giây, chờ đúng vùng khoảng 0,8 giây cho một lần tuyệt kỹ là chi phí có thể thử. Cộng chi phí đó sau mỗi từ trong hàng chục lần/phút là bài toán khác. Không cho lặp vô hạn để săn Perfect; thất bại phải giải quyết nhanh, không giữ người chơi trong minigame.

### Độ trễ trên web: thiết kế cần kiểm, chưa đo

Các nguyên tắc dưới đây là **từ trí nhớ, chưa kiểm chứng** bằng web hoặc thiết bị trong phiếu này:

- Chấm theo mốc thời gian sự kiện phím và cùng trục thời gian với thanh; không lấy “frame kế tiếp xử lý tới đâu” làm kết quả. Một frame ở 60 Hz khoảng 16,7 ms, ở 30 Hz khoảng 33,3 ms theo phép chia; đó chưa phải toàn bộ độ trễ màn hình–phím.
- Mốc sự kiện không chữa được hình đã xuất hiện muộn. Phải đo cả cảm giác lệch thị giác, tải render và hàng đợi sự kiện; chưa có cơ sở hứa cửa sổ ±30 ms là công bằng.
- Thử ban đầu vùng Perfect tổng 200 ms, Great tổng 500 ms bao quanh; thanh 1.200 ms và báo trước 300 ms. Đây là giả thuyết lab, không phải chuẩn phản xạ hay thông số đã nghiệm thu. Chỉ thu hẹp nếu owner và người chơi đại diện vẫn thấy đúng tay.
- Nhận `keydown` một lần, bỏ giữ lặp; lấy quyền Space khi trận và thanh đang hoạt động để tránh cuộn trang/nút đang focus. Khi bảng học/cài đặt mở, không cướp Space của bảng. Blur/dừng phải dừng hoặc hủy lượt canh có quy tắc, không tự phạt Miss khi người chơi mất focus.
- Khi B dùng Space phân cách, phải phân biệt “giữa các từ” và “đang canh”; không tái sử dụng Space còn giữ hoặc lần phân cách vừa tới để chấm ngay. Không buffer một Space gõ sớm rồi tự đạt Perfect. Chỉ một lượt canh hoạt động, một lần giải quyết và một lần tiêu tài nguyên.
- Nếu đưa vào sim, thời điểm chấm và lệnh phải ghi đủ để replay ra cùng kết quả. Không đưa đồng hồ trình duyệt trực tiếp vào sim tất định 60 Hz. Dừng hình không được nuốt phím hoặc khiến thanh và cách chấm chạy khác nhau. Online sau này cần hợp đồng riêng; không kết luận RTT quyết định solo hiện tại.

## 6. D — Gõ để chuẩn bị, Space để chọn thời điểm; không có vạch bắt buộc

Ý tưởng lai là lấy **quyền chủ động phóng** của C, giữ lượng gõ của A, bỏ bài canh phản xạ khỏi đường mặc định. Chỉ áp cho tuyệt kỹ, không phải tất cả chiêu.

### Một lần tung và nơi hiển thị

1. Chân Nguyên đầy, ô tuyệt kỹ cấp từ quen/đến hạn, ví dụ **`bright`**.
2. Gõ `b r i g h t`; từ được chấm và ghi sự kiện học ngay. Ô chuyển sang **“Ultimate ready · Space”**; chưa phóng và chưa tiêu thanh. Đây là trạng thái chuẩn bị mới, khác `held` chờ đích hiện nay.
3. Người chơi có thể tiếp tục gõ từ của ô 1/2/4, dùng hộ thân hoặc di chuyển. Tối đa một tuyệt kỹ đã chuẩn bị, không chuẩn bị lặp để lấy điểm/nạp tài nguyên.
4. Khi thấy cụm quái phù hợp, ấn **Space một lần** để phóng. Lấy vị trí người và điểm ngắm lúc phóng, không đóng băng mục tiêu từ lúc gõ xong. Có đích hợp lệ mới tiêu thanh; chưa có đích thì báo **“No target”**, vẫn sẵn sàng. Có thể dùng cách tự chọn cụm theo luật hiện tại để chơi không chuột.

Chỉ ô 5 đổi trạng thái và có chỉ dẫn Space cố định; không thêm thước, danh sách hay nhãn trên quái. Nếu muốn canh lực, đó là một nhánh tùy chọn riêng để so sánh trong lab, không đồng thời ép cả chuỗi dài và canh.

### Ưu, nhược, học và 15–90 WPM

**Ưu:** tách “tôi đã gõ được từ” khỏi “tôi muốn đánh lúc này”. Người 15 WPM có thể chuẩn bị trước, người 90 WPM không phải chờ vạch sau từng từ. Vẫn có một động tác chốt mạnh bằng Space, nhưng mắt được trả về sân. Từ vựng tiếp tục luân phiên theo hồ sơ, không phải nhớ mật khẩu.

**Nhược:** thêm trạng thái phải nhớ; có thể quên Space, lỡ ấn hoặc tích trữ tuyệt kỹ để làm đợt sau quá dễ. Chuẩn bị sớm xóa bớt rủi ro gõ giữa nguy hiểm, nên không thể coi đây là thay đổi miễn phí về cân bằng. Tốc độ gõ vẫn quyết định thời gian chuẩn bị, chỉ tránh cộng một cửa sổ phản xạ vào cuối.

**Rủi ro cần chốt trước triển khai:** trạng thái chuẩn bị chỉ giữ trong đợt hiện tại, không chuyển sang đợt kế; hết đợt trả ô 5 về chưa chuẩn bị, giữ Chân Nguyên theo luật hiện tại. Gục xóa chuẩn bị; pause giữ nó. Trong lúc đầy thanh/đã chuẩn bị không có lợi ích nạp vượt 100. Cần gợi ý Ready đủ rõ mà không nhấp nháy thúc ép. Nếu giữ tới hết đợt làm trải nghiệm chờ tối ưu quá mạnh, thử lại thời hạn giữ; không tự thêm đồng hồ đếm ngược ngay từ đầu.

Đây **không phải thay đổi một dòng**: phải tách hoàn thành từ, chuẩn bị và giải quyết Cast; nguồn gốc/mục tiêu lấy ở lúc phóng; học không bị phát lại khi phóng. Chưa triển khai hoặc chốt nó thành canon.

Một biến thể B mềm hơn, chỉ nên xét nếu D vẫn thiếu nghi thức: ba từ ôn được tích lũy qua các lượt gõ bình thường, mỗi từ vẫn tung chiêu thường, không bắt nhập liền ba từ. Ưu điểm là không khóa tự vệ; nhược điểm là gần trùng thanh Chân Nguyên đang có. Tôi chưa khuyên thêm bộ đếm này vì dễ tạo tài nguyên thừa và thưởng kép.

## 7. Kết luận đề xuất cho Claude/owner

| Phương án | Khuyên dùng ở đâu | Điều kiện quyết định |
| --- | --- | --- |
| A: một từ → đúng ô chiêu | Nền cho chiêu thường, tự vệ, Ấn; giữ từ luân phiên | Cải thiện độ rõ của chọn chiêu và phản hồi; không biến thành năm từ cố định. |
| B: nhập liền 3–5 từ | Chưa đưa vào trận; nếu thử, chỉ 3 từ quen cho tuyệt kỹ | Phải thắng được chi phí cam kết dài và cho ngắt để tự cứu. Không mặc định nhiều từ là học tốt hơn. |
| C: canh Space | Chỉ lab tuyệt kỹ, tùy chọn; chưa làm mặc định | So với D có thêm vui rõ rệt mà không gây nhìn lệch, mất nhịp và phạt người học. Miss vẫn có sức cơ bản. |
| D: chuẩn bị một từ → Space tự chọn lúc phóng | Ưu tiên thử trước C cho tuyệt kỹ | Owner thấy quyền chọn thời điểm đáng với trạng thái Ready mới; kiểm lại cân bằng chuẩn bị trước. |

**Không áp vạch chạy cho mọi kỹ năng. Chưa cần bỏ hẳn ý vạch chạy; khoanh nó vào thử nghiệm tuyệt kỹ.** Khuyến nghị sản phẩm lúc này là giữ A; bước thử kế tiếp ưu tiên D. Nếu C không vui hơn D một cách rõ ràng, bỏ vạch và giữ quyền chủ động. Nếu D cũng làm quên chiêu hoặc rối hơn, giữ cách chữ cuối tung ngay. Không thay luật đang chạy chỉ vì cơ chế mới nghe có vẻ nhiều điểm nhấn hơn.

Phản hồi hình, âm, phản ứng quái và cảm giác chiêu đáp đúng ý có thể là nguồn thiếu cao trào; phiếu này không kiểm tra chúng. Nếu nhập hiện tại đã căng mà người chơi vẫn thấy nhạt, tăng một bài kiểm tra Space có thể làm bận hơn mà chưa làm hay hơn.

## 8. Bài thử nhỏ cho owner — chỉ mô tả, chưa làm

**Câu hỏi duy nhất:** tuyệt kỹ thú vị hơn nhờ được tự chọn lúc phóng, hay nhờ canh đúng vùng? Không xây cả hệ kỹ năng mới để trả lời câu này.

### Bốn lượt đối chiếu

Một lab dùng cùng camera, quái, từ quen đã kiểm tra, đánh nền và hiệu ứng/âm hiện có; có cả đoạn thưa và đoạn đông, cùng một báo đòn cần dùng hộ thân. Đặt rõ **“Input experiment”**. Mỗi lượt 75–90 giây, cho 4 cơ hội tuyệt kỹ bằng lịch tài nguyên thử cố định; không ghi tiến trình/học thật. Không dùng kết quả lịch thử để kết luận cân bằng trận chính.

| Lượt | Chuẩn bị và phóng | Cần cảm nhận |
| --- | --- | --- |
| 1 — A | Một từ, chữ cuối tự tung | Mốc so sánh hiện tại. |
| 2 — D | Một từ, Ready, Space tự chọn lúc tung | Quyền chủ động có đủ tạo điểm nhấn không? |
| 3 — C | Một từ, báo trước rồi vạch; Space canh, hết lượt vẫn tung cơ bản | Niềm vui thêm có lớn hơn gián đoạn và nhìn lệch không? |
| 4 — B | Ba từ quen liền, chữ cuối tung; cho ngắt sang hộ thân rồi quay lại | Nghi thức hay sự chờ đợi? Người chậm có bỏ chuỗi không? |

Giữ chiêu thường/hộ thân theo A trong cả bốn lượt. C chỉ dùng các hệ số thử đã nêu, chưa thay đổi M_q của từ. B không tăng sát thương trong lượt đầu để thấy riêng chi phí nhập; nếu muốn thử B mạnh hơn, làm lượt phụ và báo rõ đã đổi hai biến. Cả bốn dùng cùng hình/âm để tránh hiệu ứng đẹp hơn bị nhầm là input hay hơn.

Cho 2 lần làm quen mỗi cơ chế. Đảo thứ tự lượt giữa người chơi; dùng các bộ từ tương đương và đổi chéo để giảm lợi thế nhớ lại cùng từ. Owner tự chơi trước để chọn hướng; để nói về 15–90 WPM cần người gõ thật ở các nhóm 15–30, 31–60, 61–90. Bot gõ chậm hoặc owner cố tình gõ chậm chỉ đo được thời gian cơ học, không thay tải nhận thức của người mới.

### Ghi ít nhưng đúng thứ cần quyết

- Thời gian từ chữ đầu → sẵn sàng, sẵn sàng → phóng; tách thời gian sửa và chờ canh khỏi WPM.
- Độ chính xác từ; số bỏ dở; số lần hộ thân/báo đòn bị lỡ khi đang nhập hoặc canh. Ghi sự kiện để owner xem lại, không suy nguyên nhân từ số damage đơn thuần.
- Với C: tỉ lệ Perfect/Great/Miss, Space sớm, giữ lặp, chênh lệch cảm giác sớm/muộn; thêm lượt 30/60 FPS và bàn phím owner đang dùng. Không dùng một số trung bình che hết nhóm chậm.
- Với D: lần quên Ready, ấn nhầm Space, thời gian giữ chiêu; owner có nhìn sân và chọn cụm chủ động hơn không?
- Sau mỗi lượt hỏi ngắn: **“Control”**, **“Enjoyment”**, **“Distraction”** theo thang 1–5; hỏi họ muốn chơi thêm lượt nào và vì sao. Các câu khảo sát trong lab là tiếng Anh.
- Ôn rất ngắn sau lượt bằng nghĩa → từ, dùng bộ từ tương đương; đây chỉ là tín hiệu phụ. Một buổi ngắn không chứng minh khả năng nhớ dài hạn; nếu cần kết luận học, phải có lần kiểm lại sau.

**Cổng chọn hướng, số thử chứ chưa nghiệm thu:** cơ chế mới được owner ưu tiên và tăng ít nhất 1 điểm Enjoyment/5 so với A sau làm quen; không giảm độ chính xác quá 3 điểm phần trăm và không thêm quá 1 lần lỡ tự vệ trong một lượt so với A ở cùng người. Xem từng lượt và lời giải thích vì bốn cơ hội tuyệt kỹ là mẫu nhỏ. C chỉ đi tiếp nếu còn được ưu tiên hơn D; ưu thế chỉ ở nhóm gõ nhanh chưa đủ để đổi mặc định cho mọi người. Nếu kết quả không rõ, giữ A và thu thêm quan sát, không gọi là PASS.

Đây là cổng chọn **cơ chế để tiếp tục**, không thay hai lượt chấm mù theo mức 8,5 cho sản phẩm nhìn/nghe trong play host. Không phát sinh art, video, audio hoặc tài nguyên mới trong phiếu này.

## 9. Phạm vi bàn giao

Chỉ tạo `docs/codex-queue/392b-report.md`. Không đọc báo cáo 392; không sửa source, canon, script hay test; không tạo media, không chạy build/bộ test, không đổi nhánh hoặc thực hiện lệnh Git bị cấm. Không gọi Gemini/ChatGPT bên ngoài hoặc agent phụ. Không có URL web hay dẫn chứng thương mại được bịa; nhận định UX/học và nguyên tắc độ trễ ngoài nguồn cục bộ đều là **từ trí nhớ, chưa kiểm chứng**, cần lab/người chơi để xác nhận.

Owner/Claude cần xem trước: lựa chọn **A làm nền, D thử trước, C chỉ thử ở tuyệt kỹ**, và mức chấp nhận cho Miss. Chưa có cơ chế nào mới được triển khai hay được chấp nhận về cảm giác chơi trong báo cáo này.
