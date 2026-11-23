import json

raw_items = json.load(open("scratch/b22_r02_raw_p1.json"))

reviews = [
    # 00: sexual relationship
    {"pos": "phrase", "ipa": "/ˈsɛkʃuəl rɪˈleɪʃnʃɪp/", "vi": "quan hệ tình dục; quan hệ thể xác"},
    # 01: small boat
    {"pos": "phrase", "ipa": "/smɔːl boʊt/", "vi": "thuyền nhỏ; xuồng chèo"},
    # 02: software program
    {"pos": "phrase", "ipa": "/ˈsɔːftwɛr ˈproʊɡræm/", "vi": "phần mềm; chương trình phần mềm"},
    # 03: solid food
    {"pos": "phrase", "ipa": "/ˈsɑːlɪd fuːd/", "vi": "thức ăn đặc; thức ăn dạng rắn"},
    # 04: sport car
    {"pos": "phrase", "ipa": "/spɔːrt kɑːr/", "vi": "xe thể thao; ô tô thể thao"},
    # 05: staff tree
    {"pos": "phrase", "ipa": "/stæf triː/", "vi": "cây dây gối Celastrus"},
    # 06: standing army
    {"pos": "phrase", "ipa": "/ˈstændɪŋ ˈɑːrmi/", "vi": "quân đội thường trực"},
    # 07: strike out
    {"pos": "phrase", "ipa": "/straɪk aʊt/", "vi": "gạch bỏ; bị loại khỏi cuộc đấu"},
    # 08: strike up
    {"pos": "phrase", "ipa": "/straɪk ʌp/", "vi": "trỗi khúc nhạc; bắt chuyện"},
    # 09: sun dance
    {"pos": "phrase", "ipa": "/sʌn dæns/", "vi": "điệu múa tế Mặt Trời da đỏ"},
    # 10: tax benefit
    {"pos": "phrase", "ipa": "/tæks ˈbɛnɪfɪt/", "vi": "ưu đãi thuế; quyền lợi giảm thuế"},
    # 11: time sharing
    {"pos": "phrase", "ipa": "/taɪm ˈʃɛrɪŋ/", "vi": "phân chia thời gian; dùng chung máy"},
    # 12: trust fund
    {"pos": "phrase", "ipa": "/trʌst fʌnd/", "vi": "quỹ tín thác; quỹ ủy thác tài sản"},
    # 13: truth drug
    {"pos": "phrase", "ipa": "/truːθ drʌɡ/", "vi": "thuốc thú tội; huyết thanh nói thật"},
    # 14: turning point
    {"pos": "phrase", "ipa": "/ˈtɜːrnɪŋ pɔɪnt/", "vi": "bước ngoặt; thời khắc quyết định"},
    # 15: united states senate
    {"pos": "phrase", "ipa": "/juːˈnaɪtɪd steɪts ˈsɛnət/", "vi": "Thượng viện Hoa Kỳ"},
    # 16: upper side
    {"pos": "phrase", "ipa": "/ˈʌpər saɪd/", "vi": "mặt trên; phía trên cùng"},
    # 17: village green
    {"pos": "phrase", "ipa": "/ˈvɪlɪdʒ ɡriːn/", "vi": "bãi cỏ trung tâm làng quê"},
    # 18: war zone
    {"pos": "phrase", "ipa": "/wɔːr zoʊn/", "vi": "vùng chiến sự; khu vực chiến sự"},
    # 19: wedding picture
    {"pos": "phrase", "ipa": "/ˈwɛdɪŋ ˈpɪktʃər/", "vi": "ảnh cưới; ảnh chụp hôn lễ"},
    # 20: finals
    {"pos": "noun", "ipa": "/ˈfaɪnlz/", "vi": "các trận chung kết; kỳ thi cuối kỳ"},
    # 21: readier
    {"pos": "adj", "ipa": "/ˈrɛdiər/", "vi": "sẵn sàng hơn; chuẩn bị kỹ hơn"},
    # 22: readiest
    {"pos": "adj", "ipa": "/ˈrɛdiɪst/", "vi": "sẵn sàng nhất; chuẩn bị tốt nhất"},
    # 23: association theory
    {"pos": "phrase", "ipa": "/əˌsoʊsiˈeɪʃn ˈθiːəri/", "vi": "thuyết liên tưởng tâm lý"},
    # 24: at fault
    {"pos": "phrase", "ipa": "/æt fɔːlt/", "vi": "có lỗi; có trách nhiệm sai sót"},
    # 25: back pack
    {"pos": "phrase", "ipa": "/bæk pæk/", "vi": "ba lô du lịch; ba lô đeo lưng"},
    # 26: become flat
    {"pos": "phrase", "ipa": "/bɪˈkʌm flæt/", "vi": "hết ga; bị xẹp lốp; mất bọt"},
    # 27: beyond doubt
    {"pos": "phrase", "ipa": "/bɪˈjɑːnd daʊt/", "vi": "không còn nghi ngờ; rõ như ban ngày"},
    # 28: black bear
    {"pos": "phrase", "ipa": "/blæk bɛr/", "vi": "gấu đen châu Mỹ"},
    # 29: block capital
    {"pos": "phrase", "ipa": "/blɑːk ˈkæpɪtl/", "vi": "chữ in hoa nét rời; chữ in hoa"},
    # 30: blood count
    {"pos": "phrase", "ipa": "/blʌd kaʊnt/", "vi": "chỉ số huyết học; số lượng tế bào"},
    # 31: blood profile
    {"pos": "phrase", "ipa": "/blʌd ˈproʊfaɪl/", "vi": "xét nghiệm công thức máu toàn bộ"},
    # 32: book of facts
    {"pos": "phrase", "ipa": "/bʊk əv fækts/", "vi": "sách sự kiện tra cứu; niên giám"},
    # 33: break camp
    {"pos": "phrase", "ipa": "/breɪk kæmp/", "vi": "nhổ trại; dỡ bỏ doanh trại"},
    # 34: business suit
    {"pos": "phrase", "ipa": "/ˈbɪznəs suːt/", "vi": "bộ vest công sở; com-lê lịch thiệp"},
    # 35: capital of japan
    {"pos": "phrase", "ipa": "/ˈkæpɪtl əv dʒəˈpæn/", "vi": "thủ đô nước Nhật; Tokyo"},
    # 36: capital of texas
    {"pos": "phrase", "ipa": "/ˈkæpɪtl əv ˈtɛksəs/", "vi": "thủ phủ bang Texas; Austin"},
    # 37: catch cold
    {"pos": "phrase", "ipa": "/kætʃ koʊld/", "vi": "bị cảm lạnh; nhiễm lạnh"},
    # 38: chain up
    {"pos": "phrase", "ipa": "/tʃeɪn ʌp/", "vi": "xích lại cẩn thận; khóa bằng xích"},
    # 39: china rose
    {"pos": "phrase", "ipa": "/ˈtʃaɪnə roʊz/", "vi": "hoa dâm bụt; hoa hồng Trung Quốc"},
    # 40: civil leader
    {"pos": "phrase", "ipa": "/ˈsɪvl ˈliːdər/", "vi": "thủ lĩnh dân sự; lãnh đạo công dân"},
    # 41: coffee table
    {"pos": "phrase", "ipa": "/ˈkɔːfi ˈteɪbl/", "vi": "bàn trà phòng khách; bàn uống nước"},
    # 42: cold weather
    {"pos": "phrase", "ipa": "/koʊld ˈwɛðər/", "vi": "thời tiết giá rét; đợt rét lạnh"},
    # 43: computer address
    {"pos": "phrase", "ipa": "/kəmˈpjuːtər əˈdrɛs/", "vi": "địa chỉ bộ nhớ máy tính"},
    # 44: computer operation
    {"pos": "phrase", "ipa": "/kəmˈpjuːtər ˌɑːpəˈreɪʃn/", "vi": "thao tác xử lý dữ liệu máy tính"},
    # 45: cook out
    {"pos": "phrase", "ipa": "/kʊk aʊt/", "vi": "nấu ăn ngoài trời; mở tiệc nướng"},
    # 46: cook up
    {"pos": "phrase", "ipa": "/kʊk ʌp/", "vi": "bịa đặt ra; dàn dựng kế hoạch"},
    # 47: core bit
    {"pos": "phrase", "ipa": "/kɔːr bɪt/", "vi": "mũi khoan lấy mẫu lõi địa chất"},
    # 48: course session
    {"pos": "phrase", "ipa": "/kɔːrs ˈsɛʃn/", "vi": "buổi học trong khóa; tiết học"},
    # 49: death valley
    {"pos": "phrase", "ipa": "/dɛθ ˈvæli/", "vi": "Thung lũng Chết California"},
    # 50: defense secretary
    {"pos": "phrase", "ipa": "/dɪˈfɛns ˈsɛkrətɛri/", "vi": "Bộ trưởng Quốc phòng"},
    # 51: department of labor
    {"pos": "phrase", "ipa": "/dɪˈpɑːrtmənt əv ˈleɪbər/", "vi": "Bộ Lao động Hoa Kỳ"},
    # 52: discovered check
    {"pos": "phrase", "ipa": "/dɪˈskʌvərd tʃɛk/", "vi": "nước chiếu rút mở trong cờ vua"},
    # 53: dog rose
    {"pos": "phrase", "ipa": "/dɔːɡ roʊz/", "vi": "cây hoa tầm xuân dại"},
    # 54: eastern united states
    {"pos": "phrase", "ipa": "/ˈiːstərn juːˈnaɪtɪd steɪts/", "vi": "miền Đông nước Mỹ"},
    # 55: emergency room
    {"pos": "phrase", "ipa": "/ɪˈmɜːrdʒənsi ruːm/", "vi": "phòng cấp cứu bệnh viện"},
    # 56: enter upon
    {"pos": "phrase", "ipa": "/ˈɛntər əˈpɑːn/", "vi": "bắt tay vào; tiếp quản quyền sở hữu"},
    # 57: escape from
    {"pos": "phrase", "ipa": "/ɪˈskeɪp frʌm/", "vi": "trốn thoát khỏi; né tránh được"},
    # 58: european central bank
    {"pos": "phrase", "ipa": "/ˌjʊərəˈpiːən ˈsɛntrəl bæŋk/", "vi": "Ngân hàng Trung ương châu Âu; ECB"},
    # 59: executive officer
    {"pos": "phrase", "ipa": "/ɪɡˈzɛkjətɪv ˈɔːfɪsər/", "vi": "phó chỉ huy tàu; phó thuyền trưởng"},
    # 60: falling off
    {"pos": "phrase", "ipa": "/ˈfɔːlɪŋ ɔːf/", "vi": "sự sa sút sụt giảm; độ dốc xuống"},
    # 61: farm building
    {"pos": "phrase", "ipa": "/fɑːrm ˈbɪldɪŋ/", "vi": "khu nhà phụ nông trại; chuồng trại"},
    # 62: fast time scale
    {"pos": "phrase", "ipa": "/fæst taɪm skeɪl/", "vi": "thang chia thời gian tốc độ nhanh"},
    # 63: federal agent
    {"pos": "phrase", "ipa": "/ˈfɛdərəl ˈeɪdʒənt/", "vi": "đặc vụ liên bang FBI"},
    # 64: figure of speech
    {"pos": "phrase", "ipa": "/ˈfɪɡjər əv spiːtʃ/", "vi": "biện pháp tu từ; cách nói bóng bẩy"},
    # 65: fill in
    {"pos": "phrase", "ipa": "/fɪl ɪn/", "vi": "điền vào phiếu; thông báo chi tiết"},
    # 66: first strike
    {"pos": "phrase", "ipa": "/fɜːrst straɪk/", "vi": "đòn hạt nhân phủ đầu bất ngờ"},
    # 67: five hundred
    {"pos": "phrase", "ipa": "/faɪv ˈhʌndrəd/", "vi": "năm trăm"},
    # 68: floor leader
    {"pos": "phrase", "ipa": "/flɔːr ˈliːdər/", "vi": "lãnh đạo phe tại nghị trường viện"},
    # 69: fly front
    {"pos": "phrase", "ipa": "/flaɪ frʌnt/", "vi": "nẹp áo cài khuy giấu kín"},
    # 70: fuel level
    {"pos": "phrase", "ipa": "/ˈfjuːəl ˈlɛvl/", "vi": "mức nhiên liệu trong bình chứa"},
    # 71: full moon
    {"pos": "phrase", "ipa": "/fʊl muːn/", "vi": "trăng rằm; trăng tròn vằng vặc"},
    # 72: gas plant
    {"pos": "phrase", "ipa": "/ɡæs plænt/", "vi": "cây bụi Dictamnus; nhà máy khí đốt"},
    # 73: golden state
    {"pos": "phrase", "ipa": "/ˈɡoʊldən steɪt/", "vi": "biệt danh bang California"},
    # 74: governor general
    {"pos": "phrase", "ipa": "/ˈɡʌvərnər ˈdʒɛnrəl/", "vi": "toàn quyền đại diện Hoàng gia"},
    # 75: hearing dog
    {"pos": "phrase", "ipa": "/ˈhɪrɪŋ dɔːɡ/", "vi": "chó dẫn đường trợ thính người điếc"},
    # 76: hold firm
    {"pos": "phrase", "ipa": "/hoʊld fɜːrm/", "vi": "giữ vững lập trường; kiên định"},
    # 77: honest woman
    {"pos": "phrase", "ipa": "/ˈɑːnɪst ˈwʊmən/", "vi": "người vợ cưới hỏi đường hoàng"},
    # 78: honor system
    {"pos": "phrase", "ipa": "/ˈɑːnər ˈsɪstəm/", "vi": "quy chế tự giác danh dự thi cử"},
    # 79: hot water plant
    {"pos": "phrase", "ipa": "/hɑːt ˈwɔːtər plænt/", "vi": "cây hoa Achimenes"},
    # 80: housing project
    {"pos": "phrase", "ipa": "/ˈhaʊzɪŋ ˈprɑːdʒɛkt/", "vi": "dự án nhà ở xã hội; cư xá công"},
    # 81: ice plant
    {"pos": "phrase", "ipa": "/aɪs plænt/", "vi": "cây mọng nước giọt băng móng rồng"},
    # 82: ii peter
    {"pos": "phrase", "ipa": "/tuː ˈpiːtər/", "vi": "Thư thứ hai của Thánh Phêrô"},
    # 83: ill health
    {"pos": "phrase", "ipa": "/ɪl hɛlθ/", "vi": "sức khỏe yếu kém; tình trạng ốm đau"},
    # 84: insurance claim
    {"pos": "phrase", "ipa": "/ɪnˈʃʊrəns kleɪm/", "vi": "hồ sơ yêu cầu bồi thường bảo hiểm"},
    # 85: iron age
    {"pos": "phrase", "ipa": "/ˈaɪərn eɪdʒ/", "vi": "thời đại đồ sắt tiền sử"},
    # 86: john paul ii
    {"pos": "phrase", "ipa": "/dʒɑːn pɔːl tuː/", "vi": "Giáo hoàng John Paul II"},
    # 87: key ring
    {"pos": "phrase", "ipa": "/kiː rɪŋ/", "vi": "vòng móc chìa khóa"},
    # 88: king james version
    {"pos": "phrase", "ipa": "/kɪŋ dʒeɪmz ˈvɜːrʒn/", "vi": "Kinh Thánh bản King James KJV"},
    # 89: labor department
    {"pos": "phrase", "ipa": "/ˈleɪbər dɪˈpɑːrtmənt/", "vi": "Bộ Lao động; cơ quan lao động"},
    # 90: labor force
    {"pos": "phrase", "ipa": "/ˈleɪbər fɔːrs/", "vi": "lực lượng lao động; nguồn nhân lực"},
    # 91: laugh off
    {"pos": "phrase", "ipa": "/læf ɔːf/", "vi": "cười xòa bỏ qua chuyện buồn rầu"},
    # 92: lay in
    {"pos": "phrase", "ipa": "/leɪ ɪn/", "vi": "dự trữ tích trữ vật tư đồ ăn"},
    # 93: learning ability
    {"pos": "phrase", "ipa": "/ˈlɜːrnɪŋ əˈbɪləti/", "vi": "khả năng tiếp thu; năng lực học hỏi"},
    # 94: letter stock
    {"pos": "phrase", "ipa": "/ˈlɛtər stɑːk/", "vi": "cổ phiếu chưa đăng ký phát hành"},
    # 95: library card
    {"pos": "phrase", "ipa": "/ˈlaɪbrɛri kɑːrd/", "vi": "thẻ mượn sách; thẻ thư viện"},
    # 96: limit point
    {"pos": "phrase", "ipa": "/ˈlɪmɪt pɔɪnt/", "vi": "điểm tụ; điểm giới hạn toán học"},
    # 97: line of duty
    {"pos": "phrase", "ipa": "/laɪn əv ˈduːti/", "vi": "khi đang thi hành công vụ"},
    # 98: links course
    {"pos": "phrase", "ipa": "/lɪŋks kɔːrs/", "vi": "sân golf ven biển địa hình đồi cát"},
    # 99: majority leader
    {"pos": "phrase", "ipa": "/məˈdʒɔːrəti ˈliːdər/", "vi": "lãnh tụ phe đa số nghị viện"}
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

json.dump(out_items, open("scratch/b22_r02_p1.json", "w"), ensure_ascii=False, indent=2)
print("Round 2 Part 1 reviewed successfully: 100 items saved to scratch/b22_r02_p1.json")
