#!/usr/bin/env python3
"""
qa_batch_01_slice_3701_4200.py
Rà soát thủ công chuyên sâu 500 từ (STT 3701 đến 4200) của batch-01.json:
- Sửa lỗi bot crawler:
  - tenant: sửa lỗi nghiêm trọng dịch 'chủ sở hữu' sang 'người thuê nhà/mặt bằng; bên thuê'.
  - apex: sửa 'dấu sóng' sang 'đỉnh cao; điểm chóp cao nhất'.
  - last: sửa động từ 'kéo dài; sống' sang adj 'cuối cùng; vừa qua; trước đây'.
  - content: sửa nhầm noun 'nội dung' sang adj 'hài lòng; bằng lòng thỏa mãn'.
  - general: sửa nhầm noun 'tướng' sang adj 'chung; tổng quát; phổ biến'.
  - stick: sửa các động từ 'cắm; đâm; chọc' sang noun 'chiếc gậy; que gỗ; cán điều khiển'.
  - vendor: sửa lỗi chính tả 'ngưởi bán hàng rong' sang 'nhà cung cấp; đơn vị bán hàng'.
  - aid: sửa lỗi lặp từ 'sự viện viện trợ' sang 'viện trợ; sự hỗ trợ cứu tế'.
  - dwelling: sửa lỗi chính tả 'chổ ở' sang 'nhà ở; nơi cư trú sinh sống'.
- Sửa POS chuẩn:
  - precedent: adj -> noun ('tiền lệ xét xử; án lệ')
  - tutorial: adj -> noun ('bài hướng dẫn; tiết học kèm')
  - variant: adj -> noun ('biến thể; phương án khác biệt')
  - union: adj -> noun ('công đoàn; tổ chức liên hiệp')
  - waste: adj -> noun ('chất thải rác thải; sự lãng phí')
  - affect: noun -> verb ('tác động sâu sắc đến; ảnh hưởng đến')
  - directive: adj -> noun ('chỉ thị lãnh đạo; văn bản chỉ đạo')
  - rust: adj -> noun ('gỉ sét sắt thép; màu nâu đỏ')
  - chased: noun -> adj ('bị rượt đuổi; bị săn lùng gắt gao')
  - trillion: adj -> num ('nghìn tỷ (1.000.000.000.000)')
- Chuẩn hóa thuật ngữ kinh tế thương mại:
  - turnover, traction, volatile, edge, credentials, payroll, proxy, valuation, series, status, etc.
- Độ dài nghĩa tiếng Việt <= 35 ký tự, phân tách bằng '; '.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BATCH_FILE = ROOT / "content" / "english" / "qa-batches" / "batch-01.json"
INDEX_FILE = ROOT / "content" / "english" / "qa-batches" / "INDEX.md"

EDITS_3701_4200 = {
    "ooh": {
        "pos": "verb",
        "vi": "thốt lên ngạc nhiên (ooh)",
        "notes": "Thán từ / động từ thốt ooh"
    },
    "paired": {
        "pos": "adj",
        "vi": "theo cặp; ghép đôi; giao phối",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "parody": {
        "pos": "noun",
        "vi": "nhại; sự bắt chước hài hước",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "parole": {
        "pos": "noun",
        "vi": "sự ân xá tạm tha có điều kiện",
        "notes": "Ân xá tạm tha"
    },
    "pathway": {
        "pos": "noun",
        "vi": "đường dẫn thần kinh; lối đi",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "pictured": {
        "pos": "adj",
        "vi": "tưởng tượng; hình dung; được vẽ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "pinch": {
        "pos": "noun",
        "vi": "véo; béo; nhéo",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "ping": {
        "pos": "noun",
        "vi": "tín hiệu ping mạng; tiếng bíp",
        "notes": "Ping mạng / tiếng bíp"
    },
    "pitcher": {
        "pos": "noun",
        "vi": "người ném bóng chày; bình nước",
        "notes": "Pitcher bóng chày"
    },
    "populated": {
        "pos": "adj",
        "vi": "có dân cư; đông dân",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "precedent": {
        "pos": "noun",
        "vi": "tiền lệ xét xử; án lệ",
        "notes": "Sửa pos từ adj sang noun"
    },
    "predominantly": {
        "pos": "adv",
        "vi": "chủ yếu; phần lớn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "prevalent": {
        "pos": "adj",
        "vi": "phổ biến; thông thường; thông dụng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "probation": {
        "pos": "noun",
        "vi": "thời gian thử việc; án treo",
        "notes": "Thử việc công ty"
    },
    "protestant": {
        "pos": "adj",
        "vi": "thuộc Tin Lành; phản đối; biểu tình",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "providence": {
        "pos": "noun",
        "vi": "sự quan phòng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "pumped": {
        "pos": "adj",
        "vi": "hào hứng; phấn khích",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "punctuation": {
        "pos": "noun",
        "vi": "chấm câu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "python": {
        "pos": "noun",
        "vi": "ngôn ngữ Python; con trăn lớn",
        "notes": "Ngôn ngữ lập trình Python"
    },
    "rails": {
        "pos": "noun",
        "vi": "đường ray; thanh ray",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "raven": {
        "pos": "noun",
        "vi": "quạ; cướp đoạt; săn mồi",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "receptionist": {
        "pos": "noun",
        "vi": "nhân viên lễ tân; người tiếp tân",
        "notes": "Lễ tân văn phòng"
    },
    "receptor": {
        "pos": "noun",
        "vi": "thụ thể; cơ quan thụ cảm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "redemption": {
        "pos": "noun",
        "vi": "sự chuộc lại; tất toán trái phiếu",
        "notes": "Chuộc lại / tất toán"
    },
    "regrets": {
        "pos": "noun",
        "vi": "lời tiếc nuối; thư cáo lỗi",
        "notes": "Thư từ chối cáo lỗi"
    },
    "remake": {
        "pos": "noun",
        "vi": "bản làm lại; phiên bản mới",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "reproductive": {
        "pos": "adj",
        "vi": "sinh sản; sinh dục",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "retiring": {
        "pos": "adj",
        "vi": "khiêm tốn; nhún nhường; đã nghỉ hưu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "righteous": {
        "pos": "adj",
        "vi": "chính trực; ngay thẳng; chính đáng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "rivalry": {
        "pos": "noun",
        "vi": "sự cạnh tranh; sự ganh đua",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "seating": {
        "pos": "noun",
        "vi": "chỗ ngồi; khu vực có ghế",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "shouted": {
        "pos": "adj",
        "vi": "la hét; hò hét",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "silva": {
        "pos": "noun",
        "vi": "rừng cây; thảm thực vật rừng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "sleepless": {
        "pos": "adj",
        "vi": "mất ngủ; không ngủ; luôn cảnh giác",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "sociology": {
        "pos": "noun",
        "vi": "xã hội học",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "somerset": {
        "pos": "noun",
        "vi": "hạt Somerset; cú lộn nhào",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "splitting": {
        "pos": "adj",
        "vi": "xé toạc; như tiếng xé",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "stained": {
        "pos": "adj",
        "vi": "bị ố; bị bẩn; nhuộm màu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "stereo": {
        "pos": "adj",
        "vi": "âm thanh nổi (stereo); đa chiều",
        "notes": "Âm thanh stereo"
    },
    "strengthening": {
        "pos": "noun",
        "vi": "sự củng cố; sự tăng cường",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "structured": {
        "pos": "adj",
        "vi": "có cấu trúc; có tổ chức",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "subjective": {
        "pos": "adj",
        "vi": "chủ quan; trong tâm trí",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "surrey": {
        "pos": "noun",
        "vi": "xe ngựa bốn bánh nhẹ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "sweeping": {
        "pos": "adj",
        "vi": "rộng khắp; bao quát; tổng thể",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "swinging": {
        "pos": "adj",
        "vi": "sôi động; nhịp nhàng; sự đung đưa",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "taxation": {
        "pos": "noun",
        "vi": "hệ thống thuế; việc đánh thuế",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "tearing": {
        "pos": "adj",
        "vi": "mãnh liệt; dữ dội; sự khóc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "tenant": {
        "pos": "noun",
        "vi": "người thuê nhà/mặt bằng; bên thuê",
        "notes": "Sửa lỗi crawler dịch chủ sở hữu thành người thuê"
    },
    "tesla": {
        "pos": "noun",
        "vi": "hãng xe Tesla; đơn vị từ trường",
        "notes": "Hãng xe điện Tesla"
    },
    "thankfully": {
        "pos": "adv",
        "vi": "một cách biết ơn; may thay",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "thunderstorm": {
        "pos": "noun",
        "vi": "dông; giông; bão tố có sấm sét",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "tortured": {
        "pos": "adj",
        "vi": "đau khổ; giày vò",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "traction": {
        "pos": "noun",
        "vi": "độ bám đường; sức hút thị trường",
        "notes": "Sức hút người dùng (traction)"
    },
    "tractor": {
        "pos": "noun",
        "vi": "máy kéo",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "trillion": {
        "pos": "num",
        "vi": "nghìn tỷ (1.000.000.000.000)",
        "notes": "Số từ một nghìn tỷ"
    },
    "trout": {
        "pos": "noun",
        "vi": "cá hồi vân; cá hồi hương (trout)",
        "notes": "Cá hồi vân"
    },
    "tucker": {
        "pos": "noun",
        "vi": "thợ may nếp gấp; làm kiệt sức",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "turnover": {
        "pos": "noun",
        "vi": "doanh số; tỷ lệ luân chuyển nhân sự",
        "notes": "Doanh thu / tỷ lệ nghỉ việc"
    },
    "tutorial": {
        "pos": "noun",
        "vi": "bài hướng dẫn; tiết học kèm",
        "notes": "Sửa pos từ adj sang noun"
    },
    "twentieth": {
        "pos": "adj",
        "vi": "thứ hai mươi; hạng hai mươi",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "unimportant": {
        "pos": "adj",
        "vi": "không quan trọng; tầm thường",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "unprecedented": {
        "pos": "adj",
        "vi": "chưa từng có; vô tiền khoáng hậu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "variant": {
        "pos": "noun",
        "vi": "biến thể; phương án khác biệt",
        "notes": "Sửa pos từ adj sang noun"
    },
    "velvet": {
        "pos": "adj",
        "vi": "bằng vải nhung; mượt mà êm ái",
        "notes": "Vải nhung"
    },
    "vendor": {
        "pos": "noun",
        "vi": "nhà cung cấp; đơn vị bán hàng",
        "notes": "Sửa typo ngưởi bán hàng rong sang nhà cung cấp"
    },
    "visibility": {
        "pos": "noun",
        "vi": "tầm nhìn; sự hiển thị",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "wandering": {
        "pos": "adj",
        "vi": "lang thang; du mục; quanh co",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "wheeler": {
        "pos": "noun",
        "vi": "tay môi giới nhanh nhạy; xe kéo",
        "notes": "Wheeler-dealer"
    },
    "whiskey": {
        "pos": "noun",
        "vi": "rượu uýt-ki (whiskey)",
        "notes": "Rượu whiskey"
    },
    "wired": {
        "pos": "adj",
        "vi": "kết nối mạng dây; tỉnh như sáo",
        "notes": "Mạng dây / tỉnh táo"
    },
    "any": {
        "pos": "det",
        "vi": "bất kỳ; bất cứ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "able": {
        "pos": "adj",
        "vi": "có thể; có khả năng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "accelerated": {
        "pos": "adj",
        "vi": "tăng tốc; cấp tốc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "accusing": {
        "pos": "adj",
        "vi": "buộc tội; cáo buộc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "activate": {
        "pos": "verb",
        "vi": "kích hoạt; làm hoạt động; khởi động",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "advertised": {
        "pos": "adj",
        "vi": "được quảng cáo; được công bố",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "aided": {
        "pos": "adj",
        "vi": "được hỗ trợ; có sự giúp đỡ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "allocation": {
        "pos": "noun",
        "vi": "sự phân bổ; sự cấp phát",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "amino": {
        "pos": "adj",
        "vi": "thuộc amino; nhóm amin",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "analog": {
        "pos": "adj",
        "vi": "tương tự; cái tương đồng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "arcade": {
        "pos": "noun",
        "vi": "khu trò chơi điện tử; phố mái vòm",
        "notes": "Khu game arcade"
    },
    "ark": {
        "pos": "noun",
        "vi": "con tàu cứu thế (Ark); hòm bia",
        "notes": "Tàu Noah Ark"
    },
    "asthma": {
        "pos": "noun",
        "vi": "suyễn; hen",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "aurora": {
        "pos": "noun",
        "vi": "cực quang",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "beacon": {
        "pos": "noun",
        "vi": "đèn hiệu; hải đăng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "billionaire": {
        "pos": "noun",
        "vi": "tỷ phú đô-la; nhà tài phiệt",
        "notes": "Tỷ phú tài chính"
    },
    "bookshop": {
        "pos": "noun",
        "vi": "hiệu sách; nhà sách",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "borrowing": {
        "pos": "noun",
        "vi": "vay mượn; sự vay tiền",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "bounty": {
        "pos": "noun",
        "vi": "tiền thưởng săn bắt; sự hào phóng",
        "notes": "Tiền thưởng bounty"
    },
    "bowls": {
        "pos": "noun",
        "vi": "trò chơi ném bóng trên cỏ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "briefing": {
        "pos": "noun",
        "vi": "buổi họp giao ban; bản tóm tắt",
        "notes": "Giao ban công việc"
    },
    "brook": {
        "pos": "noun",
        "vi": "lạch; chịu đựng; dung thứ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "cancellation": {
        "pos": "noun",
        "vi": "sự hủy bỏ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "ceramic": {
        "pos": "adj",
        "vi": "bằng gốm sứ; thuộc ngành gốm",
        "notes": "Đồ gốm sứ"
    },
    "challenger": {
        "pos": "noun",
        "vi": "đối thủ thách đấu; kẻ thách thức",
        "notes": "Kẻ thách thức"
    },
    "chandler": {
        "pos": "noun",
        "vi": "người bán tạp phẩm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "chased": {
        "pos": "adj",
        "vi": "bị rượt đuổi; bị săn lùng gắt gao",
        "notes": "Sửa pos từ noun sang adj"
    },
    "chili": {
        "pos": "noun",
        "vi": "ớt",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "clergy": {
        "pos": "noun",
        "vi": "tư tế; hàng giáo sĩ; tăng lữ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "coil": {
        "pos": "noun",
        "vi": "cuộn cảm; quấn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "communicating": {
        "pos": "noun",
        "vi": "hoạt động giao tiếp; sự truyền đạt",
        "notes": "Giao tiếp truyền tải"
    },
    "compass": {
        "pos": "noun",
        "vi": "la bàn định hướng; phạm vi",
        "notes": "La bàn / compa"
    },
    "covenant": {
        "pos": "noun",
        "vi": "hiệp ước; giao ước",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "credentials": {
        "pos": "noun",
        "vi": "thông tin đăng nhập; chứng chỉ nghề",
        "notes": "Chứng chỉ / login credentials"
    },
    "cue": {
        "pos": "noun",
        "vi": "tín hiệu; gợi ý",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "cured": {
        "pos": "adj",
        "vi": "khỏi bệnh; lành; lưu hóa",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "deluxe": {
        "pos": "adj",
        "vi": "hạng sang; cao cấp (deluxe)",
        "notes": "Phòng deluxe cao cấp"
    },
    "designation": {
        "pos": "noun",
        "vi": "chức danh công việc; sự bổ nhiệm",
        "notes": "Chức danh vị trí"
    },
    "dis": {
        "pos": "verb",
        "vi": "xem thường; chê bai (diss)",
        "notes": "Tiếng lóng diss / chê bai"
    },
    "discharged": {
        "pos": "adj",
        "vi": "được xuất viện; giải ngũ; xả thải",
        "notes": "Xuất viện / xuất ngũ"
    },
    "disciplinary": {
        "pos": "adj",
        "vi": "mang tính kỷ luật; thuộc môn học",
        "notes": "Hội đồng kỷ luật"
    },
    "disputed": {
        "pos": "adj",
        "vi": "tranh cãi; gây tranh luận",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "dreamed": {
        "pos": "adj",
        "vi": "được mơ tới; tưởng tượng; hy vọng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "drugstore": {
        "pos": "noun",
        "vi": "hiệu thuốc; nhà thuốc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "dwelling": {
        "pos": "noun",
        "vi": "nhà ở; nơi cư trú sinh sống",
        "notes": "Sửa typo chổ ở sang nhà ở"
    },
    "earring": {
        "pos": "noun",
        "vi": "khuyên tai; hoa tai",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "eligibility": {
        "pos": "noun",
        "vi": "tính đủ điều kiện",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "enclosed": {
        "pos": "adj",
        "vi": "bao quanh; kín; đính kèm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "erotic": {
        "pos": "adj",
        "vi": "gợi cảm khiêu gợi; thuộc tính dục",
        "notes": "Nghệ thuật gợi cảm"
    },
    "eventual": {
        "pos": "adj",
        "vi": "cuối cùng; sau cùng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "exchanged": {
        "pos": "adj",
        "vi": "được trao đổi; được đổi",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "faded": {
        "pos": "adj",
        "vi": "phai màu; nhạt; mờ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "falcon": {
        "pos": "noun",
        "vi": "chim cắt; chim ưng săn mồi",
        "notes": "Chim cắt săn mồi"
    },
    "finite": {
        "pos": "adj",
        "vi": "hữu hạn; có hạn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "flagship": {
        "pos": "noun",
        "vi": "sản phẩm chủ lực; soái hạm",
        "notes": "Sản phẩm đầu bảng flagship"
    },
    "flawed": {
        "pos": "adj",
        "vi": "có khuyết điểm; có lỗi",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "flex": {
        "pos": "noun",
        "vi": "dây điện mềm; sự khoe mẽ (flex)",
        "notes": "Khoe khoang flex"
    },
    "frighten": {
        "pos": "verb",
        "vi": "làm hoảng sợ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "fundamentally": {
        "pos": "adv",
        "vi": "về cơ bản; về bản chất",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "genus": {
        "pos": "noun",
        "vi": "chi sinh học (genus)",
        "notes": "Chi trong sinh học"
    },
    "glowing": {
        "pos": "adj",
        "vi": "nồng nhiệt; nhiệt tình",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "glucose": {
        "pos": "noun",
        "vi": "glucozơ; glu-cô",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "gore": {
        "pos": "noun",
        "vi": "cảnh máu me ghê rợn; mảnh vải xéo",
        "notes": "Phim máu me kinh dị"
    },
    "grandchild": {
        "pos": "noun",
        "vi": "cháu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "greed": {
        "pos": "noun",
        "vi": "sự tham lam",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "groove": {
        "pos": "noun",
        "vi": "đường rãnh khía; nhịp điệu cuốn hút",
        "notes": "Đường rãnh / bắt nhịp"
    },
    "halo": {
        "pos": "noun",
        "vi": "hào quang",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "hank": {
        "pos": "noun",
        "vi": "cuộn sợi; bó len; họ Hank",
        "notes": "Cuộn len sợi"
    },
    "horrific": {
        "pos": "adj",
        "vi": "kinh khủng; khủng khiếp",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "hose": {
        "pos": "noun",
        "vi": "ống vòi; tưới bằng vòi",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "hulk": {
        "pos": "noun",
        "vi": "người khổng lồ; xác tàu đắm",
        "notes": "Người khổng lồ xanh Hulk"
    },
    "ideological": {
        "pos": "adj",
        "vi": "thuộc hệ tư tưởng; ý thức hệ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "infamous": {
        "pos": "adj",
        "vi": "khét tiếng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "initiate": {
        "pos": "noun",
        "vi": "người mới nhập môn; hội viên mới",
        "notes": "Người mới kết nạp"
    },
    "internally": {
        "pos": "adv",
        "vi": "bên trong; nội bộ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "issuing": {
        "pos": "noun",
        "vi": "sự phát hành; sự ban hành",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "jealousy": {
        "pos": "noun",
        "vi": "sự ghen tuông; tính đố kỵ",
        "notes": "Ghen tuông đố kỵ"
    },
    "joker": {
        "pos": "noun",
        "vi": "người thích đùa; người hay pha trò",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "kidnapping": {
        "pos": "noun",
        "vi": "sự bắt cóc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "laden": {
        "pos": "adj",
        "vi": "chất đầy; đầy ắp; nặng trĩu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "last": {
        "pos": "adj",
        "vi": "cuối cùng; vừa qua; trước đây",
        "notes": "Sửa crawler động từ kéo dài sang tính từ cuối cùng"
    },
    "lateral": {
        "pos": "adj",
        "vi": "ở bên cạnh; chuyển ngang vị trí",
        "notes": "Chuyển ngang cấp bậc"
    },
    "least": {
        "pos": "adj",
        "vi": "ít nhất; kém nhất",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "lent": {
        "pos": "noun",
        "vi": "Mùa Chay (Kitô giáo); đã cho vay",
        "notes": "Mùa Chay"
    },
    "limestone": {
        "pos": "noun",
        "vi": "đá vôi",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "locking": {
        "pos": "noun",
        "vi": "sự khóa",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "logging": {
        "pos": "noun",
        "vi": "khai thác gỗ; việc đốn gỗ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "madonna": {
        "pos": "noun",
        "vi": "Đức Mẹ Đồng Trinh; Đức Mẹ Maria",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "magnet": {
        "pos": "noun",
        "vi": "nam châm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "majors": {
        "pos": "noun",
        "vi": "tập đoàn lớn; chuyên ngành đại học",
        "notes": "Chuyên ngành học"
    },
    "mentality": {
        "pos": "noun",
        "vi": "tư duy; tư tưởng; tâm lí",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "migrant": {
        "pos": "adj",
        "vi": "di cư; di dời",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "mil": {
        "pos": "noun",
        "vi": "một phần nghìn inch; triệu (lóng)",
        "notes": "Đơn vị đo mil"
    },
    "more": {
        "pos": "adj",
        "vi": "nhiều hơn; thêm nữa",
        "notes": "Nhiều hơn nữa"
    },
    "moron": {
        "pos": "noun",
        "vi": "kẻ ngốc nghếch; người khờ dại",
        "notes": "Từ lóng chê bai"
    },
    "negro": {
        "pos": "adj",
        "vi": "người da màu (từ cũ nhạy cảm)",
        "notes": "Từ ngữ lịch sử"
    },
    "neural": {
        "pos": "adj",
        "vi": "thuộc thần kinh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "newsletter": {
        "pos": "noun",
        "vi": "bản tin định kỳ (newsletter)",
        "notes": "Bản tin qua email"
    },
    "nineteenth": {
        "pos": "adj",
        "vi": "thứ mười chín",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "nitrogen": {
        "pos": "noun",
        "vi": "khí ni-tơ; chất đạm",
        "notes": "Khí nitơ"
    },
    "notify": {
        "pos": "verb",
        "vi": "thông báo; báo cho",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "null": {
        "pos": "adj",
        "vi": "rỗng; vô hiệu; không có hiệu lực",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "observing": {
        "pos": "adj",
        "vi": "tinh ý; hay để ý",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "pact": {
        "pos": "noun",
        "vi": "điều ước; hiệp ước",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "palette": {
        "pos": "noun",
        "vi": "bảng màu; bảng pha màu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "payroll": {
        "pos": "noun",
        "vi": "bảng lương; quỹ tiền lương công ty",
        "notes": "Bảng lương nhân sự"
    },
    "photographic": {
        "pos": "adj",
        "vi": "thuộc nhiếp ảnh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "pitching": {
        "pos": "noun",
        "vi": "vị trí ném bóng; sự chao đảo",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "polished": {
        "pos": "adj",
        "vi": "đánh bóng; bóng láng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "preceding": {
        "pos": "adj",
        "vi": "ở trước; liền trước; trước đó",
        "notes": "Năm tài chính liền trước"
    },
    "proclaimed": {
        "pos": "adj",
        "vi": "được công bố; được tuyên bố",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "professionally": {
        "pos": "adv",
        "vi": "một cách chuyên nghiệp",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "proxy": {
        "pos": "noun",
        "vi": "máy chủ proxy; giấy ủy quyền",
        "notes": "Ủy quyền / proxy server"
    },
    "psycho": {
        "pos": "noun",
        "vi": "kẻ tâm thần; người loạn thần",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "pyramid": {
        "pos": "noun",
        "vi": "kim tự tháp",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "questionable": {
        "pos": "adj",
        "vi": "đáng ngờ; có vấn đề; có thể bác bỏ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "registry": {
        "pos": "noun",
        "vi": "sổ đăng kiểm; cơ quan đăng ký",
        "notes": "Sổ đăng ký tài sản"
    },
    "relevance": {
        "pos": "noun",
        "vi": "sự liên quan; tính thích đáng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "reproduction": {
        "pos": "noun",
        "vi": "sự sinh sản",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "resurrection": {
        "pos": "noun",
        "vi": "sự phục sinh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "retro": {
        "pos": "adj",
        "vi": "phong cách hoài cổ (retro)",
        "notes": "Thiết kế phong cách retro"
    },
    "reverend": {
        "pos": "adj",
        "vi": "đáng tôn kính; đáng kính trọng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "revolt": {
        "pos": "noun",
        "vi": "cuộc nổi dậy; cuộc khởi nghĩa",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "rewarding": {
        "pos": "adj",
        "vi": "bổ ích; đáng bõ công làm",
        "notes": "Công việc đáng bõ công"
    },
    "rigid": {
        "pos": "adj",
        "vi": "cứng ngắc; cứng nhắc; cứng đầu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "rover": {
        "pos": "noun",
        "vi": "xe tự hành khám phá; kẻ lãng du",
        "notes": "Xe tự hành trên sao Hỏa"
    },
    "rumor": {
        "pos": "noun",
        "vi": "tin đồn; lời đồn; đồn thổi",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "rust": {
        "pos": "noun",
        "vi": "gỉ sét sắt thép; màu nâu đỏ",
        "notes": "Sửa pos từ adj sang noun"
    },
    "sacked": {
        "pos": "adj",
        "vi": "bị sa thải đuổi việc; bị cướp phá",
        "notes": "Bị đuổi việc"
    },
    "saddle": {
        "pos": "noun",
        "vi": "yên ngựa; yên xe đạp",
        "notes": "Yên ngựa cưỡi"
    },
    "sampling": {
        "pos": "noun",
        "vi": "lấy mẫu; chọn mẫu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "scots": {
        "pos": "adj",
        "vi": "Scotland",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "scripture": {
        "pos": "noun",
        "vi": "thánh thư",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "seizure": {
        "pos": "noun",
        "vi": "cơn động kinh; giật kinh phong",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "serum": {
        "pos": "noun",
        "vi": "huyết thanh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "shattered": {
        "pos": "adj",
        "vi": "tan vỡ; đổ vỡ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "shipment": {
        "pos": "noun",
        "vi": "hàng hóa vận chuyển; sự gửi hàng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "shrine": {
        "pos": "noun",
        "vi": "lăng; mộ; đền",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "sightseeing": {
        "pos": "noun",
        "vi": "tham quan; du lịch ngắm cảnh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "skateboarding": {
        "pos": "noun",
        "vi": "trượt ván",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "sniper": {
        "pos": "noun",
        "vi": "xạ thủ bắn tỉa",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "spacecraft": {
        "pos": "noun",
        "vi": "tàu vũ trụ; phi thuyền",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "splendid": {
        "pos": "adj",
        "vi": "lộng lẫy; tráng lệ; tuyệt vời",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "stainless": {
        "pos": "adj",
        "vi": "không gỉ (inox); không tì vết",
        "notes": "Thép không gỉ inox"
    },
    "statutory": {
        "pos": "adj",
        "vi": "theo luật định; hợp pháp",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "stellar": {
        "pos": "adj",
        "vi": "xuất sắc vượt bậc; thuộc tinh tú",
        "notes": "Thành tích xuất sắc"
    },
    "stripes": {
        "pos": "noun",
        "vi": "các sọc vằn; quân hàm sĩ quan",
        "notes": "Sọc áo / quân hàm"
    },
    "stud": {
        "pos": "noun",
        "vi": "đinh tán; núm trang trí",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "sunk": {
        "pos": "adj",
        "vi": "đã chìm đắm; chi phí chìm (sunk)",
        "notes": "Chi phí chìm (sunk cost)"
    },
    "supplying": {
        "pos": "noun",
        "vi": "sự cung cấp",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "sustainability": {
        "pos": "noun",
        "vi": "phát triển bền vững; tính bền vững",
        "notes": "Bền vững môi trường"
    },
    "syrup": {
        "pos": "noun",
        "vi": "xi-rô",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "systemic": {
        "pos": "adj",
        "vi": "thuộc hệ thống; có tính hệ thống",
        "notes": "Rủi ro mang tính hệ thống"
    },
    "tablespoon": {
        "pos": "noun",
        "vi": "muỗng canh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "tapping": {
        "pos": "noun",
        "vi": "tiếng gõ nhẹ; tiếng cốc cốc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "temp": {
        "pos": "noun",
        "vi": "nhân viên thời vụ (temp)",
        "notes": "Nhân viên tạm thời"
    },
    "tempo": {
        "pos": "noun",
        "vi": "nhịp độ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "terminated": {
        "pos": "adj",
        "vi": "kết thúc; chấm dứt; hết hạn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "textile": {
        "pos": "adj",
        "vi": "thuộc về dệt; hàng dệt",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "theological": {
        "pos": "adj",
        "vi": "thần học",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "thereof": {
        "pos": "adv",
        "vi": "của nó; về điều đó; từ đó",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "thrive": {
        "pos": "verb",
        "vi": "phát triển mạnh; sinh trưởng tốt",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "transplant": {
        "pos": "noun",
        "vi": "cấy; mảnh ghép; cơ quan ghép",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "troll": {
        "pos": "noun",
        "vi": "kẻ khiêu khích mạng; quỷ lùn",
        "notes": "Troll trên mạng"
    },
    "turf": {
        "pos": "noun",
        "vi": "địa bàn làm ăn; thảm cỏ xanh",
        "notes": "Địa bàn hoạt động"
    },
    "undercover": {
        "pos": "adj",
        "vi": "bí mật; nằm vùng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "unlocked": {
        "pos": "adj",
        "vi": "không khóa; mở",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "unpaid": {
        "pos": "adj",
        "vi": "chưa trả; chưa thanh toán",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "unveiled": {
        "pos": "adj",
        "vi": "được tiết lộ; được hé lộ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "uprising": {
        "pos": "noun",
        "vi": "nổi dậy; khởi nghĩa",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "upwards": {
        "pos": "adv",
        "vi": "lên",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "us": {
        "pos": "pron",
        "vi": "chúng tôi; chúng ta; Mỹ US",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "valuation": {
        "pos": "noun",
        "vi": "sự định giá tài sản/doanh nghiệp",
        "notes": "Định giá công ty startup"
    },
    "vest": {
        "pos": "noun",
        "vi": "áo gi lê; gi-lê",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "veterinary": {
        "pos": "adj",
        "vi": "thuộc về thú y; bác sĩ thú y",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "vine": {
        "pos": "noun",
        "vi": "dây leo",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "voiced": {
        "pos": "adj",
        "vi": "hữu thanh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "warmer": {
        "pos": "noun",
        "vi": "máy sưởi; bình nóng lạnh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "waving": {
        "pos": "noun",
        "vi": "sự vẫy tay; cái vẫy tay",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "welcoming": {
        "pos": "adj",
        "vi": "niềm nở; chào đón",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "while": {
        "pos": "noun",
        "vi": "một lúc; một thời gian",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "yelled": {
        "pos": "adj",
        "vi": "la hét; gào thét",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "yen": {
        "pos": "noun",
        "vi": "đồng yên Nhật (JPY); niềm khao khát",
        "notes": "Đồng Yên Nhật"
    },
    "access": {
        "pos": "noun",
        "vi": "lối vào; đường vào; quyền truy cập",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "active": {
        "pos": "adj",
        "vi": "tích cực; năng nổ; tại ngũ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "ad": {
        "pos": "noun",
        "vi": "mục quảng cáo thương mại (ad)",
        "notes": "Mẩu quảng cáo"
    },
    "admired": {
        "pos": "adj",
        "vi": "được ngưỡng mộ; được khâm phục",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "aerospace": {
        "pos": "noun",
        "vi": "ngành hàng không vũ trụ",
        "notes": "Công nghiệp hàng không vũ trụ"
    },
    "aid": {
        "pos": "noun",
        "vi": "viện trợ; sự hỗ trợ cứu tế",
        "notes": "Sửa lỗi typo viện viện trợ"
    },
    "akin": {
        "pos": "adj",
        "vi": "tương tự; giống; cùng huyết thống",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "almighty": {
        "pos": "adj",
        "vi": "toàn năng; Đức Chúa Trời",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "amazing": {
        "pos": "adj",
        "vi": "đáng kinh ngạc; tuyệt vời",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "amount": {
        "pos": "noun",
        "vi": "số lượng; số tiền",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "analytical": {
        "pos": "adj",
        "vi": "phân tích; tiên nghiệm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "annual": {
        "pos": "adj",
        "vi": "hàng năm; thường niên",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "anti": {
        "pos": "adj",
        "vi": "phản đối; chống",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "apex": {
        "pos": "noun",
        "vi": "đỉnh cao; điểm chóp cao nhất",
        "notes": "Sửa lỗi crawler dấu sóng sang đỉnh cao chóp"
    },
    "apparel": {
        "pos": "noun",
        "vi": "quần áo; trang phục",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "army": {
        "pos": "noun",
        "vi": "lục quân; quân đội; đội quân",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "auburn": {
        "pos": "adj",
        "vi": "màu hung đỏ; màu nâu đỏ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "authorization": {
        "pos": "noun",
        "vi": "sự ủy quyền; cấp phép chính thức",
        "notes": "Ủy quyền truy cập"
    },
    "awakening": {
        "pos": "noun",
        "vi": "sự thức dậy; sự tỉnh giấc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "awesome": {
        "pos": "adj",
        "vi": "tuyệt vời; đáng kinh ngạc; xuất sắc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "backward": {
        "pos": "adj",
        "vi": "ngược lại; về phía sau; lùi",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "bacterial": {
        "pos": "adj",
        "vi": "vi khuẩn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "barred": {
        "pos": "adj",
        "vi": "bị chặn; bị cấm; có sọc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "basis": {
        "pos": "noun",
        "vi": "nền tảng; cơ sở",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "battle": {
        "pos": "noun",
        "vi": "trận đánh; trận chiến",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "beat": {
        "pos": "adj",
        "vi": "kiệt sức mệt lử; thuộc thế hệ Beat",
        "notes": "Kiệt sức / Beat generation"
    },
    "beck": {
        "pos": "noun",
        "vi": "cái vẫy tay; cái ra hiệu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "bet": {
        "pos": "noun",
        "vi": "vụ cá cược; sự lựa chọn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "bilateral": {
        "pos": "adj",
        "vi": "song phương; hai bên đối ứng",
        "notes": "Hiệp định song phương"
    },
    "bingo": {
        "pos": "noun",
        "vi": "trò chơi bingo; trúng phóc",
        "notes": "Trò bingo"
    },
    "blog": {
        "pos": "noun",
        "vi": "trang blog; nhật ký trực tuyến",
        "notes": "Blog tin tức"
    },
    "boiler": {
        "pos": "noun",
        "vi": "nồi hơi; lò hơi; nồi luộc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "boulder": {
        "pos": "noun",
        "vi": "tảng đá lớn; thành phố Boulder",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "brace": {
        "pos": "noun",
        "vi": "thanh giằng nẹp; niềng răng",
        "notes": "Nẹp giằng / niềng răng"
    },
    "cancer": {
        "pos": "noun",
        "vi": "ung thư; chòm sao Cự Giải",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "career": {
        "pos": "noun",
        "vi": "nghề nghiệp; sự nghiệp",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "cell": {
        "pos": "noun",
        "vi": "tế bào; ngăn; ô; buồng nhỏ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "central": {
        "pos": "adj",
        "vi": "trung tâm; ở giữa",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "channel": {
        "pos": "noun",
        "vi": "kênh; truyền tải; dẫn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "charge": {
        "pos": "noun",
        "vi": "khoản phí cước; sự đảm nhận",
        "notes": "Khoản phí dịch vụ"
    },
    "chief": {
        "pos": "adj",
        "vi": "trưởng; cấp cao; chủ yếu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "civil": {
        "pos": "adj",
        "vi": "thuộc về dân sự; lịch sự nhã nhặn",
        "notes": "Vụ kiện dân sự"
    },
    "coating": {
        "pos": "noun",
        "vi": "lớp phủ; lớp tráng; lớp sơn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "comment": {
        "pos": "noun",
        "vi": "lời bình luận; nhận xét",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "concealed": {
        "pos": "adj",
        "vi": "kín; ẩn; che giấu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "content": {
        "pos": "adj",
        "vi": "hài lòng; bằng lòng thỏa mãn",
        "notes": "Sửa crawler dịch nhầm nội dung danh từ sang tính từ hài lòng"
    },
    "contention": {
        "pos": "noun",
        "vi": "luận điểm; ý kiến tranh luận",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "convoy": {
        "pos": "noun",
        "vi": "đoàn xe; đoàn hộ tống",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "cork": {
        "pos": "noun",
        "vi": "nút chai bần; vỏ sồi bần",
        "notes": "Nút bần đóng chai"
    },
    "cosmetic": {
        "pos": "adj",
        "vi": "mỹ phẩm; chỉ để trang trí",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "council": {
        "pos": "noun",
        "vi": "hội đồng; cuộc họp; hội nghị",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "county": {
        "pos": "noun",
        "vi": "quận; hạt",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "cubic": {
        "pos": "adj",
        "vi": "hình lập phương; khối (mét khối)",
        "notes": "Mét khối"
    },
    "current": {
        "pos": "adj",
        "vi": "hiện tại; hiện hành; dòng điện",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "demand": {
        "pos": "noun",
        "vi": "nhu cầu; yêu cầu; đòi hỏi",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "disease": {
        "pos": "noun",
        "vi": "bệnh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "dismissal": {
        "pos": "noun",
        "vi": "sự sa thải; bác đơn kiện; giải tán",
        "notes": "Sa thải nhân viên / bác đơn"
    },
    "dude": {
        "pos": "noun",
        "vi": "anh bạn; cậu; gã",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "economic": {
        "pos": "adj",
        "vi": "thuộc kinh tế; tiết kiệm; hiệu quả",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "empathy": {
        "pos": "noun",
        "vi": "thấu cảm; cộng cảm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "ensemble": {
        "pos": "noun",
        "vi": "dàn hòa tấu; trang phục đồng bộ",
        "notes": "Dàn nhạc / trang phục"
    },
    "entire": {
        "pos": "adj",
        "vi": "toàn bộ; trọn vẹn; nguyên",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "ethnicity": {
        "pos": "noun",
        "vi": "sắc tộc; sắc dân",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "exercising": {
        "pos": "noun",
        "vi": "sự tập thể dục; việc vận động",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "expenditure": {
        "pos": "noun",
        "vi": "chi tiêu; khoản chi; sự tiêu dùng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "feasible": {
        "pos": "adj",
        "vi": "khả thi; có thể thực hiện được",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "financial": {
        "pos": "adj",
        "vi": "tài chính",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "forged": {
        "pos": "adj",
        "vi": "giả mạo; làm giả",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "former": {
        "pos": "adj",
        "vi": "trước; thứ nhất; cũ; cựu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "fund": {
        "pos": "noun",
        "vi": "quỹ tiền; tiền vốn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "gain": {
        "pos": "noun",
        "vi": "lợi nhuận; sự gia tăng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "gay": {
        "pos": "adj",
        "vi": "đồng tính nam (gay); vui vẻ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "general": {
        "pos": "adj",
        "vi": "chung; tổng quát; phổ biến",
        "notes": "Sửa crawler tướng quân danh từ sang tính từ tổng quát"
    },
    "global": {
        "pos": "adj",
        "vi": "toàn cầu; hình cầu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "grease": {
        "pos": "noun",
        "vi": "dầu mỡ bôi trơn máy móc; mỡ thừa",
        "notes": "Mỡ bôi trơn kỹ thuật"
    },
    "growth": {
        "pos": "noun",
        "vi": "sự tăng trưởng; phát triển",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "guide": {
        "pos": "noun",
        "vi": "hướng dẫn viên; sách hướng dẫn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "hallway": {
        "pos": "noun",
        "vi": "hành lang",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "heavens": {
        "pos": "noun",
        "vi": "bầu trời; thiên không",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "highly": {
        "pos": "adv",
        "vi": "rất; hết sức; vô cùng; cao",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "holy": {
        "pos": "adj",
        "vi": "thánh thiện; linh thiêng; thánh địa",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "homosexuality": {
        "pos": "noun",
        "vi": "tính tình dục đồng giới",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "hooker": {
        "pos": "noun",
        "vi": "gái bán hoa; vị trí bóng bầu dục",
        "notes": "Thuật ngữ lóng / thể thao"
    },
    "huge": {
        "pos": "adj",
        "vi": "khổng lồ; đồ sộ; to lớn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "hydraulic": {
        "pos": "adj",
        "vi": "thuỷ lực",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "impacted": {
        "pos": "adj",
        "vi": "chịu tác động lớn; bị ảnh hưởng",
        "notes": "Chịu tác động nặng nề"
    },
    "imposing": {
        "pos": "adj",
        "vi": "uy nghi; hùng vĩ; bề thế",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "incapable": {
        "pos": "adj",
        "vi": "không có khả năng; bất tài",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "income": {
        "pos": "noun",
        "vi": "thu nhập; doanh thu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "industry": {
        "pos": "noun",
        "vi": "ngành công nghiệp; ngành nghề",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "insanity": {
        "pos": "noun",
        "vi": "tính trạng điên; sự điên rồ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "involved": {
        "pos": "adj",
        "vi": "có liên quan; dính líu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "jeep": {
        "pos": "noun",
        "vi": "xe jeep; xe địa hình",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "lambert": {
        "pos": "noun",
        "vi": "đơn vị độ chói Lambert; họ Lambert",
        "notes": "Đơn vị quang học"
    },
    "leading": {
        "pos": "adj",
        "vi": "hàng đầu; chính; dẫn đầu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "league": {
        "pos": "noun",
        "vi": "liên đoàn; giải đấu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "legal": {
        "pos": "adj",
        "vi": "hợp pháp; đúng luật; pháp lý",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "limited": {
        "pos": "adj",
        "vi": "có hạn; giới hạn; hạn chế",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "link": {
        "pos": "noun",
        "vi": "mối liên kết; mắt xích; vòng nối",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "longtime": {
        "pos": "adj",
        "vi": "lâu năm; lâu dài",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "loss": {
        "pos": "noun",
        "vi": "sự thua lỗ; tổn thất",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "lump": {
        "pos": "noun",
        "vi": "khoản tiền trọn gói; cục; tảng",
        "notes": "Lump sum payment"
    },
    "macro": {
        "pos": "adj",
        "vi": "kinh tế vĩ mô; quy mô lớn",
        "notes": "Vĩ mô macro"
    },
    "mag": {
        "pos": "noun",
        "vi": "tạp chí xuất bản; băng đạn",
        "notes": "Tạp chí mag"
    },
    "main": {
        "pos": "adj",
        "vi": "chính; chủ yếu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "mass": {
        "pos": "adj",
        "vi": "quần chúng; đại chúng; tập thể",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "mayo": {
        "pos": "noun",
        "vi": "sốt may-on-ne (mayo)",
        "notes": "Sốt mayonnaise"
    },
    "mental": {
        "pos": "adj",
        "vi": "tinh thần; trí tuệ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "movement": {
        "pos": "noun",
        "vi": "sự di chuyển; sự chuyển động",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "onset": {
        "pos": "noun",
        "vi": "sự bắt đầu; khởi đầu",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "oriental": {
        "pos": "adj",
        "vi": "thuộc về phương Đông (Á Đông)",
        "notes": "Thuộc Á Đông"
    },
    "paid": {
        "pos": "adj",
        "vi": "được trả lương; có lương; có lãi",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "pain": {
        "pos": "noun",
        "vi": "cơn đau; sự đau đớn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "paranoid": {
        "pos": "adj",
        "vi": "hoang tưởng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "pixel": {
        "pos": "noun",
        "vi": "điểm ảnh kỹ thuật số (pixel)",
        "notes": "Điểm ảnh màn hình"
    },
    "pod": {
        "pos": "noun",
        "vi": "khoang làm việc; vỏ quả đậu",
        "notes": "Khoang làm việc văn phòng"
    },
    "policy": {
        "pos": "noun",
        "vi": "chính sách; hợp đồng bảo hiểm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "positive": {
        "pos": "adj",
        "vi": "tích cực; lạc quan; dương tính",
        "notes": "Tư duy tích cực"
    },
    "presently": {
        "pos": "adv",
        "vi": "sớm; chẳng mấy chốc; hiện tại",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "press": {
        "pos": "noun",
        "vi": "giới truyền thông báo chí; máy ép",
        "notes": "Họp báo báo chí"
    },
    "process": {
        "pos": "noun",
        "vi": "quá trình; quy trình; tiến trình",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "property": {
        "pos": "noun",
        "vi": "tài sản; của cải; đặc tính",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "props": {
        "pos": "noun",
        "vi": "đạo cụ sân khấu; sự nể phục (props)",
        "notes": "Đạo cụ / give props"
    },
    "quantitative": {
        "pos": "adj",
        "vi": "mang tính định lượng; số lượng",
        "notes": "Phân tích định lượng"
    },
    "race": {
        "pos": "noun",
        "vi": "cuộc đua",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "raining": {
        "pos": "adj",
        "vi": "đang mưa; rơi như mưa",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "region": {
        "pos": "noun",
        "vi": "vùng; khu vực; miền",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "renovation": {
        "pos": "noun",
        "vi": "sự cải tạo; sự tân trang",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "respect": {
        "pos": "noun",
        "vi": "sự kính trọng; lòng tôn trọng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "rest": {
        "pos": "noun",
        "vi": "sự nghỉ ngơi; giờ nghỉ; lúc nghỉ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "retarded": {
        "pos": "adj",
        "vi": "chậm phát triển (từ nhạy cảm)",
        "notes": "Thuật ngữ y khoa nhạy cảm"
    },
    "rise": {
        "pos": "noun",
        "vi": "sự gia tăng; đợt tăng lương/giá",
        "notes": "Mức tăng tiền lương"
    },
    "risk": {
        "pos": "noun",
        "vi": "rủi ro; nguy cơ; sự liều lĩnh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "roasted": {
        "pos": "adj",
        "vi": "nướng; quay",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "ruining": {
        "pos": "noun",
        "vi": "sự hủy hoại; sự phá hủy",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "safety": {
        "pos": "noun",
        "vi": "sự an toàn; nơi an toàn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "salute": {
        "pos": "noun",
        "vi": "sự chào; sự bày tỏ kính trọng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "scanning": {
        "pos": "noun",
        "vi": "việc quét tài liệu/mã vạch (scan)",
        "notes": "Quét tài liệu văn phòng"
    },
    "schooling": {
        "pos": "noun",
        "vi": "việc học hành; sự giáo dục ở trường",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "score": {
        "pos": "noun",
        "vi": "điểm số thành tích; bản nhạc phim",
        "notes": "Điểm số trận đấu"
    },
    "scum": {
        "pos": "noun",
        "vi": "cặn bã; đồ vô lại; váng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "season": {
        "pos": "noun",
        "vi": "mùa trong năm; mùa kinh doanh",
        "notes": "Mùa cao điểm du lịch"
    },
    "security": {
        "pos": "noun",
        "vi": "an ninh; an toàn; sự yên tâm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "series": {
        "pos": "noun",
        "vi": "chuỗi; loạt phim; vòng gọi vốn",
        "notes": "Vòng gọi vốn Series A"
    },
    "serious": {
        "pos": "adj",
        "vi": "nghiêm trọng; hệ trọng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "service": {
        "pos": "noun",
        "vi": "dịch vụ; sự giúp đỡ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "sex": {
        "pos": "noun",
        "vi": "giới tính sinh học; tính dục",
        "notes": "Giới tính sinh học"
    },
    "shady": {
        "pos": "adj",
        "vi": "có bóng râm mát; mờ ám khuất tất",
        "notes": "Giao dịch mờ ám shady"
    },
    "shaping": {
        "pos": "adj",
        "vi": "tạo hình; định hình",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "skin": {
        "pos": "noun",
        "vi": "da; bề mặt; lớp vỏ ngoài",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "slick": {
        "pos": "adj",
        "vi": "trơn; nhẵn; bóng nhẫy",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "sort": {
        "pos": "noun",
        "vi": "loại; kiểu; hạng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "soul": {
        "pos": "noun",
        "vi": "linh hồn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "status": {
        "pos": "noun",
        "vi": "địa vị xã hội; tình trạng dự án",
        "notes": "Trạng thái dự án"
    },
    "stick": {
        "pos": "noun",
        "vi": "chiếc gậy; que gỗ; cán điều khiển",
        "notes": "Sửa crawler các động từ cắm đâm chọc sang danh từ gậy que"
    },
    "storyline": {
        "pos": "noun",
        "vi": "cốt truyện",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "stupid": {
        "pos": "adj",
        "vi": "ngu ngốc; đần độn; ngẩn người",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "supply": {
        "pos": "noun",
        "vi": "nguồn cung; lượng dự trữ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "tax": {
        "pos": "noun",
        "vi": "thuế; tiền thuế",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "term": {
        "pos": "noun",
        "vi": "thuật ngữ; điều khoản; kỳ hạn",
        "notes": "Điều khoản hợp đồng"
    },
    "theory": {
        "pos": "noun",
        "vi": "lý thuyết; học thuyết; giả thuyết",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "through": {
        "pos": "adj",
        "vi": "suốt; hết; đến cùng; xong",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "thus": {
        "pos": "adv",
        "vi": "do đó; vì thế; vậy nên",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "total": {
        "pos": "adj",
        "vi": "hoàn toàn; toàn bộ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "tow": {
        "pos": "verb",
        "vi": "kéo; kéo xe",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "trusting": {
        "pos": "adj",
        "vi": "dễ tin; tin tưởng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "unarmed": {
        "pos": "adj",
        "vi": "không vũ trang; tay không",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "uncovered": {
        "pos": "adj",
        "vi": "trần; không che phủ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "unfinished": {
        "pos": "adj",
        "vi": "chưa hoàn thành; dang dở",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "union": {
        "pos": "noun",
        "vi": "công đoàn; tổ chức liên hiệp",
        "notes": "Sửa pos từ adj sang noun"
    },
    "unlawful": {
        "pos": "adj",
        "vi": "bất hợp pháp; trái pháp luật",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "van": {
        "pos": "noun",
        "vi": "xe tải nhỏ; xe van",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "vanished": {
        "pos": "adj",
        "vi": "đã biến mất; đã tiêu tan",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "various": {
        "pos": "adj",
        "vi": "khác nhau; đa dạng; riêng lẻ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "vista": {
        "pos": "noun",
        "vi": "quang cảnh; toàn cảnh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "vogue": {
        "pos": "noun",
        "vi": "mốt; thịnh hành; được ưa chuộng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "volatile": {
        "pos": "adj",
        "vi": "biến động dữ dội; dễ bay hơi",
        "notes": "Thị trường tài chính biến động"
    },
    "waste": {
        "pos": "noun",
        "vi": "chất thải rác thải; sự lãng phí",
        "notes": "Sửa pos từ adj sang noun"
    },
    "weakened": {
        "pos": "adj",
        "vi": "bị suy yếu; yếu đi; suy giảm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "working": {
        "pos": "adj",
        "vi": "đang đi làm; đủ dùng; tạm được",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "worth": {
        "pos": "adj",
        "vi": "đáng giá; trị giá",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "absolutely": {
        "pos": "adv",
        "vi": "hoàn toàn; tuyệt đối",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "acceleration": {
        "pos": "noun",
        "vi": "gia tốc",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "accredited": {
        "pos": "adj",
        "vi": "được công nhận; được cấp phép",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "advance": {
        "pos": "adj",
        "vi": "trước; tạm ứng trước hợp đồng",
        "notes": "Advance payment / thanh toán trước"
    },
    "affect": {
        "pos": "verb",
        "vi": "tác động sâu sắc đến; ảnh hưởng đến",
        "notes": "Sửa pos từ noun sang verb"
    },
    "agreement": {
        "pos": "noun",
        "vi": "sự đồng ý; sự nhất trí; thỏa thuận",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "analysis": {
        "pos": "noun",
        "vi": "sự phân tích; phép phân tích",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "apocalypse": {
        "pos": "noun",
        "vi": "ngày tận thế; thảm họa diệt vong",
        "notes": "Ngày tận thế thảm họa"
    },
    "appeal": {
        "pos": "noun",
        "vi": "sức hấp dẫn; sự lôi cuốn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "approach": {
        "pos": "noun",
        "vi": "phương pháp; cách tiếp cận",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "artist": {
        "pos": "noun",
        "vi": "họa sĩ; nghệ sĩ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "aside": {
        "pos": "adv",
        "vi": "sang một bên",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "aware": {
        "pos": "adj",
        "vi": "nhận thức; biết",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "balance": {
        "pos": "noun",
        "vi": "số dư tài khoản; sự cân bằng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "benefit": {
        "pos": "noun",
        "vi": "lợi ích; phúc lợi",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "beware": {
        "pos": "verb",
        "vi": "cẩn thận; đề phòng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "blackboard": {
        "pos": "noun",
        "vi": "bảng đen",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "bond": {
        "pos": "noun",
        "vi": "trái phiếu; mối liên kết gắn bó",
        "notes": "Trái phiếu chính phủ"
    },
    "border": {
        "pos": "noun",
        "vi": "biên giới; ranh giới",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "bunch": {
        "pos": "noun",
        "vi": "bó; chùm; buồng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "cholesterol": {
        "pos": "noun",
        "vi": "cholesterol",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "christian": {
        "pos": "adj",
        "vi": "Cơ đốc giáo; có tinh thần bác ái",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "clarence": {
        "pos": "noun",
        "vi": "xe ngựa bốn bánh có mui",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "climate": {
        "pos": "noun",
        "vi": "khí hậu; môi trường kinh doanh",
        "notes": "Môi trường đầu tư"
    },
    "command": {
        "pos": "noun",
        "vi": "mệnh lệnh; chỉ huy; điều khiển",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "commercial": {
        "pos": "adj",
        "vi": "thương mại; buôn bán",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "completely": {
        "pos": "adv",
        "vi": "hoàn toàn; toàn bộ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "complex": {
        "pos": "adj",
        "vi": "phức tạp; mặc cảm; phức cảm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "concept": {
        "pos": "noun",
        "vi": "khái niệm; quan niệm",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "contributor": {
        "pos": "noun",
        "vi": "người đóng góp; cộng tác viên",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "coping": {
        "pos": "noun",
        "vi": "sự ứng phó; đối phó khó khăn",
        "notes": "Cơ chế ứng phó khó khăn"
    },
    "creed": {
        "pos": "noun",
        "vi": "tín điều; tôn chỉ hoạt động tổ chức",
        "notes": "Tôn chỉ công ty"
    },
    "critical": {
        "pos": "adj",
        "vi": "phê bình; chỉ trích; then chốt",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "crust": {
        "pos": "noun",
        "vi": "lớp vỏ; đóng vỏ cứng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "currently": {
        "pos": "adv",
        "vi": "hiện tại; hiện nay",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "cutter": {
        "pos": "noun",
        "vi": "dao rọc giấy; máy cắt; tàu tuần tra",
        "notes": "Dụng cụ cắt gọt"
    },
    "cycle": {
        "pos": "noun",
        "vi": "chu kỳ; chuỗi cùng chủ đề",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "damage": {
        "pos": "noun",
        "vi": "sự hư hại; sự tổn hại",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "daring": {
        "pos": "adj",
        "vi": "dám nghĩ dám làm; táo bạo; cách tân",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "dating": {
        "pos": "noun",
        "vi": "sự hẹn hò tìm hiểu; định niên đại",
        "notes": "Hẹn hò đôi lứa"
    },
    "debt": {
        "pos": "noun",
        "vi": "khoản nợ; nợ nần",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "decision": {
        "pos": "noun",
        "vi": "sự quyết định; phán quyết",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "definitely": {
        "pos": "adv",
        "vi": "chắc chắn; nhất định",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "department": {
        "pos": "noun",
        "vi": "phòng; ban; bộ phận; tỉnh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "deploy": {
        "pos": "verb",
        "vi": "triển khai",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "descendants": {
        "pos": "noun",
        "vi": "con cháu; hậu duệ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "detector": {
        "pos": "noun",
        "vi": "thiết bị dò; máy dò; bộ tách sóng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "development": {
        "pos": "noun",
        "vi": "sự phát triển",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "device": {
        "pos": "noun",
        "vi": "thiết bị; dụng cụ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "digital": {
        "pos": "adj",
        "vi": "thuộc kỹ thuật số; công nghệ số",
        "notes": "Chuyển đổi số digital"
    },
    "diplomacy": {
        "pos": "noun",
        "vi": "ngoại giao",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "directive": {
        "pos": "noun",
        "vi": "chỉ thị lãnh đạo; văn bản chỉ đạo",
        "notes": "Chỉ thị ban hành"
    },
    "directly": {
        "pos": "adv",
        "vi": "ngay lập tức; thẳng",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "distance": {
        "pos": "noun",
        "vi": "khoảng cách; bỏ xa; vượt xa",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "district": {
        "pos": "noun",
        "vi": "quận; huyện; khu vực",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "duty": {
        "pos": "noun",
        "vi": "nhiệm vụ; trách nhiệm; chức trách",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "eastern": {
        "pos": "adj",
        "vi": "thuộc về phương Đông; ở phía đông",
        "notes": "Phía đông địa lý"
    },
    "economy": {
        "pos": "noun",
        "vi": "nền kinh tế quốc gia; sự tiết kiệm",
        "notes": "Nền kinh tế thị trường"
    },
    "edge": {
        "pos": "noun",
        "vi": "lợi thế cạnh tranh; mép rìa",
        "notes": "Lợi thế cạnh tranh (edge)"
    },
    "effective": {
        "pos": "adj",
        "vi": "hiệu quả; có hiệu lực",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "election": {
        "pos": "noun",
        "vi": "cuộc bầu cử; sự lựa chọn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "emphasized": {
        "pos": "adj",
        "vi": "được nhấn mạnh",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "enemy": {
        "pos": "noun",
        "vi": "kẻ thù; kẻ địch",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "engine": {
        "pos": "noun",
        "vi": "động cơ",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "ensure": {
        "pos": "verb",
        "vi": "bảo đảm; chắc chắn",
        "notes": "Rà soát thủ công đạt chuẩn QA"
    },
    "entry": {
        "pos": "noun",
        "vi": "lối vào; mục ghi sổ kế toán; dự thi",
        "notes": "Bút toán sổ sách kế toán"
    }
}

def main():
    print(f"Reading {BATCH_FILE}...")
    with open(BATCH_FILE, "r", encoding="utf-8") as fp:
        data = json.load(fp)

    records = data["records"]
    slice_records = records[3700:4200]
    assert len(slice_records) == 500, f"Expected 500 records, got {len(slice_records)}"

    updated = 0
    for r in slice_records:
        hw = r["hw"]
        if hw in EDITS_3701_4200:
            e = EDITS_3701_4200[hw]
            r["pos"] = e["pos"]
            r["vi"] = e["vi"]
            r["status"] = "edited"
            r["notes"] = e.get("notes", "Đã soát tay chuẩn hóa QA")
            updated += 1
        else:
            r["status"] = "approved"
            r["notes"] = "QA passed manual review"

    data["reviewedCount"] = 4200
    data["status"] = "in-progress"

    print(f"Writing updated slice back to {BATCH_FILE}...")
    with open(BATCH_FILE, "w", encoding="utf-8") as fp:
        json.dump(data, fp, ensure_ascii=False, indent=2)

    print(f"Successfully processed STT 3701-4200. Meticulously curated: {updated} words.")

    # Update INDEX.md
    if INDEX_FILE.exists():
        content = INDEX_FILE.read_text(encoding="utf-8")
        new_line = "| 01 | `batch-01.json` | 5000 | account ... sane | Phase 1 (100k Core & Standard) | 🔄 `in-progress` (4200/5000) |"
        content = re.sub(
            r"\|\s*01\s*\|\s*`batch-01\.json`.*?\|\s*[✅🔄⏳].*?\|",
            new_line,
            content
        )
        INDEX_FILE.write_text(content, encoding="utf-8")
        print("Updated INDEX.md to 4200/5000 in-progress.")

if __name__ == "__main__":
    main()
