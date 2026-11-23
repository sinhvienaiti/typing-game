import json

with open('scratch/b32_r04_raw_p4.json') as f:
    raw_items = json.load(f)

reviewed_data = {
    "lex.en.200k.056802": {"pos": "noun", "ipa": "/ˌmɛɡələˈmeɪniæks/", "vi": "kẻ mắc chứng hoang tưởng tự đại"},
    "lex.en.200k.056803": {"pos": "noun", "ipa": "/maɪˈkrɑːmɪtərz/", "vi": "thước trắc vi micrometer; vi mét"},
    "lex.en.200k.056804": {"pos": "noun", "ipa": "/ˈmaɪkroʊˌtuːbjuːlz/", "vi": "các vi ống hình ống trong tế bào"},
    "lex.en.200k.056805": {"pos": "noun", "ipa": "/ˈneɪtʃərɪsts/", "vi": "người theo chủ nghĩa khỏa thân"},
    "lex.en.200k.056806": {"pos": "noun", "ipa": "/ˈniːəfaɪts/", "vi": "người mới nhập môn; tín đồ mới"},
    "lex.en.200k.056807": {"pos": "verb", "ipa": "/nɑːkt/", "vi": "đã lắp tên vào dây cung; khía rãnh"},
    "lex.en.200k.056808": {"pos": "verb", "ipa": "/ˈnɑːkɪŋ/", "vi": "lắp tên vào dây cung; khía rãnh"},
    "lex.en.200k.056809": {"pos": "verb", "ipa": "/nɑːks/", "vi": "lắp tên vào dây cung; khía khuyết"},
    "lex.en.200k.056810": {"pos": "noun", "ipa": "/ˌɛnˌɛsˈjuːz/", "vi": "viêm niệu đạo không đặc hiệu NSU"},
    "lex.en.200k.056811": {"pos": "noun", "ipa": "/nɪˈæsəlændz/", "vi": "xứ Nyasaland; lãnh thổ Malawi xưa"},
    "lex.en.200k.056812": {"pos": "noun", "ipa": "/ˌɔːrɪˈnoʊkoʊz/", "vi": "con sông Orinoco ở Nam Mỹ"},
    "lex.en.200k.056813": {"pos": "noun", "ipa": "/oʊˈrɔːskoʊz/", "vi": "họa sĩ bích họa José Orozco"},
    "lex.en.200k.056814": {"pos": "noun", "ipa": "/ˌɔːrθəˈpiːdɪksɪz/", "vi": "khoa chấn thương chỉnh hình xương"},
    "lex.en.200k.056815": {"pos": "noun", "ipa": "/ˈoʊvərɪdʒɪz/", "vi": "số lượng dư thừa; hàng hóa dôi ra"},
    "lex.en.200k.056816": {"pos": "noun", "ipa": "/ˈpænəpliz/", "vi": "bộ giáp trụ; bộ sưu tập lộng lẫy"},
    "lex.en.200k.056817": {"pos": "noun", "ipa": "/pænˈsɛkʃuəlz/", "vi": "người toàn tính; toàn tính luyến"},
    "lex.en.200k.056818": {"pos": "noun", "ipa": "/ˈpeɪpərklɪps/", "vi": "cái kẹp giấy kim loại văn phòng"},
    "lex.en.200k.056819": {"pos": "noun", "ipa": "/ˈpæpuənz/", "vi": "người dân bản địa Papua New Guinea"},
    "lex.en.200k.056820": {"pos": "noun", "ipa": "/ˌpævəˈrɑːtiz/", "vi": "danh ca opera Luciano Pavarotti"},
    "lex.en.200k.056821": {"pos": "noun", "ipa": "/ˈpɛnaɪnzɪz/", "vi": "dãy núi Pennines ở nước Anh"},
    "lex.en.200k.056822": {"pos": "noun", "ipa": "/ˈpiːɑːnz/", "vi": "người làm công nhật; kẻ tôi đòi"},
    "lex.en.200k.056823": {"pos": "noun", "ipa": "/pəˈruːzəlz/", "vi": "sự đọc kỹ càng; sự xem xét thấu đáo"},
    "lex.en.200k.056824": {"pos": "noun", "ipa": "/ˈfæntæzəmz/", "vi": "hình bóng ma quái; ảo ảnh viển vông"},
    "lex.en.200k.056825": {"pos": "noun", "ipa": "/ˈpriːtərz/", "vi": "quan pháp quan thời La Mã cổ đại"},
    "lex.en.200k.056826": {"pos": "noun", "ipa": "/ˌpiːˌɛsˈɛfs/", "vi": "hàm phân bố điểm nhòe PSF"},
    "lex.en.200k.056827": {"pos": "noun", "ipa": "/pɪɡˈmeɪliənz/", "vi": "chàng thợ điêu khắc Pygmalion"},
    "lex.en.200k.056828": {"pos": "noun", "ipa": "/paɪˈrɑːləsiːz/", "vi": "quá trình nhiệt phân hủy hóa học"},
    "lex.en.200k.056829": {"pos": "noun", "ipa": "/ˈreɪndrɑːps/", "vi": "những hạt mưa rơi tí tách"},
    "lex.en.200k.056830": {"pos": "noun", "ipa": "/ræˈtænz/", "vi": "cây mây dẻo; roi song mây quất phạt"},
    "lex.en.200k.056831": {"pos": "noun", "ipa": "/ˈrætlərz/", "vi": "rắn đuôi chuông; xe lửa cũ lọc cọc"},
    "lex.en.200k.056832": {"pos": "noun", "ipa": "/ˌriːəˈpreɪzəlz/", "vi": "sự đánh giá lại; sự tái thẩm định"},
    "lex.en.200k.056833": {"pos": "noun", "ipa": "/riːˈbrɔːdkæsts/", "vi": "chương trình truyền hình phát lại"},
    "lex.en.200k.056834": {"pos": "verb", "ipa": "/riːdɪd/", "vi": "đã đưa ra lời khuyên; đã giải mộng"},
    "lex.en.200k.056835": {"pos": "verb", "ipa": "/riːdz/", "vi": "khuyên giải; giải thích điều bí ẩn"},
    "lex.en.200k.056836": {"pos": "verb", "ipa": "/ˈriːdɪŋ/", "vi": "khuyên nhủ; phân giải điềm báo"},
    "lex.en.200k.056837": {"pos": "noun", "ipa": "/ræmˈboʊz/", "vi": "nhà thơ tài hoa Arthur Rimbaud"},
    "lex.en.200k.056838": {"pos": "noun", "ipa": "/ˈrʊdrəz/", "vi": "thần bão tố gầm thét Rudra Ấn Độ"},
    "lex.en.200k.056839": {"pos": "noun", "ipa": "/ˈrʌmpəsɪz/", "vi": "sự ầm ĩ náo loạn; cuộc ẩu đả ồn ào"},
    "lex.en.200k.056840": {"pos": "noun", "ipa": "/ˈsæsəfræsɪz/", "vi": "cây xá xị thơm họ Nguyệt quế"},
    "lex.en.200k.056841": {"pos": "noun", "ipa": "/skæmps/", "vi": "đứa trẻ láu lỉnh; kẻ ranh mãnh"},
    "lex.en.200k.056842": {"pos": "noun", "ipa": "/ˈskuːlmeɪts/", "vi": "bạn học cùng lớp; bạn cùng trường"},
    "lex.en.200k.056843": {"pos": "noun", "ipa": "/skriːdz/", "vi": "bài văn dài dòng; thanh gạt vữa"},
    "lex.en.200k.056844": {"pos": "noun", "ipa": "/ˈsɛkjələrɪsts/", "vi": "người theo chủ nghĩa thế tục hóa"},
    "lex.en.200k.056845": {"pos": "noun", "ipa": "/ˈʃɪpˌbɪldərz/", "vi": "thợ đóng tàu thủy; nhà máy đóng tàu"},
    "lex.en.200k.056846": {"pos": "noun", "ipa": "/ˈʃoʊboʊts/", "vi": "tàu hát lưu động; kẻ thích làm màu"},
    "lex.en.200k.056847": {"pos": "noun", "ipa": "/ˈsiːkɪzəmz/", "vi": "đạo Sikh; tôn giáo người Sikh Ấn Độ"},
    "lex.en.200k.056848": {"pos": "noun", "ipa": "/sməˈlɛnsks/", "vi": "thành phố cổ Smolensk ở Nga"},
    "lex.en.200k.056849": {"pos": "noun", "ipa": "/ˈspeɪssuːts/", "vi": "bộ đồ du hành vũ trụ kín áp suất"},
    "lex.en.200k.056850": {"pos": "noun", "ipa": "/ˈspɛŋɡlərz/", "vi": "triết gia sử học Oswald Spengler"},
    "lex.en.200k.056851": {"pos": "noun", "ipa": "/ˈspaɪkiː/", "vi": "sao Giác Spica chòm Xử Nữ"},
    "lex.en.200k.056852": {"pos": "noun", "ipa": "/ˈspaɪkəz/", "vi": "ngôi sao Spica; kiểu băng số 8"},
    "lex.en.200k.056853": {"pos": "noun", "ipa": "/ˈstruːdəlz/", "vi": "bánh ngọt cuộn nhiều lớp strudel"},
    "lex.en.200k.056854": {"pos": "noun", "ipa": "/ˌsuːpərˈɑːksaɪdz/", "vi": "hợp chất gốc tự do superoxit"},
    "lex.en.200k.056855": {"pos": "noun", "ipa": "/səˈsteɪnmənts/", "vi": "sự duy trì hỗ trợ; bảo đảm hậu cần"},
    "lex.en.200k.056856": {"pos": "noun", "ipa": "/ˌtæbjuˈleɪʃənz/", "vi": "sự lập bảng số liệu biểu đồ"},
    "lex.en.200k.056857": {"pos": "noun", "ipa": "/ˈteɪlspɪnz/", "vi": "sự lao dốc xoắn ốc; đà suy thoái"},
    "lex.en.200k.056858": {"pos": "noun", "ipa": "/tɔːz/", "vi": "chữ cái Hebrew Tav; viên bi cái"},
    "lex.en.200k.056859": {"pos": "noun", "ipa": "/ˈθɛsəliz/", "vi": "vùng lịch sử Thessaly của Hy Lạp"},
    "lex.en.200k.056860": {"pos": "noun", "ipa": "/ˈθɔːrndaɪks/", "vi": "nhà tâm lý học Edward Thorndike"},
    "lex.en.200k.056861": {"pos": "noun", "ipa": "/ˈtɪpstərz/", "vi": "người mách nước cá cược chứng khoán"},
    "lex.en.200k.056862": {"pos": "adj", "ipa": "/ˈtuːθiər/", "vi": "răng to hơn; nhe nhiều răng hơn"},
    "lex.en.200k.056863": {"pos": "adj", "ipa": "/ˈtuːθiɪst/", "vi": "răng to nhất; nhe răng nhiều nhất"},
    "lex.en.200k.056864": {"pos": "noun", "ipa": "/ˈtɔːsərz/", "vi": "kẻ đáng ghét; người quăng ném đồ"},
    "lex.en.200k.056865": {"pos": "noun", "ipa": "/ˈtroʊpəsfiərz/", "vi": "tầng đối lưu khí quyển mặt đất"},
    "lex.en.200k.056866": {"pos": "noun", "ipa": "/ˈwiːɡʊərz/", "vi": "người dân tộc Duy Ngô Nhĩ Tân Cương"},
    "lex.en.200k.056867": {"pos": "noun", "ipa": "/ˈwiːɡʊərz/", "vi": "người dân tộc Duy Ngô Nhĩ"},
    "lex.en.200k.056868": {"pos": "noun", "ipa": "/vɛˈspeɪʒənz/", "vi": "Hoàng đế La Mã Vespasian"},
    "lex.en.200k.056869": {"pos": "noun", "ipa": "/ˈwɑːnəmeɪkərz/", "vi": "nhà bán lẻ John Wanamaker"},
    "lex.en.200k.056870": {"pos": "noun", "ipa": "/ˈwɛtstoʊnz/", "vi": "hòn đá mài dao kéo chuyên dụng"},
    "lex.en.200k.056871": {"pos": "noun", "ipa": "/ˈwaɪtaʊts/", "vi": "trận mù tuyết trắng xóa; bút xóa"},
    "lex.en.200k.056872": {"pos": "noun", "ipa": "/ˈviːləndz/", "vi": "đại thi hào Christoph Wieland"},
    "lex.en.200k.056873": {"pos": "noun", "ipa": "/ˈwɜːrkruːmz/", "vi": "phòng làm việc chế tác xưởng may"},
    "lex.en.200k.056874": {"pos": "phrase", "ipa": "", "vi": "học thuyết độc thần Tawhid Hồi giáo"},
    "lex.en.200k.056875": {"pos": "phrase", "ipa": "", "vi": "bác sĩ Nobel y học Alexis Carrel"},
    "lex.en.200k.056876": {"pos": "phrase", "ipa": "", "vi": "nhịp nhị phân hai phách alla breve"},
    "lex.en.200k.056877": {"pos": "phrase", "ipa": "", "vi": "chỉ số đánh giá trẻ sơ sinh Apgar"},
    "lex.en.200k.056878": {"pos": "phrase", "ipa": "", "vi": "hoa cúc đồng tiền rực rỡ sắc màu"},
    "lex.en.200k.056879": {"pos": "phrase", "ipa": "", "vi": "bè trầm đệm liên tục basso continuo"},
    "lex.en.200k.056880": {"pos": "phrase", "ipa": "", "vi": "cử chỉ cao thượng; nghĩa cử đẹp"},
    "lex.en.200k.056881": {"pos": "phrase", "ipa": "", "vi": "loài diều hâu săn mồi cánh lam xám"},
    "lex.en.200k.056882": {"pos": "phrase", "ipa": "", "vi": "trà thảo mộc hoa cúc thanh nhiệt"},
    "lex.en.200k.056883": {"pos": "phrase", "ipa": "", "vi": "con sông Chari đổ vào hồ Chad"},
    "lex.en.200k.056884": {"pos": "phrase", "ipa": "", "vi": "tổng thống Daniel Ortega Nicaragua"},
    "lex.en.200k.056885": {"pos": "phrase", "ipa": "", "vi": "thành phố cổ Al Bayda ở Libya"},
    "lex.en.200k.056886": {"pos": "phrase", "ipa": "", "vi": "cây thạch nam chuông hoa tím dại"},
    "lex.en.200k.056887": {"pos": "phrase", "ipa": "", "vi": "nhà sinh học Ernst Heinrich Haeckel"},
    "lex.en.200k.056888": {"pos": "phrase", "ipa": "", "vi": "và những người khác; cùng cộng sự"},
    "lex.en.200k.056889": {"pos": "phrase", "ipa": "", "vi": "biệt danh máy bay phản lực Leduc"},
    "lex.en.200k.056890": {"pos": "phrase", "ipa": "", "vi": "nhà soạn nhạc Pháp Francis Poulenc"},
    "lex.en.200k.056891": {"pos": "phrase", "ipa": "", "vi": "thằn lằn cổ bướm xòe diềm nước Úc"},
    "lex.en.200k.056892": {"pos": "phrase", "ipa": "", "vi": "chính khách La Mã Gaius Cassius"},
    "lex.en.200k.056893": {"pos": "phrase", "ipa": "", "vi": "chi cây bạch dương lá rụng Betula"},
    "lex.en.200k.056894": {"pos": "phrase", "ipa": "", "vi": "chi vi khuẩn đường ruột Klebsiella"},
    "lex.en.200k.056895": {"pos": "phrase", "ipa": "", "vi": "nhà thơ Ý Giambattista Marino"},
    "lex.en.200k.056896": {"pos": "phrase", "ipa": "", "vi": "động mạch cấp máu vùng mông"},
    "lex.en.200k.056897": {"pos": "phrase", "ipa": "", "vi": "tĩnh mạch dẫn lưu máu vùng mông"},
    "lex.en.200k.056898": {"pos": "phrase", "ipa": "", "vi": "xương rồng nhím gai Echinocereus"},
    "lex.en.200k.056899": {"pos": "phrase", "ipa": "", "vi": "loài sóc mac-mốt xám núi Bắc Mỹ"},
    "lex.en.200k.056900": {"pos": "phrase", "ipa": "", "vi": "thị trấn cảng Hoek van Holland"},
    "lex.en.200k.056901": {"pos": "phrase", "ipa": "", "vi": "bệnh nhiễm ký sinh trùng giun móc"}
}

