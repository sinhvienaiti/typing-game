# Phiếu 436f — Nữ chính: thân nền v3 và bốn bảng trang phục ba góc

Ngày: 17/11/2026. Đã có đủ **5 bảng bàn giao**. Runner tạo năm bảng bằng 5 lượt `image_gen`; phiên tương tác trùng phiếu đã gọi thêm 2 lượt cho thân nền trước khi phát hiện runner, nên **tổng thực tế là 7/8 lượt**, gồm một lượt sửa. Bám thân v3 và bốn bộ 436e đã được owner duyệt; không mở hướng thiết kế mới. Đây là bộ nguồn 2D giao để xem trước khi dựng 3D, chưa phải nghiệm thu mô hình hoặc rig.

## Ảnh và prompt

Thư mục: `/Volumes/SS990TPRO/htdocs/typing-game/games/immortality-cultivation/art-src/heroine/fashion/`.

| Ảnh PNG mới | Prompt thực gửi công cụ |
| --- | --- |
| [base-body.v3-turn.v1-try1.png](../../games/immortality-cultivation/art-src/heroine/fashion/base-body.v3-turn.v1-try1.png) | `base-body.v3-turn.v1-try1.prompt.txt` |
| [crimson-bride-turn.v1-try1.png](../../games/immortality-cultivation/art-src/heroine/fashion/crimson-bride-turn.v1-try1.png) | `crimson-bride-turn.v1-try1.prompt.txt` |
| [moon-blade-turn.v1-try1.png](../../games/immortality-cultivation/art-src/heroine/fashion/moon-blade-turn.v1-try1.png) | `moon-blade-turn.v1-try1.prompt.txt` |
| [jade-noble-turn.v1-try1.png](../../games/immortality-cultivation/art-src/heroine/fashion/jade-noble-turn.v1-try1.png) | `jade-noble-turn.v1-try1.prompt.txt` |
| [shadow-spider-turn.v1-try1.png](../../games/immortality-cultivation/art-src/heroine/fashion/shadow-spider-turn.v1-try1.png) | `shadow-spider-turn.v1-try1.prompt.txt` |

Cả năm PNG đều **1536×1024**, sao chép nguyên bản từ đầu ra công cụ; đã đối chiếu SHA-256. Nội dung năm tệp prompt khớp chuỗi thực gửi, gồm đường dẫn và vai trò ảnh đầu vào. Không hậu kỳ mặt, cơ thể hoặc trang phục trên PNG.

Mỗi lượt đều nhận trực tiếp chân dung `/Volumes/SS990TPRO/htdocs/typing-game-review/owner-review/2026-11-12/tu-tien/heroine/chan-dung-A.png` làm thẩm quyền khuôn mặt, `base-body.v3-try1.png` làm thẩm quyền thân và tỷ lệ, cùng lookbook `crimson-bride.v1-try1.png`, `moon-blade.v1-try1.png`, `jade-noble.v1-try1.png` hoặc `shadow-spider.v1-try1.png` đúng bộ. Riêng bảng thân, ảnh thứ ba lặp lại thân v3 để chỉ định lớp đồ nền. Không đưa ảnh game khác hoặc ảnh bên thứ ba vào công cụ.

Tạo thêm bảng thân vì v3 cũ tuy đã có ba góc nhưng còn thước và bóng chân. Bản mới bỏ hai phần này, giữ đồ nền xám than, tóc búi và giày thấp.

## Tờ ghép để xem

- [heroine-turnarounds-436f.jpg](/private/tmp/typing-game-436f/heroine-turnarounds-436f.jpg), **1536×5330**: từ trên xuống thân v3, Crimson, Moon, Jade, Shadow. Giữ nguyên kích thước từng PNG, chỉ thêm nhãn ngoài ảnh.
- [heroine-face-check-436f.jpg](/private/tmp/typing-game-436f/heroine-face-check-436f.jpg), **3080×316**: chân dung A rồi từng cặp mặt trước/nghiêng của năm bảng; chỉ cắt và phóng to để nhìn, không chỉnh mặt.
- [ABOUT.md](/private/tmp/typing-game-436f/ABOUT.md) ghi mục đích, người tạo, báo cáo và điều kiện dọn. Tệp thử ghép `heroine-faces-436f.jpg` cắt nhầm nền, không phải tệp giao; giữ nguyên, không xóa hoặc ghi đè.

