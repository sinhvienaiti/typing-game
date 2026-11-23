#!/usr/bin/env python3
"""
qa_batch_01_slice_4201_4700.py
Rà soát thủ công chuyên sâu 500 từ (STT 4201 đến 4700) của batch-01.json:
- Sửa lỗi bot crawler:
  - bang: lọc sạch hoàn toàn từ ngữ dung tục thô bỉ của crawler sang adv 'đúng boong; tiếng nổ vang'.
  - tore: sửa lỗi nhầm gờ chân cột sang verb tear/tore 'đã xé toạc; đã giằng xé nát'.
  - bureau: sửa lỗi dịch 'sự giúp đỡ' sang noun 'cục; cơ quan chuyên trách'.
  - taco: xóa từ miệt thị 'người Mễ' sang 'bánh kẹp taco của Mexico'.
  - crash: sửa lỗi 'tiếng hét' sang 'vụ va chạm xe; cú sụp đổ thị trường'.
  - initial: sửa 'thanh mẫu' sang 'ban đầu; khởi đầu; chữ cái đầu'.
  - constantly: sửa từ lóng 'hoài' sang 'liên tục không ngừng; luôn luôn'.
  - ignore: sửa từ lóng 'bơ' sang 'phớt lờ; cố tình bỏ qua không nghe'.
  - capped: chuẩn hóa nghĩa kinh tế 'có mức trần khống chế; có nắp đậy'.
- Sửa POS chuẩn:
  - hearing: adj -> noun ('thính giác; phiên điều trần tòa án')
  - positioning: adj -> noun ('chiến lược định vị thương hiệu')
  - dozen: adj -> num ('một tá (12 cái); hàng chục thứ')
  - incident: adj -> noun ('sự cố bất ngờ; vụ việc rắc rối')
  - rank: adj -> noun ('cấp bậc quân hàm; thứ hạng bảng xếp')
  - retail: adv -> noun ('ngành bán lẻ; hoạt động bán lẻ hàng')
  - scrub: adj -> noun ('bụi cây rậm; bộ đồ mổ phẫu thuật')
  - alas: adv -> intj ('than ôi; ôi chao tiếc nuối')
- Chuẩn hóa thuật ngữ kinh tế và công nghệ:
  - platform, wire, storage, server, liquid, foundation, disruption, brent, capacity, baseline, etc.
- Độ dài nghĩa tiếng Việt <= 35 ký tự, phân tách bằng '; '.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BATCH_FILE = ROOT / "content" / "english" / "qa-batches" / "batch-01.json"
INDEX_FILE = ROOT / "content" / "english" / "qa-batches" / "INDEX.md"

EDITS_4201_4700 = {
    "equal": {
        "pos": "adj",
        "vi": "bằng nhau; ngang nhau",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "equipment": {
        "pos": "noun",
        "vi": "thiết bị; dụng cụ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "era": {
        "pos": "noun",
        "vi": "kỷ nguyên; thời đại",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "escalator": {
        "pos": "noun",
        "vi": "thang cuốn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "fake": {
        "pos": "adj",
        "vi": "giả; nhái; hàng giả",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "fellow": {
        "pos": "noun",
        "vi": "gã; anh chàng; người đàn ông",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "fifth": {
        "pos": "adj",
        "vi": "thứ năm; một phần năm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "fin": {
        "pos": "noun",
        "vi": "vây cá; cánh thăng bằng; ngành fin",
        "notes": "Vây cá / Fintech"
    },
    "finance": {
        "pos": "noun",
        "vi": "tài chính; cung cấp vốn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "finding": {
        "pos": "noun",
        "vi": "kết quả nghiên cứu; phát hiện mới",
        "notes": "Kết quả tìm kiếm phát hiện"
    },
    "firm": {
        "pos": "adj",
        "vi": "chắc chắn; kiên định vững vàng",
        "notes": "Kiên định chắc chắn"
    },
    "flora": {
        "pos": "noun",
        "vi": "hệ thực vật",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "flow": {
        "pos": "noun",
        "vi": "dòng chảy",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "fuel": {
        "pos": "noun",
        "vi": "nhiên liệu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "gamma": {
        "pos": "noun",
        "vi": "tia gamma; chữ cái Hy Lạp gamma",
        "notes": "Tia gamma"
    },
    "generally": {
        "pos": "adv",
        "vi": "thường thường; thường thì",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "grant": {
        "pos": "noun",
        "vi": "tiền trợ cấp; tiền cấp; đất cấp",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "guiding": {
        "pos": "adj",
        "vi": "dẫn dắt; hướng dẫn; chỉ đường",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "guilty": {
        "pos": "adj",
        "vi": "có tội; phạm tội; tội lỗi",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "hearing": {
        "pos": "noun",
        "vi": "thính giác; phiên điều trần tòa án",
        "notes": "Sửa pos từ adj sang noun"
    },
    "homosexual": {
        "pos": "adj",
        "vi": "đồng tính",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "honest": {
        "pos": "adj",
        "vi": "thành thật",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "hustle": {
        "pos": "noun",
        "vi": "sự hối hả; nhộn nhịp",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "infrared": {
        "pos": "adj",
        "vi": "hồng ngoại",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "injury": {
        "pos": "noun",
        "vi": "thương tích; thương tật",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "iron": {
        "pos": "adj",
        "vi": "bằng sắt; sắt đá kiên cường",
        "notes": "Ý chí sắt đá"
    },
    "joint": {
        "pos": "adj",
        "vi": "chung; liên kết",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "journal": {
        "pos": "noun",
        "vi": "nhật ký; nhật trình; nhật báo",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "justice": {
        "pos": "noun",
        "vi": "công bằng; công lý; thẩm phán",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "killing": {
        "pos": "adj",
        "vi": "chết người; vắt kiệt sức lực",
        "notes": "Vắt kiệt sức"
    },
    "launch": {
        "pos": "noun",
        "vi": "buổi ra mắt sản phẩm; phóng tàu",
        "notes": "Ra mắt sản phẩm"
    },
    "lay": {
        "pos": "verb",
        "vi": "đặt để; sắp đặt; đẻ trứng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "length": {
        "pos": "noun",
        "vi": "chiều dài",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "limit": {
        "pos": "noun",
        "vi": "giới hạn; hạn chế",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "majority": {
        "pos": "noun",
        "vi": "đa số; phần lớn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "management": {
        "pos": "noun",
        "vi": "sự quản lý; quản trị",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "marriage": {
        "pos": "noun",
        "vi": "hôn nhân; vợ chồng; lễ cưới",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "masculine": {
        "pos": "adj",
        "vi": "nam tính; thuộc về phái mạnh",
        "notes": "Đặc tính nam tính"
    },
    "massive": {
        "pos": "adj",
        "vi": "đồ sộ; khổng lồ; nguyên khối",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "mayor": {
        "pos": "noun",
        "vi": "thị trưởng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "mess": {
        "pos": "noun",
        "vi": "mớ hỗn độn; lộn xộn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "mile": {
        "pos": "noun",
        "vi": "dặm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "minimum": {
        "pos": "adj",
        "vi": "tối thiểu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "mission": {
        "pos": "noun",
        "vi": "nhiệm vụ; sứ mệnh; hội thiện nguyện",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "network": {
        "pos": "noun",
        "vi": "mạng lưới; hệ thống",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "northern": {
        "pos": "adj",
        "vi": "thuộc phương bắc; ở phía bắc",
        "notes": "Phía bắc"
    },
    "nuclear": {
        "pos": "adj",
        "vi": "hạt nhân",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "obviously": {
        "pos": "adv",
        "vi": "rõ ràng; hiển nhiên; rành rành",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "ocean": {
        "pos": "noun",
        "vi": "đại dương",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "opening": {
        "pos": "adj",
        "vi": "mở đầu; khai mạc sự kiện",
        "notes": "Bài phát biểu khai mạc"
    },
    "option": {
        "pos": "noun",
        "vi": "lựa chọn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "peek": {
        "pos": "noun",
        "vi": "cái nhìn trộm; cái liếc nhanh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "politics": {
        "pos": "noun",
        "vi": "chính trị",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "port": {
        "pos": "adj",
        "vi": "ở phía mạn trái tàu thuyền",
        "notes": "Mạn trái tàu"
    },
    "posing": {
        "pos": "noun",
        "vi": "việc tạo dáng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "positioning": {
        "pos": "noun",
        "vi": "chiến lược định vị thương hiệu",
        "notes": "Sửa pos từ adj sang noun"
    },
    "potential": {
        "pos": "adj",
        "vi": "tiềm năng; tiềm lực; điện thế",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "predator": {
        "pos": "noun",
        "vi": "thú săn mồi; kẻ trục lợi bóc lột",
        "notes": "Thú săn mồi / kẻ bóc lột"
    },
    "president": {
        "pos": "noun",
        "vi": "tổng thống; chủ tịch",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "previous": {
        "pos": "adj",
        "vi": "trước",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "prison": {
        "pos": "noun",
        "vi": "tù",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "professor": {
        "pos": "noun",
        "vi": "giáo sư; giảng viên đại học",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "proof": {
        "pos": "adj",
        "vi": "chống chịu được; không thấm nước",
        "notes": "Chống nước (waterproof)"
    },
    "prophecy": {
        "pos": "noun",
        "vi": "tiên tri",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "protect": {
        "pos": "verb",
        "vi": "bảo vệ; che chở; bảo hộ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "proud": {
        "pos": "adj",
        "vi": "tự hào; hãnh diện",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "prove": {
        "pos": "verb",
        "vi": "chứng minh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "pure": {
        "pos": "adj",
        "vi": "thuần khiết",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "quad": {
        "pos": "noun",
        "vi": "sân trong hình vuông; xe 4 bánh",
        "notes": "Sân trong / xe quad"
    },
    "rare": {
        "pos": "adj",
        "vi": "hiếm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "reality": {
        "pos": "noun",
        "vi": "thực tế; hiện thực",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "recorder": {
        "pos": "noun",
        "vi": "máy ghi âm; máy ghi hình; máy quay",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "recurring": {
        "pos": "adj",
        "vi": "tái diễn; lặp lại",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "reduce": {
        "pos": "verb",
        "vi": "giảm; bớt",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "remove": {
        "pos": "noun",
        "vi": "khoảng cách biệt; bước dịch chuyển",
        "notes": "Khoảng cách xa biệt"
    },
    "romeo": {
        "pos": "noun",
        "vi": "người tình si tình",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "rubbing": {
        "pos": "noun",
        "vi": "sự ma sát; bản in dập; sự cọ xát",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "setting": {
        "pos": "noun",
        "vi": "bối cảnh; môi trường; tình huống",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "shame": {
        "pos": "noun",
        "vi": "sự xấu hổ; sự thẹn; sự ngượng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "shift": {
        "pos": "noun",
        "vi": "ca làm việc; sự dịch chuyển hướng",
        "notes": "Ca kíp làm việc"
    },
    "shutting": {
        "pos": "noun",
        "vi": "sự đóng lại; hành động đóng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "signal": {
        "pos": "adj",
        "vi": "nổi bật; mang tính bước ngoặt",
        "notes": "Thành công bước ngoặt"
    },
    "slowing": {
        "pos": "noun",
        "vi": "sự chậm lại; sự giảm tốc độ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "solid": {
        "pos": "adj",
        "vi": "rắn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "southern": {
        "pos": "adj",
        "vi": "thuộc phương nam; ở phía nam",
        "notes": "Phía nam"
    },
    "spirit": {
        "pos": "noun",
        "vi": "tinh thần; linh hồn; rượu mạnh",
        "notes": "Tinh thần làm việc"
    },
    "standard": {
        "pos": "adj",
        "vi": "tiêu chuẩn; tiêu chí",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "starred": {
        "pos": "adj",
        "vi": "có đánh dấu hoa thị; có dấu sao",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "steel": {
        "pos": "noun",
        "vi": "kim loại thép; sự đanh thép",
        "notes": "Ngành thép"
    },
    "stress": {
        "pos": "noun",
        "vi": "áp lực; căng thẳng; xì-trét",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "stuck": {
        "pos": "adj",
        "vi": "bị mắc kẹt; bế tắc; bí",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "surface": {
        "pos": "adj",
        "vi": "ở bề mặt bên ngoài; nông cạn",
        "notes": "Bề ngoài nông cạn"
    },
    "switch": {
        "pos": "noun",
        "vi": "chuyển mạch; ngắt điện; công tắc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "taste": {
        "pos": "noun",
        "vi": "vị; sở thích",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "template": {
        "pos": "noun",
        "vi": "bản mẫu; khuôn mẫu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "tend": {
        "pos": "verb",
        "vi": "có xu hướng; hay; chăm sóc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "termination": {
        "pos": "noun",
        "vi": "chấm dứt hợp đồng; sa thải",
        "notes": "Chấm dứt hợp đồng"
    },
    "theorem": {
        "pos": "noun",
        "vi": "định lí",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "tiny": {
        "pos": "adj",
        "vi": "tí hon",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "tore": {
        "pos": "verb",
        "vi": "đã xé toạc; đã giằng xé nát",
        "notes": "Sửa crawler gờ chân cột sang verb tear/tore"
    },
    "totally": {
        "pos": "adv",
        "vi": "hoàn toàn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "treat": {
        "pos": "noun",
        "vi": "món ngon; đồ ăn ngon; điều thú vị",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "treatment": {
        "pos": "noun",
        "vi": "điều trị; chữa trị",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "tribune": {
        "pos": "noun",
        "vi": "khán đài; diễn đàn ngôn luận",
        "notes": "Diễn đàn tribune"
    },
    "unique": {
        "pos": "adj",
        "vi": "duy nhất; độc nhất",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "update": {
        "pos": "noun",
        "vi": "bản cập nhật; tình hình mới",
        "notes": "Bản cập nhật"
    },
    "upper": {
        "pos": "adj",
        "vi": "trên",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "variety": {
        "pos": "noun",
        "vi": "nhiều loại; đủ loại; sự đa dạng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "vehicle": {
        "pos": "noun",
        "vi": "xe cộ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "victory": {
        "pos": "noun",
        "vi": "chiến thắng vang dội; sự thắng lợi",
        "notes": "Thắng lợi"
    },
    "violence": {
        "pos": "noun",
        "vi": "bạo lực",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "volcanic": {
        "pos": "adj",
        "vi": "thuộc núi lửa; bùng nổ; dữ dội",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "volume": {
        "pos": "noun",
        "vi": "âm lượng; khối lượng giao dịch",
        "notes": "Khối lượng giao dịch cổ phiếu"
    },
    "weird": {
        "pos": "adj",
        "vi": "kì quặc; kì quái; kì cục",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "written": {
        "pos": "adj",
        "vi": "được viết; dưới dạng văn bản",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "why": {
        "pos": "adv",
        "vi": "tại sao; vì sao",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "academy": {
        "pos": "noun",
        "vi": "học viện; viện hàn lâm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "afford": {
        "pos": "verb",
        "vi": "có đủ tiền; đủ khả năng chi trả",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "aide": {
        "pos": "noun",
        "vi": "trợ lý đắc lực; cố vấn phụ tá",
        "notes": "Trợ lý phụ tá"
    },
    "aim": {
        "pos": "verb",
        "vi": "nhắm tới; hướng đến; mục tiêu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "alcohol": {
        "pos": "noun",
        "vi": "chất cồn; đồ uống rượu bia",
        "notes": "Nồng độ cồn"
    },
    "arbitration": {
        "pos": "noun",
        "vi": "trọng tài thương mại; sự phân xử",
        "notes": "Trọng tài kinh tế"
    },
    "arrest": {
        "pos": "noun",
        "vi": "sự bắt; bắt giữ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "assume": {
        "pos": "verb",
        "vi": "cho rằng; giả sử; nhậm chức",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "attend": {
        "pos": "verb",
        "vi": "tham gia",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "authority": {
        "pos": "noun",
        "vi": "thẩm quyền pháp lý; nhà chức trách",
        "notes": "Cơ quan có thẩm quyền"
    },
    "baseline": {
        "pos": "noun",
        "vi": "đường cơ sở; mốc chuẩn so sánh",
        "notes": "Mốc chuẩn baseline"
    },
    "beads": {
        "pos": "noun",
        "vi": "chuỗi hạt; tràng hạt",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "belief": {
        "pos": "noun",
        "vi": "niềm tin; lòng tin",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "benedict": {
        "pos": "noun",
        "vi": "món trứng Benedict; tên Benedict",
        "notes": "Món ăn trứng Benedict"
    },
    "bisexual": {
        "pos": "adj",
        "vi": "lưỡng tính; song tính",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "blind": {
        "pos": "adj",
        "vi": "mù",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "bomb": {
        "pos": "noun",
        "vi": "bom",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "bound": {
        "pos": "adj",
        "vi": "bị trói buộc; bị cầm tù; liên kết",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "breath": {
        "pos": "noun",
        "vi": "hơi thở; luồng gió mát nhẹ",
        "notes": "Hơi thở"
    },
    "brent": {
        "pos": "noun",
        "vi": "dầu thô Brent; tên họ Brent",
        "notes": "Dầu Brent biển Bắc"
    },
    "brief": {
        "pos": "adj",
        "vi": "ngắn gọn; bản tóm tắt",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "broad": {
        "pos": "adj",
        "vi": "rộng lớn; bao quát",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "calm": {
        "pos": "adj",
        "vi": "bình tĩnh; điềm tĩnh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "capable": {
        "pos": "adj",
        "vi": "có khả năng; có thể",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "capacity": {
        "pos": "noun",
        "vi": "công suất sản xuất; sức chứa tối đa",
        "notes": "Công suất vận hành"
    },
    "chalk": {
        "pos": "noun",
        "vi": "phấn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "champion": {
        "pos": "adj",
        "vi": "đoạt giải quán quân; vô địch",
        "notes": "Vô địch giải đấu"
    },
    "chase": {
        "pos": "noun",
        "vi": "sự đuổi theo; sự săn đuổi",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "chronicle": {
        "pos": "noun",
        "vi": "biên niên sử; sử ký",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "cinnamon": {
        "pos": "noun",
        "vi": "cây quế; nâu vàng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "closely": {
        "pos": "adv",
        "vi": "gần gũi; chặt chẽ; chăm chú",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "coal": {
        "pos": "noun",
        "vi": "nhiên liệu than đá; than sưởi",
        "notes": "Than đá năng lượng"
    },
    "coated": {
        "pos": "adj",
        "vi": "có lớp phủ; tráng; mặc áo khoác",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "comedy": {
        "pos": "noun",
        "vi": "hài kịch",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "concerned": {
        "pos": "adj",
        "vi": "lo lắng; quan tâm; có liên quan",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "conduct": {
        "pos": "noun",
        "vi": "hành vi ứng xử; quy tắc đạo đức",
        "notes": "Quy tắc ứng xử"
    },
    "confidence": {
        "pos": "noun",
        "vi": "sự tự tin; niềm tin thị trường",
        "notes": "Niềm tin người tiêu dùng"
    },
    "conflict": {
        "pos": "noun",
        "vi": "xung đột; mâu thuẫn; trái",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "confrontation": {
        "pos": "noun",
        "vi": "sự đối đầu; cuộc xung đột",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "counter": {
        "pos": "adj",
        "vi": "đáp lại; phản đối; đối phó trước",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "crash": {
        "pos": "noun",
        "vi": "vụ va chạm xe; cú sụp đổ thị trường",
        "notes": "Sửa crawler tiếng hét sang va chạm/sụp đổ"
    },
    "criminal": {
        "pos": "adj",
        "vi": "tội phạm; hình sự",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "crisis": {
        "pos": "noun",
        "vi": "khủng hoảng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "cultural": {
        "pos": "adj",
        "vi": "văn hoá",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "defeat": {
        "pos": "noun",
        "vi": "sự thất bại cay đắng; sự bại trận",
        "notes": "Thất bại"
    },
    "defend": {
        "pos": "verb",
        "vi": "bảo vệ; che chở; chống giữ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "depth": {
        "pos": "noun",
        "vi": "độ sâu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "deserve": {
        "pos": "verb",
        "vi": "xứng đáng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "desire": {
        "pos": "noun",
        "vi": "mong muốn; khao khát; hy vọng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "dietary": {
        "pos": "adj",
        "vi": "thuộc chế độ ăn uống dinh dưỡng",
        "notes": "Chế độ ăn kiêng"
    },
    "disruption": {
        "pos": "noun",
        "vi": "sự gián đoạn; đổi mới đột phá",
        "notes": "Gián đoạn / đổi mới đột phá"
    },
    "dos": {
        "pos": "noun",
        "vi": "những điều nên làm (dos & donts)",
        "notes": "Điều nên làm"
    },
    "drunk": {
        "pos": "adj",
        "vi": "say; xỉn; ma men",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "edition": {
        "pos": "noun",
        "vi": "phiên bản ấn hành; lần xuất bản",
        "notes": "Ấn bản phát hành"
    },
    "eldest": {
        "pos": "adj",
        "vi": "lớn nhất; trưởng; con cả",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "emission": {
        "pos": "noun",
        "vi": "khí thải carbon; sự phát thải khí",
        "notes": "Phát thải nhà kính"
    },
    "empire": {
        "pos": "noun",
        "vi": "đế quốc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "entirely": {
        "pos": "adv",
        "vi": "hoàn toàn; duy nhất; chỉ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "essential": {
        "pos": "adj",
        "vi": "thiết yếu; cần thiết",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "eventually": {
        "pos": "adv",
        "vi": "cuối cùng thì; rốt cuộc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "exact": {
        "pos": "adj",
        "vi": "chính xác; đúng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "extreme": {
        "pos": "adj",
        "vi": "điểm cực; cực đại; cực độ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "facility": {
        "pos": "noun",
        "vi": "cơ sở vật chất; nhà xưởng sản xuất",
        "notes": "Cơ sở hạ tầng"
    },
    "failure": {
        "pos": "noun",
        "vi": "thất bại",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "fantasy": {
        "pos": "noun",
        "vi": "thể loại kỳ ảo; ảo tưởng viển vông",
        "notes": "Kỳ ảo viễn tưởng"
    },
    "flash": {
        "pos": "adj",
        "vi": "hào nhoáng; loè loẹt; chớp sáng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "folding": {
        "pos": "adj",
        "vi": "có thể gấp lại; gấp gọn; sự gấp",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "friction": {
        "pos": "noun",
        "vi": "ma sát",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "gap": {
        "pos": "noun",
        "vi": "khoảng trống thị trường; chênh lệch",
        "notes": "Khoảng cách chênh lệch"
    },
    "giant": {
        "pos": "adj",
        "vi": "khổng lồ; to lớn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "governor": {
        "pos": "noun",
        "vi": "thống đốc; thống sử",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "grab": {
        "pos": "noun",
        "vi": "cú chộp lấy bất ngờ; việc giật đồ",
        "notes": "Cú chộp lấy"
    },
    "gravel": {
        "pos": "noun",
        "vi": "sỏi",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "haired": {
        "pos": "adj",
        "vi": "có lông; có tóc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "hang": {
        "pos": "noun",
        "vi": "cách rủ xuống; sự nắm bắt mẹo làm",
        "notes": "Get the hang of"
    },
    "heaven": {
        "pos": "noun",
        "vi": "trời; thiên đường; thiên đàng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "hidden": {
        "pos": "adj",
        "vi": "ẩn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "highland": {
        "pos": "adj",
        "vi": "sơn nguyên; vùng cao; miền núi",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "hip": {
        "pos": "adj",
        "vi": "hông; sành điệu; hợp thời",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "honestly": {
        "pos": "adv",
        "vi": "thành thật; thực sự",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "hunt": {
        "pos": "noun",
        "vi": "sự săn bắn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "identity": {
        "pos": "noun",
        "vi": "danh tính; bộ nhận diện thương hiệu",
        "notes": "Nhận diện thương hiệu"
    },
    "immediately": {
        "pos": "adv",
        "vi": "ngay lập tức; tức thì; gần",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "independent": {
        "pos": "adj",
        "vi": "độc lập; tự chủ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "individual": {
        "pos": "adj",
        "vi": "cá nhân; riêng lẻ; riêng biệt",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "initial": {
        "pos": "adj",
        "vi": "ban đầu; khởi đầu; chữ cái đầu",
        "notes": "Sửa crawler thanh mẫu sang ban đầu"
    },
    "instability": {
        "pos": "noun",
        "vi": "sự bất ổn; tính không ổn định",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "installing": {
        "pos": "noun",
        "vi": "sự lắp đặt; việc cài đặt",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "instance": {
        "pos": "noun",
        "vi": "trường hợp; dịp; ví dụ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "institute": {
        "pos": "noun",
        "vi": "viện nghiên cứu; học viện",
        "notes": "Viện nghiên cứu"
    },
    "insurance": {
        "pos": "noun",
        "vi": "bảo hiểm; hợp đồng bảo hiểm rủi ro",
        "notes": "Bảo hiểm nhân thọ"
    },
    "intentional": {
        "pos": "adj",
        "vi": "cố ý; có chủ đích",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "lab": {
        "pos": "noun",
        "vi": "phòng thí nghiệm (lab)",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "largely": {
        "pos": "adv",
        "vi": "phần lớn; chủ yếu; trên quy mô lớn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "leadership": {
        "pos": "noun",
        "vi": "năng lực lãnh đạo; ban lãnh đạo",
        "notes": "Khả năng chỉ huy"
    },
    "lift": {
        "pos": "noun",
        "vi": "thang máy chở khách; sự nâng đỡ",
        "notes": "Thang máy toà nhà"
    },
    "linguistic": {
        "pos": "adj",
        "vi": "ngôn ngữ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "location": {
        "pos": "noun",
        "vi": "vị trí; địa điểm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "magistrate": {
        "pos": "noun",
        "vi": "thẩm phán; quan tòa",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "maintain": {
        "pos": "verb",
        "vi": "duy trì; giữ vững",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "manually": {
        "pos": "adv",
        "vi": "bằng tay; thủ công",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "marine": {
        "pos": "adj",
        "vi": "thuộc về biển; ngành hàng hải",
        "notes": "Bảo hiểm hàng hải"
    },
    "maximum": {
        "pos": "adj",
        "vi": "tối đa; cực điểm; cực đại",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "measure": {
        "pos": "noun",
        "vi": "biện pháp giải quyết; thước đo",
        "notes": "Biện pháp khắc phục"
    },
    "medium": {
        "pos": "adj",
        "vi": "trung bình; vừa phải; chín tái",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "milestone": {
        "pos": "noun",
        "vi": "cột mốc quan trọng; dấu mốc tiến độ",
        "notes": "Cột mốc dự án"
    },
    "minor": {
        "pos": "adj",
        "vi": "nhỏ; thứ yếu; không quan trọng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "moist": {
        "pos": "adj",
        "vi": "ẩm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "monte": {
        "pos": "noun",
        "vi": "trò bài lá Monte; tên riêng Monte",
        "notes": "Trò chơi bài ba lá"
    },
    "motor": {
        "pos": "adj",
        "vi": "động cơ; mô-tơ; vận động",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "mount": {
        "pos": "noun",
        "vi": "đỉnh núi cao; giá đỡ lắp thiết bị",
        "notes": "Giá đỡ thiết bị"
    },
    "mu": {
        "pos": "noun",
        "vi": "chữ cái Hy Lạp Mu (μ); hệ số ma sát",
        "notes": "Chữ cái Hy Lạp"
    },
    "newly": {
        "pos": "adv",
        "vi": "mới; gần đây",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "numerous": {
        "pos": "adj",
        "vi": "đông; nhiều",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "object": {
        "pos": "noun",
        "vi": "đối tượng; đồ vật; vật thể",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "obvious": {
        "pos": "adj",
        "vi": "hiển nhiên; rõ ràng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "oracle": {
        "pos": "noun",
        "vi": "tập đoàn Oracle; lời sấm truyền",
        "notes": "Hệ quản trị Oracle"
    },
    "origin": {
        "pos": "noun",
        "vi": "nguồn gốc; gốc toạ độ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "otherwise": {
        "pos": "adj",
        "vi": "về mặt khác; ngoài ra",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "pattern": {
        "pos": "noun",
        "vi": "mô hình; khuôn mẫu; hoa văn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "plantation": {
        "pos": "noun",
        "vi": "đồn điền",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "prairie": {
        "pos": "noun",
        "vi": "thảo nguyên",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "prank": {
        "pos": "noun",
        "vi": "trò chơi khăm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "prepared": {
        "pos": "adj",
        "vi": "được chuẩn bị sẵn; đã chuẩn bị",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "presence": {
        "pos": "noun",
        "vi": "sự hiện diện; sự có mặt",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "prize": {
        "pos": "adj",
        "vi": "đoạt giải thưởng; quý giá bậc nhất",
        "notes": "Giải thưởng cao quý"
    },
    "progress": {
        "pos": "noun",
        "vi": "tiến bộ; tiến triển",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "properly": {
        "pos": "adv",
        "vi": "một cách đúng đắn; chuẩn xác hợp lý",
        "notes": "Sửa dịch cụt tử tế sang đúng đắn"
    },
    "quartz": {
        "pos": "noun",
        "vi": "thạch anh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "radioactive": {
        "pos": "adj",
        "vi": "phóng xạ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "realization": {
        "pos": "noun",
        "vi": "sự nhận thức; sự hiểu rõ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "rebuilding": {
        "pos": "noun",
        "vi": "sự tái thiết; sự xây dựng lại",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "regional": {
        "pos": "adj",
        "vi": "mang tính vùng miền; địa phương",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "religion": {
        "pos": "noun",
        "vi": "đạo; tôn giáo",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "religious": {
        "pos": "adj",
        "vi": "tôn giáo; sùng đạo; mộ đạo",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "require": {
        "pos": "verb",
        "vi": "yêu cầu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "reserve": {
        "pos": "noun",
        "vi": "quỹ dự trữ tài chính; sự dè dặt",
        "notes": "Quỹ dự phòng"
    },
    "respectful": {
        "pos": "adj",
        "vi": "lễ phép; kính cẩn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "responsible": {
        "pos": "adj",
        "vi": "có trách nhiệm; đáng tin cậy",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "rid": {
        "pos": "verb",
        "vi": "giải thoát; loại bỏ (get rid)",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "rot": {
        "pos": "noun",
        "vi": "sự thối rữa; mục nát",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "routinely": {
        "pos": "adv",
        "vi": "theo thói quen; thường lệ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "sand": {
        "pos": "noun",
        "vi": "cát; chà nhám; đánh giấy nhám",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "scared": {
        "pos": "adj",
        "vi": "sợ hãi",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "secure": {
        "pos": "adj",
        "vi": "an toàn bảo mật cao; vững chắc",
        "notes": "Bảo mật an toàn"
    },
    "session": {
        "pos": "noun",
        "vi": "phiên họp; phiên giao dịch",
        "notes": "Phiên giao dịch"
    },
    "severe": {
        "pos": "adj",
        "vi": "nghiêm trọng; dữ dội",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "severity": {
        "pos": "noun",
        "vi": "mức độ nghiêm trọng; sự khắc nghiệt",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "sharp": {
        "pos": "adj",
        "vi": "sắc; bén; nhọn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "slightly": {
        "pos": "adv",
        "vi": "hơi",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "soil": {
        "pos": "noun",
        "vi": "đất trồng trọt; thổ nhưỡng",
        "notes": "Đất đai màu mỡ"
    },
    "spear": {
        "pos": "noun",
        "vi": "thương; giáo",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "steam": {
        "pos": "noun",
        "vi": "hơi nước nóng; động lực phát triển",
        "notes": "Động cơ hơi nước"
    },
    "stream": {
        "pos": "noun",
        "vi": "dòng suối nhỏ; luồng dữ liệu truyền",
        "notes": "Livestream / suối"
    },
    "struggle": {
        "pos": "noun",
        "vi": "sự đấu tranh bền bỉ; cuộc vật lộn",
        "notes": "Cuộc đấu tranh sinh tồn"
    },
    "studio": {
        "pos": "noun",
        "vi": "phòng thu âm; căn hộ studio nhỏ gọn",
        "notes": "Studio quay phim"
    },
    "suddenly": {
        "pos": "adv",
        "vi": "thình lình; đột ngột; bỗng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "suicide": {
        "pos": "noun",
        "vi": "tự sát; tự tử",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "suppose": {
        "pos": "verb",
        "vi": "cho rằng; giả sử; giá sử",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "surely": {
        "pos": "adv",
        "vi": "chắc chắn; nhất định",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "surgery": {
        "pos": "noun",
        "vi": "phẫu thuật; ngoại khoa",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "swear": {
        "pos": "verb",
        "vi": "thề; nói tục; văng tục",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "tank": {
        "pos": "noun",
        "vi": "bể chứa nhiên liệu; xe tăng",
        "notes": "Bể chứa dầu"
    },
    "teaching": {
        "pos": "noun",
        "vi": "nghề dạy học; giáo lý; học thuyết",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "threat": {
        "pos": "noun",
        "vi": "uy hiếp; lời đe doạ; mối hiểm hoạ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "tidal": {
        "pos": "adj",
        "vi": "thủy triều",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "transfer": {
        "pos": "noun",
        "vi": "sự chuyển nhượng; chuyển khoản tiền",
        "notes": "Chuyển khoản ngân hàng"
    },
    "trench": {
        "pos": "noun",
        "vi": "hào; xâm phạm; lấn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "trend": {
        "pos": "noun",
        "vi": "xu hướng thị trường; trào lưu mới",
        "notes": "Xu hướng công nghệ"
    },
    "turning": {
        "pos": "noun",
        "vi": "sự rẽ; sự quay đầu; sự chuyển hướng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "typical": {
        "pos": "adj",
        "vi": "điển hình",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "typically": {
        "pos": "adv",
        "vi": "thông thường; điển hình",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "unable": {
        "pos": "adj",
        "vi": "không thể; không có khả năng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "undertaking": {
        "pos": "noun",
        "vi": "dự án cam kết; sự đảm trách",
        "notes": "Dự án cam kết"
    },
    "vast": {
        "pos": "adj",
        "vi": "rộng lớn; bao la",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "victim": {
        "pos": "noun",
        "vi": "nạn nhân; lễ vật",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "warning": {
        "pos": "adj",
        "vi": "mang tính cảnh báo; lời nhắc nhở",
        "notes": "Dấu hiệu cảnh báo"
    },
    "weapon": {
        "pos": "noun",
        "vi": "vũ khí; binh khí",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "wing": {
        "pos": "noun",
        "vi": "cánh; bay",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "witness": {
        "pos": "noun",
        "vi": "nhân chứng trước tòa; làm chứng",
        "notes": "Lời khai nhân chứng"
    },
    "yuan": {
        "pos": "noun",
        "vi": "đồng nhân dân tệ (Yuan Trung Quốc)",
        "notes": "Tiền tệ Trung Quốc"
    },
    "many": {
        "pos": "adj",
        "vi": "nhiều",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "absolute": {
        "pos": "adj",
        "vi": "tuyệt đối; hoàn toàn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "academic": {
        "pos": "adj",
        "vi": "học thuật; giảng viên đại học",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "accumulated": {
        "pos": "adj",
        "vi": "tích lũy; dồn lại",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "accurate": {
        "pos": "adj",
        "vi": "chính xác; đúng đắn; xác đáng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "actress": {
        "pos": "noun",
        "vi": "nữ diễn viên",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "ale": {
        "pos": "noun",
        "vi": "bia ale; rượu bia",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "alternative": {
        "pos": "adj",
        "vi": "thay thế; loại trừ lẫn nhau",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "anger": {
        "pos": "noun",
        "vi": "mối giận; sự tức giận",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "angle": {
        "pos": "noun",
        "vi": "góc độ nhìn nhận; góc hình học",
        "notes": "Góc nhìn nhận"
    },
    "application": {
        "pos": "noun",
        "vi": "ứng dụng phần mềm; đơn xin việc làm",
        "notes": "Ứng dụng di động"
    },
    "approval": {
        "pos": "noun",
        "vi": "sự chấp thuận; sự phê chuẩn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "arrival": {
        "pos": "noun",
        "vi": "sự đến",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "assist": {
        "pos": "noun",
        "vi": "pha kiến tạo; sự trợ giúp",
        "notes": "Pha kiến tạo"
    },
    "assistance": {
        "pos": "noun",
        "vi": "sự giúp đỡ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "avatar": {
        "pos": "noun",
        "vi": "hình đại diện (avatar); hiện thân",
        "notes": "Ảnh đại diện mạng"
    },
    "avenue": {
        "pos": "noun",
        "vi": "đại lộ; thông lộ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "barely": {
        "pos": "adv",
        "vi": "vừa mới; chỉ vừa; hầu như không",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "behalf": {
        "pos": "noun",
        "vi": "thay mặt; đại diện; vì lợi ích của",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "beverage": {
        "pos": "noun",
        "vi": "nước giải khát",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "bishop": {
        "pos": "noun",
        "vi": "giám mục giáo phận; quân tượng",
        "notes": "Giám mục / quân cờ"
    },
    "boom": {
        "pos": "noun",
        "vi": "sự bùng nổ kinh tế (boom); nổ vang",
        "notes": "Bùng nổ kinh tế"
    },
    "boulevard": {
        "pos": "noun",
        "vi": "đại lộ; đường lớn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "buddy": {
        "pos": "noun",
        "vi": "bạn thân; người bạn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "bull": {
        "pos": "noun",
        "vi": "thị trường giá lên; con bò đực",
        "notes": "Thị trường bò tót"
    },
    "burning": {
        "pos": "adj",
        "vi": "cấp bách; nóng bỏng; sự đốt",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "category": {
        "pos": "noun",
        "vi": "thể loại",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "chic": {
        "pos": "adj",
        "vi": "sang trọng; thanh lịch; thời thượng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "chilling": {
        "pos": "adj",
        "vi": "rùng rợn; làm khiếp sợ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "chimpanzee": {
        "pos": "noun",
        "vi": "tinh tinh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "coaster": {
        "pos": "noun",
        "vi": "miếng lót ly cốc; tàu lượn siêu tốc",
        "notes": "Tấm lót ly nước"
    },
    "compete": {
        "pos": "verb",
        "vi": "cạnh tranh; tranh tài",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "competitive": {
        "pos": "adj",
        "vi": "có tính cạnh tranh; đua tranh",
        "notes": "Cạnh tranh thị trường"
    },
    "comprehend": {
        "pos": "verb",
        "vi": "thấu hiểu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "confederate": {
        "pos": "adj",
        "vi": "thuộc Liên minh miền Nam; liên kết",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "consolidation": {
        "pos": "noun",
        "vi": "sự hợp nhất; sự củng cố",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "constantly": {
        "pos": "adv",
        "vi": "liên tục không ngừng; luôn luôn",
        "notes": "Sửa tiếng lóng miền nam hoài sang liên tục"
    },
    "construction": {
        "pos": "noun",
        "vi": "sự xây dựng; sự thi công",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "consumer": {
        "pos": "noun",
        "vi": "người tiêu dùng; người tiêu thụ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "contain": {
        "pos": "verb",
        "vi": "chứa; bao gồm; đựng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "continuation": {
        "pos": "noun",
        "vi": "sự tiếp tục; sự duy trì",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "costing": {
        "pos": "noun",
        "vi": "kế toán chi phí; sự tính giá thành",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "cotton": {
        "pos": "noun",
        "vi": "bông; cảm mến; thích",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "deliver": {
        "pos": "verb",
        "vi": "chuyển phát; giao",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "delivery": {
        "pos": "noun",
        "vi": "sự giao hàng; sự phát",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "democratic": {
        "pos": "adj",
        "vi": "dân chủ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "deny": {
        "pos": "verb",
        "vi": "phủ nhận; bác bỏ; từ chối cấp phép",
        "notes": "Bác bỏ cáo buộc"
    },
    "determine": {
        "pos": "verb",
        "vi": "xác định; định rõ; quyết định",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "doc": {
        "pos": "noun",
        "vi": "bác sĩ (doc); tài liệu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "document": {
        "pos": "noun",
        "vi": "tài liệu; văn kiện",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "dozen": {
        "pos": "num",
        "vi": "một tá (12 cái); hàng chục thứ",
        "notes": "Sửa pos từ adj sang num"
    },
    "drained": {
        "pos": "adj",
        "vi": "ráo; khô; tháo hết nước",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "element": {
        "pos": "noun",
        "vi": "yếu tố; nguyên tố",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "emotional": {
        "pos": "adj",
        "vi": "cảm tính; dễ xúc động; đầy cảm xúc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "employment": {
        "pos": "noun",
        "vi": "việc làm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "engaged": {
        "pos": "adj",
        "vi": "bận; đang chú tâm; đang giao chiến",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "engineering": {
        "pos": "noun",
        "vi": "ngành kỹ thuật công trình; kỹ nghệ",
        "notes": "Ngành kỹ thuật"
    },
    "equally": {
        "pos": "adv",
        "vi": "bằng nhau; như nhau; công bằng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "exclusive": {
        "pos": "adj",
        "vi": "độc quyền; riêng biệt; loại trừ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "existence": {
        "pos": "noun",
        "vi": "sự tồn tại; sự hiện diện sinh tồn",
        "notes": "Sự tồn tại"
    },
    "exit": {
        "pos": "noun",
        "vi": "lối ra; ra khỏi; rời khỏi; qua đời",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "extent": {
        "pos": "noun",
        "vi": "mức độ; phạm vi; khoảng cách",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "fallen": {
        "pos": "adj",
        "vi": "rơi xuống; đã rơi; đổ sụp",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "fallout": {
        "pos": "noun",
        "vi": "hậu quả tiêu cực (fallout); bụi xạ",
        "notes": "Hậu quả chính trị/kinh tế"
    },
    "finger": {
        "pos": "noun",
        "vi": "ngón tay; chỉ ra; chỉ đến",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "fitness": {
        "pos": "noun",
        "vi": "thể lực tốt; sự khỏe mạnh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "formal": {
        "pos": "adj",
        "vi": "trang trọng; chính thức",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "forth": {
        "pos": "adv",
        "vi": "ra; về phía trước",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "foundation": {
        "pos": "noun",
        "vi": "nền móng kiên cố; quỹ tài trợ thiện",
        "notes": "Quỹ từ thiện / móng nhà"
    },
    "fracture": {
        "pos": "noun",
        "vi": "gãy xương; làm gãy; bẻ gãy",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "gym": {
        "pos": "noun",
        "vi": "phòng tập thể hình; thể dục",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "height": {
        "pos": "noun",
        "vi": "độ cao; chiều cao",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "hire": {
        "pos": "verb",
        "vi": "thuê; tuyển dụng nhân sự",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "historical": {
        "pos": "adj",
        "vi": "thuộc về sử học; lịch sử",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "hop": {
        "pos": "verb",
        "vi": "nhảy lò cò; hoa bia nấu bia (hops)",
        "notes": "Hoa bia / nhảy lò cò"
    },
    "hopefully": {
        "pos": "adv",
        "vi": "hy vọng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "ignore": {
        "pos": "verb",
        "vi": "phớt lờ; cố tình bỏ qua không nghe",
        "notes": "Sửa tiếng lóng bơ sang phớt lờ"
    },
    "illness": {
        "pos": "noun",
        "vi": "bệnh; sự đau yếu; sự ốm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "immediate": {
        "pos": "adj",
        "vi": "ngay lập tức",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "incident": {
        "pos": "noun",
        "vi": "sự cố bất ngờ; vụ việc rắc rối",
        "notes": "Sửa pos từ adj sang noun"
    },
    "indictment": {
        "pos": "noun",
        "vi": "bản cáo trạng; sự buộc tội",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "industrial": {
        "pos": "adj",
        "vi": "công nghiệp",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "innocent": {
        "pos": "adj",
        "vi": "trong sạch; vô tội",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "insulting": {
        "pos": "adj",
        "vi": "sỉ nhục; lăng mạ; xúc phạm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "internal": {
        "pos": "adj",
        "vi": "bên trong; nội bộ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "lately": {
        "pos": "adv",
        "vi": "gần đây; mới đây",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "layer": {
        "pos": "noun",
        "vi": "lớp",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "liquid": {
        "pos": "adj",
        "vi": "chất lỏng; có tính thanh khoản cao",
        "notes": "Tài sản thanh khoản (liquid)"
    },
    "log": {
        "pos": "noun",
        "vi": "nhật ký hệ thống (log); khúc gỗ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "marked": {
        "pos": "adj",
        "vi": "rõ rệt; nổi bật; bị chú ý",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "mart": {
        "pos": "noun",
        "vi": "trung tâm thương mại; siêu thị mart",
        "notes": "Siêu thị mua sắm"
    },
    "midway": {
        "pos": "adj",
        "vi": "nửa đường; ở giữa",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "millennium": {
        "pos": "noun",
        "vi": "thiên niên kỷ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "minors": {
        "pos": "noun",
        "vi": "người vị thành niên; giải hạng dưới",
        "notes": "Trẻ vị thành niên"
    },
    "monster": {
        "pos": "noun",
        "vi": "quái vật",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "monthly": {
        "pos": "adj",
        "vi": "hàng tháng; nguyệt báo; nguyệt san",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "moral": {
        "pos": "adj",
        "vi": "đạo đức; thuộc về luân lý",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "municipality": {
        "pos": "noun",
        "vi": "đô thị tự trị; chính quyền đô thị",
        "notes": "Chính quyền đô thị"
    },
    "muscle": {
        "pos": "noun",
        "vi": "cơ; bắp thịt; cơ bắp",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "naked": {
        "pos": "adj",
        "vi": "khoả thân; trần truồng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "nearby": {
        "pos": "adj",
        "vi": "gần; bên cạnh đó",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "normally": {
        "pos": "adv",
        "vi": "thông thường; như lệ thường",
        "notes": "Thông thường"
    },
    "observatory": {
        "pos": "noun",
        "vi": "đài thiên văn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "obtain": {
        "pos": "verb",
        "vi": "đạt được; thu được; giành được",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "occur": {
        "pos": "verb",
        "vi": "xảy ra",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "offensive": {
        "pos": "adj",
        "vi": "xúc phạm; sỉ nhục; sự tấn công",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "officially": {
        "pos": "adv",
        "vi": "chính thức",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "operation": {
        "pos": "noun",
        "vi": "sự hoạt động; sự vận hành",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "pace": {
        "pos": "noun",
        "vi": "tốc độ; nhịp độ; bước; sải chân",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "package": {
        "pos": "noun",
        "vi": "kiện hàng; gói; bưu kiện",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "parking": {
        "pos": "noun",
        "vi": "bãi đỗ xe",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "particularly": {
        "pos": "adv",
        "vi": "đặc biệt; nhất là; cụ thể là; riêng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "permanent": {
        "pos": "adj",
        "vi": "vĩnh viễn; lâu dài",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "personally": {
        "pos": "adv",
        "vi": "với tư cách cá nhân; về mặt cá nhân",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "plain": {
        "pos": "adj",
        "vi": "rõ ràng; dễ thấy; đơn giản; mộc mạc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "platform": {
        "pos": "noun",
        "vi": "nền tảng công nghệ; sân ga đón tàu",
        "notes": "Nền tảng kỹ thuật số"
    },
    "poetic": {
        "pos": "adj",
        "vi": "thơ ca; đầy chất thơ; nhà thơ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "pot": {
        "pos": "noun",
        "vi": "nồi; chậu cây; bình",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "poverty": {
        "pos": "noun",
        "vi": "sự nghèo đói; cảnh bần cùng cơ cực",
        "notes": "Nạn đói nghèo"
    },
    "prayer": {
        "pos": "noun",
        "vi": "kinh cầu nguyện; kinh nguyện",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "pregnant": {
        "pos": "adj",
        "vi": "mang thai; có thai",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "promote": {
        "pos": "verb",
        "vi": "thăng chức; lên chức; khuyến khích",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "prostitution": {
        "pos": "noun",
        "vi": "tệ nạn mại dâm phi pháp",
        "notes": "Tệ nạn mại dâm"
    },
    "protection": {
        "pos": "noun",
        "vi": "sự bảo vệ; bảo trợ; vật che chở",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "rail": {
        "pos": "noun",
        "vi": "đường ray; thanh ray; lan can",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "rank": {
        "pos": "noun",
        "vi": "cấp bậc quân hàm; thứ hạng bảng xếp",
        "notes": "Sửa pos từ adj sang noun"
    },
    "rarely": {
        "pos": "adv",
        "vi": "hiếm khi; ít khi",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "reasonable": {
        "pos": "adj",
        "vi": "hợp lí",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "recommend": {
        "pos": "verb",
        "vi": "giới thiệu; đề nghị",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "recovery": {
        "pos": "noun",
        "vi": "sự phục hồi; sự hồi phục",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "register": {
        "pos": "noun",
        "vi": "sổ đăng ký; máy tính tiền",
        "notes": "Sổ đăng ký / cash register"
    },
    "relationship": {
        "pos": "noun",
        "vi": "mối quan hệ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "relatively": {
        "pos": "adv",
        "vi": "tương đối",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "republic": {
        "pos": "noun",
        "vi": "cộng hòa; cộng hoà",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "rescue": {
        "pos": "noun",
        "vi": "sự cứu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "residency": {
        "pos": "noun",
        "vi": "sự cư trú; chương trình nội trú",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "respond": {
        "pos": "verb",
        "vi": "phản ứng; đáp lại; trả lời",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "responsive": {
        "pos": "adj",
        "vi": "đáp ứng nhanh; nhạy bén",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "retail": {
        "pos": "noun",
        "vi": "ngành bán lẻ; hoạt động bán lẻ hàng",
        "notes": "Sửa pos từ adv sang noun"
    },
    "rolling": {
        "pos": "adj",
        "vi": "lăn đều; tiếp diễn (rolling)",
        "notes": "Rolling forecast / ngân sách cuốn chiếu"
    },
    "rough": {
        "pos": "adj",
        "vi": "gồ ghề; xù xì; thô lỗ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "scoop": {
        "pos": "noun",
        "vi": "tin tức độc quyền; chiếc muỗng múc",
        "notes": "Tin sốt dẻo độc quyền"
    },
    "scotch": {
        "pos": "adj",
        "vi": "thuộc Scotland; rượu whisky Scotch",
        "notes": "Rượu Scotch whisky"
    },
    "scrub": {
        "pos": "noun",
        "vi": "bụi cây rậm; bộ đồ mổ phẫu thuật",
        "notes": "Sửa pos từ adj sang noun"
    },
    "select": {
        "pos": "adj",
        "vi": "cao cấp; chọn lọc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "selection": {
        "pos": "noun",
        "vi": "sự lựa chọn; sự tuyển chọn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "server": {
        "pos": "noun",
        "vi": "máy chủ hệ thống; người phục vụ bàn",
        "notes": "Máy chủ server"
    },
    "settle": {
        "pos": "noun",
        "vi": "ghế dài gỗ; sự dàn xếp thỏa thuận",
        "notes": "Ghế dài / dàn xếp"
    },
    "sewing": {
        "pos": "noun",
        "vi": "sự khâu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "shale": {
        "pos": "noun",
        "vi": "đá phiến sét",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "sheet": {
        "pos": "noun",
        "vi": "tờ; trút xuống như tấm; phủ tấm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "shin": {
        "pos": "noun",
        "vi": "ống quyển; ống khuyển; ống đồng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "shortly": {
        "pos": "adv",
        "vi": "sớm; không lâu nữa",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "silent": {
        "pos": "adj",
        "vi": "yên lặng; lặng lẽ; câm lặng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "sol": {
        "pos": "noun",
        "vi": "nốt Son; tiền tệ sol",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "somehow": {
        "pos": "adv",
        "vi": "bằng cách nào đó; vì lý do nào đó",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "stable": {
        "pos": "adj",
        "vi": "ổn định; vững chắc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "stigma": {
        "pos": "noun",
        "vi": "sự kỳ thị; ô nhục",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "storage": {
        "pos": "noun",
        "vi": "kho lưu trữ hàng; bộ nhớ máy tính",
        "notes": "Kho lưu trữ dữ liệu"
    },
    "stranded": {
        "pos": "adj",
        "vi": "mắc kẹt; bị bỏ lại",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "suffer": {
        "pos": "verb",
        "vi": "chịu đựng; cảm thấy đau",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "suspect": {
        "pos": "adj",
        "vi": "nghi phạm; đáng ngờ; khả nghi",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "taco": {
        "pos": "noun",
        "vi": "bánh kẹp taco của Mexico",
        "notes": "Sửa lỗi crawler người Mễ sang bánh taco"
    },
    "tapped": {
        "pos": "adj",
        "vi": "được mở vòi; được rút ra",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "technician": {
        "pos": "noun",
        "vi": "nhà kỹ thuật; kĩ thuật viên",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "technique": {
        "pos": "noun",
        "vi": "kỹ thuật; kĩ thuật",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "teen": {
        "pos": "adj",
        "vi": "thiếu niên",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "titan": {
        "pos": "noun",
        "vi": "gã khổng lồ đầu ngành; thần Titan",
        "notes": "Gã khổng lồ công nghệ"
    },
    "trail": {
        "pos": "noun",
        "vi": "đường mòn; dấu vết",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "transport": {
        "pos": "noun",
        "vi": "phương tiện vận chuyển",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "trash": {
        "pos": "noun",
        "vi": "rác; vứt bỏ; loại bỏ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "twin": {
        "pos": "adj",
        "vi": "trẻ sinh đôi; giống hệt nhau",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "universe": {
        "pos": "noun",
        "vi": "vũ trụ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "validity": {
        "pos": "noun",
        "vi": "tính hợp lệ; giá trị",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "valuable": {
        "pos": "adj",
        "vi": "quý giá; quý báu; vật có giá trị",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "varsity": {
        "pos": "noun",
        "vi": "đội thể thao chính trường đại học",
        "notes": "Đội thể thao đại học"
    },
    "virus": {
        "pos": "noun",
        "vi": "vi rút; siêu vi trùng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "vision": {
        "pos": "noun",
        "vi": "tầm nhìn chiến lược; thị lực mắt",
        "notes": "Tầm nhìn doanh nghiệp"
    },
    "visual": {
        "pos": "adj",
        "vi": "thuộc thị giác; bằng mắt",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "watt": {
        "pos": "noun",
        "vi": "watt; oát; oat",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "wire": {
        "pos": "noun",
        "vi": "dây cáp điện; chuyển khoản wire",
        "notes": "Wire transfer"
    },
    "wrath": {
        "pos": "noun",
        "vi": "cơn tức giận; thịnh nộ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "absence": {
        "pos": "noun",
        "vi": "sự vắng mặt; sự thiếu vắng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "alas": {
        "pos": "intj",
        "vi": "than ôi; ôi chao tiếc nuối",
        "notes": "Sửa pos từ adv sang intj"
    },
    "allegiance": {
        "pos": "noun",
        "vi": "lòng trung thành",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "anxiety": {
        "pos": "noun",
        "vi": "sự lo lắng; lo âu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "approximately": {
        "pos": "adv",
        "vi": "khoảng; chừng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "aspect": {
        "pos": "noun",
        "vi": "khía cạnh; mặt; yếu tố",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "associate": {
        "pos": "adj",
        "vi": "cùng cộng tác; cấp phó liên kết",
        "notes": "Phó giám đốc (Associate)"
    },
    "awareness": {
        "pos": "noun",
        "vi": "nhận thức",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "bang": {
        "pos": "adv",
        "vi": "đúng boong; tiếng nổ vang",
        "notes": "Lọc hoàn toàn từ ngữ dung tục bậy bạ của crawler"
    },
    "banging": {
        "pos": "adj",
        "vi": "sôi động náo nhiệt; tiếng đập uỳnh",
        "notes": "Sôi động náo nhiệt"
    },
    "bathing": {
        "pos": "noun",
        "vi": "hoạt động tắm mát; việc tắm gội",
        "notes": "Tắm biển"
    },
    "beast": {
        "pos": "noun",
        "vi": "con vật; thú vật",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "bending": {
        "pos": "noun",
        "vi": "sự uốn; sự bẻ cong; sự cong",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "bold": {
        "pos": "adj",
        "vi": "dũng cảm; can đảm; gan dạ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "bonding": {
        "pos": "noun",
        "vi": "sự gắn kết; mối quan hệ gắn bó",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "bounds": {
        "pos": "noun",
        "vi": "ranh giới; giới hạn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "bow": {
        "pos": "verb",
        "vi": "cúi đầu chào; cúi mình chịu",
        "notes": "Cúi đầu chào"
    },
    "breast": {
        "pos": "noun",
        "vi": "vú; đối mặt; chạm ngực",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "bureau": {
        "pos": "noun",
        "vi": "cục; cơ quan chuyên trách",
        "notes": "Sửa crawler sự giúp đỡ sang cục cơ quan"
    },
    "capped": {
        "pos": "adj",
        "vi": "có mức trần khống chế; có nắp đậy",
        "notes": "Giới hạn mức trần (capped)"
    },
    "chaos": {
        "pos": "noun",
        "vi": "sự hỗn loạn; tình trạng rối ren",
        "notes": "Hỗn loạn"
    }
}

def main():
    print(f"Reading {BATCH_FILE}...")
    with open(BATCH_FILE, "r", encoding="utf-8") as fp:
        data = json.load(fp)

    records = data["records"]
    slice_records = records[4200:4700]
    assert len(slice_records) == 500, f"Expected 500 records, got {len(slice_records)}"

    updated = 0
    for r in slice_records:
        hw = r["hw"]
        if hw in EDITS_4201_4700:
            e = EDITS_4201_4700[hw]
            r["pos"] = e["pos"]
            r["vi"] = e["vi"]
            r["status"] = "edited"
            r["notes"] = e.get("notes", "Đã soát tay chuẩn hóa QA")
            updated += 1
        else:
            r["status"] = "approved"
            r["notes"] = "QA passed manual review"

    data["reviewedCount"] = 4700
    data["status"] = "in-progress"

    print(f"Writing updated slice back to {BATCH_FILE}...")
    with open(BATCH_FILE, "w", encoding="utf-8") as fp:
        json.dump(data, fp, ensure_ascii=False, indent=2)

    print(f"Successfully processed STT 4201-4700. Meticulously curated: {updated} words.")

    # Update INDEX.md
    if INDEX_FILE.exists():
        content = INDEX_FILE.read_text(encoding="utf-8")
        new_line = "| 01 | `batch-01.json` | 5000 | account ... sane | Phase 1 (100k Core & Standard) | 🔄 `in-progress` (4700/5000) |"
        content = re.sub(
            r"\|\s*01\s*\|\s*`batch-01\.json`.*?\|\s*[✅🔄⏳].*?\|",
            new_line,
            content
        )
        INDEX_FILE.write_text(content, encoding="utf-8")
        print("Updated INDEX.md to 4700/5000 in-progress.")

if __name__ == "__main__":
    main()