output_items = []
errors = []

for item in raw_items:
    item_id = item['id']
    if item_id not in reviewed_data:
        errors.append(f"Missing reviewed data for {item_id}")
        continue
    
    rev = reviewed_data[item_id]
    vi = rev['vi']
    pos = rev['pos']
    ipa = rev['ipa']
    
    # Validation
    if len(vi) > 35:
        errors.append(f"Length violation (>35) for {item_id} ({item['hw']}): '{vi}' ({len(vi)} chars)")
    if pos not in ['noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase']:
        errors.append(f"Invalid POS '{pos}' for {item_id}")
    if ipa != "":
        if not (ipa.startswith('/') and ipa.endswith('/') and ipa.count('/') == 2):
            errors.append(f"Invalid IPA format '{ipa}' for {item_id}")
    elif ' ' not in item['hw']:
        errors.append(f"Single word missing IPA for {item_id} ({item['hw']})")
        
    new_item = {
        "id": item["id"],
        "hw": item["hw"],
        "pos": pos,
        "ipa": ipa,
        "vi": vi,
        "cefr": item.get("cefr", "C2"),
        "tier": item.get("tier", 5),
        "status": "reviewed",
        "notes": item.get("notes", "")
    }
    output_items.append(new_item)

if errors:
    print(f"Validation FAILED with {len(errors)} errors:")
    for e in errors:
        print(" - " + e)
    exit(1)

with open('scratch/b32_r04_p4.json', 'w', encoding='utf-8') as f:
    json.dump(output_items, f, ensure_ascii=False, indent=2)

print(f"Successfully authored and validated Part 4: {len(output_items)} items saved to scratch/b32_r04_p4.json")
