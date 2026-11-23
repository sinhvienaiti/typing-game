import json

# Manual cognitive QA review for Batch 29 Round 2 Part 2 (IDs 040602 to 040701)
reviewed_items = [
    {"id": "lex.en.200k.040602", "hw": "shunt circuit", "pos": "phrase", "ipa": "", "vi": "mạch điện rẽ song song", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040603", "hw": "siberian millet", "pos": "phrase", "ipa": "", "vi": "kê đuôi chồn Siberia", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040604", "hw": "siege of vicksburg", "pos": "phrase", "ipa": "", "vi": "cuộc vây hãm thành Vicksburg", "cefr": "B2", "tier": "history", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040605", "hw": "slender wild oat", "pos": "phrase", "ipa": "", "vi": "cỏ yến mạch hoang mảnh dẻ", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040606", "hw": "small white aster", "pos": "phrase", "ipa": "", "vi": "hoa cúc tây trắng nhỏ", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040607", "hw": "southern aster", "pos": "phrase", "ipa": "", "vi": "hoa cúc tây phương nam", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040608", "hw": "stagger bush", "pos": "phrase", "ipa": "", "vi": "cây bụi độc hoa trắng", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040609", "hw": "summer savoury", "pos": "phrase", "ipa": "", "vi": "rau húng quế mùa hè savoury", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040610", "hw": "sun myung moon", "pos": "phrase", "ipa": "", "vi": "giáo chủ Sun Myung Moon", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040611", "hw": "surety bond", "pos": "phrase", "ipa": "", "vi": "hợp đồng bảo lãnh bảo lãnh", "cefr": "C1", "tier": "business", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040612", "hw": "syntactic category", "pos": "phrase", "ipa": "", "vi": "từ loại ngữ pháp; nhóm cú pháp", "cefr": "C2", "tier": "academic", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040613", "hw": "syrian bean caper", "pos": "phrase", "ipa": "", "vi": "cây bạch hoa Syria thuốc", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040614", "hw": "terrestrial dynamical time", "pos": "phrase", "ipa": "", "vi": "thời gian động lực Trái Đất", "cefr": "C2", "tier": "science", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040615", "hw": "theodore francis powys", "pos": "phrase", "ipa": "", "vi": "nhà văn Theodore Powys", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040616", "hw": "thomas lanier williams", "pos": "phrase", "ipa": "", "vi": "nhà soạn kịch Tennessee Williams", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040617", "hw": "timothy leary", "pos": "phrase", "ipa": "", "vi": "nhà tâm lý Timothy Leary", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040618", "hw": "touch modality", "pos": "phrase", "ipa": "", "vi": "phương thức cảm giác xúc giác", "cefr": "C2", "tier": "academic", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040619", "hw": "toy spaniel", "pos": "phrase", "ipa": "", "vi": "chó cảnh spaniel mini", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040620", "hw": "transvaal daisy", "pos": "phrase", "ipa": "", "vi": "hoa cúc đồng tiền Nam Phi", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040621", "hw": "welsh corgi", "pos": "phrase", "ipa": "", "vi": "chó cưng corgi chân ngắn xứ Wales", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040622", "hw": "william maxwell aitken", "pos": "phrase", "ipa": "", "vi": "huân tước Beaverbrook Aitken", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040623", "hw": "winter savoury", "pos": "phrase", "ipa": "", "vi": "rau thơm húng mùa đông savoury", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040624", "hw": "wood aster", "pos": "phrase", "ipa": "", "vi": "hoa cúc sao rừng dại", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040625", "hw": "admirers", "pos": "noun", "ipa": "/ədˈmaɪərərz/", "vi": "người thán phục; người ái mộ", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040626", "hw": "agitations", "pos": "noun", "ipa": "/ˌædʒɪˈteɪʃənz/", "vi": "sự xao xuyến; phong trào cổ động", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040627", "hw": "airways", "pos": "noun", "ipa": "/ˈɛrweɪz/", "vi": "tuyến đường hàng không; đường thở", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040628", "hw": "backseats", "pos": "noun", "ipa": "/ˈbækˌsiːts/", "vi": "băng ghế sau xe; vị trí phụ", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040629", "hw": "braggs", "pos": "noun", "ipa": "/bræɡz/", "vi": "định luật Bragg; người Bragg", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040630", "hw": "breakaways", "pos": "noun", "ipa": "/ˈbreɪkəweɪz/", "vi": "nhóm ly khai; sự bứt phá tách đàn", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040631", "hw": "bruneis", "pos": "noun", "ipa": "/bruːˈnaɪz/", "vi": "người Brunei; vương quốc Brunei", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040632", "hw": "cartons", "pos": "noun", "ipa": "/ˈkɑːrtənz/", "vi": "thùng các-tông; hộp bìa cứng", "cefr": "A2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040633", "hw": "caymans", "pos": "noun", "ipa": "/ˈkeɪmənz/", "vi": "cá sấu caiman Nam Mỹ", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040634", "hw": "certs", "pos": "noun", "ipa": "/sɜːrts/", "vi": "điều chắc chắn ăn; chứng chỉ thi", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040635", "hw": "chutes", "pos": "noun", "ipa": "/ʃuːts/", "vi": "máng trượt đổ rác; dù nhảy dù", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040636", "hw": "clippings", "pos": "noun", "ipa": "/ˈklɪpɪŋz/", "vi": "đoạn cắt báo chí; vụn cỏ tỉa", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040637", "hw": "coolants", "pos": "noun", "ipa": "/ˈkuːlənts/", "vi": "chất làm mát động cơ tản nhiệt", "cefr": "C1", "tier": "technology", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040638", "hw": "corbetts", "pos": "noun", "ipa": "/ˈkɔːrbɪts/", "vi": "gia tộc Corbett; nhà văn Corbett", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040639", "hw": "cravens", "pos": "noun", "ipa": "/ˈkreɪvənz/", "vi": "kẻ hèn nhát ti tiện nhút nhát", "cefr": "C2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040640", "hw": "cumbrias", "pos": "noun", "ipa": "/ˈkʌmbriəz/", "vi": "hạt Cumbria ở Tây Bắc nước Anh", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040641", "hw": "downturns", "pos": "noun", "ipa": "/ˈdaʊntɜːrnz/", "vi": "thời kỳ suy thoái; đà đi xuống", "cefr": "B2", "tier": "business", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040642", "hw": "driers", "pos": "noun", "ipa": "/ˈdraɪərz/", "vi": "máy sấy khô; chất làm khô sơn", "cefr": "A2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040643", "hw": "enclaves", "pos": "noun", "ipa": "/ˈɛnkleɪvz/", "vi": "vùng đất lọt; cộng đồng biệt lập", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040644", "hw": "entourages", "pos": "noun", "ipa": "/ˌɑːntuˈrɑːʒɪz/", "vi": "đoàn tùy tùng; ban bệ tháp tùng", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040645", "hw": "epochs", "pos": "noun", "ipa": "/ˈɛpəks/", "vi": "kỷ nguyên địa chất; thời đại mới", "cefr": "B2", "tier": "academic", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040646", "hw": "foggier", "pos": "adj", "ipa": "/ˈfɑːɡiər/", "vi": "nhiều sương mù hơn; mù mờ hơn", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040647", "hw": "foggiest", "pos": "adj", "ipa": "/ˈfɑːɡiɪst/", "vi": "mờ mịt nhất; nhiều sương mù nhất", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040648", "hw": "forgeries", "pos": "noun", "ipa": "/ˈfɔːrdʒəriz/", "vi": "tội làm giả giấy tờ; đồ giả mạo", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040649", "hw": "gators", "pos": "noun", "ipa": "/ˈɡeɪtərz/", "vi": "cá sấu mõm ngắn Mỹ", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040650", "hw": "gentries", "pos": "noun", "ipa": "/ˈdʒɛntriz/", "vi": "tầng lớp quý tộc điền trang", "cefr": "C1", "tier": "history", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040651", "hw": "germanics", "pos": "noun", "ipa": "/dʒɜːrˈmænɪks/", "vi": "người German; ngữ tộc German", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040652", "hw": "gimmicks", "pos": "noun", "ipa": "/ˈɡɪmɪks/", "vi": "mẹo quảng cáo; chiêu trò thu hút", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040653", "hw": "gladiators", "pos": "noun", "ipa": "/ˈɡlædieɪtərz/", "vi": "võ sĩ giác đấu thời La Mã cổ", "cefr": "B2", "tier": "history", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040654", "hw": "gymnasiums", "pos": "noun", "ipa": "/dʒɪmˈneɪziəmz/", "vi": "phòng tập thể dục; trường cấp ba", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040655", "hw": "hammerings", "pos": "noun", "ipa": "/ˈhæmərɪŋz/", "vi": "tiếng gõ búa; thất bại nặng nề", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040656", "hw": "harrisburgs", "pos": "noun", "ipa": "/ˈhærɪsbɜːrɡz/", "vi": "thành phố Harrisburg Mỹ", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040657", "hw": "impositions", "pos": "noun", "ipa": "/ˌɪmpəˈzɪʃənz/", "vi": "sự áp đặt; gánh nặng phiền toái", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040658", "hw": "impromptus", "pos": "noun", "ipa": "/ɪmˈprɑːmptuːz/", "vi": "khúc ngẫu hứng; lời ứng khẩu", "cefr": "C2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040659", "hw": "krugers", "pos": "noun", "ipa": "/ˈkruːɡərz/", "vi": "vườn quốc gia Kruger; người Kruger", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040660", "hw": "lewder", "pos": "adj", "ipa": "/ˈluːdər/", "vi": "dâm ô hơn; phóng đãng tục tĩu hơn", "cefr": "C2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040661", "hw": "lewdest", "pos": "adj", "ipa": "/ˈluːdɪst/", "vi": "dâm dục nhất; thô bỉ tục tĩu nhất", "cefr": "C2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040662", "hw": "lifeboats", "pos": "noun", "ipa": "/ˈlaɪfboʊts/", "vi": "xuồng cứu sinh khẩn cấp trên tàu", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040663", "hw": "mammalians", "pos": "noun", "ipa": "/mæˈmeɪliənz/", "vi": "loài thú có vú; động vật nuôi con", "cefr": "B2", "tier": "science", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040664", "hw": "moldings", "pos": "noun", "ipa": "/ˈmoʊldɪŋz/", "vi": "đường gờ chỉ viền trang trí tường", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040665", "hw": "motorbiked", "pos": "verb", "ipa": "/ˈmoʊtərbaɪkt/", "vi": "đã đi xe mô tô phân khối lớn", "cefr": "A2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040666", "hw": "motorbiking", "pos": "verb", "ipa": "/ˈmoʊtərbaɪkɪŋ/", "vi": "việc lái xe máy; phượt xe gắn máy", "cefr": "A2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040667", "hw": "nuttier", "pos": "adj", "ipa": "/ˈnʌtiər/", "vi": "đậm vị bùi hạt hơn; gàn dở hơn", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040668", "hw": "nuttiest", "pos": "adj", "ipa": "/ˈnʌtiɪst/", "vi": "bùi béo nhất; gàn dở quái lạ nhất", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040669", "hw": "oculuses", "pos": "noun", "ipa": "/ˈɑːkjələsɪz/", "vi": "cửa sổ tròn đỉnh vòm; mắt tròn", "cefr": "C2", "tier": "architecture", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040670", "hw": "ogdens", "pos": "noun", "ipa": "/ˈɑːɡdənz/", "vi": "thành phố Ogden; gia tộc Ogden", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040671", "hw": "paramedics", "pos": "noun", "ipa": "/ˌpærəˈmɛdɪks/", "vi": "nhân viên y tế cứu thương khẩn cấp", "cefr": "B2", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040672", "hw": "philharmonics", "pos": "noun", "ipa": "/ˌfɪlhɑːrˈmɑːnɪks/", "vi": "dàn nhạc đại hòa tấu giao hưởng", "cefr": "C1", "tier": "music", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040673", "hw": "plumpest", "pos": "adj", "ipa": "/ˈplʌmpɪst/", "vi": "đầy đặn nhất; bụ bẫm mập mạp nhất", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040674", "hw": "raffled", "pos": "verb", "ipa": "/ˈræfəld/", "vi": "đã bán vé số trúng thưởng xổ số", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040675", "hw": "raggeder", "pos": "adj", "ipa": "/ˈræɡɪdər/", "vi": "rách rưới tả tơi hơn; lởm chởm hơn", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040676", "hw": "raggedest", "pos": "adj", "ipa": "/ˈræɡɪdɪst/", "vi": "tả tơi rách rưới nhất; gồ ghề nhất", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040677", "hw": "recoiled", "pos": "verb", "ipa": "/rɪˈkɔɪld/", "vi": "đã giật nảy lùi lại; chùn bước lùi", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040678", "hw": "recoiling", "pos": "verb", "ipa": "/rɪˈkɔɪlɪŋ/", "vi": "đang giật lùi; đang co rúm người", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040679", "hw": "recoils", "pos": "noun", "ipa": "/ˈriːkɔɪlz/", "vi": "độ giật súng; phản lực giật lùi", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040680", "hw": "redoes", "pos": "verb", "ipa": "/ˌriːˈduːz/", "vi": "làm lại từ đầu; trang hoàng lại", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040681", "hw": "redoing", "pos": "verb", "ipa": "/ˌriːˈduːɪŋ/", "vi": "đang thực hiện lại; sửa sang lại", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040682", "hw": "remissions", "pos": "noun", "ipa": "/rɪˈmɪʃənz/", "vi": "giai đoạn thuyên giảm bệnh", "cefr": "C1", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040683", "hw": "renounced", "pos": "verb", "ipa": "/rɪˈnaʊnst/", "vi": "đã tuyên bố từ bỏ; đã chối bỏ", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040684", "hw": "rotterdams", "pos": "noun", "ipa": "/ˈrɑːtərdæmz/", "vi": "thành phố cảng Rotterdam Hà Lan", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040685", "hw": "sevilles", "pos": "noun", "ipa": "/səˈvɪlz/", "vi": "cam đắng Seville; vùng Seville", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040686", "hw": "shoppers", "pos": "noun", "ipa": "/ˈʃɑːpərz/", "vi": "người đi mua hàng; khách mua sắm", "cefr": "A2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040687", "hw": "shrubs", "pos": "noun", "ipa": "/ʃrʌbz/", "vi": "cây bụi rậm; đồ uống siro hoa quả", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040688", "hw": "soms", "pos": "noun", "ipa": "/sɑːmz/", "vi": "đồng tiền som Kyrgyzstan", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040689", "hw": "sprinters", "pos": "noun", "ipa": "/ˈsprɪntərz/", "vi": "vận động viên chạy nước rút tốc độ", "cefr": "B2", "tier": "sports", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040690", "hw": "steads", "pos": "noun", "ipa": "/stɛdz/", "vi": "vị trí thay thế; vai trò thế chỗ", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040691", "hw": "suezes", "pos": "noun", "ipa": "/ˈsuːɛzɪz/", "vi": "kênh đào Suez; thành phố Suez", "cefr": "B2", "tier": "geography", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040692", "hw": "sulfates", "pos": "noun", "ipa": "/ˈsʌlfeɪts/", "vi": "muối sunfat; este axit sunfuric", "cefr": "C1", "tier": "science", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040693", "hw": "sumners", "pos": "noun", "ipa": "/ˈsʌmnərz/", "vi": "nghị sĩ Sumner; gia tộc Sumner", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040694", "hw": "swagged", "pos": "verb", "ipa": "/swæɡd/", "vi": "đã uốn vòng cung; đã buông rủ", "cefr": "C2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040695", "hw": "swagging", "pos": "verb", "ipa": "/ˈswæɡɪŋ/", "vi": "việc kết dải rủ hoa lá trang trí", "cefr": "C2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040696", "hw": "swags", "pos": "noun", "ipa": "/swæɡz/", "vi": "dải hoa lá rủ; mớ đồ đạc cuộn", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040697", "hw": "sweatshirts", "pos": "noun", "ipa": "/ˈswɛtʃɜːrts/", "vi": "áo nỉ chui đầu dài tay thể thao", "cefr": "A2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040698", "hw": "tangents", "pos": "noun", "ipa": "/ˈtændʒənts/", "vi": "tiếp tuyến đường cong; hàm số tang", "cefr": "B2", "tier": "academic", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040699", "hw": "tracers", "pos": "noun", "ipa": "/ˈtreɪsərz/", "vi": "chất đồng vị đánh dấu; đạn vạch", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040700", "hw": "transporters", "pos": "noun", "ipa": "/trænˈspɔːrtərz/", "vi": "xe tải chuyên chở ô tô container", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040701", "hw": "turings", "pos": "noun", "ipa": "/ˈtjʊərɪŋz/", "vi": "máy Turing; nhà toán học Turing", "cefr": "B2", "tier": "technology", "status": "reviewed", "notes": ""}
]

# Validation
ALLOWED_POS = {"noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "det", "num", "phrase"}
with open('scratch/b29_r02_raw_p2.json', 'r', encoding='utf-8') as f:
    raw_items = json.load(f)

assert len(reviewed_items) == 100, f"Expected 100 items, got {len(reviewed_items)}"
for r, rev in zip(raw_items, reviewed_items):
    assert r["id"] == rev["id"], f"ID mismatch: {r['id']} vs {rev['id']}"
    assert r["hw"] == rev["hw"], f"HW mismatch: {r['hw']} vs {rev['hw']}"
    assert rev["pos"] in ALLOWED_POS, f"Invalid POS for {rev['id']}: {rev['pos']}"
    assert 0 < len(rev["vi"]) <= 35, f"Invalid VI length ({len(rev['vi'])}) for {rev['id']}: {rev['vi']}"
    assert rev["status"] == "reviewed", f"Status must be reviewed: {rev['id']}"
    if " " not in rev["hw"]:
        assert rev["ipa"].startswith("/") and rev["ipa"].endswith("/") and rev["ipa"].count("/") == 2, f"Invalid single-word IPA: {rev['id']}: {rev['ipa']}"

with open('scratch/b29_r02_p2.json', 'w', encoding='utf-8') as f:
    json.dump(reviewed_items, f, ensure_ascii=False, indent=2)

print("Batch 29 Round 2 Part 2 validated and written successfully. Total items:", len(reviewed_items))
