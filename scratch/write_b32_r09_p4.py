import json

items = [
  {"id": "lex.en.200k.059303", "hw": "riboses", "pos": "noun", "ipa": "/rˈaɪboʊsɪz/", "vi": "đường đơn ribose trong ARN"},
  {"id": "lex.en.200k.059304", "hw": "roselles", "pos": "noun", "ipa": "/roʊzˈɛlz/", "vi": "cây bụp giấm hoa atiso đỏ"},
  {"id": "lex.en.200k.059305", "hw": "scherzi", "pos": "noun", "ipa": "/skˈɛrtsiː/", "vi": "các khúc nhạc scherzo vui nhộn"},
  {"id": "lex.en.200k.059306", "hw": "scherzos", "pos": "noun", "ipa": "/skˈɛrtsoʊz/", "vi": "khúc nhạc scherzo vui tươi nhanh"},
  {"id": "lex.en.200k.059307", "hw": "sclerodermas", "pos": "noun", "ipa": "/sklˌɛrədˈɜːrməz/", "vi": "chứng bệnh xơ cứng bì tự miễn"},
  {"id": "lex.en.200k.059308", "hw": "sculleries", "pos": "noun", "ipa": "/skˈʌləriz/", "vi": "gian rửa bát dọn dẹp phụ bếp"},
  {"id": "lex.en.200k.059309", "hw": "segregationists", "pos": "noun", "ipa": "/sˌɛɡrəɡˈeɪʃənɪsts/", "vi": "kẻ chủ trương phân biệt chủng tộc"},
  {"id": "lex.en.200k.059310", "hw": "siltstones", "pos": "noun", "ipa": "/sˈɪltstoʊnz/", "vi": "đá trầm tích bột kết"},
  {"id": "lex.en.200k.059311", "hw": "sleepwalkers", "pos": "noun", "ipa": "/slˈipwˌɔkɚz/", "vi": "người mắc chứng mộng du ban đêm"},
  {"id": "lex.en.200k.059312", "hw": "soakers", "pos": "noun", "ipa": "/sˈoʊkɚz/", "vi": "cơn mưa tầm tã; kẻ bợm rượu"},
  {"id": "lex.en.200k.059313", "hw": "standers", "pos": "noun", "ipa": "/stˈændɚz/", "vi": "người đứng; giá đỡ chống"},
  {"id": "lex.en.200k.059314", "hw": "stitchers", "pos": "noun", "ipa": "/stˈɪtʃɚz/", "vi": "thợ may khâu; máy đóng gáy sách"},
  {"id": "lex.en.200k.059315", "hw": "strayers", "pos": "noun", "ipa": "/strˈeɪɚz/", "vi": "kẻ đi lạc hướng; thú lạc bầy"},
  {"id": "lex.en.200k.059316", "hw": "sundresses", "pos": "noun", "ipa": "/sˈʌndrɛsɪz/", "vi": "váy mùa hè hai dây thoáng mát"},
  {"id": "lex.en.200k.059317", "hw": "tamaracks", "pos": "noun", "ipa": "/tˈæməræks/", "vi": "cây thông rụng lá tamarack Mỹ"},
  {"id": "lex.en.200k.059318", "hw": "tankas", "pos": "noun", "ipa": "/tˈɑːŋkəz/", "vi": "thể thơ đoản ca tanka Nhật Bản"},
  {"id": "lex.en.200k.059319", "hw": "thbs", "pos": "noun", "ipa": "/θˌiːeɪtʃbˈiːz/", "vi": "bằng cử nhân thần học"},
  {"id": "lex.en.200k.059320", "hw": "topsails", "pos": "noun", "ipa": "/tˈɑːpseɪlz/", "vi": "cánh buồm trên tầng hai của tàu"},
  {"id": "lex.en.200k.059321", "hw": "transexuals", "pos": "noun", "ipa": "/trænzsˈɛkʃuːəlz/", "vi": "người phẫu thuật chuyển đổi giới"},
  {"id": "lex.en.200k.059322", "hw": "trypsins", "pos": "noun", "ipa": "/trˈɪpsɪnz/", "vi": "enzym tiêu hóa đạm trypsin"},
  {"id": "lex.en.200k.059323", "hw": "ulcerations", "pos": "noun", "ipa": "/ˌʌlsɚˈeɪʃənz/", "vi": "vết loét da niêm mạc; sự lở loét"},
  {"id": "lex.en.200k.059324", "hw": "vetches", "pos": "noun", "ipa": "/vˈɛtʃɪz/", "vi": "cây họ đậu vetch làm thức ăn"},
  {"id": "lex.en.200k.059325", "hw": "virions", "pos": "noun", "ipa": "/vˈɪriɑːnz/", "vi": "hạt vi-rút hoàn chỉnh virion"},
  {"id": "lex.en.200k.059326", "hw": "weals", "pos": "noun", "ipa": "/wˈiːlz/", "vi": "vết lằn roi sưng đỏ trên da"},
  {"id": "lex.en.200k.059327", "hw": "woodworkers", "pos": "noun", "ipa": "/wˈʊdwˌɜːrkɚz/", "vi": "thợ mộc điêu khắc chế tác gỗ"},
  {"id": "lex.en.200k.059328", "hw": "worshipers", "pos": "noun", "ipa": "/wˈɜːrʃɪpɚz/", "vi": "tín đồ sùng bái kính cẩn"},
  {"id": "lex.en.200k.059329", "hw": "zeolites", "pos": "noun", "ipa": "/zˈiːəlaɪts/", "vi": "khoáng chất nhôm silicat zeolit"},
  {"id": "lex.en.200k.059330", "hw": "zeps", "pos": "noun", "ipa": "/zˈɛps/", "vi": "bánh mì kẹp dài kiểu zeppelin"},
  {"id": "lex.en.200k.059331", "hw": "actinide series", "pos": "phrase", "ipa": "/ˈæktənaɪd ˈsɪriːz/", "vi": "dãy nguyên tố phóng xạ actini"},
  {"id": "lex.en.200k.059332", "hw": "actus reus", "pos": "phrase", "ipa": "/ˈæktəs ˈreɪəs/", "vi": "hành vi khách quan phạm tội"},
  {"id": "lex.en.200k.059333", "hw": "ahura mazda", "pos": "phrase", "ipa": "/əˈhʊərə ˈmæzdə/", "vi": "thần ánh sáng tối cao Ahura Mazda"},
  {"id": "lex.en.200k.059334", "hw": "aleksandr prokhorov", "pos": "phrase", "ipa": "/ˌælɪɡˈzændər ˈprɑːkərəf/", "vi": "nhà vật lý Aleksandr Prokhorov"},
  {"id": "lex.en.200k.059335", "hw": "apis mellifera", "pos": "phrase", "ipa": "/ˈeɪpɪs mɛˈlɪfərə/", "vi": "loài ong mật châu Âu"},
  {"id": "lex.en.200k.059336", "hw": "auricular appendage", "pos": "phrase", "ipa": "/ɔːˈrɪkjʊlər əˈpɛndɪdʒ/", "vi": "tiểu nhĩ của tâm nhĩ buồng tim"},
  {"id": "lex.en.200k.059337", "hw": "blue copperas", "pos": "phrase", "ipa": "/bluː ˈkɑːpərəs/", "vi": "phèn xanh đồng sunfat ngậm nước"},
  {"id": "lex.en.200k.059338", "hw": "bovine spongiform encephalitis", "pos": "phrase", "ipa": "/ˈboʊvaɪn ˈspʌndʒɪfɔːrm ɛnˌsɛfəˈlaɪtɪs/", "vi": "bệnh xốp não bò điên truyền nhiễm"},
  {"id": "lex.en.200k.059339", "hw": "calcined lime", "pos": "phrase", "ipa": "/ˈkælsɪfaɪd laɪm/", "vi": "vôi sống nung canxi oxit"},
  {"id": "lex.en.200k.059340", "hw": "cardiac glycoside", "pos": "phrase", "ipa": "/ˈkɑːrdiæk ˈɡlaɪkəsaɪd/", "vi": "thuốc glycosid trợ tim"},
  {"id": "lex.en.200k.059341", "hw": "charles francois gounod", "pos": "phrase", "ipa": "/ʃɑːrl frɑːnˈswɑː ɡuːˈnoʊ/", "vi": "nhà soạn nhạc Charles Gounod"},
  {"id": "lex.en.200k.059342", "hw": "choroid plexus", "pos": "phrase", "ipa": "/ˈkɔːrɔɪd ˈplɛksəs/", "vi": "đám rối màng đệm tiết dịch não"},
  {"id": "lex.en.200k.059343", "hw": "circumflex humeral artery", "pos": "phrase", "ipa": "/ˈsɜːrkəmflɛks ˈhjuːmərəl ˈɑːrtəri/", "vi": "động mạch mũ cánh tay"},
  {"id": "lex.en.200k.059344", "hw": "citrus nobilis", "pos": "phrase", "ipa": "/ˈsɪtrəs ˈnoʊbəlɪs/", "vi": "loài quýt ngọt Citrus nobilis"},
  {"id": "lex.en.200k.059345", "hw": "common speedwell", "pos": "phrase", "ipa": "/ˈkɑːmən ˈspiːdwɛl/", "vi": "cỏ rau má tây hoa tím veronica"},
  {"id": "lex.en.200k.059346", "hw": "compound pistil", "pos": "phrase", "ipa": "/ˈkɑːmpaʊnd ˈpɪstɪl/", "vi": "bộ nhụy kép nhiều lá noãn"},
  {"id": "lex.en.200k.059347", "hw": "corn speedwell", "pos": "phrase", "ipa": "/kɔːrn ˈspiːdwɛl/", "vi": "cỏ veronica hoa nhỏ đồng ruộng"},
  {"id": "lex.en.200k.059348", "hw": "deathwatch beetle", "pos": "phrase", "ipa": "/ˈdɛθwɑːtʃ ˈbiːtl/", "vi": "mọt gỗ gõ đầu tích tắc báo tử"},
  {"id": "lex.en.200k.059349", "hw": "eddy merckx", "pos": "phrase", "ipa": "/ˈɛdi mɛrks/", "vi": "tay đua xe đạp Eddy Merckx"},
  {"id": "lex.en.200k.059350", "hw": "ethelred ii", "pos": "phrase", "ipa": "/ˈɛθəlrɛd ðə ˈsɛkənd/", "vi": "vua Anh Ethelred Không Sẵn Sàng"},
  {"id": "lex.en.200k.059351", "hw": "field speedwell", "pos": "phrase", "ipa": "/fiːld ˈspiːdwɛl/", "vi": "loài cỏ rau má tây đồng nội"},
  {"id": "lex.en.200k.059352", "hw": "genus diplodocus", "pos": "phrase", "ipa": "/ˈdʒiːnəs dɪˈplɑːdəkəs/", "vi": "chi khủng long cổ dài Diplodocus"},
  {"id": "lex.en.200k.059353", "hw": "genus leishmania", "pos": "phrase", "ipa": "/ˈdʒiːnəs liːʃˈmeɪniə/", "vi": "chi đơn bào Leishmania"},
  {"id": "lex.en.200k.059354", "hw": "genus lilium", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈlɪliəm/", "vi": "chi thực vật hoa loa kèn hoa ly"},
  {"id": "lex.en.200k.059355", "hw": "genus naja", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈneɪdʒə/", "vi": "chi rắn hổ mang độc Naja"},
  {"id": "lex.en.200k.059356", "hw": "genus noctua", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈnɑːktʃʊə/", "vi": "chi bướm đêm ngài cú Noctua"},
  {"id": "lex.en.200k.059357", "hw": "genus protea", "pos": "phrase", "ipa": "/ˈdʒiːnəs proʊˈtiːə/", "vi": "chi hoa đường bệ Nam Phi Protea"},
  {"id": "lex.en.200k.059358", "hw": "genus vinca", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈvɪŋkə/", "vi": "chi thực vật cây dừa cạn Vinca"},
  {"id": "lex.en.200k.059359", "hw": "greater rhomboid muscle", "pos": "phrase", "ipa": "/ˈɡreɪtər ˈrɑːmbɔɪd ˈmʌsl/", "vi": "cơ trám lớn ở lưng"},
  {"id": "lex.en.200k.059360", "hw": "gustatory modality", "pos": "phrase", "ipa": "/ˈɡʌstətɔːri moʊˈdæləti/", "vi": "giác quan cảm nhận vị giác"},
  {"id": "lex.en.200k.059361", "hw": "haleakala national park", "pos": "phrase", "ipa": "/hˌɑːliˌɑːkəˈlɑː ˈnæʃənəl pɑːrk/", "vi": "Vườn quốc gia Haleakalā Hawaii"},
  {"id": "lex.en.200k.059362", "hw": "hypostasis of christ", "pos": "phrase", "ipa": "/haɪˈpɑːstəsɪs əv kraɪst/", "vi": "bản vị hợp nhất của Chúa Kitô"},
  {"id": "lex.en.200k.059363", "hw": "ischemic anoxia", "pos": "phrase", "ipa": "/ɪsˈkiːmɪk ænˈɑːksiə/", "vi": "thiếu oxy do thiếu máu cục bộ"},
  {"id": "lex.en.200k.059364", "hw": "islets of langerhans", "pos": "phrase", "ipa": "/ˈaɪlɪts əv ˈlɑːŋɡərhɑːnz/", "vi": "đảo tụy nội tiết Langerhans"},
  {"id": "lex.en.200k.059365", "hw": "italo calvino", "pos": "phrase", "ipa": "/ˈiːtəloʊ kælˈviːnoʊ/", "vi": "nhà văn Ý Italo Calvino"},
  {"id": "lex.en.200k.059366", "hw": "jackknife clam", "pos": "phrase", "ipa": "/ˈdʒæknaɪf klæm/", "vi": "loài nghêu móng tay vỏ dài"},
  {"id": "lex.en.200k.059367", "hw": "john millington synge", "pos": "phrase", "ipa": "/dʒɑːn ˈmɪlɪŋtən sɪŋ/", "vi": "nhà soạn kịch John M. Synge"},
  {"id": "lex.en.200k.059368", "hw": "juice reamer", "pos": "phrase", "ipa": "/dʒuːs ˈriːmər/", "vi": "dụng cụ xoay vắt cam chanh múi"},
  {"id": "lex.en.200k.059369", "hw": "junipero serra", "pos": "phrase", "ipa": "/huːˈniːpɛroʊ ˈsɛrə/", "vi": "tu sĩ truyền giáo Junípero Serra"},
  {"id": "lex.en.200k.059370", "hw": "kahlil gibran", "pos": "phrase", "ipa": "/kɑːˈliːl dʒɪbrˈɑːn/", "vi": "nhà thơ triết gia Kahlil Gibran"},
  {"id": "lex.en.200k.059371", "hw": "kit and boodle", "pos": "phrase", "ipa": "/kɪt ənd ˈbuːdl/", "vi": "tất cả mọi thứ trọn gói"},
  {"id": "lex.en.200k.059372", "hw": "lesser rhomboid muscle", "pos": "phrase", "ipa": "/ˈlɛsər ˈrɑːmbɔɪd ˈmʌsl/", "vi": "cơ trám bé ở vùng lưng trên"},
  {"id": "lex.en.200k.059373", "hw": "lobster thermidor", "pos": "phrase", "ipa": "/ˈlɑːbstər ˌθɜːrmɪˈdɔːr/", "vi": "món tôm hùm đút lò Thermidor"},
  {"id": "lex.en.200k.059374", "hw": "luigi pirandello", "pos": "phrase", "ipa": "/luˈiːdʒi ˌpɪrənˈdɛloʊ/", "vi": "nhà viết kịch Luigi Pirandello"},
  {"id": "lex.en.200k.059375", "hw": "malice aforethought", "pos": "phrase", "ipa": "/ˈmælɪs əˈfɔːrθɔːt/", "vi": "ác ý tính toán mưu sát từ trước"},
  {"id": "lex.en.200k.059376", "hw": "malignant neuroma", "pos": "phrase", "ipa": "/məˈlɪɡnənt nʊˈroʊmə/", "vi": "khối u thần kinh ác tính"},
  {"id": "lex.en.200k.059377", "hw": "manx shearwater", "pos": "phrase", "ipa": "/mæŋks ˈʃɪərwɔːtər/", "vi": "loài chim hải âu Manx xẻ cánh"},
  {"id": "lex.en.200k.059378", "hw": "maxim gorki", "pos": "phrase", "ipa": "/ˈmæksɪm ˈɡɔːrki/", "vi": "đại văn hào Maxim Gorky"},
  {"id": "lex.en.200k.059379", "hw": "medgar wiley evers", "pos": "phrase", "ipa": "/ˈmɛdɡər ˈwaɪli ˈɛvərz/", "vi": "nhà đấu tranh Medgar Wiley Evers"},
  {"id": "lex.en.200k.059380", "hw": "medulla oblongata", "pos": "phrase", "ipa": "/mɪˈdʌlə ˌɑːblɔːŋˈɡɑːtə/", "vi": "hành não của thân não"},
  {"id": "lex.en.200k.059381", "hw": "myasthenia gravis", "pos": "phrase", "ipa": "/ˌmaɪəsˈθiːniə ˈɡrævɪs/", "vi": "bệnh nhược cơ tự miễn mạn tính"},
  {"id": "lex.en.200k.059382", "hw": "newburg sauce", "pos": "phrase", "ipa": "/ˈnuːbɜːrɡ sɔːs/", "vi": "sốt kem bơ rượu vang Newburg"},
  {"id": "lex.en.200k.059383", "hw": "ohmic resistance", "pos": "phrase", "ipa": "/ˈoʊmɪk rɪˈzɪstəns/", "vi": "điện trở thuần Ôm"},
  {"id": "lex.en.200k.059384", "hw": "panthera tigris", "pos": "phrase", "ipa": "/pænˈθɪərə ˈtaɪɡrɪs/", "vi": "loài hổ chúa sơn lâm"},
  {"id": "lex.en.200k.059385", "hw": "passive resister", "pos": "phrase", "ipa": "/ˈpæsɪv rɪˈzɪstər/", "vi": "người kháng cự bất bạo động"},
  {"id": "lex.en.200k.059386", "hw": "pomme blanche", "pos": "phrase", "ipa": "/pɔːm blɑːnʃ/", "vi": "cây củ củ cải dại Prairie"},
  {"id": "lex.en.200k.059387", "hw": "pomme de prairie", "pos": "phrase", "ipa": "/pɔːm də prɛərˈiː/", "vi": "loài củ đậu thảo nguyên Bắc Mỹ"},
  {"id": "lex.en.200k.059388", "hw": "primum mobile", "pos": "phrase", "ipa": "/ˈpriːməm ˈmoʊbɪliː/", "vi": "động cơ đầu tiên; nguyên động lực"},
  {"id": "lex.en.200k.059389", "hw": "pythian games", "pos": "phrase", "ipa": "/ˈpɪθiən ɡeɪmz/", "vi": "đại hội thể thao Pythia Hy Lạp"},
  {"id": "lex.en.200k.059390", "hw": "ralph bunche", "pos": "phrase", "ipa": "/rælf bʌntʃ/", "vi": "nhà ngoại giao Nobel Ralph Bunche"},
  {"id": "lex.en.200k.059391", "hw": "ralph johnson bunche", "pos": "phrase", "ipa": "/rælf ˈdʒɑːnsən bʌntʃ/", "vi": "học giả Nobel Ralph Bunche"},
  {"id": "lex.en.200k.059392", "hw": "rhomboid minor muscle", "pos": "phrase", "ipa": "/ˈrɑːmbɔɪd ˈmaɪnər ˈmʌsl/", "vi": "cơ trám bé vùng lưng trên"},
  {"id": "lex.en.200k.059393", "hw": "rhomboid muscle", "pos": "phrase", "ipa": "/ˈrɑːmbɔɪd ˈmʌsl/", "vi": "nhóm cơ trám kéo xương bả vai"},
  {"id": "lex.en.200k.059394", "hw": "sigmund romberg", "pos": "phrase", "ipa": "/ˈsɪɡmənd ˈrɑːmbɜːrɡ/", "vi": "nhà soạn kịch Sigmund Romberg"},
  {"id": "lex.en.200k.059395", "hw": "simple pistil", "pos": "phrase", "ipa": "/ˈsɪmpl ˈpɪstɪl/", "vi": "nhụy hoa đơn một lá noãn"},
  {"id": "lex.en.200k.059396", "hw": "soiree musicale", "pos": "phrase", "ipa": "/swɑːˈreɪ mjuːzɪˈkæl/", "vi": "buổi tiệc âm nhạc dạ hội"},
  {"id": "lex.en.200k.059397", "hw": "spanish psyllium", "pos": "phrase", "ipa": "/ˈspænɪʃ ˈsɪliəm/", "vi": "hạt mã đề hạt đen Tây Ban Nha"},
  {"id": "lex.en.200k.059398", "hw": "spasmodic laryngitis", "pos": "phrase", "ipa": "/spæzˈmɑːdɪk ˌlærɪnˈdʒaɪtɪs/", "vi": "viêm thanh quản co thắt khàn tiếng"},
  {"id": "lex.en.200k.059399", "hw": "spiny softshell", "pos": "phrase", "ipa": "/ˈspaɪni ˈsɑːftʃɛl/", "vi": "loài ba ba gai mai mềm nước ngọt"},
  {"id": "lex.en.200k.059400", "hw": "stearic acid", "pos": "phrase", "ipa": "/stɪˈærɪk ˈæsɪd/", "vi": "axit béo no axit stearic"},
  {"id": "lex.en.200k.059401", "hw": "sulfur hexafluoride", "pos": "phrase", "ipa": "/ˈsʌlfər ˌhɛksəˈflʊəraɪd/", "vi": "khí lưu huỳnh hexaflorua"},
  {"id": "lex.en.200k.059402", "hw": "texas bluebonnet", "pos": "phrase", "ipa": "/ˈtɛksəs ˈbluːbɑːnɪt/", "vi": "hoa lupin bluebonnet Texas"}
]

with open('scratch/b32_r09_raw_p4.json') as f:
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

with open('scratch/b32_r09_p4.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Part 4 validated and written successfully.")
