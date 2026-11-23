import json
import re

items = [
    {"id": "lex.en.200k.041602", "hw": "gazelle hound", "pos": "phrase", "ipa": "", "vi": "chó săn linh dương Saluki", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041603", "hw": "genus aster", "pos": "phrase", "ipa": "", "vi": "chi cúc tây Aster", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041604", "hw": "genus mya", "pos": "phrase", "ipa": "", "vi": "chi ngao cát Mya", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041605", "hw": "georg simon ohm", "pos": "phrase", "ipa": "", "vi": "nhà vật lý Georg Simon Ohm", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041606", "hw": "golden warbler", "pos": "phrase", "ipa": "", "vi": "chim chích vàng họng vàng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041607", "hw": "green mushroom pimple", "pos": "phrase", "ipa": "", "vi": "nấm mụn màu lục", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041608", "hw": "hairpin bend", "pos": "phrase", "ipa": "", "vi": "khúc cua tay áo; khúc cua gấp", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041609", "hw": "hairy golden aster", "pos": "phrase", "ipa": "", "vi": "cây cúc vàng lông mịn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041610", "hw": "heath aster", "pos": "phrase", "ipa": "", "vi": "hoa cúc thạch thảo trắng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041611", "hw": "huntingdon willow", "pos": "phrase", "ipa": "", "vi": "cây liễu trắng Huntingdon", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041612", "hw": "index of refraction", "pos": "phrase", "ipa": "", "vi": "chiết suất; chỉ số khúc xạ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041613", "hw": "interstitial fluid", "pos": "phrase", "ipa": "", "vi": "dịch mô kẽ; dịch kẽ tế bào", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041614", "hw": "ionizing radiation", "pos": "phrase", "ipa": "", "vi": "bức xạ ion hóa", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041615", "hw": "james hargreaves", "pos": "phrase", "ipa": "", "vi": "nhà sáng chế James Hargreaves", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041616", "hw": "john galbraith", "pos": "phrase", "ipa": "", "vi": "nhà kinh tế John K. Galbraith", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041617", "hw": "john philip sousa", "pos": "phrase", "ipa": "", "vi": "nhạc trưởng John Philip Sousa", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041618", "hw": "jorge borges", "pos": "phrase", "ipa": "", "vi": "nhà văn Jorge Luis Borges", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041619", "hw": "juan ramon jimenez", "pos": "phrase", "ipa": "", "vi": "nhà thơ Juan Ramón Jiménez", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041620", "hw": "leper lily", "pos": "phrase", "ipa": "", "vi": "hoa chuông rằn; hoa tỳ bà", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041621", "hw": "leyte island", "pos": "phrase", "ipa": "", "vi": "đảo Leyte Philippines", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041622", "hw": "lingual vein", "pos": "phrase", "ipa": "", "vi": "tĩnh mạch dưới lưỡi", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041623", "hw": "loony bin", "pos": "phrase", "ipa": "", "vi": "bệnh viện tâm thần; nhà thương", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041624", "hw": "lorenz milton hart", "pos": "phrase", "ipa": "", "vi": "nhà viết lời bài hát Lorenz Hart", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041625", "hw": "lynx lynx", "pos": "phrase", "ipa": "", "vi": "loài linh miêu Á-Âu", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041626", "hw": "marine archeology", "pos": "phrase", "ipa": "", "vi": "ngành khảo cổ học dưới nước", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041627", "hw": "mooring mast", "pos": "phrase", "ipa": "", "vi": "trụ neo khí cầu; cột neo", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041628", "hw": "nikita khrushchev", "pos": "phrase", "ipa": "", "vi": "nhà lãnh đạo Nikita Khrushchev", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041629", "hw": "orange mushroom pimple", "pos": "phrase", "ipa": "", "vi": "nấm mụn màu cam mục gỗ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041630", "hw": "pair of tweezers", "pos": "phrase", "ipa": "", "vi": "cái nhíp; kẹp nhổ lông", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041631", "hw": "parabolic geometry", "pos": "phrase", "ipa": "", "vi": "hình học parabol", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041632", "hw": "pariah dog", "pos": "phrase", "ipa": "", "vi": "chó hoang vô chủ; chó cỏ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041633", "hw": "pistachio tree", "pos": "phrase", "ipa": "", "vi": "cây hạt dẻ cười; cây hồ trăn", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041634", "hw": "planing machine", "pos": "phrase", "ipa": "", "vi": "máy bào gỗ; máy bào kim loại", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041635", "hw": "prairie aster", "pos": "phrase", "ipa": "", "vi": "hoa cúc thảo nguyên", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041636", "hw": "premature ventricular contraction", "pos": "phrase", "ipa": "", "vi": "ngoại tâm thu thất sớm", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041637", "hw": "republic of djibouti", "pos": "phrase", "ipa": "", "vi": "Cộng hòa Djibouti", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041638", "hw": "riparian forest", "pos": "phrase", "ipa": "", "vi": "rừng ven sông suối", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041639", "hw": "riparian right", "pos": "phrase", "ipa": "", "vi": "quyền sử dụng nguồn nước ven sông", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041640", "hw": "rock outcrop", "pos": "phrase", "ipa": "", "vi": "mỏm đá lộ thiên; khối đá trồi", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041641", "hw": "roman numeral", "pos": "phrase", "ipa": "", "vi": "chữ số La Mã; số La Mã", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041642", "hw": "ruck up", "pos": "phrase", "ipa": "", "vi": "bị đùn lại; nhăn nhúm lại", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041643", "hw": "sauvignon blanc", "pos": "phrase", "ipa": "", "vi": "rượu vang nho Sauvignon Blanc", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041644", "hw": "screw auger", "pos": "phrase", "ipa": "", "vi": "mũi khoan xoắn ruột gà", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041645", "hw": "sir john suckling", "pos": "phrase", "ipa": "", "vi": "nhà thơ Sir John Suckling", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041646", "hw": "social stratification", "pos": "phrase", "ipa": "", "vi": "sự phân tầng xã hội", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041647", "hw": "sonora gum", "pos": "phrase", "ipa": "", "vi": "nhựa cây cánh kiến Sonora", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041648", "hw": "soured cream", "pos": "phrase", "ipa": "", "vi": "kem chua lên men; sốt kem chua", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041649", "hw": "strait of messina", "pos": "phrase", "ipa": "", "vi": "eo biển Messina", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041650", "hw": "stratified language", "pos": "phrase", "ipa": "", "vi": "ngôn ngữ phân tầng xã hội", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041651", "hw": "takeover arbitrage", "pos": "phrase", "ipa": "", "vi": "kinh doanh chênh lệch mua lại", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041652", "hw": "teresa of avila", "pos": "phrase", "ipa": "", "vi": "Thánh nữ Têrêsa Avila", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041653", "hw": "toothache tree", "pos": "phrase", "ipa": "", "vi": "cây tiêu gai tê lưỡi", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041654", "hw": "total hysterectomy", "pos": "phrase", "ipa": "", "vi": "cắt bỏ tử cung toàn phần", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041655", "hw": "trimmer arch", "pos": "phrase", "ipa": "", "vi": "vòm gạch đỡ ống khói", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041656", "hw": "trouser cuff", "pos": "phrase", "ipa": "", "vi": "gấu quần gấp; gấu lật ống quần", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041657", "hw": "turnip cabbage", "pos": "phrase", "ipa": "", "vi": "củ su hào; bắp cải su", "cefr": "A2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041658", "hw": "typographical error", "pos": "phrase", "ipa": "", "vi": "lỗi in ấn; lỗi đánh máy", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041659", "hw": "uncle remus", "pos": "phrase", "ipa": "", "vi": "nhân vật bác Remus", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041660", "hw": "vertebral vein", "pos": "phrase", "ipa": "", "vi": "tĩnh mạch đốt sống", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041661", "hw": "volga river", "pos": "phrase", "ipa": "", "vi": "dòng sông Volga", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041662", "hw": "wheat scab", "pos": "phrase", "ipa": "", "vi": "bệnh khô vằn hạt lúa mì", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041663", "hw": "white prairie aster", "pos": "phrase", "ipa": "", "vi": "cúc thảo nguyên hoa trắng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041664", "hw": "willamette river", "pos": "phrase", "ipa": "", "vi": "dòng sông Willamette", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041665", "hw": "willow aster", "pos": "phrase", "ipa": "", "vi": "hoa cúc cánh liễu dại", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041666", "hw": "yellow warbler", "pos": "phrase", "ipa": "", "vi": "chim chích vàng Bắc Mỹ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041667", "hw": "abodes", "pos": "noun", "ipa": "/əˈboʊdz/", "vi": "các nơi ở; những chốn cư ngụ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041668", "hw": "abominations", "pos": "noun", "ipa": "/əˌbɑːmɪˈneɪʃənz/", "vi": "những điều kinh tởm gớm ghiếc", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041669", "hw": "allotments", "pos": "noun", "ipa": "/əˈlɑːtmənts/", "vi": "các phần chia; mảnh đất thuê nhỏ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041670", "hw": "arieses", "pos": "noun", "ipa": "/ˈɛəriːzɪz/", "vi": "người thuộc cung Bạch Dương", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041671", "hw": "bharats", "pos": "noun", "ipa": "/ˈbɑːrəts/", "vi": "các danh xưng Bharat Ấn Độ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041672", "hw": "cfos", "pos": "noun", "ipa": "/ˌsiːɛfˈoʊz/", "vi": "các giám đốc tài chính CFO", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041673", "hw": "chipotles", "pos": "noun", "ipa": "/tʃɪˈpoʊtleɪz/", "vi": "các quả ớt hiểm hun khói", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041674", "hw": "choreographers", "pos": "noun", "ipa": "/ˌkɔːriˈɑːɡrəfərz/", "vi": "các biên đạo múa; nhà dàn dựng", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041675", "hw": "commotions", "pos": "noun", "ipa": "/kəˈmoʊʃənz/", "vi": "các cuộc náo động; sự xáo trộn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041676", "hw": "concierges", "pos": "noun", "ipa": "/koʊnsiˈɛrʒɪz/", "vi": "những người hỗ trợ khách sạn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041677", "hw": "denominators", "pos": "noun", "ipa": "/dɪˈnɑːmɪneɪtərz/", "vi": "các mẫu số toán học", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041678", "hw": "dopplers", "pos": "noun", "ipa": "/ˈdɑːplərz/", "vi": "các thiết bị siêu âm Doppler", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041679", "hw": "dowries", "pos": "noun", "ipa": "/ˈdaʊriz/", "vi": "các của hồi môn; của thách cưới", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041680", "hw": "duplexes", "pos": "noun", "ipa": "/ˈduːplɛksɪz/", "vi": "các căn nhà song lập; căn hộ đôi", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041681", "hw": "ects", "pos": "noun", "ipa": "/ˌiːsiːˈtiːz/", "vi": "các ca liệu pháp sốc điện", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041682", "hw": "etchings", "pos": "noun", "ipa": "/ˈɛtʃɪŋz/", "vi": "các bản khắc axit; tranh in kẽm", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041683", "hw": "exterminations", "pos": "noun", "ipa": "/ɪkˌstɜːrmɪˈneɪʃənz/", "vi": "những cuộc tận diệt; sự triệt hạ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041684", "hw": "eyres", "pos": "noun", "ipa": "/ˈɛərz/", "vi": "các tòa án lưu động cổ nước Anh", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041685", "hw": "fatimas", "pos": "noun", "ipa": "/ˈfætɪməz/", "vi": "những người tên Fatima", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041686", "hw": "flotations", "pos": "noun", "ipa": "/floʊˈteɪʃənz/", "vi": "các đợt chào bán cổ phiếu; nổi", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041687", "hw": "forewords", "pos": "noun", "ipa": "/ˈfɔːrwərdz/", "vi": "các lời tựa; những lời tựa đầu", "cefr": "B1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041688", "hw": "grandchildren", "pos": "noun", "ipa": "/ˈɡræntʃɪldrən/", "vi": "các cháu nội ngoại", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041689", "hw": "harems", "pos": "noun", "ipa": "/ˈhɑːrəmz/", "vi": "các hậu cung; các cung tần", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041690", "hw": "himalayases", "pos": "noun", "ipa": "/ˌhɪməˈleɪəzɪz/", "vi": "các rặng núi dãy Himalaya hùng vĩ", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041691", "hw": "hippos", "pos": "noun", "ipa": "/ˈhɪpoʊz/", "vi": "những con hà mã", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041692", "hw": "hypnotics", "pos": "noun", "ipa": "/hɪpˈnɑːtɪks/", "vi": "các loại thuốc an thần gây ngủ", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041693", "hw": "incubators", "pos": "noun", "ipa": "/ˈɪŋkjəbeɪtərz/", "vi": "lồng ấp trẻ sơ sinh; lò ấp trứng", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041694", "hw": "jurors", "pos": "noun", "ipa": "/ˈdʒʊrərz/", "vi": "các thành viên bồi thẩm đoàn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041695", "hw": "kilos", "pos": "noun", "ipa": "/ˈkiːloʊz/", "vi": "các cân; những ki-lô-gam", "cefr": "A1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041696", "hw": "kvs", "pos": "noun", "ipa": "/ˌkeɪˈviːz/", "vi": "các kilovolt; các đơn vị kV", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041697", "hw": "lati", "pos": "noun", "ipa": "/ˈlɑːtiː/", "vi": "các đồng lats tiền Latvia", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041698", "hw": "latu", "pos": "noun", "ipa": "/ˈlɑːtuː/", "vi": "đồng tiền latu Latvia", "cefr": "C1", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041699", "hw": "lockouts", "pos": "noun", "ipa": "/ˈlɑːkaʊts/", "vi": "các cuộc đóng cửa xưởng biểu tình", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041700", "hw": "lubed", "pos": "verb", "ipa": "/luːbd/", "vi": "đã bôi trơn; đã tra dầu nhờn", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""},
    {"id": "lex.en.200k.041701", "hw": "lubes", "pos": "noun", "ipa": "/luːbz/", "vi": "các chất bôi trơn; dầu nhớt", "cefr": "B2", "tier": "expanded", "status": "reviewed", "notes": ""}
]

with open('scratch/b29_r04_raw_p2.json') as f:
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

with open('scratch/b29_r04_p2.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print(f"Batch 29 Round 4 Part 2 validated and written successfully. Total items: {len(items)}")
