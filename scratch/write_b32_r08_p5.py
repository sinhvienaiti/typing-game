import json

items = [
  {"id": "lex.en.200k.058902", "hw": "quickstepping", "pos": "verb", "ipa": "/kwˈɪkstɛpɪŋ/", "vi": "đang nhảy điệu quickstep"},
  {"id": "lex.en.200k.058903", "hw": "quicksteps", "pos": "noun", "ipa": "/kwˈɪkstɛps/", "vi": "điệu nhảy bước nhanh quickstep"},
  {"id": "lex.en.200k.058904", "hw": "radioisotopes", "pos": "noun", "ipa": "/rˌeɪdioʊˈaɪsətoʊps/", "vi": "đồng vị phóng xạ"},
  {"id": "lex.en.200k.058905", "hw": "railcars", "pos": "noun", "ipa": "/rˈeɪlkˌɑrz/", "vi": "toa xe lửa tự hành; toa tàu"},
  {"id": "lex.en.200k.058906", "hw": "ravishes", "pos": "verb", "ipa": "/rˈævɪʃɪz/", "vi": "làm say mê ngây ngất; hãm hiếp"},
  {"id": "lex.en.200k.058907", "hw": "reallocated", "pos": "verb", "ipa": "/rˌiˈæləkˌeɪtɪd/", "vi": "đã phân bổ lại ngân sách"},
  {"id": "lex.en.200k.058908", "hw": "reallocates", "pos": "verb", "ipa": "/riˈæləkeɪts/", "vi": "phân bổ lại nguồn lực"},
  {"id": "lex.en.200k.058909", "hw": "reallocating", "pos": "verb", "ipa": "/riˈæləkˌeɪtɪŋ/", "vi": "đang phân bổ lại"},
  {"id": "lex.en.200k.058910", "hw": "recriminations", "pos": "noun", "ipa": "/rɪkrˌɪmɪnˈeɪʃənz/", "vi": "sự chỉ trích cãi vã lẫn nhau"},
  {"id": "lex.en.200k.058911", "hw": "rejoinders", "pos": "noun", "ipa": "/rɪdʒˈɔɪndɚz/", "vi": "lời đối đáp nhanh; lời cãi lại"},
  {"id": "lex.en.200k.058912", "hw": "repairers", "pos": "noun", "ipa": "/rɪpˈɛrɚz/", "vi": "thợ sửa chữa; người phục chế"},
  {"id": "lex.en.200k.058913", "hw": "reprobates", "pos": "noun", "ipa": "/rˈɛprəbeɪts/", "vi": "kẻ hư hỏng sa đọa vô luân"},
  {"id": "lex.en.200k.058914", "hw": "republications", "pos": "noun", "ipa": "/riːˌpʌblɪkˈeɪʃənz/", "vi": "sự tái bản sách báo; bản in lại"},
  {"id": "lex.en.200k.058915", "hw": "riffled", "pos": "verb", "ipa": "/rˈɪfəld/", "vi": "đã lật nhanh trang giấy; khuấy sóng"},
  {"id": "lex.en.200k.058916", "hw": "riffles", "pos": "noun", "ipa": "/rˈɪfəlz/", "vi": "gợn sóng lăn tăn ghềnh đá"},
  {"id": "lex.en.200k.058917", "hw": "riffling", "pos": "verb", "ipa": "/rˈɪfəlɪŋ/", "vi": "đang lật nhanh trang giấy"},
  {"id": "lex.en.200k.058918", "hw": "ringgits", "pos": "noun", "ipa": "/rˈɪŋɡɪts/", "vi": "đồng ringgit của Malaysia"},
  {"id": "lex.en.200k.058919", "hw": "sadhus", "pos": "noun", "ipa": "/sˈɑːduːz/", "vi": "đạo sĩ khổ hạnh Ấn Độ giáo"},
  {"id": "lex.en.200k.058920", "hw": "saidas", "pos": "noun", "ipa": "/sˈaɪdəz/", "vi": "thành phố cảng Saida ở Liban"},
  {"id": "lex.en.200k.058921", "hw": "sennetts", "pos": "noun", "ipa": "/sˈɛnɪts/", "vi": "đạo diễn phim hài Mack Sennett"},
  {"id": "lex.en.200k.058922", "hw": "sitwells", "pos": "noun", "ipa": "/sˈɪtwɛlz/", "vi": "nhà thơ Edith Sitwell"},
  {"id": "lex.en.200k.058923", "hw": "slouchier", "pos": "adj", "ipa": "/slˈaʊtʃiɚ/", "vi": "dáng đi lom khom hơn; chùng hơn"},
  {"id": "lex.en.200k.058924", "hw": "slouchiest", "pos": "adj", "ipa": "/slˈaʊtʃiɪst/", "vi": "dáng đi lom khom nhất; chùng nhất"},
  {"id": "lex.en.200k.058925", "hw": "smallmouths", "pos": "noun", "ipa": "/smˈɔːlmaʊθs/", "vi": "cá vược miệng nhỏ nước ngọt"},
  {"id": "lex.en.200k.058926", "hw": "smokestacks", "pos": "noun", "ipa": "/smˈoʊkstˌæks/", "vi": "ống khói cao nhà máy; ống xả tàu"},
  {"id": "lex.en.200k.058927", "hw": "solanums", "pos": "noun", "ipa": "/soʊlˈeɪnəmz/", "vi": "chi thực vật họ Cà solanum"},
  {"id": "lex.en.200k.058928", "hw": "soothsayers", "pos": "noun", "ipa": "/sˌuθsˈeɪɚz/", "vi": "thầy bói toán; nhà tiên tri"},
  {"id": "lex.en.200k.058929", "hw": "spasticities", "pos": "noun", "ipa": "/spæstˈɪsətiz/", "vi": "chứng co cứng cơ; tăng trương lực"},
  {"id": "lex.en.200k.058930", "hw": "spironolactones", "pos": "noun", "ipa": "/spˌaɪroʊnoʊlˈæktoʊnz/", "vi": "thuốc lợi tiểu spironolactone"},
  {"id": "lex.en.200k.058931", "hw": "stengels", "pos": "noun", "ipa": "/stˈɛŋɡəlz/", "vi": "huấn luyện viên Casey Stengel"},
  {"id": "lex.en.200k.058932", "hw": "stopeses", "pos": "noun", "ipa": "/stˈoʊpsɪz/", "vi": "nhà vận động Marie Stopes"},
  {"id": "lex.en.200k.058933", "hw": "sugarloafs", "pos": "noun", "ipa": "/ʃˈʊɡɚloʊfs/", "vi": "khối đường hình nón; đồi núi nón"},
  {"id": "lex.en.200k.058934", "hw": "suppressants", "pos": "noun", "ipa": "/səprˈɛsənts/", "vi": "thuốc ức chế; chất kìm hãm"},
  {"id": "lex.en.200k.058935", "hw": "sycophants", "pos": "noun", "ipa": "/sˈɪkəfænts/", "vi": "kẻ xu nịnh; kẻ bợ đỡ luồn cúi"},
  {"id": "lex.en.200k.058936", "hw": "techier", "pos": "adj", "ipa": "/tˈɛkiɚ/", "vi": "dễ cáu bẳn hơn; rành công nghệ hơn"},
  {"id": "lex.en.200k.058937", "hw": "techiest", "pos": "adj", "ipa": "/tˈɛkiɪst/", "vi": "dễ cáu nhất; rành công nghệ nhất"},
  {"id": "lex.en.200k.058938", "hw": "tineas", "pos": "noun", "ipa": "/tˈɪniəz/", "vi": "bệnh nấm da hắc lào"},
  {"id": "lex.en.200k.058939", "hw": "townies", "pos": "noun", "ipa": "/tˈaʊniz/", "vi": "người dân bản xứ thị trấn"},
  {"id": "lex.en.200k.058940", "hw": "toxoplasmoses", "pos": "noun", "ipa": "/tˌɑːksoʊplæzmˈoʊsiːz/", "vi": "bệnh nhiễm toxoplasma"},
  {"id": "lex.en.200k.058941", "hw": "trippers", "pos": "noun", "ipa": "/trˈɪpɚz/", "vi": "người du ngoạn ngắn; kẻ phê thuốc"},
  {"id": "lex.en.200k.058942", "hw": "truffauts", "pos": "noun", "ipa": "/truːfˈoʊz/", "vi": "đạo diễn François Truffaut"},
  {"id": "lex.en.200k.058943", "hw": "tuscaroras", "pos": "noun", "ipa": "/tˌʌskərˈɔːrəz/", "vi": "người da đỏ bản địa Tuscarora"},
  {"id": "lex.en.200k.058944", "hw": "underestimations", "pos": "noun", "ipa": "/ˌʌndərˌɛstəmˈeɪʃənz/", "vi": "sự đánh giá quá thấp"},
  {"id": "lex.en.200k.058945", "hw": "urinalyses", "pos": "noun", "ipa": "/jˌʊrənˈæləsiːz/", "vi": "xét nghiệm phân tích nước tiểu"},
  {"id": "lex.en.200k.058946", "hw": "veroneses", "pos": "noun", "ipa": "/vˌɛrənˈeɪseɪz/", "vi": "danh họa Paolo Veronese"},
  {"id": "lex.en.200k.058947", "hw": "wakers", "pos": "noun", "ipa": "/wˈeɪkɚz/", "vi": "người thức giấc; người đánh thức"},
  {"id": "lex.en.200k.058948", "hw": "wbses", "pos": "noun", "ipa": "/dˈʌbəljubiːˈɛsɪz/", "vi": "hướng tây nghiêng nam"},
  {"id": "lex.en.200k.058949", "hw": "ader wax", "pos": "phrase", "ipa": "/ˈɑːdər wæks/", "vi": "sáp ozokerit tinh chế ader"},
  {"id": "lex.en.200k.058950", "hw": "althea rosea", "pos": "phrase", "ipa": "/ælˈθiːə ˈroʊziə/", "vi": "cây hoa thục quỳ alcea"},
  {"id": "lex.en.200k.058951", "hw": "archean aeon", "pos": "phrase", "ipa": "/ɑːrˈkiːən ˈiːɑːn/", "vi": "liên đại Thái Cổ của Trái Đất"},
  {"id": "lex.en.200k.058952", "hw": "areca nut", "pos": "phrase", "ipa": "/əˈriːkə nʌt/", "vi": "quả cau; hạt cau nhai trầu"},
  {"id": "lex.en.200k.058953", "hw": "areca palm", "pos": "phrase", "ipa": "/əˈriːkə pɑːm/", "vi": "cây cau ăn trầu"},
  {"id": "lex.en.200k.058954", "hw": "arroz con pollo", "pos": "phrase", "ipa": "/ɑːˈroʊz koʊn ˈpɔɪoʊ/", "vi": "món cơm gà kiểu Tây Ban Nha"},
  {"id": "lex.en.200k.058955", "hw": "battle of lepanto", "pos": "phrase", "ipa": "/ˈbætl əv lɪˈpæntoʊ/", "vi": "hải chiến lịch sử Lepanto"},
  {"id": "lex.en.200k.058956", "hw": "bernard malamud", "pos": "phrase", "ipa": "/ˈbɜːrnərd ˈmæləmʊd/", "vi": "nhà văn Bernard Malamud"},
  {"id": "lex.en.200k.058957", "hw": "caddis fly", "pos": "phrase", "ipa": "/ˈkædɪs flaɪ/", "vi": "loài bướm nước; ấu trùng caddis"},
  {"id": "lex.en.200k.058958", "hw": "ceylon bowstring hemp", "pos": "phrase", "ipa": "/sɪˈlɑːn ˈboʊstrɪŋ hɛmp/", "vi": "cây lưỡi hổ gai Ceylon"},
  {"id": "lex.en.200k.058959", "hw": "class reptilia", "pos": "phrase", "ipa": "/klæs rɛpˈtɪliə/", "vi": "lớp động vật bò sát"},
  {"id": "lex.en.200k.058960", "hw": "cooky jar", "pos": "phrase", "ipa": "/ˈkʊki dʒɑːr/", "vi": "hũ thủy tinh đựng bánh quy"},
  {"id": "lex.en.200k.058961", "hw": "cordate leaf", "pos": "phrase", "ipa": "/ˈkɔːrdeɪt liːf/", "vi": "lá cây hình trái tim"},
  {"id": "lex.en.200k.058962", "hw": "ecosoc commission", "pos": "phrase", "ipa": "/ˈiːkoʊsɑːk kəˈmɪʃən/", "vi": "ủy ban Hội đồng Kinh tế Xã hội"},
  {"id": "lex.en.200k.058963", "hw": "edgar varese", "pos": "phrase", "ipa": "/ɛdˈɡɑːr vɑːˈrɛz/", "vi": "nhà soạn nhạc Edgard Varèse"},
  {"id": "lex.en.200k.058964", "hw": "erwin schrodinger", "pos": "phrase", "ipa": "/ˈɛrvɪn ˈʃroʊdɪŋər/", "vi": "nhà vật lý Erwin Schrödinger"},
  {"id": "lex.en.200k.058965", "hw": "freeboard deck", "pos": "phrase", "ipa": "/ˈfriːbɔːrd dɛk/", "vi": "boong mạn khô của tàu thủy"},
  {"id": "lex.en.200k.058966", "hw": "genus borrelia", "pos": "phrase", "ipa": "/ˈdʒiːnəs bəˈrɛliə/", "vi": "chi xoắn khuẩn Borrelia"},
  {"id": "lex.en.200k.058967", "hw": "genus delphinium", "pos": "phrase", "ipa": "/ˈdʒiːnəs dɛlˈfɪniəm/", "vi": "chi hoa phi yến Delphinium"},
  {"id": "lex.en.200k.058968", "hw": "genus impatiens", "pos": "phrase", "ipa": "/ˈdʒiːnəs ɪmˈpeɪʃənz/", "vi": "chi hoa bóng nước Impatiens"},
  {"id": "lex.en.200k.058969", "hw": "giorgio de chirico", "pos": "phrase", "ipa": "/ˈdʒɔːrdʒoʊ deɪ ˈkiːrɪkoʊ/", "vi": "danh họa Giorgio de Chirico"},
  {"id": "lex.en.200k.058970", "hw": "gulf of lepanto", "pos": "phrase", "ipa": "/ɡʌlf əv lɪˈpæntoʊ/", "vi": "vịnh Lepanto ở Hy Lạp"},
  {"id": "lex.en.200k.058971", "hw": "herpes varicella zoster", "pos": "phrase", "ipa": "/ˈhɜːrpiːz ˌværəˈsɛlə ˈzɑːstər/", "vi": "vi-rút gây thủy đậu và zona"},
  {"id": "lex.en.200k.058972", "hw": "hurly burly", "pos": "phrase", "ipa": "/ˈhɜːrli ˈbɜːrli/", "vi": "sự huyên náo hỗn loạn; cảnh ồn ào"},
  {"id": "lex.en.200k.058973", "hw": "hypermedia system", "pos": "phrase", "ipa": "/ˈhaɪpərmiːdiə ˈsɪstəm/", "vi": "hệ thống siêu phương tiện"},
  {"id": "lex.en.200k.058974", "hw": "james ussher", "pos": "phrase", "ipa": "/dʒeɪmz ˈʌʃər/", "vi": "tổng giám mục James Ussher"},
  {"id": "lex.en.200k.058975", "hw": "john galsworthy", "pos": "phrase", "ipa": "/dʒɑːn ˈɡɔːlzwɜːrði/", "vi": "nhà văn John Galsworthy"},
  {"id": "lex.en.200k.058976", "hw": "kauri resin", "pos": "phrase", "ipa": "/ˈkaʊri ˈrɛzɪn/", "vi": "nhựa thơm cây thông kauri"},
  {"id": "lex.en.200k.058977", "hw": "lateral condyle", "pos": "phrase", "ipa": "/ˈlætərəl ˈkɑːndaɪl/", "vi": "lồi cầu ngoài xương đùi"},
  {"id": "lex.en.200k.058978", "hw": "leonid ilyich brezhnev", "pos": "phrase", "ipa": "/leɪˈoʊnɪd ˈɪljɪtʃ ˈbrɛʒnɛf/", "vi": "nhà lãnh đạo Leonid Brezhnev"},
  {"id": "lex.en.200k.058979", "hw": "leslie howard stainer", "pos": "phrase", "ipa": "/ˈlɛzli ˈhaʊərd ˈsteɪnər/", "vi": "nam diễn viên Leslie Howard"},
  {"id": "lex.en.200k.058980", "hw": "luggage carrousel", "pos": "phrase", "ipa": "/ˈlʌɡɪdʒ ˌkærəˈsɛl/", "vi": "băng chuyền nhận hành lý sân bay"},
  {"id": "lex.en.200k.058981", "hw": "magnolia grandiflora", "pos": "phrase", "ipa": "/mæɡˈnoʊliə ˌɡrændəˈflɔːrə/", "vi": "hoa mộc lan đại thụ phương nam"},
  {"id": "lex.en.200k.058982", "hw": "non vult", "pos": "phrase", "ipa": "/nɑːn vʌlt/", "vi": "lời nhận án không cãi của bị cáo"},
  {"id": "lex.en.200k.058983", "hw": "noncoding dna", "pos": "phrase", "ipa": "/nɑːnˈkoʊdɪŋ ˌdiːɛnˈeɪ/", "vi": "đoạn ADN không mã hóa protein"},
  {"id": "lex.en.200k.058984", "hw": "otto neumann sverdrup", "pos": "phrase", "ipa": "/ˈɑːtoʊ ˈnɔɪmən ˈsvɛrdrʊp/", "vi": "nhà thám hiểm Otto Sverdrup"},
  {"id": "lex.en.200k.058985", "hw": "palestinian hizballah", "pos": "phrase", "ipa": "/ˌpæləˈstɪniən ˌhɪzbəˈlɑː/", "vi": "nhánh Hezbollah tại Palestine"},
  {"id": "lex.en.200k.058986", "hw": "patrilineal sib", "pos": "phrase", "ipa": "/ˌpætrəˈlɪniəl sɪb/", "vi": "dòng họ thân tộc bên nội"},
  {"id": "lex.en.200k.058987", "hw": "pinus edulis", "pos": "phrase", "ipa": "/ˈpaɪnəs ˈɛdʒʊlɪs/", "vi": "cây thông hạt ăn được Colorado"},
  {"id": "lex.en.200k.058988", "hw": "pinus palustris", "pos": "phrase", "ipa": "/ˈpaɪnəs pəˈlʌstrɪs/", "vi": "cây thông lá dài đầm lầy"},
  {"id": "lex.en.200k.058989", "hw": "placenta previa", "pos": "phrase", "ipa": "/pləˈsɛntə ˈpriːviə/", "vi": "hiện tượng nhau thai tiền đạo"},
  {"id": "lex.en.200k.058990", "hw": "plasmodium vivax", "pos": "phrase", "ipa": "/plæzˈmoʊdiəm ˈvaɪvæks/", "vi": "ký sinh trùng sốt rét vivax"},
  {"id": "lex.en.200k.058991", "hw": "primula vulgaris", "pos": "phrase", "ipa": "/ˈprɪmjʊlə vʌlˈɡɛərɪs/", "vi": "hoa anh thảo vàng hoang dại"},
  {"id": "lex.en.200k.058992", "hw": "pupillary sphincter", "pos": "phrase", "ipa": "/ˈpjuːpəlɛri ˈsfɪŋktər/", "vi": "cơ thắt cơ vòng con ngươi mắt"},
  {"id": "lex.en.200k.058993", "hw": "quercus rubra", "pos": "phrase", "ipa": "/ˈkwɜːrkəs ˈruːbrə/", "vi": "loài sồi đỏ phương Bắc"},
  {"id": "lex.en.200k.058994", "hw": "river adige", "pos": "phrase", "ipa": "/ˈrɪvər ˈɑːdɪdʒeɪ/", "vi": "sông Adige miền bắc nước Ý"},
  {"id": "lex.en.200k.058995", "hw": "robert benchley", "pos": "phrase", "ipa": "/ˈrɑːbərt ˈbɛntʃli/", "vi": "nhà văn hài Robert Benchley"},
  {"id": "lex.en.200k.058996", "hw": "robert charles benchley", "pos": "phrase", "ipa": "/ˈrɑːbərt tʃɑːrlz ˈbɛntʃli/", "vi": "nghệ sĩ Robert Charles Benchley"},
  {"id": "lex.en.200k.058997", "hw": "rubus australis", "pos": "phrase", "ipa": "/ˈruːbəs ɔːˈstreɪlɪs/", "vi": "loài mâm xôi leo New Zealand"},
  {"id": "lex.en.200k.058998", "hw": "smooth bark kauri", "pos": "phrase", "ipa": "/smuːð bɑːrk ˈkaʊri/", "vi": "cây kauri vỏ nhẵn Australia"},
  {"id": "lex.en.200k.058999", "hw": "sulfa drug", "pos": "phrase", "ipa": "/ˈsʌlfə drʌɡ/", "vi": "thuốc kháng sinh nhóm sulfamid"},
  {"id": "lex.en.200k.059000", "hw": "summer tanager", "pos": "phrase", "ipa": "/ˈsʌmər ˈtænədʒər/", "vi": "chim hồng y đỏ mùa hè"},
  {"id": "lex.en.200k.059001", "hw": "swamp dewberry", "pos": "phrase", "ipa": "/swɑːmp ˈduːbɛri/", "vi": "dâu mâm xôi mọc đầm lầy"}
]

with open('scratch/b32_r08_raw_p5.json') as f:
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

with open('scratch/b32_r08_p5.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Part 5 validated and written successfully.")
