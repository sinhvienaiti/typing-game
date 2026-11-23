import json

# Manual word-by-word cognitive review for Batch 21 Round 10 Part 2 (records 4600-4699, IDs 200k.004602 to 200k.004701)
reviewed_entries = [
    # 4600: brain science
    {"ipa": "/breɪn ˈsaɪəns/", "vi": "khoa học não bộ; thần kinh học", "pos": "phrase"},
    # 4601: brain trust
    {"ipa": "/breɪn trʌst/", "vi": "nhóm cố vấn tinh hoa; ban tham mưu", "pos": "phrase"},
    # 4602: building complex
    {"ipa": "/ˈbɪldɪŋ ˈkɑːmplɛks/", "vi": "khu phức hợp tòa nhà đa năng", "pos": "phrase"},
    # 4603: business firm
    {"ipa": "/ˈbɪznəs fɜːrm/", "vi": "công ty kinh doanh; hãng thương mại", "pos": "phrase"},
    # 4604: call option
    {"ipa": "/kɔːl ˈɑːpʃən/", "vi": "quyền chọn mua trong tài chính", "pos": "phrase"},
    # 4605: centre of attention
    {"ipa": "/ˈsɛntər ʌv əˈtɛnʃən/", "vi": "tâm điểm của sự chú ý dõi theo", "pos": "phrase"},
    # 4606: centre stage
    {"ipa": "/ˈsɛntər steɪdʒ/", "vi": "trung tâm sân khấu; vị trí nổi bật", "pos": "phrase"},
    # 4607: chief secretary
    {"ipa": "/tʃiːf ˈsɛkrətɛri/", "vi": "tổng thư ký; bí thư trưởng cơ quan", "pos": "phrase"},
    # 4608: chinese wall
    {"ipa": "/ˌtʃaɪˈniːz wɔːl/", "vi": "bức tường ngăn cách thông tin vốn", "pos": "phrase"},
    # 4609: christmas present
    {"ipa": "/ˈkrɪsməs ˈprɛznt/", "vi": "món quà Giáng sinh tặng người thân", "pos": "phrase"},
    # 4610: coach dog
    {"ipa": "/koʊtʃ dɔːɡ/", "vi": "chó đốm Đan Mạch Dalmatian", "pos": "phrase"},
    # 4611: come alive
    {"ipa": "/kʌm əˈlaɪv/", "vi": "trở nên sống động; bừng tỉnh lại", "pos": "phrase"},
    # 4612: commercial bank
    {"ipa": "/kəˈmɜːrʃl bæŋk/", "vi": "ngân hàng thương mại huy động vốn", "pos": "phrase"},
    # 4613: computer code
    {"ipa": "/kəmˈpjuːtər koʊd/", "vi": "mã lệnh chương trình máy tính", "pos": "phrase"},
    # 4614: computer paper
    {"ipa": "/kəmˈpjuːtər ˈpeɪpər/", "vi": "giấy in máy tính liên tục đục lỗ", "pos": "phrase"},
    # 4615: construction paper
    {"ipa": "/kənˈstrʌkʃən ˈpeɪpər/", "vi": "giấy bìa màu thủ công cho học sinh", "pos": "phrase"},
    # 4616: core out
    {"ipa": "/kɔːr aʊt/", "vi": "khoét rỗng ruột quả; nạo bỏ lõi", "pos": "phrase"},
    # 4617: credit card
    {"ipa": "/ˈkrɛdɪt kɑːrd/", "vi": "thẻ tín dụng thanh toán quốc tế", "pos": "phrase"},
    # 4618: dance step
    {"ipa": "/dæns stɛp/", "vi": "bước nhảy vũ đạo khi khiêu vũ", "pos": "phrase"},
    # 4619: data structure
    {"ipa": "/ˈdeɪtə ˈstrʌktʃər/", "vi": "cấu trúc dữ liệu trong lập trình", "pos": "phrase"},
    # 4620: death benefit
    {"ipa": "/dɛθ ˈbɛnɪfɪt/", "vi": "tiền trợ cấp tử tuất bảo hiểm", "pos": "phrase"},
    # 4621: death seat
    {"ipa": "/dɛθ siːt/", "vi": "ghế tử thần bên cạnh tài xế lái xe", "pos": "phrase"},
    # 4622: dinner set
    {"ipa": "/ˈdɪnər sɛt/", "vi": "bộ đồ ăn tối gồm chén đĩa bàn ăn", "pos": "phrase"},
    # 4623: double standard
    {"ipa": "/ˈdʌbl ˈstændərd/", "vi": "tiêu chuẩn kép; thói bất công kép", "pos": "phrase"},
    # 4624: draw together
    {"ipa": "/drɔː təˈɡɛðər/", "vi": "gắn kết lại gần nhau; xích lại gần", "pos": "phrase"},
    # 4625: east africa
    {"ipa": "/iːst ˈæfrɪkə/", "vi": "vùng lãnh thổ Đông Phi; xứ Đông Phi", "pos": "phrase"},
    # 4626: east indian
    {"ipa": "/iːst ˈɪndiən/", "vi": "người dân vùng Đông Ấn đảo Caribe", "pos": "phrase"},
    # 4627: english professor
    {"ipa": "/ˈɪŋɡlɪʃ prəˈfɛsər/", "vi": "giáo sư dạy tiếng Anh và văn học", "pos": "phrase"},
    # 4628: executive program
    {"ipa": "/ɪɡˈzɛkjətɪv ˈproʊɡræm/", "vi": "chương trình điều hành giám đốc", "pos": "phrase"},
    # 4629: field of operations
    {"ipa": "/fiːld ʌv ˌɑːpəˈreɪʃənz/", "vi": "chiến trường tác chiến; mặt trận", "pos": "phrase"},
    # 4630: field theory
    {"ipa": "/fiːld ˈθiːəri/", "vi": "lý thuyết trường trong vật lý học", "pos": "phrase"},
    # 4631: field trial
    {"ipa": "/fiːld ˈtraɪəl/", "vi": "thử nghiệm thực địa ngoài thực tế", "pos": "phrase"},
    # 4632: financial management service
    {"ipa": "/faɪˈnænʃl ˈmænɪdʒmənt ˈsɜːrvɪs/", "vi": "Cục Quản lý Tài chính Hoa Kỳ", "pos": "phrase"},
    # 4633: financial statement
    {"ipa": "/faɪˈnænʃl ˈsteɪtmənt/", "vi": "bản báo cáo tài chính định kỳ năm", "pos": "phrase"},
    # 4634: fire screen
    {"ipa": "/ˈfaɪər skriːn/", "vi": "tấm lưới chắn tàn lửa lò sưởi", "pos": "phrase"},
    # 4635: fire tree
    {"ipa": "/ˈfaɪər triː/", "vi": "cây phượng vĩ đỏ; cây hoa lửa", "pos": "phrase"},
    # 4636: general agent
    {"ipa": "/ˈdʒɛnrəl ˈeɪdʒənt/", "vi": "tổng đại lý phân phối toàn quyền", "pos": "phrase"},
    # 4637: german language
    {"ipa": "/ˈdʒɜːrmən ˈlæŋɡwɪdʒ/", "vi": "tiếng Đức ngôn ngữ thuộc German", "pos": "phrase"},
    # 4638: give birth
    {"ipa": "/ɡɪv bɜːrθ/", "vi": "sinh con đẻ cái; khai sinh ra", "pos": "phrase"},
    # 4639: gun dog
    {"ipa": "/ɡʌn dɔːɡ/", "vi": "chó săn tha mồi cho thợ săn bắn", "pos": "phrase"},
    # 4640: high horse
    {"ipa": "/haɪ hɔːrs/", "vi": "thái độ kiêu căng; vẻ ngạo mạn", "pos": "phrase"},
    # 4641: holy land
    {"ipa": "/ˈhoʊli lænd/", "vi": "Đất Thánh thiêng liêng ở Palestine", "pos": "phrase"},
    # 4642: horse around
    {"ipa": "/hɔːrs əˈraʊnd/", "vi": "nô đùa ầm ĩ; giỡn cợt quậy phá", "pos": "phrase"},
    # 4643: hot spring
    {"ipa": "/hɑːt sprɪŋ/", "vi": "suối nước nóng tự nhiên khoáng chất", "pos": "phrase"},
    # 4644: international development association
    {"ipa": "/ˌɪntərˈnæʃnəl dɪˈvɛləpmənt əˌsoʊsiˈeɪʃən/", "vi": "Hiệp hội Phát triển Quốc tế IDA", "pos": "phrase"},
    # 4645: international scale
    {"ipa": "/ˌɪntərˈnæʃnəl skeɪl/", "vi": "thang đo quy chuẩn quốc tế", "pos": "phrase"},
    # 4646: kick in
    {"ipa": "/kɪk ɪn/", "vi": "bắt đầu phát huy tác dụng thuốc", "pos": "phrase"},
    # 4647: killing field
    {"ipa": "/ˈkɪlɪŋ fiːld/", "vi": "cánh đồng chết thảm sát diệt chủng", "pos": "phrase"},
    # 4648: la tour
    {"ipa": "/lɑː ˈtʊr/", "vi": "họa sĩ Georges de La Tour Pháp", "pos": "phrase"},
    # 4649: language unit
    {"ipa": "/ˈlæŋɡwɪdʒ ˈjuːnɪt/", "vi": "đơn vị ngôn ngữ cấu trúc ngữ pháp", "pos": "phrase"},
    # 4650: law agent
    {"ipa": "/lɔː ˈeɪdʒənt/", "vi": "luật sư đại diện; viên chức tòa án", "pos": "phrase"},
    # 4651: lead plant
    {"ipa": "/lɛd plænt/", "vi": "cây bụi chỉ thị quặng chì mọc", "pos": "phrase"},
    # 4652: library program
    {"ipa": "/ˈlaɪbrɛri ˈproʊɡræm/", "vi": "chương trình hoạt động của thư viện", "pos": "phrase"},
    # 4653: lie in wait
    {"ipa": "/laɪ ɪn weɪt/", "vi": "mai phục đón lõng; rình rập chờ đợi", "pos": "phrase"},
    # 4654: lie low
    {"ipa": "/laɪ loʊ/", "vi": "ẩn mình nằm gai nếm mật; lánh mặt", "pos": "phrase"},
    # 4655: local authority
    {"ipa": "/ˈloʊkl əˈθɔːrəti/", "vi": "chính quyền địa phương cấp sở tại", "pos": "phrase"},
    # 4656: long horse
    {"ipa": "/lɔːŋ hɔːrs/", "vi": "ngựa gỗ nhảy dài môn thể dục", "pos": "phrase"},
    # 4657: love apple
    {"ipa": "/lʌv ˈæpl/", "vi": "quả cà chua đỏ; trái tình yêu xưa", "pos": "phrase"},
    # 4658: mass action
    {"ipa": "/mæs ˈækʃən/", "vi": "tác dụng khối lượng trong hóa học", "pos": "phrase"},
    # 4659: may wine
    {"ipa": "/meɪ waɪn/", "vi": "rượu vang thảo mộc tháng năm Đức", "pos": "phrase"},
    # 4660: military machine
    {"ipa": "/ˈmɪlətɛri məˈʃiːn/", "vi": "cỗ máy quân sự; lực lượng quân đội", "pos": "phrase"},
    # 4661: missing link
    {"ipa": "/ˈmɪsɪŋ lɪŋk/", "vi": "mắt xích tiến hóa còn thiếu", "pos": "phrase"},
    # 4662: mobile phone
    {"ipa": "/ˈmoʊbl foʊn/", "vi": "điện thoại di động; máy cầm tay", "pos": "phrase"},
    # 4663: mother cell
    {"ipa": "/ˈmʌðər sɛl/", "vi": "tế bào mẹ phân chia trong sinh học", "pos": "phrase"},
    # 4664: mountain time
    {"ipa": "/ˈmaʊntn taɪm/", "vi": "múi giờ miền Núi Bắc Mỹ MST", "pos": "phrase"},
    # 4665: north wind
    {"ipa": "/nɔːrθ wɪnd/", "vi": "ngọn gió bấc; gió mùa phương bắc", "pos": "phrase"},
    # 4666: not to mention
    {"ipa": "/nɑːt tuː ˈmɛnʃən/", "vi": "chưa kể đến; ấy là còn chưa nói", "pos": "phrase"},
    # 4667: on your guard
    {"ipa": "/ɑːn jɔːr ɡɑːrd/", "vi": "hãy cảnh giác; cẩn thận đề phòng", "pos": "phrase"},
    # 4668: paris university
    {"ipa": "/ˈpærɪs ˌjuːnɪˈvɜːrsəti/", "vi": "Viện Đại học Paris Sorbonne Pháp", "pos": "phrase"},
    # 4669: peace officer
    {"ipa": "/piːs ˈɔːfɪsər/", "vi": "viên chức giữ gìn an ninh trật tự", "pos": "phrase"},
    # 4670: personal effects
    {"ipa": "/ˈpɜːrsənl ɪˈfɛkts/", "vi": "tư trang vật dụng cá nhân mang theo", "pos": "phrase"},
    # 4671: physical property
    {"ipa": "/ˈfɪzɪkl ˈprɑːpərti/", "vi": "tính chất vật lý của vật chất", "pos": "phrase"},
    # 4672: physical science
    {"ipa": "/ˈfɪzɪkl ˈsaɪəns/", "vi": "khoa học vật lý tự nhiên tự nhiên", "pos": "phrase"},
    # 4673: piece of ass
    {"ipa": "/piːs ʌv æs/", "vi": "bạn tình gợi cảm; người khêu gợi", "pos": "phrase"},
    # 4674: place of birth
    {"ipa": "/pleɪs ʌv bɜːrθ/", "vi": "nơi sinh; quê quán nơi chôn rau", "pos": "phrase"},
    # 4675: place setting
    {"ipa": "/pleɪs ˈsɛtɪŋ/", "vi": "bộ đồ ăn sắp đặt sẵn trên bàn tiệc", "pos": "phrase"},
    # 4676: population growth
    {"ipa": "/ˌpɑːpjuˈleɪʃən ɡroʊθ/", "vi": "tốc độ gia tăng dân số quốc gia", "pos": "phrase"},
    # 4677: program library
    {"ipa": "/ˈproʊɡræm ˈlaɪbrɛri/", "vi": "thư viện chương trình phần mềm", "pos": "phrase"},
    # 4678: reaction time
    {"ipa": "/riˈækʃən taɪm/", "vi": "thời gian phản xạ phản ứng nhanh", "pos": "phrase"},
    # 4679: rock island
    {"ipa": "/rɑːk ˈaɪlənd/", "vi": "thành phố Rock Island bang Illinois", "pos": "phrase"},
    # 4680: roll down
    {"ipa": "/roʊl daʊn/", "vi": "lăn xuống dốc; hạ kính xe hơi", "pos": "phrase"},
    # 4681: roll off
    {"ipa": "/roʊl ɔːf/", "vi": "xuất xưởng hàng loạt; đọc vanh vách", "pos": "phrase"},
    # 4682: round dance
    {"ipa": "/raʊnd dæns/", "vi": "điệu múa vòng tròn tập thể dân gian", "pos": "phrase"},
    # 4683: russian river
    {"ipa": "/ˈrʌʃn ˈrɪvər/", "vi": "sông Russian tại bang California Mỹ", "pos": "phrase"},
    # 4684: say hey kid
    {"ipa": "/seɪ heɪ kɪd/", "vi": "huyền thoại bóng chày Willie Mays", "pos": "phrase"},
    # 4685: search language
    {"ipa": "/sɜːrtʃ ˈlæŋɡwɪdʒ/", "vi": "ngôn ngữ truy vấn tìm kiếm dữ liệu", "pos": "phrase"},
    # 4686: set apart
    {"ipa": "/sɛt əˈpɑːrt/", "vi": "để dành riêng; làm cho nổi bật hơn", "pos": "phrase"},
    # 4687: sex crime
    {"ipa": "/sɛks kraɪm/", "vi": "tội phạm xâm hại tình dục dâm ô", "pos": "phrase"},
    # 4688: shoot up
    {"ipa": "/ʃuːt ʌp/", "vi": "tăng vọt phi mã; tiêm chích ma túy", "pos": "phrase"},
    # 4689: shut away
    {"ipa": "/ʃʌt əˈweɪ/", "vi": "nhốt giam cách ly; cất kỹ đồ đạc", "pos": "phrase"},
    # 4690: significant figure
    {"ipa": "/sɪɡˈnɪfɪkənt ˈfɪɡjər/", "vi": "chữ số có nghĩa trong tính toán", "pos": "phrase"},
    # 4691: south african
    {"ipa": "/saʊθ ˈæfrɪkən/", "vi": "thuộc về Nam Phi; người dân Nam Phi", "pos": "phrase"},
    # 4692: spanish people
    {"ipa": "/ˈspænɪʃ ˈpiːpl/", "vi": "người dân tộc Tây Ban Nha xứ bò tót", "pos": "phrase"},
    # 4693: speech act
    {"ipa": "/spiːtʃ ækt/", "vi": "hành vi ngôn từ; hành động bằng lời", "pos": "phrase"},
    # 4694: sports page
    {"ipa": "/spɔːrts peɪdʒ/", "vi": "chuyên trang thể thao trên báo chí", "pos": "phrase"},
    # 4695: square deal
    {"ipa": "/skwɛr diːl/", "vi": "sự đối xử công bằng sòng phẳng", "pos": "phrase"},
    # 4696: standard pressure
    {"ipa": "/ˈstændərd ˈprɛʃər/", "vi": "áp suất khí quyển tiêu chuẩn 1 atm", "pos": "phrase"},
    # 4697: stick around
    {"ipa": "/stɪk əˈraʊnd/", "vi": "nán lại gần đây chờ đợi; túc trực", "pos": "phrase"},
    # 4698: study hall
    {"ipa": "/ˈstʌdi hɔːl/", "vi": "phòng tự học yên tĩnh; tiết tự học", "pos": "phrase"},
    # 4699: sure as shooting
    {"ipa": "/ʃʊr æz ˈʃuːtɪŋ/", "vi": "chắc chắn như đinh đóng cột", "pos": "phrase"}
]

with open("scratch/b21_r10_raw_p2.json", "r", encoding="utf-8") as f:
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

with open("scratch/b21_r10_p2.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Successfully processed {len(output)} entries for Round 10 Part 2.")
