import json

items = [
  {"id": "lex.en.200k.063303", "hw": "doobs", "pos": "noun", "ipa": "/duːbz/", "vi": "cỏ gà Bermuda phủ bãi cỏ xanh"},
  {"id": "lex.en.200k.063304", "hw": "ducats", "pos": "noun", "ipa": "/ˈdʌkəts/", "vi": "đồng tiền vàng cổ châu Âu ducat"},
  {"id": "lex.en.200k.063305", "hw": "eratostheneses", "pos": "noun", "ipa": "/ˌɛrəˈtɑːsθəˌniːzɪz/", "vi": "nhà toán học Hy Lạp Eratosthenes"},
  {"id": "lex.en.200k.063306", "hw": "evangels", "pos": "noun", "ipa": "/ɪˈvændʒəlz/", "vi": "sách Phúc Âm; tin mừng cứu rỗi"},
  {"id": "lex.en.200k.063307", "hw": "faroeses", "pos": "noun", "ipa": "/ˌfɛəroʊˈiːzɪz/", "vi": "người dân và tiếng quần đảo Faroe"},
  {"id": "lex.en.200k.063308", "hw": "fleabags", "pos": "noun", "ipa": "/ˈfliːbæɡz/", "vi": "khách sạn xập xệ; con vật nhiều rận"},
  {"id": "lex.en.200k.063309", "hw": "fleshlier", "pos": "adj", "ipa": "/ˈflɛʃliər/", "vi": "nặng tính xác thịt nhục dục hơn"},
  {"id": "lex.en.200k.063310", "hw": "fleshliest", "pos": "adj", "ipa": "/ˈflɛʃliɪst/", "vi": "nặng tính xác thịt trần tục nhất"},
  {"id": "lex.en.200k.063311", "hw": "flunkies", "pos": "noun", "ipa": "/ˈflʌŋkiz/", "vi": "kẻ bợ đỡ hầu hạ nịnh hót cấp trên"},
  {"id": "lex.en.200k.063312", "hw": "flyways", "pos": "noun", "ipa": "/ˈflaɪweɪz/", "vi": "đường bay di cư định kỳ của chim"},
  {"id": "lex.en.200k.063313", "hw": "fooleries", "pos": "noun", "ipa": "/ˈfuːləriz/", "vi": "hành động ngốc nghếch khờ dại"},
  {"id": "lex.en.200k.063314", "hw": "friaries", "pos": "noun", "ipa": "/ˈfraɪəriz/", "vi": "tu viện của các tu sĩ hành khất"},
  {"id": "lex.en.200k.063315", "hw": "friesians", "pos": "noun", "ipa": "/ˈfriːʒənz/", "vi": "giống bò sữa lang trắng đen Hà Lan"},
  {"id": "lex.en.200k.063316", "hw": "gands", "pos": "noun", "ipa": "/ɡɑːndz/", "vi": "thành phố Ghent (Gand) của Bỉ"},
  {"id": "lex.en.200k.063317", "hw": "garbanzos", "pos": "noun", "ipa": "/ɡɑːrˈbɑːnzoʊz/", "vi": "hạt đậu gà bùi ngậy giàu đạm"},
  {"id": "lex.en.200k.063318", "hw": "graziers", "pos": "noun", "ipa": "/ˈɡreɪʒərz/", "vi": "chủ trang trại chăn thả gia súc cỏ"},
  {"id": "lex.en.200k.063319", "hw": "gushier", "pos": "adj", "ipa": "/ˈɡʌʃiər/", "vi": "dào dạt sướt mướt quá khích hơn"},
  {"id": "lex.en.200k.063320", "hw": "gushiest", "pos": "adj", "ipa": "/ˈɡʌʃiɪst/", "vi": "sướt mướt phô trương tình cảm nhất"},
  {"id": "lex.en.200k.063321", "hw": "hassels", "pos": "noun", "ipa": "/ˈhɑːsəlz/", "vi": "nhà hóa học Na Uy Odd Hassel"},
  {"id": "lex.en.200k.063322", "hw": "hazans", "pos": "noun", "ipa": "/ˈhɑːzənz/", "vi": "ca trưởng xướng kinh Do Thái giáo"},
  {"id": "lex.en.200k.063323", "hw": "inhs", "pos": "noun", "ipa": "/ˌaɪˌɛnˈeɪtʃɪz/", "vi": "thuốc kháng sinh đặc trị lao INH"},
  {"id": "lex.en.200k.063324", "hw": "interrupters", "pos": "noun", "ipa": "/ˌɪntəˈrʌptərz/", "vi": "bộ ngắt mạch điện; người ngắt lời"},
  {"id": "lex.en.200k.063325", "hw": "jeroboams", "pos": "noun", "ipa": "/ˌdʒɛrəˈboʊəmz/", "vi": "chai rượu sâm banh cỡ lớn (3 lít)"},
  {"id": "lex.en.200k.063326", "hw": "karakorams", "pos": "noun", "ipa": "/ˌkærəˈkɔːrəmz/", "vi": "dãy núi cao Karakoram ở châu Á"},
  {"id": "lex.en.200k.063327", "hw": "keycards", "pos": "noun", "ipa": "/ˈkiːkɑːrdz/", "vi": "thẻ từ mở khóa cửa ra vào"},
  {"id": "lex.en.200k.063328", "hw": "langtries", "pos": "noun", "ipa": "/ˈlæŋtriz/", "vi": "nữ diễn viên Anh Lillie Langtry"},
  {"id": "lex.en.200k.063329", "hw": "limousins", "pos": "noun", "ipa": "/ˈlɪməzɪnz/", "vi": "giống bò thịt Pháp; vùng Limousin"},
  {"id": "lex.en.200k.063330", "hw": "longshoremen", "pos": "noun", "ipa": "/ˈlɔːŋʃɔːrmən/", "vi": "công nhân bốc xếp hàng hóa bến cảng"},
  {"id": "lex.en.200k.063331", "hw": "lycanthropies", "pos": "noun", "ipa": "/laɪˈkænθrəpiz/", "vi": "truyền thuyết người hóa chó sói"},
  {"id": "lex.en.200k.063332", "hw": "mainsprings", "pos": "noun", "ipa": "/ˈmeɪnsprɪŋz/", "vi": "dây cót chính; động lực chủ chốt"},
  {"id": "lex.en.200k.063333", "hw": "mayoresses", "pos": "noun", "ipa": "/ˈmɛərəsɪz/", "vi": "nữ thị trưởng; phu nhân thị trưởng"},
  {"id": "lex.en.200k.063334", "hw": "mazers", "pos": "noun", "ipa": "/ˈmeɪzərz/", "vi": "chén gỗ uống rượu cổ viền bạc"},
  {"id": "lex.en.200k.063335", "hw": "metalheads", "pos": "noun", "ipa": "/ˈmɛtəlˌhɛdz/", "vi": "người hâm mộ dòng nhạc heavy metal"},
  {"id": "lex.en.200k.063336", "hw": "mincers", "pos": "noun", "ipa": "/ˈmɪnsərz/", "vi": "máy xay nhuyễn thịt; người đi ẻo lả"},
  {"id": "lex.en.200k.063337", "hw": "minges", "pos": "noun", "ipa": "/ˈmɪndʒɪz/", "vi": "vùng lông mu (tiếng lóng thô tục)"},
  {"id": "lex.en.200k.063338", "hw": "moluccases", "pos": "noun", "ipa": "/məˈlʌkəsɪz/", "vi": "quần đảo gia vị Maluku Indonesia"},
  {"id": "lex.en.200k.063339", "hw": "monetisations", "pos": "noun", "ipa": "/ˌmɑːnɪtaɪˈzeɪʃənz/", "vi": "sự kiếm tiền; tiền tệ hóa (Anh)"},
  {"id": "lex.en.200k.063340", "hw": "monopolists", "pos": "noun", "ipa": "/məˈnɑːpəlɪsts/", "vi": "người nắm giữ thế độc quyền bán"},
  {"id": "lex.en.200k.063341", "hw": "motets", "pos": "noun", "ipa": "/moʊˈtɛts/", "vi": "bản thánh ca hợp xướng đa thanh cổ"},
  {"id": "lex.en.200k.063342", "hw": "mukdens", "pos": "noun", "ipa": "/ˈmʊkdɛnz/", "vi": "thành phố Thẩm Dương (Phụng Thiên)"},
  {"id": "lex.en.200k.063343", "hw": "musials", "pos": "noun", "ipa": "/ˈmjuːziəlz/", "vi": "cầu thủ bóng chày Mỹ Stan Musial"},
  {"id": "lex.en.200k.063344", "hw": "nadps", "pos": "noun", "ipa": "/ˌɛnˌeɪˌdiːˈpiːz/", "vi": "coenzym chuyển hóa tế bào NADP"},
  {"id": "lex.en.200k.063345", "hw": "nanchangs", "pos": "noun", "ipa": "/nænˈtʃæŋz/", "vi": "thành phố Nam Xương tỉnh Giang Tây"},
  {"id": "lex.en.200k.063346", "hw": "naturopathies", "pos": "noun", "ipa": "/ˌneɪtʃəˈrɑːpəθiz/", "vi": "y học tự nhiên không dùng thuốc tây"},
  {"id": "lex.en.200k.063347", "hw": "noncompliants", "pos": "noun", "ipa": "/ˌnɑːnkəmˈplaɪənts/", "vi": "người không tuân thủ điều trị y tế"},
  {"id": "lex.en.200k.063348", "hw": "novelettes", "pos": "noun", "ipa": "/ˌnɑːvəˈlɛts/", "vi": "tiểu thuyết ngắn; tác phẩm nhạc nhẹ"},
  {"id": "lex.en.200k.063349", "hw": "olfactions", "pos": "noun", "ipa": "/ɑːlˈfækʃənz/", "vi": "chức năng ngửi mùi của khứu giác"},
  {"id": "lex.en.200k.063350", "hw": "opvs", "pos": "noun", "ipa": "/ˌoʊˌpiːˈviːz/", "vi": "vắc-xin uống phòng bại liệt OPV"},
  {"id": "lex.en.200k.063351", "hw": "ouzos", "pos": "noun", "ipa": "/ˈuːzoʊz/", "vi": "rượu mạnh mùi hồi Hy Lạp ouzo"},
  {"id": "lex.en.200k.063352", "hw": "paramedicals", "pos": "noun", "ipa": "/ˌpærəˈmɛdɪkəlz/", "vi": "nhân viên y tế cấp cứu hỗ trợ"},
  {"id": "lex.en.200k.063353", "hw": "phlebotomies", "pos": "noun", "ipa": "/flɪˈbɑːtəmiz/", "vi": "thủ thuật chích lấy máu tĩnh mạch"},
  {"id": "lex.en.200k.063354", "hw": "pianissimos", "pos": "noun", "ipa": "/ˌpiːəˈnɪsəˌmoʊz/", "vi": "cường độ nhạc cực nhỏ nhẹ êm dịu"},
  {"id": "lex.en.200k.063355", "hw": "poitous", "pos": "noun", "ipa": "/pwɑːˈtuːz/", "vi": "tỉnh lịch sử Poitou miền tây Pháp"},
  {"id": "lex.en.200k.063356", "hw": "potawatomis", "pos": "noun", "ipa": "/ˌpɑːtəˈwɑːtəmiz/", "vi": "bộ tộc bản địa Bắc Mỹ Potawatomi"},
  {"id": "lex.en.200k.063357", "hw": "pyromaniacs", "pos": "noun", "ipa": "/ˌpaɪroʊˈmeɪniˌæks/", "vi": "người mắc chứng cuồng phóng hỏa đốt"},
  {"id": "lex.en.200k.063358", "hw": "ramachandras", "pos": "noun", "ipa": "/ˌrɑːməˈtʃʌndrəz/", "vi": "vị thần hóa thân Rama Ấn Độ giáo"},
  {"id": "lex.en.200k.063359", "hw": "redbirds", "pos": "noun", "ipa": "/ˈrɛdbɜːrdz/", "vi": "chim hồng y giáo chủ lông đỏ"},
  {"id": "lex.en.200k.063360", "hw": "relaxins", "pos": "noun", "ipa": "/rɪˈlæksɪnz/", "vi": "hoóc môn thai kỳ giãn khớp chậu"},
  {"id": "lex.en.200k.063361", "hw": "ribeses", "pos": "noun", "ipa": "/ˈraɪbiːzɪz/", "vi": "chi cây quả lý chua và phúc bồn tử"},
  {"id": "lex.en.200k.063362", "hw": "roadhogs", "pos": "noun", "ipa": "/ˈroʊdhɔːɡz/", "vi": "kẻ lái xe ích kỷ lấn làn cản đường"},
  {"id": "lex.en.200k.063363", "hw": "rogets", "pos": "noun", "ipa": "/rəˈʒeɪz/", "vi": "tác giả từ điển đồng nghĩa Roget"},
  {"id": "lex.en.200k.063364", "hw": "rosicrucians", "pos": "noun", "ipa": "/ˌroʊzəˈkruːʃənz/", "vi": "hội viên hội kín Thập Tự Hoa Hồng"},
  {"id": "lex.en.200k.063365", "hw": "rubels", "pos": "noun", "ipa": "/ˈruːbəlz/", "vi": "đồng tiền rúp Belarus hoặc Nga"},
  {"id": "lex.en.200k.063366", "hw": "saamis", "pos": "noun", "ipa": "/ˈsɑːmiz/", "vi": "người bản địa Sami vùng Bắc Âu"},
  {"id": "lex.en.200k.063367", "hw": "saktis", "pos": "noun", "ipa": "/ˈʃʌktiz/", "vi": "nữ thần sức mạnh vũ trụ Shakti"},
  {"id": "lex.en.200k.063368", "hw": "sarasvatis", "pos": "noun", "ipa": "/ˌsærəˈsvɑːtiz/", "vi": "nữ thần tri thức âm nhạc Sarasvati"},
  {"id": "lex.en.200k.063369", "hw": "sarnoffs", "pos": "noun", "ipa": "/ˈsɑːrnɔːfs/", "vi": "nhà tiên phong truyền hình Sarnoff"},
  {"id": "lex.en.200k.063370", "hw": "schmoozed", "pos": "verb", "ipa": "/ʃmuːzd/", "vi": "đã tán gẫu thân mật tạo quan hệ"},
  {"id": "lex.en.200k.063371", "hw": "schmoozes", "pos": "noun", "ipa": "/ˈʃmuːzɪz/", "vi": "cuộc tán gẫu xã giao thân mật"},
  {"id": "lex.en.200k.063372", "hw": "schmoozing", "pos": "verb", "ipa": "/ˈʃmuːzɪŋ/", "vi": "đang tán gẫu xã giao thân thiện"},
  {"id": "lex.en.200k.063373", "hw": "schrodingers", "pos": "noun", "ipa": "/ˈʃroʊdɪŋərz/", "vi": "nhà vật lý lượng tử Schrödinger"},
  {"id": "lex.en.200k.063374", "hw": "sepulchers", "pos": "noun", "ipa": "/ˈsɛpəlkərz/", "vi": "lăng mộ đá chôn cất người chết"},
  {"id": "lex.en.200k.063375", "hw": "shogis", "pos": "noun", "ipa": "/ˈʃoʊɡiz/", "vi": "trò chơi cờ tướng truyền thống Nhật"},
  {"id": "lex.en.200k.063376", "hw": "showplaces", "pos": "noun", "ipa": "/ˈʃoʊpleɪsɪz/", "vi": "nơi trưng bày đẹp; thắng cảnh nổi"},
  {"id": "lex.en.200k.063377", "hw": "shuttlecocked", "pos": "verb", "ipa": "/ˈʃʌtəlˌkɑːkt/", "vi": "đã đẩy qua đẩy lại như cầu lông"},
  {"id": "lex.en.200k.063378", "hw": "shuttlecocking", "pos": "verb", "ipa": "/ˈʃʌtəlˌkɑːkɪŋ/", "vi": "đang đẩy qua lại như quả cầu"},
  {"id": "lex.en.200k.063379", "hw": "sidetracked", "pos": "verb", "ipa": "/ˈsaɪdtrækt/", "vi": "đã làm lạc hướng; bị phân tâm"},
  {"id": "lex.en.200k.063380", "hw": "sidetracking", "pos": "verb", "ipa": "/ˈsaɪdtrækɪŋ/", "vi": "đang đánh lạc hướng sang việc khác"},
  {"id": "lex.en.200k.063381", "hw": "sidetracks", "pos": "noun", "ipa": "/ˈsaɪdtræks/", "vi": "đường ray tránh tàu; nhánh phụ"},
  {"id": "lex.en.200k.063382", "hw": "sintering", "pos": "verb", "ipa": "/ˈsɪntərɪŋ/", "vi": "đang thiêu kết bột kim loại gốm"},
  {"id": "lex.en.200k.063383", "hw": "sinters", "pos": "verb", "ipa": "/ˈsɪntərz/", "vi": "nung thiêu kết kết dính hạt bột"},
  {"id": "lex.en.200k.063384", "hw": "sleepyheads", "pos": "noun", "ipa": "/ˈsliːpihɛdz/", "vi": "người hay buồn ngủ mê ngủ dậy muộn"},
  {"id": "lex.en.200k.063385", "hw": "spearfishes", "pos": "noun", "ipa": "/ˈspɪərfɪʃɪz/", "vi": "cá mỏ kiếm biển sâu cùng họ cá cờ"},
  {"id": "lex.en.200k.063386", "hw": "stragglers", "pos": "noun", "ipa": "/ˈstræɡlərz/", "vi": "người đi tụt lại sau hàng ngũ"},
  {"id": "lex.en.200k.063387", "hw": "tamponades", "pos": "noun", "ipa": "/ˌtæmpəˈneɪdz/", "vi": "chứng chèn ép tim; nút gạc cầm máu"},
  {"id": "lex.en.200k.063388", "hw": "thatcherisms", "pos": "noun", "ipa": "/ˈθætʃəˌrɪzəmz/", "vi": "chính sách kinh tế tự do Thatcher"},
  {"id": "lex.en.200k.063389", "hw": "thermographies", "pos": "noun", "ipa": "/θɜːrˈmɑːɡrəfiz/", "vi": "kỹ thuật chụp ảnh nhiệt hồng ngoại"},
  {"id": "lex.en.200k.063390", "hw": "tholes", "pos": "noun", "ipa": "/θoʊlz/", "vi": "chốt giữ mái chèo trên mạn thuyền"},
  {"id": "lex.en.200k.063391", "hw": "thromboembolisms", "pos": "noun", "ipa": "/ˌθrɑːmboʊˈɛmbəˌlɪzəmz/", "vi": "tắc mạch máu do cục máu đông trôi"},
  {"id": "lex.en.200k.063392", "hw": "tius", "pos": "noun", "ipa": "/ˈtiːuːz/", "vi": "thần chiến tranh Đức cổ Tiu (Tyr)"},
  {"id": "lex.en.200k.063393", "hw": "tossups", "pos": "noun", "ipa": "/ˈtɔːsʌpz/", "vi": "cuộc đấu ngang tài khó đoán"},
  {"id": "lex.en.200k.063394", "hw": "touchbacks", "pos": "noun", "ipa": "/ˈtʌtʃbæks/", "vi": "pha bóng dừng khu vực cuối sân Mỹ"},
  {"id": "lex.en.200k.063395", "hw": "tswanas", "pos": "noun", "ipa": "/ˈtswɑːnəz/", "vi": "người dân và tiếng Tswana châu Phi"},
  {"id": "lex.en.200k.063396", "hw": "underbodies", "pos": "noun", "ipa": "/ˈʌndərˌbɑːdiz/", "vi": "gầm dưới xe cộ; phần bụng dưới"},
  {"id": "lex.en.200k.063397", "hw": "vanzettis", "pos": "noun", "ipa": "/vænˈzɛtiz/", "vi": "nhân vật vụ án Sacco và Vanzetti"},
  {"id": "lex.en.200k.063398", "hw": "verticalities", "pos": "noun", "ipa": "/ˌvɜːrtɪˈkælɪtiz/", "vi": "tính thẳng đứng theo chiều dọc"},
  {"id": "lex.en.200k.063399", "hw": "villons", "pos": "noun", "ipa": "/viˈjɔːnz/", "vi": "nhà thơ Pháp thời trung cổ Villon"},
  {"id": "lex.en.200k.063400", "hw": "viscountesses", "pos": "noun", "ipa": "/ˈvaɪkaʊntəsɪz/", "vi": "nữ tử tước; phu nhân của tử tước"},
  {"id": "lex.en.200k.063401", "hw": "wesers", "pos": "noun", "ipa": "/ˈveɪzərz/", "vi": "sông Weser ở miền bắc nước Đức"},
  {"id": "lex.en.200k.063402", "hw": "yobs", "pos": "noun", "ipa": "/jɑːbz/", "vi": "thanh niên du côn thô lỗ quậy phá"}
]

with open('scratch/b33_r07_raw_p4.json') as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100

for i, (item, r) in enumerate(zip(items, raw)):
    assert item['id'] == r['id'], f"Mismatch id at {i}: {item['id']} vs {r['id']}"
    assert item['hw'] == r['hw'], f"Mismatch hw at {i}: {item['hw']} vs {r['hw']}"
    assert len(item['vi']) <= 35, f"vi length > 35 at {i} ({item['hw']}): {len(item['vi'])}"
    assert item['pos'] in ['noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'], f"Invalid pos at {i}: {item['pos']}"
    assert item['ipa'].startswith('/') and item['ipa'].endswith('/') and item['ipa'].count('/') == 2, f"Invalid ipa at {i}: {item['ipa']}"
    assert not item['ipa'][1:-1].startswith(' ') and not item['ipa'][1:-1].endswith(' '), f"Space in ipa at {i}: {item['ipa']}"
    r['pos'] = item['pos']
    r['ipa'] = item['ipa']
    r['vi'] = item['vi']
    r['status'] = 'reviewed'

with open('scratch/b33_r07_p4.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)
print("Saved scratch/b33_r07_p4.json OK")