Sandbox không cho ghi thư mục review bên cạnh repo, nên dùng đúng vị trí dự phòng của phiếu. Chưa chuyển sang review hoặc chạy trình dựng chỉ mục. Khi chuyển, dùng thư mục `owner-review/2026-11-17/tu-tien/heroine-turnarounds-436f/`, chuyển cả `ABOUT.md`, rồi chạy `node scripts/review-index.mjs`.

## Độ giống mặt và tính nhất quán

Đã xem cả năm PNG, bảng tổng và bảng cắt mặt. Các góc trước có cùng hướng tạo hình: mắt nâu dáng hạnh nhân, lông mày mảnh, sống mũi nhỏ, môi đầy vừa, cằm thuôn và tóc mai tương tự. Các góc nghiêng giữ dáng trán–mũi–môi–cằm khá sát nhau; không thấy một bảng đổi rõ sang nhân vật khác. Mặt của Crimson và Jade gần thân nền; Shadow có cảm giác mắt sắc hơn nhẹ. Khăn Moon làm thay đổi độ tương phản vùng mắt nên khó so trực tiếp hơn.

**Không thể xác nhận “giống hệt” chân dung A chỉ bằng quan sát:** chân dung A là góc ba phần tư, còn nguồn mới là trước/nghiêng; bản mới có nét dựng hình mềm và đều hơn, độ mở mắt, môi và đường hàm vẫn có sai khác nhỏ giữa ảnh. Không gán phần trăm nhận dạng hoặc tự tuyên bố đã khóa danh tính tuyệt đối. Owner cần xem tờ cắt mặt, đặc biệt mắt của Shadow và mặt dưới khăn Moon. Chưa có hai giám khảo độc lập và không tự chấm đạt 8,5.

Mỗi bảng có thứ tự trước–nghiêng nhìn sang phải ảnh–sau. Góc sau là lưng thật, không thấy mặt. Tay tách thân theo dáng chữ A, chân tách nhẹ; hình chiếu nghiêng làm tay/chân chồng nhau một phần. Nền xám, ánh sáng đều; không thấy thước, chữ, watermark, hào quang hoặc bóng đổ nền. Các mốc khớp và tỷ lệ được giữ theo hướng v3; chưa đo hình học 3D hay xác nhận mọi góc đúng 30° tuyệt đối.

## Các ô trang phục và chỗ cần lưu ý khi tách mô hình

| Bảng | Tóc | Đầu | Áo / thân dưới | Đai | Giày | Phụ kiện và phần bị che |
| --- | --- | --- | --- | --- | --- | --- |
| Thân v3 | Búi đen gọn, tóc mai; thấy gáy và búi sau | Không trang sức | Bodysuit xám than kín cổ, sát nách; biên cổ/nách/hông rõ | Không | Giày bệt xám than, thấy trước/nghiêng/sau | Không; dùng làm thân chung, không dùng hình khối quần áo thay giải phẫu bên trong. |
| Crimson Bride | Búi đen, tóc mai | Quan phượng vàng–đỏ, hoa tai, choker ren | Váy đỏ thẫm trễ vai, ren hoa hồng, phượng/mẫu đơn vàng, xẻ chân trái; găng vàng dài | Khóa hoa vàng, chuỗi hạt và tua đỏ | Mũi nhọn đỏ, viền vàng, dây cổ chân đính đá; gót rõ ở góc nghiêng | Voan đỏ là ô riêng: thấy mép thêu, điểm treo đầu và lớp rủ sau. Voan trong che phủ phần lớn lưng và thêu sau váy; tà dài che giày sau. Cần tách voan, găng, chuỗi/tua và váy thành các lớp riêng. |
| Moon Blade | Búi đen | Quan trăng bạc, hoa nhỏ, chuỗi pha lê/tua trắng | Áo trắng bạc cổ cao, ô ngực và khuy bạc; quần ngắn đen, tất mỏng; áo choàng xanh bạc bất đối xứng vai phải | Khóa trăng, dây pha lê, tua trắng | Cao gót bạc, đá xanh, gót sau rõ | Khăn mắt trong có biên trên/dưới và nút buộc sau riêng. Kiếm/vỏ ở hông trái; áo choàng vai phải thấy cả sau, nhưng che một phần tay và hông. Tách khăn, quan, giáp vai, áo choàng, tất, đai đùi, kiếm/vỏ và tua. |
| Jade Noble | Búi cao đen | Trâm vàng–ngọc, hoa và chuỗi ngọc/tua ngắn | Áo xanh ngọc cổ đứng, vai chạm lộng vàng, tay rộng lót ngà, tà dài thêu hạc/hoa/mây; quần ngà | Đai xanh, khóa hoa vàng gắn ngọc; ngọc bội tròn lớn và tua dài | Giày xanh–vàng, đá ngọc, gót thấp | Tay áo rủ che một phần cẳng tay; tà sau che hông và phần lớn quần. Có đủ biên ngoài, không đủ mặt trong toàn bộ tay áo. Tách giáp vai, tay áo, thân/tà, đai, ngọc bội–chuỗi–tua. |
| Shadow Spider | Búi đen | Tiara vàng mảnh và chuỗi rủ | Corset da đen, cổ/yếm ren, hở eo nhẹ, nhiều dải váy đen–rêu; xẻ chân phải | Khóa mạng nhện vàng–ngọc, dây xích, hạt và tua | Cao gót đen, mạng vàng, dây cổ chân và đá xanh | Giáp cẳng tay phải; vòng bắp tay/vòng cổ tay và nét mực ở tay trái; đai đùi phải. Nhiều tà chồng che mặt sau chân. Tách corset, yếm ren, từng nhóm tà, đai, giáp/vòng và trang sức đùi; nét mực là dữ liệu bề mặt da. |

