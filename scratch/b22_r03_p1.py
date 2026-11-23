import json

raw_items = json.load(open("scratch/b22_r03_raw_p1.json"))

reviews = [
    # 00: fights
    {"pos": "noun", "ipa": "/faɪts/", "vi": "các trận đánh; các cuộc ẩu đả"},
    # 01: hears
    {"pos": "verb", "ipa": "/hɪrz/", "vi": "nghe thấy; lắng nghe; tiếp nhận"},
    # 02: prices
    {"pos": "noun", "ipa": "/ˈpraɪsɪz/", "vi": "các mức giá cả; biểu giá thị trường"},
    # 03: air flow
    {"pos": "phrase", "ipa": "/ɛr floʊ/", "vi": "luồng không khí; lưu lượng gió"},
    # 04: air transport
    {"pos": "phrase", "ipa": "/ɛr ˈtrænspɔːrt/", "vi": "vận tải hàng không; giao thông bay"},
    # 05: alternative energy
    {"pos": "phrase", "ipa": "/ɔːlˈtɜːrnətɪv ˈɛnərdʒi/", "vi": "nguồn năng lượng thay thế"},
    # 06: ancient history
    {"pos": "phrase", "ipa": "/ˈeɪnʃənt ˈhɪstəri/", "vi": "lịch sử cổ đại; chuyện dĩ vãng"},
    # 07: balance of trade
    {"pos": "phrase", "ipa": "/ˈbæləns əv treɪd/", "vi": "cán cân thương mại xuất nhập khẩu"},
    # 08: bank martin
    {"pos": "phrase", "ipa": "/bæŋk ˈmɑːrtn/", "vi": "chim nhạn cát bờ sông Riparia"},
    # 09: basic color
    {"pos": "phrase", "ipa": "/ˈbeɪsɪk ˈkʌlər/", "vi": "màu cơ bản; thuốc nhuộm gốc bazơ"},
    # 10: beat generation
    {"pos": "phrase", "ipa": "/biːt ˌdʒɛnəˈreɪʃn/", "vi": "thế hệ Beat văn học Mỹ"},
    # 11: black fox
    {"pos": "phrase", "ipa": "/blæk fɑːks/", "vi": "con cáo đen lông bạc"},
    # 12: black hole
    {"pos": "phrase", "ipa": "/blæk hoʊl/", "vi": "hố đen vũ trụ; lỗ đen không gian"},
    # 13: black muslim
    {"pos": "phrase", "ipa": "/blæk ˈmʊzlɪm/", "vi": "tín đồ Hồi giáo da đen Mỹ"},
    # 14: blame game
    {"pos": "phrase", "ipa": "/bleɪm ɡeɪm/", "vi": "trò đổ lỗi; đùn đẩy trách nhiệm"},
    # 15: bob around
    {"pos": "phrase", "ipa": "/bɑːb əˈraʊnd/", "vi": "nhấp nhô bồng bềnh xung quanh"},
    # 16: bob under
    {"pos": "phrase", "ipa": "/bɑːb ˈʌndər/", "vi": "chìm lỉm dưới nước; lặn thụt xuống"},
    # 17: brain cell
    {"pos": "phrase", "ipa": "/breɪn sɛl/", "vi": "tế bào não bộ; tế bào thần kinh"},
    # 18: breakfast time
    {"pos": "phrase", "ipa": "/ˈbrɛkfəst taɪm/", "vi": "giờ ăn điểm tâm sáng"},
    # 19: bring to bear
    {"pos": "phrase", "ipa": "/brɪŋ tuː bɛr/", "vi": "vận dụng tối đa; gây sức ép lớn"},
    # 20: cancer cell
    {"pos": "phrase", "ipa": "/ˈkænsər sɛl/", "vi": "tế bào ung thư ác tính"},
    # 21: cancer drug
    {"pos": "phrase", "ipa": "/ˈkænsər drʌɡ/", "vi": "thuốc đặc trị ung thư hóa trị"},
    # 22: capital gain
    {"pos": "phrase", "ipa": "/ˈkæpɪtl ɡeɪn/", "vi": "lợi tức vốn; lãi vốn đầu tư"},
    # 23: car pool
    {"pos": "phrase", "ipa": "/kɑːr puːl/", "vi": "nhóm đi chung xe ô tô; đi chung xe"},
    # 24: carrying out
    {"pos": "phrase", "ipa": "/ˈkæriɪŋ aʊt/", "vi": "việc thực hiện thi hành kế hoạch"},
    # 25: change owners
    {"pos": "phrase", "ipa": "/tʃeɪndʒ ˈoʊnərz/", "vi": "đổi chủ sở hữu; chuyển quyền sở hữu"},
    # 26: chicken little
    {"pos": "phrase", "ipa": "/ˈtʃɪkɪn ˈlɪtl/", "vi": "chú gà Chicken Little; kẻ lo xa"},
    # 27: chief financial officer
    {"pos": "phrase", "ipa": "/tʃiːf faɪˈnænʃl ˈɔːfɪsər/", "vi": "giám đốc tài chính CFO"},
    # 28: chosen people
    {"pos": "phrase", "ipa": "/ˈtʃoʊzn ˈpiːpl/", "vi": "dân tuyển của Chúa; dân Do Thái"},
    # 29: christmas disease
    {"pos": "phrase", "ipa": "/ˈkrɪsməs dɪˈziːz/", "vi": "bệnh máu khó đông B Christmas"},
    # 30: coffee bar
    {"pos": "phrase", "ipa": "/ˈkɔːfi bɑːr/", "vi": "quầy pha cà phê; quán cà phê nhỏ"},
    # 31: context of use
    {"pos": "phrase", "ipa": "/ˈkɑːntɛkst əv juːs/", "vi": "bối cảnh sử dụng; ngữ cảnh áp dụng"},
    # 32: cream off
    {"pos": "phrase", "ipa": "/kriːm ɔːf/", "vi": "hớt lấy phần tinh túy nhất"},
    # 33: current intelligence
    {"pos": "phrase", "ipa": "/ˈkɜːrənt ɪnˈtɛlɪdʒəns/", "vi": "thông tin tình báo thời sự cập nhật"},
    # 34: cutting out
    {"pos": "phrase", "ipa": "/ˈkʌtɪŋ aʊt/", "vi": "sự cắt rời; phẫu thuật cắt bỏ"},
    # 35: cycle on
    {"pos": "phrase", "ipa": "/ˈsaɪkl ɑːn/", "vi": "quay lại điểm đầu chu kỳ hoạt động"},
    # 36: dance hall
    {"pos": "phrase", "ipa": "/dæns hɔːl/", "vi": "vũ trường khiêu vũ; phòng nhảy"},
    # 37: death squad
    {"pos": "phrase", "ipa": "/dɛθ skwɑːd/", "vi": "biệt đội tử thần; đội ám sát bí mật"},
    # 38: degree of freedom
    {"pos": "phrase", "ipa": "/dɪˈɡriː əv ˈfriːdəm/", "vi": "bậc tự do trong thống kê cơ học"},
    # 39: desire to know
    {"pos": "phrase", "ipa": "/dɪˈzaɪər tuː noʊ/", "vi": "sự khao khát hiểu biết; tính tò mò"},
    # 40: developing country
    {"pos": "phrase", "ipa": "/dɪˈvɛləpɪŋ ˈkʌntri/", "vi": "quốc gia đang phát triển"},
    # 41: double agent
    {"pos": "phrase", "ipa": "/ˈdʌbl ˈeɪdʒənt/", "vi": "điệp viên hai mang; gián điệp 2 mặt"},
    # 42: double feature
    {"pos": "phrase", "ipa": "/ˈdʌbl ˈfiːtʃər/", "vi": "buổi chiếu hai phim liền một vé"},
    # 43: drinking song
    {"pos": "phrase", "ipa": "/ˈdrɪŋkɪŋ sɔːŋ/", "vi": "bài ca bàn rượu; khúc hát nâng ly"},
    # 44: extended family
    {"pos": "phrase", "ipa": "/ɪkˈstɛndɪd ˈfæməli/", "vi": "đại gia đình nhiều thế hệ"},
    # 45: fair hearing
    {"pos": "phrase", "ipa": "/fɛr ˈhɪrɪŋ/", "vi": "phiên điều trần xét xử công bằng"},
    # 46: farm bill
    {"pos": "phrase", "ipa": "/fɑːrm bɪl/", "vi": "dự luật phát triển nông nghiệp Mỹ"},
    # 47: field capacity
    {"pos": "phrase", "ipa": "/fiːld kəˈpæsəti/", "vi": "độ ẩm đồng ruộng tối đa giữ nước"},
    # 48: fill again
    {"pos": "phrase", "ipa": "/fɪl əˈɡɛn/", "vi": "rót đầy lại; bổ sung cho đầy"},
    # 49: film festival
    {"pos": "phrase", "ipa": "/fɪlm ˈfɛstəvl/", "vi": "liên hoan phim điện ảnh"},
    # 50: finance company
    {"pos": "phrase", "ipa": "/ˈfaɪnæns ˈkʌmpəni/", "vi": "công ty tài chính cho vay tiêu dùng"},
    # 51: fish doctor
    {"pos": "phrase", "ipa": "/fɪʃ ˈdɑːktər/", "vi": "bác sĩ thú y chữa bệnh cho cá"},
    # 52: florida key
    {"pos": "phrase", "ipa": "/ˈflɔːrədə kiː/", "vi": "đảo đá ngầm san hô Florida Keys"},
    # 53: flow of air
    {"pos": "phrase", "ipa": "/floʊ əv ɛr/", "vi": "luồng không khí; dòng đối lưu gió"},
    # 54: flying field
    {"pos": "phrase", "ipa": "/ˈflaɪɪŋ fiːld/", "vi": "sân bay dã chiến nhỏ; bãi cất cánh"},
    # 55: foot rule
    {"pos": "phrase", "ipa": "/fʊt ruːl/", "vi": "thước đo một foot dài 12 inch"},
    # 56: forced sale
    {"pos": "phrase", "ipa": "/fɔːrst seɪl/", "vi": "bán tháo tài sản phát mại cưỡng chế"},
    # 57: forest fire
    {"pos": "phrase", "ipa": "/ˈfɔːrɪst ˈfaɪər/", "vi": "vụ cháy rừng thảm khốc; cháy rừng"},
    # 58: game bird
    {"pos": "phrase", "ipa": "/ɡeɪm bɜːrd/", "vi": "chim săn hoang dã; chim thịt săn"},
    # 59: gas ring
    {"pos": "phrase", "ipa": "/ɡæs rɪŋ/", "vi": "vòng kiềng bếp gas ngọn lửa"},
    # 60: hang in
    {"pos": "phrase", "ipa": "/hæŋ ɪn/", "vi": "kiên trì cố gắng; không nản lòng"},
    # 61: hang on
    {"pos": "phrase", "ipa": "/hæŋ ɑːn/", "vi": "chờ máy một lát; bám chặt lấy"},
    # 62: heat unit
    {"pos": "phrase", "ipa": "/hiːt ˈjuːnɪt/", "vi": "đơn vị nhiệt lượng calo BTU"},
    # 63: holiday season
    {"pos": "phrase", "ipa": "/ˈhɑːlədeɪ ˈsiːzn/", "vi": "mùa nghỉ lễ cuối năm; mùa lễ hội"},
    # 64: horse trade
    {"pos": "phrase", "ipa": "/hɔːrs treɪd/", "vi": "thương lượng ngã giá căng thẳng"},
    # 65: independent agency
    {"pos": "phrase", "ipa": "/ˌɪndɪˈpɛndənt ˈeɪdʒənsi/", "vi": "cơ quan độc lập thuộc chính phủ"},
    # 66: industrial process
    {"pos": "phrase", "ipa": "/ɪnˈdʌstriəl ˈprɑːsɛs/", "vi": "quy trình công nghệ sản xuất"},
    # 67: japanese capital
    {"pos": "phrase", "ipa": "/ˌdʒæpəˈniːz ˈkæpɪtl/", "vi": "thủ đô nước Nhật; Tokyo"},
    # 68: job candidate
    {"pos": "phrase", "ipa": "/dʒɑːb ˈkændɪdeɪt/", "vi": "ứng viên ứng tuyển việc làm"},
    # 69: just the ticket
    {"pos": "phrase", "ipa": "/dʒʌst ðə ˈtɪkɪt/", "vi": "đúng thứ cần tìm; đúng nguyện vọng"},
    # 70: labor union
    {"pos": "phrase", "ipa": "/ˈleɪbər ˈjuːnjən/", "vi": "công đoàn; tổ chức nghiệp đoàn"},
    # 71: laugh line
    {"pos": "phrase", "ipa": "/læf laɪn/", "vi": "nếp nhăn khóe cười; rãnh cười"},
    # 72: lay away
    {"pos": "phrase", "ipa": "/leɪ əˈweɪ/", "vi": "đặt cọc giữ hàng; để dành tiết kiệm"},
    # 73: liberal party
    {"pos": "phrase", "ipa": "/ˈlɪbərəl ˈpɑːrti/", "vi": "Đảng Tự do chính trị"},
    # 74: limited edition
    {"pos": "phrase", "ipa": "/ˈlɪmɪtɪd ɪˈdɪʃn/", "vi": "ấn bản giới hạn; phiên bản giới hạn"},
    # 75: line storm
    {"pos": "phrase", "ipa": "/laɪn stɔːrm/", "vi": "bão lốc điểm phân thu xuân"},
    # 76: loan office
    {"pos": "phrase", "ipa": "/loʊn ˈɔːfɪs/", "vi": "văn phòng cho vay; hiệu cầm đồ"},
    # 77: major suit
    {"pos": "phrase", "ipa": "/ˈmeɪdʒər suːt/", "vi": "chất bích và cơ trong bài bridge"},
    # 78: meat house
    {"pos": "phrase", "ipa": "/miːt haʊs/", "vi": "nhà xông khói ướp thịt gia đình"},
    # 79: military plane
    {"pos": "phrase", "ipa": "/ˈmɪlətɛri pleɪn/", "vi": "máy bay chiến đấu quân sự"},
    # 80: national holiday
    {"pos": "phrase", "ipa": "/ˈnæʃnəl ˈhɑːlədeɪ/", "vi": "ngày quốc khánh; ngày quốc lễ"},
    # 81: near beer
    {"pos": "phrase", "ipa": "/nɪr bɪr/", "vi": "bia nồng độ cồn cực thấp không say"},
    # 82: nuclear club
    {"pos": "phrase", "ipa": "/ˈnuːkliər klʌb/", "vi": "nhóm quốc gia có vũ khí hạt nhân"},
    # 83: ocean current
    {"pos": "phrase", "ipa": "/ˈoʊʃn ˈkɜːrənt/", "vi": "dòng hải lưu đại dương; dòng biển"},
    # 84: order of payment
    {"pos": "phrase", "ipa": "/ˈɔːrdər əv ˈpeɪmənt/", "vi": "lệnh ủy nhiệm chi; lệnh thanh toán"},
    # 85: pack together
    {"pos": "phrase", "ipa": "/pæk təˈɡɛðər/", "vi": "xếp nén chặt vào nhau; bó cụm lại"},
    # 86: passing game
    {"pos": "phrase", "ipa": "/ˈpæsɪŋ ɡeɪm/", "vi": "lối chơi phối hợp chuyền bóng ngắn"},
    # 87: personal matters
    {"pos": "phrase", "ipa": "/ˈpɜːrsənl ˈmætərz/", "vi": "chuyện đời tư cá nhân; việc riêng"},
    # 88: physical condition
    {"pos": "phrase", "ipa": "/ˈfɪzɪkl kənˈdɪʃn/", "vi": "thể trạng; tình trạng thể chất"},
    # 89: pick apart
    {"pos": "phrase", "ipa": "/pɪk əˈpɑːrt/", "vi": "bới móc mổ xẻ khuyết điểm"},
    # 90: planned community
    {"pos": "phrase", "ipa": "/plænd kəˈmjuːnəti/", "vi": "khu đô thị dân cư quy hoạch bài bản"},
    # 91: planning commission
    {"pos": "phrase", "ipa": "/ˈplænɪŋ kəˈmɪʃn/", "vi": "ủy ban quy hoạch kiến thiết đô thị"},
    # 92: population profile
    {"pos": "phrase", "ipa": "/ˌpɑːpjuˈleɪʃn ˈproʊfaɪl/", "vi": "hồ sơ cơ cấu nhân khẩu học dân số"},
    # 93: power pack
    {"pos": "phrase", "ipa": "/ˈpaʊər pæk/", "vi": "bộ pin sạc nguồn điện lưu động"},
    # 94: president grant
    {"pos": "phrase", "ipa": "/ˈprɛzədənt ɡrænt/", "vi": "Tổng thống Ulysses S. Grant"},
    # 95: pull ahead
    {"pos": "phrase", "ipa": "/pʊl əˈhɛd/", "vi": "vươn lên dẫn đầu; bứt phá dẫn trước"},
    # 96: purchase price
    {"pos": "phrase", "ipa": "/ˈpɜːrtʃəs praɪs/", "vi": "giá mua vào; giá cả thanh toán mua"},
    # 97: quarter rest
    {"pos": "phrase", "ipa": "/ˈkwɔːrtər rɛst/", "vi": "dấu lặng đen trong khuông nhạc"},
    # 98: ray of light
    {"pos": "phrase", "ipa": "/reɪ əv laɪt/", "vi": "tia sáng rọi; tia hy vọng mong manh"},
    # 99: religious leader
    {"pos": "phrase", "ipa": "/rɪˈlɪdʒəs ˈliːdər/", "vi": "vị chức sắc lãnh đạo tôn giáo"}
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

json.dump(out_items, open("scratch/b22_r03_p1.json", "w"), ensure_ascii=False, indent=2)
print("Round 3 Part 1 reviewed successfully: 100 items saved to scratch/b22_r03_p1.json")
