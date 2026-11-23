import json

# Manual word-by-word cognitive review for Batch 21 Round 5 Part 2 (records 2100-2199, IDs 200k.002102 to 200k.002201)
reviewed_entries = [
    # 2100: hot water
    {"ipa": "/hɑːt ˈwɔːtər/", "vi": "nước sôi lửa bỏng; cảnh khốn đốn", "pos": "phrase"},
    # 2101: human action
    {"ipa": "/ˈhjuːmən ˈækʃən/", "vi": "hành động của con người", "pos": "phrase"},
    # 2102: human process
    {"ipa": "/ˈhjuːmən ˈprɑːsɛs/", "vi": "tiến trình có con người can thiệp", "pos": "phrase"},
    # 2103: in particular
    {"ipa": "/ɪn pərˈtɪkjələr/", "vi": "nói riêng; đặc biệt chú trọng", "pos": "phrase"},
    # 2104: in the beginning
    {"ipa": "/ɪn ðə bɪˈɡɪnɪŋ/", "vi": "lúc ban sơ; vào thời kỳ đầu tiên", "pos": "phrase"},
    # 2105: land office
    {"ipa": "/lænd ˈɔːfɪs/", "vi": "nha địa chính; sở quản lý đất đai", "pos": "phrase"},
    # 2106: language school
    {"ipa": "/ˈlæŋɡwɪdʒ skuːl/", "vi": "trường đào tạo ngoại ngữ", "pos": "phrase"},
    # 2107: lead story
    {"ipa": "/liːd ˈstɔːri/", "vi": "tin bài trang nhất; bài báo đinh", "pos": "phrase"},
    # 2108: let drive
    {"ipa": "/lɛt draɪv/", "vi": "nổ súng bắn phá; giáng đòn mạnh", "pos": "phrase"},
    # 2109: mark off
    {"ipa": "/mɑːrk ɔːf/", "vi": "phân định ranh giới; gạch tên đi", "pos": "phrase"},
    # 2110: match play
    {"ipa": "/mætʃ pleɪ/", "vi": "thể thức đấu lỗ đối kháng trong gôn", "pos": "phrase"},
    # 2111: mean value
    {"ipa": "/miːn ˈvæljuː/", "vi": "giá trị trung bình toán học", "pos": "phrase"},
    # 2112: means test
    {"ipa": "/miːnz tɛst/", "vi": "thẩm tra điều kiện thu nhập tài sản", "pos": "phrase"},
    # 2113: military post
    {"ipa": "/ˈmɪlətɛri poʊst/", "vi": "đồn binh; căn cứ đóng quân đồn trú", "pos": "phrase"},
    # 2114: modern man
    {"ipa": "/ˈmɑːdərn mæn/", "vi": "người hiện đại; người tinh khôn", "pos": "phrase"},
    # 2115: music director
    {"ipa": "/ˈmjuːzɪk dəˈrɛktər/", "vi": "giám đốc âm nhạc; chỉ huy dàn nhạc", "pos": "phrase"},
    # 2116: national bank
    {"ipa": "/ˈnæʃənəl bæŋk/", "vi": "ngân hàng quốc gia; ngân hàng lớn", "pos": "phrase"},
    # 2117: national park
    {"ipa": "/ˈnæʃənəl pɑːrk/", "vi": "vườn quốc gia; công viên bảo tồn", "pos": "phrase"},
    # 2118: new river
    {"ipa": "/nuː ˈrɪvər/", "vi": "sông New tại miền Đông nước Mỹ", "pos": "phrase"},
    # 2119: north by west
    {"ipa": "/nɔːrθ baɪ wɛst/", "vi": "hướng bắc chếch tây một góc nhỏ", "pos": "phrase"},
    # 2120: old french
    {"ipa": "/oʊld frɛntʃ/", "vi": "tiếng Pháp cổ thời Trung Cổ", "pos": "phrase"},
    # 2121: open society
    {"ipa": "/ˈoʊpən səˈsaɪəti/", "vi": "xã hội mở tự do dân chủ", "pos": "phrase"},
    # 2122: page number
    {"ipa": "/peɪdʒ ˈnʌmbər/", "vi": "số thứ tự trang tài liệu", "pos": "phrase"},
    # 2123: pass off
    {"ipa": "/pæs ɔːf/", "vi": "mạo nhận là; diễn ra trôi qua êm ả", "pos": "phrase"},
    # 2124: playing field
    {"ipa": "/ˈpleɪɪŋ fiːld/", "vi": "sân cỏ thi đấu; sân chơi bình đẳng", "pos": "phrase"},
    # 2125: point source
    {"ipa": "/pɔɪnt sɔːrs/", "vi": "nguồn điểm phát xạ ô nhiễm", "pos": "phrase"},
    # 2126: possible action
    {"ipa": "/ˈpɑːsəbəl ˈækʃən/", "vi": "hành động khả dĩ; phương án có thể", "pos": "phrase"},
    # 2127: price control
    {"ipa": "/praɪs kənˈtroʊl/", "vi": "biện pháp kiểm soát bình ổn giá", "pos": "phrase"},
    # 2128: public trust
    {"ipa": "/ˈpʌblɪk trʌst/", "vi": "niềm tin của dân; quỹ tín thác công", "pos": "phrase"},
    # 2129: record book
    {"ipa": "/ˈrɛkərd bʊk/", "vi": "sổ ghi chép biên niên; sổ kỷ lục", "pos": "phrase"},
    # 2130: research project
    {"ipa": "/rɪˈsɜːrtʃ ˈprɑːdʒɛkt/", "vi": "đề tài dự án nghiên cứu khoa học", "pos": "phrase"},
    # 2131: round top
    {"ipa": "/raʊnd tɑːp/", "vi": "lều rạp xiếc hình chóp tròn", "pos": "phrase"},
    # 2132: short list
    {"ipa": "/ʃɔːrt lɪst/", "vi": "danh sách rút gọn ứng viên", "pos": "phrase"},
    # 2133: sleep off
    {"ipa": "/sliːp ɔːf/", "vi": "ngủ cho giã rượu; ngủ cho tan mệt", "pos": "phrase"},
    # 2134: social club
    {"ipa": "/ˈsoʊʃəl klʌb/", "vi": "câu lạc bộ giao lưu xã hội", "pos": "phrase"},
    # 2135: social security
    {"ipa": "/ˈsoʊʃəl sɪˈkjʊrəti/", "vi": "chế độ an sinh xã hội nhà nước", "pos": "phrase"},
    # 2136: sort of
    {"ipa": "/sɔːrt ʌv/", "vi": "đại loại là; có phần hơi hơi", "pos": "phrase"},
    # 2137: south america
    {"ipa": "/saʊθ əˈmɛrɪkə/", "vi": "lục địa Nam Mỹ; khu vực Nam Mỹ", "pos": "phrase"},
    # 2138: stop press
    {"ipa": "/stɑːp prɛs/", "vi": "tin nóng giờ chót chèn gấp lên báo", "pos": "phrase"},
    # 2139: take ten
    {"ipa": "/teɪk tɛn/", "vi": "nghỉ giải lao mười phút ngắn", "pos": "phrase"},
    # 2140: tax system
    {"ipa": "/tæks ˈsɪstəm/", "vi": "hệ thống chế độ thuế khóa", "pos": "phrase"},
    # 2141: term of office
    {"ipa": "/tɜːrm ʌv ˈɔːfɪs/", "vi": "nhiệm kỳ giữ cương vị công tác", "pos": "phrase"},
    # 2142: think piece
    {"ipa": "/θɪŋk piːs/", "vi": "bài báo bình luận phân tích sâu", "pos": "phrase"},
    # 2143: top round
    {"ipa": "/tɑːp raʊnd/", "vi": "thịt bắp đùi trên của con bò", "pos": "phrase"},
    # 2144: trade name
    {"ipa": "/treɪd neɪm/", "vi": "tên thương mại; nhãn hiệu buôn bán", "pos": "phrase"},
    # 2145: travel to
    {"ipa": "/ˈtrævəl tuː/", "vi": "đi du lịch đến; di chuyển tới", "pos": "phrase"},
    # 2146: trust company
    {"ipa": "/trʌst ˈkʌmpəni/", "vi": "công ty quản lý ủy thác tài sản", "pos": "phrase"},
    # 2147: under attack
    {"ipa": "/ˈʌndər əˈtæk/", "vi": "đang bị tấn công; bị chỉ trích gắt", "pos": "phrase"},
    # 2148: united states president
    {"ipa": "/juːˈnaɪtɪd steɪts ˈprɛzədənt/", "vi": "Tổng thống Hợp chúng quốc Hoa Kỳ", "pos": "phrase"},
    # 2149: walk around
    {"ipa": "/wɔːk əˈraʊnd/", "vi": "đi dạo dạo quanh ngắm cảnh", "pos": "phrase"},
    # 2150: west by north
    {"ipa": "/wɛst baɪ nɔːrθ/", "vi": "hướng tây chếch bắc một góc nhỏ", "pos": "phrase"},
    # 2151: whatever may come
    {"ipa": "/wʌtˈɛvər meɪ kʌm/", "vi": "dù cho bất cứ chuyện gì xảy đến", "pos": "phrase"},
    # 2152: word class
    {"ipa": "/wɜːrd klæs/", "vi": "từ loại trong ngữ pháp ngôn ngữ", "pos": "phrase"},
    # 2153: work table
    {"ipa": "/wɜːrk ˈteɪbəl/", "vi": "bàn làm việc bàn thao tác", "pos": "phrase"},
    # 2154: ends
    {"ipa": "/ɛndz/", "vi": "các đầu mút; những mục đích chung", "pos": "noun"},
    # 2155: founded
    {"ipa": "/ˈfaʊndɪd/", "vi": "đã thành lập; đã sáng lập", "pos": "verb"},
    # 2156: founds
    {"ipa": "/faʊndz/", "vi": "chi phí ăn ở; việc đúc kim loại", "pos": "noun"},
    # 2157: musts
    {"ipa": "/mʌsts/", "vi": "những điều bắt buộc; thứ cốt yếu", "pos": "noun"},
    # 2158: shown
    {"ipa": "/ʃoʊn/", "vi": "được trình chiếu; đã được cho thấy", "pos": "verb"},
    # 2159: ahead of time
    {"ipa": "/əˈhɛd ʌv taɪm/", "vi": "trước thời hạn; sớm hơn dự tính", "pos": "phrase"},
    # 2160: air force
    {"ipa": "/ɛr fɔːrs/", "vi": "quân chủng không quân tác chiến", "pos": "phrase"},
    # 2161: air space
    {"ipa": "/ɛr speɪs/", "vi": "vùng trời; không phận quốc gia", "pos": "phrase"},
    # 2162: bank line
    {"ipa": "/bæŋk laɪn/", "vi": "hạn mức cấp vốn tín dụng ngân hàng", "pos": "phrase"},
    # 2163: bank run
    {"ipa": "/bæŋk rʌn/", "vi": "làn sóng ồ ạt rút tiền gửi", "pos": "phrase"},
    # 2164: beat about
    {"ipa": "/biːt əˈbaʊt/", "vi": "tìm khắp nơi; nói vòng vo tam quốc", "pos": "phrase"},
    # 2165: beat out
    {"ipa": "/biːt aʊt/", "vi": "đánh bại đối thủ; đập lửa tắt", "pos": "phrase"},
    # 2166: beat up
    {"ipa": "/biːt ʌp/", "vi": "đánh đập túi bụi; tàn tạ bầm giập", "pos": "phrase"},
    # 2167: blood money
    {"ipa": "/blʌd ˈmʌni/", "vi": "tiền đền mạng; tiền đền tội ác", "pos": "phrase"},
    # 2168: blue point
    {"ipa": "/bluː pɔɪnt/", "vi": "loại hàu xanh bờ đông nước Mỹ", "pos": "phrase"},
    # 2169: cause of action
    {"ipa": "/kɔːz ʌv ˈækʃən/", "vi": "căn cứ pháp lý để khởi kiện", "pos": "phrase"},
    # 2170: character set
    {"ipa": "/ˈkærɪktər sɛt/", "vi": "bộ mã ký tự trong máy tính", "pos": "phrase"},
    # 2171: church service
    {"ipa": "/tʃɜːrtʃ ˈsɜːrvɪs/", "vi": "buổi lễ phụng vụ tại thánh đường", "pos": "phrase"},
    # 2172: control account
    {"ipa": "/kənˈtroʊl əˈkaʊnt/", "vi": "tài khoản kiểm soát tổng hợp", "pos": "phrase"},
    # 2173: day care center
    {"ipa": "/deɪ kɛr ˈsɛntər/", "vi": "nhà trẻ ban ngày; trung tâm giữ trẻ", "pos": "phrase"},
    # 2174: deep down
    {"ipa": "/diːp daʊn/", "vi": "trong sâu thẳm tâm hồn; thâm tâm", "pos": "phrase"},
    # 2175: double time
    {"ipa": "/ˈdʌbəl taɪm/", "vi": "chạy bước gấp đôi; lương gấp đôi", "pos": "phrase"},
    # 2176: double up
    {"ipa": "/ˈdʌbəl ʌp/", "vi": "gập người ôm bụng; ở ghép chung", "pos": "phrase"},
    # 2177: drop in
    {"ipa": "/drɑːp ɪn/", "vi": "ghé thăm bất ngờ; tạt qua chơi", "pos": "phrase"},
    # 2178: fall into place
    {"ipa": "/fɔːl ˈɪntuː pleɪs/", "vi": "vào đúng vị trí; sáng tỏ ngọn ngành", "pos": "phrase"},
    # 2179: focus on
    {"ipa": "/ˈfoʊkəs ɑːn/", "vi": "tập trung cao độ vào; chú trọng", "pos": "phrase"},
    # 2180: football play
    {"ipa": "/ˈfʊtˌbɔːl pleɪ/", "vi": "pha dàn xếp tấn công bóng bầu dục", "pos": "phrase"},
    # 2181: for sale
    {"ipa": "/fɔːr seɪl/", "vi": "được rao bán; để bán", "pos": "phrase"},
    # 2182: gas up
    {"ipa": "/ɡæs ʌp/", "vi": "đổ đầy bình xăng xe; nạp nhiên liệu", "pos": "phrase"},
    # 2183: get ahead
    {"ipa": "/ɡɛt əˈhɛd/", "vi": "vươn lên dẫn đầu; thăng tiến xa", "pos": "phrase"},
    # 2184: hot line
    {"ipa": "/hɑːt laɪn/", "vi": "đường dây nóng khẩn cấp kết nối", "pos": "phrase"},
    # 2185: information return
    {"ipa": "/ˌɪnfərˈmeɪʃən rɪˈtɜːrn/", "vi": "tờ khai báo thông tin thuế", "pos": "phrase"},
    # 2186: inside information
    {"ipa": "/ˈɪnˌsaɪd ˌɪnfərˈmeɪʃən/", "vi": "thông tin nội gián; tin nội bộ", "pos": "phrase"},
    # 2187: left stage
    {"ipa": "/lɛft steɪdʒ/", "vi": "phía cánh trái của sân khấu kịch", "pos": "phrase"},
    # 2188: loved one
    {"ipa": "/lʌvd wʌn/", "vi": "người thân yêu ruột thịt trong nhà", "pos": "phrase"},
    # 2189: mark down
    {"ipa": "/mɑːrk daʊn/", "vi": "hạ giá bán hàng; ghi chép lại", "pos": "phrase"},
    # 2190: match point
    {"ipa": "/mætʃ pɔɪnt/", "vi": "điểm quyết định ván đấu chung cuộc", "pos": "phrase"},
    # 2191: military control
    {"ipa": "/ˈmɪlətɛri kənˈtroʊl/", "vi": "sự kiểm soát của quân đội quân sự", "pos": "phrase"},
    # 2192: military court
    {"ipa": "/ˈmɪlətɛri kɔːrt/", "vi": "tòa án binh; tòa án quân sự", "pos": "phrase"},
    # 2193: music stand
    {"ipa": "/ˈmjuːzɪk stænd/", "vi": "giá đỡ bản nhạc tập biểu diễn", "pos": "phrase"},
    # 2194: natural number
    {"ipa": "/ˈnætʃərəl ˈnʌmbər/", "vi": "tập hợp số tự nhiên toán học", "pos": "phrase"},
    # 2195: news event
    {"ipa": "/nuːz ɪˈvɛnt/", "vi": "sự kiện thời sự đáng đưa tin", "pos": "phrase"},
    # 2196: next door
    {"ipa": "/nɛkst dɔːr/", "vi": "ở ngay nhà bên cạnh; sát vách", "pos": "phrase"},
    # 2197: pass through
    {"ipa": "/pæs θruː/", "vi": "đi ngang qua; trải qua giai đoạn", "pos": "phrase"},
    # 2198: piece of work
    {"ipa": "/piːs ʌv wɜːrk/", "vi": "tác phẩm hoàn thiện; kẻ khó ưa", "pos": "phrase"},
    # 2199: police action
    {"ipa": "/pəˈliːs ˈækʃən/", "vi": "chiến dịch hành động của cảnh sát", "pos": "phrase"},
]

with open('scratch/b21_r05_raw_p2.json') as f:
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

with open('scratch/b21_r05_p2.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r05_p2.json created successfully and validated!")