Các phía trái/phải trong bảng tính theo nhân vật. Thiết kế sau lưng do công cụ suy ra từ góc lookbook duy nhất; vẫn cần người dựng kiểm tra nối họa tiết, mặt trong vải, độ dày ren, va chạm lớp và vị trí bất đối xứng. Tờ ba góc không tự cung cấp mesh hay ô trang phục đã tách sẵn.

## Phần bỏ qua và bàn giao

Runner không dùng lượt sửa vì chưa thấy lỗi đổi mặt hoặc đổi bộ rõ rệt đủ để yêu cầu vẽ lại; giữ các sai khác nhỏ nêu trên cho owner đối chiếu. Phiên tương tác ngừng tạo thêm ngay khi phát hiện trùng phiếu để không nhân đôi bốn bảng trang phục. Không dựng Tripo, rig hoặc đưa vào game vì ngoài phiếu. Không sửa code/docs Tu Tiên, không chạy build/test, làm video, xóa/ghi đè ảnh cũ, đổi nhánh hoặc thực hiện thao tác ghi Git. Không gặp giới hạn công cụ.

## Hai ảnh từ phiên tương tác trùng phiếu

Hai phiên `01a1e866-9dab` (runner) và `01a1e866-a2fd` (tương tác) đã cùng nhận 436f. Phiên tương tác phát hiện trùng khi sao chép gặp PNG try1 đã có; không thay thế PNG của runner. Bộ năm bảng và tờ ghép bên trên giữ các bản try1 của runner.

| Ảnh bổ sung, không nằm trong tờ ghép chính | Kết quả |
| --- | --- |
| [base-body.v3-turn.v1-try1.png](/private/tmp/typing-game-436f/base-body.v3-turn.v1-try1.png) | Bản lỗi: công cụ lấy áo xanh–ngà và trang sức từ chân dung thay vì đồ nền. Giữ riêng trong thư mục tạm, không dùng làm nguồn Tripo. Prompt thật cùng thư mục, cùng tên `.prompt.txt`. |
| [base-body.v3-turn.v1-try2.png](../../games/immortality-cultivation/art-src/heroine/fashion/base-body.v3-turn.v1-try2.png) | Bản sửa: đúng bodysuit xám than, tóc búi, giày thấp, không thước; đủ trước/nghiêng/sau. 1536×1024, PNG nguyên bản. Prompt thật nằm cạnh ảnh. Là lựa chọn thân nền bổ sung, không thay bản try1 của runner. |

Bản sửa dùng thân v3 làm ảnh đích đầu tiên và chân dung A chỉ cho khuôn mặt; không dùng ảnh ngoài dự án. Mặt trước cùng hướng tạo hình với bộ chính nhưng vẫn cần owner đối chiếu với chân dung, không xác nhận danh tính tuyệt đối. Không tạo thêm bảng sau lượt sửa này. Tất cả ảnh của hai phiên đều được giữ, không xóa hoặc ghi đè.
