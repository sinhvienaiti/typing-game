import json

raw_items = json.load(open("scratch/b22_r01_raw_p3.json"))

reviews = [
    # 00: control stick
    {"pos": "phrase", "ipa": "/kənˈtroʊl stɪk/", "vi": "cần điều khiển máy bay; cần lái"},
    # 01: core group
    {"pos": "phrase", "ipa": "/kɔːr ɡruːp/", "vi": "nhóm nòng cốt; nhóm cốt lõi"},
    # 02: corner post
    {"pos": "phrase", "ipa": "/ˈkɔːrnər poʊst/", "vi": "cột góc; cột ranh giới góc"},
    # 03: county seat
    {"pos": "phrase", "ipa": "/ˈkaʊnti siːt/", "vi": "thủ phủ hạt; trung tâm hành chính"},
    # 04: criminal law
    {"pos": "phrase", "ipa": "/ˈkrɪmɪnl lɔː/", "vi": "luật hình sự"},
    # 05: cross product
    {"pos": "phrase", "ipa": "/krɔːs ˈprɑːdʌkt/", "vi": "tích có hướng; tích vector"},
    # 06: difference of opinion
    {"pos": "phrase", "ipa": "/ˈdɪfrəns əv əˈpɪnjən/", "vi": "sự bất đồng quan điểm; bất hòa"},
    # 07: double bar
    {"pos": "phrase", "ipa": "/ˈdʌbl bɑːr/", "vi": "vạch kép; vạch nhịp đôi"},
    # 08: drug lord
    {"pos": "phrase", "ipa": "/drʌɡ lɔːrd/", "vi": "ông trùm ma túy"},
    # 09: dry run
    {"pos": "phrase", "ipa": "/draɪ rʌn/", "vi": "buổi diễn tập; chạy thử nghiệm"},
    # 10: dry season
    {"pos": "phrase", "ipa": "/draɪ ˈsiːzn/", "vi": "mùa khô; mùa ít mưa"},
    # 11: east wind
    {"pos": "phrase", "ipa": "/iːst wɪnd/", "vi": "gió đông; ngọn gió từ phía đông"},
    # 12: economic theory
    {"pos": "phrase", "ipa": "/ˌiːkəˈnɑːmɪk ˈθiːəri/", "vi": "lý thuyết kinh tế; học thuyết"},
    # 13: electric company
    {"pos": "phrase", "ipa": "/ɪˈlɛktrɪk ˈkʌmpəni/", "vi": "công ty điện lực"},
    # 14: european nation
    {"pos": "phrase", "ipa": "/ˌjʊərəˈpiːən ˈneɪʃn/", "vi": "quốc gia châu Âu"},
    # 15: exchange rate
    {"pos": "phrase", "ipa": "/ɪksˈtʃeɪndʒ reɪt/", "vi": "tỷ giá hối đoái; tỷ giá ngoại tệ"},
    # 16: eye operation
    {"pos": "phrase", "ipa": "/aɪ ˌɑːpəˈreɪʃn/", "vi": "phẫu thuật mắt; mổ mắt"},
    # 17: factor in
    {"pos": "phrase", "ipa": "/ˈfæktər ɪn/", "vi": "tính đến; cân nhắc; tính vào"},
    # 18: fashion industry
    {"pos": "phrase", "ipa": "/ˈfæʃn ˈɪndəstri/", "vi": "ngành công nghiệp thời trang"},
    # 19: feature film
    {"pos": "phrase", "ipa": "/ˈfiːtʃər fɪlm/", "vi": "phim truyện dài; phim chiếu rạp"},
    # 20: feed in
    {"pos": "phrase", "ipa": "/fiːd ɪn/", "vi": "nạp liệu vào; tiếp năng lượng"},
    # 21: feed on
    {"pos": "phrase", "ipa": "/fiːd ɑːn/", "vi": "ăn; nuôi sống bằng; lợi dụng"},
    # 22: field strength
    {"pos": "phrase", "ipa": "/fiːld strɛŋkθ/", "vi": "cường độ trường; cường độ điện từ"},
    # 23: first appearance
    {"pos": "phrase", "ipa": "/fɜːrst əˈpɪrəns/", "vi": "lần xuất hiện đầu tiên; màn ra mắt"},
    # 24: flow from
    {"pos": "phrase", "ipa": "/floʊ frʌm/", "vi": "bắt nguồn từ; là hệ quả của"},
    # 25: flow out
    {"pos": "phrase", "ipa": "/floʊ aʊt/", "vi": "chảy tràn ra; tuôn trào ra"},
    # 26: flying school
    {"pos": "phrase", "ipa": "/ˈflaɪɪŋ skuːl/", "vi": "trường dạy bay; trường phi công"},
    # 27: for keeps
    {"pos": "phrase", "ipa": "/fɔːr kiːps/", "vi": "mãi mãi; sở hữu vĩnh viễn"},
    # 28: fourth of july
    {"pos": "phrase", "ipa": "/fɔːrθ əv dʒuːˈlaɪ/", "vi": "Ngày Quốc khánh Mỹ 4 tháng 7"},
    # 29: free kick
    {"pos": "phrase", "ipa": "/friː kɪk/", "vi": "quả đá phạt; cú sút phạt"},
    # 30: free zone
    {"pos": "phrase", "ipa": "/friː zoʊn/", "vi": "khu miễn thuế; khu phi thuế quan"},
    # 31: french teacher
    {"pos": "phrase", "ipa": "/frɛntʃ ˈtiːtʃər/", "vi": "giáo viên tiếng Pháp"},
    # 32: get stuck
    {"pos": "phrase", "ipa": "/ɡɛt stʌk/", "vi": "bị kẹt lại; lâm vào bế tắc"},
    # 33: ground glass
    {"pos": "phrase", "ipa": "/ɡraʊnd ɡlæs/", "vi": "kính mờ; bột thủy tinh mài"},
    # 34: hard core
    {"pos": "phrase", "ipa": "/hɑːrd kɔːr/", "vi": "lực lượng nòng cốt; phần cứng rắn"},
    # 35: holy oil
    {"pos": "phrase", "ipa": "/ˈhoʊli ɔɪl/", "vi": "dầu thánh; dầu ban phép"},
    # 36: income statement
    {"pos": "phrase", "ipa": "/ˈɪnkʌm ˈsteɪtmənt/", "vi": "báo cáo thu nhập; báo cáo kết quả"},
    # 37: international wanted notice
    {"pos": "phrase", "ipa": "/ˌɪntərˈnæʃnəl ˈwɑːntɪd ˈnoʊtɪs/", "vi": "lệnh truy nã quốc tế"},
    # 38: johnson city
    {"pos": "phrase", "ipa": "/ˈdʒɑːnsn ˈsɪti/", "vi": "thành phố Johnson City"},
    # 39: join battle
    {"pos": "phrase", "ipa": "/dʒɔɪn ˈbætl/", "vi": "tham chiến; xung trận giao tranh"},
    # 40: jump off
    {"pos": "phrase", "ipa": "/dʒʌmp ɔːf/", "vi": "nhảy xuống; khởi phát; bắt đầu"},
    # 41: labour of love
    {"pos": "phrase", "ipa": "/ˈleɪbər əv lʌv/", "vi": "công việc làm vì đam mê yêu thích"},
    # 42: land agent
    {"pos": "phrase", "ipa": "/lænd ˈeɪdʒənt/", "vi": "môi giới bất động sản; quản lý đất"},
    # 43: leading lady
    {"pos": "phrase", "ipa": "/ˈliːdɪŋ ˈleɪdi/", "vi": "nữ diễn viên chính; nữ chính"},
    # 44: letter of credit
    {"pos": "phrase", "ipa": "/ˈlɛtər əv ˈkrɛdɪt/", "vi": "thư tín dụng; chứng từ LC"},
    # 45: library science
    {"pos": "phrase", "ipa": "/ˈlaɪbrɛri ˈsaɪəns/", "vi": "khoa học thư viện"},
    # 46: like blue murder
    {"pos": "phrase", "ipa": "/laɪk bluː ˈmɜːrdər/", "vi": "hết tốc lực; như điên cuồng"},
    # 47: little bear
    {"pos": "phrase", "ipa": "/ˈlɪtl bɛr/", "vi": "chòm sao Tiểu Hùng"},
    # 48: living standards
    {"pos": "phrase", "ipa": "/ˈlɪvɪŋ ˈstændərdz/", "vi": "mức sống; điều kiện sinh hoạt"},
    # 49: long suit
    {"pos": "phrase", "ipa": "/lɔːŋ suːt/", "vi": "sở trường; bộ bài nhiều cây nhất"},
    # 50: lower status
    {"pos": "phrase", "ipa": "/ˈloʊər ˈsteɪtəs/", "vi": "địa vị thấp hơn; thân phận thấp kém"},
    # 51: marriage offer
    {"pos": "phrase", "ipa": "/ˈmærɪdʒ ˈɔːfər/", "vi": "lời cầu hôn; lời dạm ngõ"},
    # 52: memory board
    {"pos": "phrase", "ipa": "/ˈmɛməri bɔːrd/", "vi": "bo mạch bộ nhớ; thẻ nhớ máy tính"},
    # 53: mental test
    {"pos": "phrase", "ipa": "/ˈmɛntl tɛst/", "vi": "bài kiểm tra tâm lý; trắc nghiệm"},
    # 54: minute gun
    {"pos": "phrase", "ipa": "/ˈmɪnɪt ɡʌn/", "vi": "tiếng súng đại bác điểm từng phút"},
    # 55: new stone age
    {"pos": "phrase", "ipa": "/njuː stoʊn eɪdʒ/", "vi": "thời kỳ đồ đá mới; đồ đá mới"},
    # 56: ocean state
    {"pos": "phrase", "ipa": "/ˈoʊʃn steɪt/", "vi": "biệt danh bang Rhode Island"},
    # 57: paper plant
    {"pos": "phrase", "ipa": "/ˈpeɪpər plænt/", "vi": "cây cói giấy; nhà máy giấy"},
    # 58: passed ball
    {"pos": "phrase", "ipa": "/pæst bɔːl/", "vi": "bóng vuột tay bắt bóng chày"},
    # 59: personal estate
    {"pos": "phrase", "ipa": "/ˈpɜːrsənl ɪˈsteɪt/", "vi": "động sản; tài sản cá nhân"},
    # 60: point of reference
    {"pos": "phrase", "ipa": "/pɔɪnt əv ˈrɛfrəns/", "vi": "điểm quy chiếu; chuẩn so sánh"},
    # 61: police van
    {"pos": "phrase", "ipa": "/pəˈliːs væn/", "vi": "xe thùng cảnh sát; xe chở phạm nhân"},
    # 62: poor rates
    {"pos": "phrase", "ipa": "/pʊr reɪts/", "vi": "thuế cứu tế người nghèo xưa"},
    # 63: primary election
    {"pos": "phrase", "ipa": "/ˈpraɪmɛri ɪˈlɛkʃn/", "vi": "cuộc bầu cử sơ bộ; vòng sơ bộ"},
    # 64: progress report
    {"pos": "phrase", "ipa": "/ˈprɑːɡrɛs rɪˈpɔːrt/", "vi": "báo cáo tiến độ"},
    # 65: proper name
    {"pos": "phrase", "ipa": "/ˈprɑːpər neɪm/", "vi": "tên riêng; danh từ riêng"},
    # 66: putting green
    {"pos": "phrase", "ipa": "/ˈpʌtɪŋ ɡriːn/", "vi": "khu gạt bóng cỏ xanh trên sân golf"},
    # 67: queen of england
    {"pos": "phrase", "ipa": "/kwiːn əv ˈɪŋɡlənd/", "vi": "Nữ hoàng nước Anh"},
    # 68: rate of exchange
    {"pos": "phrase", "ipa": "/reɪt əv ɪksˈtʃeɪndʒ/", "vi": "tỷ giá hối đoái; tỷ giá ngoại tệ"},
    # 69: real presence
    {"pos": "phrase", "ipa": "/riːl ˈprɛzns/", "vi": "sự hiện diện thực thể Thánh Thể"},
    # 70: ring road
    {"pos": "phrase", "ipa": "/rɪŋ roʊd/", "vi": "đường vành đai; đường vòng ngoại ô"},
    # 71: road agent
    {"pos": "phrase", "ipa": "/roʊd ˈeɪdʒənt/", "vi": "tướng cướp chặn đường; cướp xa lộ"},
    # 72: rock band
    {"pos": "phrase", "ipa": "/rɑːk bænd/", "vi": "ban nhạc rock; ban nhạc rốc"},
    # 73: royal blue
    {"pos": "phrase", "ipa": "/ˈrɔɪəl bluː/", "vi": "màu xanh lam hoàng gia"},
    # 74: run dry
    {"pos": "phrase", "ipa": "/rʌn draɪ/", "vi": "cạn khô; cạn kiệt nguồn cung"},
    # 75: saw wood
    {"pos": "phrase", "ipa": "/sɔː wʊd/", "vi": "cưa gỗ; ngáy khò khò khi ngủ"},
    # 76: sea captain
    {"pos": "phrase", "ipa": "/siː ˈkæptɪn/", "vi": "thuyền trưởng tàu viễn dương"},
    # 77: selling price
    {"pos": "phrase", "ipa": "/ˈsɛlɪŋ praɪs/", "vi": "giá bán; mức giá niêm yết"},
    # 78: shared out
    {"pos": "phrase", "ipa": "/ʃɛrd aʊt/", "vi": "đã chia phần; được phân phát"},
    # 79: shot metal
    {"pos": "phrase", "ipa": "/ʃɑːt ˈmɛtl/", "vi": "hợp kim đúc đạn chì"},
    # 80: slow match
    {"pos": "phrase", "ipa": "/sloʊ mætʃ/", "vi": "dây cháy chậm; ngòi nổ chậm"},
    # 81: sound structure
    {"pos": "phrase", "ipa": "/saʊnd ˈstrʌktʃər/", "vi": "cấu trúc ngữ âm; kết cấu vững chắc"},
    # 82: south west africa
    {"pos": "phrase", "ipa": "/saʊθ wɛst ˈæfrɪkə/", "vi": "vùng Tây Nam Phi; Namibia cũ"},
    # 83: speech production
    {"pos": "phrase", "ipa": "/spiːtʃ prəˈdʌkʃn/", "vi": "sự tạo lời nói; quá trình phát âm"},
    # 84: speech sound
    {"pos": "phrase", "ipa": "/spiːtʃ saʊnd/", "vi": "ngữ âm; âm thanh lời nói"},
    # 85: sports section
    {"pos": "phrase", "ipa": "/spɔːrts ˈsɛkʃn/", "vi": "chuyên mục thể thao trên báo"},
    # 86: supreme being
    {"pos": "phrase", "ipa": "/suːˈpriːm ˈbiːɪŋ/", "vi": "Đấng Tối cao; Thượng đế"},
    # 87: tea set
    {"pos": "phrase", "ipa": "/tiː sɛt/", "vi": "bộ ấm chén uống trà; bộ đồ trà"},
    # 88: team teaching
    {"pos": "phrase", "ipa": "/tiːm ˈtiːtʃɪŋ/", "vi": "hình thức giảng dạy theo nhóm"},
    # 89: television program
    {"pos": "phrase", "ipa": "/ˈtɛləvɪʒn ˈproʊɡræm/", "vi": "chương trình truyền hình"},
    # 90: three hundred
    {"pos": "phrase", "ipa": "/θriː ˈhʌndrəd/", "vi": "ba trăm"},
    # 91: time loan
    {"pos": "phrase", "ipa": "/taɪm loʊn/", "vi": "khoản vay có kỳ hạn cố định"},
    # 92: touch base
    {"pos": "phrase", "ipa": "/tʌtʃ beɪs/", "vi": "liên lạc ngắn; trao đổi nhanh"},
    # 93: union shop
    {"pos": "phrase", "ipa": "/ˈjuːnjən ʃɑːp/", "vi": "xưởng yêu cầu gia nhập công đoàn"},
    # 94: war criminal
    {"pos": "phrase", "ipa": "/wɔːr ˈkrɪmɪnl/", "vi": "tội phạm chiến tranh"},
    # 95: waste of energy
    {"pos": "phrase", "ipa": "/weɪst əv ˈɛnərdʒi/", "vi": "sự lãng phí năng lượng; uổng công"},
    # 96: wedding present
    {"pos": "phrase", "ipa": "/ˈwɛdɪŋ ˈprɛznt/", "vi": "quà mừng đám cưới; quà cưới"},
    # 97: white wine
    {"pos": "phrase", "ipa": "/waɪt waɪn/", "vi": "rượu vang trắng"},
    # 98: wind park
    {"pos": "phrase", "ipa": "/wɪnd pɑːrk/", "vi": "trang trại điện gió; phong điện"},
    # 99: written agreement
    {"pos": "phrase", "ipa": "/ˈrɪtn əˈɡriːmənt/", "vi": "văn bản thỏa thuận; hợp đồng viết"}
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

json.dump(out_items, open("scratch/b22_r01_p3.json", "w"), ensure_ascii=False, indent=2)
print("Part 3 reviewed successfully: 100 items saved to scratch/b22_r01_p3.json")
