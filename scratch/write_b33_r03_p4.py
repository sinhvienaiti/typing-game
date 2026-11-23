import json

items = [
  {"id": "lex.en.200k.061303", "hw": "sashays", "pos": "noun", "ipa": "/sæˈʃeɪz/", "vi": "bước trượt lả lướt; dáng đi ưỡn ẹo"},
  {"id": "lex.en.200k.061304", "hw": "scopolamines", "pos": "noun", "ipa": "/skəˈpɑːləmiːnz/", "vi": "thuốc chống say tàu xe scopolamine"},
  {"id": "lex.en.200k.061305", "hw": "seafarers", "pos": "noun", "ipa": "/ˈsiːfɛərərz/", "vi": "thủy thủ đi biển; người đi biển"},
  {"id": "lex.en.200k.061306", "hw": "seeled", "pos": "verb", "ipa": "/siːld/", "vi": "đã khâu mí mắt chim săn luyện"},
  {"id": "lex.en.200k.061307", "hw": "seeling", "pos": "verb", "ipa": "/ˈsiːlɪŋ/", "vi": "đang khâu kín mí mắt chim ưng"},
  {"id": "lex.en.200k.061308", "hw": "seels", "pos": "verb", "ipa": "/siːlz/", "vi": "khâu tạm mí mắt chim ưng; bịt mắt"},
  {"id": "lex.en.200k.061309", "hw": "shofars", "pos": "noun", "ipa": "/ˈʃoʊfɑːrz/", "vi": "tù và sừng cừu shofar Do Thái"},
  {"id": "lex.en.200k.061310", "hw": "shofroth", "pos": "noun", "ipa": "/ʃoʊˈfroʊθ/", "vi": "nhiều chiếc tù và sừng cừu shofar"},
  {"id": "lex.en.200k.061311", "hw": "sildenafils", "pos": "noun", "ipa": "/sɪlˈdɛnəfɪlz/", "vi": "dược chất giãn mạch sildenafil"},
  {"id": "lex.en.200k.061312", "hw": "silverfishes", "pos": "noun", "ipa": "/ˈsɪlvərfɪʃɪz/", "vi": "con bọ bạc; con sâu ăn giấy sách"},
  {"id": "lex.en.200k.061313", "hw": "sloes", "pos": "noun", "ipa": "/sloʊz/", "vi": "quả mận gai đen chát châu Âu"},
  {"id": "lex.en.200k.061314", "hw": "spheroids", "pos": "noun", "ipa": "/ˈsfɪərɔɪdz/", "vi": "hình phỏng cầu hơi dẹt; khối cầu"},
  {"id": "lex.en.200k.061315", "hw": "stellers", "pos": "noun", "ipa": "/ˈstɛlərz/", "vi": "nhà tự nhiên học Đức Georg Steller"},
  {"id": "lex.en.200k.061316", "hw": "stepladders", "pos": "noun", "ipa": "/ˈstɛplædərz/", "vi": "chiếc thang chữ A tự đứng gấp gọn"},
  {"id": "lex.en.200k.061317", "hw": "sterols", "pos": "noun", "ipa": "/ˈstɪrɔːlz/", "vi": "hợp chất rượu vòng hữu cơ sterol"},
  {"id": "lex.en.200k.061318", "hw": "tarsals", "pos": "noun", "ipa": "/ˈtɑːrsəlz/", "vi": "các xương cổ chân; đĩa sụn mi mắt"},
  {"id": "lex.en.200k.061319", "hw": "televangelists", "pos": "noun", "ipa": "/ˌtɛləˈvændʒəlɪsts/", "vi": "nhà truyền đạo qua truyền hình"},
  {"id": "lex.en.200k.061320", "hw": "tethyses", "pos": "noun", "ipa": "/ˈtɛθɪsɪz/", "vi": "nữ thần biển Tethys; đại dương cổ"},
  {"id": "lex.en.200k.061321", "hw": "themistocleses", "pos": "noun", "ipa": "/θəˈmɪstəkliːzɪz/", "vi": "tướng lĩnh Athens cổ Themistocles"},
  {"id": "lex.en.200k.061322", "hw": "thetides", "pos": "noun", "ipa": "/ˈθɛtɪdiːz/", "vi": "nữ thần biển Thetis mẹ Achilles"},
  {"id": "lex.en.200k.061323", "hw": "topcoats", "pos": "noun", "ipa": "/ˈtɑːpkoʊts/", "vi": "áo khoác ngoài; lớp sơn phủ ngoài"},
  {"id": "lex.en.200k.061324", "hw": "topoi", "pos": "noun", "ipa": "/ˈtɔːpɔɪ/", "vi": "mô-típ văn học; chủ đề tu từ lặp"},
  {"id": "lex.en.200k.061325", "hw": "toposes", "pos": "noun", "ipa": "/ˈtɑːpoʊsɪz/", "vi": "chủ đề tu từ học; không gian topos"},
  {"id": "lex.en.200k.061326", "hw": "transferees", "pos": "noun", "ipa": "/ˌtrænsfəˈriːz/", "vi": "người chuyển công tác; bên nhận"},
  {"id": "lex.en.200k.061327", "hw": "trebuchets", "pos": "noun", "ipa": "/ˈtrɛbjʊʃɛts/", "vi": "máy bắn đá đối trọng công thành cổ"},
  {"id": "lex.en.200k.061328", "hw": "tubules", "pos": "noun", "ipa": "/ˈtuːbjuːlz/", "vi": "tiểu quản sinh học; ống thận nhỏ"},
  {"id": "lex.en.200k.061329", "hw": "tufas", "pos": "noun", "ipa": "/ˈtuːfəz/", "vi": "đá vôi xốp kết tủa từ suối khoáng"},
  {"id": "lex.en.200k.061330", "hw": "tupped", "pos": "verb", "ipa": "/tʌpt/", "vi": "đã cho cừu đực nhảy phối giống"},
  {"id": "lex.en.200k.061331", "hw": "tupping", "pos": "verb", "ipa": "/ˈtʌpɪŋ/", "vi": "đang cho cừu đực phối giống cái"},
  {"id": "lex.en.200k.061332", "hw": "tups", "pos": "noun", "ipa": "/tʌps/", "vi": "con cừu đực giống; đầu búa máy dập"},
  {"id": "lex.en.200k.061333", "hw": "unais", "pos": "noun", "ipa": "/uːˈnaɪz/", "vi": "con lười hai ngón Nam Mỹ"},
  {"id": "lex.en.200k.061334", "hw": "vacays", "pos": "noun", "ipa": "/ˈveɪkeɪz/", "vi": "kỳ nghỉ phép đi du lịch (thân mật)"},
  {"id": "lex.en.200k.061335", "hw": "veblens", "pos": "noun", "ipa": "/ˈvɛblənz/", "vi": "nhà kinh tế học Thorstein Veblen"},
  {"id": "lex.en.200k.061336", "hw": "vespuccis", "pos": "noun", "ipa": "/vɛˈspuːtʃiz/", "vi": "nhà hàng hải Ý Amerigo Vespucci"},
  {"id": "lex.en.200k.061337", "hw": "viennes", "pos": "noun", "ipa": "/viˈɛnz/", "vi": "thành phố lịch sử Vienne ở Pháp"},
  {"id": "lex.en.200k.061338", "hw": "violoncellos", "pos": "noun", "ipa": "/ˌvaɪələnˈtʃɛloʊz/", "vi": "cây đàn dây trung trầm xen-lô"},
  {"id": "lex.en.200k.061339", "hw": "amphibole group", "pos": "phrase", "ipa": "/ˈæmfɪboʊl ɡruːp/", "vi": "nhóm khoáng vật silicat amphibol"},
  {"id": "lex.en.200k.061340", "hw": "andre markoff", "pos": "phrase", "ipa": "/ɑːnˈdreɪ ˈmɑːrkɔːf/", "vi": "nhà toán học Nga Andrey Markov"},
  {"id": "lex.en.200k.061341", "hw": "artemus ward", "pos": "phrase", "ipa": "/ˈɑːrtɪməs wɔːrd/", "vi": "nhà văn trào phúng Mỹ Artemus Ward"},
  {"id": "lex.en.200k.061342", "hw": "bartolome esteban murillo", "pos": "phrase", "ipa": "/bɑːrtɔːlɔːˈmeɪ ɛsˈtɛbɑːn mʊˈriːjoʊ/", "vi": "họa sĩ Tây Ban Nha Esteban Murillo"},
  {"id": "lex.en.200k.061343", "hw": "carbon dichloride", "pos": "phrase", "ipa": "/ˈkɑːrbən daɪˈklɔːraɪd/", "vi": "hợp chất hóa học cacbon điclorua"},
  {"id": "lex.en.200k.061344", "hw": "cattail family", "pos": "phrase", "ipa": "/ˈkætteɪl ˈfæməli/", "vi": "họ thực vật cây cỏ nến bồn bồn"},
  {"id": "lex.en.200k.061345", "hw": "christiaan huygens", "pos": "phrase", "ipa": "/ˈkrɪstiɑːn ˈhɔɪɡənz/", "vi": "nhà vật lý thiên văn học Huygens"},
  {"id": "lex.en.200k.061346", "hw": "clematis versicolor", "pos": "phrase", "ipa": "/ˈklɛmətɪs ˈvɜːrsɪkʌlər/", "vi": "dây hoa ông lão tím nhạt Bắc Mỹ"},
  {"id": "lex.en.200k.061347", "hw": "clematis virginiana", "pos": "phrase", "ipa": "/ˈklɛmətɪs vərˌdʒɪniˈeɪnə/", "vi": "dây leo hoa ông lão trắng Virginia"},
  {"id": "lex.en.200k.061348", "hw": "cloud seeder", "pos": "phrase", "ipa": "/klaʊd ˈsiːdər/", "vi": "kỹ thuật viên gieo mây làm mưa"},
  {"id": "lex.en.200k.061349", "hw": "cola acuminata", "pos": "phrase", "ipa": "/ˈkoʊlə əˌkjuːmɪˈneɪtə/", "vi": "cây cô-la hạt chứa caffein Tây Phi"},
  {"id": "lex.en.200k.061350", "hw": "consumer durables", "pos": "phrase", "ipa": "/kənˈsuːmər ˈdʊərəblz/", "vi": "hàng hóa tiêu dùng lâu bền"},
  {"id": "lex.en.200k.061351", "hw": "crape jasmine", "pos": "phrase", "ipa": "/kreɪp ˈdʒæzmɪn/", "vi": "cây hoa lài tây cánh nhăn trắng"},
  {"id": "lex.en.200k.061352", "hw": "crape myrtle", "pos": "phrase", "ipa": "/kreɪp ˈmɜːrtl/", "vi": "cây hoa bằng lăng; cây tử vi"},
  {"id": "lex.en.200k.061353", "hw": "creeping crowfoot", "pos": "phrase", "ipa": "/ˈkriːpɪŋ ˈkroʊfʊt/", "vi": "cây mao lương thân bò hoa vàng"},
  {"id": "lex.en.200k.061354", "hw": "cursed crowfoot", "pos": "phrase", "ipa": "/ˈkɜːrsɪd ˈkroʊfʊt/", "vi": "cây mao lương độc mọc vùng đầm lầy"},
  {"id": "lex.en.200k.061355", "hw": "delirium tremens", "pos": "phrase", "ipa": "/dɪˈlɪriəm ˈtriːmɛnz/", "vi": "cơn mê sảng run tay do cai rượu"},
  {"id": "lex.en.200k.061356", "hw": "dmitri ivanovich mendeleev", "pos": "phrase", "ipa": "/dɪˈmiːtri iˈvɑːnəvɪtʃ ˌmɛndəˈleɪɛf/", "vi": "nhà hóa học Nga Dmitri Mendeleev"},
  {"id": "lex.en.200k.061357", "hw": "dolce far niente", "pos": "phrase", "ipa": "/ˈdɔːltʃeɪ fɑːr niˈɛnteɪ/", "vi": "niềm vui nhàn nhã thảnh thơi vô lo"},
  {"id": "lex.en.200k.061358", "hw": "edward james muggeridge", "pos": "phrase", "ipa": "/ˈɛdwərd dʒeɪmz ˈmʌɡərɪdʒ/", "vi": "nhiếp ảnh gia Eadweard Muybridge"},
  {"id": "lex.en.200k.061359", "hw": "eira barbara", "pos": "phrase", "ipa": "/ˈeɪrə ˈbɑːrbərə/", "vi": "loài chồn tayra leo cây Nam Mỹ"},
  {"id": "lex.en.200k.061360", "hw": "equus kiang", "pos": "phrase", "ipa": "/ˈiːkwəs kiˈɑːŋ/", "vi": "loài lừa hoang Tây Tạng Kiang"},
  {"id": "lex.en.200k.061361", "hw": "erich von stroheim", "pos": "phrase", "ipa": "/ˈɛrɪk fɔːn ˈstroʊhaɪm/", "vi": "đạo diễn diễn viên Áo Von Stroheim"},
  {"id": "lex.en.200k.061362", "hw": "franz werfel", "pos": "phrase", "ipa": "/frɑːnts ˈvɛərfəl/", "vi": "tiểu thuyết gia Áo Franz Werfel"},
  {"id": "lex.en.200k.061363", "hw": "gaetano donizetti", "pos": "phrase", "ipa": "/ɡaɪˈtɑːnoʊ ˌdɑːnɪˈtsɛti/", "vi": "nhà soạn nhạc opera Ý Donizetti"},
  {"id": "lex.en.200k.061364", "hw": "genus chiton", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈkaɪtn/", "vi": "chi ốc song kinh bám đá Chiton"},
  {"id": "lex.en.200k.061365", "hw": "genus dendrobium", "pos": "phrase", "ipa": "/ˈdʒiːnəs dɛnˈdroʊbiəm/", "vi": "chi phong lan hoàng thảo Dendrobium"},
  {"id": "lex.en.200k.061366", "hw": "genus festuca", "pos": "phrase", "ipa": "/ˈdʒiːnəs fɛsˈtjuːkə/", "vi": "chi cỏ đuôi trâu ôn đới Festuca"},
  {"id": "lex.en.200k.061367", "hw": "genus lanius", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈleɪniəs/", "vi": "chi chim bách thanh săn mồi Lanius"},
  {"id": "lex.en.200k.061368", "hw": "genus majorana", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌmædʒəˈreɪnə/", "vi": "chi cây kinh giới ngọt Majorana"},
  {"id": "lex.en.200k.061369", "hw": "genus oryza", "pos": "phrase", "ipa": "/ˈdʒiːnəs əˈraɪzə/", "vi": "chi thực vật cây lúa gạo Oryza"},
  {"id": "lex.en.200k.061370", "hw": "giambattista marini", "pos": "phrase", "ipa": "/ˌdʒɑːmbɑːˈtiːstə mɑːˈriːni/", "vi": "nhà thơ Ý Giambattista Marino"},
  {"id": "lex.en.200k.061371", "hw": "gulf of aegina", "pos": "phrase", "ipa": "/ɡʌlf əv iˈdʒaɪnə/", "vi": "vịnh biển Saronic Aegina ở Hy Lạp"},
  {"id": "lex.en.200k.061372", "hw": "henri becquerel", "pos": "phrase", "ipa": "/ɑ̃ːˈri ˌbɛkəˈrɛl/", "vi": "nhà vật lý tìm phóng xạ Becquerel"},
  {"id": "lex.en.200k.061373", "hw": "imperforate anus", "pos": "phrase", "ipa": "/ɪmˈpɜːrfərət ˈeɪnəs/", "vi": "dị tật bẩm sinh không có hậu môn"},
  {"id": "lex.en.200k.061374", "hw": "johannes evangelista purkinje", "pos": "phrase", "ipa": "/joʊˈhɑːnəs iːˌvændʒəˈliːstə ˈpɜːrkɪndʒi/", "vi": "nhà giải phẫu sinh lý học Purkinje"},
  {"id": "lex.en.200k.061375", "hw": "karl scheele", "pos": "phrase", "ipa": "/kɑːrl ˈʃeɪlə/", "vi": "nhà hóa học Thụy Điển Carl Scheele"},
  {"id": "lex.en.200k.061376", "hw": "lake ladoga", "pos": "phrase", "ipa": "/leɪk ˈlɑːdəɡə/", "vi": "hồ nước ngọt lớn Ladoga của Nga"},
  {"id": "lex.en.200k.061377", "hw": "luigi galvani", "pos": "phrase", "ipa": "/luːˈiːdʒi ɡælˈvɑːni/", "vi": "nhà vật lý điện sinh học Galvani"},
  {"id": "lex.en.200k.061378", "hw": "markoff chain", "pos": "phrase", "ipa": "/ˈmɑːrkɔːf tʃeɪn/", "vi": "chuỗi xác suất Markov toán học"},
  {"id": "lex.en.200k.061379", "hw": "markoff process", "pos": "phrase", "ipa": "/ˈmɑːrkɔːf ˈprɑːsɛs/", "vi": "quá trình ngẫu nhiên Markov toán"},
  {"id": "lex.en.200k.061380", "hw": "monadic operation", "pos": "phrase", "ipa": "/məˈnædɪk ˌɑːpəˈreɪʃən/", "vi": "phép toán một ngôi trong toán học"},
  {"id": "lex.en.200k.061381", "hw": "negara brunei darussalam", "pos": "phrase", "ipa": "/nəˈɡɑːrə ˈbruːnaɪ ˌdɑːrʊsəˈlɑːm/", "vi": "Vương quốc Brunei Đông Nam Á"},
  {"id": "lex.en.200k.061382", "hw": "nikolai ivanovich bukharin", "pos": "phrase", "ipa": "/nɪkəˈlaɪ iˈvɑːnəvɪtʃ bʊˈkɑːrɪn/", "vi": "chính khách Xô Viết Bukharin"},
  {"id": "lex.en.200k.061383", "hw": "owlet moth", "pos": "phrase", "ipa": "/ˈaʊlət mɔːθ/", "vi": "loài bướm đêm họ Noctuidae"},
  {"id": "lex.en.200k.061384", "hw": "palmitic acid", "pos": "phrase", "ipa": "/pælˈmɪtɪk ˈæsɪd/", "vi": "axit béo bão hòa palmitic dầu cọ"},
  {"id": "lex.en.200k.061385", "hw": "peter minuit", "pos": "phrase", "ipa": "/ˈpiːtər ˈmɪnjuɪt/", "vi": "thống đốc Hà Lan Peter Minuit"},
  {"id": "lex.en.200k.061386", "hw": "pieter zeeman", "pos": "phrase", "ipa": "/ˈpiːtər ˈzeɪmɑːn/", "vi": "nhà vật lý Nobel Pieter Zeeman"},
  {"id": "lex.en.200k.061387", "hw": "pluperfect tense", "pos": "phrase", "ipa": "/pluːˈpɜːrfɪkt tɛns/", "vi": "thì quá khứ hoàn thành ngữ pháp"},
  {"id": "lex.en.200k.061388", "hw": "polygenic disease", "pos": "phrase", "ipa": "/ˌpɑːliˈdʒɛnɪk dɪˈziːz/", "vi": "bệnh di truyền đa gen phối hợp"},
  {"id": "lex.en.200k.061389", "hw": "polygenic disorder", "pos": "phrase", "ipa": "/ˌpɑːliˈdʒɛnɪk dɪsˈɔːrdər/", "vi": "rối loạn bẩm sinh do đa gen gây ra"},
  {"id": "lex.en.200k.061390", "hw": "prunus domestica", "pos": "phrase", "ipa": "/ˈpruːnəs dəˈmɛstɪkə/", "vi": "cây mận hậu trồng lấy quả châu Âu"},
  {"id": "lex.en.200k.061391", "hw": "raffaello santi", "pos": "phrase", "ipa": "/ˌræfeɪˈɛloʊ ˈsɑːnti/", "vi": "danh họa Phục hưng Ý Raphael"},
  {"id": "lex.en.200k.061392", "hw": "ragtag and bobtail", "pos": "phrase", "ipa": "/ˈræɡtæɡ ænd ˈbɑːbteɪl/", "vi": "lũ ô hợp hạ lưu; đám đông lôm côm"},
  {"id": "lex.en.200k.061393", "hw": "rattus rattus", "pos": "phrase", "ipa": "/ˈrætəs ˈrætəs/", "vi": "loài chuột đen gặm nhấm truyền bệnh"},
  {"id": "lex.en.200k.061394", "hw": "respiratory syncytial virus", "pos": "phrase", "ipa": "/ˈrɛspərətɔːri sɪnˈsɪʃəl ˈvaɪrəs/", "vi": "vi-rút hợp bào đường hô hấp RSV"},
  {"id": "lex.en.200k.061395", "hw": "riss glaciation", "pos": "phrase", "ipa": "/rɪs ˌɡleɪsiˈeɪʃən/", "vi": "thời kỳ băng hà Riss dãy Alps"},
  {"id": "lex.en.200k.061396", "hw": "sanwa millet", "pos": "phrase", "ipa": "/ˈsɑːnwə ˈmɪlɪt/", "vi": "cây kê lương thực hạt nhỏ Sanwa"},
  {"id": "lex.en.200k.061397", "hw": "saphenous nerve", "pos": "phrase", "ipa": "/səˈfiːnəs nɜːrv/", "vi": "dây thần kinh hiển cảm giác chân"},
  {"id": "lex.en.200k.061398", "hw": "sayan mountains", "pos": "phrase", "ipa": "/səˈjɑːn ˈmaʊntnz/", "vi": "dãy núi Sayan ở miền nam Siberia"},
  {"id": "lex.en.200k.061399", "hw": "scaphoid bone", "pos": "phrase", "ipa": "/ˈskæfɔɪd boʊn/", "vi": "xương thuyền nằm ở vùng cổ tay"},
  {"id": "lex.en.200k.061400", "hw": "scleral veins", "pos": "phrase", "ipa": "/ˈsklɪərəl veɪnz/", "vi": "tĩnh mạch củng mạc nhãn cầu mắt"},
  {"id": "lex.en.200k.061401", "hw": "scribing block", "pos": "phrase", "ipa": "/ˈskraɪbɪŋ blɑːk/", "vi": "đế vạch dấu chuẩn cơ khí rà phẳng"},
  {"id": "lex.en.200k.061402", "hw": "sequoia gigantea", "pos": "phrase", "ipa": "/sɪˈkwɔɪə dʒaɪˈɡæntiə/", "vi": "cây cù tùng khổng lồ California"}
]

with open('scratch/b33_r03_raw_p4.json') as f:
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

with open('scratch/b33_r03_p4.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Batch 33 Round 3 Part 4 validated and written successfully.")
