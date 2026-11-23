import json

# Manual word-by-word cognitive review for Batch 21 Round 7 Part 5 (records 3400-3499, IDs 200k.003402 to 200k.003501)
reviewed_entries = [
    # 3400: hot dog
    {"ipa": "/hɑːt dɔːɡ/", "vi": "bánh mì kẹp xúc xích nóng hổi Mỹ", "pos": "phrase"},
    # 3401: human nature
    {"ipa": "/ˈhjuːmən ˈneɪtʃər/", "vi": "bản tính tự nhiên của con người", "pos": "phrase"},
    # 3402: ice age
    {"ipa": "/aɪs eɪdʒ/", "vi": "kỷ băng hà lạnh giá trong lịch sử", "pos": "phrase"},
    # 3403: internet site
    {"ipa": "/ˈɪntərnɛt saɪt/", "vi": "trang thông tin điện tử; trang web", "pos": "phrase"},
    # 3404: law degree
    {"ipa": "/lɔː dɪˈɡriː/", "vi": "bằng cử nhân cử chỉ ngành luật", "pos": "phrase"},
    # 3405: leading light
    {"ipa": "/ˈliːdɪŋ laɪt/", "vi": "nhân vật kiệt xuất; ngọn hải đăng", "pos": "phrase"},
    # 3406: lie about
    {"ipa": "/laɪ əˈbaʊt/", "vi": "nằm dài lười biếng; vứt bừa bãi", "pos": "phrase"},
    # 3407: light speed
    {"ipa": "/laɪt spiːd/", "vi": "vận tốc truyền của ánh sáng chân", "pos": "phrase"},
    # 3408: line of battle
    {"ipa": "/laɪn ʌv ˈbætəl/", "vi": "đội hình chiến đấu của chiến hạm", "pos": "phrase"},
    # 3409: may queen
    {"ipa": "/meɪ kwiːn/", "vi": "nữ hoàng lễ hội hoa tháng Năm cổ", "pos": "phrase"},
    # 3410: military hospital
    {"ipa": "/ˈmɪlətɛri ˈhɑːspɪtl/", "vi": "bệnh viện quân y; quân y viện lớn", "pos": "phrase"},
    # 3411: mine field
    {"ipa": "/maɪn fiːld/", "vi": "bãi rải mìn; tình thế đầy cạm bẫy", "pos": "phrase"},
    # 3412: moment of truth
    {"ipa": "/ˈmoʊmənt ʌv truːθ/", "vi": "thời khắc quyết định then chốt", "pos": "phrase"},
    # 3413: name and address
    {"ipa": "/neɪm ænd əˈdrɛs/", "vi": "họ tên đầy đủ và địa chỉ liên lạc", "pos": "phrase"},
    # 3414: offer price
    {"ipa": "/ˈɔːfər praɪs/", "vi": "giá chào bán; giá niêm yết chào mua", "pos": "phrase"},
    # 3415: old high german
    {"ipa": "/oʊld haɪ ˈdʒɜːrmən/", "vi": "tiếng Đức Thượng cổ trong lịch sử", "pos": "phrase"},
    # 3416: opening line
    {"ipa": "/ˈoʊpənɪŋ laɪn/", "vi": "câu mở màn kịch; dòng văn mở đầu", "pos": "phrase"},
    # 3417: poor boy
    {"ipa": "/pʊr bɔɪ/", "vi": "bánh mì kẹp thịt kiểu New Orleans", "pos": "phrase"},
    # 3418: pop off
    {"ipa": "/pɑːp ɔːf/", "vi": "chết đột ngột; biến đi nhanh chóng", "pos": "phrase"},
    # 3419: position paper
    {"ipa": "/pəˈzɪʃən ˈpeɪpər/", "vi": "bản tuyên bố lập trường chính sách", "pos": "phrase"},
    # 3420: press lord
    {"ipa": "/prɛs lɔːrd/", "vi": "ông trùm truyền thông báo chí lớn", "pos": "phrase"},
    # 3421: queen it over
    {"ipa": "/kwiːn ɪt ˈoʊvər/", "vi": "lên mặt kẻ cả; ra oai hống hách", "pos": "phrase"},
    # 3422: red cross
    {"ipa": "/rɛd krɔːs/", "vi": "Hội Chữ thập đỏ nhân đạo quốc tế", "pos": "phrase"},
    # 3423: red region
    {"ipa": "/rɛd ˈriːdʒən/", "vi": "vùng quang phổ đỏ; hỏa ngục lửa", "pos": "phrase"},
    # 3424: safe period
    {"ipa": "/seɪf ˈpɪriəd/", "vi": "thời kỳ an toàn trong chu kỳ nữ", "pos": "phrase"},
    # 3425: secretary of war
    {"ipa": "/ˈsɛkrətɛri ʌv wɔːr/", "vi": "Bộ trưởng Chiến tranh của Hoa Kỳ", "pos": "phrase"},
    # 3426: service contract
    {"ipa": "/ˈsɜːrvɪs ˈkɑːntrækt/", "vi": "hợp đồng dịch vụ bảo trì định kỳ", "pos": "phrase"},
    # 3427: short sale
    {"ipa": "/ʃɔːrt seɪl/", "vi": "giao dịch bán khống chứng khoán", "pos": "phrase"},
    # 3428: sign industry
    {"ipa": "/saɪn ˈɪndəstri/", "vi": "ngành sản xuất biển bảng quảng cáo", "pos": "phrase"},
    # 3429: small ship
    {"ipa": "/smɔːl ʃɪp/", "vi": "chiếc thuyền buồm nhỏ; ghe xuồng", "pos": "phrase"},
    # 3430: sound property
    {"ipa": "/saʊnd ˈprɑːpərti/", "vi": "đặc tính âm học của làn sóng âm", "pos": "phrase"},
    # 3431: speed of light
    {"ipa": "/spiːd ʌv laɪt/", "vi": "tốc độ ánh sáng trong chân không", "pos": "phrase"},
    # 3432: square one
    {"ipa": "/skwɛr wʌn/", "vi": "vạch xuất phát lại từ con số không", "pos": "phrase"},
    # 3433: square up
    {"ipa": "/skwɛr ʌp/", "vi": "thanh toán sòng phẳng nợ; thủ thế", "pos": "phrase"},
    # 3434: staff member
    {"ipa": "/stæf ˈmɛmbər/", "vi": "thành viên ban tham mưu; nhân viên", "pos": "phrase"},
    # 3435: stand fast
    {"ipa": "/stænd fæst/", "vi": "kiên định giữ vững lập trường ý chí", "pos": "phrase"},
    # 3436: star sign
    {"ipa": "/stɑːr saɪn/", "vi": "cung hoàng đạo theo ngày sinh tháng", "pos": "phrase"},
    # 3437: stock power
    {"ipa": "/stɑːk ˈpaʊər/", "vi": "giấy ủy quyền sang tên cổ phần", "pos": "phrase"},
    # 3438: stopped up
    {"ipa": "/stɑːpt ʌp/", "vi": "bị nghẹt mũi; bị tắc nghẽn ống", "pos": "phrase"},
    # 3439: thomas more
    {"ipa": "/ˈtɑːməs mɔːr/", "vi": "triết gia Thomas More nước Anh", "pos": "phrase"},
    # 3440: throw in
    {"ipa": "/θroʊ ɪn/", "vi": "quả ném biên; tặng kèm miễn phí", "pos": "phrase"},
    # 3441: title role
    {"ipa": "/ˈtaɪtl roʊl/", "vi": "vai diễn mang tên tác phẩm kịch", "pos": "phrase"},
    # 3442: to begin with
    {"ipa": "/tuː bɪˈɡɪn wɪð/", "vi": "trước hết cần nói; ngay từ ban đầu", "pos": "phrase"},
    # 3443: track meet
    {"ipa": "/træk miːt/", "vi": "hội thi đấu điền kinh trên sân bãi", "pos": "phrase"},
    # 3444: trade bill
    {"ipa": "/treɪd bɪl/", "vi": "dự luật thương mại; hối phiếu", "pos": "phrase"},
    # 3445: true statement
    {"ipa": "/truː ˈsteɪtmənt/", "vi": "lời tuyên bố đúng chân thực khách", "pos": "phrase"},
    # 3446: union member
    {"ipa": "/ˈjuːnjən ˈmɛmbər/", "vi": "đoàn viên nghiệp đoàn công đoàn", "pos": "phrase"},
    # 3447: united states code
    {"ipa": "/juːˈnaɪtɪd steɪts koʊd/", "vi": "Bộ luật Liên bang Hoa Kỳ hiện hành", "pos": "phrase"},
    # 3448: war secretary
    {"ipa": "/wɔːr ˈsɛkrətɛri/", "vi": "Bộ trưởng Chiến tranh của Hoa Kỳ", "pos": "phrase"},
    # 3449: white russia
    {"ipa": "/waɪt ˈrʌʃə/", "vi": "quốc gia Belarus; vùng đất Bạch Nga", "pos": "phrase"},
    # 3450: wind up
    {"ipa": "/wɪnd ʌp/", "vi": "kết cục rơi vào; lên dây cót máy", "pos": "phrase"},
    # 3451: without doubt
    {"ipa": "/wɪˈðaʊt daʊt/", "vi": "chắc chắn trăm phần trăm; không ngờ", "pos": "phrase"},
    # 3452: young lady
    {"ipa": "/jʌŋ ˈleɪdi/", "vi": "tiểu thư quý phái; thiếu nữ trẻ", "pos": "phrase"},
    # 3453: openest
    {"ipa": "/ˈoʊpənɪst/", "vi": "thông thoáng nhất; cởi mở nhất", "pos": "adj"},
    # 3454: shat
    {"ipa": "/ʃæt/", "vi": "đã đi vệ sinh nặng; đã đại tiện", "pos": "verb"},
    # 3455: air gun
    {"ipa": "/ɛr ɡʌn/", "vi": "khẩu súng hơi bắn đạn chì giải trí", "pos": "phrase"},
    # 3456: back channel
    {"ipa": "/bæk ˈtʃænəl/", "vi": "kênh liên lạc ngoại giao bí mật", "pos": "phrase"},
    # 3457: bad luck
    {"ipa": "/bæd lʌk/", "vi": "vận rủi xui xẻo; điều không may mắn", "pos": "phrase"},
    # 3458: brown study
    {"ipa": "/braʊn ˈstʌdi/", "vi": "tâm trạng trầm tư mặc tưởng sâu", "pos": "phrase"},
    # 3459: budget for
    {"ipa": "/ˈbʌdʒɪt fɔːr/", "vi": "dự trù kinh phí ngân sách cho việc", "pos": "phrase"},
    # 3460: business address
    {"ipa": "/ˈbɪznəs əˈdrɛs/", "vi": "địa chỉ trụ sở kinh doanh công ty", "pos": "phrase"},
    # 3461: car insurance
    {"ipa": "/kɑːr ɪnˈʃʊrəns/", "vi": "bảo hiểm trách nhiệm dân sự xe ô tô", "pos": "phrase"},
    # 3462: carry away
    {"ipa": "/ˈkæri əˈweɪ/", "vi": "cuốn phăng đi; làm cho phấn khích", "pos": "phrase"},
    # 3463: change of color
    {"ipa": "/tʃeɪndʒ ʌv ˈkʌlər/", "vi": "hiện tượng đổi màu sắc biến màu", "pos": "phrase"},
    # 3464: city planning
    {"ipa": "/ˈsɪti ˈplænɪŋ/", "vi": "quy hoạch kiến thiết đô thị", "pos": "phrase"},
    # 3465: civil law
    {"ipa": "/ˈsɪvəl lɔː/", "vi": "bộ luật dân sự điều chỉnh quan hệ", "pos": "phrase"},
    # 3466: civil order
    {"ipa": "/ˈsɪvəl ˈɔːrdər/", "vi": "trật tự an ninh xã hội dân sự công", "pos": "phrase"},
    # 3467: civil service
    {"ipa": "/ˈsɪvəl ˈsɜːrvɪs/", "vi": "ngành công vụ nhà nước; công chức", "pos": "phrase"},
    # 3468: civil war
    {"ipa": "/ˈsɪvəl wɔːr/", "vi": "cuộc nội chiến huynh đệ tương tàn", "pos": "phrase"},
    # 3469: count out
    {"ipa": "/kaʊnt aʊt/", "vi": "đếm tiền; trọng tài đếm đo ván", "pos": "phrase"},
    # 3470: cross street
    {"ipa": "/krɔːs striːt/", "vi": "con phố cắt ngang giao cắt lộ trình", "pos": "phrase"},
    # 3471: dead sea
    {"ipa": "/dɛd siː/", "vi": "vùng Biển Chết cực mặn Trung Đông", "pos": "phrase"},
    # 3472: direct support
    {"ipa": "/dəˈrɛkt səˈpɔːrt/", "vi": "hỏa lực chi viện yểm trợ trực tiếp", "pos": "phrase"},
    # 3473: economic value
    {"ipa": "/ˌɛkəˈnɑːmɪk ˈvæljuː/", "vi": "giá trị kinh tế hữu ích của tài sản", "pos": "phrase"},
    # 3474: fair deal
    {"ipa": "/fɛr diːl/", "vi": "sự đối xử công bằng; giá hợp lý", "pos": "phrase"},
    # 3475: fall upon
    {"ipa": "/fɔːl əˈpɑːn/", "vi": "bất ngờ tấn công; tình cờ bắt gặp", "pos": "phrase"},
    # 3476: father brown
    {"ipa": "/ˈfɑːðər braʊn/", "vi": "nhân vật thám tử linh mục Cha Brown", "pos": "phrase"},
    # 3477: female child
    {"ipa": "/ˈfiːmeɪl tʃaɪld/", "vi": "bé gái nhỏ tuổi; đứa con gái nhỏ", "pos": "phrase"},
    # 3478: field officer
    {"ipa": "/fiːld ˈɔːfɪsər/", "vi": "sĩ quan cấp tá chỉ huy chiến trường", "pos": "phrase"},
    # 3479: fire sale
    {"ipa": "/ˈfaɪər seɪl/", "vi": "bán tháo hạ giá; xả hàng thanh lý", "pos": "phrase"},
    # 3480: food product
    {"ipa": "/fuːd ˈprɑːdʌkt/", "vi": "sản phẩm chế biến thực phẩm sạch", "pos": "phrase"},
    # 3481: football league
    {"ipa": "/ˈfʊtˌbɔːl liːɡ/", "vi": "giải đấu bóng đá liên đoàn quốc gia", "pos": "phrase"},
    # 3482: football official
    {"ipa": "/ˈfʊtˌbɔːl əˈfɪʃəl/", "vi": "trọng tài điều khiển trận bóng đá", "pos": "phrase"},
    # 3483: foreign policy
    {"ipa": "/ˈfɔːrən ˈpɑːləsi/", "vi": "đường lối chính sách ngoại giao", "pos": "phrase"},
    # 3484: game equipment
    {"ipa": "/ɡeɪm ɪˈkwɪpmənt/", "vi": "dụng cụ trang thiết bị thể thao", "pos": "phrase"},
    # 3485: game theory
    {"ipa": "/ɡeɪm ˈθiːəri/", "vi": "lý thuyết trò chơi trong kinh tế", "pos": "phrase"},
    # 3486: get wind
    {"ipa": "/ɡɛt wɪnd/", "vi": "đánh hơi nghe ngóng biết tin mật", "pos": "phrase"},
    # 3487: girl friday
    {"ipa": "/ɡɜːrl ˈfraɪdeɪ/", "vi": "nữ trợ lý đắc lực tháo vát đa năng", "pos": "phrase"},
    # 3488: go for broke
    {"ipa": "/ɡoʊ fɔːr broʊk/", "vi": "được ăn cả ngã về không; liều hết", "pos": "phrase"},
    # 3489: ground attack
    {"ipa": "/ɡraʊnd əˈtæk/", "vi": "đòn oanh tạc mục tiêu mặt đất", "pos": "phrase"},
    # 3490: gun room
    {"ipa": "/ɡʌn ruːm/", "vi": "kho chứa vũ khí trên chiến hạm", "pos": "phrase"},
    # 3491: half sister
    {"ipa": "/hæf ˈsɪstər/", "vi": "chị em gái cùng cha khác mẹ ruột", "pos": "phrase"},
    # 3492: hard cash
    {"ipa": "/hɑːrd kæʃ/", "vi": "tiền mặt trao tay ngay lập tức", "pos": "phrase"},
    # 3493: health insurance
    {"ipa": "/hɛlθ ɪnˈʃʊrəns/", "vi": "chính sách bảo hiểm y tế sức khỏe", "pos": "phrase"},
    # 3494: high mass
    {"ipa": "/haɪ mæs/", "vi": "thánh lễ trọng thể có ca đoàn xướng", "pos": "phrase"},
    # 3495: high status
    {"ipa": "/haɪ ˈsteɪtəs/", "vi": "địa vị xã hội cao quý; thế đứng cao", "pos": "phrase"},
    # 3496: holy place
    {"ipa": "/ˈhoʊli pleɪs/", "vi": "nơi thánh địa tôn nghiêm thờ cúng", "pos": "phrase"},
    # 3497: hotel room
    {"ipa": "/hoʊˈtɛl ruːm/", "vi": "phòng nghỉ khách sạn tiện nghi", "pos": "phrase"},
    # 3498: in fashion
    {"ipa": "/ɪn ˈfæʃən/", "vi": "hợp thời trang sành điệu; đang mốt", "pos": "phrase"},
    # 3499: into the wind
    {"ipa": "/ˈɪntuː ðə wɪnd/", "vi": "bay ngược chiều gió thổi rát mặt", "pos": "phrase"},
]

with open('scratch/b21_r07_raw_p5.json') as f:
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

with open('scratch/b21_r07_p5.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("b21_r07_p5.json created successfully and validated!")
