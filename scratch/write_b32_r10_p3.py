import json

items = [
  {"id": "lex.en.200k.059703", "hw": "rhus dermatitis", "pos": "phrase", "ipa": "/rʊs ˌdɜːrməˈtaɪtɪs/", "vi": "viêm da do tiếp xúc sơn độc Rhus"},
  {"id": "lex.en.200k.059704", "hw": "rima oris", "pos": "phrase", "ipa": "/ˈraɪmə ˈɔːrɪs/", "vi": "khe miệng giữa hai bờ môi"},
  {"id": "lex.en.200k.059705", "hw": "rutabaga plant", "pos": "phrase", "ipa": "/ˌruːtəˈbeɪɡə plænt/", "vi": "cây cải củ Thụy Điển rutabaga"},
  {"id": "lex.en.200k.059706", "hw": "sauropod dinosaur", "pos": "phrase", "ipa": "/ˈsɔːrəpɑːd ˈdaɪnəsɔːr/", "vi": "khủng long chân thằn lằn ăn cỏ"},
  {"id": "lex.en.200k.059707", "hw": "seafood newburg", "pos": "phrase", "ipa": "/ˈsiːfuːd ˈnuːbɜːrɡ/", "vi": "món hải sản sốt kem bơ Newburg"},
  {"id": "lex.en.200k.059708", "hw": "shatterproof glass", "pos": "phrase", "ipa": "/ˈʃætərpruːf ɡlæs/", "vi": "kính an toàn chống vỡ vụn"},
  {"id": "lex.en.200k.059709", "hw": "shrimp newburg", "pos": "phrase", "ipa": "/ʃrɪmp ˈnuːbɜːrɡ/", "vi": "món tôm sốt kem bơ Newburg"},
  {"id": "lex.en.200k.059710", "hw": "solan goose", "pos": "phrase", "ipa": "/ˈsoʊlən ɡuːs/", "vi": "loài chim điên biển phương bắc"},
  {"id": "lex.en.200k.059711", "hw": "spark arrester", "pos": "phrase", "ipa": "/spɑːrk əˈrɛstər/", "vi": "thiết bị dập tàn lửa ống khói"},
  {"id": "lex.en.200k.059712", "hw": "spike arrester", "pos": "phrase", "ipa": "/spaɪk əˈrɛstər/", "vi": "bộ triệt xung điện đột biến"},
  {"id": "lex.en.200k.059713", "hw": "succinic acid", "pos": "phrase", "ipa": "/səkˈsɪnɪk ˈæsɪd/", "vi": "axit hổ phách axit succinic"},
  {"id": "lex.en.200k.059714", "hw": "sulphur hexafluoride", "pos": "phrase", "ipa": "/ˈsʌlfər ˌhɛksəˈflʊəraɪd/", "vi": "khí cách điện lưu huỳnh SF6"},
  {"id": "lex.en.200k.059715", "hw": "sweet calamus", "pos": "phrase", "ipa": "/swiːt ˈkæləməs/", "vi": "cây thủy xương bồ thơm"},
  {"id": "lex.en.200k.059716", "hw": "swizzle stick", "pos": "phrase", "ipa": "/ˈswɪzl stɪk/", "vi": "que khuấy cocktail rượu"},
  {"id": "lex.en.200k.059717", "hw": "thermionic emission", "pos": "phrase", "ipa": "/ˌθɜːrmiˈɑːnɪk ɪˈmɪʃən/", "vi": "hiện tượng phát xạ nhiệt electron"},
  {"id": "lex.en.200k.059718", "hw": "thiamine pyrophosphate", "pos": "phrase", "ipa": "/ˈθaɪəmɪn ˌpaɪroʊˈfɑːsfeɪt/", "vi": "coenzym thiamine pyrophosphate"},
  {"id": "lex.en.200k.059719", "hw": "tolu balsam", "pos": "phrase", "ipa": "/toʊˈluː ˈbɔːlsəm/", "vi": "nhựa thơm tolu làm dược liệu"},
  {"id": "lex.en.200k.059720", "hw": "tolu balsam tree", "pos": "phrase", "ipa": "/toʊˈluː ˈbɔːlsəm triː/", "vi": "cây lấy nhựa thơm tolu Nam Mỹ"},
  {"id": "lex.en.200k.059721", "hw": "variola major", "pos": "phrase", "ipa": "/vəˈraɪələ ˈmeɪdʒər/", "vi": "chủng vi-rút đậu mùa thể nặng"},
  {"id": "lex.en.200k.059722", "hw": "variola major virus", "pos": "phrase", "ipa": "/vəˈraɪələ ˈmeɪdʒər ˈvaɪrəs/", "vi": "vi-rút gây bệnh đậu mùa ác tính"},
  {"id": "lex.en.200k.059723", "hw": "variola minor", "pos": "phrase", "ipa": "/vəˈraɪələ ˈmaɪnər/", "vi": "chủng vi-rút đậu mùa thể nhẹ"},
  {"id": "lex.en.200k.059724", "hw": "variola minor virus", "pos": "phrase", "ipa": "/vəˈraɪələ ˈmaɪnər ˈvaɪrəs/", "vi": "vi-rút gây bệnh đậu mùa nhẹ"},
  {"id": "lex.en.200k.059725", "hw": "variola vaccine", "pos": "phrase", "ipa": "/vəˈraɪələ vækˈsiːn/", "vi": "vắc-xin phòng ngừa bệnh đậu mùa"},
  {"id": "lex.en.200k.059726", "hw": "variola virus", "pos": "phrase", "ipa": "/vəˈraɪələ ˈvaɪrəs/", "vi": "vi-rút gây bệnh đậu mùa"},
  {"id": "lex.en.200k.059727", "hw": "venial sin", "pos": "phrase", "ipa": "/ˈviːniəl sɪn/", "vi": "tội nhẹ tha thứ theo giáo lý"},
  {"id": "lex.en.200k.059728", "hw": "virginia mcmath", "pos": "phrase", "ipa": "/vərˈdʒɪnjə məkˈmæθ/", "vi": "nữ diễn viên kịch Ginger Rogers"},
  {"id": "lex.en.200k.059729", "hw": "visceral pleura", "pos": "phrase", "ipa": "/ˈvɪsərəl ˈplʊərə/", "vi": "màng phổi tạng bọc sát nhu mô"},
  {"id": "lex.en.200k.059730", "hw": "wallace carothers", "pos": "phrase", "ipa": "/ˈwɑːləs kəˈrʌðərz/", "vi": "nhà hóa học phát minh nilon"},
  {"id": "lex.en.200k.059731", "hw": "waterwheel plant", "pos": "phrase", "ipa": "/ˈwɔːtərwiːl plænt/", "vi": "cây bánh xe nước Aldrovanda"},
  {"id": "lex.en.200k.059732", "hw": "whitlow grass", "pos": "phrase", "ipa": "/ˈwɪtloʊ ɡræs/", "vi": "cỏ hoa trắng đực Draba verna"},
  {"id": "lex.en.200k.059733", "hw": "wild hollyhock", "pos": "phrase", "ipa": "/waɪld ˈhɑːlihɑːk/", "vi": "cây hoa thục quỳ dại thảo nguyên"},
  {"id": "lex.en.200k.059734", "hw": "yerba mansa", "pos": "phrase", "ipa": "/ˌjɛərbə ˈmænsə/", "vi": "cây dược liệu đầm lầy yerba mansa"},
  {"id": "lex.en.200k.059735", "hw": "adoptees", "pos": "noun", "ipa": "/ədˈɑptˈiz/", "vi": "người con nuôi được nhận nuôi"},
  {"id": "lex.en.200k.059736", "hw": "akhenatens", "pos": "noun", "ipa": "/ˌɑːkəˈnɑːtənz/", "vi": "Pharaon Akhenaten tôn giáo"},
  {"id": "lex.en.200k.059737", "hw": "ampersands", "pos": "noun", "ipa": "/ˈæmpərsændz/", "vi": "ký tự dấu và ampersand"},
  {"id": "lex.en.200k.059738", "hw": "astragali", "pos": "noun", "ipa": "/æstrˈæɡəlaɪ/", "vi": "các xương sên ở cổ chân"},
  {"id": "lex.en.200k.059739", "hw": "astragaluses", "pos": "noun", "ipa": "/æstrˈæɡələsɪz/", "vi": "cây thuốc hoàng kỳ; xương sên"},
  {"id": "lex.en.200k.059740", "hw": "bailees", "pos": "noun", "ipa": "/beɪlˈiːz/", "vi": "người nhận giữ đồ ký gửi ủy thác"},
  {"id": "lex.en.200k.059741", "hw": "barques", "pos": "noun", "ipa": "/bˈɑːrks/", "vi": "thuyền buồm ba cột kiểu barque"},
  {"id": "lex.en.200k.059742", "hw": "beeriest", "pos": "adj", "ipa": "/bˈɪəriɪst/", "vi": "nồng nặc mùi men bia nhất"},
  {"id": "lex.en.200k.059743", "hw": "bonbons", "pos": "noun", "ipa": "/bˈɑːnbɑːnz/", "vi": "viên kẹo sô-cô-la nhân mềm"},
  {"id": "lex.en.200k.059744", "hw": "brahmanas", "pos": "noun", "ipa": "/brˈɑːmənəz/", "vi": "kinh văn giải nghĩa Bà-la-môn"},
  {"id": "lex.en.200k.059745", "hw": "brahmaputras", "pos": "noun", "ipa": "/ˌbrɑːməpˈuːtrəz/", "vi": "dòng sông lớn Brahmaputra"},
  {"id": "lex.en.200k.059746", "hw": "calvadoses", "pos": "noun", "ipa": "/kˌælvədˈoʊsɪz/", "vi": "rượu táo chưng cất Calvados"},
  {"id": "lex.en.200k.059747", "hw": "ceros", "pos": "noun", "ipa": "/sˈɪəroʊz/", "vi": "loài cá thu cero đốm vàng"},
  {"id": "lex.en.200k.059748", "hw": "chestier", "pos": "adj", "ipa": "/tʃˈɛstiɚ/", "vi": "ngực nở nang hơn; giọng khàn hơn"},
  {"id": "lex.en.200k.059749", "hw": "chestiest", "pos": "adj", "ipa": "/tʃˈɛstiɪst/", "vi": "ngực nở nang nhất; giọng khàn nhất"},
  {"id": "lex.en.200k.059750", "hw": "clapboarded", "pos": "verb", "ipa": "/klˈæpbɔːrdɪd/", "vi": "đã đóng ván lợp che tường"},
  {"id": "lex.en.200k.059751", "hw": "clapboarding", "pos": "verb", "ipa": "/klˈæpbɔːrdɪŋ/", "vi": "việc đóng ốp ván gỗ chồng mép"},
  {"id": "lex.en.200k.059752", "hw": "clapboards", "pos": "noun", "ipa": "/klˈæpbˌɔrdz/", "vi": "tấm ván gỗ ốp tường chồng mí"},
  {"id": "lex.en.200k.059753", "hw": "colonizers", "pos": "noun", "ipa": "/kˈɑlənˌaɪzɚz/", "vi": "kẻ đi xâm chiếm lập thuộc địa"},
  {"id": "lex.en.200k.059754", "hw": "colophons", "pos": "noun", "ipa": "/kˈɑːləfɑːnz/", "vi": "trang ghi thông tin xuất bản sách"},
  {"id": "lex.en.200k.059755", "hw": "comedowns", "pos": "noun", "ipa": "/kˈʌmdaʊnz/", "vi": "sự sa sút thất vọng; hụt hẫng"},
  {"id": "lex.en.200k.059756", "hw": "compositors", "pos": "noun", "ipa": "/kəmpˈɑːzətɚz/", "vi": "thợ sắp chữ xếp bản in"},
  {"id": "lex.en.200k.059757", "hw": "cottontails", "pos": "noun", "ipa": "/kˈɑːtnteɪlz/", "vi": "loài thỏ đuôi bông Bắc Mỹ"},
  {"id": "lex.en.200k.059758", "hw": "cowhides", "pos": "noun", "ipa": "/kˈaʊhaɪdz/", "vi": "tấm da bò thuộc; roi da bò"},
  {"id": "lex.en.200k.059759", "hw": "crosswinds", "pos": "noun", "ipa": "/krˈɔːswɪndz/", "vi": "luồng gió thổi ngang đường bay"},
  {"id": "lex.en.200k.059760", "hw": "dachas", "pos": "noun", "ipa": "/dˈɑːtʃəz/", "vi": "nhà nghỉ ngoại ô nông thôn Nga"},
  {"id": "lex.en.200k.059761", "hw": "daturas", "pos": "noun", "ipa": "/dətˈʊərəz/", "vi": "chi thực vật cây cà độc dược"},
  {"id": "lex.en.200k.059762", "hw": "denizens", "pos": "noun", "ipa": "/dˈɛnəzənz/", "vi": "cư dân ngụ cư; sinh vật bản địa"},
  {"id": "lex.en.200k.059763", "hw": "directionalities", "pos": "noun", "ipa": "/dɪˌrɛkʃənˈælətiz/", "vi": "tính định hướng trong không gian"},
  {"id": "lex.en.200k.059764", "hw": "dniepers", "pos": "noun", "ipa": "/dnˈiːpɚz/", "vi": "dòng sông Dnieper ở Đông Âu"},
  {"id": "lex.en.200k.059765", "hw": "druggists", "pos": "noun", "ipa": "/drˈʌɡəsts/", "vi": "dược sĩ nhà thuốc; người bào chế"},
  {"id": "lex.en.200k.059766", "hw": "elands", "pos": "noun", "ipa": "/ˈiːləndz/", "vi": "loài linh dương lớn eland"},
  {"id": "lex.en.200k.059767", "hw": "enticements", "pos": "noun", "ipa": "/ɪntˈaɪsmənts/", "vi": "sự cám dỗ mời gọi; mồi nhử"},
  {"id": "lex.en.200k.059768", "hw": "epiruses", "pos": "noun", "ipa": "/ɛpˈaɪrəsɪz/", "vi": "vùng đất cổ Epirus ở Hy Lạp"},
  {"id": "lex.en.200k.059769", "hw": "euphorbias", "pos": "noun", "ipa": "/juːfˈɔːrbiəz/", "vi": "chi thực vật đại kích mủ trắng"},
  {"id": "lex.en.200k.059770", "hw": "explications", "pos": "noun", "ipa": "/ˌɛksplɪkˈeɪʃənz/", "vi": "sự giảng giải cặn kẽ ý nghĩa"},
  {"id": "lex.en.200k.059771", "hw": "factoids", "pos": "noun", "ipa": "/fˈæktoɪdz/", "vi": "mẩu tin vụn vặt; tin ngụy tạo"},
  {"id": "lex.en.200k.059772", "hw": "flintlocks", "pos": "noun", "ipa": "/flˈɪntlˌɑks/", "vi": "súng hỏa mai bắn đá lửa xưa"},
  {"id": "lex.en.200k.059773", "hw": "floes", "pos": "noun", "ipa": "/flˈoʊz/", "vi": "mảng băng trôi dạt trên biển"},
  {"id": "lex.en.200k.059774", "hw": "fusiliers", "pos": "noun", "ipa": "/fjˌuːzəlˈɪərz/", "vi": "lính bộ binh trang bị súng kíp"},
  {"id": "lex.en.200k.059775", "hw": "galoises", "pos": "noun", "ipa": "/ɡælˈwɑːz/", "vi": "nhà toán học Évariste Galois"},
  {"id": "lex.en.200k.059776", "hw": "gonadotropins", "pos": "noun", "ipa": "/ɡoʊnˌædətrˈoʊpɪnz/", "vi": "hoóc-môn hướng sinh dục tuyến yên"},
  {"id": "lex.en.200k.059777", "hw": "gynecomastias", "pos": "noun", "ipa": "/ˌɡaɪnɪkoʊmˈæstiəz/", "vi": "chứng phì đại tuyến vú ở nam giới"},
  {"id": "lex.en.200k.059778", "hw": "haircares", "pos": "noun", "ipa": "/hˈɛərkɛərz/", "vi": "sản phẩm chăm sóc nuôi dưỡng tóc"},
  {"id": "lex.en.200k.059779", "hw": "heracliti", "pos": "noun", "ipa": "/ˌhɛrəklˈaɪtaɪ/", "vi": "triết gia dòng chảy Heraclitus"},
  {"id": "lex.en.200k.059780", "hw": "iconoclasts", "pos": "noun", "ipa": "/aɪkˈɑːnəklæsts/", "vi": "người đập phá tượng thần cổ"},
  {"id": "lex.en.200k.059781", "hw": "inkwells", "pos": "noun", "ipa": "/ˈɪŋkwɛlz/", "vi": "lọ đựng mực viết chấm ngòi bút"},
  {"id": "lex.en.200k.059782", "hw": "insoles", "pos": "noun", "ipa": "/ˈɪnsoʊlz/", "vi": "miếng lót đệm bên trong giày"},
  {"id": "lex.en.200k.059783", "hw": "internationalisations", "pos": "noun", "ipa": "/ˌɪntərnæʃənəlaɪzˈeɪʃənz/", "vi": "quá trình quốc tế hóa hoạt động"},
  {"id": "lex.en.200k.059784", "hw": "ipecacs", "pos": "noun", "ipa": "/ˈɪpɪkæks/", "vi": "rễ cây thuốc gây nôn ipeca"},
  {"id": "lex.en.200k.059785", "hw": "jackdaws", "pos": "noun", "ipa": "/dʒˈækdɔːz/", "vi": "loài chim quạ gáy xám jackdaw"},
  {"id": "lex.en.200k.059786", "hw": "karelias", "pos": "noun", "ipa": "/kərˈiːliəz/", "vi": "vùng đất biên giới Karelia"},
  {"id": "lex.en.200k.059787", "hw": "kisumus", "pos": "noun", "ipa": "/kɪsˈuːmuːz/", "vi": "thành phố Kisumu của Kenya"},
  {"id": "lex.en.200k.059788", "hw": "kleists", "pos": "noun", "ipa": "/klˈaɪsts/", "vi": "nhà viết kịch Heinrich Kleist"},
  {"id": "lex.en.200k.059789", "hw": "lactases", "pos": "noun", "ipa": "/lˈækteɪsɪz/", "vi": "men enzym tiêu hóa đường sữa"},
  {"id": "lex.en.200k.059790", "hw": "lardners", "pos": "noun", "ipa": "/lˈɑːrdnɚz/", "vi": "nhà văn châm biếm Ring Lardner"},
  {"id": "lex.en.200k.059791", "hw": "lectors", "pos": "noun", "ipa": "/lˈɛktɚz/", "vi": "người đọc bài phụng vụ thánh lễ"},
  {"id": "lex.en.200k.059792", "hw": "levantines", "pos": "noun", "ipa": "/lˈɛvəntaɪnz/", "vi": "người dân vùng đất Levant"},
  {"id": "lex.en.200k.059793", "hw": "limans", "pos": "noun", "ipa": "/lˈaɪmənz/", "vi": "vụng biển cửa sông đầm phá liman"},
  {"id": "lex.en.200k.059794", "hw": "lofotens", "pos": "noun", "ipa": "/loʊfˈoʊtənz/", "vi": "quần đảo Lofoten ngoạn mục Na Uy"},
  {"id": "lex.en.200k.059795", "hw": "lxxes", "pos": "noun", "ipa": "/ˌɛlɛksˈɛksɪz/", "vi": "bản dịch Kinh Thánh Bảy Mươi LXX"},
  {"id": "lex.en.200k.059796", "hw": "maraschinos", "pos": "noun", "ipa": "/ˌmærəskˈiːnoʊz/", "vi": "quả anh đào ngâm rượu maraschino"},
  {"id": "lex.en.200k.059797", "hw": "matamoroses", "pos": "noun", "ipa": "/mˌætəmˈɔːroʊsɪz/", "vi": "thành phố Matamoros ở Mexico"},
  {"id": "lex.en.200k.059798", "hw": "mauritians", "pos": "noun", "ipa": "/mɔːrˈɪʃənz/", "vi": "người dân quốc đảo Mauritius"},
  {"id": "lex.en.200k.059799", "hw": "midbrains", "pos": "noun", "ipa": "/mˈɪdbreɪnz/", "vi": "phần não giữa trung não"},
  {"id": "lex.en.200k.059800", "hw": "milliliters", "pos": "noun", "ipa": "/mˈɪləlˌitɚz/", "vi": "đơn vị thể tích mi-li-lít ml"},
  {"id": "lex.en.200k.059801", "hw": "molluscs", "pos": "noun", "ipa": "/mˈɑːləsks/", "vi": "động vật thân mềm ngành nhuyễn thể"},
  {"id": "lex.en.200k.059802", "hw": "novelizations", "pos": "noun", "ipa": "/nˌɑːvəlaɪzˈeɪʃənz/", "vi": "tác phẩm chuyển thành tiểu thuyết"}
]

with open('scratch/b32_r10_raw_p3.json') as f:
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

with open('scratch/b32_r10_p3.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Part 3 validated and written successfully.")
