import json

# Manual cognitive QA review for Batch 29 Round 2 Part 4 (IDs 040802 to 040901)
reviewed_items = [
    {"id": "lex.en.200k.040802", "hw": "spiral ratchet screwdriver", "pos": "phrase", "ipa": "", "vi": "tua vít bánh cóc xoắn ốc tự động", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040803", "hw": "stellar parallax", "pos": "phrase", "ipa": "", "vi": "thị sai sao vũ trụ", "cefr": "C2", "tier": "science", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040804", "hw": "subcutaneous injection", "pos": "phrase", "ipa": "", "vi": "tiêm thuốc dưới mô da", "cefr": "C1", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040805", "hw": "sweet cassava", "pos": "phrase", "ipa": "", "vi": "củ khoai mì ngọt; sắn ngọt", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040806", "hw": "switchboard operator", "pos": "phrase", "ipa": "", "vi": "nhân viên trực tổng đài điện thoại", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040807", "hw": "teamsters union", "pos": "phrase", "ipa": "", "vi": "nghiệp đoàn tài xế lái xe tải", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040808", "hw": "the hots", "pos": "phrase", "ipa": "", "vi": "cơn khao khát tình cảm mê đắm", "cefr": "C2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040809", "hw": "timothy francis leary", "pos": "phrase", "ipa": "", "vi": "nhà tâm lý Timothy Leary", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040810", "hw": "trailing windmills", "pos": "phrase", "ipa": "", "vi": "cây hoa cối xay bò mặt đất", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040811", "hw": "turnip greens", "pos": "phrase", "ipa": "", "vi": "lá củ cải xanh dùng nấu ăn", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040812", "hw": "vertebral column", "pos": "phrase", "ipa": "", "vi": "cột sống xương lưng", "cefr": "C1", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040813", "hw": "virgil garnett thomson", "pos": "phrase", "ipa": "", "vi": "nhạc sĩ Virgil Thomson", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040814", "hw": "visual acuity", "pos": "phrase", "ipa": "", "vi": "độ sắc nét thị lực mắt", "cefr": "C1", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040815", "hw": "visual modality", "pos": "phrase", "ipa": "", "vi": "phương thức thị giác giác quan", "cefr": "C2", "tier": "academic", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040816", "hw": "walter rudolf hess", "pos": "phrase", "ipa": "", "vi": "nhà sinh lý học Walter Hess", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040817", "hw": "white wood aster", "pos": "phrase", "ipa": "", "vi": "hoa cúc tây rừng trắng", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040818", "hw": "wiper arm", "pos": "phrase", "ipa": "", "vi": "cần gạt nước kính xe ô tô", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040819", "hw": "wiper motor", "pos": "phrase", "ipa": "", "vi": "mô tơ điều khiển cần gạt nước", "cefr": "B2", "tier": "technology", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040820", "hw": "zinc vitriol", "pos": "phrase", "ipa": "", "vi": "kẽm sunfat tinh thể muối", "cefr": "C2", "tier": "science", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040821", "hw": "adventurers", "pos": "noun", "ipa": "/ədˈvɛntʃərərz/", "vi": "nhà thám hiểm; người ưa mạo hiểm", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040822", "hw": "aeroplanes", "pos": "noun", "ipa": "/ˈɛrəpleɪnz/", "vi": "máy bay phản lực; tàu bay", "cefr": "A2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040823", "hw": "andromedas", "pos": "noun", "ipa": "/ænˈdrɑːmədəz/", "vi": "thiên hà Tiên Nữ; cây bụi đầm lầy", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040824", "hw": "bachelorettes", "pos": "noun", "ipa": "/ˌbætʃələˈrɛts/", "vi": "cô nàng độc thân; quý cô độc thân", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040825", "hw": "bagels", "pos": "noun", "ipa": "/ˈbeɪɡəlz/", "vi": "bánh mì vòng men nướng giòn", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040826", "hw": "bais", "pos": "noun", "ipa": "/baɪz/", "vi": "dân tộc Bạch; tiếng Bạch Trung Quốc", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040827", "hw": "bangors", "pos": "noun", "ipa": "/ˈbæŋɡɔːrz/", "vi": "thành phố Bangor bang Maine", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040828", "hw": "basques", "pos": "noun", "ipa": "/bæsks/", "vi": "người Basque; xứ Basque Tây Ban Nha", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040829", "hw": "bavarias", "pos": "noun", "ipa": "/bəˈvɛriəz/", "vi": "bang Bayern vùng Bavaria Đức", "cefr": "B2", "tier": "geography", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040830", "hw": "bigots", "pos": "noun", "ipa": "/ˈbɪɡəts/", "vi": "kẻ cố chấp mù quáng; người hẹp hòi", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040831", "hw": "boas", "pos": "noun", "ipa": "/ˈboʊəz/", "vi": "trăn siết mồi boa; khăn quàng lông", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040832", "hw": "britts", "pos": "noun", "ipa": "/brɪts/", "vi": "cá trích con; ấu trùng cá", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040833", "hw": "bucharests", "pos": "noun", "ipa": "/ˈbuːkərɛsts/", "vi": "thủ đô Bucharest Rumani", "cefr": "B2", "tier": "geography", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040834", "hw": "bumpier", "pos": "adj", "ipa": "/ˈbʌmpiər/", "vi": "gồ ghề mấp mô hơn; xóc nảy hơn", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040835", "hw": "bumpiest", "pos": "adj", "ipa": "/ˈbʌmpiɪst/", "vi": "gồ ghề mấp mô nhất; gập ghềnh nhất", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040836", "hw": "burnhams", "pos": "noun", "ipa": "/ˈbɜːrnhəmz/", "vi": "gia tộc Burnham; kiến trúc sư", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040837", "hw": "castors", "pos": "noun", "ipa": "/ˈkæstərz/", "vi": "bánh xe lăn nhỏ; sao đôi Castor", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040838", "hw": "ciceros", "pos": "noun", "ipa": "/ˈsɪsəroʊz/", "vi": "hùng biện gia Cicero La Mã cổ", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040839", "hw": "circumferences", "pos": "noun", "ipa": "/sərˈkʌmfərənsɪz/", "vi": "chu vi đường tròn; đường bao quanh", "cefr": "B2", "tier": "academic", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040840", "hw": "cleopatras", "pos": "noun", "ipa": "/ˌkliːəˈpætrəz/", "vi": "nữ hoàng Cleopatra Ai Cập cổ", "cefr": "B1", "tier": "history", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040841", "hw": "davies", "pos": "noun", "ipa": "/ˈdeɪviz/", "vi": "nhà hóa học Humphry Davy", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040842", "hw": "dempseys", "pos": "noun", "ipa": "/ˈdɛmpsiz/", "vi": "võ sĩ vô địch Jack Dempsey", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040843", "hw": "dohas", "pos": "noun", "ipa": "/ˈdoʊhəz/", "vi": "thủ đô Doha nước Qatar", "cefr": "B2", "tier": "geography", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040844", "hw": "facets", "pos": "noun", "ipa": "/ˈfæsɪts/", "vi": "mặt giác cắt kim cương; khía cạnh", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040845", "hw": "facetted", "pos": "adj", "ipa": "/ˈfæsɪtɪd/", "vi": "được mài nhiều mặt giác góc cạnh", "cefr": "C2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040846", "hw": "facetting", "pos": "noun", "ipa": "/ˈfæsɪtɪŋ/", "vi": "việc mài giũa giác cắt góc cạnh", "cefr": "C2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040847", "hw": "fireballs", "pos": "noun", "ipa": "/ˈfaɪərbɔːlz/", "vi": "quả cầu lửa sáng; quả cầu sét", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040848", "hw": "firths", "pos": "noun", "ipa": "/fɜːrθs/", "vi": "vịnh hẹp ven biển; cửa sông biển", "cefr": "C2", "tier": "geography", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040849", "hw": "flossed", "pos": "verb", "ipa": "/flɑːst/", "vi": "đã làm sạch răng bằng chỉ nha khoa", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040850", "hw": "flosses", "pos": "noun", "ipa": "/ˈflɑːsɪz/", "vi": "cuộn sợi chỉ tơ nha khoa làm sạch", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040851", "hw": "flossing", "pos": "verb", "ipa": "/ˈflɑːsɪŋ/", "vi": "dùng chỉ nha khoa làm sạch răng", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040852", "hw": "foresees", "pos": "verb", "ipa": "/fɔːrˈsiːz/", "vi": "nhìn thấy trước; dự đoán trước", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040853", "hw": "genoas", "pos": "noun", "ipa": "/ˈdʒɛnoʊəz/", "vi": "cánh buồm genoa; thành phố Genoa", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040854", "hw": "handkerchiefs", "pos": "noun", "ipa": "/ˈhæŋkərtʃɪfs/", "vi": "khăn mùi soa bỏ túi; khăn tay vải", "cefr": "A2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040855", "hw": "hebrewses", "pos": "noun", "ipa": "/ˈhiːbruːzɪz/", "vi": "người Do Thái Hê-bơ-rơ cổ đại", "cefr": "B2", "tier": "history", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040856", "hw": "hepburns", "pos": "noun", "ipa": "/ˈhɛpbɜːrnz/", "vi": "minh tinh Audrey Hepburn tài ba", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040857", "hw": "hookups", "pos": "noun", "ipa": "/ˈhʊkʌps/", "vi": "mối tình một đêm; đầu nối ghép", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040858", "hw": "insolvencies", "pos": "noun", "ipa": "/ɪnˈsɑːlvənsiz/", "vi": "tình trạng vỡ nợ phá sản công ty", "cefr": "C1", "tier": "business", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040859", "hw": "iveses", "pos": "noun", "ipa": "/ˈaɪvzɪz/", "vi": "nhạc sĩ Charles Ives tiên phong", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040860", "hw": "klans", "pos": "noun", "ipa": "/klænz/", "vi": "hội kín phân biệt chủng tộc KKK", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040861", "hw": "lunds", "pos": "noun", "ipa": "/lʌndz/", "vi": "thành phố cổ Lund ở Thụy Điển", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040862", "hw": "marquees", "pos": "noun", "ipa": "/mɑːrˈkiːz/", "vi": "nhà bạt ngoài trời; mái rạp che", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040863", "hw": "mckinleys", "pos": "noun", "ipa": "/məˈkɪnliz/", "vi": "đỉnh núi McKinley; núi Denali", "cefr": "C2", "tier": "geography", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040864", "hw": "meades", "pos": "noun", "ipa": "/miːdz/", "vi": "tướng George Meade thời nội chiến", "cefr": "C2", "tier": "history", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040865", "hw": "melanomas", "pos": "noun", "ipa": "/ˌmɛləˈnoʊməz/", "vi": "khối u hắc tố ác tính; ung thư da", "cefr": "C1", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040866", "hw": "melanomata", "pos": "noun", "ipa": "/ˌmɛləˈnoʊmətə/", "vi": "các khối u hắc tố ác tính ở da", "cefr": "C2", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040867", "hw": "morleys", "pos": "noun", "ipa": "/ˈmɔːrliz/", "vi": "nhà vật lý Edward Morley quang học", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040868", "hw": "nativities", "pos": "noun", "ipa": "/nəˈtɪvətiz/", "vi": "cảnh Chúa Giáng sinh; sự sinh nở", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040869", "hw": "nooks", "pos": "noun", "ipa": "/nʊks/", "vi": "ngóc ngách nhỏ hẻo lánh kín đáo", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040870", "hw": "overdrives", "pos": "noun", "ipa": "/ˈoʊvərdraɪvz/", "vi": "bộ truyền động tăng tốc; quá tải", "cefr": "C1", "tier": "technology", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040871", "hw": "passovers", "pos": "noun", "ipa": "/ˈpæsoʊvərz/", "vi": "đại lễ Vượt Qua người Do Thái", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040872", "hw": "pekings", "pos": "noun", "ipa": "/piːˈkɪŋz/", "vi": "thủ đô Bắc Kinh; vịt quay Bắc Kinh", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040873", "hw": "polytechnics", "pos": "noun", "ipa": "/ˌpɑːliˈtɛknɪks/", "vi": "trường cao đẳng bách khoa", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040874", "hw": "posses", "pos": "noun", "ipa": "/ˈpɑːsiz/", "vi": "nhóm vũ trang tự quản; toán người", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040875", "hw": "rankins", "pos": "noun", "ipa": "/ˈræŋkɪnz/", "vi": "nữ hạ nghị sĩ Jeannette Rankin Mỹ", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040876", "hw": "respites", "pos": "noun", "ipa": "/ˈrɛspɪts/", "vi": "khoảng thời gian nghỉ ngơi tạm lắng", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040877", "hw": "rets", "pos": "verb", "ipa": "/rɛts/", "vi": "ngâm đay gai xuống nước rục tách xơ", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040878", "hw": "retted", "pos": "verb", "ipa": "/ˈrɛtɪd/", "vi": "đã ngâm nước phân rã tách sợi gai", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040879", "hw": "sabers", "pos": "noun", "ipa": "/ˈseɪbərz/", "vi": "thanh kiếm lưỡi cong kỵ binh Mỹ", "cefr": "B2", "tier": "history", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040880", "hw": "shaggier", "pos": "adj", "ipa": "/ˈʃæɡiər/", "vi": "lông rậm rạp xù xì hơn; thô hơn", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040881", "hw": "shaggiest", "pos": "adj", "ipa": "/ˈʃæɡiɪst/", "vi": "lông rậm xù nhất; nham nhở nhất", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040882", "hw": "sitters", "pos": "noun", "ipa": "/ˈsɪtərz/", "vi": "người làm mẫu vẽ; người trông trẻ", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040883", "hw": "spelts", "pos": "noun", "ipa": "/spɛlts/", "vi": "hạt lúa mì dinkel spelt cổ xưa", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040884", "hw": "steiners", "pos": "noun", "ipa": "/ˈstaɪnərz/", "vi": "triết lý giáo dục Steiner Waldorf", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040885", "hw": "strasbourgs", "pos": "noun", "ipa": "/ˈstrɑːsbʊərɡz/", "vi": "thành phố Strasbourg nước Pháp", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040886", "hw": "tackier", "pos": "adj", "ipa": "/ˈtækiər/", "vi": "dính dính hơn; quê mùa kệch cỡm hơn", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040887", "hw": "tackiest", "pos": "adj", "ipa": "/ˈtækiɪst/", "vi": "quê mùa rẻ tiền nhất; dính nhất", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040888", "hw": "texans", "pos": "noun", "ipa": "/ˈtɛksənz/", "vi": "người dân tiểu bang Texas nước Mỹ", "cefr": "B1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040889", "hw": "tolkiens", "pos": "noun", "ipa": "/ˈtɒlkiːnz/", "vi": "nhà văn Tolkien tác giả Chúa Nhẫn", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040890", "hw": "tripods", "pos": "noun", "ipa": "/ˈtraɪpɑːdz/", "vi": "giá đỡ ba chân chụp ảnh máy quay", "cefr": "B1", "tier": "technology", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040891", "hw": "tulips", "pos": "noun", "ipa": "/ˈtuːlɪps/", "vi": "bông hoa tulip uất kim hương nở", "cefr": "A2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040892", "hw": "turnpikes", "pos": "noun", "ipa": "/ˈtɜːrnpaɪks/", "vi": "xa lộ thu phí tự động cao tốc", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040893", "hw": "ulysseses", "pos": "noun", "ipa": "/juːˈlɪsiːzɪz/", "vi": "anh hùng Odyssey; người dũng cảm", "cefr": "C2", "tier": "literature", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040894", "hw": "undertakers", "pos": "noun", "ipa": "/ˈʌndərteɪkərz/", "vi": "người làm dịch vụ mai táng chôn cất", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040895", "hw": "uspses", "pos": "noun", "ipa": "/ˌjuːɛspiːˈɛsɪz/", "vi": "chi nhánh Bưu chính Hoa Kỳ USPS", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040896", "hw": "vultures", "pos": "noun", "ipa": "/ˈvʌltʃərz/", "vi": "chim kền kền ăn xác thối rỉa mồi", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040897", "hw": "waterways", "pos": "noun", "ipa": "/ˈwɔːtərweɪz/", "vi": "tuyến luồng đường thủy nội địa", "cefr": "B2", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040898", "hw": "whistleblowers", "pos": "noun", "ipa": "/ˈwɪsəlbloʊərz/", "vi": "người thổi còi tố giác sai phạm", "cefr": "C1", "tier": "general", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040899", "hw": "wvs", "pos": "noun", "ipa": "/ˌdʌbəljuːˈviːz/", "vi": "tiểu bang West Virginia nước Mỹ", "cefr": "C2", "tier": "specialized", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040900", "hw": "xanaxes", "pos": "noun", "ipa": "/ˈzænæksɪz/", "vi": "viên thuốc an thần giải lo âu Xanax", "cefr": "C1", "tier": "medical", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.040901", "hw": "acetone body", "pos": "phrase", "ipa": "", "vi": "thể xeton sinh học trong máu", "cefr": "C2", "tier": "medical", "status": "reviewed", "notes": ""}
]

# Validation
ALLOWED_POS = {"noun", "verb", "adj", "adv", "intj", "prep", "conj", "pron", "det", "num", "phrase"}
with open('scratch/b29_r02_raw_p4.json', 'r', encoding='utf-8') as f:
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

with open('scratch/b29_r02_p4.json', 'w', encoding='utf-8') as f:
    json.dump(reviewed_items, f, ensure_ascii=False, indent=2)

print("Batch 29 Round 2 Part 4 validated and written successfully. Total items:", len(reviewed_items))
