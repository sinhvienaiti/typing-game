import json

# Manual word-by-word cognitive review for Batch 21 Round 6 Part 2 (records 2600-2699, IDs 200k.002602 to 200k.002701)
reviewed_entries = [
    # 2600: normal school
    {"ipa": "/ˈnɔːrməl skuːl/", "vi": "trường sư phạm đào tạo giáo viên", "pos": "phrase"},
    # 2601: north by east
    {"ipa": "/nɔːrθ baɪ iːst/", "vi": "hướng bắc hơi chếch sang đông", "pos": "phrase"},
    # 2602: open door
    {"ipa": "/ˈoʊpən dɔːr/", "vi": "chính sách mở cửa kinh tế giao lưu", "pos": "phrase"},
    # 2603: order paper
    {"ipa": "/ˈɔːrdər ˈpeɪpər/", "vi": "chương trình nghị sự nghị viện", "pos": "phrase"},
    # 2604: president washington
    {"ipa": "/ˈprɛzɪdənt ˈwɑːʃɪŋtən/", "vi": "Tổng thống George Washington của Mỹ", "pos": "phrase"},
    # 2605: price cut
    {"ipa": "/praɪs kʌt/", "vi": "sự giảm giá; sự hạ giá bán hàng", "pos": "phrase"},
    # 2606: professional person
    {"ipa": "/prəˈfɛʃənəl ˈpɜːrsən/", "vi": "người làm chuyên môn; chuyên gia", "pos": "phrase"},
    # 2607: quality control
    {"ipa": "/ˈkwɑːləti kənˈtroʊl/", "vi": "hoạt động kiểm soát chất lượng", "pos": "phrase"},
    # 2608: race car
    {"ipa": "/reɪs kɑːr/", "vi": "xe đua tốc độ; xe đua chuyên nghiệp", "pos": "phrase"},
    # 2609: red hot
    {"ipa": "/rɛd hɑːt/", "vi": "nóng đỏ rực; sôi nổi cực kỳ gay cấn", "pos": "phrase"},
    # 2610: rest energy
    {"ipa": "/rɛst ˈɛnərdʒi/", "vi": "năng lượng nghỉ của vật chất", "pos": "phrase"},
    # 2611: running board
    {"ipa": "/ˈrʌnɪŋ bɔːrd/", "vi": "bậc bước chân lên xuống xe ô tô", "pos": "phrase"},
    # 2612: school text
    {"ipa": "/skuːl tɛkst/", "vi": "sách giáo khoa trong nhà trường", "pos": "phrase"},
    # 2613: sea power
    {"ipa": "/siː ˈpaʊər/", "vi": "sức mạnh hải quân; cường quốc biển", "pos": "phrase"},
    # 2614: second growth
    {"ipa": "/ˈsɛkənd ɡroʊθ/", "vi": "rừng thứ sinh tái sinh tự nhiên", "pos": "phrase"},
    # 2615: sell off
    {"ipa": "/sɛl ɔːf/", "vi": "bán tháo tài sản; bán đại hạ giá", "pos": "phrase"},
    # 2616: sense experience
    {"ipa": "/sɛns ɪkˈspɪriəns/", "vi": "kinh nghiệm cảm giác trực quan", "pos": "phrase"},
    # 2617: set piece
    {"ipa": "/sɛt piːs/", "vi": "pha bóng cố định; cảnh dựng độc lập", "pos": "phrase"},
    # 2618: stand watch
    {"ipa": "/stænd wɑːtʃ/", "vi": "đứng gác; canh phòng cẩn mật", "pos": "phrase"},
    # 2619: starting line
    {"ipa": "/ˈstɑːrtɪŋ laɪn/", "vi": "vạch xuất phát trong cuộc thi", "pos": "phrase"},
    # 2620: station house
    {"ipa": "/ˈsteɪʃən haʊs/", "vi": "đồn công an cảnh sát; trạm cứu hỏa", "pos": "phrase"},
    # 2621: talk terms
    {"ipa": "/tɔːk tɜːrmz/", "vi": "thương lượng điều khoản; đàm phán", "pos": "phrase"},
    # 2622: time unit
    {"ipa": "/taɪm ˈjuːnɪt/", "vi": "đơn vị đo lường thời gian", "pos": "phrase"},
    # 2623: tv program
    {"ipa": "/ˌtiːˈviː ˈproʊɡræm/", "vi": "chương trình phát sóng truyền hình", "pos": "phrase"},
    # 2624: unit of time
    {"ipa": "/ˈjuːnɪt ʌv taɪm/", "vi": "đơn vị đo đếm khoảng thời gian", "pos": "phrase"},
    # 2625: white sea
    {"ipa": "/waɪt siː/", "vi": "Biển Trắng ở tây bắc nước Nga", "pos": "phrase"},
    # 2626: wish list
    {"ipa": "/wɪʃ lɪst/", "vi": "danh sách mong muốn; danh mục ước", "pos": "phrase"},
    # 2627: lets
    {"ipa": "/lɛts/", "vi": "bóng chạm lưới; những lần cho thuê", "pos": "noun"},
    # 2628: realer
    {"ipa": "/ˈriːələr/", "vi": "chân thật hơn; thực tế hơn rõ rệt", "pos": "adj"},
    # 2629: reales
    {"ipa": "/reɪˈɑːleɪs/", "vi": "các đồng tiền real cổ Tây Ban Nha", "pos": "noun"},
    # 2630: realest
    {"ipa": "/ˈriːəlɪst/", "vi": "chân thật nhất; thực tế nhất đời", "pos": "adj"},
    # 2631: reals
    {"ipa": "/riːlz/", "vi": "các đồng real Brasil; tiền real cổ", "pos": "noun"},
    # 2632: reis
    {"ipa": "/reɪs/", "vi": "các đồng reis Bồ Đào Nha cổ xưa", "pos": "noun"},
    # 2633: at close range
    {"ipa": "/æt kloʊs reɪndʒ/", "vi": "ở cự ly cận kề; ngay sát tầm mắt", "pos": "phrase"},
    # 2634: at the worst
    {"ipa": "/æt ðə wɜːrst/", "vi": "trong tình huống tồi tệ nhất", "pos": "phrase"},
    # 2635: at worst
    {"ipa": "/æt wɜːrst/", "vi": "trong kịch bản xấu nhất; tệ nhất", "pos": "phrase"},
    # 2636: back judge
    {"ipa": "/bæk dʒʌdʒ/", "vi": "trọng tài biên sân sau bóng bầu dục", "pos": "phrase"},
    # 2637: bank building
    {"ipa": "/bæŋk ˈbɪldɪŋ/", "vi": "tòa nhà trụ sở chi nhánh ngân hàng", "pos": "phrase"},
    # 2638: be active
    {"ipa": "/biː ˈæktɪv/", "vi": "hoạt động tích cực; đang vận hành", "pos": "phrase"},
    # 2639: body language
    {"ipa": "/ˈbɑːdi ˈlæŋɡwɪdʒ/", "vi": "ngôn ngữ cơ thể; cử chỉ hình thể", "pos": "phrase"},
    # 2640: building society
    {"ipa": "/ˈbɪldɪŋ səˈsaɪəti/", "vi": "tổ chức tín dụng tiết kiệm nhà ở", "pos": "phrase"},
    # 2641: call mark
    {"ipa": "/kɔːl mɑːrk/", "vi": "ký hiệu phân loại sách thư viện", "pos": "phrase"},
    # 2642: case officer
    {"ipa": "/keɪs ˈɔːfɪsər/", "vi": "sĩ quan tình báo phụ trách hồ sơ vụ", "pos": "phrase"},
    # 2643: cash in
    {"ipa": "/kæʃ ɪn/", "vi": "đổi thành tiền mặt; kiếm chác lợi", "pos": "phrase"},
    # 2644: chance event
    {"ipa": "/tʃæns ɪˈvɛnt/", "vi": "sự kiện ngẫu nhiên; biến cố tình cờ", "pos": "phrase"},
    # 2645: church building
    {"ipa": "/tʃɜːrtʃ ˈbɪldɪŋ/", "vi": "tòa nhà giáo đường thánh đường thờ", "pos": "phrase"},
    # 2646: college boy
    {"ipa": "/ˈkɑːlɪdʒ bɔɪ/", "vi": "nam sinh viên đại học trẻ tuổi", "pos": "phrase"},
    # 2647: contract out
    {"ipa": "/ˈkɑːntrækt aʊt/", "vi": "khoán thầu ra ngoài; thuê ngoài làm", "pos": "phrase"},
    # 2648: david low
    {"ipa": "/ˈdeɪvɪd loʊ/", "vi": "họa sĩ tranh biếm họa David Low", "pos": "phrase"},
    # 2649: dead march
    {"ipa": "/dɛd mɑːrtʃ/", "vi": "bản khúc quân hành tiễn đưa tang lễ", "pos": "phrase"},
    # 2650: deep water
    {"ipa": "/diːp ˈwɔːtər/", "vi": "vùng nước sâu; tình cảnh nguy khốn", "pos": "phrase"},
    # 2651: dog food
    {"ipa": "/dɔːɡ fuːd/", "vi": "thức ăn hạt cho chó nuôi trong nhà", "pos": "phrase"},
    # 2652: fair game
    {"ipa": "/fɛr ɡeɪm/", "vi": "mục tiêu dễ bị châm chọc tấn công", "pos": "phrase"},
    # 2653: fall short
    {"ipa": "/fɔːl ʃɔːrt/", "vi": "không đạt chỉ tiêu; thiếu hụt hẫng", "pos": "phrase"},
    # 2654: fall short of
    {"ipa": "/fɔːl ʃɔːrt ʌv/", "vi": "chưa đạt tới mức; không thỏa mãn", "pos": "phrase"},
    # 2655: first lady
    {"ipa": "/fɜːrst ˈleɪdi/", "vi": "đệ nhất phu nhân của nguyên thủ", "pos": "phrase"},
    # 2656: free association
    {"ipa": "/friː əˌsoʊsiˈeɪʃən/", "vi": "phương pháp liên tưởng tự do tâm lý", "pos": "phrase"},
    # 2657: free of charge
    {"ipa": "/friː ʌv tʃɑːrdʒ/", "vi": "miễn phí hoàn toàn; không mất tiền", "pos": "phrase"},
    # 2658: free weight
    {"ipa": "/friː weɪt/", "vi": "quả tạ tập thể hình tự do", "pos": "phrase"},
    # 2659: goal line
    {"ipa": "/ɡoʊl laɪn/", "vi": "vạch cầu môn; vạch vôi khung thành", "pos": "phrase"},
    # 2660: green light
    {"ipa": "/ɡriːn laɪt/", "vi": "đèn xanh giao thông; sự phê chuẩn", "pos": "phrase"},
    # 2661: ground fire
    {"ipa": "/ɡraʊnd ˈfaɪər/", "vi": "cháy ngầm lòng đất; hỏa lực mặt đất", "pos": "phrase"},
    # 2662: health code
    {"ipa": "/hɛlθ koʊd/", "vi": "quy chuẩn vệ sinh y tế an toàn", "pos": "phrase"},
    # 2663: heart rate
    {"ipa": "/hɑːrt reɪt/", "vi": "tần số nhịp đập của quả tim", "pos": "phrase"},
    # 2664: hell to pay
    {"ipa": "/hɛl tuː peɪ/", "vi": "rắc rối to lớn; hậu quả khôn lường", "pos": "phrase"},
    # 2665: house husband
    {"ipa": "/haʊs ˈhʌzbənd/", "vi": "người chồng làm nội trợ gia đình", "pos": "phrase"},
    # 2666: ice show
    {"ipa": "/aɪs ʃoʊ/", "vi": "chương trình biểu diễn trượt băng", "pos": "phrase"},
    # 2667: in operation
    {"ipa": "/ɪn ˌɑːpəˈreɪʃən/", "vi": "đang hoạt động; đang được áp dụng", "pos": "phrase"},
    # 2668: in secret
    {"ipa": "/ɪn ˈsiːkrət/", "vi": "lén lút kín đáo; một cách bí mật", "pos": "phrase"},
    # 2669: land site
    {"ipa": "/lænd saɪt/", "vi": "khu đất; địa điểm xây dựng dự án", "pos": "phrase"},
    # 2670: limited company
    {"ipa": "/ˈlɪmɪtɪd ˈkʌmpəni/", "vi": "công ty trách nhiệm hữu hạn", "pos": "phrase"},
    # 2671: low countries
    {"ipa": "/loʊ ˈkʌntriz/", "vi": "các quốc gia Vùng đất thấp ven biển", "pos": "phrase"},
    # 2672: lower class
    {"ipa": "/ˈloʊər klæs/", "vi": "tầng lớp bình dân; giai cấp hạ lưu", "pos": "phrase"},
    # 2673: married person
    {"ipa": "/ˈmærid ˈpɜːrsən/", "vi": "người đã kết hôn; người có gia đình", "pos": "phrase"},
    # 2674: medical building
    {"ipa": "/ˈmɛdɪkəl ˈbɪldɪŋ/", "vi": "tòa nhà cơ sở y tế phòng khám bệnh", "pos": "phrase"},
    # 2675: military action
    {"ipa": "/ˈmɪlətɛri ˈækʃən/", "vi": "hoạt động quân sự; tác chiến vũ lực", "pos": "phrase"},
    # 2676: moving company
    {"ipa": "/ˈmuːvɪŋ ˈkʌmpəni/", "vi": "công ty dịch vụ dọn chuyển nhà trọn", "pos": "phrase"},
    # 2677: music box
    {"ipa": "/ˈmjuːzɪk bɑːks/", "vi": "hộp phát nhạc cổ điển lên dây cót", "pos": "phrase"},
    # 2678: near east
    {"ipa": "/nɪr iːst/", "vi": "vùng Cận Đông trong lịch sử địa lý", "pos": "phrase"},
    # 2679: out of reach
    {"ipa": "/aʊt ʌv riːtʃ/", "vi": "ngoài tầm với; vượt quá tầm với tới", "pos": "phrase"},
    # 2680: pass water
    {"ipa": "/pæs ˈwɔːtər/", "vi": "đi tiểu tiện; bài tiết nước tiểu", "pos": "phrase"},
    # 2681: phone bill
    {"ipa": "/foʊn bɪl/", "vi": "hóa đơn cước phí điện thoại dịch vụ", "pos": "phrase"},
    # 2682: reach out
    {"ipa": "/riːtʃ aʊt/", "vi": "vươn tay; chủ động liên hệ ngỏ lời", "pos": "phrase"},
    # 2683: rest period
    {"ipa": "/rɛst ˈpɪriəd/", "vi": "khoảng thời gian nghỉ ngơi thư giãn", "pos": "phrase"},
    # 2684: right of search
    {"ipa": "/raɪt ʌv sɜːrtʃ/", "vi": "quyền khám xét nơi ở tàu thuyền", "pos": "phrase"},
    # 2685: rock group
    {"ipa": "/rɑːk ɡruːp/", "vi": "ban nhạc rock; nhóm nhạc rock", "pos": "phrase"},
    # 2686: rule out
    {"ipa": "/ruːl aʊt/", "vi": "loại trừ khả năng; bác bỏ hoàn toàn", "pos": "phrase"},
    # 2687: rules of order
    {"ipa": "/ruːlz ʌv ˈɔːrdər/", "vi": "quy tắc trật tự điều hành phiên họp", "pos": "phrase"},
    # 2688: special air service
    {"ipa": "/ˈspɛʃəl ɛr ˈsɜːrvɪs/", "vi": "Lực lượng Đặc nhiệm Không quân Anh", "pos": "phrase"},
    # 2689: stock up
    {"ipa": "/stɑːk ʌp/", "vi": "mua sắm tích trữ; dự trữ hàng hóa", "pos": "phrase"},
    # 2690: straight person
    {"ipa": "/streɪt ˈpɜːrsən/", "vi": "người dị tính luyến ái bình thường", "pos": "phrase"},
    # 2691: strong force
    {"ipa": "/strɔːŋ fɔːrs/", "vi": "lực tương tác hạt nhân mạnh vật lý", "pos": "phrase"},
    # 2692: table service
    {"ipa": "/ˈteɪbəl ˈsɜːrvɪs/", "vi": "dịch vụ phục vụ tận bàn; bộ đồ ăn", "pos": "phrase"},
    # 2693: tax form
    {"ipa": "/tæks fɔːrm/", "vi": "mẫu đơn kê khai thuế vụ cơ quan", "pos": "phrase"},
    # 2694: to no degree
    {"ipa": "/tuː noʊ dɪˈɡriː/", "vi": "hoàn toàn không một chút nào cả", "pos": "phrase"},
    # 2695: training college
    {"ipa": "/ˈtreɪnɪŋ ˈkɑːlɪdʒ/", "vi": "trường cao đẳng đào tạo nghề nghiệp", "pos": "phrase"},
    # 2696: training program
    {"ipa": "/ˈtreɪnɪŋ ˈproʊɡræm/", "vi": "chương trình huấn luyện đào tạo kỹ", "pos": "phrase"},
    # 2697: trump up
    {"ipa": "/trʌmp ʌp/", "vi": "bịa đặt dựng chuyện; vu khống trắng", "pos": "phrase"},
    # 2698: waiting line
    {"ipa": "/ˈweɪtɪŋ laɪn/", "vi": "hàng người xếp hàng dài chờ đợi", "pos": "phrase"},
    # 2699: watch key
    {"ipa": "/wɑːtʃ kiː/", "vi": "chìa lên dây cót đồng hồ quả quýt", "pos": "phrase"},
]

with open('scratch/b21_r06_raw_p2.json') as f:
    raw_data = json.load(f)

assert len(raw_data) == 100
assert len(reviewed_entries) == 100

output = []
for i, item in enumerate(raw_data):
    rev = reviewed_entries[i]
    assert rev["ipa"].startswith("/") and rev["ipa"].endswith("/") and rev["ipa"].count("/") == 2
    assert len(rev["vi"]) <= 35, f"vi too long: {rev['vi']} ({len(rev['vi'])} chars)"
    assert rev["pos"] in ["noun", "verb", "adj", "adv", "phrase", "intj", "prep", "conj", "pron", "det", "num"]
    
    new_item = {
        "id": item["id"],
        "hw": item["hw"],
        "pos": rev["pos"],
        "ipa": rev["ipa"],
        "vi": rev["vi"],
        "cefr": item["cefr"],
        "tier": item["tier"],
        "status": "reviewed",
        "notes": item["notes"]
    }
    output.append(new_item)

with open('scratch/b21_r06_p2.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r06_p2.json created successfully and validated!")
