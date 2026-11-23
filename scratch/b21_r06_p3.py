import json

# Manual word-by-word cognitive review for Batch 21 Round 6 Part 3 (records 2700-2799, IDs 200k.002702 to 200k.002801)
reviewed_entries = [
    # 2700: water table
    {"ipa": "/ˈwɔːtər ˈteɪbəl/", "vi": "mực nước ngầm; tầng nước ngầm", "pos": "phrase"},
    # 2701: wear on
    {"ipa": "/wɛr ɑːn/", "vi": "thời gian trôi qua chậm chạp", "pos": "phrase"},
    # 2702: west bank
    {"ipa": "/wɛst bæŋk/", "vi": "vùng Bờ Tây sông Jordan; bờ tây", "pos": "phrase"},
    # 2703: word sense
    {"ipa": "/wɜːrd sɛns/", "vi": "ngữ nghĩa của từ vựng; nét nghĩa", "pos": "phrase"},
    # 2704: air attack
    {"ipa": "/ɛr əˈtæk/", "vi": "cuộc không kích; đòn oanh tạc bay", "pos": "phrase"},
    # 2705: art director
    {"ipa": "/ɑːrt dəˈrɛktər/", "vi": "giám đốc nghệ thuật tạo hình", "pos": "phrase"},
    # 2706: black sea
    {"ipa": "/blæk siː/", "vi": "vùng Biển Đen giữa châu Âu và Á", "pos": "phrase"},
    # 2707: board member
    {"ipa": "/bɔːrd ˈmɛmbər/", "vi": "thành viên hội đồng quản trị", "pos": "phrase"},
    # 2708: body hair
    {"ipa": "/ˈbɑːdi hɛr/", "vi": "lông trên cơ thể; lông mao trên da", "pos": "phrase"},
    # 2709: call box
    {"ipa": "/kɔːl bɑːks/", "vi": "bốt điện thoại công cộng bên đường", "pos": "phrase"},
    # 2710: cash in on
    {"ipa": "/kæʃ ɪn ɑːn/", "vi": "trục lợi kiếm chác từ cơ hội", "pos": "phrase"},
    # 2711: cash out
    {"ipa": "/kæʃ aʊt/", "vi": "rút sạch tiền mặt; thanh toán tiền", "pos": "phrase"},
    # 2712: center field
    {"ipa": "/ˈsɛntər fiːld/", "vi": "khu vực giữa sân ngoài bóng chày", "pos": "phrase"},
    # 2713: church father
    {"ipa": "/tʃɜːrtʃ ˈfɑːðər/", "vi": "các giáo phụ Kitô giáo thời đầu", "pos": "phrase"},
    # 2714: civil time
    {"ipa": "/ˈsɪvəl taɪm/", "vi": "giờ dân dụng chính thức pháp lý", "pos": "phrase"},
    # 2715: color in
    {"ipa": "/ˈkʌlər ɪn/", "vi": "tô màu kín hình vẽ phác thảo", "pos": "phrase"},
    # 2716: common land
    {"ipa": "/ˈkɑːmən lænd/", "vi": "khu đất công cộng của cộng đồng", "pos": "phrase"},
    # 2717: community property
    {"ipa": "/kəˈmjuːnəti ˈprɑːpərti/", "vi": "tài sản chung của vợ chồng sau cưới", "pos": "phrase"},
    # 2718: county town
    {"ipa": "/ˈkaʊnti taʊn/", "vi": "thị trấn trung tâm hành chính hạt", "pos": "phrase"},
    # 2719: department of english
    {"ipa": "/dɪˈpɑːrtmənt ʌv ˈɪŋɡlɪʃ/", "vi": "khoa tiếng Anh trường đại học", "pos": "phrase"},
    # 2720: district line
    {"ipa": "/ˈdɪstrɪkt laɪn/", "vi": "tuyến đường ngầm; ranh giới địa hạt", "pos": "phrase"},
    # 2721: double play
    {"ipa": "/ˈdʌbəl pleɪ/", "vi": "pha loại kép hai đối thủ bóng chày", "pos": "phrase"},
    # 2722: english department
    {"ipa": "/ˈɪŋɡlɪʃ dɪˈpɑːrtmənt/", "vi": "khoa ngữ văn Anh trường đại học", "pos": "phrase"},
    # 2723: fan out
    {"ipa": "/fæn aʊt/", "vi": "xòe ra hình quạt; tỏa ra các hướng", "pos": "phrase"},
    # 2724: field event
    {"ipa": "/fiːld ɪˈvɛnt/", "vi": "môn thi đấu trên sân điền kinh bãi", "pos": "phrase"},
    # 2725: field of view
    {"ipa": "/fiːld ʌv vjuː/", "vi": "trường nhìn thị trường quang học", "pos": "phrase"},
    # 2726: field test
    {"ipa": "/fiːld tɛst/", "vi": "thử nghiệm thực tế ngoài thực địa", "pos": "phrase"},
    # 2727: first degree
    {"ipa": "/fɜːrst dɪˈɡriː/", "vi": "bỏng độ một; giết người cấp độ một", "pos": "phrase"},
    # 2728: first floor
    {"ipa": "/fɜːrst flɔːr/", "vi": "tầng trệt tầng một của tòa nhà", "pos": "phrase"},
    # 2729: foreign office
    {"ipa": "/ˈfɔːrən ˈɔːfɪs/", "vi": "Bộ Ngoại giao của vương quốc Anh", "pos": "phrase"},
    # 2730: gas company
    {"ipa": "/ɡæs ˈkʌmpəni/", "vi": "công ty cung cấp khí đốt dân dụng", "pos": "phrase"},
    # 2731: ground plan
    {"ipa": "/ɡraʊnd plæn/", "vi": "bản vẽ mặt bằng tầng trệt nhà ở", "pos": "phrase"},
    # 2732: gun down
    {"ipa": "/ɡʌn daʊn/", "vi": "nổ súng bắn hạ; hạ sát bằng súng", "pos": "phrase"},
    # 2733: half door
    {"ipa": "/hæf dɔːr/", "vi": "cửa lửng hai cánh trên dưới", "pos": "phrase"},
    # 2734: home computer
    {"ipa": "/hoʊm kəmˈpjuːtər/", "vi": "máy vi tính sử dụng trong gia đình", "pos": "phrase"},
    # 2735: lady day
    {"ipa": "/ˈleɪdi deɪ/", "vi": "ngày lễ Truyền Tin Đức Mẹ", "pos": "phrase"},
    # 2736: law practice
    {"ipa": "/lɔː ˈpræktɪs/", "vi": "văn phòng luật; việc hành nghề luật", "pos": "phrase"},
    # 2737: light upon
    {"ipa": "/laɪt əˈpɑːn/", "vi": "tình cờ bắt gặp; bất chợt chú ý", "pos": "phrase"},
    # 2738: line of products
    {"ipa": "/laɪn ʌv ˈprɑːdəkts/", "vi": "dòng sản phẩm hàng hóa cùng loại", "pos": "phrase"},
    # 2739: living trust
    {"ipa": "/ˈlɪvɪŋ trʌst/", "vi": "quỹ ủy thác tài sản khi còn sống", "pos": "phrase"},
    # 2740: low quality
    {"ipa": "/loʊ ˈkwɑːləti/", "vi": "chất lượng kém phẩm chất thấp kém", "pos": "phrase"},
    # 2741: luck it
    {"ipa": "/lʌk ɪt/", "vi": "phó mặc cho may rủi; trông cậy số", "pos": "phrase"},
    # 2742: major league
    {"ipa": "/ˈmeɪdʒər liːɡ/", "vi": "giải thể thao nhà nghề đỉnh cao", "pos": "phrase"},
    # 2743: march king
    {"ipa": "/mɑːrtʃ kɪŋ/", "vi": "ông vua hành khúc John Philip Sousa", "pos": "phrase"},
    # 2744: market value
    {"ipa": "/ˈmɑːrkɪt ˈvæljuː/", "vi": "giá trị thị trường thực tế tài sản", "pos": "phrase"},
    # 2745: military force
    {"ipa": "/ˈmɪlətɛri fɔːrs/", "vi": "lực lượng quân đội; sức mạnh vũ lực", "pos": "phrase"},
    # 2746: military issue
    {"ipa": "/ˈmɪlətɛri ˈɪʃuː/", "vi": "quân trang quân nhu do quân đội cấp", "pos": "phrase"},
    # 2747: mine run
    {"ipa": "/maɪn rʌn/", "vi": "quặng thô chưa qua tuyển chọn sàng", "pos": "phrase"},
    # 2748: numbers game
    {"ipa": "/ˈnʌmbərz ɡeɪm/", "vi": "trò chơi quay số cờ bạc; trò số má", "pos": "phrase"},
    # 2749: office staff
    {"ipa": "/ˈɔːfɪs stæf/", "vi": "tập thể cán bộ nhân viên văn phòng", "pos": "phrase"},
    # 2750: out of stock
    {"ipa": "/aʊt ʌv stɑːk/", "vi": "tạm thời hết hàng trong kho lưu", "pos": "phrase"},
    # 2751: party wall
    {"ipa": "/ˈpɑːrti wɔːl/", "vi": "bức tường ngăn chung giữa hai nhà", "pos": "phrase"},
    # 2752: piece of music
    {"ipa": "/piːs ʌv ˈmjuːzɪk/", "vi": "một bản nhạc; tác phẩm khí nhạc", "pos": "phrase"},
    # 2753: police chief
    {"ipa": "/pəˈliːs tʃiːf/", "vi": "trưởng công an; cảnh sát trưởng", "pos": "phrase"},
    # 2754: practice of law
    {"ipa": "/ˈpræktɪs ʌv lɔː/", "vi": "nghề luật sư; hành nghề tư pháp", "pos": "phrase"},
    # 2755: present moment
    {"ipa": "/ˈprɛzənt ˈmoʊmənt/", "vi": "thời khắc hiện tại; ngay lúc này", "pos": "phrase"},
    # 2756: private road
    {"ipa": "/ˈpraɪvət roʊd/", "vi": "đường đi nội bộ; ngõ sở hữu tư nhân", "pos": "phrase"},
    # 2757: public eye
    {"ipa": "/ˈpʌblɪk aɪ/", "vi": "sự quan sát của công chúng dư luận", "pos": "phrase"},
    # 2758: race problem
    {"ipa": "/reɪs ˈprɑːbləm/", "vi": "vấn đề bất bình đẳng chủng tộc", "pos": "phrase"},
    # 2759: radio set
    {"ipa": "/ˈreɪdioʊ sɛt/", "vi": "máy thu thanh; đài vô tuyến cát-sét", "pos": "phrase"},
    # 2760: reach into
    {"ipa": "/riːtʃ ˈɪntuː/", "vi": "thò tay vào trong; thọc sâu vào", "pos": "phrase"},
    # 2761: research staff
    {"ipa": "/ˈriːsɜːrtʃ stæf/", "vi": "đội ngũ cán bộ nghiên cứu khoa học", "pos": "phrase"},
    # 2762: rights issue
    {"ipa": "/raɪts ˈɪʃuː/", "vi": "đợt phát hành quyền mua cổ phiếu", "pos": "phrase"},
    # 2763: road sense
    {"ipa": "/roʊd sɛns/", "vi": "phản xạ lái xe; ý thức đi đường bộ", "pos": "phrase"},
    # 2764: road test
    {"ipa": "/roʊd tɛst/", "vi": "chạy thử xe trên đường thực tế", "pos": "phrase"},
    # 2765: rock music
    {"ipa": "/rɑːk ˈmjuːzɪk/", "vi": "thể loại nhạc rock sôi động mạnh", "pos": "phrase"},
    # 2766: security department
    {"ipa": "/sɪˈkjʊrəti dɪˈpɑːrtmənt/", "vi": "phòng bảo vệ; ban an ninh cơ quan", "pos": "phrase"},
    # 2767: security force
    {"ipa": "/sɪˈkjʊrəti fɔːrs/", "vi": "lực lượng an ninh giữ gìn trật tự", "pos": "phrase"},
    # 2768: set ahead
    {"ipa": "/sɛt əˈhɛd/", "vi": "chỉnh đồng hồ chạy sớm lên; đẩy sớm", "pos": "phrase"},
    # 2769: single bed
    {"ipa": "/ˈsɪŋɡəl bɛd/", "vi": "chiếc giường đơn dành cho một người", "pos": "phrase"},
    # 2770: sleep together
    {"ipa": "/sliːp təˈɡɛðər/", "vi": "ngủ cùng giường; quan hệ xác thịt", "pos": "phrase"},
    # 2771: spring up
    {"ipa": "/sprɪŋ ʌp/", "vi": "mọc lên như nấm; nảy sinh bất ngờ", "pos": "phrase"},
    # 2772: staff office
    {"ipa": "/stæf ˈɔːfɪs/", "vi": "văn phòng nhân sự quản trị nhân sự", "pos": "phrase"},
    # 2773: starting post
    {"ipa": "/ˈstɑːrtɪŋ poʊst/", "vi": "cột mốc xuất phát cuộc đua ngựa", "pos": "phrase"},
    # 2774: state of nature
    {"ipa": "/steɪt ʌv ˈneɪtʃər/", "vi": "trạng thái tự nhiên nguyên sơ triết", "pos": "phrase"},
    # 2775: straight line
    {"ipa": "/streɪt laɪn/", "vi": "đường thẳng tắp; vạch kẻ thẳng tắp", "pos": "phrase"},
    # 2776: touch on
    {"ipa": "/tʌtʃ ɑːn/", "vi": "bàn lướt qua; đề cập sơ lược đến", "pos": "phrase"},
    # 2777: trump out
    {"ipa": "/trʌmp aʊt/", "vi": "rêu rao rùm beng; loan tin giật gân", "pos": "phrase"},
    # 2778: university of washington
    {"ipa": "/ˌjuːnɪˈvɜːrsəti ʌv ˈwɑːʃɪŋtən/", "vi": "Đại học Washington tại Hoa Kỳ", "pos": "phrase"},
    # 2779: waiting area
    {"ipa": "/ˈweɪtɪŋ ˈɛriə/", "vi": "khu vực sảnh chờ hành khách trạm xe", "pos": "phrase"},
    # 2780: ways and means
    {"ipa": "/weɪz ænd miːnz/", "vi": "phương sách và nguồn lực tài chính", "pos": "phrase"},
    # 2781: wear out
    {"ipa": "/wɛr aʊt/", "vi": "mòn rách tả tơi; kiệt sức rã rời", "pos": "phrase"},
    # 2782: white river
    {"ipa": "/waɪt ˈrɪvər/", "vi": "dòng sông White River tại nước Mỹ", "pos": "phrase"},
    # 2783: work unit
    {"ipa": "/wɜːrk ˈjuːnɪt/", "vi": "đơn vị đo lường công cơ học jun", "pos": "phrase"},
    # 2784: written matter
    {"ipa": "/ˈrɪtən ˈmætər/", "vi": "tài liệu văn bản giấy tờ in ấn", "pos": "phrase"},
    # 2785: gods
    {"ipa": "/ɡɑːdz/", "vi": "các vị thần linh; những đấng thần", "pos": "noun"},
    # 2786: act upon
    {"ipa": "/ækt əˈpɑːn/", "vi": "hành động theo lời khuyên; tác động", "pos": "phrase"},
    # 2787: air cover
    {"ipa": "/ɛr ˈkʌvər/", "vi": "sự yểm trợ hỏa lực đường không", "pos": "phrase"},
    # 2788: average cost
    {"ipa": "/ˈævərɪdʒ kɔːst/", "vi": "chi phí bình quân trên mỗi đơn vị", "pos": "phrase"},
    # 2789: black box
    {"ipa": "/blæk bɑːks/", "vi": "hộp đen ghi dữ liệu chuyến bay", "pos": "phrase"},
    # 2790: bring round
    {"ipa": "/brɪŋ raʊnd/", "vi": "làm cho hồi tỉnh; thuyết phục thuận", "pos": "phrase"},
    # 2791: by luck
    {"ipa": "/baɪ lʌk/", "vi": "nhờ may mắn tình cờ; do số đỏ", "pos": "phrase"},
    # 2792: career girl
    {"ipa": "/kəˈrɪr ɡɜːrl/", "vi": "cô gái theo đuổi đam mê sự nghiệp", "pos": "phrase"},
    # 2793: check character
    {"ipa": "/tʃɛk ˈkærəktər/", "vi": "ký tự kiểm tra lỗi luồng dữ liệu", "pos": "phrase"},
    # 2794: choose up
    {"ipa": "/tʃuːz ʌp/", "vi": "chia phe chọn người vào hai đội", "pos": "phrase"},
    # 2795: clean house
    {"ipa": "/kliːn haʊs/", "vi": "dọn dẹp nhà cửa; thanh trừng nội bộ", "pos": "phrase"},
    # 2796: closed in
    {"ipa": "/kloʊzd ɪn/", "vi": "bị vây kín mít; không gian bít bùng", "pos": "phrase"},
    # 2797: cold water
    {"ipa": "/koʊld ˈwɔːtər/", "vi": "gáo nước lạnh dập tắt nhuệ khí", "pos": "phrase"},
    # 2798: computer game
    {"ipa": "/kəmˈpjuːtər ɡeɪm/", "vi": "trò chơi điện tử trên máy vi tính", "pos": "phrase"},
    # 2799: cover girl
    {"ipa": "/ˈkʌvər ɡɜːrl/", "vi": "người mẫu ảnh bìa tạp chí quyến rũ", "pos": "phrase"},
]

with open('scratch/b21_r06_raw_p3.json') as f:
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

with open('scratch/b21_r06_p3.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r06_p3.json created successfully and validated!")
