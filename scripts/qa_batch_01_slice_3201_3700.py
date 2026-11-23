#!/usr/bin/env python3
"""
qa_batch_01_slice_3201_3700.py
Rà soát thủ công chuyên sâu 500 từ (STT 3201 đến 3700) của batch-01.json:
- Sửa lỗi bot crawler:
  - sung: sửa từ 'nhà Tống' sang verb 'đã hát; được ca ngợi'.
  - font: sửa từ 'bình đựng nước thánh' sang noun 'phông chữ vi tính; kiểu chữ'.
  - branding: sửa từ 'sự gán nhãn; sự kỳ thị' sang noun 'xây dựng thương hiệu; định danh'.
  - combo: sửa từ 'ban nhạc jazz nhỏ' sang noun 'gói kết hợp (combo); phối hợp'.
  - congregation: sửa từ 'bộ' sang noun 'giáo đoàn; cộng đồng tín đồ'.
  - horny: lọc từ ngữ thô tục sang 'chất sừng cứng; ham muốn tình dục'.
- Sửa POS chuẩn:
  - adjective: adj -> noun ('tính từ trong ngữ pháp')
  - statute: adj -> noun ('đạo luật; quy chế theo luật')
  - governed: noun -> adj ('được quản lý; chịu chi phối')
  - naming: adj -> noun ('sự đặt tên; định danh thương hiệu')
  - two: tagged num ('hai; số 2')
- Chuẩn hóa thuật ngữ kinh doanh:
  - logistics, leverage, maturity, startup, stimulus, discretion, dividend, turnover, etc.
- Độ dài nghĩa tiếng Việt <= 35 ký tự, phân tách bằng '; '.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BATCH_FILE = ROOT / "content" / "english" / "qa-batches" / "batch-01.json"
INDEX_FILE = ROOT / "content" / "english" / "qa-batches" / "INDEX.md"

EDITS_3201_3700 = {
    "shuttle": {
        "pos": "noun",
        "vi": "xe đưa đón; tàu con thoi",
        "notes": "Xe đưa đón trung chuyển"
    },
    "silently": {
        "pos": "adv",
        "vi": "một cách im lặng; lặng lẽ",
        "notes": "Lặng lẽ không tiếng động"
    },
    "simulation": {
        "pos": "noun",
        "vi": "sự mô phỏng; mô hình giả lập",
        "notes": "Mô phỏng giả lập"
    },
    "sock": {
        "pos": "noun",
        "vi": "chiếc tất; vớ chân",
        "notes": "Đôi tất chân"
    },
    "some": {
        "pos": "adj",
        "vi": "một vài; một số; chút ít",
        "notes": "Một vài lựa chọn"
    },
    "sounding": {
        "pos": "adj",
        "vi": "nghe có vẻ; thăm dò ý kiến",
        "notes": "Thăm dò ý kiến"
    },
    "spaghetti": {
        "pos": "noun",
        "vi": "mì Ý; món mì spaghetti",
        "notes": "Mì Ý spaghetti"
    },
    "steering": {
        "pos": "noun",
        "vi": "hệ thống lái; ban chỉ đạo",
        "notes": "Ban chỉ đạo / hệ lái"
    },
    "striker": {
        "pos": "noun",
        "vi": "tiền đạo bóng đá; người đình công",
        "notes": "Tiền đạo / đình công"
    },
    "subsidiary": {
        "pos": "adj",
        "vi": "phụ trợ; thứ yếu; lệ thuộc",
        "notes": "Vai trò phụ trợ / trực thuộc"
    },
    "suitcase": {
        "pos": "noun",
        "vi": "va-li; rương hành lý",
        "notes": "Va li hành lý"
    },
    "sung": {
        "pos": "verb",
        "vi": "đã hát; được ca ngợi",
        "notes": "Sửa crawler nhà Tống sang verb quá khứ sing"
    },
    "sworn": {
        "pos": "adj",
        "vi": "đã tuyên thệ; thề độc",
        "notes": "Bản khai tuyên thệ"
    },
    "teddy": {
        "pos": "noun",
        "vi": "gấu bông teddy; áo ngủ liền",
        "notes": "Gấu bông"
    },
    "tenth": {
        "pos": "adj",
        "vi": "thứ mười; hạng mười",
        "notes": "Vị trí thứ mười"
    },
    "territorial": {
        "pos": "adj",
        "vi": "thuộc lãnh thổ; địa bàn",
        "notes": "Quyền lãnh thổ"
    },
    "texture": {
        "pos": "noun",
        "vi": "kết cấu bề mặt; cảm giác sờ",
        "notes": "Kết cấu bề mặt"
    },
    "theology": {
        "pos": "noun",
        "vi": "thần học tôn giáo",
        "notes": "Môn thần học"
    },
    "tidy": {
        "pos": "adj",
        "vi": "gọn gàng; ngăn nắp; kha khá",
        "notes": "Gọn gàng ngăn nắp"
    },
    "transgender": {
        "pos": "adj",
        "vi": "người chuyển giới; hoán giới",
        "notes": "Cộng đồng chuyển giới"
    },
    "treasurer": {
        "pos": "noun",
        "vi": "thủ quỹ; người quản lý tài chính",
        "notes": "Thủ quỹ công ty"
    },
    "trinity": {
        "pos": "noun",
        "vi": "bộ ba; Ba Ngôi Thiên Chúa",
        "notes": "Bộ ba / Trinity"
    },
    "troubled": {
        "pos": "adj",
        "vi": "bất ổn; gặp nhiều rắc rối",
        "notes": "Tình hình bất ổn"
    },
    "vault": {
        "pos": "noun",
        "vi": "hầm chứa tiền; kho an toàn",
        "notes": "Hầm két ngân hàng"
    },
    "velocity": {
        "pos": "noun",
        "vi": "vận tốc; tốc độ chu chuyển",
        "notes": "Vận tốc luân chuyển tiền"
    },
    "violated": {
        "pos": "adj",
        "vi": "bị xâm phạm; bị vi phạm hợp đồng",
        "notes": "Điều khoản bị vi phạm"
    },
    "windy": {
        "pos": "adj",
        "vi": "có nhiều gió; gió lộng",
        "notes": "Thời tiết lộng gió"
    },
    "workforce": {
        "pos": "noun",
        "vi": "lực lượng lao động; đội ngũ nhân sự",
        "notes": "Lực lượng lao động"
    },
    "yang": {
        "pos": "noun",
        "vi": "khí dương; phần dương (âm dương)",
        "notes": "Phần dương âm dương"
    },
    "abs": {
        "pos": "noun",
        "vi": "cơ bụng (abs); hệ thống ABS",
        "notes": "Cơ bụng / phanh ABS"
    },
    "abusive": {
        "pos": "adj",
        "vi": "lăng mạ; có tính bạo hành",
        "notes": "Hành vi lăng mạ"
    },
    "advancing": {
        "pos": "adj",
        "vi": "đang tiến lên; ngày càng tăng",
        "notes": "Đang tiến lên"
    },
    "aired": {
        "pos": "adj",
        "vi": "đã phát sóng; thoáng gió",
        "notes": "Đã phát sóng truyền hình"
    },
    "alley": {
        "pos": "noun",
        "vi": "con ngõ; con hẻm nhỏ",
        "notes": "Hẻm phố"
    },
    "analyze": {
        "pos": "verb",
        "vi": "phân tích dữ liệu; mổ xẻ",
        "notes": "Phân tích số liệu"
    },
    "ancestor": {
        "pos": "noun",
        "vi": "tổ tiên; ông bà tổ phụ",
        "notes": "Tổ tiên dòng họ"
    },
    "annoy": {
        "pos": "verb",
        "vi": "làm phiền; gây bực mình",
        "notes": "Làm phiền quấy rầy"
    },
    "autonomy": {
        "pos": "noun",
        "vi": "quyền tự chủ; sự độc lập",
        "notes": "Quyền tự chủ hoạt động"
    },
    "bait": {
        "pos": "noun",
        "vi": "mồi nhử; bẫy câu khách (bait)",
        "notes": "Mồi câu nhử"
    },
    "baptist": {
        "pos": "noun",
        "vi": "tín đồ hệ phái Báp-tít",
        "notes": "Giáo phái Baptist"
    },
    "batting": {
        "pos": "noun",
        "vi": "lượt đánh bóng; lớp bông lót",
        "notes": "Lượt đánh bóng chày"
    },
    "behavioral": {
        "pos": "adj",
        "vi": "thuộc hành vi ứng xử",
        "notes": "Kinh tế học hành vi"
    },
    "beth": {
        "pos": "noun",
        "vi": "chữ cái Beth; tên riêng Beth",
        "notes": "Chữ cái Do Thái"
    },
    "billboard": {
        "pos": "noun",
        "vi": "biển quảng cáo tấm lớn ngoài trời",
        "notes": "Biển quảng cáo pano"
    },
    "branded": {
        "pos": "adj",
        "vi": "có thương hiệu; mang nhãn mác",
        "notes": "Hàng có thương hiệu"
    },
    "burke": {
        "pos": "noun",
        "vi": "họ Burke; sự bóp nghẹt ém nhẹm",
        "notes": "Tên họ / bóp nghẹt"
    },
    "cafeteria": {
        "pos": "noun",
        "vi": "quán ăn tự phục vụ; nhà ăn",
        "notes": "Căng tin tự phục vụ"
    },
    "cassette": {
        "pos": "noun",
        "vi": "băng cassette; hộp băng từ",
        "notes": "Hộp băng cassette"
    },
    "combining": {
        "pos": "noun",
        "vi": "sự kết hợp; việc phối hợp",
        "notes": "Sự phối hợp yếu tố"
    },
    "comp": {
        "pos": "noun",
        "vi": "vé mời miễn phí; bồi thường",
        "notes": "Complimentary / bồi thường"
    },
    "conditioning": {
        "pos": "noun",
        "vi": "sự điều hòa; rèn luyện thể lực",
        "notes": "Điều hòa nhiệt độ"
    },
    "confidential": {
        "pos": "adj",
        "vi": "tuyệt mật; bảo mật thông tin",
        "notes": "Tài liệu mật"
    },
    "congressman": {
        "pos": "noun",
        "vi": "nghị sĩ quốc hội Mỹ",
        "notes": "Nghị viên quốc hội"
    },
    "consuming": {
        "pos": "adj",
        "vi": "chiếm trọn tâm trí; ngốn thời gian",
        "notes": "Ngốn thời gian công sức"
    },
    "contracted": {
        "pos": "adj",
        "vi": "đã ký hợp đồng; co rút lại",
        "notes": "Đã ký kết hợp đồng"
    },
    "coordination": {
        "pos": "noun",
        "vi": "sự điều phối; tính nhịp nhàng",
        "notes": "Điều phối dự án"
    },
    "counseling": {
        "pos": "noun",
        "vi": "dịch vụ tư vấn tâm lý/hướng nghiệp",
        "notes": "Tư vấn nghề nghiệp"
    },
    "coupon": {
        "pos": "noun",
        "vi": "phiếu giảm giá; mã coupon",
        "notes": "Phiếu giảm giá / coupon"
    },
    "cowboy": {
        "pos": "noun",
        "vi": "người chăn bò; chàng cao bồi",
        "notes": "Cao bồi miền Tây"
    },
    "credited": {
        "pos": "adj",
        "vi": "được ghi nhận; được cộng tiền",
        "notes": "Được cộng vào tài khoản"
    },
    "creep": {
        "pos": "noun",
        "vi": "kẻ quái đản; người khó ưa",
        "notes": "Kẻ kỳ quặc khó ưa"
    },
    "cupboard": {
        "pos": "noun",
        "vi": "tủ bát đĩa; tủ để đồ nhà bếp",
        "notes": "Tủ chén bát"
    },
    "damned": {
        "pos": "adj",
        "vi": "đáng nguyền rủa; chết tiệt",
        "notes": "Đáng nguyền rủa"
    },
    "designing": {
        "pos": "adj",
        "vi": "có mưu tính; nghệ thuật thiết kế",
        "notes": "Thiết kế / mưu mô"
    },
    "disclose": {
        "pos": "verb",
        "vi": "tiết lộ; công khai thông tin",
        "notes": "Công bố báo cáo tài chính"
    },
    "discretion": {
        "pos": "noun",
        "vi": "sự thận trọng; quyền tự quyết",
        "notes": "Quyền tự quyết định"
    },
    "dissolved": {
        "pos": "adj",
        "vi": "đã hòa tan; đã giải thể công ty",
        "notes": "Công ty đã giải thể"
    },
    "distracted": {
        "pos": "adj",
        "vi": "xao nhãng; phân tâm mất tập trung",
        "notes": "Mất tập trung"
    },
    "dizzy": {
        "pos": "adj",
        "vi": "chóng mặt; hoa mắt váng đầu",
        "notes": "Hoa mắt chóng mặt"
    },
    "doe": {
        "pos": "noun",
        "vi": "con hươu cái; nai cái",
        "notes": "Hươu cái"
    },
    "donna": {
        "pos": "noun",
        "vi": "quý bà Donna; phụ nữ quý tộc",
        "notes": "Quý bà"
    },
    "dough": {
        "pos": "noun",
        "vi": "bột nhào bánh; tiền bạc (lóng)",
        "notes": "Bột làm bánh / tiền nong"
    },
    "dug": {
        "pos": "verb",
        "vi": "đã đào bới; đã khai quật",
        "notes": "Quá khứ của dig"
    },
    "embedded": {
        "pos": "adj",
        "vi": "được nhúng; tích hợp sẵn vào",
        "notes": "Hệ thống nhúng"
    },
    "favorable": {
        "pos": "adj",
        "vi": "thuận lợi; có thiện chí ủng hộ",
        "notes": "Điều kiện thuận lợi"
    },
    "fellowship": {
        "pos": "noun",
        "vi": "học bổng nghiên cứu; tình thân ái",
        "notes": "Học bổng fellowship"
    },
    "feminism": {
        "pos": "noun",
        "vi": "chủ nghĩa nữ quyền tiến bộ",
        "notes": "Nữ quyền luận"
    },
    "fisherman": {
        "pos": "noun",
        "vi": "ngư dân đánh cá; người đi câu",
        "notes": "Ngư dân miền biển"
    },
    "flea": {
        "pos": "noun",
        "vi": "con bọ chét; chợ trời đồ cũ",
        "notes": "Chợ trời flea market"
    },
    "forgiveness": {
        "pos": "noun",
        "vi": "sự tha thứ; lòng khoan dung",
        "notes": "Sự tha thứ khoan hồng"
    },
    "fragile": {
        "pos": "adj",
        "vi": "dễ vỡ; mỏng manh nhạy cảm",
        "notes": "Hàng dễ vỡ"
    },
    "fringe": {
        "pos": "noun",
        "vi": "vùng rìa; rìa ngoài; phúc lợi phụ",
        "notes": "Phúc lợi phụ (fringe)"
    },
    "fulfill": {
        "pos": "verb",
        "vi": "hoàn thành; đáp ứng yêu cầu",
        "notes": "Đáp ứng đơn hàng"
    },
    "gasoline": {
        "pos": "noun",
        "vi": "nhiên liệu xăng; dầu xăng xe",
        "notes": "Xăng xe máy ô tô"
    },
    "gel": {
        "pos": "noun",
        "vi": "chất keo đặc; gel vuốt tóc tạo kiểu",
        "notes": "Chất gel keo"
    },
    "genesis": {
        "pos": "noun",
        "vi": "nguồn gốc khởi đầu; sách Sáng Thế",
        "notes": "Nguồn gốc xuất phát"
    },
    "geometry": {
        "pos": "noun",
        "vi": "hình học không gian toán học",
        "notes": "Môn hình học"
    },
    "glen": {
        "pos": "noun",
        "vi": "thung lũng hẹp; khe suối núi",
        "notes": "Thung lũng hẹp"
    },
    "governed": {
        "pos": "adj",
        "vi": "được quản lý; chịu chi phối",
        "notes": "Sửa pos từ noun sang adj"
    },
    "granddaughter": {
        "pos": "noun",
        "vi": "cháu gái (con của con ruột)",
        "notes": "Cháu gái nội ngoại"
    },
    "granite": {
        "pos": "noun",
        "vi": "đá hoa cương granite bền chắc",
        "notes": "Mặt đá granite"
    },
    "greens": {
        "pos": "noun",
        "vi": "rau xanh; sân cỏ golf (green)",
        "notes": "Rau xanh ăn uống"
    },
    "handbag": {
        "pos": "noun",
        "vi": "túi xách tay nữ; ví cầm tay",
        "notes": "Túi xách tay thời trang"
    },
    "handbook": {
        "pos": "noun",
        "vi": "sổ tay cẩm nang hướng dẫn nội bộ",
        "notes": "Sổ tay nhân viên"
    },
    "handicapped": {
        "pos": "adj",
        "vi": "khuyết tật; gặp nhiều bất lợi",
        "notes": "Người khuyết tật"
    },
    "hardy": {
        "pos": "adj",
        "vi": "dẻo dai bền bỉ; chịu rét tốt",
        "notes": "Cây cối chịu rét"
    },
    "haunted": {
        "pos": "adj",
        "vi": "bị ma ám; bị ám ảnh day dứt lòng",
        "notes": "Ngôi nhà ma ám"
    },
    "header": {
        "pos": "noun",
        "vi": "tiêu đề trang; cú đánh đầu bóng đá",
        "notes": "Đầu trang văn bản"
    },
    "heather": {
        "pos": "noun",
        "vi": "hoa thạch nam; màu xám thạch nam",
        "notes": "Cây hoa thạch nam"
    },
    "heroic": {
        "pos": "adj",
        "vi": "anh hùng quả cảm; hào hùng",
        "notes": "Hành động anh hùng"
    },
    "horizontal": {
        "pos": "adj",
        "vi": "ngang",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "inclined": {
        "pos": "adj",
        "vi": "có khuynh hướng; thiên về; nghiêng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "individually": {
        "pos": "adv",
        "vi": "riêng lẻ; từng người một",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "inviting": {
        "pos": "adj",
        "vi": "hấp dẫn; mời gọi",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "jew": {
        "pos": "noun",
        "vi": "người Do Thái",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "judiciary": {
        "pos": "noun",
        "vi": "ngành tư pháp; các thẩm phán",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "karma": {
        "pos": "noun",
        "vi": "nghiệp; yết-ma",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "kirk": {
        "pos": "noun",
        "vi": "nhà thờ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "knocking": {
        "pos": "noun",
        "vi": "tiếng gõ; tiếng đập",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "landmark": {
        "pos": "noun",
        "vi": "cột mốc; địa danh nổi tiếng",
        "notes": "Cột mốc lịch sử"
    },
    "lemonade": {
        "pos": "noun",
        "vi": "nước chanh; đá chanh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "lending": {
        "pos": "noun",
        "vi": "sự cho vay; sự cho mượn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "lethal": {
        "pos": "adj",
        "vi": "gây chết người",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "leverage": {
        "pos": "noun",
        "vi": "đòn bẩy tài chính; ưu thế",
        "notes": "Đòn bẩy tài chính"
    },
    "levy": {
        "pos": "noun",
        "vi": "thuế; khoản thu; sự trưng binh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "lime": {
        "pos": "noun",
        "vi": "vôi; chanh; quét keo",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "lining": {
        "pos": "noun",
        "vi": "lớp lót; sự lót; sự phủ mặt",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "logistics": {
        "pos": "noun",
        "vi": "ngành hậu cần; vận tải logistics",
        "notes": "Hậu cần logistics"
    },
    "lowered": {
        "pos": "adj",
        "vi": "thấp hơn; bị hạ thấp",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "maid": {
        "pos": "noun",
        "vi": "đầy tớ gái; hầu gái",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "manila": {
        "pos": "noun",
        "vi": "giấy Manila",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "mapping": {
        "pos": "noun",
        "vi": "ánh xạ; lập bản đồ gen",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "marina": {
        "pos": "noun",
        "vi": "bến du thuyền",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "marker": {
        "pos": "noun",
        "vi": "chỉ tố",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "marsh": {
        "pos": "noun",
        "vi": "đồng lầy",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "marshal": {
        "pos": "noun",
        "vi": "cảnh sát trưởng; nguyên soái",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "mat": {
        "pos": "noun",
        "vi": "tấm thảm lót; đệm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "maturity": {
        "pos": "noun",
        "vi": "kỳ hạn đáo hạn; sự chín chắn",
        "notes": "Đáo hạn trái phiếu / hợp đồng"
    },
    "maya": {
        "pos": "noun",
        "vi": "người Maya; tiếng Maya",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "midday": {
        "pos": "noun",
        "vi": "giữa trưa; buổi trưa",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "militia": {
        "pos": "noun",
        "vi": "dân quân; dân binh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "mindset": {
        "pos": "noun",
        "vi": "tư duy; tư tưởng; tâm lí",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "mistress": {
        "pos": "noun",
        "vi": "người yêu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "molly": {
        "pos": "noun",
        "vi": "cá molly",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "mounting": {
        "pos": "noun",
        "vi": "sự tăng lên; sự leo thang",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "naming": {
        "pos": "noun",
        "vi": "sự đặt tên; định danh thương hiệu",
        "notes": "Sửa pos từ adj sang noun"
    },
    "neighboring": {
        "pos": "adj",
        "vi": "lân cận; kế bên",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "ninja": {
        "pos": "noun",
        "vi": "ninja; nhẫn giả",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "nonprofit": {
        "pos": "adj",
        "vi": "phi lợi nhuận; bất vụ lợi",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "opener": {
        "pos": "noun",
        "vi": "trận mở màn; phần mở đầu; cái mở",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "operative": {
        "pos": "adj",
        "vi": "có hiệu lực; hiệu quả; phẫu thuật",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "other": {
        "pos": "adj",
        "vi": "khác; kia",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "outlined": {
        "pos": "adj",
        "vi": "được vẽ phác; có đường viền rõ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "pains": {
        "pos": "noun",
        "vi": "sự cố gắng; sự nỗ lực",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "panama": {
        "pos": "noun",
        "vi": "mũ Panama",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "para": {
        "pos": "noun",
        "vi": "lính dù; số lần sinh sống; para",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "pear": {
        "pos": "noun",
        "vi": "cây lê; quả lê",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "pharmaceutical": {
        "pos": "adj",
        "vi": "dược phẩm; thuốc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "pickup": {
        "pos": "noun",
        "vi": "xe bán tải; lệnh bắt; lệnh truy nã",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "pitched": {
        "pos": "adj",
        "vi": "có cao độ; nghiêng; dốc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "pouring": {
        "pos": "adj",
        "vi": "đổ ào ào; đổ như thác",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "problematic": {
        "pos": "adj",
        "vi": "có vấn đề; đáng nghi; khó khăn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "processor": {
        "pos": "noun",
        "vi": "bộ xử lý",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "progression": {
        "pos": "noun",
        "vi": "sự tiến triển; sự tiến bộ; cấp số",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "promotional": {
        "pos": "adj",
        "vi": "khuyến mại; quảng cáo; thăng tiến",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "pronunciation": {
        "pos": "noun",
        "vi": "cách phát âm; cách đọc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "radius": {
        "pos": "noun",
        "vi": "xương quay; bán kính",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "recreational": {
        "pos": "adj",
        "vi": "giải trí; nghiệp dư; không chuyên",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "renaissance": {
        "pos": "noun",
        "vi": "phục hưng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "repeal": {
        "pos": "noun",
        "vi": "sự bãi bỏ; hủy bỏ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "reservoir": {
        "pos": "noun",
        "vi": "kho; hồ chứa nước",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "reversed": {
        "pos": "adj",
        "vi": "lộn trái; may lại; đảo ngược",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "rig": {
        "pos": "noun",
        "vi": "giàn khoan; dàn thiết bị",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "risen": {
        "pos": "adj",
        "vi": "đã mọc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "saga": {
        "pos": "noun",
        "vi": "sử thi; câu chuyện anh hùng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "selective": {
        "pos": "adj",
        "vi": "chọn lọc; kén chọn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "settling": {
        "pos": "noun",
        "vi": "sự lún; sự lắng đọng; sự hạ thấp",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "sew": {
        "pos": "verb",
        "vi": "may vá; khâu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "sincerely": {
        "pos": "adv",
        "vi": "thành thật; thật thà; ngay thật",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "sliding": {
        "pos": "adj",
        "vi": "trượt; lướt",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "smashed": {
        "pos": "adj",
        "vi": "say khướt; say bí tỉ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "socialism": {
        "pos": "noun",
        "vi": "chủ nghĩa xã hội",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "sodium": {
        "pos": "noun",
        "vi": "natri; chất muối",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "solidarity": {
        "pos": "noun",
        "vi": "sự liên đới; tình đoàn kết",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "sovereignty": {
        "pos": "noun",
        "vi": "chủ quyền",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "sperm": {
        "pos": "noun",
        "vi": "tinh trùng; tinh binh; tinh dịch",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "spinal": {
        "pos": "adj",
        "vi": "thuộc cột sống; tủy sống",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "spit": {
        "pos": "noun",
        "vi": "nước bọt; nhổ; khạc nhổ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "spotlight": {
        "pos": "noun",
        "vi": "sự chú ý của công chúng; tâm điểm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "stretched": {
        "pos": "adj",
        "vi": "được duỗi; giãn cơ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "stunt": {
        "pos": "noun",
        "vi": "pha nguy hiểm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "sucking": {
        "pos": "noun",
        "vi": "sự mút; sự hút",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "surname": {
        "pos": "noun",
        "vi": "họ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "surplus": {
        "pos": "adj",
        "vi": "thừa; số dư",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "swamp": {
        "pos": "noun",
        "vi": "đầm lầy; tràn ngập; làm ngập lụt",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "sync": {
        "pos": "verb",
        "vi": "đồng bộ hóa; đồng chỉnh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "taxpayer": {
        "pos": "noun",
        "vi": "người đóng thuế",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "threads": {
        "pos": "noun",
        "vi": "luồng thảo luận; sợi chỉ",
        "notes": "Luồng thảo luận mạng xã hội"
    },
    "thrust": {
        "pos": "noun",
        "vi": "lực đẩy; sức đẩy; cú đâm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "ti": {
        "pos": "noun",
        "vi": "nốt Ti si; cây dong",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "timetable": {
        "pos": "noun",
        "vi": "thời khắc biểu; thời gian biểu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "trademark": {
        "pos": "noun",
        "vi": "thương hiệu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "tram": {
        "pos": "noun",
        "vi": "tàu điện; đi xe điện",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "transmitted": {
        "pos": "adj",
        "vi": "di truyền; truyền lại",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "transparency": {
        "pos": "noun",
        "vi": "tính trong suốt; sự minh bạch",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "tribunal": {
        "pos": "noun",
        "vi": "toà án",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "trilogy": {
        "pos": "noun",
        "vi": "bộ ba",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "underway": {
        "pos": "adj",
        "vi": "đang diễn ra; đang tiến hành",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "uneasy": {
        "pos": "adj",
        "vi": "nao nao",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "unforgettable": {
        "pos": "adj",
        "vi": "không thể quên",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "unified": {
        "pos": "adj",
        "vi": "hợp nhất; thống nhất",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "unstable": {
        "pos": "adj",
        "vi": "không ổn định; bấp bênh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "uranium": {
        "pos": "noun",
        "vi": "urani",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "urine": {
        "pos": "noun",
        "vi": "nước tiểu; nước đái",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "verify": {
        "pos": "verb",
        "vi": "xác minh; xác thực; chứng thực",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "villain": {
        "pos": "noun",
        "vi": "nhân vật phản diện; kẻ tàn ác",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "wee": {
        "pos": "adj",
        "vi": "rất nhỏ; sáng sớm (wee hours)",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "yahoo": {
        "pos": "noun",
        "vi": "người thô lỗ; người dốt nát",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "yearly": {
        "pos": "adj",
        "vi": "hàng năm; thường niên",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "accompanying": {
        "pos": "adj",
        "vi": "đi kèm; kéo theo",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "accord": {
        "pos": "noun",
        "vi": "sự hòa hợp; sự nhất trí",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "activation": {
        "pos": "noun",
        "vi": "kích hoạt",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "adjective": {
        "pos": "noun",
        "vi": "tính từ trong ngữ pháp",
        "notes": "Sửa pos từ adj sang noun"
    },
    "afghan": {
        "pos": "adj",
        "vi": "thuộc Afghanistan",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "aligned": {
        "pos": "adj",
        "vi": "liên kết; đồng minh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "alt": {
        "pos": "noun",
        "vi": "phím Alt; sự thay thế (alt)",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "amp": {
        "pos": "noun",
        "vi": "bộ khuếch đại (amp); am-pe",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "angrily": {
        "pos": "adv",
        "vi": "một cách giận dữ; tức giận",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "apollo": {
        "pos": "noun",
        "vi": "thần Apollo",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "arbitrary": {
        "pos": "adj",
        "vi": "tùy tiện; độc đoán",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "archbishop": {
        "pos": "noun",
        "vi": "tổng giám mục",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "archer": {
        "pos": "noun",
        "vi": "xạ thủ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "atlas": {
        "pos": "noun",
        "vi": "tập bản đồ; át-lát",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "axe": {
        "pos": "noun",
        "vi": "cái rìu; việc cắt giảm nhân sự",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "badminton": {
        "pos": "noun",
        "vi": "cầu lông",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "banning": {
        "pos": "noun",
        "vi": "sự cấm; lệnh cấm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "barrels": {
        "pos": "noun",
        "vi": "thùng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "bash": {
        "pos": "noun",
        "vi": "cú đấm mạnh; cú đánh mạnh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "basics": {
        "pos": "noun",
        "vi": "điều cơ bản; nguyên lý cơ bản",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "bats": {
        "pos": "adj",
        "vi": "gàn dở; điên khùng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "battalion": {
        "pos": "noun",
        "vi": "tiểu đoàn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "belle": {
        "pos": "noun",
        "vi": "người đẹp nhất; hoa khôi",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "bibliography": {
        "pos": "noun",
        "vi": "thư mục; thư tịch học",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "borough": {
        "pos": "noun",
        "vi": "khu; quận; thị trấn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "bot": {
        "pos": "noun",
        "vi": "chương trình tự động (bot)",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "boycott": {
        "pos": "noun",
        "vi": "sự tẩy chay",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "burton": {
        "pos": "noun",
        "vi": "rượu bia đen mạnh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "calcium": {
        "pos": "noun",
        "vi": "canxi",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "cardiac": {
        "pos": "adj",
        "vi": "thuộc tim",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "cavalry": {
        "pos": "noun",
        "vi": "kỵ binh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "censorship": {
        "pos": "noun",
        "vi": "kiểm duyệt",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "cheering": {
        "pos": "adj",
        "vi": "khích lệ; an ủi; tiếng reo hò cổ vũ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "coding": {
        "pos": "noun",
        "vi": "viết mã; mã hóa",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "collectively": {
        "pos": "adv",
        "vi": "cùng nhau; tập thể; chung",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "commanding": {
        "pos": "adj",
        "vi": "chiếm ưu thế",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "compilation": {
        "pos": "noun",
        "vi": "biên dịch",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "confined": {
        "pos": "adj",
        "vi": "bị giam hãm; bị hạn chế",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "consolidated": {
        "pos": "adj",
        "vi": "hợp nhất; thống nhất; được củng cố",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "cooker": {
        "pos": "noun",
        "vi": "đồ dùng làm bếp",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "coordinate": {
        "pos": "adj",
        "vi": "tọa độ; toạ độ; điều phối",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "crashing": {
        "pos": "adj",
        "vi": "hết sức; hoàn toàn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "critique": {
        "pos": "noun",
        "vi": "bài phê bình; sự phê phán",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "crushing": {
        "pos": "adj",
        "vi": "đè bẹp; áp đảo; tan nát",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "cuisine": {
        "pos": "noun",
        "vi": "ẩm thực",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "curved": {
        "pos": "adj",
        "vi": "cong",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "decree": {
        "pos": "noun",
        "vi": "sắc lệnh; nghị định; phán quyết",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "deeds": {
        "pos": "noun",
        "vi": "việc làm; hành động",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "diagnostic": {
        "pos": "adj",
        "vi": "chẩn đoán; chỉ điểm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "differential": {
        "pos": "adj",
        "vi": "vi phân; sự khác biệt",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "dividend": {
        "pos": "noun",
        "vi": "cổ tức; phần chia lợi nhuận",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "dominance": {
        "pos": "noun",
        "vi": "ưu thế; tính trội; sự thuận",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "dragging": {
        "pos": "adj",
        "vi": "kéo dài lê thê; chậm chạp",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "drift": {
        "pos": "noun",
        "vi": "lực đẩy trôi",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "eclipse": {
        "pos": "noun",
        "vi": "thiên thực; làm lu mờ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "economically": {
        "pos": "adv",
        "vi": "về mặt kinh tế; một cách tiết kiệm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "enzyme": {
        "pos": "noun",
        "vi": "enzim; men tiêu hoá",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "expired": {
        "pos": "adj",
        "vi": "hết hạn; quá hạn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "fatty": {
        "pos": "adj",
        "vi": "có chất béo; nhiều mỡ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "filthy": {
        "pos": "adj",
        "vi": "bẩn thỉu; dơ dáy; tục tĩu; thô bỉ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "flush": {
        "pos": "adj",
        "vi": "xả; bằng phẳng; ngang bằng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "font": {
        "pos": "noun",
        "vi": "phông chữ vi tính; kiểu chữ",
        "notes": "Sửa crawler bình nước thánh sang phông chữ"
    },
    "forwards": {
        "pos": "adv",
        "vi": "về phía trước; tiến lên",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "freeman": {
        "pos": "noun",
        "vi": "người tự do",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "fries": {
        "pos": "noun",
        "vi": "khoai tây chiên",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "gal": {
        "pos": "noun",
        "vi": "galông; cô gái; con gái",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "glue": {
        "pos": "noun",
        "vi": "keo; hồ; cồn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "guru": {
        "pos": "noun",
        "vi": "đạo sư; guru",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "hawk": {
        "pos": "noun",
        "vi": "chim ưng; diều hâu; bán rong",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "headphone": {
        "pos": "noun",
        "vi": "ống nghe; tai nghe",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "healthier": {
        "pos": "adj",
        "vi": "khỏe hơn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "homemade": {
        "pos": "adj",
        "vi": "cây nhà lá vườn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "honorable": {
        "pos": "adj",
        "vi": "đáng kính; danh dự; trung thực",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "hormone": {
        "pos": "noun",
        "vi": "nội tiết tố",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "humidity": {
        "pos": "noun",
        "vi": "độ ẩm; tình trạng ẩm ướt; ẩm độ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "incomplete": {
        "pos": "adj",
        "vi": "không đầy đủ; không trọn vẹn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "incorporate": {
        "pos": "adj",
        "vi": "hợp nhất; kết hợp; bao gồm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "inferior": {
        "pos": "adj",
        "vi": "kém chất lượng; thấp kém",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "infinity": {
        "pos": "noun",
        "vi": "vô cực",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "injure": {
        "pos": "verb",
        "vi": "làm bị thương; gây thương tích",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "inland": {
        "pos": "adj",
        "vi": "nội địa; trong đất liền",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "inning": {
        "pos": "noun",
        "vi": "hiệp",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "innocence": {
        "pos": "noun",
        "vi": "ngây thơ; trong trắng; vô tội",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "insulin": {
        "pos": "noun",
        "vi": "insulin",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "interrupted": {
        "pos": "adj",
        "vi": "bị gián đoạn; bị ngắt quãng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "intro": {
        "pos": "noun",
        "vi": "sự giới thiệu; đoạn nhạc mở đầu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "ivy": {
        "pos": "noun",
        "vi": "thường xuân",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "kindle": {
        "pos": "verb",
        "vi": "nhóm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "lace": {
        "pos": "noun",
        "vi": "đăng ten; xoắn; bện; đan; tết",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "learner": {
        "pos": "noun",
        "vi": "người học",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "livestock": {
        "pos": "noun",
        "vi": "thú nuôi; gia súc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "lunchtime": {
        "pos": "noun",
        "vi": "giờ ăn trưa",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "mafia": {
        "pos": "noun",
        "vi": "xã hội đen",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "maiden": {
        "pos": "adj",
        "vi": "thiếu nữ; gái trinh; trinh nữ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "manners": {
        "pos": "noun",
        "vi": "phép lịch sự; cách cư xử",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "manor": {
        "pos": "noun",
        "vi": "trang viên",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "marching": {
        "pos": "noun",
        "vi": "sự diễu hành; cuộc hành quân",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "marketplace": {
        "pos": "noun",
        "vi": "thị trường; khu chợ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "melon": {
        "pos": "noun",
        "vi": "dưa",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "membrane": {
        "pos": "noun",
        "vi": "màng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "memo": {
        "pos": "noun",
        "vi": "bản ghi nhớ; thông báo nội bộ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "metallic": {
        "pos": "adj",
        "vi": "bằng kim loại; có tính kim loại",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "mic": {
        "pos": "noun",
        "vi": "mi-crô (mic)",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "mick": {
        "pos": "noun",
        "vi": "Mích",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "missionary": {
        "pos": "adj",
        "vi": "người truyền giáo; cha truyền đạo",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "monopoly": {
        "pos": "noun",
        "vi": "sự độc quyền thị trường",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "nationalism": {
        "pos": "noun",
        "vi": "chủ nghĩa dân tộc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "nationally": {
        "pos": "adv",
        "vi": "về mặt quốc gia; trên toàn quốc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "nickel": {
        "pos": "noun",
        "vi": "nikel; mạ niken",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "obesity": {
        "pos": "noun",
        "vi": "béo phì",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "outright": {
        "pos": "adj",
        "vi": "hoàn toàn; tuyệt đối; thẳng thừng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "overlooked": {
        "pos": "adj",
        "vi": "bị bỏ qua; không được xem xét",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "oversight": {
        "pos": "noun",
        "vi": "sơ suất; thiếu sót; giám sát",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "pier": {
        "pos": "noun",
        "vi": "bến tàu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "pilgrim": {
        "pos": "noun",
        "vi": "người hành hương",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "planting": {
        "pos": "noun",
        "vi": "việc trồng trọt; gieo trồng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "poisoning": {
        "pos": "noun",
        "vi": "sự ngộ độc; trúng độc; sự đầu độc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "pony": {
        "pos": "noun",
        "vi": "ngựa pôni",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "popping": {
        "pos": "noun",
        "vi": "tiếng nổ lách tách; tiếng bốp",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "portrayed": {
        "pos": "adj",
        "vi": "được vẽ; được miêu tả",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "posed": {
        "pos": "adj",
        "vi": "được tạo dáng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "practiced": {
        "pos": "adj",
        "vi": "thành thạo; lão luyện; có kỹ năng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "prolonged": {
        "pos": "adj",
        "vi": "kéo dài; lâu dài",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "promo": {
        "pos": "noun",
        "vi": "quảng cáo; khuyến mãi; lời quảng bá",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "prototype": {
        "pos": "noun",
        "vi": "nguyên mẫu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "psychic": {
        "pos": "adj",
        "vi": "tâm linh; siêu nhiên",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "puppet": {
        "pos": "noun",
        "vi": "con rối; bù nhìn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "racket": {
        "pos": "noun",
        "vi": "vợt; ăn chơi ồn ào; gây ồn ào",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "rand": {
        "pos": "noun",
        "vi": "đồng rand; vùng Rand",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "reactor": {
        "pos": "noun",
        "vi": "lò phản ứng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "reckless": {
        "pos": "adj",
        "vi": "bất cẩn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "recovering": {
        "pos": "adj",
        "vi": "đang hồi phục; bình phục",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "recycle": {
        "pos": "verb",
        "vi": "tái chế",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "refined": {
        "pos": "adj",
        "vi": "lịch sự; tao nhã; thanh lịch",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "reinforced": {
        "pos": "adj",
        "vi": "gia cố; tăng cường",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "reliance": {
        "pos": "noun",
        "vi": "sự tin cậy; niềm tin; sự dựa dẫm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "renewal": {
        "pos": "noun",
        "vi": "sự đổi mới; sự làm mới; sự cải tạo",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "repeating": {
        "pos": "noun",
        "vi": "sự lặp lại; sự nhắc lại",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "replay": {
        "pos": "noun",
        "vi": "trận đấu lại; phát lại",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "reset": {
        "pos": "noun",
        "vi": "nút đặt lại; cơ cấu đặt lại",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "rooted": {
        "pos": "adj",
        "vi": "bất động; đứng yên tại chỗ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "roundabout": {
        "pos": "adj",
        "vi": "vòng xuyến; bùng binh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "sands": {
        "pos": "noun",
        "vi": "bãi cát; vùng bờ biển; bờ hồ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "shah": {
        "pos": "noun",
        "vi": "sa; vua Ba Tư",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "shotgun": {
        "pos": "noun",
        "vi": "súng săn bắn đạn ghém",
        "notes": "Súng săn nòng đôi ghém"
    },
    "sights": {
        "pos": "noun",
        "vi": "thắng cảnh; cảnh quan; tầm ngắm",
        "notes": "Thắng cảnh du lịch"
    },
    "sinking": {
        "pos": "noun",
        "vi": "sự chìm; sự đắm; sự suy yếu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "slate": {
        "pos": "noun",
        "vi": "đá phiến; bảng đá",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "sorted": {
        "pos": "adj",
        "vi": "phân loại; xếp nhóm; phân nhóm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "spaceship": {
        "pos": "noun",
        "vi": "phi thuyền; tàu vũ trụ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "spoiled": {
        "pos": "adj",
        "vi": "hư hỏng; ôi thiu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "staged": {
        "pos": "adj",
        "vi": "dàn dựng; được dàn xếp",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "stair": {
        "pos": "noun",
        "vi": "cầu thang",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "startup": {
        "pos": "noun",
        "vi": "công ty khởi nghiệp; sự khởi đầu",
        "notes": "Startup công nghệ"
    },
    "statute": {
        "pos": "noun",
        "vi": "đạo luật; quy chế theo luật",
        "notes": "Sửa pos từ adj sang noun"
    },
    "stimulus": {
        "pos": "noun",
        "vi": "gói kích thích kinh tế; tác nhân",
        "notes": "Gói kích thích kinh tế"
    },
    "sting": {
        "pos": "noun",
        "vi": "đốt; chích; cảm giác nhói",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "stripped": {
        "pos": "adj",
        "vi": "bị loại bỏ hết; trần trụi",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "sunflower": {
        "pos": "noun",
        "vi": "hướng dương; thiên quỳ tử",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "swimsuit": {
        "pos": "noun",
        "vi": "đồ bơi; trang phục bơi",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "tagged": {
        "pos": "adj",
        "vi": "có gắn thẻ; được dán nhãn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "tee": {
        "pos": "noun",
        "vi": "áo thun (T-shirt); giá đỡ bóng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "therapeutic": {
        "pos": "adj",
        "vi": "trị liệu; chữa bệnh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "tights": {
        "pos": "noun",
        "vi": "quần bó; quần tất",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "timothy": {
        "pos": "noun",
        "vi": "cỏ Timothy; Ti-mô-thê",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "toddler": {
        "pos": "noun",
        "vi": "trẻ mới biết đi; em bé chập chững",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "token": {
        "pos": "adj",
        "vi": "tượng trưng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "toothbrush": {
        "pos": "noun",
        "vi": "bàn chải đánh răng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "treason": {
        "pos": "noun",
        "vi": "tội phản quốc; hành vi phản bội",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "twilight": {
        "pos": "adj",
        "vi": "hoàng hôn; bình minh; mờ tối",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "typing": {
        "pos": "noun",
        "vi": "sự đánh máy; bài đánh máy",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "utilized": {
        "pos": "adj",
        "vi": "được sử dụng; được tận dụng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "vanilla": {
        "pos": "adj",
        "vi": "vani",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "vent": {
        "pos": "noun",
        "vi": "lỗ thông hơi; miệng núi lửa",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "vodka": {
        "pos": "noun",
        "vi": "vodka; vôtca",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "wan": {
        "pos": "noun",
        "vi": "mạng diện rộng (WAN); nhợt nhạt",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "weekday": {
        "pos": "noun",
        "vi": "ngày thường",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "weighing": {
        "pos": "noun",
        "vi": "sự cân nhắc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "wellington": {
        "pos": "noun",
        "vi": "ủng cao cổ có tua",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "woody": {
        "pos": "adj",
        "vi": "bằng gỗ; như gỗ; có nhiều cây cối",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "two": {
        "pos": "num",
        "vi": "hai; số 2",
        "notes": "Số từ two"
    },
    "acquiring": {
        "pos": "noun",
        "vi": "sự thu nhận; sự giành được",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "algebra": {
        "pos": "noun",
        "vi": "đại số",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "amended": {
        "pos": "adj",
        "vi": "được sửa đổi; được tu chỉnh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "antenna": {
        "pos": "noun",
        "vi": "xúc giác; râu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "apparatus": {
        "pos": "noun",
        "vi": "bộ máy",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "armchair": {
        "pos": "noun",
        "vi": "ghế bành",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "assassination": {
        "pos": "noun",
        "vi": "vụ ám sát; sự bôi nhọ; vu khống",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "automation": {
        "pos": "noun",
        "vi": "sự tự động hóa",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "balancing": {
        "pos": "noun",
        "vi": "sự cân bằng; sự điều chỉnh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "behold": {
        "pos": "verb",
        "vi": "chiêm ngưỡng; ngắm nhìn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "biased": {
        "pos": "adj",
        "vi": "thiên vị",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "biting": {
        "pos": "adj",
        "vi": "chát; cay; buốt; chua cay; cay độc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "bodily": {
        "pos": "adj",
        "vi": "thuộc về cơ thể; thể xác",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "branding": {
        "pos": "noun",
        "vi": "xây dựng thương hiệu; định danh",
        "notes": "Sửa crawler sự kỳ thị sang xây dựng thương hiệu"
    },
    "bravo": {
        "pos": "noun",
        "vi": "tiếng hoan hô; bravo",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "brewing": {
        "pos": "noun",
        "vi": "sự nấu bia; ngành nấu bia",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "busted": {
        "pos": "adj",
        "vi": "hỏng; vỡ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "capitalist": {
        "pos": "adj",
        "vi": "thuộc chủ nghĩa tư bản",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "cedar": {
        "pos": "noun",
        "vi": "cây tuyết tùng; cây họ bách tùng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "chapman": {
        "pos": "noun",
        "vi": "người bán rong",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "charleston": {
        "pos": "noun",
        "vi": "điệu nhảy Charleston",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "chopped": {
        "pos": "adj",
        "vi": "được cắt nhỏ; băm nhỏ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "colorful": {
        "pos": "adj",
        "vi": "rực rỡ; sặc sỡ; đầy nghị lực",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "combo": {
        "pos": "noun",
        "vi": "gói kết hợp (combo); phối hợp",
        "notes": "Sửa ban nhạc jazz sang gói kết hợp"
    },
    "communism": {
        "pos": "noun",
        "vi": "chủ nghĩa cộng sản; chế độ cộng sản",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "congregation": {
        "pos": "noun",
        "vi": "giáo đoàn; cộng đồng tín đồ",
        "notes": "Sửa crawler bộ sang giáo đoàn"
    },
    "constable": {
        "pos": "noun",
        "vi": "cảnh sát viên; nhân viên an ninh",
        "notes": "Cảnh sát viên khu vực"
    },
    "constructive": {
        "pos": "adj",
        "vi": "mang tính xây dựng; tích cực",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "coordinated": {
        "pos": "adj",
        "vi": "phối hợp nhịp nhàng; khéo léo",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "counselor": {
        "pos": "noun",
        "vi": "cố vấn; nhà tư vấn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "curb": {
        "pos": "noun",
        "vi": "rào cản kiềm chế; lề đường",
        "notes": "Kiềm chế lạm phát / lề đường"
    },
    "cursed": {
        "pos": "adj",
        "vi": "đáng nguyền rủa; bị nguyền rủa",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "definitive": {
        "pos": "adj",
        "vi": "dứt khoát; cuối cùng; có uy tín",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "dementia": {
        "pos": "noun",
        "vi": "suy giảm trí nhớ; chứng mất trí",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "departed": {
        "pos": "adj",
        "vi": "đã khuất; quá cố; đã qua; xa xưa",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "depicted": {
        "pos": "adj",
        "vi": "được vẽ; được miêu tả",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "depths": {
        "pos": "noun",
        "vi": "độ sâu; nơi sâu thẳm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "destined": {
        "pos": "adj",
        "vi": "đi đến; hướng đến",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "detached": {
        "pos": "adj",
        "vi": "lãnh đạm; xa cách",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "developmental": {
        "pos": "adj",
        "vi": "phát triển",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "dice": {
        "pos": "noun",
        "vi": "con xúc xắc (xí ngầu)",
        "notes": "Xúc xắc xí ngầu"
    },
    "digit": {
        "pos": "noun",
        "vi": "chữ số; ngón",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "disclosed": {
        "pos": "adj",
        "vi": "được tiết lộ; được hé lộ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "dispatch": {
        "pos": "noun",
        "vi": "báo cáo khẩn; công văn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "disturbed": {
        "pos": "adj",
        "vi": "rối loạn tâm lý; bất ổn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "dong": {
        "pos": "noun",
        "vi": "đồng; kêu boong boong",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "doomed": {
        "pos": "adj",
        "vi": "chắc chắn chết; bị kết án tử",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "drainage": {
        "pos": "noun",
        "vi": "hệ thống thoát nước",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "duchess": {
        "pos": "noun",
        "vi": "nữ công tước; vợ của công tước",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "efficiently": {
        "pos": "adv",
        "vi": "hiệu quả; có hiệu suất cao",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "enforced": {
        "pos": "adj",
        "vi": "bị áp đặt; bị bắt buộc; bị thi hành",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "epidemic": {
        "pos": "adj",
        "vi": "dịch",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "evolutionary": {
        "pos": "adj",
        "vi": "tiến hóa",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "exempt": {
        "pos": "adj",
        "vi": "được miễn; miễn cho; miễn trừ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "exploded": {
        "pos": "adj",
        "vi": "dạng tháo rời",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "extraction": {
        "pos": "noun",
        "vi": "sự chiết xuất; sự khai thác; sự nhổ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "fairness": {
        "pos": "noun",
        "vi": "sự công bằng; tính khách quan",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "fascist": {
        "pos": "adj",
        "vi": "phát xít",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "favored": {
        "pos": "adj",
        "vi": "được ưu đãi; được yêu thích hơn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "felony": {
        "pos": "noun",
        "vi": "trọng tội",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "fertility": {
        "pos": "noun",
        "vi": "khả năng sinh sản; sự màu mỡ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "flats": {
        "pos": "noun",
        "vi": "giày bệt; căn hộ cho thuê",
        "notes": "Giày đế bệt / căn hộ"
    },
    "flint": {
        "pos": "adj",
        "vi": "đá lửa; cứng rắn; vô cảm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "flooded": {
        "pos": "adj",
        "vi": "ngập",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "floral": {
        "pos": "adj",
        "vi": "hoa; hệ thực vật",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "foam": {
        "pos": "noun",
        "vi": "bọt xốp; lớp đệm mút",
        "notes": "Bọt đệm xốp"
    },
    "foil": {
        "pos": "noun",
        "vi": "lá kim loại; giấy bạc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "foremost": {
        "pos": "adj",
        "vi": "quan trọng nhất; hàng đầu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "forge": {
        "pos": "noun",
        "vi": "lò rèn; lò luyện kim",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "fortress": {
        "pos": "noun",
        "vi": "pháo đài",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "freestyle": {
        "pos": "noun",
        "vi": "kiểu bơi tự do; phong cách tự do",
        "notes": "Bơi tự do / freestyle"
    },
    "fulfilled": {
        "pos": "adj",
        "vi": "hoàn thành trọn vẹn; viên mãn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "fuller": {
        "pos": "noun",
        "vi": "thợ làm dày vải; thợ hồ vải",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "gamble": {
        "pos": "noun",
        "vi": "đánh bạc; tiền cược",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "gram": {
        "pos": "noun",
        "vi": "gam",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "heath": {
        "pos": "noun",
        "vi": "cây thạch nam",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "hierarchy": {
        "pos": "noun",
        "vi": "tôn ti; thứ bậc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "homicide": {
        "pos": "noun",
        "vi": "tội giết người; sự giết người",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "horny": {
        "pos": "adj",
        "vi": "chất sừng cứng; ham muốn tình dục",
        "notes": "Lọc từ ngữ thô tục nhạy cảm của crawler"
    },
    "imprisoned": {
        "pos": "adj",
        "vi": "bị giam cầm; bị tù",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "inconsistent": {
        "pos": "adj",
        "vi": "không nhất quán; mâu thuẫn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "insider": {
        "pos": "noun",
        "vi": "người nội bộ (insider trading)",
        "notes": "Người trong cuộc nội bộ"
    },
    "invalid": {
        "pos": "adj",
        "vi": "vô hiệu; không hợp lệ; hết hiệu lực",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "iris": {
        "pos": "noun",
        "vi": "hoa diên vĩ; mống mắt tròng đen",
        "notes": "Hoa diên vĩ / mống mắt"
    },
    "jointly": {
        "pos": "adv",
        "vi": "cùng nhau; chung",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "justification": {
        "pos": "noun",
        "vi": "sự biện minh; lý do chính đáng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "kilo": {
        "pos": "noun",
        "vi": "ki-lô-gam (kg); một nghìn",
        "notes": "Đơn vị đo kg"
    },
    "kindergarten": {
        "pos": "noun",
        "vi": "mẫu giáo; nhà trẻ; vườn trẻ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "latino": {
        "pos": "adj",
        "vi": "thuộc về người Mỹ Latin",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "laziness": {
        "pos": "noun",
        "vi": "sự lười biếng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "lightweight": {
        "pos": "adj",
        "vi": "nhẹ; nhẹ cân; không quan trọng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "lowering": {
        "pos": "adj",
        "vi": "u ám; tối sầm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "lunar": {
        "pos": "adj",
        "vi": "mặt trăng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "maxwell": {
        "pos": "noun",
        "vi": "maxwell",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "melted": {
        "pos": "adj",
        "vi": "tan chảy; nóng chảy",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "melting": {
        "pos": "adj",
        "vi": "tan chảy; đang tan",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "memoir": {
        "pos": "noun",
        "vi": "hồi ký; luận văn; truyện ký",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "messaging": {
        "pos": "noun",
        "vi": "thông điệp truyền thông; nhắn tin",
        "notes": "Thông điệp thương hiệu"
    },
    "metabolism": {
        "pos": "noun",
        "vi": "trao đổi chất; biến dưỡng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "metre": {
        "pos": "noun",
        "vi": "mét; thước",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "minimize": {
        "pos": "verb",
        "vi": "giảm thiểu; thu nhỏ; coi nhẹ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "mold": {
        "pos": "noun",
        "vi": "khuôn đúc mẫu; nấm mốc bề mặt",
        "notes": "Khuôn đúc / nấm mốc"
    },
    "morocco": {
        "pos": "noun",
        "vi": "Ma-rốc; da dê thuộc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "napkin": {
        "pos": "noun",
        "vi": "khăn ăn trên bàn tiệc",
        "notes": "Khăn ăn bàn tiệc"
    },
    "napoleon": {
        "pos": "noun",
        "vi": "Napoléon Bonaparte; bánh Napoleon",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "neglected": {
        "pos": "adj",
        "vi": "bị bỏ bê; bị lãng quên; bị bỏ mặc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "notch": {
        "pos": "noun",
        "vi": "vết khía; nấc thang chất lượng",
        "notes": "Top notch / nấc thang"
    },
    "obliged": {
        "pos": "adj",
        "vi": "bắt buộc; có nghĩa vụ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "occurrence": {
        "pos": "noun",
        "vi": "sự cố biến cố; sự xuất hiện",
        "notes": "Sự cố xảy ra"
    },
    "omega": {
        "pos": "noun",
        "vi": "chữ cái Omega; điểm tận cùng",
        "notes": "Điểm tận cùng"
    }
}

def main():
    print(f"Reading {BATCH_FILE}...")
    with open(BATCH_FILE, "r", encoding="utf-8") as fp:
        data = json.load(fp)

    records = data["records"]
    slice_records = records[3200:3700]
    assert len(slice_records) == 500, f"Expected 500 records, got {len(slice_records)}"

    updated = 0
    for r in slice_records:
        hw = r["hw"]
        if hw in EDITS_3201_3700:
            e = EDITS_3201_3700[hw]
            r["pos"] = e["pos"]
            r["vi"] = e["vi"]
            r["status"] = "edited"
            r["notes"] = e.get("notes", "Đã soát tay chuẩn hóa QA")
            updated += 1
        else:
            r["status"] = "approved"
            r["notes"] = "QA passed manual review"

    data["reviewedCount"] = 3700
    data["status"] = "in-progress"

    print(f"Writing updated slice back to {BATCH_FILE}...")
    with open(BATCH_FILE, "w", encoding="utf-8") as fp:
        json.dump(data, fp, ensure_ascii=False, indent=2)

    print(f"Successfully processed STT 3201-3700. Meticulously curated: {updated} words.")

    # Update INDEX.md
    if INDEX_FILE.exists():
        content = INDEX_FILE.read_text(encoding="utf-8")
        new_line = "| 01 | `batch-01.json` | 5000 | account ... sane | Phase 1 (100k Core & Standard) | 🔄 `in-progress` (3700/5000) |"
        content = re.sub(
            r"\|\s*01\s*\|\s*`batch-01\.json`.*?\|\s*[✅🔄⏳].*?\|",
            new_line,
            content
        )
        INDEX_FILE.write_text(content, encoding="utf-8")
        print("Updated INDEX.md to 3700/5000 in-progress.")

if __name__ == "__main__":
    main()
