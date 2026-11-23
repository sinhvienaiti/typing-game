import json

raw_items = json.load(open("scratch/b22_r02_raw_p5.json"))

reviews = [
    # 00: age limit
    {"pos": "phrase", "ipa": "/eɪdʒ ˈlɪmɪt/", "vi": "giới hạn độ tuổi; hạn định tuổi"},
    # 01: apartment house
    {"pos": "phrase", "ipa": "/əˈpɑːrtmənt haʊs/", "vi": "tòa nhà chung cư; khu tập thể"},
    # 02: bear market
    {"pos": "phrase", "ipa": "/bɛr ˈmɑːrkɪt/", "vi": "thị trường gấu giá xuống"},
    # 03: benefit album
    {"pos": "phrase", "ipa": "/ˈbɛnɪfɪt ˈælbəm/", "vi": "album ca nhạc từ thiện gây quỹ"},
    # 04: block letter
    {"pos": "phrase", "ipa": "/blɑːk ˈlɛtər/", "vi": "chữ in hoa nét đậm rời"},
    # 05: bowl over
    {"pos": "phrase", "ipa": "/boʊl ˈoʊvər/", "vi": "xô ngã nhào; làm kinh ngạc sững sờ"},
    # 06: box seat
    {"pos": "phrase", "ipa": "/bɑːks siːt/", "vi": "ghế ngồi trong lô danh dự"},
    # 07: british parliament
    {"pos": "phrase", "ipa": "/ˈbrɪtɪʃ ˈpɑːrləmənt/", "vi": "Nghị viện Anh; Quốc hội Anh"},
    # 08: bus station
    {"pos": "phrase", "ipa": "/bʌs ˈsteɪʃn/", "vi": "bến xe buýt; bến xe khách"},
    # 09: business concern
    {"pos": "phrase", "ipa": "/ˈbɪznəs kənˈsɜːrn/", "vi": "cơ sở kinh doanh; doanh nghiệp"},
    # 10: business lunch
    {"pos": "phrase", "ipa": "/ˈbɪznəs lʌntʃ/", "vi": "bữa trưa bàn công việc làm ăn"},
    # 11: business sector
    {"pos": "phrase", "ipa": "/ˈbɪznəs ˈsɛktər/", "vi": "khu vực kinh doanh doanh nghiệp"},
    # 12: camp bed
    {"pos": "phrase", "ipa": "/kæmp bɛd/", "vi": "giường xếp dã chiến gấp gọn"},
    # 13: car loan
    {"pos": "phrase", "ipa": "/kɑːr loʊn/", "vi": "khoản vay mua xe ô tô trả góp"},
    # 14: cash machine
    {"pos": "phrase", "ipa": "/kæʃ məˈʃiːn/", "vi": "máy rút tiền tự động cây ATM"},
    # 15: centre of mass
    {"pos": "phrase", "ipa": "/ˈsɛntər əv mæs/", "vi": "khối tâm cơ học vật lý"},
    # 16: charge per unit
    {"pos": "phrase", "ipa": "/tʃɑːrdʒ pɜːr ˈjuːnɪt/", "vi": "đơn giá trên mỗi sản phẩm"},
    # 17: church roll
    {"pos": "phrase", "ipa": "/tʃɜːrtʃ roʊl/", "vi": "danh sách giáo dân trong giáo xứ"},
    # 18: commercial credit company
    {"pos": "phrase", "ipa": "/kəˈmɜːrʃl ˈkrɛdɪt ˈkʌmpəni/", "vi": "công ty tín dụng thương mại"},
    # 19: computer screen
    {"pos": "phrase", "ipa": "/kəmˈpjuːtər skriːn/", "vi": "màn hình máy tính hiển thị"},
    # 20: confidence game
    {"pos": "phrase", "ipa": "/ˈkɑːnfədəns ɡeɪm/", "vi": "trò lừa đảo chiếm đoạt lòng tin"},
    # 21: contract killing
    {"pos": "phrase", "ipa": "/ˈkɑːntrækt ˈkɪlɪŋ/", "vi": "vụ giết người thuê theo hợp đồng"},
    # 22: date of reference
    {"pos": "phrase", "ipa": "/deɪt əv ˈrɛfrəns/", "vi": "ngày tham chiếu; mốc thời gian"},
    # 23: death chair
    {"pos": "phrase", "ipa": "/dɛθ tʃɛr/", "vi": "ghế điện tử hình phạm nhân"},
    # 24: drinking age
    {"pos": "phrase", "ipa": "/ˈdrɪŋkɪŋ eɪdʒ/", "vi": "độ tuổi hợp pháp được uống rượu"},
    # 25: electric current
    {"pos": "phrase", "ipa": "/ɪˈlɛktrɪk ˈkɜːrənt/", "vi": "dòng điện chạy qua mạch dẫn"},
    # 26: electric field
    {"pos": "phrase", "ipa": "/ɪˈlɛktrɪk fiːld/", "vi": "điện trường tĩnh điện"},
    # 27: electric main
    {"pos": "phrase", "ipa": "/ɪˈlɛktrɪk meɪn/", "vi": "đường dây tải điện chính tổng"},
    # 28: emotional person
    {"pos": "phrase", "ipa": "/ɪˈmoʊʃənl ˈpɜːrsn/", "vi": "người sống nội tâm giàu cảm xúc"},
    # 29: executive secretary
    {"pos": "phrase", "ipa": "/ɪɡˈzɛkjətɪv ˈsɛkrətɛri/", "vi": "thư ký điều hành ban giám đốc"},
    # 30: farm boy
    {"pos": "phrase", "ipa": "/fɑːrm bɔɪ/", "vi": "chàng trai nông thôn trang trại"},
    # 31: fellow feeling
    {"pos": "phrase", "ipa": "/ˈfɛloʊ ˈfiːlɪŋ/", "vi": "tình đồng cảm; sự sẻ chia"},
    # 32: field sport
    {"pos": "phrase", "ipa": "/fiːld spɔːrt/", "vi": "thể thao dã ngoại săn bắn câu cá"},
    # 33: find fault
    {"pos": "phrase", "ipa": "/faɪnd fɔːlt/", "vi": "bới lông tìm vết; soi mói bắt bẻ"},
    # 34: golden mean
    {"pos": "phrase", "ipa": "/ˈɡoʊldən miːn/", "vi": "thuyết trung dung triết học"},
    # 35: great falls
    {"pos": "phrase", "ipa": "/ɡreɪt fɔːlz/", "vi": "thành phố Great Falls ở Montana"},
    # 36: growth ring
    {"pos": "phrase", "ipa": "/ɡroʊθ rɪŋ/", "vi": "vòng sinh trưởng thân gỗ hàng năm"},
    # 37: hearing officer
    {"pos": "phrase", "ipa": "/ˈhɪrɪŋ ˈɔːfɪsər/", "vi": "chủ tọa phiên điều trần hành chính"},
    # 38: high temperature
    {"pos": "phrase", "ipa": "/haɪ ˈtɛmprətʃər/", "vi": "nhiệt độ cao nóng bỏng"},
    # 39: income tax return
    {"pos": "phrase", "ipa": "/ˈɪnkʌm tæks rɪˈtɜːrn/", "vi": "tờ khai quyết toán thuế thu nhập"},
    # 40: intelligence community
    {"pos": "phrase", "ipa": "/ɪnˈtɛlɪdʒəns kəˈmjuːnəti/", "vi": "cộng đồng các cơ quan tình báo"},
    # 41: jersey city
    {"pos": "phrase", "ipa": "/ˈdʒɜːrzi ˈsɪti/", "vi": "thành phố Jersey City"},
    # 42: keep quiet
    {"pos": "phrase", "ipa": "/kiːp ˈkwaɪət/", "vi": "giữ im lặng; giữ bí mật chuyện"},
    # 43: laugh away
    {"pos": "phrase", "ipa": "/læf əˈweɪ/", "vi": "cười xòa gạt bỏ phiền muộn"},
    # 44: light beer
    {"pos": "phrase", "ipa": "/laɪt bɪr/", "vi": "bia nhẹ ít cồn ít calo"},
    # 45: line feed
    {"pos": "phrase", "ipa": "/laɪn fiːd/", "vi": "lệnh xuống dòng mới mã ASCII LF"},
    # 46: london plane
    {"pos": "phrase", "ipa": "/ˈlʌndən pleɪn/", "vi": "cây tiêu huyền London lai giống"},
    # 47: louis ii
    {"pos": "phrase", "ipa": "/ˈluːi ðə ˈsɛkənd/", "vi": "Vua Louis Đệ Nhị"},
    # 48: machine operation
    {"pos": "phrase", "ipa": "/məˈʃiːn ˌɑːpəˈreɪʃn/", "vi": "thao tác vận hành máy tính cơ khí"},
    # 49: mass unit
    {"pos": "phrase", "ipa": "/mæs ˈjuːnɪt/", "vi": "đơn vị đo khối lượng"},
    # 50: master of laws
    {"pos": "phrase", "ipa": "/ˈmæstər əv lɔːz/", "vi": "bằng Thạc sĩ Luật học LLM"},
    # 51: medical aid
    {"pos": "phrase", "ipa": "/ˈmɛdɪkl eɪd/", "vi": "cứu trợ y tế; viện trợ y tế"},
    # 52: member of parliament
    {"pos": "phrase", "ipa": "/ˈmɛmbər əv ˈpɑːrləmənt/", "vi": "nghị sĩ quốc hội; đại biểu quốc hội"},
    # 53: memory access
    {"pos": "phrase", "ipa": "/ˈmɛməri ˈæksɛs/", "vi": "truy xuất dữ liệu ô nhớ RAM"},
    # 54: mother jones
    {"pos": "phrase", "ipa": "/ˈmʌðər dʒoʊnz/", "vi": "nhà hoạt động Mother Jones"},
    # 55: new wave
    {"pos": "phrase", "ipa": "/njuː weɪv/", "vi": "phong trào làn sóng mới văn nghệ"},
    # 56: not guilty
    {"pos": "phrase", "ipa": "/nɑːt ˈɡɪlti/", "vi": "tuyên trắng án vô tội trước tòa"},
    # 57: nuclear energy
    {"pos": "phrase", "ipa": "/ˈnuːkliər ˈɛnərdʒi/", "vi": "năng lượng nguyên tử hạt nhân"},
    # 58: on the wing
    {"pos": "phrase", "ipa": "/ɑːn ðə wɪŋ/", "vi": "đang dang cánh bay lượn"},
    # 59: paper bag
    {"pos": "phrase", "ipa": "/ˈpeɪpər bæɡ/", "vi": "túi giấy đựng đồ mua sắm"},
    # 60: point of entry
    {"pos": "phrase", "ipa": "/pɔɪnt əv ˈɛntri/", "vi": "cửa khẩu xuất nhập cảnh biên giới"},
    # 61: prime minister
    {"pos": "phrase", "ipa": "/praɪm ˈmɪnɪstər/", "vi": "thủ tướng chính phủ"},
    # 62: public holiday
    {"pos": "phrase", "ipa": "/ˈpʌblɪk ˈhɑːlədeɪ/", "vi": "ngày nghỉ lễ quốc gia chính thức"},
    # 63: rain check
    {"pos": "phrase", "ipa": "/reɪn tʃɛk/", "vi": "phiếu hẹn dịp khác; lời hẹn sau"},
    # 64: religious movement
    {"pos": "phrase", "ipa": "/rɪˈlɪdʒəs ˈmuːvmənt/", "vi": "phong trào vận động tôn giáo"},
    # 65: review copy
    {"pos": "phrase", "ipa": "/rɪˈvjuː ˈkɑːpi/", "vi": "bản sách in gửi cho nhà phê bình"},
    # 66: rock rose
    {"pos": "phrase", "ipa": "/rɑːk roʊz/", "vi": "cây hoa đá hồng nham Cistus"},
    # 67: royal air force
    {"pos": "phrase", "ipa": "/ˈrɔɪəl ɛr fɔːrs/", "vi": "Không quân Hoàng gia Anh RAF"},
    # 68: safety glass
    {"pos": "phrase", "ipa": "/ˈseɪfti ɡlæs/", "vi": "kính an toàn chịu lực chống vỡ"},
    # 69: search mission
    {"pos": "phrase", "ipa": "/sɜːrtʃ ˈmɪʃn/", "vi": "nhiệm vụ tìm kiếm cứu hộ cứu nạn"},
    # 70: sense of responsibility
    {"pos": "phrase", "ipa": "/sɛns əv rɪˌspɑːnsəˈbɪləti/", "vi": "tinh thần trách nhiệm cao"},
    # 71: shop floor
    {"pos": "phrase", "ipa": "/ʃɑːp flɔːr/", "vi": "phân xưởng sản xuất nhà máy"},
    # 72: silver mine
    {"pos": "phrase", "ipa": "/ˈsɪlvər maɪn/", "vi": "mỏ khai thác quặng bạc"},
    # 73: silver standard
    {"pos": "phrase", "ipa": "/ˈsɪlvər ˈstændərd/", "vi": "chế độ bản vị bạc tiền tệ"},
    # 74: size stick
    {"pos": "phrase", "ipa": "/saɪz stɪk/", "vi": "thước đo cỡ chân đóng giày dép"},
    # 75: skin color
    {"pos": "phrase", "ipa": "/skɪn ˈkʌlər/", "vi": "màu da sắc tộc cơ thể"},
    # 76: soft news
    {"pos": "phrase", "ipa": "/sɔːft nuːz/", "vi": "tin tức giải trí đời sống"},
    # 77: southern cross
    {"pos": "phrase", "ipa": "/ˈsʌðərn krɔːs/", "vi": "chòm sao Nam Thập Tự phương Nam"},
    # 78: space medicine
    {"pos": "phrase", "ipa": "/speɪs ˈmɛdsn/", "vi": "y học hàng không vũ trụ"},
    # 79: split end
    {"pos": "phrase", "ipa": "/splɪt ɛnd/", "vi": "chứng tóc chẻ ngọn; vị trí bắt bóng"},
    # 80: split second
    {"pos": "phrase", "ipa": "/splɪt ˈsɛkənd/", "vi": "khoảnh khắc tích tắc trong chớp mắt"},
    # 81: sports equipment
    {"pos": "phrase", "ipa": "/spɔːrts ɪˈkwɪpmənt/", "vi": "trang thiết bị dụng cụ thể thao"},
    # 82: starting handle
    {"pos": "phrase", "ipa": "/ˈstɑːrtɪŋ ˈhændl/", "vi": "tay quay khởi động máy nổ cơ khí"},
    # 83: street clothes
    {"pos": "phrase", "ipa": "/striːt kloʊðz/", "vi": "quần áo thường ngày dạo phố"},
    # 84: strike hard
    {"pos": "phrase", "ipa": "/straɪk hɑːrd/", "vi": "giáng đòn sấm sét; tấn công mạnh"},
    # 85: supply officer
    {"pos": "phrase", "ipa": "/səˈplaɪ ˈɔːfɪsər/", "vi": "sĩ quan hậu cần quân nhu tiếp tế"},
    # 86: support payment
    {"pos": "phrase", "ipa": "/səˈpɔːrt ˈpeɪmənt/", "vi": "tiền trợ cấp sinh hoạt gia đình"},
    # 87: supporting fire
    {"pos": "phrase", "ipa": "/səˈpɔːrtɪŋ ˈfaɪər/", "vi": "hỏa lực chi viện; hỏa lực yểm trợ"},
    # 88: supporting players
    {"pos": "phrase", "ipa": "/səˈpɔːrtɪŋ ˈpleɪərz/", "vi": "các diễn viên phụ; nhân vật phụ"},
    # 89: supreme court
    {"pos": "phrase", "ipa": "/suːˈpriːm kɔːrt/", "vi": "Tòa án Tối cao"},
    # 90: thomas kid
    {"pos": "phrase", "ipa": "/ˈtɑːməs kɪd/", "vi": "nhà soạn kịch Thomas Kyd"},
    # 91: time signal
    {"pos": "phrase", "ipa": "/taɪm ˈsɪɡnəl/", "vi": "tín hiệu xung thời gian chuẩn"},
    # 92: trial judge
    {"pos": "phrase", "ipa": "/ˈtraɪəl dʒʌdʒ/", "vi": "thẩm phán sơ thẩm xét xử vụ án"},
    # 93: unit cell
    {"pos": "phrase", "ipa": "/ˈjuːnɪt sɛl/", "vi": "ô mạng tinh thể cơ sở"},
    # 94: us attorney general
    {"pos": "phrase", "ipa": "/juː ɛs əˈtɜːrni ˈdʒɛnrəl/", "vi": "Bộ trưởng Tư pháp Hoa Kỳ"},
    # 95: warm front
    {"pos": "phrase", "ipa": "/wɔːrm frʌnt/", "vi": "khối diện khí nóng; front nóng"},
    # 96: weak point
    {"pos": "phrase", "ipa": "/wiːk pɔɪnt/", "vi": "điểm yếu điểm sơ hở chí mạng"},
    # 97: white blood cell
    {"pos": "phrase", "ipa": "/waɪt blʌd sɛl/", "vi": "tế bào bạch cầu miễn dịch"},
    # 98: departments
    {"pos": "noun", "ipa": "/dɪˈpɑːrtmənts/", "vi": "các phòng ban; các bộ phận; các sở"},
    # 99: energies
    {"pos": "noun", "ipa": "/ˈɛnərdʒiz/", "vi": "các dạng năng lượng; nguồn sinh lực"}
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

json.dump(out_items, open("scratch/b22_r02_p5.json", "w"), ensure_ascii=False, indent=2)
print("Round 2 Part 5 reviewed successfully: 100 items saved to scratch/b22_r02_p5.json")
