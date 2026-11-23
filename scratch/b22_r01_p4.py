import json

raw_items = json.load(open("scratch/b22_r01_raw_p4.json"))

reviews = [
    # 00: funned
    {"pos": "verb", "ipa": "/fʌnd/", "vi": "đã đùa giỡn; đã trêu cợt"},
    # 01: livings
    {"pos": "noun", "ipa": "/ˈlɪvɪŋz/", "vi": "kế sinh nhai; bổng lộc giáo xứ"},
    # 02: agreed upon
    {"pos": "phrase", "ipa": "/əˈɡriːd əˈpɑːn/", "vi": "đã được thống nhất; đã đồng thuận"},
    # 03: back exercise
    {"pos": "phrase", "ipa": "/bæk ˈɛksərsaɪz/", "vi": "bài tập cơ lưng; động tác lưng"},
    # 04: bear away
    {"pos": "phrase", "ipa": "/bɛr əˈweɪ/", "vi": "đoạt giải; mang đi; đổi hướng buồm"},
    # 05: black tea
    {"pos": "phrase", "ipa": "/blæk tiː/", "vi": "trà đen; hồng trà"},
    # 06: blood heat
    {"pos": "phrase", "ipa": "/blʌd hiːt/", "vi": "thân nhiệt bình thường; độ ấm máu"},
    # 07: bottom round
    {"pos": "phrase", "ipa": "/ˈbɑːtəm raʊnd/", "vi": "thịt bắp đùi sau bò; nạc mông bò"},
    # 08: center spread
    {"pos": "phrase", "ipa": "/ˈsɛntər sprɛd/", "vi": "hai trang giữa báo; tranh giữa báo"},
    # 09: chair of state
    {"pos": "phrase", "ipa": "/tʃɛr əv steɪt/", "vi": "ngai vàng nghi lễ; ghế chủ tọa"},
    # 10: change of shape
    {"pos": "phrase", "ipa": "/tʃeɪndʒ əv ʃeɪp/", "vi": "sự biến dạng; đổi hình dạng"},
    # 11: change shape
    {"pos": "phrase", "ipa": "/tʃeɪndʒ ʃeɪp/", "vi": "thay đổi hình dạng; biến dạng"},
    # 12: cheap money
    {"pos": "phrase", "ipa": "/tʃiːp ˈmʌni/", "vi": "vốn vay lãi suất thấp; tín dụng rẻ"},
    # 13: china tree
    {"pos": "phrase", "ipa": "/ˈtʃaɪnə triː/", "vi": "cây xoan tàu; cây neem"},
    # 14: class fellow
    {"pos": "phrase", "ipa": "/klæs ˈfɛloʊ/", "vi": "bạn cùng lớp; bạn đồng khóa"},
    # 15: cold fish
    {"pos": "phrase", "ipa": "/koʊld fɪʃ/", "vi": "người lạnh lùng; kẻ vô cảm"},
    # 16: commercial credit
    {"pos": "phrase", "ipa": "/kəˈmɜːrʃl ˈkrɛdɪt/", "vi": "tín dụng thương mại"},
    # 17: commercial message
    {"pos": "phrase", "ipa": "/kəˈmɜːrʃl ˈmɛsɪdʒ/", "vi": "thông điệp quảng cáo thương mại"},
    # 18: county agent
    {"pos": "phrase", "ipa": "/ˈkaʊnti ˈeɪdʒənt/", "vi": "cán bộ khuyến nông quận hạt"},
    # 19: covered stand
    {"pos": "phrase", "ipa": "/ˈkʌvərd stænd/", "vi": "khán đài có mái che"},
    # 20: criminal court
    {"pos": "phrase", "ipa": "/ˈkrɪmɪnl kɔːrt/", "vi": "tòa án hình sự"},
    # 21: daughter cell
    {"pos": "phrase", "ipa": "/ˈdɔːtər sɛl/", "vi": "tế bào con trong phân bào"},
    # 22: dead on target
    {"pos": "phrase", "ipa": "/dɛd ɑːn ˈtɑːrɡɪt/", "vi": "hoàn toàn chính xác; trúng đích"},
    # 23: dead soul
    {"pos": "phrase", "ipa": "/dɛd soʊl/", "vi": "linh hồn người chết; nông nô chết"},
    # 24: democratic party
    {"pos": "phrase", "ipa": "/ˌdɛməˈkrætɪk ˈpɑːrti/", "vi": "Đảng Dân chủ"},
    # 25: east african
    {"pos": "phrase", "ipa": "/iːst ˈæfrɪkən/", "vi": "thuộc Đông Phi; người Đông Phi"},
    # 26: economic condition
    {"pos": "phrase", "ipa": "/ˌiːkəˈnɑːmɪk kənˈdɪʃn/", "vi": "tình hình kinh tế; thực trạng"},
    # 27: electric power
    {"pos": "phrase", "ipa": "/ɪˈlɛktrɪk ˈpaʊər/", "vi": "điện năng; công suất điện"},
    # 28: english civil war
    {"pos": "phrase", "ipa": "/ˈɪŋɡlɪʃ ˈsɪvl wɔːr/", "vi": "Nội chiến nước Anh"},
    # 29: executive council
    {"pos": "phrase", "ipa": "/ɪɡˈzɛkjətɪv ˈkaʊnsl/", "vi": "hội đồng điều hành; ban chấp hành"},
    # 30: eye disease
    {"pos": "phrase", "ipa": "/aɪ dɪˈziːz/", "vi": "bệnh về mắt; nhãn bệnh"},
    # 31: eye doctor
    {"pos": "phrase", "ipa": "/aɪ ˈdɑːktər/", "vi": "bác sĩ nhãn khoa; bác sĩ mắt"},
    # 32: factor out
    {"pos": "phrase", "ipa": "/ˈfæktər aʊt/", "vi": "đặt làm nhân tử chung; loại trừ"},
    # 33: farm girl
    {"pos": "phrase", "ipa": "/fɑːrm ɡɜːrl/", "vi": "cô gái nông thôn; nữ trang trại"},
    # 34: financial condition
    {"pos": "phrase", "ipa": "/faɪˈnænʃl kənˈdɪʃn/", "vi": "tình hình tài chính; thực trạng vốn"},
    # 35: fish ball
    {"pos": "phrase", "ipa": "/fɪʃ bɔːl/", "vi": "chả cá viên; cá viên chiên"},
    # 36: five iron
    {"pos": "phrase", "ipa": "/faɪv ˈaɪərn/", "vi": "gậy sắt số 5 trong đánh golf"},
    # 37: flow off
    {"pos": "phrase", "ipa": "/floʊ ɔːf/", "vi": "chảy thoát đi; tiêu thoát nước"},
    # 38: foot race
    {"pos": "phrase", "ipa": "/fʊt reɪs/", "vi": "cuộc thi chạy bộ; cuộc đua việt dã"},
    # 39: foreign mission
    {"pos": "phrase", "ipa": "/ˈfɔːrən ˈmɪʃn/", "vi": "phái bộ ngoại giao; đoàn truyền đạo"},
    # 40: fuel system
    {"pos": "phrase", "ipa": "/ˈfjuːəl ˈsɪstəm/", "vi": "hệ thống cung cấp nhiên liệu"},
    # 41: function word
    {"pos": "phrase", "ipa": "/ˈfʌŋkʃn wɜːrd/", "vi": "từ chức năng; hư từ"},
    # 42: general medicine
    {"pos": "phrase", "ipa": "/ˈdʒɛnrəl ˈmɛdsn/", "vi": "nội khoa tổng quát; y đa khoa"},
    # 43: grand island
    {"pos": "phrase", "ipa": "/ɡrænd ˈaɪlənd/", "vi": "thành phố Grand Island"},
    # 44: grand river
    {"pos": "phrase", "ipa": "/ɡrænd ˈrɪvər/", "vi": "sông Grand River"},
    # 45: hair cell
    {"pos": "phrase", "ipa": "/hɛr sɛl/", "vi": "tế bào lông thính giác tai trong"},
    # 46: high command
    {"pos": "phrase", "ipa": "/haɪ kəˈmænd/", "vi": "bộ chỉ huy tối cao; bộ tổng tư lệnh"},
    # 47: hot seat
    {"pos": "phrase", "ipa": "/hɑːt siːt/", "vi": "ghế nóng; ghế điện tử hình"},
    # 48: hotel manager
    {"pos": "phrase", "ipa": "/hoʊˈtɛl ˈmænɪdʒər/", "vi": "quản lý khách sạn; trưởng cơ sở"},
    # 49: housing development
    {"pos": "phrase", "ipa": "/ˈhaʊzɪŋ dɪˈvɛləpmənt/", "vi": "khu đô thị nhà ở; khu dân cư mới"},
    # 50: investment trust
    {"pos": "phrase", "ipa": "/ɪnˈvɛstmənt trʌst/", "vi": "quỹ đầu tư ủy thác; quỹ đầu tư"},
    # 51: job description
    {"pos": "phrase", "ipa": "/dʒɑːb dɪˈskrɪpʃn/", "vi": "bản mô tả công việc; bản JD"},
    # 52: kick start
    {"pos": "phrase", "ipa": "/kɪk stɑːrt/", "vi": "cần khởi động xe máy; sự hích đẩy"},
    # 53: labor market
    {"pos": "phrase", "ipa": "/ˈleɪbər ˈmɑːrkɪt/", "vi": "thị trường lao động; giới lao động"},
    # 54: laugh at
    {"pos": "phrase", "ipa": "/læf æt/", "vi": "cười nhạo; chế giễu; xem thường"},
    # 55: least common multiple
    {"pos": "phrase", "ipa": "/liːst ˈkɑːmən ˈmʌltɪpl/", "vi": "bội số chung nhỏ nhất; BCNN"},
    # 56: lee side
    {"pos": "phrase", "ipa": "/liː saɪd/", "vi": "phía khuất gió tàu thuyền"},
    # 57: leg it
    {"pos": "phrase", "ipa": "/lɛɡ ɪt/", "vi": "chạy trốn thục mạng; cuốc bộ nhanh"},
    # 58: legal status
    {"pos": "phrase", "ipa": "/ˈliːɡl ˈsteɪtəs/", "vi": "tư cách pháp nhân; địa vị pháp lý"},
    # 59: long jump
    {"pos": "phrase", "ipa": "/lɔːŋ dʒʌmp/", "vi": "môn nhảy xa; cú nhảy xa"},
    # 60: mail call
    {"pos": "phrase", "ipa": "/meɪl kɔːl/", "vi": "giờ điểm danh phát thư quân đội"},
    # 61: market garden
    {"pos": "phrase", "ipa": "/ˈmɑːrkɪt ˈɡɑːrdn/", "vi": "vườn trồng rau thương phẩm bán chợ"},
    # 62: moon around
    {"pos": "phrase", "ipa": "/muːn əˈraʊnd/", "vi": "tha thẩn mơ màng; vẩn vơ sầu muộn"},
    # 63: morning dress
    {"pos": "phrase", "ipa": "/ˈmɔːrnɪŋ drɛs/", "vi": "lễ phục ban ngày nam giới"},
    # 64: national guard
    {"pos": "phrase", "ipa": "/ˈnæʃnəl ɡɑːrd/", "vi": "Lực lượng Vệ binh Quốc gia Mỹ"},
    # 65: natural glass
    {"pos": "phrase", "ipa": "/ˈnætʃrəl ɡlæs/", "vi": "thủy tinh tự nhiên; đá vỏ chai"},
    # 66: news magazine
    {"pos": "phrase", "ipa": "/nuːz ˌmæɡəˈziːn/", "vi": "tạp chí thời sự; tạp chí tin tức"},
    # 67: nuclear power
    {"pos": "phrase", "ipa": "/ˈnuːkliər ˈpaʊər/", "vi": "năng lượng hạt nhân; điện hạt nhân"},
    # 68: operating room
    {"pos": "phrase", "ipa": "/ˈɑːpəreɪtɪŋ ruːm/", "vi": "phòng mổ; phòng phẫu thuật"},
    # 69: pack on
    {"pos": "phrase", "ipa": "/pæk ɑːn/", "vi": "tăng cân nhanh; đắp thêm cân nặng"},
    # 70: personal memory
    {"pos": "phrase", "ipa": "/ˈpɜːrsənl ˈmɛməri/", "vi": "ký ức cá nhân; kỷ niệm riêng tư"},
    # 71: photo opportunity
    {"pos": "phrase", "ipa": "/ˈfoʊtoʊ ˌɑːpərˈtuːnəti/", "vi": "cơ hội chụp ảnh; dịp chụp quảng bá"},
    # 72: physical contact
    {"pos": "phrase", "ipa": "/ˈfɪzɪkl ˈkɑːntækt/", "vi": "tiếp xúc thân thể; va chạm vật lý"},
    # 73: population commission
    {"pos": "phrase", "ipa": "/ˌpɑːpjuˈleɪʃn kəˈmɪʃn/", "vi": "ủy ban dân số"},
    # 74: port of call
    {"pos": "phrase", "ipa": "/pɔːrt əv kɔːl/", "vi": "cảng ghé chân; trạm dừng chân tàu"},
    # 75: positive degree
    {"pos": "phrase", "ipa": "/ˈpɑːzətɪv dɪˈɡriː/", "vi": "cấp nguyên trong so sánh ngữ pháp"},
    # 76: power failure
    {"pos": "phrase", "ipa": "/ˈpaʊər ˈfeɪljər/", "vi": "sự cố mất điện; cúp điện đột ngột"},
    # 77: practice teacher
    {"pos": "phrase", "ipa": "/ˈpræktɪs ˈtiːtʃər/", "vi": "giáo sinh thực tập"},
    # 78: prison term
    {"pos": "phrase", "ipa": "/ˈprɪzn tɜːrm/", "vi": "thời hạn tù giam; mức án tù"},
    # 79: private foundation
    {"pos": "phrase", "ipa": "/ˈpraɪvət faʊnˈdeɪʃn/", "vi": "quỹ từ thiện tư nhân; quỹ tư nhân"},
    # 80: race murder
    {"pos": "phrase", "ipa": "/reɪs ˈmɜːrdər/", "vi": "tội diệt chủng chủng tộc"},
    # 81: reference book
    {"pos": "phrase", "ipa": "/ˈrɛfrəns bʊk/", "vi": "sách tra cứu; sách tham khảo"},
    # 82: scale value
    {"pos": "phrase", "ipa": "/skeɪl ˈvæljuː/", "vi": "giá trị thang đo; chỉ số tỷ lệ"},
    # 83: sea of japan
    {"pos": "phrase", "ipa": "/siː əv dʒəˈpæn/", "vi": "biển Nhật Bản"},
    # 84: second joint
    {"pos": "phrase", "ipa": "/ˈsɛkənd dʒɔɪnt/", "vi": "má đùi gà; đùi trên gia cầm"},
    # 85: sense of hearing
    {"pos": "phrase", "ipa": "/sɛns əv ˈhɪrɪŋ/", "vi": "thính giác; khả năng nghe"},
    # 86: side arm
    {"pos": "phrase", "ipa": "/saɪd ɑːrm/", "vi": "vũ khí đeo bên hông; súng lục"},
    # 87: silver star
    {"pos": "phrase", "ipa": "/ˈsɪlvər stɑːr/", "vi": "Huân chương Ngôi sao Bạc"},
    # 88: single file
    {"pos": "phrase", "ipa": "/ˈsɪŋɡl faɪl/", "vi": "hàng một; đoàn người đi hàng một"},
    # 89: skin effect
    {"pos": "phrase", "ipa": "/skɪn ɪˈfɛkt/", "vi": "hiệu ứng bề mặt dòng điện"},
    # 90: smoke out
    {"pos": "phrase", "ipa": "/smoʊk aʊt/", "vi": "hun khói tống khứ; lôi ra ánh sáng"},
    # 91: social security administration
    {"pos": "phrase", "ipa": "/ˈsoʊʃl sɪˈkjʊrəti ədˌmɪnɪˈstreɪʃn/", "vi": "Cơ quan An sinh Xã hội Mỹ"},
    # 92: spanish american
    {"pos": "phrase", "ipa": "/ˈspænɪʃ əˈmɛrɪkən/", "vi": "người Mỹ gốc Tây Ban Nha"},
    # 93: spanish war
    {"pos": "phrase", "ipa": "/ˈspænɪʃ wɔːr/", "vi": "Chiến tranh Tây Ban Nha - Mỹ"},
    # 94: spending money
    {"pos": "phrase", "ipa": "/ˈspɛndɪŋ ˈmʌni/", "vi": "tiền tiêu vặt; tiền chi tiêu"},
    # 95: spot pass
    {"pos": "phrase", "ipa": "/spɑːt pæs/", "vi": "đường chuyền bóng đúng điểm hẹn"},
    # 96: starting block
    {"pos": "phrase", "ipa": "/ˈstɑːrtɪŋ blɑːk/", "vi": "bàn đạp xuất phát trong điền kinh"},
    # 97: state attorney
    {"pos": "phrase", "ipa": "/steɪt əˈtɜːrni/", "vi": "công tố viên tiểu bang"},
    # 98: steel company
    {"pos": "phrase", "ipa": "/stiːl ˈkʌmpəni/", "vi": "công ty luyện thép; tập đoàn thép"},
    # 99: straight life insurance
    {"pos": "phrase", "ipa": "/streɪt laɪf ɪnˈʃʊrəns/", "vi": "bảo hiểm nhân thọ trọn đời"}
]

for r in reviews:
    r["ipa"] = r["ipa"].strip()

assert len(reviews) == 100
assert len(raw_items) == 100

out_items = []
for i in range(100):
    item = dict(raw_items[i])
    rev = reviews[i]
    item["pos"] = rev["pos"]
    item["ipa"] = rev["ipa"]
    item["vi"] = rev["vi"]
    item["status"] = "reviewed"
    
    assert len(item["vi"]) <= 35, f"vi too long at {i}: {item['vi']}"
    assert len(item["vi"]) > 0
    assert item["ipa"].startswith("/") and item["ipa"].endswith("/") and item["ipa"].count("/") == 2
    out_items.append(item)

json.dump(out_items, open("scratch/b22_r01_p4.json", "w"), ensure_ascii=False, indent=2)
print("Part 4 reviewed successfully: 100 items saved to scratch/b22_r01_p4.json")
