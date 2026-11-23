import json

raw_items = json.load(open("scratch/b22_r01_raw_p5.json"))

reviews = [
    # 00: summer camp
    {"pos": "phrase", "ipa": "/ˈsʌmər kæmp/", "vi": "trại hè; khu cắm trại mùa hè"},
    # 01: tea party
    {"pos": "phrase", "ipa": "/tiː ˈpɑːrti/", "vi": "tiệc trà; phong trào Tiệc Trà"},
    # 02: tea service
    {"pos": "phrase", "ipa": "/tiː ˈsɜːrvɪs/", "vi": "bộ ấm chén pha trà; bộ đồ uống trà"},
    # 03: tour de force
    {"pos": "phrase", "ipa": "/ˌtʊər də ˈfɔːrs/", "vi": "kiệt tác; kỳ công phi thường"},
    # 04: trade protection
    {"pos": "phrase", "ipa": "/treɪd prəˈtɛkʃn/", "vi": "bảo hộ thương mại; bảo hộ mậu dịch"},
    # 05: trade wind
    {"pos": "phrase", "ipa": "/treɪd wɪnd/", "vi": "gió mậu dịch; gió tín phong"},
    # 06: turning away
    {"pos": "phrase", "ipa": "/ˈtɜːrnɪŋ əˈweɪ/", "vi": "sự quay lưng; sự từ chối né tránh"},
    # 07: water sport
    {"pos": "phrase", "ipa": "/ˈwɔːtər spɔːrt/", "vi": "thể thao dưới nước; môn dưới nước"},
    # 08: work flow
    {"pos": "phrase", "ipa": "/wɜːrk floʊ/", "vi": "quy trình làm việc; luồng công việc"},
    # 09: behinds
    {"pos": "noun", "ipa": "/bɪˈhaɪndz/", "vi": "phần mông; những chỗ kín phía sau"},
    # 10: easied
    {"pos": "verb", "ipa": "/ˈiːzid/", "vi": "đã làm dịu bớt; đã nới lỏng"},
    # 11: sixes
    {"pos": "noun", "ipa": "/ˈsɪksɪz/", "vi": "những con số sáu; các quân sáu"},
    # 12: agent bank
    {"pos": "phrase", "ipa": "/ˈeɪdʒənt bæŋk/", "vi": "ngân hàng đại lý; ngân hàng đầu mối"},
    # 13: american plane
    {"pos": "phrase", "ipa": "/əˈmɛrɪkən pleɪn/", "vi": "cây tiêu huyền Mỹ"},
    # 14: bank holding company
    {"pos": "phrase", "ipa": "/bæŋk ˈhoʊldɪŋ ˈkʌmpəni/", "vi": "công ty cổ phần ngân hàng"},
    # 15: base of operations
    {"pos": "phrase", "ipa": "/beɪs əv ˌɑːpəˈreɪʃnz/", "vi": "căn cứ tác chiến; căn cứ chỉ huy"},
    # 16: be quiet
    {"pos": "phrase", "ipa": "/biː ˈkwaɪət/", "vi": "hãy giữ trật tự; im lặng nào"},
    # 17: big ben
    {"pos": "phrase", "ipa": "/bɪɡ bɛn/", "vi": "tháp đồng hồ Big Ben London"},
    # 18: black prince
    {"pos": "phrase", "ipa": "/blæk prɪns/", "vi": "Hoàng tử Đen Edward xứ Wales"},
    # 19: blue jack
    {"pos": "phrase", "ipa": "/bluː dʒæk/", "vi": "cá khế vây xanh; cây sồi xanh"},
    # 20: body guard
    {"pos": "phrase", "ipa": "/ˈbɑːdi ɡɑːrd/", "vi": "vệ sĩ riêng; cận vệ bảo vệ"},
    # 21: bottom dog
    {"pos": "phrase", "ipa": "/ˈbɑːtəm dɔːɡ/", "vi": "kẻ yếm thế; người dưới đáy xã hội"},
    # 22: box camera
    {"pos": "phrase", "ipa": "/bɑːks ˈkæmərə/", "vi": "máy ảnh hộp cổ điển"},
    # 23: building supply house
    {"pos": "phrase", "ipa": "/ˈbɪldɪŋ səˈplaɪ haʊs/", "vi": "cửa hàng vật liệu xây dựng"},
    # 24: buy the farm
    {"pos": "phrase", "ipa": "/baɪ ðə fɑːrm/", "vi": "thiệt mạng; tử trận; qua đời"},
    # 25: car port
    {"pos": "phrase", "ipa": "/kɑːr pɔːrt/", "vi": "mái che để xe; nhà để xe mở"},
    # 26: carry weight
    {"pos": "phrase", "ipa": "/ˈkæri weɪt/", "vi": "có ảnh hưởng lớn; có trọng lượng"},
    # 27: cell wall
    {"pos": "phrase", "ipa": "/sɛl wɔːl/", "vi": "thành tế bào; vách tế bào"},
    # 28: century plant
    {"pos": "phrase", "ipa": "/ˈsɛntʃəri plænt/", "vi": "cây thùa Mỹ Agave"},
    # 29: city limit
    {"pos": "phrase", "ipa": "/ˈsɪti ˈlɪmɪt/", "vi": "ranh giới thành phố; địa giới"},
    # 30: climate change
    {"pos": "phrase", "ipa": "/ˈklaɪmət tʃeɪndʒ/", "vi": "biến đổi khí hậu toàn cầu"},
    # 31: cover glass
    {"pos": "phrase", "ipa": "/ˈkʌvər ɡlæs/", "vi": "lamen; kính đậy tiêu bản"},
    # 32: critical review
    {"pos": "phrase", "ipa": "/ˈkrɪtɪkl rɪˈvjuː/", "vi": "bài phê bình; bài thẩm định"},
    # 33: data file
    {"pos": "phrase", "ipa": "/ˈdeɪtə faɪl/", "vi": "tệp dữ liệu; tập tin dữ liệu"},
    # 34: domestic help
    {"pos": "phrase", "ipa": "/dəˈmɛstɪk hɛlp/", "vi": "người giúp việc gia đình; người làm"},
    # 35: drinking water
    {"pos": "phrase", "ipa": "/ˈdrɪŋkɪŋ ˈwɔːtər/", "vi": "nước uống sinh hoạt; nước sạch"},
    # 36: electric car
    {"pos": "phrase", "ipa": "/ɪˈlɛktrɪk kɑːr/", "vi": "xe ô tô điện; xe chạy điện"},
    # 37: end user
    {"pos": "phrase", "ipa": "/ɛnd ˈjuːzər/", "vi": "người dùng cuối"},
    # 38: equal to
    {"pos": "phrase", "ipa": "/ˈiːkwəl tuː/", "vi": "bằng với; đủ sức đương đầu"},
    # 39: estate tax
    {"pos": "phrase", "ipa": "/ɪˈsteɪt tæks/", "vi": "thuế di sản thừa kế"},
    # 40: face guard
    {"pos": "phrase", "ipa": "/feɪs ɡɑːrd/", "vi": "mặt nạ bảo hộ; lưới che chắn mặt"},
    # 41: falling out
    {"pos": "phrase", "ipa": "/ˈfɔːlɪŋ aʊt/", "vi": "sự bất hòa; cuộc tranh cãi rạn nứt"},
    # 42: fashion model
    {"pos": "phrase", "ipa": "/ˈfæʃn ˈmɑːdl/", "vi": "người mẫu thời trang"},
    # 43: feed back
    {"pos": "phrase", "ipa": "/fiːd bæk/", "vi": "phản hồi ý kiến; cấp dữ liệu ngược"},
    # 44: flying start
    {"pos": "phrase", "ipa": "/ˈflaɪɪŋ stɑːrt/", "vi": "sự khởi đầu thuận lợi rực rỡ"},
    # 45: food web
    {"pos": "phrase", "ipa": "/fuːd wɛb/", "vi": "lưới thức ăn sinh thái"},
    # 46: football score
    {"pos": "phrase", "ipa": "/ˈfʊtbɔːl skɔːr/", "vi": "tỷ số trận đấu bóng đá"},
    # 47: foreign exchange
    {"pos": "phrase", "ipa": "/ˈfɔːrən ɪksˈtʃeɪndʒ/", "vi": "thị trường ngoại hối; đổi ngoại tệ"},
    # 48: forest god
    {"pos": "phrase", "ipa": "/ˈfɔːrɪst ɡɑːd/", "vi": "thần rừng; sơn thần"},
    # 49: forget me drug
    {"pos": "phrase", "ipa": "/fərˈɡɛt miː drʌɡ/", "vi": "thuốc mê làm mất trí nhớ tạm thời"},
    # 50: four hundred
    {"pos": "phrase", "ipa": "/fɔːr ˈhʌndrəd/", "vi": "bốn trăm"},
    # 51: fuel line
    {"pos": "phrase", "ipa": "/ˈfjuːəl laɪn/", "vi": "đường ống dẫn nhiên liệu xe"},
    # 52: gain ground
    {"pos": "phrase", "ipa": "/ɡeɪn ɡraʊnd/", "vi": "giành thêm thế mạnh; lấn tới"},
    # 53: garden current
    {"pos": "phrase", "ipa": "/ˈɡɑːrdn ˈkɜːrənt/", "vi": "cây lý chua vườn"},
    # 54: golden years
    {"pos": "phrase", "ipa": "/ˈɡoʊldən jɪrz/", "vi": "những năm tuổi già an nhàn"},
    # 55: grand tour
    {"pos": "phrase", "ipa": "/ɡrænd tʊr/", "vi": "chuyến du ngoạn châu Âu"},
    # 56: ground rose
    {"pos": "phrase", "ipa": "/ɡraʊnd roʊz/", "vi": "hoa hồng bụi bò đất"},
    # 57: group discussion
    {"pos": "phrase", "ipa": "/ɡruːp dɪˈskʌʃn/", "vi": "buổi thảo luận nhóm; đàm luận nhóm"},
    # 58: hall pass
    {"pos": "phrase", "ipa": "/hɔːl pæs/", "vi": "thẻ ra ngoài hành lang lớp học"},
    # 59: hard steel
    {"pos": "phrase", "ipa": "/hɑːrd stiːl/", "vi": "thép cứng đặc chủng; thép cường lực"},
    # 60: high jump
    {"pos": "phrase", "ipa": "/haɪ dʒʌmp/", "vi": "môn nhảy cao trong điền kinh"},
    # 61: high tech
    {"pos": "phrase", "ipa": "/haɪ tɛk/", "vi": "công nghệ cao; kỹ thuật tân tiến"},
    # 62: historical school
    {"pos": "phrase", "ipa": "/hɪˈstɔːrɪkl skuːl/", "vi": "trường phái lịch sử luận"},
    # 63: hole out
    {"pos": "phrase", "ipa": "/hoʊl aʊt/", "vi": "đánh bóng vào lỗ golf"},
    # 64: hole up
    {"pos": "phrase", "ipa": "/hoʊl ʌp/", "vi": "ẩn náu kỹ; trốn biệt tăm"},
    # 65: home loan
    {"pos": "phrase", "ipa": "/hoʊm loʊn/", "vi": "khoản vay mua nhà; vay thế chấp nhà"},
    # 66: ice machine
    {"pos": "phrase", "ipa": "/aɪs məˈʃiːn/", "vi": "máy làm đá viên; máy tạo đá"},
    # 67: ill service
    {"pos": "phrase", "ipa": "/ɪl ˈsɜːrvɪs/", "vi": "hành động nhiệt tình gây hại"},
    # 68: impossible action
    {"pos": "phrase", "ipa": "/ɪmˈpɑːsəbl ˈækʃn/", "vi": "hành động bất khả thi; điều vô vọng"},
    # 69: in advance
    {"pos": "phrase", "ipa": "/ɪn ədˈvæns/", "vi": "trước; thanh toán trước"},
    # 70: john henry
    {"pos": "phrase", "ipa": "/dʒɑːn ˈhɛnri/", "vi": "anh hùng huyền thoại John Henry"},
    # 71: low level flight
    {"pos": "phrase", "ipa": "/loʊ ˈlɛvl flaɪt/", "vi": "chuyến bay tầm thấp; đường bay thấp"},
    # 72: mail car
    {"pos": "phrase", "ipa": "/meɪl kɑːr/", "vi": "toa xe lửa chở bưu phẩm"},
    # 73: mail order
    {"pos": "phrase", "ipa": "/meɪl ˈɔːrdər/", "vi": "đặt hàng qua thư bưu điện"},
    # 74: mail service
    {"pos": "phrase", "ipa": "/meɪl ˈsɜːrvɪs/", "vi": "dịch vụ bưu chính; ngành thư tín"},
    # 75: marketing cost
    {"pos": "phrase", "ipa": "/ˈmɑːrkɪtɪŋ kɔːst/", "vi": "chi phí tiếp thị; chi phí quảng bá"},
    # 76: mass card
    {"pos": "phrase", "ipa": "/mæs kɑːrd/", "vi": "thiệp xin lễ cầu nguyện Công giáo"},
    # 77: max out
    {"pos": "phrase", "ipa": "/mæks aʊt/", "vi": "chạm mức tối đa; xài hết hạn mức"},
    # 78: mental picture
    {"pos": "phrase", "ipa": "/ˈmɛntl ˈpɪktʃər/", "vi": "hình ảnh trong tâm trí; hình dung"},
    # 79: middle low german
    {"pos": "phrase", "ipa": "/ˈmɪdl loʊ ˈdʒɜːrmən/", "vi": "tiếng Hạ Đức trung đại"},
    # 80: military strength
    {"pos": "phrase", "ipa": "/ˈmɪlətɛri strɛŋkθ/", "vi": "tiềm lực quân sự; sức mạnh quân sự"},
    # 81: milk can
    {"pos": "phrase", "ipa": "/mɪlk kæn/", "vi": "bình thiếc đựng sữa tươi; thùng sữa"},
    # 82: natural family planning
    {"pos": "phrase", "ipa": "/ˈnætʃrəl ˈfæməli ˈplænɪŋ/", "vi": "kế hoạch hóa gia đình tự nhiên"},
    # 83: new ireland
    {"pos": "phrase", "ipa": "/njuː ˈaɪərlənd/", "vi": "đảo New Ireland"},
    # 84: new jersey
    {"pos": "phrase", "ipa": "/njuː ˈdʒɜːrzi/", "vi": "tiểu bang New Jersey"},
    # 85: paris green
    {"pos": "phrase", "ipa": "/ˈpærɪs ɡriːn/", "vi": "thuốc trừ sâu xanh Paris"},
    # 86: physical ability
    {"pos": "phrase", "ipa": "/ˈfɪzɪkl əˈbɪləti/", "vi": "năng lực thể chất; thể lực cơ thể"},
    # 87: point duty
    {"pos": "phrase", "ipa": "/pɔɪnt ˈduːti/", "vi": "nhiệm vụ điều tiết giao thông"},
    # 88: police investigation
    {"pos": "phrase", "ipa": "/pəˈliːs ɪnˌvɛstəˈɡeɪʃn/", "vi": "cuộc điều tra của cảnh sát"},
    # 89: political boss
    {"pos": "phrase", "ipa": "/pəˈlɪtɪkl bɔːs/", "vi": "ông trùm chính trị; đầu sỏ phe phái"},
    # 90: presence of mind
    {"pos": "phrase", "ipa": "/ˈprɛzns əv maɪnd/", "vi": "sự nhanh trí; tinh thần bình tĩnh"},
    # 91: president johnson
    {"pos": "phrase", "ipa": "/ˈprɛzədənt ˈdʒɑːnsn/", "vi": "Tổng thống Lyndon Johnson"},
    # 92: press agent
    {"pos": "phrase", "ipa": "/prɛs ˈeɪdʒənt/", "vi": "chuyên viên phụ trách báo chí"},
    # 93: property owner
    {"pos": "phrase", "ipa": "/ˈprɑːpərti ˈoʊnər/", "vi": "chủ sở hữu bất động sản; địa chủ"},
    # 94: public discussion
    {"pos": "phrase", "ipa": "/ˈpʌblɪk dɪˈskʌʃn/", "vi": "thảo luận công khai; tranh luận mở"},
    # 95: pull round
    {"pos": "phrase", "ipa": "/pʊl raʊnd/", "vi": "bình phục sau ốm; qua khỏi cơn nguy"},
    # 96: religious writing
    {"pos": "phrase", "ipa": "/rɪˈlɪdʒəs ˈraɪtɪŋ/", "vi": "kinh sách tôn giáo; văn bản giáo lý"},
    # 97: right of entry
    {"pos": "phrase", "ipa": "/raɪt əv ˈɛntri/", "vi": "quyền vào kiểm tra; quyền tiếp cận"},
    # 98: rock plant
    {"pos": "phrase", "ipa": "/rɑːk plænt/", "vi": "cây mọc kẽ đá; thực vật vùng đá"},
    # 99: screen door
    {"pos": "phrase", "ipa": "/skriːn dɔːr/", "vi": "cửa lưới chống muỗi; cửa chống bọ"}
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

json.dump(out_items, open("scratch/b22_r01_p5.json", "w"), ensure_ascii=False, indent=2)
print("Part 5 reviewed successfully: 100 items saved to scratch/b22_r01_p5.json")
