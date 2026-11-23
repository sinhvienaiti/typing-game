import json

# Manual word-by-word cognitive review for Batch 21 Round 10 Part 4 (records 4800-4899, IDs 200k.004802 to 200k.004901)
reviewed_entries = [
    # 4800: red cent
    {"ipa": "/rɛd sɛnt/", "vi": "một xu lẻ; đồng xu nhỏ không đáng", "pos": "phrase"},
    # 4801: reference work
    {"ipa": "/ˈrɛfrəns wɜːrk/", "vi": "sách tra cứu; tài liệu tham khảo", "pos": "phrase"},
    # 4802: religious song
    {"ipa": "/rɪˈlɪdʒəs sɔːŋ/", "vi": "bài thánh ca; ca khúc tôn giáo", "pos": "phrase"},
    # 4803: rest mass
    {"ipa": "/rɛst mæs/", "vi": "khối lượng nghỉ trong vật lý học", "pos": "phrase"},
    # 4804: ring girl
    {"ipa": "/rɪŋ ɡɜːrl/", "vi": "cô gái cầm biển hiệp đấu quyền anh", "pos": "phrase"},
    # 4805: roll around
    {"ipa": "/roʊl əˈraʊnd/", "vi": "lại đến hẹn; lăn tròn qua lại", "pos": "phrase"},
    # 4806: running pop
    {"ipa": "/ˈrʌnɪŋ pɑːp/", "vi": "cây lạc tiên hoa đỏ; dây chanh leo", "pos": "phrase"},
    # 4807: russian capital
    {"ipa": "/ˈrʌʃn ˈkæpɪtl/", "vi": "thủ đô Mát-xcơ-va của nước Nga", "pos": "phrase"},
    # 4808: sales campaign
    {"ipa": "/seɪlz kæmˈpeɪn/", "vi": "chiến dịch đẩy mạnh bán hàng hóa", "pos": "phrase"},
    # 4809: section eight
    {"ipa": "/ˈsɛkʃən eɪt/", "vi": "lệnh giải ngũ tâm thần; kẻ tâm thần", "pos": "phrase"},
    # 4810: sense of purpose
    {"ipa": "/sɛns ʌv ˈpɜːrpəs/", "vi": "ý thức về mục đích sống cuộc đời", "pos": "phrase"},
    # 4811: service firm
    {"ipa": "/ˈsɜːrvɪs fɜːrm/", "vi": "công ty cung ứng dịch vụ thương mại", "pos": "phrase"},
    # 4812: sex cell
    {"ipa": "/sɛks sɛl/", "vi": "tế bào sinh dục; giao tử sinh sản", "pos": "phrase"},
    # 4813: shape up
    {"ipa": "/ʃeɪp ʌp/", "vi": "tiến triển tốt; rèn luyện thân thể", "pos": "phrase"},
    # 4814: software system
    {"ipa": "/ˈsɔːftwɛr ˈsɪstəm/", "vi": "hệ thống phần mềm ứng dụng máy tính", "pos": "phrase"},
    # 4815: soul food
    {"ipa": "/soʊl fuːd/", "vi": "món ăn truyền thống người da đen Mỹ", "pos": "phrase"},
    # 4816: south american indian
    {"ipa": "/saʊθ əˈmɛrɪkən ˈɪndiən/", "vi": "thổ dân da đỏ bản địa vùng Nam Mỹ", "pos": "phrase"},
    # 4817: stage direction
    {"ipa": "/steɪdʒ dəˈrɛkʃən/", "vi": "lời chỉ dẫn diễn xuất kịch bản", "pos": "phrase"},
    # 4818: stay fresh
    {"ipa": "/steɪ frɛʃ/", "vi": "giữ được độ tươi ngon lâu hỏng", "pos": "phrase"},
    # 4819: technical school
    {"ipa": "/ˈtɛknɪkl skuːl/", "vi": "trường trung cấp kỹ thuật thực hành", "pos": "phrase"},
    # 4820: tell apart
    {"ipa": "/tɛl əˈpɑːrt/", "vi": "phân biệt rạch ròi giữa hai vật", "pos": "phrase"},
    # 4821: test equipment
    {"ipa": "/tɛst ɪˈkwɪpmənt/", "vi": "trang thiết bị kiểm tra đo lường", "pos": "phrase"},
    # 4822: texas star
    {"ipa": "/ˈtɛksəs stɑːr/", "vi": "cây hoa sao Texas Lindheimera", "pos": "phrase"},
    # 4823: time zone
    {"ipa": "/taɪm zoʊn/", "vi": "múi giờ chuẩn trên toàn thế giới", "pos": "phrase"},
    # 4824: tired of
    {"ipa": "/ˈtaɪərd ʌv/", "vi": "chán ngấy; phát mệt với ai việc gì", "pos": "phrase"},
    # 4825: title bar
    {"ipa": "/ˈtaɪtl bɑːr/", "vi": "thanh tiêu đề cửa sổ phần mềm máy", "pos": "phrase"},
    # 4826: trade secret
    {"ipa": "/treɪd ˈsiːkrət/", "vi": "bí mật kinh doanh thương mại", "pos": "phrase"},
    # 4827: trial period
    {"ipa": "/ˈtraɪəl ˈpɪriəd/", "vi": "giai đoạn thử việc; thời gian thử", "pos": "phrase"},
    # 4828: type species
    {"ipa": "/taɪp ˈspiːʃiːz/", "vi": "loài chuẩn trong phân loại sinh học", "pos": "phrase"},
    # 4829: victory day
    {"ipa": "/ˈvɪktəri deɪ/", "vi": "Ngày Chiến thắng mừng hòa bình", "pos": "phrase"},
    # 4830: warm to
    {"ipa": "/wɔːrm tuː/", "vi": "hào hứng đón nhận; bắt đầu quý mến", "pos": "phrase"},
    # 4831: waste matter
    {"ipa": "/weɪst ˈmætər/", "vi": "chất thải bỏ đi; cặn bã phế thải", "pos": "phrase"},
    # 4832: wear upon
    {"ipa": "/wɛr əˈpɑːn/", "vi": "làm kiệt sức mỏi mòn; đè nặng lên", "pos": "phrase"},
    # 4833: west wind
    {"ipa": "/wɛst wɪnd/", "vi": "ngọn gió thổi từ phương tây tới", "pos": "phrase"},
    # 4834: word division
    {"ipa": "/wɜːrd dɪˈvɪʒən/", "vi": "việc ngắt từ xuống dòng bản in", "pos": "phrase"},
    # 4835: words per minute
    {"ipa": "/wɜːrdz pər ˈmɪnɪt/", "vi": "số từ gõ được mỗi phút tốc độ WPM", "pos": "phrase"},
    # 4836: written material
    {"ipa": "/ˈrɪtn məˈtɪriəl/", "vi": "tài liệu viết; ấn phẩm văn bản in", "pos": "phrase"},
    # 4837: dues
    {"ipa": "/duːz/", "vi": "các khoản hội phí; những quyền lợi", "pos": "noun"},
    # 4838: humaner
    {"ipa": "/hjuːˈmeɪnər/", "vi": "nhân đạo hơn; giàu tình người hơn", "pos": "adj"},
    # 4839: humanest
    {"ipa": "/hjuːˈmeɪnɪst/", "vi": "nhân đạo nhất; giàu tình người nhất", "pos": "adj"},
    # 4840: rs
    {"ipa": "/ɑːrz/", "vi": "những chữ cái R; các âm rung R", "pos": "noun"},
    # 4841: adult body
    {"ipa": "/əˈdʌlt ˈbɑːdi/", "vi": "thân xác người lớn trưởng thành", "pos": "phrase"},
    # 4842: agency security
    {"ipa": "/ˈeɪdʒənsi sɪˈkjʊrəti/", "vi": "trái phiếu cơ quan chính phủ", "pos": "phrase"},
    # 4843: arms deal
    {"ipa": "/ɑːrmz diːl/", "vi": "thương vụ mua bán vũ khí quân dụng", "pos": "phrase"},
    # 4844: army unit
    {"ipa": "/ˈɑːrmi ˈjuːnɪt/", "vi": "đơn vị quân đội lục quân vũ trang", "pos": "phrase"},
    # 4845: bank of japan
    {"ipa": "/bæŋk ʌv dʒəˈpæn/", "vi": "Ngân hàng Trung ương Nhật Bản BOJ", "pos": "phrase"},
    # 4846: bar code
    {"ipa": "/bɑːr koʊd/", "vi": "mã vạch hàng hóa; mã vạch quét đọc", "pos": "phrase"},
    # 4847: bear out
    {"ipa": "/bɛr aʊt/", "vi": "xác thực tính đúng đắn; chứng thực", "pos": "phrase"},
    # 4848: bear up
    {"ipa": "/bɛr ʌp/", "vi": "vững vàng kiên cường vượt qua nạn", "pos": "phrase"},
    # 4849: best evidence rule
    {"ipa": "/bɛst ˈɛvɪdəns ruːl/", "vi": "quy tắc ưu tiên chứng cứ bản gốc", "pos": "phrase"},
    # 4850: black cat
    {"ipa": "/blæk kæt/", "vi": "con mèo đen; mèo mun lông đen tuyền", "pos": "phrase"},
    # 4851: book bag
    {"ipa": "/bʊk bæɡ/", "vi": "cặp xách sách vở; ba lô học sinh", "pos": "phrase"},
    # 4852: border on
    {"ipa": "/ˈbɔːrdər ɑːn/", "vi": "tiếp giáp biên giới; gần như suýt", "pos": "phrase"},
    # 4853: bringing up
    {"ipa": "/ˈbrɪŋɪŋ ʌp/", "vi": "công ơn nuôi dưỡng; dưỡng dục trẻ", "pos": "phrase"},
    # 4854: calling card
    {"ipa": "/ˈkɔːlɪŋ kɑːrd/", "vi": "danh thiếp cá nhân; thẻ điện thoại", "pos": "phrase"},
    # 4855: capital of california
    {"ipa": "/ˈkæpɪtl ʌv ˌkælɪˈfɔːrnjə/", "vi": "thủ phủ Sacramento bang California", "pos": "phrase"},
    # 4856: center of mass
    {"ipa": "/ˈsɛntər ʌv mæs/", "vi": "khối tâm điểm đặt khối lượng vật", "pos": "phrase"},
    # 4857: christ within
    {"ipa": "/kraɪst wɪˈðɪn/", "vi": "Đức Kitô ngự trị trong tâm hồn", "pos": "phrase"},
    # 4858: christian church
    {"ipa": "/ˈkrɪstʃən tʃɜːrtʃ/", "vi": "giáo hội Kitô giáo; nhà thờ Cơ Đốc", "pos": "phrase"},
    # 4859: civil union
    {"ipa": "/ˈsɪvl ˈjuːnjən/", "vi": "kết hợp dân sự; kết đôi hợp pháp", "pos": "phrase"},
    # 4860: club drug
    {"ipa": "/klʌb drʌɡ/", "vi": "thuốc lắc quán bar; ma túy bar", "pos": "phrase"},
    # 4861: cold feet
    {"ipa": "/koʊld fiːt/", "vi": "chùn bước sợ hãi; lo lắng phút chót", "pos": "phrase"},
    # 4862: color property
    {"ipa": "/ˈkʌlər ˈprɑːpərti/", "vi": "thuộc tính màu sắc của hình ảnh", "pos": "phrase"},
    # 4863: crime rate
    {"ipa": "/kraɪm reɪt/", "vi": "tỷ lệ tội phạm trên đầu dân số", "pos": "phrase"},
    # 4864: cross section
    {"ipa": "/krɔːs ˈsɛkʃən/", "vi": "mặt cắt ngang; mẫu đại diện thu nhỏ", "pos": "phrase"},
    # 4865: cut glass
    {"ipa": "/kʌt ɡlæs/", "vi": "thủy tinh pha lê cắt mài hoa văn", "pos": "phrase"},
    # 4866: dinner party
    {"ipa": "/ˈdɪnər ˈpɑːrti/", "vi": "bữa tiệc tối chiêu đãi khách mời", "pos": "phrase"},
    # 4867: dinner service
    {"ipa": "/ˈdɪnər ˈsɜːrvɪs/", "vi": "bộ chén đĩa sứ bàn ăn tiệc tối", "pos": "phrase"},
    # 4868: district manager
    {"ipa": "/ˈdɪstrɪkt ˈmænɪdʒər/", "vi": "quản lý vùng phụ trách khu vực", "pos": "phrase"},
    # 4869: double cross
    {"ipa": "/ˈdʌbl krɔːs/", "vi": "sự phản bội hai lòng; đâm sau lưng", "pos": "phrase"},
    # 4870: draw close
    {"ipa": "/drɔː kloʊs/", "vi": "tiến lại gần; cận kề thời điểm", "pos": "phrase"},
    # 4871: driving range
    {"ipa": "/ˈdraɪvɪŋ reɪndʒ/", "vi": "sân tập đánh bóng gôn bãi cỏ rộng", "pos": "phrase"},
    # 4872: european russia
    {"ipa": "/ˌjʊrəˈpiːən ˈrʌʃə/", "vi": "phần lãnh thổ châu Âu của nước Nga", "pos": "phrase"},
    # 4873: eye contact
    {"ipa": "/aɪ ˈkɑːntækt/", "vi": "giao tiếp bằng ánh mắt nhìn nhau", "pos": "phrase"},
    # 4874: farm team
    {"ipa": "/fɑːrm tiːm/", "vi": "đội tuyển trẻ đào tạo nguồn dự bị", "pos": "phrase"},
    # 4875: field glass
    {"ipa": "/fiːld ɡlæs/", "vi": "ống nhòm dã chiến hai mắt", "pos": "phrase"},
    # 4876: fighting french
    {"ipa": "/ˈfaɪtɪŋ frɛntʃ/", "vi": "lực lượng Kháng chiến Pháp tự do", "pos": "phrase"},
    # 4877: file away
    {"ipa": "/faɪl əˈweɪ/", "vi": "lưu trữ vào cặp tài liệu hồ sơ", "pos": "phrase"},
    # 4878: first quarter
    {"ipa": "/fɜːrst ˈkwɔːrtər/", "vi": "tuần trăng đầu tháng; quý một năm", "pos": "phrase"},
    # 4879: floor cover
    {"ipa": "/flɔːr ˈkʌvər/", "vi": "thảm trải sàn nhà; tấm lót sàn", "pos": "phrase"},
    # 4880: general services administration
    {"ipa": "/ˈdʒɛnrəl ˈsɜːrvɪsɪz ədˌmɪnɪˈstreɪʃən/", "vi": "Cục Quản lý Dịch vụ Tổng hợp Hoa Kỳ", "pos": "phrase"},
    # 4881: german mark
    {"ipa": "/ˈdʒɜːrmən mɑːrk/", "vi": "đồng Mác tiền tệ cũ của nước Đức", "pos": "phrase"},
    # 4882: go to pieces
    {"ipa": "/ɡoʊ tuː ˈpiːsɪz/", "vi": "suy sụp tinh thần; vỡ òa tan nát", "pos": "phrase"},
    # 4883: good afternoon
    {"ipa": "/ɡʊd ˌæftərˈnuːn/", "vi": "chào buổi chiều; lời chào ban chiều", "pos": "phrase"},
    # 4884: hard copy
    {"ipa": "/hɑːrd ˈkɑːpi/", "vi": "bản in trên giấy; bản cứng hồ sơ", "pos": "phrase"},
    # 4885: higher status
    {"ipa": "/ˈhaɪər ˈsteɪtəs/", "vi": "địa vị xã hội cao hơn; bậc trên", "pos": "phrase"},
    # 4886: home guard
    {"ipa": "/hoʊm ɡɑːrd/", "vi": "lực lượng dân quân tự vệ quê nhà", "pos": "phrase"},
    # 4887: home port
    {"ipa": "/hoʊm pɔːrt/", "vi": "cảng đăng ký của tàu; cảng nhà đỗ", "pos": "phrase"},
    # 4888: hot spot
    {"ipa": "/hɑːt spɑːt/", "vi": "điểm nóng chiến sự; điểm phát sóng", "pos": "phrase"},
    # 4889: house martin
    {"ipa": "/haʊs ˈmɑːrtɪn/", "vi": "loài chim nhạn làm tổ góc nhà", "pos": "phrase"},
    # 4890: human waste
    {"ipa": "/ˈhjuːmən weɪst/", "vi": "chất thải bài tiết của loài người", "pos": "phrase"},
    # 4891: hundred and one
    {"ipa": "/ˈhʌndrəd ænd wʌn/", "vi": "một trăm lẻ một; vô số điều kể", "pos": "phrase"},
    # 4892: indian chief
    {"ipa": "/ˈɪndiən tʃiːf/", "vi": "tù trưởng bộ tộc da đỏ bản địa Mỹ", "pos": "phrase"},
    # 4893: kick back
    {"ipa": "/kɪk bæk/", "vi": "thư giãn nghỉ ngơi; tiền lại quả", "pos": "phrase"},
    # 4894: knowledge base
    {"ipa": "/ˈnɑːlɪdʒ beɪs/", "vi": "cơ sở tri thức thông tin dữ liệu", "pos": "phrase"},
    # 4895: language learning
    {"ipa": "/ˈlæŋɡwɪdʒ ˈlɜːrnɪŋ/", "vi": "việc học tập rèn luyện ngoại ngữ", "pos": "phrase"},
    # 4896: legal opinion
    {"ipa": "/ˈliːɡl əˈpɪnjən/", "vi": "ý kiến tư vấn pháp lý của luật sư", "pos": "phrase"},
    # 4897: live birth
    {"ipa": "/laɪv bɜːrθ/", "vi": "ca sinh con còn sống khỏe mạnh", "pos": "phrase"},
    # 4898: long iron
    {"ipa": "/lɔːŋ ˈaɪərn/", "vi": "gậy sắt dài số nhỏ trong môn golf", "pos": "phrase"},
    # 4899: low profile
    {"ipa": "/loʊ ˈproʊfaɪl/", "vi": "thái độ khiêm nhường kín tiếng", "pos": "phrase"}
]

with open("scratch/b21_r10_raw_p4.json", "r", encoding="utf-8") as f:
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

with open("scratch/b21_r10_p4.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"Successfully processed {len(output)} entries for Round 10 Part 4.")
