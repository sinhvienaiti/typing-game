import json

# Manual word-by-word cognitive review for Batch 21 Round 5 Part 3 (records 2200-2299, IDs 200k.002202 to 200k.002301)
reviewed_entries = [
    # 2200: press run
    {"ipa": "/prɛs rʌn/", "vi": "lượt in ấn báo chí; số bản in ấn", "pos": "phrase"},
    # 2201: professional life
    {"ipa": "/prəˈfɛʃənəl laɪf/", "vi": "đời sống sự nghiệp chuyên môn", "pos": "phrase"},
    # 2202: real property
    {"ipa": "/riːl ˈprɑːpərti/", "vi": "bất động sản địa ốc nhà đất", "pos": "phrase"},
    # 2203: send away
    {"ipa": "/sɛnd əˈweɪ/", "vi": "sa thải nhân viên; gửi bưu điện đi", "pos": "phrase"},
    # 2204: set upon
    {"ipa": "/sɛt əˈpɑːn/", "vi": "tấn công ập tới; vây hãm áp đảo", "pos": "phrase"},
    # 2205: small stuff
    {"ipa": "/smɔːl stʌf/", "vi": "chuyện vặt vãnh; dây thừng nhỏ", "pos": "phrase"},
    # 2206: stage left
    {"ipa": "/steɪdʒ lɛft/", "vi": "phía cánh trái sân khấu kịch", "pos": "phrase"},
    # 2207: straight off
    {"ipa": "/streɪt ɔːf/", "vi": "ngay lập tức tức thì; ngay từ đầu", "pos": "phrase"},
    # 2208: street child
    {"ipa": "/striːt tʃaɪld/", "vi": "trẻ em đường phố cơ nhỡ", "pos": "phrase"},
    # 2209: take note
    {"ipa": "/teɪk noʊt/", "vi": "ghi chép lưu ý kỹ; chú tâm", "pos": "phrase"},
    # 2210: travel by
    {"ipa": "/ˈtrævəl baɪ/", "vi": "di chuyển bằng phương tiện; đi qua", "pos": "phrase"},
    # 2211: voice part
    {"ipa": "/vɔɪs pɑːrt/", "vi": "bè thanh nhạc; phần xướng âm", "pos": "phrase"},
    # 2212: feels
    {"ipa": "/fiːlz/", "vi": "những cảm xúc xúc động; cảm giác", "pos": "noun"},
    # 2213: surer
    {"ipa": "/ˈʃʊrər/", "vi": "chắc chắn hơn; xác đáng hơn", "pos": "adj"},
    # 2214: surest
    {"ipa": "/ˈʃʊrɪst/", "vi": "chắc chắn nhất; đáng tin cậy nhất", "pos": "adj"},
    # 2215: families
    {"ipa": "/ˈfæməliz/", "vi": "các gia đình; những dòng họ", "pos": "noun"},
    # 2216: keeps
    {"ipa": "/kiːps/", "vi": "tháp canh lâu đài; kế sinh nhai", "pos": "noun"},
    # 2217: black september
    {"ipa": "/blæk sɛpˈtɛmbər/", "vi": "tổ chức Tháng Chín Đen Palestine", "pos": "phrase"},
    # 2218: body english
    {"ipa": "/ˈbɑːdi ˈɪŋɡlɪʃ/", "vi": "uốn éo người điều hướng bóng bay", "pos": "phrase"},
    # 2219: car park
    {"ipa": "/kɑːr pɑːrk/", "vi": "bãi đỗ xe ô tô; bãi giữ xe", "pos": "phrase"},
    # 2220: class period
    {"ipa": "/klæs ˈpɪriəd/", "vi": "tiết học giảng đường; giờ học", "pos": "phrase"},
    # 2221: common room
    {"ipa": "/ˈkɑːmən ruːm/", "vi": "phòng sinh hoạt tập thể chung", "pos": "phrase"},
    # 2222: control center
    {"ipa": "/kənˈtroʊl ˈsɛntər/", "vi": "trung tâm điều hành kiểm soát", "pos": "phrase"},
    # 2223: crazy house
    {"ipa": "/ˈkreɪzi haʊs/", "vi": "bệnh viện tâm thần; nơi hỗn loạn", "pos": "phrase"},
    # 2224: cross out
    {"ipa": "/krɔːs aʊt/", "vi": "gạch chéo xóa bỏ dòng chữ", "pos": "phrase"},
    # 2225: cut short
    {"ipa": "/kʌt ʃɔːrt/", "vi": "cắt ngang ngắt lời; kết thúc sớm", "pos": "phrase"},
    # 2226: dead body
    {"ipa": "/dɛd ˈbɑːdi/", "vi": "thi thể người chết; xác chết", "pos": "phrase"},
    # 2227: dead hand
    {"ipa": "/dɛd hænd/", "vi": "ảnh hưởng trói buộc của quá khứ", "pos": "phrase"},
    # 2228: dead room
    {"ipa": "/dɛd ruːm/", "vi": "nhà xác bệnh viện; phòng tiêu âm", "pos": "phrase"},
    # 2229: dog days
    {"ipa": "/dɔːɡ deɪz/", "vi": "những ngày hè oi ả ngột ngạt", "pos": "phrase"},
    # 2230: double first
    {"ipa": "/ˈdʌbəl fɜːrst/", "vi": "tốt nghiệp thủ khoa hai môn đại học", "pos": "phrase"},
    # 2231: drop by
    {"ipa": "/drɑːp baɪ/", "vi": "tạt qua ghé chơi; tiện đường thăm", "pos": "phrase"},
    # 2232: due date
    {"ipa": "/djuː deɪt/", "vi": "ngày đáo hạn nợ; ngày dự sinh", "pos": "phrase"},
    # 2233: easy street
    {"ipa": "/ˈiːzi striːt/", "vi": "cuộc sống sung túc; cảnh an nhàn", "pos": "phrase"},
    # 2234: free french
    {"ipa": "/friː frɛntʃ/", "vi": "lực lượng kháng chiến Pháp Tự Do", "pos": "phrase"},
    # 2235: full page
    {"ipa": "/fʊl peɪdʒ/", "vi": "quảng cáo nguyên trang báo", "pos": "phrase"},
    # 2236: give voice
    {"ipa": "/ɡɪv vɔɪs/", "vi": "nói lên tiếng lòng; cất tiếng nói", "pos": "phrase"},
    # 2237: great wall
    {"ipa": "/ɡreɪt wɔːl/", "vi": "Vạn Lý Trường Thành của Trung Quốc", "pos": "phrase"},
    # 2238: hard drive
    {"ipa": "/hɑːrd draɪv/", "vi": "ổ đĩa cứng máy tính", "pos": "phrase"},
    # 2239: high sea
    {"ipa": "/haɪ siː/", "vi": "vùng biển quốc tế tự do hàng hải", "pos": "phrase"},
    # 2240: home base
    {"ipa": "/hoʊm beɪs/", "vi": "căn cứ địa hậu phương; gôn nhà", "pos": "phrase"},
    # 2241: home truth
    {"ipa": "/hoʊm truːθ/", "vi": "sự thật mất lòng đau đớn", "pos": "phrase"},
    # 2242: hot war
    {"ipa": "/hɑːt wɔːr/", "vi": "chiến tranh nóng bùng nổ vũ lực", "pos": "phrase"},
    # 2243: hour hand
    {"ipa": "/ˈaʊər hænd/", "vi": "kim chỉ giờ trên mặt đồng hồ", "pos": "phrase"},
    # 2244: ice up
    {"ipa": "/aɪs ʌp/", "vi": "đóng băng bao phủ mặt kính", "pos": "phrase"},
    # 2245: kept up
    {"ipa": "/kɛpt ʌp/", "vi": "được bảo dưỡng chăm chút tốt", "pos": "phrase"},
    # 2246: king post
    {"ipa": "/kɪŋ poʊst/", "vi": "trụ đứng chống nóc giàn mái", "pos": "phrase"},
    # 2247: law of areas
    {"ipa": "/lɔː ʌv ˈɛriəz/", "vi": "định luật hai Kepler quét diện tích", "pos": "phrase"},
    # 2248: make peace
    {"ipa": "/meɪk piːs/", "vi": "giảng hòa kết thúc chiến tranh", "pos": "phrase"},
    # 2249: national trust
    {"ipa": "/ˈnæʃənəl trʌst/", "vi": "tổ chức bảo tồn di sản quốc gia", "pos": "phrase"},
    # 2250: oil company
    {"ipa": "/ɔɪl ˈkʌmpəni/", "vi": "công ty khai thác dầu khí", "pos": "phrase"},
    # 2251: on tour
    {"ipa": "/ɑːn tʊr/", "vi": "đang trong chuyến đi lưu diễn", "pos": "phrase"},
    # 2252: own goal
    {"ipa": "/oʊn ɡoʊl/", "vi": "bàn đá phản lưới nhà; gậy ông đập", "pos": "phrase"},
    # 2253: playing period
    {"ipa": "/ˈpleɪɪŋ ˈpɪriəd/", "vi": "thời gian thi đấu chính thức hiệp", "pos": "phrase"},
    # 2254: police department
    {"ipa": "/pəˈliːs dɪˈpɑːrtmənt/", "vi": "sở cảnh sát khu vực đô thị", "pos": "phrase"},
    # 2255: police force
    {"ipa": "/pəˈliːs fɔːrs/", "vi": "lực lượng nhân viên cảnh sát", "pos": "phrase"},
    # 2256: political program
    {"ipa": "/pəˈlɪtɪkəl ˈproʊɡræm/", "vi": "cương lĩnh hành động chính trị", "pos": "phrase"},
    # 2257: production line
    {"ipa": "/prəˈdʌkʃən laɪn/", "vi": "dây chuyền lắp ráp sản xuất", "pos": "phrase"},
    # 2258: production order
    {"ipa": "/prəˈdʌkʃən ˈɔːrdər/", "vi": "lệnh sản xuất chế tạo hàng", "pos": "phrase"},
    # 2259: public property
    {"ipa": "/ˈpʌblɪk ˈprɑːpərti/", "vi": "tài sản thuộc sở hữu công cộng", "pos": "phrase"},
    # 2260: research center
    {"ipa": "/rɪˈsɜːrtʃ ˈsɛntər/", "vi": "viện trung tâm nghiên cứu khoa học", "pos": "phrase"},
    # 2261: running light
    {"ipa": "/ˈrʌnɪŋ laɪt/", "vi": "đèn định vị hành trình tàu xe", "pos": "phrase"},
    # 2262: safe house
    {"ipa": "/seɪf haʊs/", "vi": "ngôi nhà an toàn ẩn náu bí mật", "pos": "phrase"},
    # 2263: school paper
    {"ipa": "/skuːl ˈpeɪpər/", "vi": "báo tường tập san học đường", "pos": "phrase"},
    # 2264: see double
    {"ipa": "/siː ˈdʌbəl/", "vi": "nhìn một hóa hai do hoa mắt", "pos": "phrase"},
    # 2265: show the door
    {"ipa": "/ʃoʊ ðə dɔːr/", "vi": "thẳng tay tống cổ đuổi ra cửa", "pos": "phrase"},
    # 2266: social event
    {"ipa": "/ˈsoʊʃəl ɪˈvɛnt/", "vi": "sự kiện giao lưu xã hội họp mặt", "pos": "phrase"},
    # 2267: social policy
    {"ipa": "/ˈsoʊʃəl ˈpɑːləsi/", "vi": "chính sách phúc lợi an sinh xã hội", "pos": "phrase"},
    # 2268: society of friends
    {"ipa": "/səˈsaɪəti ʌv frɛndz/", "vi": "Hội Thân hữu Quaker; giáo phái", "pos": "phrase"},
    # 2269: sort out
    {"ipa": "/sɔːrt aʊt/", "vi": "phân loại; tháo gỡ ổn thỏa", "pos": "phrase"},
    # 2270: sound law
    {"ipa": "/saʊnd lɔː/", "vi": "quy luật biến âm lịch sử ngôn ngữ", "pos": "phrase"},
    # 2271: south american country
    {"ipa": "/saʊθ əˈmɛrɪkən ˈkʌntri/", "vi": "quốc gia thuộc lục địa Nam Mỹ", "pos": "phrase"},
    # 2272: speed up
    {"ipa": "/spiːd ʌp/", "vi": "tăng tốc độ; đẩy nhanh tiến độ", "pos": "phrase"},
    # 2273: stage name
    {"ipa": "/steɪdʒ neɪm/", "vi": "nghệ danh biểu diễn sân khấu", "pos": "phrase"},
    # 2274: stage set
    {"ipa": "/steɪdʒ sɛt/", "vi": "cảnh trí dàn dựng sân khấu kịch", "pos": "phrase"},
    # 2275: taking hold
    {"ipa": "/ˈteɪkɪŋ hoʊld/", "vi": "sự bắt rễ bám sâu; sự nắm lấy", "pos": "phrase"},
    # 2276: test room
    {"ipa": "/tɛst ruːm/", "vi": "phòng thử nghiệm máy móc; phòng thi", "pos": "phrase"},
    # 2277: travel time
    {"ipa": "/ˈtrævəl taɪm/", "vi": "thời gian di chuyển trên đường", "pos": "phrase"},
    # 2278: tv room
    {"ipa": "/ˌtiːˈviː ruːm/", "vi": "phòng xem tivi gia đình", "pos": "phrase"},
    # 2279: word form
    {"ipa": "/wɜːrd fɔːrm/", "vi": "hình thái dạng thức cấu tạo từ", "pos": "phrase"},
    # 2280: works program
    {"ipa": "/wɜːrks ˈproʊɡræm/", "vi": "chương trình việc làm công ích", "pos": "phrase"},
    # 2281: write off
    {"ipa": "/raɪt ɔːf/", "vi": "xóa sổ nợ khó đòi; phế bỏ xe hỏng", "pos": "phrase"},
    # 2282: beat back
    {"ipa": "/biːt bæk/", "vi": "đánh bật quân giặc lui về; đẩy lui", "pos": "phrase"},
    # 2283: bill of health
    {"ipa": "/bɪl ʌv hɛlθ/", "vi": "chứng thư kiểm dịch y tế tàu biển", "pos": "phrase"},
    # 2284: blood group
    {"ipa": "/blʌd ɡruːp/", "vi": "hệ nhóm máu sinh học", "pos": "phrase"},
    # 2285: book value
    {"ipa": "/bʊk ˈvæljuː/", "vi": "giá trị sổ sách kế toán tài sản", "pos": "phrase"},
    # 2286: by nature
    {"ipa": "/baɪ ˈneɪtʃər/", "vi": "vốn dĩ từ trong bản chất bản tính", "pos": "phrase"},
    # 2287: center bit
    {"ipa": "/ˈsɛntər bɪt/", "vi": "mũi khoan định tâm khoét lỗ mộc", "pos": "phrase"},
    # 2288: central american
    {"ipa": "/ˈsɛntrəl əˈmɛrɪkən/", "vi": "người Trung Mỹ; thuộc vùng Trung Mỹ", "pos": "phrase"},
    # 2289: city council
    {"ipa": "/ˈsɪti ˈkaʊnsəl/", "vi": "hội đồng nhân dân thành phố", "pos": "phrase"},
    # 2290: cold work
    {"ipa": "/koʊld wɜːrk/", "vi": "gia công kim loại nguội cơ khí", "pos": "phrase"},
    # 2291: company union
    {"ipa": "/ˈkʌmpəni ˈjuːnjən/", "vi": "công đoàn cơ sở nội bộ công ty", "pos": "phrase"},
    # 2292: cost of living
    {"ipa": "/kɔːst ʌv ˈlɪvɪŋ/", "vi": "chi phí sinh hoạt đắt đỏ hàng ngày", "pos": "phrase"},
    # 2293: dead air
    {"ipa": "/dɛd ɛr/", "vi": "khoảng lặng chết trên sóng đài", "pos": "phrase"},
    # 2294: death wish
    {"ipa": "/dɛθ wɪʃ/", "vi": "ước muốn tự sát tìm đến cái chết", "pos": "phrase"},
    # 2295: double back
    {"ipa": "/ˈdʌbəl bæk/", "vi": "quay ngoắt ngược lại lối cũ", "pos": "phrase"},
    # 2296: double over
    {"ipa": "/ˈdʌbəl ˈoʊvər/", "vi": "gập người vì quá đau đớn", "pos": "phrase"},
    # 2297: drive line
    {"ipa": "/draɪv laɪn/", "vi": "hệ thống truyền lực cơ cấu xe hơi", "pos": "phrase"},
    # 2298: drop out
    {"ipa": "/drɑːp aʊt/", "vi": "bỏ học giữa chừng; tách biệt xã hội", "pos": "phrase"},
    # 2299: economic system
    {"ipa": "/ˌiːkəˈnɑːmɪk ˈsɪstəm/", "vi": "hệ thống thể chế kinh tế quốc gia", "pos": "phrase"},
]

with open('scratch/b21_r05_raw_p3.json') as f:
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

with open('scratch/b21_r05_p3.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r05_p3.json created successfully and validated!")
