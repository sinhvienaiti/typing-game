import json
import re

items = [
    {"id": "lex.en.200k.041502", "hw": "cuddlier", "pos": "adj", "ipa": "/ˈkʌdliər/", "vi": "dễ ôm ấp hơn; đáng yêu hơn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041503", "hw": "cuddliest", "pos": "adj", "ipa": "/ˈkʌdliɪst/", "vi": "dễ ôm ấp nhất; đáng yêu nhất", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041504", "hw": "daks", "pos": "noun", "ipa": "/dæks/", "vi": "các trạm bưu điện dã chiến", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041505", "hw": "danubes", "pos": "noun", "ipa": "/ˈdænjuːbz/", "vi": "các vùng sông Danube", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041506", "hw": "deciphers", "pos": "verb", "ipa": "/dɪˈsaɪfərz/", "vi": "giải mã; đọc hiểu mật mã", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041507", "hw": "delved", "pos": "verb", "ipa": "/dɛlvd/", "vi": "đã đào sâu; đã nghiên cứu kỹ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041508", "hw": "delves", "pos": "verb", "ipa": "/dɛlvz/", "vi": "đào sâu; nghiên cứu kỹ lưỡng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041509", "hw": "delving", "pos": "verb", "ipa": "/ˈdɛlvɪŋ/", "vi": "đang đào sâu; đang tìm hiểu", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041510", "hw": "dissed", "pos": "verb", "ipa": "/dɪst/", "vi": "đã coi thường; đã chỉ trích", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041511", "hw": "disses", "pos": "verb", "ipa": "/ˈdɪsɪz/", "vi": "coi thường; chỉ trích; xấc xược", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041512", "hw": "dissing", "pos": "verb", "ipa": "/ˈdɪsɪŋ/", "vi": "đang coi thường; đang chỉ trích", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041513", "hw": "dunkirks", "pos": "noun", "ipa": "/ˈdʌnkərks/", "vi": "những cuộc di tản rút lui", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041514", "hw": "eyeshadows", "pos": "noun", "ipa": "/ˈaɪʃædoʊz/", "vi": "các loại phấn mắt trang điểm", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041515", "hw": "finishers", "pos": "noun", "ipa": "/ˈfɪnɪʃərz/", "vi": "người hoàn thành chặng đua", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041516", "hw": "gauntlets", "pos": "noun", "ipa": "/ˈɡɔːntlɪts/", "vi": "những chiếc găng tay giáp sắt", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041517", "hw": "gettysburgs", "pos": "noun", "ipa": "/ˈɡɛtɪzbɜːrɡz/", "vi": "các chiến trường Gettysburg", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041518", "hw": "ghostlier", "pos": "adj", "ipa": "/ˈɡoʊstliər/", "vi": "ma quái hơn; mờ ảo như ma hơn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041519", "hw": "ghostliest", "pos": "adj", "ipa": "/ˈɡoʊstliɪst/", "vi": "ma quái nhất; mờ ảo như ma nhất", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041520", "hw": "grillings", "pos": "noun", "ipa": "/ˈɡrɪlɪŋz/", "vi": "các cuộc thẩm vấn gắt gao", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041521", "hw": "haters", "pos": "noun", "ipa": "/ˈheɪtərz/", "vi": "những kẻ thù ghét; kẻ đố kỵ", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041522", "hw": "hazier", "pos": "adj", "ipa": "/ˈheɪziər/", "vi": "mờ sương hơn; mơ hồ hơn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041523", "hw": "haziest", "pos": "adj", "ipa": "/ˈheɪziɪst/", "vi": "mờ sương nhất; mơ hồ nhất", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041524", "hw": "imperialists", "pos": "noun", "ipa": "/ɪmˈpɪriəlɪsts/", "vi": "những kẻ theo chủ nghĩa đế quốc", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041525", "hw": "jinxes", "pos": "noun", "ipa": "/ˈdʒɪŋksɪz/", "vi": "những điều xui xẻo; điềm gở", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041526", "hw": "jinxing", "pos": "verb", "ipa": "/ˈdʒɪŋksɪŋ/", "vi": "đang ám quẻ; đem lại xui xẻo", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041527", "hw": "kelloggs", "pos": "noun", "ipa": "/ˈkɛlɔːɡz/", "vi": "ngũ cốc ăn sáng Kellogg", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041528", "hw": "keplers", "pos": "noun", "ipa": "/ˈkɛplərz/", "vi": "những người họ Kepler", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041529", "hw": "kyrgyzstans", "pos": "noun", "ipa": "/ˌkɜːrɡɪzˈstænz/", "vi": "các vùng đất Kyrgyzstan", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041530", "hw": "linkages", "pos": "noun", "ipa": "/ˈlɪŋkɪdʒɪz/", "vi": "các mối liên kết; sự móc nối", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041531", "hw": "louvres", "pos": "noun", "ipa": "/ˈluːvrəz/", "vi": "các bảo tàng Louvre; cửa sổ chớp", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041532", "hw": "mohawks", "pos": "noun", "ipa": "/ˈmoʊhɔːks/", "vi": "người da đỏ Mohawk; tóc đinh nhọn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041533", "hw": "nadas", "pos": "noun", "ipa": "/ˈnɑːdəz/", "vi": "những con số không tròn trĩnh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041534", "hw": "naftas", "pos": "noun", "ipa": "/ˈnæftəz/", "vi": "các hiệp ước thương mại NAFTA", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041535", "hw": "pancreases", "pos": "noun", "ipa": "/ˈpæŋkriəsɪz/", "vi": "các tuyến tụy", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041536", "hw": "parlours", "pos": "noun", "ipa": "/ˈpɑːrlərz/", "vi": "các phòng khách; phòng tiếp khách", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041537", "hw": "pashas", "pos": "noun", "ipa": "/ˈpɑːʃəz/", "vi": "các vị quan pasha Thổ Nhĩ Kỳ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041538", "hw": "peorias", "pos": "noun", "ipa": "/piˈɔːriəz/", "vi": "các thành phố Peoria", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041539", "hw": "periodicals", "pos": "noun", "ipa": "/ˌpɪriˈɑːdɪkəlz/", "vi": "các ấn phẩm định kỳ; báo tạp chí", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041540", "hw": "postmasters", "pos": "noun", "ipa": "/ˈpoʊstmæstərz/", "vi": "những người giám đốc bưu cục", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041541", "hw": "prentices", "pos": "noun", "ipa": "/ˈprɛntɪsɪz/", "vi": "những người học việc; môn sinh", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041542", "hw": "rantings", "pos": "noun", "ipa": "/ˈræntɪŋz/", "vi": "những lời huyên thuyên la lối", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041543", "hw": "saratogas", "pos": "noun", "ipa": "/ˌsærəˈtoʊɡəz/", "vi": "các vali lớn; các loài cá rồng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041544", "hw": "shockers", "pos": "noun", "ipa": "/ˈʃɑːkərz/", "vi": "những điều gây sốc; tin sửng sốt", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041545", "hw": "showrooms", "pos": "noun", "ipa": "/ˈʃoʊruːmz/", "vi": "các phòng trưng bày sản phẩm", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041546", "hw": "soggier", "pos": "adj", "ipa": "/ˈsɑːɡiər/", "vi": "sũng nước hơn; nhớp nhúa hơn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041547", "hw": "soggiest", "pos": "adj", "ipa": "/ˈsɑːɡiɪst/", "vi": "sũng nước nhất; nhớp nhúa nhất", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041548", "hw": "specialities", "pos": "noun", "ipa": "/ˌspɛʃiˈælətiz/", "vi": "các đặc sản; những chuyên ngành", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041549", "hw": "spleens", "pos": "noun", "ipa": "/spliːnz/", "vi": "các lá lách; sự tức giận", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041550", "hw": "tays", "pos": "noun", "ipa": "/teɪz/", "vi": "các dòng sông Tay ở Scotland", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041551", "hw": "touchier", "pos": "adj", "ipa": "/ˈtʌtʃiər/", "vi": "nhạy cảm hơn; dễ nổi nóng hơn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041552", "hw": "touchiest", "pos": "adj", "ipa": "/ˈtʌtʃiɪst/", "vi": "nhạy cảm nhất; dễ nổi nóng nhất", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041553", "hw": "tranquiler", "pos": "adj", "ipa": "/ˈtræŋkwɪlər/", "vi": "yên tĩnh hơn; thanh bình hơn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041554", "hw": "tranquilest", "pos": "adj", "ipa": "/ˈtræŋkwɪlɪst/", "vi": "yên tĩnh nhất; thanh bình nhất", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041555", "hw": "whiteheads", "pos": "noun", "ipa": "/ˈwaɪthɛdz/", "vi": "các nốt mụn đầu trắng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041556", "hw": "whits", "pos": "noun", "ipa": "/wɪts/", "vi": "chút ít; mảy may; lượng rất nhỏ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041557", "hw": "yemenis", "pos": "noun", "ipa": "/ˈjɛməniz/", "vi": "những người dân Yemen", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041558", "hw": "abel tasman", "pos": "phrase", "ipa": "", "vi": "nhà hàng hải Abel Tasman", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041559", "hw": "acetate rayon", "pos": "phrase", "ipa": "", "vi": "sợi tơ nhân tạo axetat", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041560", "hw": "adipose cell", "pos": "phrase", "ipa": "", "vi": "tế bào mỡ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041561", "hw": "alluvial sediment", "pos": "phrase", "ipa": "", "vi": "trầm tích phù sa; lớp bồi tích", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041562", "hw": "american ginseng", "pos": "phrase", "ipa": "", "vi": "nhân sâm Mỹ; sâm Bắc Mỹ", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041563", "hw": "angle of refraction", "pos": "phrase", "ipa": "", "vi": "góc khúc xạ ánh sáng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041564", "hw": "artificial insemination", "pos": "phrase", "ipa": "", "vi": "thụ tinh nhân tạo", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041565", "hw": "austrian schilling", "pos": "phrase", "ipa": "", "vi": "đồng schilling nước Áo", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041566", "hw": "bawling out", "pos": "phrase", "ipa": "", "vi": "trận mắng mỏ té tát", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041567", "hw": "belarusian monetary unit", "pos": "phrase", "ipa": "", "vi": "đơn vị tiền tệ Belarus", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041568", "hw": "bengal kino", "pos": "phrase", "ipa": "", "vi": "nhựa cây kino Bengal", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041569", "hw": "beverly sills", "pos": "phrase", "ipa": "", "vi": "ca sĩ opera Beverly Sills", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041570", "hw": "big spender", "pos": "phrase", "ipa": "", "vi": "kẻ vung tay quá trán; tiêu hoang", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041571", "hw": "billiard saloon", "pos": "phrase", "ipa": "", "vi": "câu lạc bộ bi-a; quán bi-a", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041572", "hw": "cannabis sativa", "pos": "phrase", "ipa": "", "vi": "cây cần sa; cây gai dầu", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041573", "hw": "cape may warbler", "pos": "phrase", "ipa": "", "vi": "chim chích Cape May", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041574", "hw": "cartesian plane", "pos": "phrase", "ipa": "", "vi": "mặt phẳng tọa độ Descartes", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041575", "hw": "cellulose ester", "pos": "phrase", "ipa": "", "vi": "este của cellulose", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041576", "hw": "charlestown navy yard", "pos": "phrase", "ipa": "", "vi": "xưởng hải quân Charlestown", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041577", "hw": "chinese hibiscus", "pos": "phrase", "ipa": "", "vi": "cây hoa dâm bụt; bông bụt", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041578", "hw": "chromosomal anomaly", "pos": "phrase", "ipa": "", "vi": "bất thường nhiễm sắc thể", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041579", "hw": "cinco de mayo", "pos": "phrase", "ipa": "", "vi": "lễ hội Cinco de Mayo", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041580", "hw": "collared lizard", "pos": "phrase", "ipa": "", "vi": "thằn lằn có khoang cổ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041581", "hw": "conjoined twin", "pos": "phrase", "ipa": "", "vi": "cặp song sinh dính liền", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041582", "hw": "corn chowder", "pos": "phrase", "ipa": "", "vi": "súp ngô kem sữa; canh ngô", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041583", "hw": "corneal transplant", "pos": "phrase", "ipa": "", "vi": "phẫu thuật ghép giác mạc", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041584", "hw": "crown wart", "pos": "phrase", "ipa": "", "vi": "bệnh bướu rễ cỏ linh lăng", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041585", "hw": "crybaby tree", "pos": "phrase", "ipa": "", "vi": "cây vông mồng gà; cây đậu san hô", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041586", "hw": "dipole antenna", "pos": "phrase", "ipa": "", "vi": "ăng-ten lưỡng cực", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041587", "hw": "dorothy sayers", "pos": "phrase", "ipa": "", "vi": "nhà văn Dorothy L. Sayers", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041588", "hw": "double obelisk", "pos": "phrase", "ipa": "", "vi": "ký hiệu chữ thập kép; vạch kép", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041589", "hw": "economic strangulation", "pos": "phrase", "ipa": "", "vi": "bóp nghẹt nền kinh tế", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041590", "hw": "elan vital", "pos": "phrase", "ipa": "", "vi": "sinh lực sáng tạo; lực sống", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041591", "hw": "elongate leaf", "pos": "phrase", "ipa": "", "vi": "chiếc lá thon dài", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041592", "hw": "emily jane bronte", "pos": "phrase", "ipa": "", "vi": "nhà văn Emily Brontë", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041593", "hw": "epistle to titus", "pos": "phrase", "ipa": "", "vi": "Thư gửi tín hữu Titô", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041594", "hw": "erectile dysfunction", "pos": "phrase", "ipa": "", "vi": "chứng rối loạn cương dương", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041595", "hw": "euclidean geometry", "pos": "phrase", "ipa": "", "vi": "hình học Euclid phẳng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041596", "hw": "european fire salamander", "pos": "phrase", "ipa": "", "vi": "kỳ giông lửa châu Âu", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041597", "hw": "external orifice", "pos": "phrase", "ipa": "", "vi": "lỗ tiểu ngoài; miệng ngoài", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041598", "hw": "felled seam", "pos": "phrase", "ipa": "", "vi": "đường may cuốn đè", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041599", "hw": "fire salamander", "pos": "phrase", "ipa": "", "vi": "loài kỳ giông lửa", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041600", "hw": "flue pipe", "pos": "phrase", "ipa": "", "vi": "ống môi của phong cầm", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041601", "hw": "french polynesia", "pos": "phrase", "ipa": "", "vi": "xứ Polynésie thuộc Pháp", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""}
]

with open('scratch/b29_r04_raw_p1.json') as f:
    raw = json.load(f)

assert len(items) == 100, f"Expected 100 items, got {len(items)}"
allowed_pos = {'noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'}

for idx, (it, r) in enumerate(zip(items, raw)):
    assert it['id'] == r['id'], f"ID mismatch: {it['id']} vs {r['id']}"
    assert it['hw'] == r['hw'], f"HW mismatch: {it['hw']} vs {r['hw']}"
    assert it['pos'] in allowed_pos, f"Invalid POS {it['pos']} for {it['id']}"
    assert len(it['vi']) > 0, f"Empty VI for {it['id']}"
    assert len(it['vi']) <= 35, f"Invalid VI length ({len(it['vi'])}) for {it['id']}: {it['vi']}"
    if it['pos'] != 'phrase' and ' ' not in it['hw']:
        assert it['ipa'].startswith('/') and it['ipa'].endswith('/') and it['ipa'].count('/') == 2, f"Invalid IPA for {it['id']}: {it['ipa']}"

with open('scratch/b29_r04_p1.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print(f"Batch 29 Round 4 Part 1 validated and written successfully. Total items: {len(items)}")
