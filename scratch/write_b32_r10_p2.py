import json

items = [
  {"id": "lex.en.200k.059603", "hw": "ottumwas", "pos": "noun", "ipa": "/ɑːtˈʌmwəz/", "vi": "thành phố Ottumwa bang Iowa"},
  {"id": "lex.en.200k.059604", "hw": "pangeas", "pos": "noun", "ipa": "/pændʒˈiːəz/", "vi": "siêu lục địa nguyên thủy Pangea"},
  {"id": "lex.en.200k.059605", "hw": "parolees", "pos": "noun", "ipa": "/pɚˌoʊlˈiz/", "vi": "người mãn hạn tù có điều kiện"},
  {"id": "lex.en.200k.059606", "hw": "patrocluses", "pos": "noun", "ipa": "/pətrˈoʊkləsɪz/", "vi": "dũng tướng Patroclus thành Troy"},
  {"id": "lex.en.200k.059607", "hw": "peloponneses", "pos": "noun", "ipa": "/ˌpɛləpəˈniːsɪz/", "vi": "bán đảo Peloponnese của Hy Lạp"},
  {"id": "lex.en.200k.059608", "hw": "pentameters", "pos": "noun", "ipa": "/pɛntˈæmɪtɚz/", "vi": "thể thơ năm nhịp ngũ đoạn"},
  {"id": "lex.en.200k.059609", "hw": "pentobarbitals", "pos": "noun", "ipa": "/pˌɛntoʊbˈɑːrbɪtɑːlz/", "vi": "thuốc an thần pentobarbital"},
  {"id": "lex.en.200k.059610", "hw": "pincushions", "pos": "noun", "ipa": "/pˈɪnkʊʃənz/", "vi": "gối cắm kim khâu; đệm ghim kim"},
  {"id": "lex.en.200k.059611", "hw": "poncas", "pos": "noun", "ipa": "/pˈɑːŋkəz/", "vi": "người bản địa da đỏ Ponca"},
  {"id": "lex.en.200k.059612", "hw": "pones", "pos": "noun", "ipa": "/pˈoʊnz/", "vi": "bánh bột ngô nướng hình thoi"},
  {"id": "lex.en.200k.059613", "hw": "poorhouses", "pos": "noun", "ipa": "/pˈʊrhaʊsɪz/", "vi": "nhà tế bần nuôi người nghèo khó"},
  {"id": "lex.en.200k.059614", "hw": "portcullises", "pos": "noun", "ipa": "/pɔːrtkˈʌlɪsɪz/", "vi": "cửa sập bằng sắt ở cổng thành"},
  {"id": "lex.en.200k.059615", "hw": "preened", "pos": "verb", "ipa": "/prˈind/", "vi": "đã rỉa lông chuốt sắc; diện"},
  {"id": "lex.en.200k.059616", "hw": "preening", "pos": "verb", "ipa": "/prˈinɪŋ/", "vi": "đang rỉa lông; chăm chút vẻ ngoài"},
  {"id": "lex.en.200k.059617", "hw": "preens", "pos": "verb", "ipa": "/prˈiːnz/", "vi": "rỉa lông mượt mà; diện chải chuốt"},
  {"id": "lex.en.200k.059618", "hw": "presuppositions", "pos": "noun", "ipa": "/ˌpriːsʌpəzˈɪʃənz/", "vi": "tiền giả định; tiền đề ngầm định"},
  {"id": "lex.en.200k.059619", "hw": "privations", "pos": "noun", "ipa": "/praɪvˈeɪʃənz/", "vi": "cảnh túng thiếu kham khổ; cơ cực"},
  {"id": "lex.en.200k.059620", "hw": "prompters", "pos": "noun", "ipa": "/prˈɑːmptɚz/", "vi": "máy nhắc chữ; người nhắc tuồng"},
  {"id": "lex.en.200k.059621", "hw": "rameseses", "pos": "noun", "ipa": "/rˈæməsiːzɪz/", "vi": "các Pharaon Ramses Ai Cập"},
  {"id": "lex.en.200k.059622", "hw": "reaffirmations", "pos": "noun", "ipa": "/riːˌæfərmˈeɪʃənz/", "vi": "sự tái khẳng định; xác nhận lại"},
  {"id": "lex.en.200k.059623", "hw": "recalculated", "pos": "verb", "ipa": "/rikˈælkjəlˌeɪtɪd/", "vi": "đã tính toán lại số liệu"},
  {"id": "lex.en.200k.059624", "hw": "recalculates", "pos": "verb", "ipa": "/riːkˈælkjəleɪts/", "vi": "tính toán lại các giá trị"},
  {"id": "lex.en.200k.059625", "hw": "recalculating", "pos": "verb", "ipa": "/rikˈælkjəlˌeɪtɪŋ/", "vi": "đang tính toán lại số liệu"},
  {"id": "lex.en.200k.059626", "hw": "relicts", "pos": "noun", "ipa": "/rˈɛlɪkts/", "vi": "sinh vật tàn dư cổ sinh thái sót"},
  {"id": "lex.en.200k.059627", "hw": "rfds", "pos": "noun", "ipa": "/ˌɑːrɛfdˈiːz/", "vi": "dịch vụ giao thư nông thôn RFD"},
  {"id": "lex.en.200k.059628", "hw": "rostocks", "pos": "noun", "ipa": "/rˈɑːstɑːks/", "vi": "thành phố cảng Rostock nước Đức"},
  {"id": "lex.en.200k.059629", "hw": "rozelles", "pos": "noun", "ipa": "/roʊzˈɛlz/", "vi": "cây bụp giấm atiso đỏ chua"},
  {"id": "lex.en.200k.059630", "hw": "sallower", "pos": "adj", "ipa": "/sˈæloʊɚ/", "vi": "xanh xao vàng vọt hơn"},
  {"id": "lex.en.200k.059631", "hw": "sallowest", "pos": "adj", "ipa": "/sˈæloʊɪst/", "vi": "xanh xao vàng vọt nhất"},
  {"id": "lex.en.200k.059632", "hw": "secondments", "pos": "noun", "ipa": "/sɪkˈɑːndmənts/", "vi": "sự biệt phái luân chuyển công tác"},
  {"id": "lex.en.200k.059633", "hw": "serest", "pos": "adj", "ipa": "/sˈɪərɪst/", "vi": "khô cằn nứt nẻ nhất; tàn héo nhất"},
  {"id": "lex.en.200k.059634", "hw": "snowplows", "pos": "noun", "ipa": "/snˈoʊplˌaʊz/", "vi": "xe ủi gạt tuyết mặt đường"},
  {"id": "lex.en.200k.059635", "hw": "sociolinguisticses", "pos": "noun", "ipa": "/ˌsoʊsioʊlɪŋɡwˈɪstɪksɪz/", "vi": "ngành xã hội ngôn ngữ học"},
  {"id": "lex.en.200k.059636", "hw": "streptomyceses", "pos": "noun", "ipa": "/strˌɛptoʊmˈaɪsiːsɪz/", "vi": "chi xạ khuẩn sinh streptomyces"},
  {"id": "lex.en.200k.059637", "hw": "stymied", "pos": "verb", "ipa": "/stˈaɪmid/", "vi": "đã làm bế tắc; cản trở đứng hình"},
  {"id": "lex.en.200k.059638", "hw": "stymieing", "pos": "verb", "ipa": "/stˈaɪmiɪŋ/", "vi": "đang cản trở; gây thế bí tắc"},
  {"id": "lex.en.200k.059639", "hw": "stymies", "pos": "noun", "ipa": "/stˈaɪmiz/", "vi": "thế bế tắc; tình thế cản trở"},
  {"id": "lex.en.200k.059640", "hw": "stymying", "pos": "verb", "ipa": "/stˈaɪmiɪŋ/", "vi": "gây khó dễ; cản trở ngáng đường"},
  {"id": "lex.en.200k.059641", "hw": "suomis", "pos": "noun", "ipa": "/swˈoʊmiz/", "vi": "đất nước Phần Lan Suomi"},
  {"id": "lex.en.200k.059642", "hw": "swales", "pos": "noun", "ipa": "/swˈeɪlz/", "vi": "vùng mương trũng dẫn thoát nước"},
  {"id": "lex.en.200k.059643", "hw": "thds", "pos": "noun", "ipa": "/θˌiːeɪtʃdˈiːz/", "vi": "bằng tiến sĩ thần học ThD"},
  {"id": "lex.en.200k.059644", "hw": "thebans", "pos": "noun", "ipa": "/θˈiːbənz/", "vi": "người dân thành bang cổ Thebes"},
  {"id": "lex.en.200k.059645", "hw": "themises", "pos": "noun", "ipa": "/θˈiːmɪsɪz/", "vi": "nữ thần công lý Themis Hy Lạp"},
  {"id": "lex.en.200k.059646", "hw": "thermocouples", "pos": "noun", "ipa": "/θˈɜːrmoʊkˌʌpəlz/", "vi": "cặp nhiệt điện đo nhiệt độ"},
  {"id": "lex.en.200k.059647", "hw": "thzes", "pos": "noun", "ipa": "/tˈiːeɪtʃzɛdz/", "vi": "đơn vị tần số tê-ra-héc THz"},
  {"id": "lex.en.200k.059648", "hw": "trisomies", "pos": "noun", "ipa": "/traɪsˈoʊmiz/", "vi": "đột biến thể ba nhiễm sắc thể"},
  {"id": "lex.en.200k.059649", "hw": "tsushimas", "pos": "noun", "ipa": "/tsuːʃˈiːməz/", "vi": "hải chiến eo biển Tsushima Đối Mã"},
  {"id": "lex.en.200k.059650", "hw": "virologists", "pos": "noun", "ipa": "/vɪrˈɑlədʒɪsts/", "vi": "chuyên gia nghiên cứu vi-rút học"},
  {"id": "lex.en.200k.059651", "hw": "walkovers", "pos": "noun", "ipa": "/wˈɔːkoʊvɚz/", "vi": "chiến thắng dễ không cần thi đấu"},
  {"id": "lex.en.200k.059652", "hw": "whoopees", "pos": "noun", "ipa": "/wˈuːpiːz/", "vi": "tiếng reo hoan hỉ; cuộc liên hoan"},
  {"id": "lex.en.200k.059653", "hw": "yaoundes", "pos": "noun", "ipa": "/jˌaʊndˈeɪz/", "vi": "thủ đô Yaoundé của Cameroon"},
  {"id": "lex.en.200k.059654", "hw": "alaskan malamute", "pos": "phrase", "ipa": "/əˈlæskən ˈmæləmjuːt/", "vi": "giống chó kéo xe Alaska khổng lồ"},
  {"id": "lex.en.200k.059655", "hw": "andreas vesalius", "pos": "phrase", "ipa": "/ænˈdreɪəs vɪˈseɪliəs/", "vi": "nhà giải phẫu Andreas Vesalius"},
  {"id": "lex.en.200k.059656", "hw": "anemic anoxia", "pos": "phrase", "ipa": "/əˈniːmɪk ænˈɑːksiə/", "vi": "thiếu oxy mô do thiếu máu"},
  {"id": "lex.en.200k.059657", "hw": "arrester hook", "pos": "phrase", "ipa": "/əˈrɛstər hʊk/", "vi": "móc hãm máy bay trên tàu sân bay"},
  {"id": "lex.en.200k.059658", "hw": "balsam of tolu", "pos": "phrase", "ipa": "/ˈbɔːlsəm əv toʊˈluː/", "vi": "nhựa thơm tolu làm thuốc ho"},
  {"id": "lex.en.200k.059659", "hw": "bitter aloes", "pos": "phrase", "ipa": "/ˈbɪtər ˈæloʊz/", "vi": "nhựa khô cây lô hội đắng"},
  {"id": "lex.en.200k.059660", "hw": "bowhead whale", "pos": "phrase", "ipa": "/ˈboʊhɛd weɪl/", "vi": "loài cá voi đầu cong Bắc Cực"},
  {"id": "lex.en.200k.059661", "hw": "calamus oil", "pos": "phrase", "ipa": "/ˈkæləməs ɔɪl/", "vi": "tinh dầu cây thủy xương bồ"},
  {"id": "lex.en.200k.059662", "hw": "charles taze russell", "pos": "phrase", "ipa": "/tʃɑːrlz teɪz ˈrʌsəl/", "vi": "mục sư Charles Taze Russell"},
  {"id": "lex.en.200k.059663", "hw": "chelate compound", "pos": "phrase", "ipa": "/ˈkiːleɪt ˈkɑːmpaʊnd/", "vi": "hợp chất phức vòng càng chelat"},
  {"id": "lex.en.200k.059664", "hw": "clastic rock", "pos": "phrase", "ipa": "/ˈklæstɪk rɑːk/", "vi": "đá trầm tích cơ học vụn vỡ"},
  {"id": "lex.en.200k.059665", "hw": "comminuted fracture", "pos": "phrase", "ipa": "/ˈkɑːmɪnuːtɪd ˈfræktʃər/", "vi": "vết gãy nát xương nhiều mảnh"},
  {"id": "lex.en.200k.059666", "hw": "comte de rochambeau", "pos": "phrase", "ipa": "/kɔːmt də ˌroʊʃæmˈboʊ/", "vi": "bá tước tướng quân Rochambeau"},
  {"id": "lex.en.200k.059667", "hw": "consonantal system", "pos": "phrase", "ipa": "/ˌkɑːnsəˈnæntl ˈsɪstəm/", "vi": "hệ thống các phụ âm ngôn ngữ"},
  {"id": "lex.en.200k.059668", "hw": "crna gora", "pos": "phrase", "ipa": "/tsərnɑː ˈɡɔːrə/", "vi": "quốc gia Montenegro Crna Gora"},
  {"id": "lex.en.200k.059669", "hw": "diachronic linguistics", "pos": "phrase", "ipa": "/ˌdaɪəˈkrɑːnɪk lɪŋˈɡwɪstɪks/", "vi": "ngôn ngữ học nghiên cứu lịch đại"},
  {"id": "lex.en.200k.059670", "hw": "eustachian tube", "pos": "phrase", "ipa": "/juːˈsteɪkiən tuːb/", "vi": "vòi tai thông họng Eustachius"},
  {"id": "lex.en.200k.059671", "hw": "flavian dynasty", "pos": "phrase", "ipa": "/ˈfleɪviən ˈdaɪnəsti/", "vi": "triều đại hoàng đế La Mã Flavian"},
  {"id": "lex.en.200k.059672", "hw": "genus opuntia", "pos": "phrase", "ipa": "/ˈdʒiːnəs oʊˈpʌnʃiə/", "vi": "chi xương rồng tai thỏ Opuntia"},
  {"id": "lex.en.200k.059673", "hw": "hemorrhagic septicemia", "pos": "phrase", "ipa": "/ˌhɛməˈrædʒɪk ˌsɛptɪˈsiːmiə/", "vi": "bệnh tụ huyết trùng xuất huyết"},
  {"id": "lex.en.200k.059674", "hw": "hepatic tanager", "pos": "phrase", "ipa": "/hɪˈpætɪk ˈtænədʒər/", "vi": "chim hồng y màu gan hepatic"},
  {"id": "lex.en.200k.059675", "hw": "homo habilis", "pos": "phrase", "ipa": "/ˈhoʊmoʊ ˈhæbəlɪs/", "vi": "người khéo léo Homo habilis"},
  {"id": "lex.en.200k.059676", "hw": "inga edulis", "pos": "phrase", "ipa": "/ˈɪŋɡə ˈɛdʒʊlɪs/", "vi": "cây que kem Inga edulis"},
  {"id": "lex.en.200k.059677", "hw": "jacques monod", "pos": "phrase", "ipa": "/ʒɑːk məˈnoʊ/", "vi": "nhà sinh học Nobel Jacques Monod"},
  {"id": "lex.en.200k.059678", "hw": "labia minora", "pos": "phrase", "ipa": "/ˈleɪbiə mɪˈnɔːrə/", "vi": "môi bé âm hộ giải phẫu"},
  {"id": "lex.en.200k.059679", "hw": "lightning arrester", "pos": "phrase", "ipa": "/ˈlaɪtnɪŋ əˈrɛstər/", "vi": "thiết bị chống sét van lan truyền"},
  {"id": "lex.en.200k.059680", "hw": "lobster newburg", "pos": "phrase", "ipa": "/ˈlɑːbstər ˈnuːbɜːrɡ/", "vi": "món tôm hùm sốt bơ trứng Newburg"},
  {"id": "lex.en.200k.059681", "hw": "magen david", "pos": "phrase", "ipa": "/ˈmɑːɡən dɑːˈviːd/", "vi": "ngôi sao sáu cánh Magen David"},
  {"id": "lex.en.200k.059682", "hw": "mastoid bone", "pos": "phrase", "ipa": "/ˈmæstɔɪd boʊn/", "vi": "xương chũm sau tai"},
  {"id": "lex.en.200k.059683", "hw": "mastoid process", "pos": "phrase", "ipa": "/ˈmæstɔɪd ˈprɑːsɛs/", "vi": "mỏm chũm của xương thái dương"},
  {"id": "lex.en.200k.059684", "hw": "matzah ball", "pos": "phrase", "ipa": "/ˈmɑːtsə bɔːl/", "vi": "viên bột súp không men matzah"},
  {"id": "lex.en.200k.059685", "hw": "matzah meal", "pos": "phrase", "ipa": "/ˈmɑːtsə miːl/", "vi": "bột nghiền từ bánh matzah"},
  {"id": "lex.en.200k.059686", "hw": "meningeal artery", "pos": "phrase", "ipa": "/mɪˈnɪndʒiəl ˈɑːrtəri/", "vi": "động mạch màng não nuôi màng cứng"},
  {"id": "lex.en.200k.059687", "hw": "meningeal veins", "pos": "phrase", "ipa": "/mɪˈnɪndʒiəl veɪnz/", "vi": "các tĩnh mạch dẫn máu màng não"},
  {"id": "lex.en.200k.059688", "hw": "middle meningeal artery", "pos": "phrase", "ipa": "/ˈmɪdl mɪˈnɪndʒiəl ˈɑːrtəri/", "vi": "động mạch màng não giữa"},
  {"id": "lex.en.200k.059689", "hw": "monkey pinscher", "pos": "phrase", "ipa": "/ˈmʌŋki ˈpɪntʃər/", "vi": "giống chó khỉ Affenpinscher"},
  {"id": "lex.en.200k.059690", "hw": "mountain hollyhock", "pos": "phrase", "ipa": "/ˈmaʊntn ˈhɑːlihɑːk/", "vi": "cây hoa cẩm quỳ núi Bắc Mỹ"},
  {"id": "lex.en.200k.059691", "hw": "mud dauber", "pos": "phrase", "ipa": "/mʌd ˈdɔːbər/", "vi": "loài tò vò xây tổ bằng bùn đất"},
  {"id": "lex.en.200k.059692", "hw": "nasal decongestant", "pos": "phrase", "ipa": "/ˈneɪzl ˌdiːkənˈdʒɛstənt/", "vi": "thuốc chống nghẹt mũi thông mũi"},
  {"id": "lex.en.200k.059693", "hw": "nephrotic syndrome", "pos": "phrase", "ipa": "/nɛfˈrɑːtɪk ˈsɪndroʊm/", "vi": "hội chứng thận hư tiết đạm niệu"},
  {"id": "lex.en.200k.059694", "hw": "nipa palm", "pos": "phrase", "ipa": "/ˈniːpə pɑːm/", "vi": "cây dừa nước đầm lầy nhiệt đới"},
  {"id": "lex.en.200k.059695", "hw": "oeil de boeuf", "pos": "phrase", "ipa": "/ˌɜːj də ˈbɜːf/", "vi": "cửa sổ tròn mắt bò kiến trúc cổ"},
  {"id": "lex.en.200k.059696", "hw": "old stager", "pos": "phrase", "ipa": "/oʊld ˈsteɪdʒər/", "vi": "người lão luyện già dặn kinh nghiệm"},
  {"id": "lex.en.200k.059697", "hw": "opera comique", "pos": "phrase", "ipa": "/ˌɑːpərə koʊˈmiːk/", "vi": "thể loại nhạc kịch opéra-comique"},
  {"id": "lex.en.200k.059698", "hw": "opuntia tuna", "pos": "phrase", "ipa": "/oʊˈpʌnʃiə ˈtuːnə/", "vi": "cây xương rồng quả gai ăn được"},
  {"id": "lex.en.200k.059699", "hw": "order carnivora", "pos": "phrase", "ipa": "/ˈɔːrdər kɑːrˈnɪvərə/", "vi": "bộ động vật có vú Ăn thịt"},
  {"id": "lex.en.200k.059700", "hw": "picea abies", "pos": "phrase", "ipa": "/ˈpaɪsiːə ˈeɪbiːiː/", "vi": "loài cây vân sam Na Uy thông Noel"},
  {"id": "lex.en.200k.059701", "hw": "queensboro bridge", "pos": "phrase", "ipa": "/ˌkwiːnzbərə ˈbrɪdʒ/", "vi": "cây cầu thép Queensboro New York"},
  {"id": "lex.en.200k.059702", "hw": "ramon lully", "pos": "phrase", "ipa": "/rəˈmoʊn ˈlʌli/", "vi": "triết gia Ramon Llull thời Trung Cổ"}
]

with open('scratch/b32_r10_raw_p2.json') as f:
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

with open('scratch/b32_r10_p2.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Part 2 validated and written successfully.")
