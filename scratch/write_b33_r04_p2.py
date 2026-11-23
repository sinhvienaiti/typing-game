import json

items = [
  {"id": "lex.en.200k.061603", "hw": "ovis poli", "pos": "phrase", "ipa": "/ˈoʊvɪs ˈpoʊlaɪ/", "vi": "cừu sừng xoắn Marco Polo châu Á"},
  {"id": "lex.en.200k.061604", "hw": "oxblood red", "pos": "phrase", "ipa": "/ˈɑːksblʌd rɛd/", "vi": "màu đỏ rượu vang huyết bò sẫm"},
  {"id": "lex.en.200k.061605", "hw": "pomace fly", "pos": "phrase", "ipa": "/ˈpʌmɪs flaɪ/", "vi": "loài ruồi giấm thích trái cây chín"},
  {"id": "lex.en.200k.061606", "hw": "progressive vaccinia", "pos": "phrase", "ipa": "/prəˈɡrɛsɪv vækˈsɪniə/", "vi": "biến chứng loét hoại tử vắc-xin đậu"},
  {"id": "lex.en.200k.061607", "hw": "regional enteritis", "pos": "phrase", "ipa": "/ˈriːdʒənl ˌɛntəˈraɪtɪs/", "vi": "bệnh viêm ruột từng vùng Crohn"},
  {"id": "lex.en.200k.061608", "hw": "robin redbreast", "pos": "phrase", "ipa": "/ˈrɑːbɪn ˈrɛdbrɛst/", "vi": "chim cổ đỏ châu Âu báo xuân"},
  {"id": "lex.en.200k.061609", "hw": "roman jakobson", "pos": "phrase", "ipa": "/ˈroʊmən ˈjɑːkəbsən/", "vi": "nhà ngôn ngữ học Roman Jakobson"},
  {"id": "lex.en.200k.061610", "hw": "saale river", "pos": "phrase", "ipa": "/ˈzɑːlə ˈrɪvər/", "vi": "dòng sông Saale miền trung nước Đức"},
  {"id": "lex.en.200k.061611", "hw": "salmo salar", "pos": "phrase", "ipa": "/ˈsælmoʊ ˈseɪlɑːr/", "vi": "loài cá hồi Đại Tây Dương di cư"},
  {"id": "lex.en.200k.061612", "hw": "saphenous vein", "pos": "phrase", "ipa": "/səˈfiːnəs veɪn/", "vi": "tĩnh mạch hiển nông ở chi dưới"},
  {"id": "lex.en.200k.061613", "hw": "senecio aureus", "pos": "phrase", "ipa": "/sɪˈniːʃioʊ ˈɔːriəs/", "vi": "cây cúc thảo dược vàng Bắc Mỹ"},
  {"id": "lex.en.200k.061614", "hw": "short saphenous vein", "pos": "phrase", "ipa": "/ʃɔːrt səˈfiːnəs veɪn/", "vi": "tĩnh mạch hiển ngắn bắp cẳng chân"},
  {"id": "lex.en.200k.061615", "hw": "sodium lauryl sulfate", "pos": "phrase", "ipa": "/ˈsoʊdiəm ˈlɔːrəl ˈsʌlfeɪt/", "vi": "chất tạo bọt tẩy rửa SLS natri"},
  {"id": "lex.en.200k.061616", "hw": "spanish peseta", "pos": "phrase", "ipa": "/ˈspænɪʃ pəˈseɪtə/", "vi": "đồng tiền cổ peseta Tây Ban Nha"},
  {"id": "lex.en.200k.061617", "hw": "sphenoid bone", "pos": "phrase", "ipa": "/ˈsfiːnɔɪd boʊn/", "vi": "xương bướm nằm ở nền giữa hộp sọ"},
  {"id": "lex.en.200k.061618", "hw": "staphylococcal infection", "pos": "phrase", "ipa": "/ˌstæfɪloʊˈkɑːkl ɪnˈfɛkʃən/", "vi": "nhiễm trùng vi khuẩn tụ cầu vàng"},
  {"id": "lex.en.200k.061619", "hw": "tufted titmouse", "pos": "phrase", "ipa": "/ˈtʌftɪd ˈtɪtmaʊs/", "vi": "chim bạc má mào nhọn Bắc Mỹ"},
  {"id": "lex.en.200k.061620", "hw": "william of wykeham", "pos": "phrase", "ipa": "/ˈwɪljəm əv ˈwɪkəm/", "vi": "Giám mục Anh William xứ Wykeham"},
  {"id": "lex.en.200k.061621", "hw": "aaves", "pos": "noun", "ipa": "/eɪ eɪ viː iːz/", "vi": "tiếng Anh bản địa Mỹ gốc Phi AAVE"},
  {"id": "lex.en.200k.061622", "hw": "algols", "pos": "noun", "ipa": "/ˈælɡɔːlz/", "vi": "ngôn ngữ lập trình cổ điển ALGOL"},
  {"id": "lex.en.200k.061623", "hw": "allografts", "pos": "noun", "ipa": "/ˈæloʊɡræfts/", "vi": "mảnh mô ghép đồng loại cùng loài"},
  {"id": "lex.en.200k.061624", "hw": "apulias", "pos": "noun", "ipa": "/əˈpjuːliəz/", "vi": "vùng gót giày Apulia miền nam Ý"},
  {"id": "lex.en.200k.061625", "hw": "betelgeuses", "pos": "noun", "ipa": "/ˈbiːtldʒuːzɪz/", "vi": "sao siêu khổng lồ đỏ Betelgeuse"},
  {"id": "lex.en.200k.061626", "hw": "betulas", "pos": "noun", "ipa": "/ˈbɛtjʊləz/", "vi": "chi cây gỗ bạch dương vỏ trắng"},
  {"id": "lex.en.200k.061627", "hw": "bigwigs", "pos": "noun", "ipa": "/ˈbɪɡwɪɡz/", "vi": "nhân vật cộm cán; ông lớn quyền thế"},
  {"id": "lex.en.200k.061628", "hw": "brindisis", "pos": "noun", "ipa": "/brɪnˈdiːzɪz/", "vi": "thành phố cảng Brindisi miền nam Ý"},
  {"id": "lex.en.200k.061629", "hw": "carabiners", "pos": "noun", "ipa": "/ˌkærəˈbiːnərz/", "vi": "móc khóa an toàn leo núi carabiner"},
  {"id": "lex.en.200k.061630", "hw": "carrels", "pos": "noun", "ipa": "/ˈkærəlz/", "vi": "bàn học cá nhân có vách thư viện"},
  {"id": "lex.en.200k.061631", "hw": "catabolisms", "pos": "noun", "ipa": "/kəˈtæbəlɪzəmz/", "vi": "quá trình dị hóa phân giải chất"},
  {"id": "lex.en.200k.061632", "hw": "challahs", "pos": "noun", "ipa": "/ˈxɑːləz/", "vi": "bánh mì tết bím ngày lễ Do Thái"},
  {"id": "lex.en.200k.061633", "hw": "charnels", "pos": "noun", "ipa": "/ˈtʃɑːrnlz/", "vi": "nhà chứa hài cốt; hầm mộ xương cốt"},
  {"id": "lex.en.200k.061634", "hw": "chlorates", "pos": "noun", "ipa": "/ˈklɔːreɪts/", "vi": "muối hóa chất oxy hóa mạnh clorat"},
  {"id": "lex.en.200k.061635", "hw": "chungkings", "pos": "noun", "ipa": "/ˌtʃʊŋˈkɪŋz/", "vi": "thành phố Trùng Khánh Trung Quốc"},
  {"id": "lex.en.200k.061636", "hw": "crossbreeds", "pos": "noun", "ipa": "/ˈkrɔːsbriːdz/", "vi": "giống vật nuôi cây trồng lai tạo"},
  {"id": "lex.en.200k.061637", "hw": "cruddier", "pos": "adj", "ipa": "/ˈkrʌdiər/", "vi": "bẩn thỉu cáu ghét hơn; tồi tệ hơn"},
  {"id": "lex.en.200k.061638", "hw": "cruddiest", "pos": "adj", "ipa": "/ˈkrʌdiɪst/", "vi": "bẩn thỉu ghê tởm nhất; tồi tệ nhất"},
  {"id": "lex.en.200k.061639", "hw": "daikons", "pos": "noun", "ipa": "/ˈdaɪkɑːnz/", "vi": "củ cải trắng khổng lồ Nhật Bản"},
  {"id": "lex.en.200k.061640", "hw": "deliuses", "pos": "noun", "ipa": "/ˈdiːliəsɪz/", "vi": "nhà soạn nhạc Anh Frederick Delius"},
  {"id": "lex.en.200k.061641", "hw": "diaghilevs", "pos": "noun", "ipa": "/diˈæɡɪlɛvz/", "vi": "ông bầu ba lê Nga Sergei Diaghilev"},
  {"id": "lex.en.200k.061642", "hw": "diols", "pos": "noun", "ipa": "/ˈdaɪoʊlz/", "vi": "hợp chất rượu hữu cơ hai nhóm OH"},
  {"id": "lex.en.200k.061643", "hw": "downdrafts", "pos": "noun", "ipa": "/ˈdaʊndræfts/", "vi": "luồng gió giáng thẳng xuống mặt đất"},
  {"id": "lex.en.200k.061644", "hw": "ecclesiologies", "pos": "noun", "ipa": "/ɪˌkliːziˈɑːlədʒiz/", "vi": "giáo hội học nghiên cứu hội thánh"},
  {"id": "lex.en.200k.061645", "hw": "elmonts", "pos": "noun", "ipa": "/ˈɛlmɑːnts/", "vi": "khu dân cư Elmont bang New York"},
  {"id": "lex.en.200k.061646", "hw": "elns", "pos": "noun", "ipa": "/iː ɛl ɛnz/", "vi": "quân đội giải phóng quốc gia ELN"},
  {"id": "lex.en.200k.061647", "hw": "ethicists", "pos": "noun", "ipa": "/ˈɛθɪsɪsts/", "vi": "nhà nghiên cứu triết học đạo đức"},
  {"id": "lex.en.200k.061648", "hw": "fastnesses", "pos": "noun", "ipa": "/ˈfæstnəsɪz/", "vi": "pháo đài kiên cố hiểm trở; độ bền"},
  {"id": "lex.en.200k.061649", "hw": "fermions", "pos": "noun", "ipa": "/ˈfɜːrmiɑːnz/", "vi": "hạt cơ bản vật chất fermion vật lý"},
  {"id": "lex.en.200k.061650", "hw": "floreys", "pos": "noun", "ipa": "/ˈflɔːriz/", "vi": "nhà dược lý tìm penicillin Florey"},
  {"id": "lex.en.200k.061651", "hw": "flytraps", "pos": "noun", "ipa": "/ˈflaɪtræps/", "vi": "dụng cụ bẫy ruồi; cây bắt ruồi"},
  {"id": "lex.en.200k.061652", "hw": "freeloaders", "pos": "noun", "ipa": "/ˈfriːloʊdərz/", "vi": "kẻ ăn chực ăn bám không chịu trả"},
  {"id": "lex.en.200k.061653", "hw": "garonnes", "pos": "noun", "ipa": "/ɡəˈrɑːnz/", "vi": "dòng sông lớn Garonne tây nam Pháp"},
  {"id": "lex.en.200k.061654", "hw": "gentlewomen", "pos": "noun", "ipa": "/ˈdʒɛntlwɪmɪn/", "vi": "quý bà lịch thiệp dòng dõi cao quý"},
  {"id": "lex.en.200k.061655", "hw": "giantesses", "pos": "noun", "ipa": "/ˈdʒaɪəntəsɪz/", "vi": "người đàn bà khổng lồ to lớn"},
  {"id": "lex.en.200k.061656", "hw": "guyots", "pos": "noun", "ipa": "/ɡiˈoʊz/", "vi": "núi ngầm đỉnh phẳng dưới đáy biển"},
  {"id": "lex.en.200k.061657", "hw": "halberds", "pos": "noun", "ipa": "/ˈhælbərdz/", "vi": "cây kích rìu giáo dài thời Trung cổ"},
  {"id": "lex.en.200k.061658", "hw": "haredim", "pos": "noun", "ipa": "/hɑːˈreɪdɪm/", "vi": "tín đồ Do Thái chính thống Haredi"},
  {"id": "lex.en.200k.061659", "hw": "haredis", "pos": "noun", "ipa": "/hɑːˈreɪdiz/", "vi": "các tín đồ Do Thái giáo Haredi"},
  {"id": "lex.en.200k.061660", "hw": "hemipteras", "pos": "noun", "ipa": "/hɪˈmɪptərəz/", "vi": "bộ côn trùng cánh nửa họ bọ xít"},
  {"id": "lex.en.200k.061661", "hw": "herakleses", "pos": "noun", "ipa": "/ˈhɛrəkliːzɪz/", "vi": "anh hùng dũng sĩ Hy Lạp Heracles"},
  {"id": "lex.en.200k.061662", "hw": "hoaglands", "pos": "noun", "ipa": "/ˈhoʊɡləndz/", "vi": "nhà sinh học Mahlon Hoagland Mỹ"},
  {"id": "lex.en.200k.061663", "hw": "hohenzollerns", "pos": "noun", "ipa": "/ˌhoʊənˈzɑːlərnz/", "vi": "hoàng tộc trị vì nước Phổ-Đức"},
  {"id": "lex.en.200k.061664", "hw": "hullos", "pos": "noun", "ipa": "/həˈloʊz/", "vi": "tiếng hô chào hỏi; lời chào mừng"},
  {"id": "lex.en.200k.061665", "hw": "iraks", "pos": "noun", "ipa": "/ɪˈrɑːks/", "vi": "nước Cộng hòa Iraq vùng Trung Đông"},
  {"id": "lex.en.200k.061666", "hw": "karyotypes", "pos": "noun", "ipa": "/ˈkɛrioʊtaɪps/", "vi": "bộ nhiễm sắc thể đặc trưng loài"},
  {"id": "lex.en.200k.061667", "hw": "kazakhstanis", "pos": "noun", "ipa": "/ˌkɑːzɑːkˈstɑːniz/", "vi": "công dân nước Cộng hòa Kazakhstan"},
  {"id": "lex.en.200k.061668", "hw": "klebsiellas", "pos": "noun", "ipa": "/ˌklɛbsiˈɛləz/", "vi": "vi khuẩn gây viêm phổi Klebsiella"},
  {"id": "lex.en.200k.061669", "hw": "loofahs", "pos": "noun", "ipa": "/ˈluːfəz/", "vi": "xơ mướp khô chà tắm; quả mướp hương"},
  {"id": "lex.en.200k.061670", "hw": "loupes", "pos": "noun", "ipa": "/luːps/", "vi": "kính lúp nhỏ đeo mắt thợ kim hoàn"},
  {"id": "lex.en.200k.061671", "hw": "mailbags", "pos": "noun", "ipa": "/ˈmeɪlbæɡz/", "vi": "túi bưu kiện đựng thư của bưu điện"},
  {"id": "lex.en.200k.061672", "hw": "malcontents", "pos": "noun", "ipa": "/ˌmælkənˈtɛnts/", "vi": "kẻ bất mãn chống đối chính quyền"},
  {"id": "lex.en.200k.061673", "hw": "mananas", "pos": "noun", "ipa": "/mɑːnˈjɑːnəz/", "vi": "ngày mai; thói quen trì hoãn việc"},
  {"id": "lex.en.200k.061674", "hw": "maniocs", "pos": "noun", "ipa": "/ˈmæniɑːks/", "vi": "củ khoai mì; cây sắn lấy bột năng"},
  {"id": "lex.en.200k.061675", "hw": "manzanitas", "pos": "noun", "ipa": "/ˌmænzəˈniːtəz/", "vi": "cây bụi gỗ cứng manzanita Tây Mỹ"},
  {"id": "lex.en.200k.061676", "hw": "marmosets", "pos": "noun", "ipa": "/ˈmɑːrməzɛts/", "vi": "loài khỉ đuôi dài tí hon Nam Mỹ"},
  {"id": "lex.en.200k.061677", "hw": "mashhads", "pos": "noun", "ipa": "/mæʃˈhɑːdz/", "vi": "thánh địa thành phố Mashhad Iran"},
  {"id": "lex.en.200k.061678", "hw": "matriarchies", "pos": "noun", "ipa": "/ˈmeɪtriɑːrkiz/", "vi": "chế độ mẫu hệ do phụ nữ đứng đầu"},
  {"id": "lex.en.200k.061679", "hw": "mccullerses", "pos": "noun", "ipa": "/məˈkʌlərzɪz/", "vi": "nữ nhà văn Mỹ Carson McCullers"},
  {"id": "lex.en.200k.061680", "hw": "midribs", "pos": "noun", "ipa": "/ˈmɪdrɪbz/", "vi": "đường gân chính giữa sống lá cây"},
  {"id": "lex.en.200k.061681", "hw": "millays", "pos": "noun", "ipa": "/mɪˈleɪz/", "vi": "nữ thi sĩ Mỹ Edna Vincent Millay"},
  {"id": "lex.en.200k.061682", "hw": "mimeses", "pos": "noun", "ipa": "/mɪˈmiːsiːz/", "vi": "sự bắt chước nghệ thuật; ngụy trang"},
  {"id": "lex.en.200k.061683", "hw": "minimuses", "pos": "noun", "ipa": "/ˈmɪnəməsɪz/", "vi": "ngón tay út; sinh vật nhỏ bé nhất"},
  {"id": "lex.en.200k.061684", "hw": "mistranslations", "pos": "noun", "ipa": "/ˌmɪstrænsˈleɪʃənz/", "vi": "lỗi dịch thuật sai nghĩa câu văn"},
  {"id": "lex.en.200k.061685", "hw": "moneylenders", "pos": "noun", "ipa": "/ˈmʌniˌlɛndərz/", "vi": "kẻ cho vay tiền lãi cao; chủ nợ"},
  {"id": "lex.en.200k.061686", "hw": "mousepads", "pos": "noun", "ipa": "/ˈmaʊspædz/", "vi": "tấm lót di chuột máy tính để bàn"},
  {"id": "lex.en.200k.061687", "hw": "mrds", "pos": "noun", "ipa": "/ɛm ɑːr diːz/", "vi": "từ điển điện tử đọc được bằng máy"},
  {"id": "lex.en.200k.061688", "hw": "nestoriuses", "pos": "noun", "ipa": "/nɛsˈtɔːriəsɪz/", "vi": "thượng phụ giáo phái Nestorius cổ"},
  {"id": "lex.en.200k.061689", "hw": "outfalls", "pos": "noun", "ipa": "/ˈaʊtfɔːlz/", "vi": "cửa xả nước thải ra sông hoặc biển"},
  {"id": "lex.en.200k.061690", "hw": "outsizes", "pos": "noun", "ipa": "/ˈaʊtsaɪzɪz/", "vi": "kích cỡ ngoại cỡ quá khổ lớn hơn"},
  {"id": "lex.en.200k.061691", "hw": "palimpsests", "pos": "noun", "ipa": "/ˈpælɪmpsɛsts/", "vi": "bản thảo cạo viết đè lên lớp cũ"},
  {"id": "lex.en.200k.061692", "hw": "papists", "pos": "noun", "ipa": "/ˈpeɪpɪsts/", "vi": "tín đồ theo Giáo hoàng Roma (cũ)"},
  {"id": "lex.en.200k.061693", "hw": "patrases", "pos": "noun", "ipa": "/ˈpætrəsɪz/", "vi": "thành phố cảng lớn Patras Hy Lạp"},
  {"id": "lex.en.200k.061694", "hw": "payableses", "pos": "noun", "ipa": "/ˈpeɪəblzɪz/", "vi": "khoản tiền nợ phải trả kế toán"},
  {"id": "lex.en.200k.061695", "hw": "phons", "pos": "noun", "ipa": "/fɑːnz/", "vi": "đơn vị đo độ to cảm nhận âm thanh"},
  {"id": "lex.en.200k.061696", "hw": "pinkoes", "pos": "noun", "ipa": "/ˈpɪŋkoʊz/", "vi": "người có khuynh hướng cánh tả nhẹ"},
  {"id": "lex.en.200k.061697", "hw": "pinkos", "pos": "noun", "ipa": "/ˈpɪŋkoʊz/", "vi": "người ngả theo quan điểm cánh tả"},
  {"id": "lex.en.200k.061698", "hw": "pions", "pos": "noun", "ipa": "/ˈpaɪɑːnz/", "vi": "hạt hạ nguyên tử meson pi vật lý"},
  {"id": "lex.en.200k.061699", "hw": "pleasances", "pos": "noun", "ipa": "/ˈplɛzənsɪz/", "vi": "khu vườn hoa kín đáo thanh tĩnh"},
  {"id": "lex.en.200k.061700", "hw": "porterhouses", "pos": "noun", "ipa": "/ˈpɔːrtərhaʊzɪz/", "vi": "miếng bít tết thăn chữ T hảo hạng"},
  {"id": "lex.en.200k.061701", "hw": "potlatches", "pos": "noun", "ipa": "/ˈpɑːtlætʃɪz/", "vi": "lễ hội tặng quà da đỏ Bắc Mỹ"},
  {"id": "lex.en.200k.061702", "hw": "proteomes", "pos": "noun", "ipa": "/ˈproʊtioʊmz/", "vi": "hệ toàn bộ protein của sinh vật"}
]

with open('scratch/b33_r04_raw_p2.json') as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100

for i, (item, r) in enumerate(zip(items, raw)):
    assert item['id'] == r['id'], f"Mismatch id at {i}: {item['id']} vs {r['id']}"
    assert item['hw'] == r['hw'], f"Mismatch hw at {i}: {item['hw']} vs {r['hw']}"
    assert len(item['vi']) <= 35, f"vi length > 35 at {i} ({item['hw']}): {len(item['vi'])}"
    assert item['pos'] in ['noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'], f"Invalid pos at {i}: {item['pos']}"
    if ' ' not in item['hw']:
        assert item['ipa'].startswith('/') and item['ipa'].endswith('/') and item['ipa'].count('/') == 2, f"Invalid ipa at {i}: {item['ipa']}"
    r['pos'] = item['pos']
    r['ipa'] = item['ipa']
    r['vi'] = item['vi']
    r['status'] = 'reviewed'

with open('scratch/b33_r04_p2.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Batch 33 Round 4 Part 2 validated and written successfully.")
