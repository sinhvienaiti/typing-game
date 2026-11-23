import json

items = [
  {"id": "lex.en.200k.065303", "hw": "defenestrations", "pos": "noun", "ipa": "/diːˌfɛnəˈstreɪʃənz/", "vi": "hành vi ném người ra ngoài cửa sổ"},
  {"id": "lex.en.200k.065304", "hw": "disavowals", "pos": "noun", "ipa": "/ˌdɪsəˈvaʊəlz/", "vi": "sự phủ nhận chối bỏ trách nhiệm"},
  {"id": "lex.en.200k.065305", "hw": "dolmens", "pos": "noun", "ipa": "/ˈdɑːlmɛnz/", "vi": "cổng mộ đá cự thạch thời tiền sử"},
  {"id": "lex.en.200k.065306", "hw": "dotards", "pos": "noun", "ipa": "/ˈdoʊtərdz/", "vi": "người già lẩm cẩm suy giảm trí tuệ"},
  {"id": "lex.en.200k.065307", "hw": "estrones", "pos": "noun", "ipa": "/ˈɛstroʊnz/", "vi": "hoóc môn nội tiết tố nữ estrone"},
  {"id": "lex.en.200k.065308", "hw": "fantails", "pos": "noun", "ipa": "/ˈfænteɪlz/", "vi": "chim đuôi quạt; boong đuôi tàu rộng"},
  {"id": "lex.en.200k.065309", "hw": "flatterers", "pos": "noun", "ipa": "/ˈflætərərz/", "vi": "kẻ nịnh bợ xu nịnh lấy lòng người"},
  {"id": "lex.en.200k.065310", "hw": "fluoroses", "pos": "noun", "ipa": "/flʊˈroʊsiːz/", "vi": "bệnh nhiễm độc fluor răng và xương"},
  {"id": "lex.en.200k.065311", "hw": "fusillades", "pos": "noun", "ipa": "/ˌfjuːzəˈleɪdz/", "vi": "loạt đạn bắn liên thanh; tràng pháo"},
  {"id": "lex.en.200k.065312", "hw": "gangers", "pos": "noun", "ipa": "/ˈɡæŋərz/", "vi": "đốc công phụ trách tổ đội thợ đường"},
  {"id": "lex.en.200k.065313", "hw": "gauds", "pos": "noun", "ipa": "/ɡɔːdz/", "vi": "đồ trang sức hào nhoáng rẻ tiền"},
  {"id": "lex.en.200k.065314", "hw": "godunovs", "pos": "noun", "ipa": "/ɡɔːdʊˈnɔːfs/", "vi": "sa hoàng Nga Boris Godunov"},
  {"id": "lex.en.200k.065315", "hw": "goethalses", "pos": "noun", "ipa": "/ˈɡoʊθəlzɪz/", "vi": "kỹ sư trưởng kênh Panama Goethals"},
  {"id": "lex.en.200k.065316", "hw": "gordimers", "pos": "noun", "ipa": "/ˈɡɔːrdəmɪrz/", "vi": "nữ nhà văn Nobel Nam Phi Gordimer"},
  {"id": "lex.en.200k.065317", "hw": "halluces", "pos": "noun", "ipa": "/ˈhæləsiːz/", "vi": "các ngón chân cái (giải phẫu học)"},
  {"id": "lex.en.200k.065318", "hw": "halluxes", "pos": "noun", "ipa": "/ˈhæləksɪz/", "vi": "ngón chân cái (thuật ngữ giải phẫu)"},
  {"id": "lex.en.200k.065319", "hw": "hotboxes", "pos": "noun", "ipa": "/ˈhɑːtbɑːksɪz/", "vi": "ổ trục tàu quá nhiệt; bẫy hai chốt"},
  {"id": "lex.en.200k.065320", "hw": "housemasters", "pos": "noun", "ipa": "/ˈhaʊsmæstərz/", "vi": "thầy giám thị quản lý khu nội trú"},
  {"id": "lex.en.200k.065321", "hw": "hubcaps", "pos": "noun", "ipa": "/ˈhʌbkæps/", "vi": "nắp chụp trang trí tâm bánh xe hơi"},
  {"id": "lex.en.200k.065322", "hw": "hydroids", "pos": "noun", "ipa": "/ˈhaɪdrɔɪdz/", "vi": "loài thủy tức nhỏ sống ở biển"},
  {"id": "lex.en.200k.065323", "hw": "intensions", "pos": "noun", "ipa": "/ɪnˈtɛnʃənz/", "vi": "nội hàm khái niệm logic; độ căng"},
  {"id": "lex.en.200k.065324", "hw": "itraconazoles", "pos": "noun", "ipa": "/ˌɪtrəˈkɑːnəˌzoʊlz/", "vi": "thuốc kháng nấm mạnh itraconazole"},
  {"id": "lex.en.200k.065325", "hw": "japes", "pos": "noun", "ipa": "/dʒeɪps/", "vi": "trò đùa châm biếm; lời nói giễu cợt"},
  {"id": "lex.en.200k.065326", "hw": "jujubes", "pos": "noun", "ipa": "/ˈdʒuːdʒuːbz/", "vi": "quả táo tàu; kẹo dẻo trái cây mềm"},
  {"id": "lex.en.200k.065327", "hw": "kalinins", "pos": "noun", "ipa": "/kəˈliːnɪnz/", "vi": "chủ tịch Xô Viết Mikhail Kalinin"},
  {"id": "lex.en.200k.065328", "hw": "kraits", "pos": "noun", "ipa": "/kraɪts/", "vi": "rắn cạp nong cực độc ở châu Á"},
  {"id": "lex.en.200k.065329", "hw": "latticeworks", "pos": "noun", "ipa": "/ˈlætɪswɜːrks/", "vi": "giàn lưới mắt cáo bằng gỗ hay sắt"},
  {"id": "lex.en.200k.065330", "hw": "lodgements", "pos": "noun", "ipa": "/ˈlɑːdʒmənts/", "vi": "chỗ tạm trú; sự đọng lại; đơn nộp"},
  {"id": "lex.en.200k.065331", "hw": "lycees", "pos": "noun", "ipa": "/liːˈseɪz/", "vi": "trường trung học công lập ở Pháp"},
  {"id": "lex.en.200k.065332", "hw": "massasoits", "pos": "noun", "ipa": "/ˈmæsəˌsɔɪts/", "vi": "tù trưởng bản địa Mỹ Massasoit"},
  {"id": "lex.en.200k.065333", "hw": "mazier", "pos": "adj", "ipa": "/ˈmeɪziər/", "vi": "ngoằn ngoèo rối rắm khó hiểu hơn"},
  {"id": "lex.en.200k.065334", "hw": "maziest", "pos": "adj", "ipa": "/ˈmeɪziɪst/", "vi": "ngoằn ngoèo mê cung rắc rối nhất"},
  {"id": "lex.en.200k.065335", "hw": "memels", "pos": "noun", "ipa": "/ˈmeɪməlz/", "vi": "cảng Klaipėda Litva (tên cũ Memel)"},
  {"id": "lex.en.200k.065336", "hw": "menningers", "pos": "noun", "ipa": "/ˈmɛnɪŋərz/", "vi": "bác sĩ tâm thần Mỹ Karl Menninger"},
  {"id": "lex.en.200k.065337", "hw": "meqs", "pos": "noun", "ipa": "/ˌɛmˌiːˈkjuːz/", "vi": "đơn vị mili đương lượng hóa (mEq)"},
  {"id": "lex.en.200k.065338", "hw": "merchantabilities", "pos": "noun", "ipa": "/ˌmɜːrtʃəntəˈbɪlətiz/", "vi": "khả năng đủ chuẩn lưu thông bán"},
  {"id": "lex.en.200k.065339", "hw": "meristems", "pos": "noun", "ipa": "/ˈmɛrɪstɛmz/", "vi": "mô phân sinh giúp cây mọc dài to"},
  {"id": "lex.en.200k.065340", "hw": "millenarians", "pos": "noun", "ipa": "/ˌmɪləˈnɛriənz/", "vi": "người tin vào kỷ nguyên ngàn năm"},
  {"id": "lex.en.200k.065341", "hw": "moochers", "pos": "noun", "ipa": "/ˈmuːtʃərz/", "vi": "kẻ hay ăn bám xin xỏ (tiếng lóng)"},
  {"id": "lex.en.200k.065342", "hw": "muezzins", "pos": "noun", "ipa": "/mjuːˈɛzɪnz/", "vi": "người xướng lời mời cầu nguyện Hồi"},
  {"id": "lex.en.200k.065343", "hw": "muralists", "pos": "noun", "ipa": "/ˈmjʊrəlɪsts/", "vi": "họa sĩ vẽ tranh bích họa trên tường"},
  {"id": "lex.en.200k.065344", "hw": "mycobacterias", "pos": "noun", "ipa": "/ˌmaɪkoʊbækˈtɪriəz/", "vi": "vi khuẩn gây bệnh lao Mycobacteria"},
  {"id": "lex.en.200k.065345", "hw": "myotises", "pos": "noun", "ipa": "/maɪˈoʊtɪsɪz/", "vi": "loài dơi nhỏ tai chuột sống hang"},
  {"id": "lex.en.200k.065346", "hw": "nabus", "pos": "noun", "ipa": "/ˈnɑːbuːz/", "vi": "thần trí tuệ chữ viết Babylon Nabu"},
  {"id": "lex.en.200k.065347", "hw": "nanticokes", "pos": "noun", "ipa": "/ˈnæntɪˌkoʊks/", "vi": "bộ tộc bản địa Nanticoke miền đông"},
  {"id": "lex.en.200k.065348", "hw": "neckerchiefs", "pos": "noun", "ipa": "/ˈnɛkərtʃɪfs/", "vi": "khăn vuông quàng buộc quanh cổ"},
  {"id": "lex.en.200k.065349", "hw": "nullahs", "pos": "noun", "ipa": "/ˈnʌləz/", "vi": "khe suối cạn xói mòn mùa khô Ấn Độ"},
  {"id": "lex.en.200k.065350", "hw": "oarfishes", "pos": "noun", "ipa": "/ˈɔːrfɪʃɪz/", "vi": "cá mái chèo thân dải dài biển sâu"},
  {"id": "lex.en.200k.065351", "hw": "oceanuses", "pos": "noun", "ipa": "/oʊˈsiːənəsɪz/", "vi": "thần đại dương Oceanus Hy Lạp cổ"},
  {"id": "lex.en.200k.065352", "hw": "ogees", "pos": "noun", "ipa": "/oʊˈdʒiːz/", "vi": "đường cong chữ S trong kiến trúc"},
  {"id": "lex.en.200k.065353", "hw": "pardners", "pos": "noun", "ipa": "/ˈpɑːrdnərz/", "vi": "bạn đồng hành thân (lóng miền Tây)"},
  {"id": "lex.en.200k.065354", "hw": "paschas", "pos": "noun", "ipa": "/ˈpæskəz/", "vi": "lễ Vượt Qua Do Thái; lễ Phục Sinh"},
  {"id": "lex.en.200k.065355", "hw": "polders", "pos": "noun", "ipa": "/ˈpoʊldərz/", "vi": "vùng đất lấn biển đắp đê Hà Lan"},
  {"id": "lex.en.200k.065356", "hw": "poseurs", "pos": "noun", "ipa": "/poʊˈzɜːrz/", "vi": "kẻ làm dáng giả tạo khoe mẽ"},
  {"id": "lex.en.200k.065357", "hw": "postfixes", "pos": "noun", "ipa": "/ˈpoʊstfɪksɪz/", "vi": "hậu tố gắn sau từ; ký pháp hậu tố"},
  {"id": "lex.en.200k.065358", "hw": "preservationists", "pos": "noun", "ipa": "/ˌprɛzərˈveɪʃənɪsts/", "vi": "người ủng hộ bảo tồn thiên nhiên"},
  {"id": "lex.en.200k.065359", "hw": "prognostications", "pos": "noun", "ipa": "/prɑːɡˌnɑːstəˈkeɪʃənz/", "vi": "lời tiên đoán dự báo tương lai"},
  {"id": "lex.en.200k.065360", "hw": "protestations", "pos": "noun", "ipa": "/ˌprɑːtɛˈsteɪʃənz/", "vi": "lời phản kháng kịch liệt; cam đoan"},
  {"id": "lex.en.200k.065361", "hw": "psychometricses", "pos": "noun", "ipa": "/ˌsaɪkəˈmɛtrɪksɪz/", "vi": "ngành trắc nghiệm đo lường tâm lý"},
  {"id": "lex.en.200k.065362", "hw": "purebloods", "pos": "noun", "ipa": "/ˈpjʊərblʌdz/", "vi": "thú nòi thuần chủng; dòng dõi thuần"},
  {"id": "lex.en.200k.065363", "hw": "recalculations", "pos": "noun", "ipa": "/ˌriːkælkjəˈleɪʃənz/", "vi": "quá trình tính toán kiểm tra lại"},
  {"id": "lex.en.200k.065364", "hw": "redcoats", "pos": "noun", "ipa": "/ˈrɛdkoʊts/", "vi": "lính Anh mặc quân phục áo đỏ xưa"},
  {"id": "lex.en.200k.065365", "hw": "sacagaweas", "pos": "noun", "ipa": "/ˌsækədʒəˈwiːəz/", "vi": "nữ dẫn đường bản địa Mỹ Sacagawea"},
  {"id": "lex.en.200k.065366", "hw": "samhitas", "pos": "noun", "ipa": "/sɑːmˈhiːtəz/", "vi": "tập thánh ca cổ Veda Samhita Ấn Độ"},
  {"id": "lex.en.200k.065367", "hw": "shalwars", "pos": "noun", "ipa": "/ˈʃælwɑːrz/", "vi": "quần ống rộng túm cổ chân Nam Á"},
  {"id": "lex.en.200k.065368", "hw": "shillelaghs", "pos": "noun", "ipa": "/ʃɪˈleɪliz/", "vi": "gậy gỗ sồi chiến đấu Ai-len"},
  {"id": "lex.en.200k.065369", "hw": "soymilks", "pos": "noun", "ipa": "/ˈsɔɪmɪlks/", "vi": "sữa thực vật chế biến từ đậu nành"},
  {"id": "lex.en.200k.065370", "hw": "sparlings", "pos": "noun", "ipa": "/ˈspɑːrlɪŋz/", "vi": "cá ốt-me châu Âu mùi dưa chuột"},
  {"id": "lex.en.200k.065371", "hw": "spiffs", "pos": "noun", "ipa": "/spɪfs/", "vi": "tiền thưởng bán hàng; vẻ bảnh bao"},
  {"id": "lex.en.200k.065372", "hw": "spittoons", "pos": "noun", "ipa": "/spɪˈtuːnz/", "vi": "ống nhổ bằng đồng hoặc sứ thời xưa"},
  {"id": "lex.en.200k.065373", "hw": "stapedes", "pos": "noun", "ipa": "/stəˈpiːdiːz/", "vi": "các xương bàn đạp trong tai giữa"},
  {"id": "lex.en.200k.065374", "hw": "stapeses", "pos": "noun", "ipa": "/ˈsteɪpiːzɪz/", "vi": "xương bàn đạp truyền rung động tai"},
  {"id": "lex.en.200k.065375", "hw": "steichens", "pos": "noun", "ipa": "/ˈstaɪkənz/", "vi": "nhiếp ảnh gia Mỹ Edward Steichen"},
  {"id": "lex.en.200k.065376", "hw": "stokowskis", "pos": "noun", "ipa": "/stəˈkɔːfskiz/", "vi": "nhạc trưởng tài hoa Stokowski"},
  {"id": "lex.en.200k.065377", "hw": "stroheims", "pos": "noun", "ipa": "/ˈstroʊhaɪmz/", "vi": "đạo diễn điện ảnh Mỹ Stroheim"},
  {"id": "lex.en.200k.065378", "hw": "tampaxes", "pos": "noun", "ipa": "/ˈtæmpæksɪz/", "vi": "băng vệ sinh dạng ống đặt Tampax"},
  {"id": "lex.en.200k.065379", "hw": "tanguys", "pos": "noun", "ipa": "/tɑːŋˈɡiːz/", "vi": "họa sĩ siêu thực Pháp Yves Tanguy"},
  {"id": "lex.en.200k.065380", "hw": "teffs", "pos": "noun", "ipa": "/tɛfs/", "vi": "hạt ngũ cốc nhỏ giàu sắt Ethiopia"},
  {"id": "lex.en.200k.065381", "hw": "thunderheads", "pos": "noun", "ipa": "/ˈθʌndərˌhɛdz/", "vi": "đám mây dông bão lớn tích tụ cao"},
  {"id": "lex.en.200k.065382", "hw": "trigons", "pos": "noun", "ipa": "/ˈtraɪɡɑːnz/", "vi": "hình tam giác; tam hợp chiêm tinh"},
  {"id": "lex.en.200k.065383", "hw": "tzars", "pos": "noun", "ipa": "/zɑːrz/", "vi": "sa hoàng đế chế Nga; ông trùm lớn"},
  {"id": "lex.en.200k.065384", "hw": "urds", "pos": "noun", "ipa": "/ʊərdz/", "vi": "nữ thần định mệnh quá khứ Bắc Âu"},
  {"id": "lex.en.200k.065385", "hw": "vaishnavas", "pos": "noun", "ipa": "/ˈvaɪʃnəvəz/", "vi": "tín đồ Ấn Độ giáo tôn thờ Vishnu"},
  {"id": "lex.en.200k.065386", "hw": "vascularities", "pos": "noun", "ipa": "/ˌvæskjəˈlærətiz/", "vi": "mật độ phân bố mạch máu trong mô"},
  {"id": "lex.en.200k.065387", "hw": "vaudevillians", "pos": "noun", "ipa": "/ˌvɔːdəˈvɪliənz/", "vi": "nghệ sĩ biểu diễn kịch tạp kỹ hài"},
  {"id": "lex.en.200k.065388", "hw": "vestments", "pos": "noun", "ipa": "/ˈvɛstmənts/", "vi": "lễ phục nghi lễ của linh mục"},
  {"id": "lex.en.200k.065389", "hw": "wernickes", "pos": "noun", "ipa": "/ˈvɛrnəkəz/", "vi": "bác sĩ thần kinh Đức Carl Wernicke"},
  {"id": "lex.en.200k.065390", "hw": "wheatfields", "pos": "noun", "ipa": "/ˈwiːtfiːldz/", "vi": "cánh đồng trồng lúa mì vàng rộng"},
  {"id": "lex.en.200k.065391", "hw": "woodpiles", "pos": "noun", "ipa": "/ˈwʊdpaɪlz/", "vi": "đống gỗ củi xếp gọn dùng sưởi ấm"},
  {"id": "lex.en.200k.065392", "hw": "zetlands", "pos": "noun", "ipa": "/ˈzɛtləndz/", "vi": "quần đảo Shetland (tên viết cũ)"},
  {"id": "lex.en.200k.065393", "hw": "alnus rubra", "pos": "phrase", "ipa": "/ˈælnəs ˈruːbrə/", "vi": "cây tống quán sủ vỏ đỏ tây Bắc Mỹ"},
  {"id": "lex.en.200k.065394", "hw": "army cutworm", "pos": "phrase", "ipa": "/ˈɑːrmi ˈkʌtwɜːrm/", "vi": "sâu xám di trú phá hoại mùa màng"},
  {"id": "lex.en.200k.065395", "hw": "battle of navarino", "pos": "phrase", "ipa": "/ˈbætəl əv ˌnævəˈriːnoʊ/", "vi": "hải chiến Navarino năm 1827 Hy Lạp"},
  {"id": "lex.en.200k.065396", "hw": "biogeographical region", "pos": "phrase", "ipa": "/ˌbaɪoʊˌdʒiːəˈɡræfəkəl ˈriːdʒən/", "vi": "khu vực vùng địa lý sinh học lớn"},
  {"id": "lex.en.200k.065397", "hw": "bosie ball", "pos": "phrase", "ipa": "/ˈboʊzi bɔːl/", "vi": "quả ném xoáy lừa trong môn cricket"},
  {"id": "lex.en.200k.065398", "hw": "bristlecone pine", "pos": "phrase", "ipa": "/ˈbrɪsəlˌkoʊn paɪn/", "vi": "cây thông nón gai cổ thụ ngàn năm"},
  {"id": "lex.en.200k.065399", "hw": "canis familiaris", "pos": "phrase", "ipa": "/ˈkeɪnɪs fəˌmɪliˈɛrɪs/", "vi": "loài chó nhà thuần hóa làm bạn"},
  {"id": "lex.en.200k.065400", "hw": "carrick bitt", "pos": "phrase", "ipa": "/ˈkærɪk bɪt/", "vi": "cọc gỗ đỡ tời kéo neo trên boong"},
  {"id": "lex.en.200k.065401", "hw": "coffea arabica", "pos": "phrase", "ipa": "/ˈkɔːfiə əˈræbɪkə/", "vi": "cây cà phê chè Arabica hương thơm"},
  {"id": "lex.en.200k.065402", "hw": "depressor muscle", "pos": "phrase", "ipa": "/dɪˈprɛsər ˈmʌsəl/", "vi": "cơ kéo hạ bộ phận xuống vùng mặt"}
]

with open('scratch/b34_r01_raw_p4.json') as f:
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

with open('scratch/b34_r01_p4.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r01_p4.json OK")
