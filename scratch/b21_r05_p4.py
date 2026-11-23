import json

# Manual word-by-word cognitive review for Batch 21 Round 5 Part 4 (records 2300-2399, IDs 200k.002302 to 200k.002401)
reviewed_entries = [
    # 2300: face value
    {"ipa": "/feɪs ˈvæljuː/", "vi": "giá trị danh nghĩa mệnh giá", "pos": "phrase"},
    # 2301: fall in line
    {"ipa": "/fɔːl ɪn laɪn/", "vi": "tuân theo kỷ luật; phục tùng", "pos": "phrase"},
    # 2302: fall open
    {"ipa": "/fɔːl ˈoʊpən/", "vi": "bật mở toang ra; há hốc miệng", "pos": "phrase"},
    # 2303: federal party
    {"ipa": "/ˈfɛdərəl ˈpɑːrti/", "vi": "Đảng Liên bang trong lịch sử Mỹ", "pos": "phrase"},
    # 2304: field of fire
    {"ipa": "/fiːld ʌv ˈfaɪər/", "vi": "khu vực xạ giới hỏa lực bắn", "pos": "phrase"},
    # 2305: full blood
    {"ipa": "/fʊl blʌd/", "vi": "thuần chủng; cùng một cha mẹ", "pos": "phrase"},
    # 2306: future date
    {"ipa": "/ˈfjuːtʃər deɪt/", "vi": "thời điểm tương lai; ngày hẹn", "pos": "phrase"},
    # 2307: gas well
    {"ipa": "/ɡæs wɛl/", "vi": "giếng khai thác khí đốt tự nhiên", "pos": "phrase"},
    # 2308: go ahead
    {"ipa": "/ɡoʊ əˈhɛd/", "vi": "tiến hành triển khai; đi trước", "pos": "phrase"},
    # 2309: green line
    {"ipa": "/ɡriːn laɪn/", "vi": "đường ranh giới đình chiến xanh", "pos": "phrase"},
    # 2310: green party
    {"ipa": "/ɡriːn ˈpɑːrti/", "vi": "Đảng Xanh bảo vệ môi trường", "pos": "phrase"},
    # 2311: high table
    {"ipa": "/haɪ ˈteɪbəl/", "vi": "bàn danh dự giáo sư viện đại học", "pos": "phrase"},
    # 2312: hold close
    {"ipa": "/hoʊld kloʊs/", "vi": "ôm chặt vào lòng; trân trọng giữ", "pos": "phrase"},
    # 2313: ice over
    {"ipa": "/aɪs ˈoʊvər/", "vi": "đóng băng mặt nước hồ", "pos": "phrase"},
    # 2314: language system
    {"ipa": "/ˈlæŋɡwɪdʒ ˈsɪstəm/", "vi": "hệ thống cấu trúc ngôn ngữ", "pos": "phrase"},
    # 2315: line drive
    {"ipa": "/laɪn draɪv/", "vi": "cú đánh bóng bẹt căng bóng chày", "pos": "phrase"},
    # 2316: line management
    {"ipa": "/laɪn ˈmænɪdʒmənt/", "vi": "quản lý tác nghiệp trực tiếp", "pos": "phrase"},
    # 2317: link up
    {"ipa": "/lɪŋk ʌp/", "vi": "kết nối; phối hợp tác chiến", "pos": "phrase"},
    # 2318: north america
    {"ipa": "/nɔːrθ əˈmɛrɪkə/", "vi": "lục địa Bắc Mỹ; vùng Bắc Mỹ", "pos": "phrase"},
    # 2319: office boy
    {"ipa": "/ˈɔːfɪs bɔɪ/", "vi": "nhân viên văn phòng phụ việc vặt", "pos": "phrase"},
    # 2320: oil business
    {"ipa": "/ɔɪl ˈbɪznəs/", "vi": "ngành kinh doanh dầu khí", "pos": "phrase"},
    # 2321: oil change
    {"ipa": "/ɔɪl tʃeɪndʒ/", "vi": "thay dầu nhớt động cơ xe", "pos": "phrase"},
    # 2322: paper money
    {"ipa": "/ˈpeɪpər ˈmʌni/", "vi": "tiền giấy lưu hành hợp pháp", "pos": "phrase"},
    # 2323: pass around
    {"ipa": "/pæs əˈraʊnd/", "vi": "truyền tay chuyền vòng quanh", "pos": "phrase"},
    # 2324: past perfect
    {"ipa": "/pæst ˈpɜːrfɪkt/", "vi": "thì quá khứ hoàn thành ngữ pháp", "pos": "phrase"},
    # 2325: plan of action
    {"ipa": "/plæn ʌv ˈækʃən/", "vi": "kế hoạch hành động cụ thể", "pos": "phrase"},
    # 2326: practice game
    {"ipa": "/ˈpræktɪs ɡeɪm/", "vi": "trận thi đấu tập luyện nội bộ", "pos": "phrase"},
    # 2327: sign away
    {"ipa": "/saɪn əˈweɪ/", "vi": "ký giấy từ bỏ quyền lợi tài sản", "pos": "phrase"},
    # 2328: sleep around
    {"ipa": "/sliːp əˈraʊnd/", "vi": "quan hệ tình dục bừa bãi", "pos": "phrase"},
    # 2329: source book
    {"ipa": "/sɔːrs bʊk/", "vi": "sách tập hợp tư liệu gốc", "pos": "phrase"},
    # 2330: space age
    {"ipa": "/speɪs eɪdʒ/", "vi": "kỷ nguyên khám phá vũ trụ", "pos": "phrase"},
    # 2331: stage business
    {"ipa": "/steɪdʒ ˈbɪznəs/", "vi": "động tác diễn xuất phụ trên kịch", "pos": "phrase"},
    # 2332: standard of life
    {"ipa": "/ˈstændərd ʌv laɪf/", "vi": "tiêu chuẩn chất lượng cuộc sống", "pos": "phrase"},
    # 2333: straight man
    {"ipa": "/streɪt mæn/", "vi": "vai phụ nghiêm túc làm nền hài", "pos": "phrase"},
    # 2334: table game
    {"ipa": "/ˈteɪbəl ɡeɪm/", "vi": "trò chơi bàn cờ giải trí", "pos": "phrase"},
    # 2335: take charge
    {"ipa": "/teɪk tʃɑːrdʒ/", "vi": "nắm quyền chỉ huy; đứng ra lo", "pos": "phrase"},
    # 2336: take effect
    {"ipa": "/teɪk ɪˈfɛkt/", "vi": "bắt đầu phát huy hiệu lực", "pos": "phrase"},
    # 2337: take in charge
    {"ipa": "/teɪk ɪn tʃɑːrdʒ/", "vi": "nhận trách nhiệm chăm sóc; giam", "pos": "phrase"},
    # 2338: tax law
    {"ipa": "/tæks lɔː/", "vi": "luật thuế khóa tài chính", "pos": "phrase"},
    # 2339: top dog
    {"ipa": "/tɑːp dɔːɡ/", "vi": "kẻ thống trị; kẻ đứng đầu quyền", "pos": "phrase"},
    # 2340: waiting game
    {"ipa": "/ˈweɪtɪŋ ɡeɪm/", "vi": "chiến thuật kiên nhẫn chờ thời", "pos": "phrase"},
    # 2341: walk away
    {"ipa": "/wɔːk əˈweɪ/", "vi": "bỏ đi; rũ bỏ trách nhiệm dễ dàng", "pos": "phrase"},
    # 2342: way station
    {"ipa": "/weɪ ˈsteɪʃən/", "vi": "trạm dừng chân nghỉ dọc đường", "pos": "phrase"},
    # 2343: write down
    {"ipa": "/raɪt daʊn/", "vi": "ghi chép vào giấy; khấu trừ", "pos": "phrase"},
    # 2344: moneys
    {"ipa": "/ˈmʌniz/", "vi": "các khoản tiền; những nguồn vốn", "pos": "noun"},
    # 2345: american football
    {"ipa": "/əˈmɛrɪkən ˈfʊtˌbɔːl/", "vi": "môn bóng bầu dục kiểu Mỹ", "pos": "phrase"},
    # 2346: art department
    {"ipa": "/ɑːrt dɪˈpɑːrtmənt/", "vi": "khoa mỹ thuật; tổ thiết kế bối cảnh", "pos": "phrase"},
    # 2347: bad blood
    {"ipa": "/bæd blʌd/", "vi": "mối thù hằn; hiềm khích căm ghét", "pos": "phrase"},
    # 2348: ball game
    {"ipa": "/bɔːl ɡeɪm/", "vi": "trận đấu bóng; cục diện mới", "pos": "phrase"},
    # 2349: beat down
    {"ipa": "/biːt daʊn/", "vi": "mặt trời chiếu gắt; mặc cả hạ giá", "pos": "phrase"},
    # 2350: blue law
    {"ipa": "/bluː lɔː/", "vi": "luật cấm hoạt động ngày Chủ nhật", "pos": "phrase"},
    # 2351: blue story
    {"ipa": "/bluː ˈstɔːri/", "vi": "chuyện tiếu lâm tiếu táo mặn mà", "pos": "phrase"},
    # 2352: board of education
    {"ipa": "/bɔːrd ʌv ˌɛdʒəˈkeɪʃən/", "vi": "hội đồng giáo dục địa phương", "pos": "phrase"},
    # 2353: bring outside
    {"ipa": "/brɪŋ ˌaʊtˈsaɪd/", "vi": "đưa ra ngoài khu vực", "pos": "phrase"},
    # 2354: building department
    {"ipa": "/ˈbɪldɪŋ dɪˈpɑːrtmənt/", "vi": "sở quản lý xây dựng đô thị", "pos": "phrase"},
    # 2355: call attention
    {"ipa": "/kɔːl əˈtɛnʃən/", "vi": "kêu gọi sự chú ý tập trung", "pos": "phrase"},
    # 2356: card game
    {"ipa": "/kɑːrd ɡeɪm/", "vi": "trò chơi đánh bài xì phé", "pos": "phrase"},
    # 2357: community center
    {"ipa": "/kəˈmjuːnəti ˈsɛntər/", "vi": "trung tâm văn hóa cộng đồng", "pos": "phrase"},
    # 2358: decision making
    {"ipa": "/dɪˈsɪʒən ˈmeɪkɪŋ/", "vi": "quá trình ra quyết định chiến lược", "pos": "phrase"},
    # 2359: die away
    {"ipa": "/daɪ əˈweɪ/", "vi": "âm thanh lịm dần; tắt dần trong gió", "pos": "phrase"},
    # 2360: double take
    {"ipa": "/ˈdʌbəl teɪk/", "vi": "sững sờ nhìn lại lần hai kinh ngạc", "pos": "phrase"},
    # 2361: extra time
    {"ipa": "/ˈɛkstrə taɪm/", "vi": "hai hiệp phụ bù giờ thi đấu", "pos": "phrase"},
    # 2362: family practice
    {"ipa": "/ˈfæməli ˈpræktɪs/", "vi": "chuyên khoa y học bác sĩ gia đình", "pos": "phrase"},
    # 2363: final cut
    {"ipa": "/ˈfaɪnəl kʌt/", "vi": "bản dựng phim hoàn chỉnh cuối", "pos": "phrase"},
    # 2364: fine art
    {"ipa": "/faɪn ɑːrt/", "vi": "nghệ thuật thị giác; mỹ thuật", "pos": "phrase"},
    # 2365: fire department
    {"ipa": "/ˈfaɪər dɪˈpɑːrtmənt/", "vi": "sở phòng cháy chữa cháy", "pos": "phrase"},
    # 2366: food bank
    {"ipa": "/fuːd bæŋk/", "vi": "ngân hàng thực phẩm cứu trợ", "pos": "phrase"},
    # 2367: football season
    {"ipa": "/ˈfʊtˌbɔːl ˈsiːzən/", "vi": "mùa giải thi đấu bóng đá bóng bầu", "pos": "phrase"},
    # 2368: for the asking
    {"ipa": "/fɔːr ðə ˈæskɪŋ/", "vi": "chỉ cần mở lời hỏi là có ngay", "pos": "phrase"},
    # 2369: french person
    {"ipa": "/frɛntʃ ˈpɜːrsən/", "vi": "người mang quốc tịch Pháp", "pos": "phrase"},
    # 2370: future perfect
    {"ipa": "/ˈfjuːtʃər ˈpɜːrfɪkt/", "vi": "thì tương lai hoàn thành ngữ pháp", "pos": "phrase"},
    # 2371: great russian
    {"ipa": "/ɡreɪt ˈrʌʃən/", "vi": "người Nga Đại Nga lịch sử", "pos": "phrase"},
    # 2372: ground control
    {"ipa": "/ɡraʊnd kənˈtroʊl/", "vi": "trạm điều khiển kiểm soát mặt đất", "pos": "phrase"},
    # 2373: ground level
    {"ipa": "/ɡraʊnd ˈlɛvəl/", "vi": "cao độ mặt đất; tầng trệt tòa nhà", "pos": "phrase"},
    # 2374: hair care
    {"ipa": "/hɛr kɛr/", "vi": "chăm sóc dưỡng tóc tạo kiểu", "pos": "phrase"},
    # 2375: happy event
    {"ipa": "/ˈhæpi ɪˈvɛnt/", "vi": "tin mừng sinh con; hỷ sự gia đình", "pos": "phrase"},
    # 2376: happy hour
    {"ipa": "/ˈhæpi ˈaʊər/", "vi": "giờ vàng giảm giá đồ uống quán bar", "pos": "phrase"},
    # 2377: king john
    {"ipa": "/kɪŋ dʒɑːn/", "vi": "Vua John của nước Anh", "pos": "phrase"},
    # 2378: land development
    {"ipa": "/lænd dɪˈvɛləpmənt/", "vi": "quy hoạch phát triển đất đai dự án", "pos": "phrase"},
    # 2379: league together
    {"ipa": "/liːɡ təˈɡɛðər/", "vi": "liên minh liên kết lại với nhau", "pos": "phrase"},
    # 2380: legal system
    {"ipa": "/ˈliːɡəl ˈsɪstəm/", "vi": "hệ thống thể chế luật pháp", "pos": "phrase"},
    # 2381: living space
    {"ipa": "/ˈlɪvɪŋ speɪs/", "vi": "không gian sinh tồn; diện tích sống", "pos": "phrase"},
    # 2382: main street
    {"ipa": "/meɪn striːt/", "vi": "đường phố chính; khu thương mại", "pos": "phrase"},
    # 2383: major term
    {"ipa": "/ˈmeɪdʒər tɜːrm/", "vi": "đại từ trong tam đoạn luận logic", "pos": "phrase"},
    # 2384: market price
    {"ipa": "/ˈmɑːrkɪt praɪs/", "vi": "giá cả theo cơ chế thị trường", "pos": "phrase"},
    # 2385: market town
    {"ipa": "/ˈmɑːrkɪt taʊn/", "vi": "thị trấn họp phiên chợ quê", "pos": "phrase"},
    # 2386: married man
    {"ipa": "/ˈmærid mæn/", "vi": "người đàn ông đã có gia đình", "pos": "phrase"},
    # 2387: medical history
    {"ipa": "/ˈmɛdɪkəl ˈhɪstəri/", "vi": "tiền sử bệnh lý; bệnh sử bệnh nhân", "pos": "phrase"},
    # 2388: middle class
    {"ipa": "/ˈmɪdəl klæs/", "vi": "tầng lớp giai cấp trung lưu", "pos": "phrase"},
    # 2389: military police
    {"ipa": "/ˈmɪlətɛri pəˈliːs/", "vi": "quân cảnh; cảnh sát quân sự", "pos": "phrase"},
    # 2390: natural order
    {"ipa": "/ˈnætʃərəl ˈɔːrdər/", "vi": "trật tự thuận theo tự nhiên", "pos": "phrase"},
    # 2391: north star
    {"ipa": "/nɔːrθ stɑːr/", "vi": "sao Bắc Cực định hướng trên trời", "pos": "phrase"},
    # 2392: of sound mind
    {"ipa": "/ʌv saʊnd maɪnd/", "vi": "tinh thần minh mẫn sáng suốt", "pos": "phrase"},
    # 2393: poor person
    {"ipa": "/pʊr ˈpɜːrsən/", "vi": "người nghèo khổ thiếu thốn", "pos": "phrase"},
    # 2394: property line
    {"ipa": "/ˈprɑːpərti laɪn/", "vi": "ranh giới quyền sở hữu đất đai", "pos": "phrase"},
    # 2395: quick time
    {"ipa": "/kwɪk taɪm/", "vi": "nhịp bước hành quân nhanh", "pos": "phrase"},
    # 2396: school district
    {"ipa": "/skuːl ˈdɪstrɪkt/", "vi": "khu học chánh quản lý trường học", "pos": "phrase"},
    # 2397: sell out
    {"ipa": "/sɛl aʊt/", "vi": "bán sạch vé hàng; phản bội lý tưởng", "pos": "phrase"},
    # 2398: sell up
    {"ipa": "/sɛl ʌp/", "vi": "bán thanh lý hết nhà đất tài sản", "pos": "phrase"},
    # 2399: serious music
    {"ipa": "/ˈsɪriəs ˈmjuːzɪk/", "vi": "dòng nhạc cổ điển hàn lâm bác học", "pos": "phrase"},
]

with open('scratch/b21_r05_raw_p4.json') as f:
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

with open('scratch/b21_r05_p4.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r05_p4.json created successfully and validated!")
