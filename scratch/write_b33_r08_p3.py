import json

items = [
  {"id": "lex.en.200k.063703", "hw": "estheticians", "pos": "noun", "ipa": "/ˌɛsθəˈtɪʃənz/", "vi": "chuyên viên chăm sóc thẩm mỹ da"},
  {"id": "lex.en.200k.063704", "hw": "eucalypts", "pos": "noun", "ipa": "/ˈjuːkəlɪpts/", "vi": "cây bạch đàn tinh dầu thơm Úc"},
  {"id": "lex.en.200k.063705", "hw": "evolutionists", "pos": "noun", "ipa": "/ˌɛvəˈluːʃənɪsts/", "vi": "người theo học thuyết tiến hóa"},
  {"id": "lex.en.200k.063706", "hw": "externs", "pos": "noun", "ipa": "/ˈɛkstɜːrnz/", "vi": "sinh viên y thực tập ngoại trú"},
  {"id": "lex.en.200k.063707", "hw": "fafnirs", "pos": "noun", "ipa": "/ˈfɑːvnɪrz/", "vi": "rồng giữ kho báu Fafnir thần thoại"},
  {"id": "lex.en.200k.063708", "hw": "fincens", "pos": "noun", "ipa": "/ˈfɪnsɛnz/", "vi": "Mạng lưới Chống Tội phạm Tài chính"},
  {"id": "lex.en.200k.063709", "hw": "fnmas", "pos": "noun", "ipa": "/ˌɛfˌɛnˌɛmˈeɪz/", "vi": "hiệp hội thế chấp Mỹ Fannie Mae"},
  {"id": "lex.en.200k.063710", "hw": "frogmen", "pos": "noun", "ipa": "/ˈfrɑːɡmən/", "vi": "thợ lặn người nhái đặc công biển"},
  {"id": "lex.en.200k.063711", "hw": "girondes", "pos": "noun", "ipa": "/ʒɪˈrɔːndz/", "vi": "phái ôn hòa Girondin Cách mạng Pháp"},
  {"id": "lex.en.200k.063712", "hw": "haggais", "pos": "noun", "ipa": "/ˈhæɡaɪz/", "vi": "nhà tiên tri và sách Ha-gai"},
  {"id": "lex.en.200k.063713", "hw": "hinaults", "pos": "noun", "ipa": "/iˈnoʊz/", "vi": "cua-rơ huyền thoại Bernard Hinault"},
  {"id": "lex.en.200k.063714", "hw": "hogmanays", "pos": "noun", "ipa": "/ˌhɑːɡməˈneɪz/", "vi": "lễ đêm giao thừa ở Scotland"},
  {"id": "lex.en.200k.063715", "hw": "homesteaders", "pos": "noun", "ipa": "/ˈhoʊmstɛdərz/", "vi": "người đi khai hoang lập trang trại"},
  {"id": "lex.en.200k.063716", "hw": "imbroglios", "pos": "noun", "ipa": "/ɪmˈbroʊlioʊz/", "vi": "tình huống rắc rối rối ren khó xử"},
  {"id": "lex.en.200k.063717", "hw": "jemmied", "pos": "verb", "ipa": "/ˈdʒɛmid/", "vi": "đã cạy khóa cửa bằng xà beng nhỏ"},
  {"id": "lex.en.200k.063718", "hw": "jemmies", "pos": "noun", "ipa": "/ˈdʒɛmiz/", "vi": "xà beng nhỏ dùng cạy khóa; mở khóa"},
  {"id": "lex.en.200k.063719", "hw": "jitneys", "pos": "noun", "ipa": "/ˈdʒɪtniz/", "vi": "xe buýt nhỏ chở khách giá rẻ"},
  {"id": "lex.en.200k.063720", "hw": "kansans", "pos": "noun", "ipa": "/ˈkænzənz/", "vi": "người dân sinh sống bang Kansas Mỹ"},
  {"id": "lex.en.200k.063721", "hw": "kauris", "pos": "noun", "ipa": "/ˈkaʊriz/", "vi": "cây thông kauri cổ thụ và nhựa thơm"},
  {"id": "lex.en.200k.063722", "hw": "keisters", "pos": "noun", "ipa": "/ˈkiːstərz/", "vi": "mông đít (tiếng lóng); vali đồ nghề"},
  {"id": "lex.en.200k.063723", "hw": "kelpies", "pos": "noun", "ipa": "/ˈkɛlpiz/", "vi": "chó chăn gia súc Úc; thủy quái ngựa"},
  {"id": "lex.en.200k.063724", "hw": "keratosises", "pos": "noun", "ipa": "/ˌkɛrəˈtoʊsɪsɪz/", "vi": "chứng dày sừng tăng sản biểu bì da"},
  {"id": "lex.en.200k.063725", "hw": "kosciuszkos", "pos": "noun", "ipa": "/ˌkɑːʃiˈʊʃkoʊz/", "vi": "anh hùng dân tộc Ba Lan Kościuszko"},
  {"id": "lex.en.200k.063726", "hw": "kritis", "pos": "noun", "ipa": "/ˈkriːtiz/", "vi": "hòn đảo Crete cổ kính của Hy Lạp"},
  {"id": "lex.en.200k.063727", "hw": "kyds", "pos": "noun", "ipa": "/kɪdz/", "vi": "nhà viết kịch Anh Thomas Kyd"},
  {"id": "lex.en.200k.063728", "hw": "lapwings", "pos": "noun", "ipa": "/ˈlæpwɪŋz/", "vi": "chim te te mào đồng cỏ châu Âu"},
  {"id": "lex.en.200k.063729", "hw": "latiums", "pos": "noun", "ipa": "/ˈleɪʃiəmz/", "vi": "vùng cổ Latium quanh thành Rome Ý"},
  {"id": "lex.en.200k.063730", "hw": "lightships", "pos": "noun", "ipa": "/ˈlaɪtʃɪps/", "vi": "tàu neo cố định làm hải đăng biển"},
  {"id": "lex.en.200k.063731", "hw": "lumpectomies", "pos": "noun", "ipa": "/lʌmˈpɛktəmiz/", "vi": "phẫu thuật cắt bỏ khối u bảo tồn"},
  {"id": "lex.en.200k.063732", "hw": "magnesites", "pos": "noun", "ipa": "/ˈmæɡnəsaɪts/", "vi": "quặng khoáng vật magie cacbonat"},
  {"id": "lex.en.200k.063733", "hw": "mantells", "pos": "noun", "ipa": "/ˈmæntəlz/", "vi": "nhà địa chất Anh Gideon Mantell"},
  {"id": "lex.en.200k.063734", "hw": "marinelands", "pos": "noun", "ipa": "/məˈriːnlændz/", "vi": "công viên thủy cung đại dương"},
  {"id": "lex.en.200k.063735", "hw": "melters", "pos": "noun", "ipa": "/ˈmɛltərz/", "vi": "thợ nấu chảy kim loại; nồi nung"},
  {"id": "lex.en.200k.063736", "hw": "nevi", "pos": "noun", "ipa": "/ˈniːvaɪ/", "vi": "các nốt ruồi sắc tố bớt trên da"},
  {"id": "lex.en.200k.063737", "hw": "nonesuches", "pos": "noun", "ipa": "/ˈnʌnsʌtʃɪz/", "vi": "người hay vật tuyệt vời vô song"},
  {"id": "lex.en.200k.063738", "hw": "ockhams", "pos": "noun", "ipa": "/ˈɑːkəmz/", "vi": "triết gia Anh William of Ockham"},
  {"id": "lex.en.200k.063739", "hw": "oversleeping", "pos": "verb", "ipa": "/ˌoʊvərˈsliːpɪŋ/", "vi": "đang ngủ quên lố giờ thức dậy"},
  {"id": "lex.en.200k.063740", "hw": "oversleeps", "pos": "verb", "ipa": "/ˌoʊvərˈsliːps/", "vi": "ngủ quên dậy muộn quá giờ quy định"},
  {"id": "lex.en.200k.063741", "hw": "pallones", "pos": "noun", "ipa": "/pɑːˈloʊneɪz/", "vi": "môn bóng đấm tay Ý cổ truyền"},
  {"id": "lex.en.200k.063742", "hw": "pawls", "pos": "noun", "ipa": "/pɔːlz/", "vi": "cái chốt hãm bánh răng một chiều"},
  {"id": "lex.en.200k.063743", "hw": "phantasmagorias", "pos": "noun", "ipa": "/fænˌtæzməˈɡɔːriəz/", "vi": "cảnh tượng ảo ảnh ma mị biến đổi"},
  {"id": "lex.en.200k.063744", "hw": "pilotages", "pos": "noun", "ipa": "/ˈpaɪlətɪdʒɪz/", "vi": "nghề hoa tiêu dẫn tàu ra vào cảng"},
  {"id": "lex.en.200k.063745", "hw": "pinyons", "pos": "noun", "ipa": "/ˈpɪnjənz/", "vi": "cây thông lùn tây Mỹ lấy hạt ăn"},
  {"id": "lex.en.200k.063746", "hw": "potentates", "pos": "noun", "ipa": "/ˈpoʊtənˌteɪts/", "vi": "vua chúa tối cao; nhà cầm quyền"},
  {"id": "lex.en.200k.063747", "hw": "presentments", "pos": "noun", "ipa": "/prɪˈzɛntmənts/", "vi": "bản kiến nghị truy tố; sự trình bày"},
  {"id": "lex.en.200k.063748", "hw": "pterosaurs", "pos": "noun", "ipa": "/ˈtɛrəsɔːrz/", "vi": "bò sát bay tiền sử thời khủng long"},
  {"id": "lex.en.200k.063749", "hw": "quadrates", "pos": "noun", "ipa": "/ˈkwɑːdrɪts/", "vi": "hình vuông; xương vuông khớp hàm sọ"},
  {"id": "lex.en.200k.063750", "hw": "ramifications", "pos": "noun", "ipa": "/ˌræməfəˈkeɪʃənz/", "vi": "hệ quả kéo theo; sự chia nhánh"},
  {"id": "lex.en.200k.063751", "hw": "rochambeaus", "pos": "noun", "ipa": "/ˌrɑːʃəmˈboʊz/", "vi": "tướng Rochambeau; trò oẳn tù tì"},
  {"id": "lex.en.200k.063752", "hw": "rousers", "pos": "noun", "ipa": "/ˈraʊzərz/", "vi": "người khuấy động; lời diễn văn sôi"},
  {"id": "lex.en.200k.063753", "hw": "sculpins", "pos": "noun", "ipa": "/ˈskʌlpɪnz/", "vi": "cá đầu bẹt gai vây vùng biển lạnh"},
  {"id": "lex.en.200k.063754", "hw": "scythias", "pos": "noun", "ipa": "/ˈsɪθiəz/", "vi": "vùng thảo nguyên cổ Scythia Âu-Á"},
  {"id": "lex.en.200k.063755", "hw": "seismographs", "pos": "noun", "ipa": "/ˈsaɪzməˌɡræfs/", "vi": "máy địa chấn kế ghi rung động đất"},
  {"id": "lex.en.200k.063756", "hw": "snoots", "pos": "noun", "ipa": "/snuːts/", "vi": "kẻ hợm hĩnh khinh người; mũi mõm"},
  {"id": "lex.en.200k.063757", "hw": "soffits", "pos": "noun", "ipa": "/ˈsɑːfɪts/", "vi": "mặt dưới vòm trần hay mái đua nhà"},
  {"id": "lex.en.200k.063758", "hw": "souvlakis", "pos": "noun", "ipa": "/suːˈvlɑːkiz/", "vi": "món thịt xiên nướng kiểu Hy Lạp"},
  {"id": "lex.en.200k.063759", "hw": "stainers", "pos": "noun", "ipa": "/ˈsteɪnərz/", "vi": "thợ nhuộm vải gỗ; chất làm ố màu"},
  {"id": "lex.en.200k.063760", "hw": "supergiants", "pos": "noun", "ipa": "/ˈsuːpərˌdʒaɪənts/", "vi": "ngôi sao siêu khổng lồ sáng chói"},
  {"id": "lex.en.200k.063761", "hw": "swattered", "pos": "verb", "ipa": "/ˈswɑːtərd/", "vi": "đã vỗ nước bì bõm (vịt ngan)"},
  {"id": "lex.en.200k.063762", "hw": "swattering", "pos": "verb", "ipa": "/ˈswɑːtərɪŋ/", "vi": "đang vẫy vùng bì bõm trên mặt nước"},
  {"id": "lex.en.200k.063763", "hw": "swatters", "pos": "noun", "ipa": "/ˈswɑːtərz/", "vi": "cái vỉ đập ruồi muỗi; người đập"},
  {"id": "lex.en.200k.063764", "hw": "tanakhs", "pos": "noun", "ipa": "/tɑːˈnɑːxs/", "vi": "bộ Kinh Thánh tiếng Do Thái Tanakh"},
  {"id": "lex.en.200k.063765", "hw": "torquemadas", "pos": "noun", "ipa": "/ˌtɔːrkəˈmɑːdəz/", "vi": "trưởng tòa dị giáo Tây Ban Nha"},
  {"id": "lex.en.200k.063766", "hw": "transaminases", "pos": "noun", "ipa": "/trænsˈæməˌneɪsɪz/", "vi": "enzym chuyển nhóm amin men gan"},
  {"id": "lex.en.200k.063767", "hw": "tricksier", "pos": "adj", "ipa": "/ˈtrɪksiər/", "vi": "tinh quái lắt léo gian xảo hơn"},
  {"id": "lex.en.200k.063768", "hw": "tricksiest", "pos": "adj", "ipa": "/ˈtrɪksiɪst/", "vi": "tinh quái lắt léo gian xảo nhất"},
  {"id": "lex.en.200k.063769", "hw": "tsarinas", "pos": "noun", "ipa": "/zɑːˈriːnəz/", "vi": "nữ hoàng Nga; phu nhân sa hoàng"},
  {"id": "lex.en.200k.063770", "hw": "unitarianisms", "pos": "noun", "ipa": "/ˌjuːnɪˈtɛriəˌnɪzəmz/", "vi": "thuyết nhất vị phủ nhận Ba Ngôi"},
  {"id": "lex.en.200k.063771", "hw": "vacuoles", "pos": "noun", "ipa": "/ˈvækjuˌoʊlz/", "vi": "bào quan không bào trong tế bào"},
  {"id": "lex.en.200k.063772", "hw": "vareses", "pos": "noun", "ipa": "/vəˈrɛzɪz/", "vi": "nhà soạn nhạc Mỹ gốc Pháp Varèse"},
  {"id": "lex.en.200k.063773", "hw": "victrolas", "pos": "noun", "ipa": "/vɪkˈtroʊləz/", "vi": "máy quay đĩa hát cổ hiệu Victrola"},
  {"id": "lex.en.200k.063774", "hw": "vldls", "pos": "noun", "ipa": "/ˌviːˌɛlˌdiːˈɛlz/", "vi": "lipoprotein mỡ xấu tỷ trọng thấp"},
  {"id": "lex.en.200k.063775", "hw": "watteaus", "pos": "noun", "ipa": "/wɑːˈtoʊz/", "vi": "danh họa Rococo Pháp Watteau"},
  {"id": "lex.en.200k.063776", "hw": "whiteners", "pos": "noun", "ipa": "/ˈwaɪtnərz/", "vi": "chất tẩy trắng; bột kem pha cà phê"},
  {"id": "lex.en.200k.063777", "hw": "womanisers", "pos": "noun", "ipa": "/ˈwʊməˌnaɪzərz/", "vi": "đàn ông trăng hoa lăng nhăng (Anh)"},
  {"id": "lex.en.200k.063778", "hw": "woodcarvings", "pos": "noun", "ipa": "/ˈwʊdˌkɑːrvɪŋz/", "vi": "tác phẩm nghệ thuật điêu khắc gỗ"},
  {"id": "lex.en.200k.063779", "hw": "yeastier", "pos": "adj", "ipa": "/ˈjiːstiər/", "vi": "nhiều bọt men hơn; sôi nổi hơn"},
  {"id": "lex.en.200k.063780", "hw": "yeastiest", "pos": "adj", "ipa": "/ˈjiːstiɪst/", "vi": "nhiều bọt men nhất; hăng hái nhất"},
  {"id": "lex.en.200k.063781", "hw": "acanthus mollis", "pos": "phrase", "ipa": "/əˈkænθəs ˈmɑːlɪs/", "vi": "cây ô rô mềm lá to hoa trắng tím"},
  {"id": "lex.en.200k.063782", "hw": "achille ratti", "pos": "phrase", "ipa": "/ɑːˈkiːl ˈrɑːti/", "vi": "Giáo hoàng Piô XI Achille Ratti"},
  {"id": "lex.en.200k.063783", "hw": "aldol reaction", "pos": "phrase", "ipa": "/ˈældɔːl riˈækʃən/", "vi": "phản ứng ngưng tụ aldol hữu cơ"},
  {"id": "lex.en.200k.063784", "hw": "alexander alexandrovich blok", "pos": "phrase", "ipa": "/ˌælɪɡˈzændər blɑːk/", "vi": "nhà thơ Nga Aleksandr Blok"},
  {"id": "lex.en.200k.063785", "hw": "ambulant plague", "pos": "phrase", "ipa": "/ˈæmbjʊlənt pleɪɡ/", "vi": "bệnh dịch hạch thể nhẹ đi lại được"},
  {"id": "lex.en.200k.063786", "hw": "american widgeon", "pos": "phrase", "ipa": "/əˈmɛrɪkən ˈwɪdʒən/", "vi": "vịt trời đầu vằn trắng Bắc Mỹ"},
  {"id": "lex.en.200k.063787", "hw": "antidiabetic drug", "pos": "phrase", "ipa": "/ˌæntidaɪəˈbɛtɪk drʌɡ/", "vi": "thuốc điều trị bệnh tiểu đường"},
  {"id": "lex.en.200k.063788", "hw": "arnold schonberg", "pos": "phrase", "ipa": "/ˈɑːrnəld ˈʃɜːrnbɛrɡ/", "vi": "nhà soạn nhạc Áo Arnold Schoenberg"},
  {"id": "lex.en.200k.063789", "hw": "baron verulam", "pos": "phrase", "ipa": "/ˈbærən ˈvɛrələm/", "vi": "triết gia Anh Francis Bacon"},
  {"id": "lex.en.200k.063790", "hw": "bougainvillea glabra", "pos": "phrase", "ipa": "/ˌbuːɡənˈvɪliə ˈɡleɪbrə/", "vi": "cây hoa giấy cảnh leo giàn sặc sỡ"},
  {"id": "lex.en.200k.063791", "hw": "brandy snifter", "pos": "phrase", "ipa": "/ˈbrændi ˈsnɪftər/", "vi": "ly bầu tròn ngắn uống rượu brandy"},
  {"id": "lex.en.200k.063792", "hw": "bufo viridis", "pos": "phrase", "ipa": "/ˈbjuːfoʊ ˈvɪrɪdɪs/", "vi": "cóc đốm xanh lục vùng châu Âu"},
  {"id": "lex.en.200k.063793", "hw": "canticle of canticles", "pos": "phrase", "ipa": "/ˈkæntɪkəl əv ˈkæntɪkəlz/", "vi": "sách Nhã Ca (Diễm Ca) Kinh Thánh"},
  {"id": "lex.en.200k.063794", "hw": "cinchona officinalis", "pos": "phrase", "ipa": "/sɪŋˈkoʊnə əˌfɪsəˈneɪlɪs/", "vi": "cây canh-ki-na lấy vỏ làm ký ninh"},
  {"id": "lex.en.200k.063795", "hw": "dame alicia markova", "pos": "phrase", "ipa": "/deɪm əˈliːʃə mɑːrˈkoʊvə/", "vi": "nghệ sĩ ba lê Anh Alicia Markova"},
  {"id": "lex.en.200k.063796", "hw": "darius milhaud", "pos": "phrase", "ipa": "/dɑːˈrjuːs miˈjoʊ/", "vi": "nhà soạn nhạc Pháp Darius Milhaud"},
  {"id": "lex.en.200k.063797", "hw": "decimal numeration system", "pos": "phrase", "ipa": "/ˈdɛsəməl ˌnuːməˈreɪʃən ˈsɪstəm/", "vi": "hệ đếm thập phân cơ số mười"},
  {"id": "lex.en.200k.063798", "hw": "elias canetti", "pos": "phrase", "ipa": "/ɪˈlaɪəs kəˈnɛti/", "vi": "nhà văn giải Nobel Elias Canetti"},
  {"id": "lex.en.200k.063799", "hw": "epicyclic gear", "pos": "phrase", "ipa": "/ˌɛpɪˈsaɪklɪk ɡɪər/", "vi": "bánh răng hành tinh truyền động"},
  {"id": "lex.en.200k.063800", "hw": "epicyclic gear train", "pos": "phrase", "ipa": "/ˌɛpɪˈsaɪklɪk ɡɪər treɪn/", "vi": "hệ truyền động bánh răng hành tinh"},
  {"id": "lex.en.200k.063801", "hw": "epicyclic train", "pos": "phrase", "ipa": "/ˌɛpɪˈsaɪklɪk treɪn/", "vi": "hộp số bánh răng hành tinh"},
  {"id": "lex.en.200k.063802", "hw": "evangelista torricelli", "pos": "phrase", "ipa": "/eɪvɑːndʒeɪˈliːstə ˌtɔːriˈtʃɛli/", "vi": "nhà vật lý Ý phát minh khí áp kế"}
]

with open('scratch/b33_r08_raw_p3.json') as f:
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

with open('scratch/b33_r08_p3.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)
print("Saved scratch/b33_r08_p3.json OK")
