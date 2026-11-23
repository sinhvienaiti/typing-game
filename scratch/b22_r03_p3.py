import json

raw_items = json.load(open("scratch/b22_r03_raw_p3.json"))

reviews = [
    # 00: machine shop
    {"pos": "phrase", "ipa": "/məˈʃiːn ʃɑːp/", "vi": "xưởng cơ khí gia công máy móc"},
    # 01: major planet
    {"pos": "phrase", "ipa": "/ˈmeɪdʒər ˈplænɪt/", "vi": "hành tinh lớn trong hệ Mặt Trời"},
    # 02: medical assistant
    {"pos": "phrase", "ipa": "/ˈmɛdɪkl əˈsɪstənt/", "vi": "trợ lý y tế; phụ tá phòng khám"},
    # 03: mental ability
    {"pos": "phrase", "ipa": "/ˈmɛntl əˈbɪləti/", "vi": "năng lực trí tuệ; khả năng tư duy"},
    # 04: military governor
    {"pos": "phrase", "ipa": "/ˈmɪlətɛri ˈɡʌvərnər/", "vi": "thống đốc quân sự"},
    # 05: moon shot
    {"pos": "phrase", "ipa": "/muːn ʃɑːt/", "vi": "dự án thám hiểm Mặt Trăng kỳ vĩ"},
    # 06: negative charge
    {"pos": "phrase", "ipa": "/ˈnɛɡətɪv tʃɑːrdʒ/", "vi": "điện tích âm"},
    # 07: night bird
    {"pos": "phrase", "ipa": "/naɪt bɜːrd/", "vi": "chim ăn đêm; người hay thức khuya"},
    # 08: night vision
    {"pos": "phrase", "ipa": "/naɪt ˈvɪʒn/", "vi": "thị lực ban đêm; kính nhìn đêm"},
    # 09: open chain
    {"pos": "phrase", "ipa": "/ˈoʊpən tʃeɪn/", "vi": "mạch hở phân tử hóa học hữu cơ"},
    # 10: passing play
    {"pos": "phrase", "ipa": "/ˈpæsɪŋ pleɪ/", "vi": "pha phối hợp chuyền bóng tấn công"},
    # 11: paying attention
    {"pos": "phrase", "ipa": "/ˈpeɪɪŋ əˈtɛnʃn/", "vi": "sự chú ý tập trung; sự lắng nghe"},
    # 12: phase change
    {"pos": "phrase", "ipa": "/feɪz tʃeɪndʒ/", "vi": "sự chuyển pha trạng thái vật chất"},
    # 13: plant disease
    {"pos": "phrase", "ipa": "/plænt dɪˈziːz/", "vi": "bệnh cây trồng hại mùa màng"},
    # 14: play false
    {"pos": "phrase", "ipa": "/pleɪ fɔːls/", "vi": "lừa dối tráo trở; chơi xấu phản bội"},
    # 15: post hole
    {"pos": "phrase", "ipa": "/poʊst hoʊl/", "vi": "hố đào chôn cột rào cọc tiêu"},
    # 16: president taylor
    {"pos": "phrase", "ipa": "/ˈprɛzədənt ˈteɪlər/", "vi": "Tổng thống Zachary Taylor"},
    # 17: primary color
    {"pos": "phrase", "ipa": "/ˈpraɪmɛri ˈkʌlər/", "vi": "màu sắc nguyên bản cơ bản gốc"},
    # 18: public debate
    {"pos": "phrase", "ipa": "/ˈpʌblɪk dɪˈbeɪt/", "vi": "cuộc tranh luận công khai"},
    # 19: public relations man
    {"pos": "phrase", "ipa": "/ˈpʌblɪk rɪˈleɪʃnz mæn/", "vi": "chuyên viên quan hệ công chúng PR"},
    # 20: race horse
    {"pos": "phrase", "ipa": "/reɪs hɔːrs/", "vi": "ngựa đua thuần chủng trường đua"},
    # 21: rain date
    {"pos": "phrase", "ipa": "/reɪn deɪt/", "vi": "ngày hoãn tổ chức dự phòng khi mưa"},
    # 22: raise hell
    {"pos": "phrase", "ipa": "/reɪz hɛl/", "vi": "gây náo loạn quậy phá; phản đối dữ"},
    # 23: rare earth
    {"pos": "phrase", "ipa": "/rɛr ɜːrθ/", "vi": "nguyên tố đất hiếm công nghệ cao"},
    # 24: red planet
    {"pos": "phrase", "ipa": "/rɛd ˈplænɪt/", "vi": "Hành tinh Đỏ Sao Hỏa"},
    # 25: richard ii
    {"pos": "phrase", "ipa": "/ˈrɪtʃərd ðə ˈsɛkənd/", "vi": "Vua Richard Đệ Nhị"},
    # 26: right wing
    {"pos": "phrase", "ipa": "/raɪt wɪŋ/", "vi": "phe cánh hữu; phe bảo thủ chính trị"},
    # 27: running suit
    {"pos": "phrase", "ipa": "/ˈrʌnɪŋ suːt/", "vi": "bộ quần áo nỉ chạy bộ thể thao"},
    # 28: safety feature
    {"pos": "phrase", "ipa": "/ˈseɪfti ˈfiːtʃər/", "vi": "tính năng an toàn bảo vệ"},
    # 29: scientific research
    {"pos": "phrase", "ipa": "/ˌsaɪənˈtɪfɪk rɪˈsɜːrtʃ/", "vi": "nghiên cứu khoa học hàn lâm"},
    # 30: search engine
    {"pos": "phrase", "ipa": "/sɜːrtʃ ˈɛndʒɪn/", "vi": "công cụ tìm kiếm trực tuyến mạng"},
    # 31: senate campaign
    {"pos": "phrase", "ipa": "/ˈsɛnət kæmˈpeɪn/", "vi": "chiến dịch tranh cử Thượng viện"},
    # 32: senior status
    {"pos": "phrase", "ipa": "/ˈsiːnjər ˈsteɪtəs/", "vi": "chế độ thẩm phán bán về hưu"},
    # 33: sense of duty
    {"pos": "phrase", "ipa": "/sɛns əv ˈduːti/", "vi": "tinh thần trách nhiệm bổn phận"},
    # 34: shooting box
    {"pos": "phrase", "ipa": "/ˈʃuːtɪŋ bɑːks/", "vi": "chòi săn bắn động vật mùa săn"},
    # 35: skin cell
    {"pos": "phrase", "ipa": "/skɪn sɛl/", "vi": "tế bào da biểu bì"},
    # 36: skin pop
    {"pos": "phrase", "ipa": "/skɪn pɑːp/", "vi": "tiêm ma túy dưới da nông"},
    # 37: social democratic party
    {"pos": "phrase", "ipa": "/ˈsoʊʃl ˌdɛməˈkrætɪk ˈpɑːrti/", "vi": "Đảng Dân chủ Xã hội"},
    # 38: solid ground
    {"pos": "phrase", "ipa": "/ˈsɑːlɪd ɡraʊnd/", "vi": "nền đất vững chắc; cơ sở vững vàng"},
    # 39: split run
    {"pos": "phrase", "ipa": "/splɪt rʌn/", "vi": "bản in quảng cáo phân vùng"},
    # 40: squad room
    {"pos": "phrase", "ipa": "/skwɑːd ruːm/", "vi": "phòng giao ban cảnh sát điều tra"},
    # 41: stand guard
    {"pos": "phrase", "ipa": "/stænd ɡɑːrd/", "vi": "đứng gác tuần tra cảnh giới"},
    # 42: state supreme court
    {"pos": "phrase", "ipa": "/steɪt suːˈpriːm kɔːrt/", "vi": "Tòa án Tối cao tiểu bang"},
    # 43: steel industry
    {"pos": "phrase", "ipa": "/stiːl ˈɪndəstri/", "vi": "ngành công nghiệp luyện kim thép"},
    # 44: stick figure
    {"pos": "phrase", "ipa": "/stɪk ˈfɪɡjər/", "vi": "hình vẽ người que cách điệu"},
    # 45: stock exchange
    {"pos": "phrase", "ipa": "/stɑːk ɪksˈtʃeɪndʒ/", "vi": "sở giao dịch chứng khoán"},
    # 46: strike pay
    {"pos": "phrase", "ipa": "/straɪk peɪ/", "vi": "tiền trợ cấp đình công công đoàn"},
    # 47: strong suit
    {"pos": "phrase", "ipa": "/strɔːŋ suːt/", "vi": "sở trường thế mạnh; bộ bài mạnh"},
    # 48: sun rose
    {"pos": "phrase", "ipa": "/sʌn roʊz/", "vi": "cây hoa đá mặt trời Helianthemum"},
    # 49: surprise attack
    {"pos": "phrase", "ipa": "/sərˈpraɪz əˈtæk/", "vi": "cuộc tấn công bất ngờ tập kích"},
    # 50: sweet william
    {"pos": "phrase", "ipa": "/swiːt ˈwɪljəm/", "vi": "hoa cẩm chướng thơm rực rỡ"},
    # 51: switch over
    {"pos": "phrase", "ipa": "/swɪtʃ ˈoʊvər/", "vi": "chuyển đổi phương thức sang"},
    # 52: systems software
    {"pos": "phrase", "ipa": "/ˈsɪstəmz ˈsɔːftwɛr/", "vi": "phần mềm hệ thống máy tính"},
    # 53: take for granted
    {"pos": "phrase", "ipa": "/teɪk fɔːr ˈɡræntɪd/", "vi": "coi là điều hiển nhiên"},
    # 54: television station
    {"pos": "phrase", "ipa": "/ˈtɛləvɪʒn ˈsteɪʃn/", "vi": "đài phát thanh truyền hình"},
    # 55: temperature change
    {"pos": "phrase", "ipa": "/ˈtɛmprətʃər tʃeɪndʒ/", "vi": "sự biến đổi dao động nhiệt độ"},
    # 56: testing room
    {"pos": "phrase", "ipa": "/ˈtɛstɪŋ ruːm/", "vi": "phòng thử nghiệm kiểm tra"},
    # 57: text edition
    {"pos": "phrase", "ipa": "/tɛkst ɪˈdɪʃn/", "vi": "sách giáo khoa dùng giảng dạy"},
    # 58: thousand times
    {"pos": "phrase", "ipa": "/ˈθaʊznd taɪmz/", "vi": "ngàn lần; gấp muôn vạn lần"},
    # 59: time bomb
    {"pos": "phrase", "ipa": "/taɪm bɑːm/", "vi": "bom nổ chậm; hiểm họa tiềm tàng"},
    # 60: trade magazine
    {"pos": "phrase", "ipa": "/treɪd ˌmæɡəˈziːn/", "vi": "tạp chí chuyên ngành thương mại"},
    # 61: traditional knowledge
    {"pos": "phrase", "ipa": "/trəˈdɪʃənl ˈnɑːlɪdʒ/", "vi": "tri thức bản địa truyền thống"},
    # 62: transfer of training
    {"pos": "phrase", "ipa": "/trænsˈfɜːr əv ˈtreɪnɪŋ/", "vi": "sự chuyển giao kỹ năng đào tạo"},
    # 63: travel agent
    {"pos": "phrase", "ipa": "/ˈtrævl ˈeɪdʒənt/", "vi": "đại lý môi giới lữ hành du lịch"},
    # 64: truck stop
    {"pos": "phrase", "ipa": "/trʌk stɑːp/", "vi": "trạm dừng nghỉ chân xe tải xa lộ"},
    # 65: urban area
    {"pos": "phrase", "ipa": "/ˈɜːrbən ˈɛriə/", "vi": "khu vực thành thị đô thị hóa"},
    # 66: web page
    {"pos": "phrase", "ipa": "/wɛb peɪdʒ/", "vi": "trang web mạng điện tử"},
    # 67: wild ass
    {"pos": "phrase", "ipa": "/waɪld æs/", "vi": "con lừa hoang dã thảo nguyên"},
    # 68: word of honor
    {"pos": "phrase", "ipa": "/wɜːrd əv ˈɑːnər/", "vi": "lời hứa danh dự uy tín"},
    # 69: work papers
    {"pos": "phrase", "ipa": "/wɜːrk ˈpeɪpərz/", "vi": "hồ sơ giấy tờ lao động kiểm toán"},
    # 70: accounted
    {"pos": "verb", "ipa": "/əˈkaʊntɪd/", "vi": "đã giải trình; đã chiếm tỷ lệ"},
    # 71: junes
    {"pos": "noun", "ipa": "/dʒuːnz/", "vi": "những tháng Sáu mùa hè"},
    # 72: periods
    {"pos": "noun", "ipa": "/ˈpɪriədz/", "vi": "các giai đoạn thời kỳ; chu kỳ kinh"},
    # 73: totaling
    {"pos": "verb", "ipa": "/ˈtoʊtəlɪŋ/", "vi": "đang tổng cộng; lên tới con số"},
    # 74: air hole
    {"pos": "phrase", "ipa": "/ɛr hoʊl/", "vi": "lỗ thông khí; túi khí hẫng máy bay"},
    # 75: american black bear
    {"pos": "phrase", "ipa": "/əˈmɛrɪkən blæk bɛr/", "vi": "gấu đen Bắc Mỹ Ursus americanus"},
    # 76: at random
    {"pos": "phrase", "ipa": "/æt ˈrændəm/", "vi": "ngẫu nhiên bất kỳ; tùy hứng"},
    # 77: birthday card
    {"pos": "phrase", "ipa": "/ˈbɜːrθdeɪ kɑːrd/", "vi": "thiệp chúc mừng sinh nhật"},
    # 78: blood sport
    {"pos": "phrase", "ipa": "/blʌd spɔːrt/", "vi": "môn thể thao săn bắn đẫm máu"},
    # 79: blow out
    {"pos": "phrase", "ipa": "/bloʊ aʊt/", "vi": "thổi tắt nến; nổ lốp xe đột ngột"},
    # 80: blow over
    {"pos": "phrase", "ipa": "/bloʊ ˈoʊvər/", "vi": "qua đi lắng dịu; tiêu tan sóng gió"},
    # 81: blow up
    {"pos": "phrase", "ipa": "/bloʊ ʌp/", "vi": "nổ tung phát nổ; nổi trận lôi đình"},
    # 82: blue sky
    {"pos": "phrase", "ipa": "/bluː skaɪ/", "vi": "bầu trời xanh biếc; ý tưởng mở"},
    # 83: call the shots
    {"pos": "phrase", "ipa": "/kɔːl ðə ʃɑːts/", "vi": "nắm quyền ra quyết định chi phối"},
    # 84: carry nation
    {"pos": "phrase", "ipa": "/ˈkæri ˈneɪʃn/", "vi": "nhà cải cách Carry Nation"},
    # 85: charles ii
    {"pos": "phrase", "ipa": "/tʃɑːrlz ðə ˈsɛkənd/", "vi": "Vua Charles Đệ Nhị"},
    # 86: charles river
    {"pos": "phrase", "ipa": "/tʃɑːrlz ˈrɪvər/", "vi": "sông Charles ở Boston"},
    # 87: christmas tree
    {"pos": "phrase", "ipa": "/ˈkrɪsməs triː/", "vi": "cây thông trang trí Giáng sinh"},
    # 88: city editor
    {"pos": "phrase", "ipa": "/ˈsɪti ˈɛdɪtər/", "vi": "biên tập viên thời sự địa phương"},
    # 89: community of interests
    {"pos": "phrase", "ipa": "/kəˈmjuːnəti əv ˈɪntrəsts/", "vi": "cộng đồng chung quyền lợi"},
    # 90: computer memory
    {"pos": "phrase", "ipa": "/kəmˈpjuːtər ˈmɛməri/", "vi": "bộ nhớ RAM máy tính"},
    # 91: concept album
    {"pos": "phrase", "ipa": "/ˈkɑːnsɛpt ˈælbəm/", "vi": "album nhạc theo chủ đề xuyên suốt"},
    # 92: contact mike
    {"pos": "phrase", "ipa": "/ˈkɑːntækt maɪk/", "vi": "micro tiếp xúc thu rung động"},
    # 93: crew member
    {"pos": "phrase", "ipa": "/kruː ˈmɛmbər/", "vi": "thành viên tổ lái; thủy thủ đoàn"},
    # 94: cry out
    {"pos": "phrase", "ipa": "/kraɪ aʊt/", "vi": "hét to la lối thất thanh đau đớn"},
    # 95: cry out for
    {"pos": "phrase", "ipa": "/kraɪ aʊt fɔːr/", "vi": "rất cần kíp; khẩn thiết đòi hỏi"},
    # 96: cup of tea
    {"pos": "phrase", "ipa": "/kʌp əv tiː/", "vi": "tách trà nóng; sở thích cá nhân"},
    # 97: dark horse
    {"pos": "phrase", "ipa": "/dɑːrk hɔːrs/", "vi": "ngựa ô nhân tố bất ngờ khó đoán"},
    # 98: direct flight
    {"pos": "phrase", "ipa": "/dəˈrɛkt flaɪt/", "vi": "chuyến bay thẳng không đổi máy bay"},
    # 99: display case
    {"pos": "phrase", "ipa": "/dɪˈspleɪ keɪs/", "vi": "tủ kính trưng bày bảo tàng"}
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

json.dump(out_items, open("scratch/b22_r03_p3.json", "w"), ensure_ascii=False, indent=2)
print("Round 3 Part 3 reviewed successfully: 100 items saved to scratch/b22_r03_p3.json")
