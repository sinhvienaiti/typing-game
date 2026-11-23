import json

# Manual word-by-word cognitive review for Batch 21 Round 8 Part 3 (records 3700-3799, IDs 200k.003702 to 200k.003801)
reviewed_entries = [
    # 3700: draw up
    {"ipa": "/drɔː ʌp/", "vi": "soạn thảo văn bản; dừng xe lại", "pos": "phrase"},
    # 3701: drug company
    {"ipa": "/drʌɡ ˈkʌmpəni/", "vi": "công ty dược phẩm; hãng dược", "pos": "phrase"},
    # 3702: east india
    {"ipa": "/iːst ˈɪndiə/", "vi": "vùng Đông Ấn; xứ Đông Ấn", "pos": "phrase"},
    # 3703: fair chance
    {"ipa": "/fɛr tʃæns/", "vi": "cơ hội khả quan; triển vọng tốt", "pos": "phrase"},
    # 3704: favorite son
    {"ipa": "/ˈfeɪvərɪt sʌn/", "vi": "con cưng quê hương; ứng viên cưng", "pos": "phrase"},
    # 3705: first estate
    {"ipa": "/fɜːrst ɪˈsteɪt/", "vi": "đẳng cấp tăng lữ; giới giáo sĩ", "pos": "phrase"},
    # 3706: free agency
    {"ipa": "/friː ˈeɪdʒənsi/", "vi": "tình trạng cầu thủ tự do; tự chủ", "pos": "phrase"},
    # 3707: george guess
    {"ipa": "/dʒɔːrdʒ ɡɛs/", "vi": "George Guess; học giả Sequoyah", "pos": "phrase"},
    # 3708: girl wonder
    {"ipa": "/ɡɜːrl ˈwʌndər/", "vi": "cô bé thần đồng; thần đồng nữ", "pos": "phrase"},
    # 3709: gold mine
    {"ipa": "/ɡoʊld maɪn/", "vi": "mỏ vàng; nguồn lợi khổng lồ", "pos": "phrase"},
    # 3710: good faith
    {"ipa": "/ɡʊd feɪθ/", "vi": "thiện chí; sự thành tín trung thực", "pos": "phrase"},
    # 3711: green paper
    {"ipa": "/ɡriːn ˈpeɪpər/", "vi": "sách xanh tham vấn chính sách", "pos": "phrase"},
    # 3712: group theory
    {"ipa": "/ɡruːp ˈθiːəri/", "vi": "lý thuyết nhóm trong toán học", "pos": "phrase"},
    # 3713: growth industry
    {"ipa": "/ɡroʊθ ˈɪndəstri/", "vi": "ngành công nghiệp tăng trưởng cao", "pos": "phrase"},
    # 3714: hand wear
    {"ipa": "/hænd wɛr/", "vi": "găng tay; đồ che bảo vệ tay", "pos": "phrase"},
    # 3715: head trip
    {"ipa": "/hɛd trɪp/", "vi": "trải nghiệm tâm trí kích thích", "pos": "phrase"},
    # 3716: holy person
    {"ipa": "/ˈhoʊli ˈpɜːrsn/", "vi": "bậc thánh nhân; người thánh thiện", "pos": "phrase"},
    # 3717: holy week
    {"ipa": "/ˈhoʊli wiːk/", "vi": "Tuần Thánh trong Công giáo", "pos": "phrase"},
    # 3718: ice field
    {"ipa": "/aɪs fiːld/", "vi": "cánh đồng băng; cánh đồng tuyết", "pos": "phrase"},
    # 3719: inside track
    {"ipa": "/ˌɪnˈsaɪd træk/", "vi": "vị thế thuận lợi; đường đua trong", "pos": "phrase"},
    # 3720: lie down
    {"ipa": "/laɪ daʊn/", "vi": "nằm xuống; ngả lưng nghỉ ngơi", "pos": "phrase"},
    # 3721: light unit
    {"ipa": "/laɪt ˈjuːnɪt/", "vi": "đơn vị đo quang thông ánh sáng", "pos": "phrase"},
    # 3722: long distance
    {"ipa": "/lɔːŋ ˈdɪstəns/", "vi": "đường dài; khoảng cách xa xôi", "pos": "phrase"},
    # 3723: low german
    {"ipa": "/loʊ ˈdʒɜːrmən/", "vi": "tiếng Hạ Đức; phương ngữ Đức", "pos": "phrase"},
    # 3724: male person
    {"ipa": "/meɪl ˈpɜːrsn/", "vi": "nam giới; người đàn ông; phái nam", "pos": "phrase"},
    # 3725: married couple
    {"ipa": "/ˈmærɪd ˈkʌpl/", "vi": "cặp vợ chồng; đôi vợ chồng mới", "pos": "phrase"},
    # 3726: mass number
    {"ipa": "/mæs ˈnʌmbər/", "vi": "số khối nguyên tử trong hóa học", "pos": "phrase"},
    # 3727: mobile home
    {"ipa": "/ˈmoʊbl hoʊm/", "vi": "nhà di động dạng xe moóc", "pos": "phrase"},
    # 3728: mouth off
    {"ipa": "/maʊθ ɔːf/", "vi": "nói năng xấc xược; bép xép to tiếng", "pos": "phrase"},
    # 3729: natural language
    {"ipa": "/ˈnætʃrəl ˈlæŋɡwɪdʒ/", "vi": "ngôn ngữ tự nhiên của loài người", "pos": "phrase"},
    # 3730: nature study
    {"ipa": "/ˈneɪtʃər ˈstʌdi/", "vi": "học về thiên nhiên; tự nhiên học", "pos": "phrase"},
    # 3731: opening move
    {"ipa": "/ˈoʊpnɪŋ muːv/", "vi": "nước cờ mở màn; bước đi ban đầu", "pos": "phrase"},
    # 3732: paper round
    {"ipa": "/ˈpeɪpər raʊnd/", "vi": "tuyến phát báo dạo; việc giao báo", "pos": "phrase"},
    # 3733: part of speech
    {"ipa": "/pɑːrt ʌv spiːtʃ/", "vi": "từ loại; phân loại ngữ pháp của từ", "pos": "phrase"},
    # 3734: pay cash
    {"ipa": "/peɪ kæʃ/", "vi": "thanh toán bằng tiền mặt ngay", "pos": "phrase"},
    # 3735: person agreement
    {"ipa": "/ˈpɜːrsn əˈɡriːmənt/", "vi": "sự hòa hợp về ngôi trong ngữ pháp", "pos": "phrase"},
    # 3736: picture writing
    {"ipa": "/ˈpɪktʃər ˈraɪtɪŋ/", "vi": "chữ viết tượng hình; lối viết hình", "pos": "phrase"},
    # 3737: political movement
    {"ipa": "/pəˈlɪtɪkl ˈmuːvmənt/", "vi": "phong trào vận động chính trị", "pos": "phrase"},
    # 3738: position effect
    {"ipa": "/pəˈzɪʃən ɪˈfɛkt/", "vi": "hiệu ứng vị trí gen di truyền", "pos": "phrase"},
    # 3739: power plant
    {"ipa": "/ˈpaʊər plænt/", "vi": "nhà máy phát điện; trạm phát điện", "pos": "phrase"},
    # 3740: press box
    {"ipa": "/prɛs bɑːks/", "vi": "khu vực ghế dành cho phóng viên", "pos": "phrase"},
    # 3741: primary care
    {"ipa": "/ˈpraɪmɛri kɛr/", "vi": "chăm sóc y tế ban đầu cơ sở", "pos": "phrase"},
    # 3742: prime time
    {"ipa": "/praɪm taɪm/", "vi": "giờ vàng phát sóng truyền hình", "pos": "phrase"},
    # 3743: private eye
    {"ipa": "/ˈpraɪvət aɪ/", "vi": "thám tử tư; điều tra viên độc lập", "pos": "phrase"},
    # 3744: pull over
    {"ipa": "/pʊl ˈoʊvər/", "vi": "tấp xe vào lề; lệnh cho tấp lề", "pos": "phrase"},
    # 3745: quick march
    {"ipa": "/kwɪk mɑːrtʃ/", "vi": "hành quân nhanh; bước đi nhanh đều", "pos": "phrase"},
    # 3746: quick study
    {"ipa": "/kwɪk ˈstʌdi/", "vi": "người sáng dạ; tiếp thu rất nhanh", "pos": "phrase"},
    # 3747: record album
    {"ipa": "/ˈrɛkərd ˈælbəm/", "vi": "album đĩa nhạc; album ghi âm", "pos": "phrase"},
    # 3748: review article
    {"ipa": "/rɪˈvjuː ˈɑːrtɪkl/", "vi": "bài báo tổng quan; bài điểm sách", "pos": "phrase"},
    # 3749: right smart
    {"ipa": "/raɪt smɑːrt/", "vi": "khá nhiều; rất nhiều; đáng kể", "pos": "phrase"},
    # 3750: ring out
    {"ipa": "/rɪŋ aʊt/", "vi": "vang dội ngân vang; tiễn đưa năm", "pos": "phrase"},
    # 3751: ring up
    {"ipa": "/rɪŋ ʌp/", "vi": "gọi điện thoại; ghi hóa đơn tính", "pos": "phrase"},
    # 3752: rise up
    {"ipa": "/raɪz ʌp/", "vi": "vùng lên khởi nghĩa; nổi dậy chống", "pos": "phrase"},
    # 3753: rock star
    {"ipa": "/rɑːk stɑːr/", "vi": "ngôi sao nhạc rock; danh ca rốc", "pos": "phrase"},
    # 3754: senior high school
    {"ipa": "/ˈsiːnjər haɪ skuːl/", "vi": "trường trung học phổ thông; cấp ba", "pos": "phrase"},
    # 3755: separate off
    {"ipa": "/ˈsɛpəreɪt ɔːf/", "vi": "ngăn cách biệt lập; chia tách ra", "pos": "phrase"},
    # 3756: set theory
    {"ipa": "/sɛt ˈθiːəri/", "vi": "lý thuyết tập hợp trong toán học", "pos": "phrase"},
    # 3757: short letter
    {"ipa": "/ʃɔːrt ˈlɛtər/", "vi": "bức thư ngắn; lá thư ngắn gửi đi", "pos": "phrase"},
    # 3758: sick person
    {"ipa": "/sɪk ˈpɜːrsn/", "vi": "người bệnh; bệnh nhân ốm đau", "pos": "phrase"},
    # 3759: social organization
    {"ipa": "/ˈsoʊʃl ˌɔːrɡənəˈzeɪʃən/", "vi": "tổ chức xã hội; cơ cấu xã hội", "pos": "phrase"},
    # 3760: south africa
    {"ipa": "/saʊθ ˈæfrɪkə/", "vi": "nước Cộng hòa Nam Phi; xứ Nam Phi", "pos": "phrase"},
    # 3761: space travel
    {"ipa": "/speɪs ˈtrævl/", "vi": "du hành không gian; du lịch vũ trụ", "pos": "phrase"},
    # 3762: spread out
    {"ipa": "/sprɛd aʊt/", "vi": "lan rộng; tỏa rộng ra các hướng", "pos": "phrase"},
    # 3763: spring to mind
    {"ipa": "/sprɪŋ tuː maɪnd/", "vi": "lóe lên trong tâm trí; chợt nhớ ra", "pos": "phrase"},
    # 3764: stock room
    {"ipa": "/stɑːk ruːm/", "vi": "phòng chứa đồ; kho chứa hàng hóa", "pos": "phrase"},
    # 3765: student center
    {"ipa": "/ˈstuːdnt ˈsɛntər/", "vi": "trung tâm hỗ trợ sinh viên", "pos": "phrase"},
    # 3766: take the count
    {"ipa": "/teɪk ðə kaʊnt/", "vi": "bị đếm nốc ao; chịu thua cuộc", "pos": "phrase"},
    # 3767: throw back
    {"ipa": "/θroʊ bæk/", "vi": "ném trả lại; gợi nhớ quá khứ", "pos": "phrase"},
    # 3768: throw off
    {"ipa": "/θroʊ ɔːf/", "vi": "ném bỏ đi; thoát khỏi; dứt bỏ", "pos": "phrase"},
    # 3769: track record
    {"ipa": "/træk ˈrɛkərd/", "vi": "thành tích quá khứ; hồ sơ năng lực", "pos": "phrase"},
    # 3770: track star
    {"ipa": "/træk stɑːr/", "vi": "ngôi sao điền kinh xuất sắc", "pos": "phrase"},
    # 3771: trade union
    {"ipa": "/treɪd ˈjuːnjən/", "vi": "công đoàn lao động; nghiệp đoàn", "pos": "phrase"},
    # 3772: trip line
    {"ipa": "/trɪp laɪn/", "vi": "dây giật mỏ neo; dây chằng tháo mở", "pos": "phrase"},
    # 3773: water plant
    {"ipa": "/ˈwɔːtər plænt/", "vi": "cây thủy sinh; nhà máy cấp nước", "pos": "phrase"},
    # 3774: wedding day
    {"ipa": "/ˈwɛdɪŋ deɪ/", "vi": "ngày thành hôn; ngày cưới trọng đại", "pos": "phrase"},
    # 3775: work surface
    {"ipa": "/wɜːrk ˈsɜːrfɪs/", "vi": "bề mặt làm việc; mặt bàn thao tác", "pos": "phrase"},
    # 3776: kinder
    {"ipa": "/ˈkaɪndər/", "vi": "tử tế hơn; tốt bụng hơn; hiền hơn", "pos": "adj"},
    # 3777: kindest
    {"ipa": "/ˈkaɪndɪst/", "vi": "tốt bụng nhất; nhân từ nhất", "pos": "adj"},
    # 3778: presidents
    {"ipa": "/ˈprɛzɪdənts/", "vi": "các tổng thống; các vị chủ tịch", "pos": "noun"},
    # 3779: air spring
    {"ipa": "/ɛr sprɪŋ/", "vi": "lò xo không khí nén; giảm xóc khí", "pos": "phrase"},
    # 3780: art collection
    {"ipa": "/ɑːrt kəˈlɛkʃən/", "vi": "bộ sưu tập tác phẩm nghệ thuật", "pos": "phrase"},
    # 3781: attack dog
    {"ipa": "/əˈtæk dɔːɡ/", "vi": "chó săn tấn công; chó canh gác cắn", "pos": "phrase"},
    # 3782: bad block
    {"ipa": "/bæd blɑːk/", "vi": "khối bộ nhớ hỏng trên đĩa từ", "pos": "phrase"},
    # 3783: base rate
    {"ipa": "/beɪs reɪt/", "vi": "lãi suất cơ sở; mức phí cơ bản", "pos": "phrase"},
    # 3784: bet on
    {"ipa": "/bɛt ɑːn/", "vi": "đặt cược vào; tin chắc vào việc", "pos": "phrase"},
    # 3785: big tree
    {"ipa": "/bɪɡ triː/", "vi": "cây cự mộc; cây tùng bách khổng lồ", "pos": "phrase"},
    # 3786: black disease
    {"ipa": "/blæk dɪˈziːz/", "vi": "bệnh hoại tử gan đen ở cừu", "pos": "phrase"},
    # 3787: black spot
    {"ipa": "/blæk spɑːt/", "vi": "điểm đen tai nạn; bệnh đốm lá đen", "pos": "phrase"},
    # 3788: british capital
    {"ipa": "/ˈbrɪtɪʃ ˈkæpɪtl/", "vi": "thủ đô Luân Đôn của nước Anh", "pos": "phrase"},
    # 3789: building material
    {"ipa": "/ˈbɪldɪŋ məˈtɪriəl/", "vi": "vật liệu xây dựng công trình", "pos": "phrase"},
    # 3790: business executive
    {"ipa": "/ˈbɪznəs ɪɡˈzɛkjətɪv/", "vi": "giám đốc điều hành doanh nghiệp", "pos": "phrase"},
    # 3791: calling into question
    {"ipa": "/ˈkɔːlɪŋ ˈɪntuː ˈkwɛstʃən/", "vi": "sự hoài nghi chất vấn; nghi vấn", "pos": "phrase"},
    # 3792: camera care
    {"ipa": "/ˈkæmrə kɛr/", "vi": "bảo dưỡng máy ảnh; gìn giữ máy ảnh", "pos": "phrase"},
    # 3793: cast on
    {"ipa": "/kæst ɑːn/", "vi": "gầy mũi đan len; bắt đầu mũi đan", "pos": "phrase"},
    # 3794: chief of staff
    {"ipa": "/tʃiːf ʌv stæf/", "vi": "tham mưu trưởng; chánh văn phòng", "pos": "phrase"},
    # 3795: church officer
    {"ipa": "/tʃɜːrtʃ ˈɔːfɪsər/", "vi": "chức sắc nhà thờ; quản trị giáo xứ", "pos": "phrase"},
    # 3796: claim form
    {"ipa": "/kleɪm fɔːrm/", "vi": "đơn yêu cầu bồi thường bảo hiểm", "pos": "phrase"},
    # 3797: click off
    {"ipa": "/klɪk ɔːf/", "vi": "tắt công tắc; hoàn thành mau lẹ", "pos": "phrase"},
    # 3798: closed book
    {"ipa": "/kloʊzd bʊk/", "vi": "điều bí ẩn; chuyện hoàn toàn kín", "pos": "phrase"},
    # 3799: committee member
    {"ipa": "/kəˈmɪti ˈmɛmbər/", "vi": "ủy viên ủy ban; thành viên ban", "pos": "phrase"}
]

with open("scratch/b21_r08_raw_p3.json", "r", encoding="utf-8") as f:
    raw_data = json.load(f)

assert len(raw_data) == 100
assert len(reviewed_entries) == 100

output = []
for i, item in enumerate(raw_data):
    rev = reviewed_entries[i]
    assert len(rev["vi"]) <= 35, f"Too long: {item['hw']} -> {rev['vi']} ({len(rev['vi'])} chars)"
    assert rev["ipa"].startswith("/") and rev["ipa"].endswith("/"), f"Bad IPA: {item['hw']} -> {rev['ipa']}"
    assert rev["ipa"].count("/") == 2, f"Bad slash count: {item['hw']} -> {rev['ipa']}"
    assert rev["pos"] in ["noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "det", "num", "phrase"]

    entry = {
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
    output.append(entry)

with open("scratch/b21_r08_p3.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Successfully processed {len(output)} entries for Part 3.")
