import json

# Manual word-by-word cognitive review for Batch 21 Round 7 Part 3 (records 3200-3299, IDs 200k.003202 to 200k.003301)
reviewed_entries = [
    # 3200: fast break
    {"ipa": "/fæst breɪk/", "vi": "pha phản công nhanh chớp nhoáng rổ", "pos": "phrase"},
    # 3201: father figure
    {"ipa": "/ˈfɑːðər ˈfɪɡjər/", "vi": "hình mẫu người cha; tấm gương cha", "pos": "phrase"},
    # 3202: female body
    {"ipa": "/ˈfiːmeɪl ˈbɑːdi/", "vi": "thân thể phụ nữ; cơ thể nữ giới", "pos": "phrase"},
    # 3203: field hospital
    {"ipa": "/fiːld ˈhɑːspɪtl/", "vi": "bệnh viện dã chiến tiền tuyến cứu", "pos": "phrase"},
    # 3204: football player
    {"ipa": "/ˈfʊtˌbɔːl ˈpleɪər/", "vi": "cầu thủ bóng đá; cầu thủ bóng bầu", "pos": "phrase"},
    # 3205: general manager
    {"ipa": "/ˈdʒɛnərəl ˈmænɪdʒər/", "vi": "tổng giám đốc; giám đốc điều hành", "pos": "phrase"},
    # 3206: glass in
    {"ipa": "/ɡlæs ɪn/", "vi": "lắp kính che chắn kín hàng hiên", "pos": "phrase"},
    # 3207: good weather
    {"ipa": "/ɡʊd ˈwɛðər/", "vi": "tiết trời thuận hòa; thời tiết đẹp", "pos": "phrase"},
    # 3208: green gold
    {"ipa": "/ɡriːn ɡoʊld/", "vi": "hợp kim vàng lục; vàng xanh quý giá", "pos": "phrase"},
    # 3209: group insurance
    {"ipa": "/ɡruːp ɪnˈʃʊrəns/", "vi": "hợp đồng bảo hiểm theo nhóm tập thể", "pos": "phrase"},
    # 3210: hair space
    {"ipa": "/hɛr speɪs/", "vi": "khoảng trắng cực hẹp giữa các chữ", "pos": "phrase"},
    # 3211: happen upon
    {"ipa": "/ˈhæpən əˈpɑːn/", "vi": "tình cờ bắt gặp; ngẫu nhiên thấy", "pos": "phrase"},
    # 3212: heat up
    {"ipa": "/hiːt ʌp/", "vi": "hâm nóng lại; không khí nóng lên", "pos": "phrase"},
    # 3213: heavy water
    {"ipa": "/ˈhɛvi ˈwɔːtər/", "vi": "nước nặng điều tốc lò phản ứng hạt", "pos": "phrase"},
    # 3214: high commission
    {"ipa": "/haɪ kəˈmɪʃən/", "vi": "cơ quan cao ủy; cơ quan đại sứ quán", "pos": "phrase"},
    # 3215: holy see
    {"ipa": "/ˈhoʊli siː/", "vi": "Tòa Thánh Vatican; giáo triều La Mã", "pos": "phrase"},
    # 3216: holy year
    {"ipa": "/ˈhoʊli jɪr/", "vi": "Năm Thánh đại ân xá Công giáo Roma", "pos": "phrase"},
    # 3217: hot stuff
    {"ipa": "/hɑːt stʌf/", "vi": "người quyến rũ; điều sốt dẻo hay ho", "pos": "phrase"},
    # 3218: insurance company
    {"ipa": "/ɪnˈʃʊrəns ˈkʌmpəni/", "vi": "công ty kinh doanh bảo hiểm rủi ro", "pos": "phrase"},
    # 3219: interest rate
    {"ipa": "/ˈɪntrəst reɪt/", "vi": "mức lãi suất tiền vay ngân hàng", "pos": "phrase"},
    # 3220: law of nature
    {"ipa": "/lɔː ʌv ˈneɪtʃər/", "vi": "quy luật tự nhiên tất yếu của trời", "pos": "phrase"},
    # 3221: letter case
    {"ipa": "/ˈlɛtər keɪs/", "vi": "khay đựng chữ in chì; hộp đựng thư", "pos": "phrase"},
    # 3222: line coach
    {"ipa": "/laɪn koʊtʃ/", "vi": "HLV tuyến tiền vệ bóng bầu dục", "pos": "phrase"},
    # 3223: major form class
    {"ipa": "/ˈmeɪdʒər fɔːrm klæs/", "vi": "từ loại chính danh động tính từ ngữ", "pos": "phrase"},
    # 3224: medical bill
    {"ipa": "/ˈmɛdɪkəl bɪl/", "vi": "hóa đơn viện phí khám chữa bệnh", "pos": "phrase"},
    # 3225: minute book
    {"ipa": "/ˈmɪnɪt bʊk/", "vi": "sổ ghi chép biên bản các cuộc họp", "pos": "phrase"},
    # 3226: mother figure
    {"ipa": "/ˈmʌðər ˈfɪɡjər/", "vi": "hình mẫu người mẹ; hình bóng mẹ", "pos": "phrase"},
    # 3227: personal property
    {"ipa": "/ˈpɜːrsənəl ˈprɑːpərti/", "vi": "động sản thuộc quyền sở hữu cá nhân", "pos": "phrase"},
    # 3228: phone card
    {"ipa": "/foʊn kɑːrd/", "vi": "thẻ cào nạp tiền cước điện thoại", "pos": "phrase"},
    # 3229: plant life
    {"ipa": "/plænt laɪf/", "vi": "thế giới thực vật cỏ cây hoa lá", "pos": "phrase"},
    # 3230: police officer
    {"ipa": "/pəˈliːs ˈɔːfɪsər/", "vi": "viên cảnh sát tuần tra công vụ", "pos": "phrase"},
    # 3231: power train
    {"ipa": "/ˈpaʊər treɪn/", "vi": "hệ thống dẫn động truyền lực cơ khí", "pos": "phrase"},
    # 3232: power unit
    {"ipa": "/ˈpaʊər ˈjuːnɪt/", "vi": "bộ cấp nguồn điện năng; đơn vị công", "pos": "phrase"},
    # 3233: price increase
    {"ipa": "/praɪs ˈɪnkriːs/", "vi": "sự tăng giá cả hàng hóa leo thang", "pos": "phrase"},
    # 3234: private property
    {"ipa": "/ˈpraɪvət ˈprɑːpərti/", "vi": "tài sản quyền sở hữu tư nhân nhà ở", "pos": "phrase"},
    # 3235: public opinion
    {"ipa": "/ˈpʌblɪk əˈpɪnjən/", "vi": "dư luận xã hội; ý kiến công chúng", "pos": "phrase"},
    # 3236: rate of interest
    {"ipa": "/reɪt ʌv ˈɪntrəst/", "vi": "mức tỷ lệ lãi suất phần trăm vay", "pos": "phrase"},
    # 3237: ready and waiting
    {"ipa": "/ˈrɛdi ænd ˈweɪtɪŋ/", "vi": "sẵn sàng tươm tất và đang chờ đợi", "pos": "phrase"},
    # 3238: red river
    {"ipa": "/rɛd ˈrɪvər/", "vi": "sông Hồng tại miền Bắc Việt Nam", "pos": "phrase"},
    # 3239: return key
    {"ipa": "/rɪˈtɜːrn kiː/", "vi": "phím bấm Enter xuống dòng máy tính", "pos": "phrase"},
    # 3240: search party
    {"ipa": "/sɜːrtʃ ˈpɑːrti/", "vi": "đoàn người tìm kiếm cứu hộ cứu nạn", "pos": "phrase"},
    # 3241: ship money
    {"ipa": "/ʃɪp ˈmʌni/", "vi": "thuế đóng tàu chiến của nước Anh", "pos": "phrase"},
    # 3242: sit around
    {"ipa": "/sɪt əˈraʊnd/", "vi": "ngồi không rảnh rỗi; ngồi tán gẫu", "pos": "phrase"},
    # 3243: sleep talking
    {"ipa": "/sliːp ˈtɔːkɪŋ/", "vi": "tật nói mê sảng trong giấc ngủ đêm", "pos": "phrase"},
    # 3244: space walk
    {"ipa": "/speɪs wɔːk/", "vi": "chuyến đi bộ ra ngoài không gian vũ", "pos": "phrase"},
    # 3245: special effect
    {"ipa": "/ˈspɛʃəl ɪˈfɛkt/", "vi": "hiệu ứng kỹ xảo điện ảnh đặc biệt", "pos": "phrase"},
    # 3246: special interest group
    {"ipa": "/ˈspɛʃəl ˈɪntrəst ɡruːp/", "vi": "nhóm vận động lợi ích đặc thù", "pos": "phrase"},
    # 3247: stock company
    {"ipa": "/stɑːk ˈkʌmpəni/", "vi": "công ty cổ phần; đoàn kịch lưu diễn", "pos": "phrase"},
    # 3248: sunday school
    {"ipa": "/ˈsʌndeɪ skuːl/", "vi": "lớp giáo lý Chúa nhật cho thiếu nhi", "pos": "phrase"},
    # 3249: tax policy
    {"ipa": "/tæks ˈpɑːləsi/", "vi": "chính sách thuế khóa của chính phủ", "pos": "phrase"},
    # 3250: test range
    {"ipa": "/tɛst reɪndʒ/", "vi": "bãi thử nghiệm đạn đạo vũ khí", "pos": "phrase"},
    # 3251: the holy see
    {"ipa": "/ðə ˈhoʊli siː/", "vi": "Tòa Thánh Vatican cai quản Giáo hội", "pos": "phrase"},
    # 3252: travel along
    {"ipa": "/ˈtrævəl əˈlɔːŋ/", "vi": "di chuyển dọc theo lộ trình tuyến", "pos": "phrase"},
    # 3253: waiting list
    {"ipa": "/ˈweɪtɪŋ lɪst/", "vi": "danh sách hàng chờ xét duyệt nhận", "pos": "phrase"},
    # 3254: water gun
    {"ipa": "/ˈwɔːtər ɡʌn/", "vi": "khẩu súng nước đồ chơi trẻ em", "pos": "phrase"},
    # 3255: winning post
    {"ipa": "/ˈwɪnɪŋ poʊst/", "vi": "cột mốc vạch đích cuộc đua ngựa", "pos": "phrase"},
    # 3256: writing board
    {"ipa": "/ˈraɪtɪŋ bɔːrd/", "vi": "tấm bảng viết phấn học sinh lớp học", "pos": "phrase"},
    # 3257: written account
    {"ipa": "/ˈrɪtən əˈkaʊnt/", "vi": "bản tường trình ghi bằng văn bản", "pos": "phrase"},
    # 3258: written record
    {"ipa": "/ˈrɪtən ˈrɛkərd/", "vi": "hồ sơ tài liệu lưu trữ bằng văn bản", "pos": "phrase"},
    # 3259: nationals
    {"ipa": "/ˈnæʃənəlz/", "vi": "các công dân quốc gia; giải vô địch", "pos": "noun"},
    # 3260: smalls
    {"ipa": "/smɔːlz/", "vi": "đồ lót nhỏ; những món đồ vụn vặt", "pos": "noun"},
    # 3261: whiter
    {"ipa": "/ˈwaɪtər/", "vi": "trắng hơn; trong sạch hơn rõ rệt", "pos": "adj"},
    # 3262: whites
    {"ipa": "/waɪts/", "vi": "người da trắng; lòng trắng trứng gà", "pos": "noun"},
    # 3263: whitest
    {"ipa": "/ˈwaɪtɪst/", "vi": "trắng nhất; trong sạch thuần khiết", "pos": "adj"},
    # 3264: art rock
    {"ipa": "/ɑːrt rɑːk/", "vi": "dòng nhạc rock nghệ thuật hàn lâm", "pos": "phrase"},
    # 3265: associated state
    {"ipa": "/əˈsoʊsiˌeɪtɪd steɪt/", "vi": "quốc gia liên kết tự trị ngoại giao", "pos": "phrase"},
    # 3266: bank of england
    {"ipa": "/bæŋk ʌv ˈɪŋɡlənd/", "vi": "Ngân hàng Trung ương của nước Anh", "pos": "phrase"},
    # 3267: bed rest
    {"ipa": "/bɛd rɛst/", "vi": "tĩnh dưỡng nằm nghỉ ngơi tại giường", "pos": "phrase"},
    # 3268: beyond control
    {"ipa": "/bɪˈjɑːnd kənˈtroʊl/", "vi": "vượt khỏi tầm kiểm soát xử lý", "pos": "phrase"},
    # 3269: block off
    {"ipa": "/blɑːk ɔːf/", "vi": "rào chắn phong tỏa lối đi đường", "pos": "phrase"},
    # 3270: blood test
    {"ipa": "/blʌd tɛst/", "vi": "xét nghiệm máu phân tích sinh hóa", "pos": "phrase"},
    # 3271: call centre
    {"ipa": "/kɔːl ˈsɛntər/", "vi": "tổng đài hỗ trợ chăm sóc khách hàng", "pos": "phrase"},
    # 3272: calling together
    {"ipa": "/ˈkɔːlɪŋ təˈɡɛðər/", "vi": "việc triệu tập hội họp đông đủ", "pos": "phrase"},
    # 3273: car train
    {"ipa": "/kɑːr treɪn/", "vi": "đoàn tàu hỏa chuyên chở xe ô tô", "pos": "phrase"},
    # 3274: center stage
    {"ipa": "/ˈsɛntər steɪdʒ/", "vi": "chính giữa sân khấu; tâm điểm chú ý", "pos": "phrase"},
    # 3275: central bank
    {"ipa": "/ˈsɛntrəl bæŋk/", "vi": "ngân hàng trung ương của quốc gia", "pos": "phrase"},
    # 3276: central park
    {"ipa": "/ˈsɛntrəl pɑːrk/", "vi": "Công viên Trung tâm tại New York", "pos": "phrase"},
    # 3277: church key
    {"ipa": "/tʃɜːrtʃ kiː/", "vi": "dụng cụ bật nắp chai bia thủ công", "pos": "phrase"},
    # 3278: church of england
    {"ipa": "/tʃɜːrtʃ ʌv ˈɪŋɡlənd/", "vi": "Giáo hội Anh giáo của nước Anh", "pos": "phrase"},
    # 3279: cross question
    {"ipa": "/krɔːs ˈkwɛstʃən/", "vi": "thẩm vấn chéo; đối chất gay gắt", "pos": "phrase"},
    # 3280: dead language
    {"ipa": "/dɛd ˈlæŋɡwɪdʒ/", "vi": "tử ngữ cổ không còn ai sử dụng nói", "pos": "phrase"},
    # 3281: defense system
    {"ipa": "/dɪˈfɛns ˈsɪstəm/", "vi": "hệ thống phòng thủ an ninh quốc gia", "pos": "phrase"},
    # 3282: dog star
    {"ipa": "/dɔːɡ stɑːr/", "vi": "ngôi sao Thiên Lang sáng nhất trời", "pos": "phrase"},
    # 3283: driving school
    {"ipa": "/ˈdraɪvɪŋ skuːl/", "vi": "trung tâm dạy lái xe ô tô cơ giới", "pos": "phrase"},
    # 3284: earth mother
    {"ipa": "/ɜːrθ ˈmʌðər/", "vi": "nữ thần Mẹ Đất phì nhiêu sinh sản", "pos": "phrase"},
    # 3285: english language
    {"ipa": "/ˈɪŋɡlɪʃ ˈlæŋɡwɪdʒ/", "vi": "ngôn ngữ tiếng Anh quốc tế phổ biến", "pos": "phrase"},
    # 3286: extra large
    {"ipa": "/ˈɛkstrə lɑːrdʒ/", "vi": "cỡ cực đại rất lớn; cỡ quần áo XL", "pos": "phrase"},
    # 3287: field goal
    {"ipa": "/fiːld ɡoʊl/", "vi": "cú sút ghi bàn bóng bầu dục; ném rổ", "pos": "phrase"},
    # 3288: fire watching
    {"ipa": "/ˈfaɪər ˈwɑːtʃɪŋ/", "vi": "nhiệm vụ tuần tra canh gác hỏa hoạn", "pos": "phrase"},
    # 3289: game fish
    {"ipa": "/ɡeɪm fɪʃ/", "vi": "loài cá câu thể thao giải trí biển", "pos": "phrase"},
    # 3290: general knowledge
    {"ipa": "/ˈdʒɛnərəl ˈnɑːlɪdʒ/", "vi": "tri thức hiểu biết phổ thông cơ bản", "pos": "phrase"},
    # 3291: general security services
    {"ipa": "/ˈdʒɛnərəl sɪˈkjʊrəti ˈsɜːrvɪsɪz/", "vi": "Cơ quan An ninh Nội địa Shin Bet", "pos": "phrase"},
    # 3292: german american
    {"ipa": "/ˈdʒɜːrmən əˈmɛrɪkən/", "vi": "người Mỹ mang dòng máu gốc Đức", "pos": "phrase"},
    # 3293: give notice
    {"ipa": "/ɡɪv ˈnoʊtɪs/", "vi": "nộp đơn thôi việc; báo trước nghỉ", "pos": "phrase"},
    # 3294: holy day
    {"ipa": "/ˈhoʊli deɪ/", "vi": "ngày đại lễ tôn giáo thiêng liêng", "pos": "phrase"},
    # 3295: in demand
    {"ipa": "/ɪn dɪˈmænd/", "vi": "được săn đón; bán chạy đắt khách", "pos": "phrase"},
    # 3296: kept woman
    {"ipa": "/kɛpt ˈwʊmən/", "vi": "người phụ nữ làm bồ nhí bao nuôi", "pos": "phrase"},
    # 3297: king james
    {"ipa": "/kɪŋ dʒeɪmz/", "vi": "Vua James Đệ Nhất của nước Anh", "pos": "phrase"},
    # 3298: king of england
    {"ipa": "/kɪŋ ʌv ˈɪŋɡlənd/", "vi": "Quốc vương trị vì vương quốc Anh", "pos": "phrase"},
    # 3299: leading question
    {"ipa": "/ˈliːdɪŋ ˈkwɛstʃən/", "vi": "câu hỏi mớm cung dẫn dụ định hướng", "pos": "phrase"},
]

with open('scratch/b21_r07_raw_p3.json') as f:
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

with open('scratch/b21_r07_p3.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r07_p3.json created successfully and validated!")
