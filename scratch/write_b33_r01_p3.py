import json

items = [
  {"id": "lex.en.200k.060203", "hw": "speedups", "pos": "noun", "ipa": "/ˈspiːdʌps/", "vi": "sự tăng tốc độ; sự tăng tiến độ"},
  {"id": "lex.en.200k.060204", "hw": "sporks", "pos": "noun", "ipa": "/spɔːrks/", "vi": "muỗng nĩa kết hợp; thìa kèm nĩa"},
  {"id": "lex.en.200k.060205", "hw": "spymasters", "pos": "noun", "ipa": "/ˈspaɪmæstərz/", "vi": "trùm điệp viên; chỉ huy tình báo"},
  {"id": "lex.en.200k.060206", "hw": "stablemates", "pos": "noun", "ipa": "/ˈsteɪblmeɪts/", "vi": "ngựa chung chuồng; bạn cùng chuồng"},
  {"id": "lex.en.200k.060207", "hw": "stendhals", "pos": "noun", "ipa": "/stænˈdɑːlz/", "vi": "đại văn hào Pháp Stendhal"},
  {"id": "lex.en.200k.060208", "hw": "sunbelts", "pos": "noun", "ipa": "/ˈsʌnbɛlts/", "vi": "vành đai Mặt Trời nắng ấm nam Mỹ"},
  {"id": "lex.en.200k.060209", "hw": "supernatants", "pos": "noun", "ipa": "/ˌsuːpərˈneɪtənts/", "vi": "chất lỏng nổi trên bề mặt lắng"},
  {"id": "lex.en.200k.060210", "hw": "symbolists", "pos": "noun", "ipa": "/ˈsɪmbəlɪsts/", "vi": "nghệ sĩ phái chủ nghĩa tượng trưng"},
  {"id": "lex.en.200k.060211", "hw": "tarquins", "pos": "noun", "ipa": "/ˈtɑːrkwɪnz/", "vi": "vua bạo chúa Tarquin La Mã"},
  {"id": "lex.en.200k.060212", "hw": "tharps", "pos": "noun", "ipa": "/θɑːrps/", "vi": "biên đạo múa Twyla Tharp"},
  {"id": "lex.en.200k.060213", "hw": "tientsins", "pos": "noun", "ipa": "/tɪˈɛntsɪnz/", "vi": "thành phố Thiên Tân Trung Quốc"},
  {"id": "lex.en.200k.060214", "hw": "toques", "pos": "noun", "ipa": "/toʊks/", "vi": "mũ đầu bếp cao; mũ vành nhỏ phụ nữ"},
  {"id": "lex.en.200k.060215", "hw": "tympanums", "pos": "noun", "ipa": "/ˈtɪmpənəmz/", "vi": "màng nhĩ tai; bức vòm trán cửa"},
  {"id": "lex.en.200k.060216", "hw": "valuers", "pos": "noun", "ipa": "/ˈvæljuːərz/", "vi": "chuyên viên định giá tài sản"},
  {"id": "lex.en.200k.060217", "hw": "vaulters", "pos": "noun", "ipa": "/ˈvɔːltərz/", "vi": "vận động viên thi nhảy sào cao"},
  {"id": "lex.en.200k.060218", "hw": "villards", "pos": "noun", "ipa": "/vɪˈlɑːrdz/", "vi": "nhà tài chính báo chí Henry Villard"},
  {"id": "lex.en.200k.060219", "hw": "weenier", "pos": "adj", "ipa": "/ˈwiːniər/", "vi": "nhỏ xíu hơn; tí hon nhỏ bé hơn"},
  {"id": "lex.en.200k.060220", "hw": "weeniest", "pos": "adj", "ipa": "/ˈwiːniɪst/", "vi": "nhỏ xíu nhất; bé bỏng tí hon nhất"},
  {"id": "lex.en.200k.060221", "hw": "whackier", "pos": "adj", "ipa": "/ˈwækiər/", "vi": "kỳ quặc hơn; quái gở lố lăng hơn"},
  {"id": "lex.en.200k.060222", "hw": "whackiest", "pos": "adj", "ipa": "/ˈwækiɪst/", "vi": "kỳ quặc nhất; điên rồ lố bịch nhất"},
  {"id": "lex.en.200k.060223", "hw": "wigners", "pos": "noun", "ipa": "/ˈvɪɡnərz/", "vi": "nhà vật lý Nobel Eugene Wigner"},
  {"id": "lex.en.200k.060224", "hw": "yavapais", "pos": "noun", "ipa": "/ˈjɑːvəpaɪz/", "vi": "bộ tộc thổ dân da đỏ Yavapai Mỹ"},
  {"id": "lex.en.200k.060225", "hw": "yerkeses", "pos": "noun", "ipa": "/ˈjɜːrkiːzɪz/", "vi": "nhà tâm lý học Robert Yerkes"},
  {"id": "lex.en.200k.060226", "hw": "zephaniahs", "pos": "noun", "ipa": "/ˌzɛfəˈnaɪəz/", "vi": "tiên tri Xô-phô-ni-a Cựu Ước"},
  {"id": "lex.en.200k.060227", "hw": "abies grandis", "pos": "phrase", "ipa": "/ˈeɪbiːz ˈɡrændɪs/", "vi": "loài linh sam bạc khổng lồ bờ tây"},
  {"id": "lex.en.200k.060228", "hw": "aleksandr pavlovich", "pos": "phrase", "ipa": "/ˌælɪkˈsændər ˈpɑːvləvɪtʃ/", "vi": "Sa hoàng Aleksandr I của Nga"},
  {"id": "lex.en.200k.060229", "hw": "american hellebore", "pos": "phrase", "ipa": "/əˈmɛrɪkən ˈhɛlɪbɔːr/", "vi": "cây lê lô xanh kịch độc Bắc Mỹ"},
  {"id": "lex.en.200k.060230", "hw": "anterograde amnesia", "pos": "phrase", "ipa": "/ˌæntəroʊɡreɪd æmˈniːʒə/", "vi": "chứng quên về sau; mất nhớ xuôi"},
  {"id": "lex.en.200k.060231", "hw": "arnold gesell", "pos": "phrase", "ipa": "/ˈɑːrnəld ɡəˈzɛl/", "vi": "nhà tâm lý trẻ em Arnold Gesell"},
  {"id": "lex.en.200k.060232", "hw": "atrophic arthritis", "pos": "phrase", "ipa": "/eɪˈtrɑːfɪk ɑːrˈθraɪtɪs/", "vi": "bệnh viêm khớp biến dạng teo cơ"},
  {"id": "lex.en.200k.060233", "hw": "black hellebore", "pos": "phrase", "ipa": "/blæk ˈhɛlɪbɔːr/", "vi": "cây hoa hồng Giáng sinh hắc lê lô"},
  {"id": "lex.en.200k.060234", "hw": "bombay ceiba", "pos": "phrase", "ipa": "/bɑːmˈbeɪ ˈseɪbə/", "vi": "cây gạo hoa đỏ; cây bông gòn đỏ"},
  {"id": "lex.en.200k.060235", "hw": "bornholm disease", "pos": "phrase", "ipa": "/ˈbɔːrnhɔːlm dɪˈziːz/", "vi": "bệnh đau cơ dịch tễ Bornholm"},
  {"id": "lex.en.200k.060236", "hw": "bos indicus", "pos": "phrase", "ipa": "/bɑːs ˈɪndɪkəs/", "vi": "loài bò Zebu u lưng Ấn Độ"},
  {"id": "lex.en.200k.060237", "hw": "bouvet island", "pos": "phrase", "ipa": "/buːˈveɪ ˈaɪlənd/", "vi": "hòn đảo núi lửa hoang đảo Bouvet"},
  {"id": "lex.en.200k.060238", "hw": "cephalopod mollusk", "pos": "phrase", "ipa": "/ˈsɛfələpɑːd ˈmɑːləsk/", "vi": "động vật chân đầu; lớp chân đầu"},
  {"id": "lex.en.200k.060239", "hw": "cornus florida", "pos": "phrase", "ipa": "/ˈkɔːrnəs ˈflɔːrɪdə/", "vi": "cây sơn thù du hoa nở rộ Florida"},
  {"id": "lex.en.200k.060240", "hw": "correlational analysis", "pos": "phrase", "ipa": "/ˌkɔːrəˈleɪʃənəl əˈnæləsɪs/", "vi": "phương pháp phân tích tương quan"},
  {"id": "lex.en.200k.060241", "hw": "correlational statistics", "pos": "phrase", "ipa": "/ˌkɔːrəˈleɪʃənəl stəˈtɪstɪks/", "vi": "thống kê hệ số tương quan số liệu"},
  {"id": "lex.en.200k.060242", "hw": "el muerto", "pos": "phrase", "ipa": "/ɛl ˈmwɛərtoʊ/", "vi": "ngọn núi lửa El Muerto dãy Andes"},
  {"id": "lex.en.200k.060243", "hw": "ernst lubitsch", "pos": "phrase", "ipa": "/ɛrnst ˈluːbɪtʃ/", "vi": "đạo diễn điện ảnh Ernst Lubitsch"},
  {"id": "lex.en.200k.060244", "hw": "false hellebore", "pos": "phrase", "ipa": "/fɔːls ˈhɛlɪbɔːr/", "vi": "cây lê lô độc; cây cúc lê lô giả"},
  {"id": "lex.en.200k.060245", "hw": "false tamarisk", "pos": "phrase", "ipa": "/fɔːls ˈtæmərɪsk/", "vi": "cây liễu bách giả; cây trắc bá giả"},
  {"id": "lex.en.200k.060246", "hw": "gabonese republic", "pos": "phrase", "ipa": "/ˌɡæbəˈniːz rɪˈpʌblɪk/", "vi": "Cộng hòa Gabon ở Trung Phi"},
  {"id": "lex.en.200k.060247", "hw": "genus catalpa", "pos": "phrase", "ipa": "/ˈdʒiːnəs kəˈtælpə/", "vi": "chi cây kèn vàng trĩu hoa Catalpa"},
  {"id": "lex.en.200k.060248", "hw": "genus ceiba", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈseɪbə/", "vi": "chi cây bông gòn thân gai Ceiba"},
  {"id": "lex.en.200k.060249", "hw": "genus coleus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈkoʊliəs/", "vi": "chi cây tía tô cảnh ngũ sắc Coleus"},
  {"id": "lex.en.200k.060250", "hw": "genus dryas", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈdraɪəs/", "vi": "chi cỏ hàn đới tám cánh hoa Dryas"},
  {"id": "lex.en.200k.060251", "hw": "genus freesia", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈfriːʒiə/", "vi": "chi hoa lan dạ hương thơm Freesia"},
  {"id": "lex.en.200k.060252", "hw": "genus junco", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈdʒʌŋkoʊ/", "vi": "chi chim sẻ tuyết Junco Bắc Mỹ"},
  {"id": "lex.en.200k.060253", "hw": "genus ulmus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈʌlməs/", "vi": "chi cây du rụng lá họ Du Ulmaceae"},
  {"id": "lex.en.200k.060254", "hw": "german tamarisk", "pos": "phrase", "ipa": "/ˈdʒɜːrmən ˈtæmərɪsk/", "vi": "cây liễu bách Đức hoa chùm hồng"},
  {"id": "lex.en.200k.060255", "hw": "green hellebore", "pos": "phrase", "ipa": "/ɡriːn ˈhɛlɪbɔːr/", "vi": "cây thiết bao hoa xanh lục độc"},
  {"id": "lex.en.200k.060256", "hw": "grigori potemkin", "pos": "phrase", "ipa": "/ɡrɪˈɡɔːri poʊˈtɛmkɪn/", "vi": "Thống chế Nga Grigori Potemkin"},
  {"id": "lex.en.200k.060257", "hw": "gros ventre", "pos": "phrase", "ipa": "/ɡroʊ ˈvɑːntrə/", "vi": "bộ tộc da đỏ Gros Ventre Bắc Mỹ"},
  {"id": "lex.en.200k.060258", "hw": "heterodyne receiver", "pos": "phrase", "ipa": "/ˈhɛtərədaɪn rɪˈsiːvər/", "vi": "máy thu sóng vô tuyến ngoại sai"},
  {"id": "lex.en.200k.060259", "hw": "hieratic script", "pos": "phrase", "ipa": "/haɪəˈrætɪk skrɪpt/", "vi": "chữ viết thảo giáo phẩm Ai Cập cổ"},
  {"id": "lex.en.200k.060260", "hw": "hottentot bread vine", "pos": "phrase", "ipa": "/ˈhɑːtntɑːt brɛd vaɪn/", "vi": "dây leo củ chân voi dại Nam Phi"},
  {"id": "lex.en.200k.060261", "hw": "jacques lucien monod", "pos": "phrase", "ipa": "/ʒɑːk lyˈsjɛ̃ː moʊˈnoʊ/", "vi": "nhà sinh học Nobel Jacques Monod"},
  {"id": "lex.en.200k.060262", "hw": "john broadus watson", "pos": "phrase", "ipa": "/dʒɑːn ˈbrɔːdəs ˈwɑːtsən/", "vi": "nhà tâm lý học hành vi John Watson"},
  {"id": "lex.en.200k.060263", "hw": "karl baedeker", "pos": "phrase", "ipa": "/kɑːrl ˈbɛdɪkər/", "vi": "nhà xuất bản sách du lịch Baedeker"},
  {"id": "lex.en.200k.060264", "hw": "karl czerny", "pos": "phrase", "ipa": "/kɑːrl ˈtʃɜːrni/", "vi": "nhà soạn nhạc piano Karl Czerny"},
  {"id": "lex.en.200k.060265", "hw": "kia quen", "pos": "phrase", "ipa": "/kiːɑː kwɛn/", "vi": "huyện tự trị Cáp Nhĩ Kiềm"},
  {"id": "lex.en.200k.060266", "hw": "listeria monocytogenes", "pos": "phrase", "ipa": "/lɪˈstɪəriə ˌmɑːnoʊsaɪˈtɑːdʒɪniːz/", "vi": "khuẩn listeria gây ngộ độc thức ăn"},
  {"id": "lex.en.200k.060267", "hw": "macrobiotic diet", "pos": "phrase", "ipa": "/ˌmækroʊbaɪˈɑːtɪk ˈdaɪət/", "vi": "chế độ ăn thực dưỡng dưỡng sinh"},
  {"id": "lex.en.200k.060268", "hw": "monica seles", "pos": "phrase", "ipa": "/ˈmɑːnɪkə ˈsɛlɪʃ/", "vi": "ngôi sao quần vợt Monica Seles"},
  {"id": "lex.en.200k.060269", "hw": "paul hindemith", "pos": "phrase", "ipa": "/pɔːl ˈhɪndəmɪt/", "vi": "nhà soạn nhạc Paul Hindemith"},
  {"id": "lex.en.200k.060270", "hw": "pingpong paddle", "pos": "phrase", "ipa": "/ˈpɪŋpɑːŋ ˈpædl/", "vi": "vợt đánh bóng bàn có mút"},
  {"id": "lex.en.200k.060271", "hw": "prothrombin accelerator", "pos": "phrase", "ipa": "/proʊˈθrɑːmbɪn ækˈsɛləreɪtər/", "vi": "yếu tố đông máu V xúc tác máu"},
  {"id": "lex.en.200k.060272", "hw": "robert mearns yerkes", "pos": "phrase", "ipa": "/ˈrɑːbərt mɪərnz ˈjɜːrkiːz/", "vi": "nhà linh trưởng học Robert Yerkes"},
  {"id": "lex.en.200k.060273", "hw": "salix cinerea", "pos": "phrase", "ipa": "/ˈseɪlɪks sɪˈnɪriə/", "vi": "loài liễu xám tro bụi rậm châu Âu"},
  {"id": "lex.en.200k.060274", "hw": "serratus muscles", "pos": "phrase", "ipa": "/səˈreɪtəs ˈmʌslz/", "vi": "các bó cơ hình răng cưa lồng ngực"},
  {"id": "lex.en.200k.060275", "hw": "subacute bacterial endocarditis", "pos": "phrase", "ipa": "/ˌsʌbəˈkjuːt bækˈtɪəriəl ˌɛndoʊkɑːrˈdaɪtɪs/", "vi": "viêm nội tâm mạc khuẩn bán cấp"},
  {"id": "lex.en.200k.060276", "hw": "tall bilberry", "pos": "phrase", "ipa": "/tɔːl ˈbɪlbɛri/", "vi": "cây việt quất thân cao quả đen"},
  {"id": "lex.en.200k.060277", "hw": "tamarisk family", "pos": "phrase", "ipa": "/ˈtæmərɪsk ˈfæməli/", "vi": "họ thực vật liễu bách thạch nam"},
  {"id": "lex.en.200k.060278", "hw": "tartaric acid", "pos": "phrase", "ipa": "/tɑːrˈtærɪk ˈæsɪd/", "vi": "axit tartaric tự nhiên của nho"},
  {"id": "lex.en.200k.060279", "hw": "theodore dreiser", "pos": "phrase", "ipa": "/ˈθiːədɔːr ˈdraɪzər/", "vi": "nhà văn Mỹ Theodore Dreiser"},
  {"id": "lex.en.200k.060280", "hw": "white hellebore", "pos": "phrase", "ipa": "/waɪt ˈhɛlɪbɔːr/", "vi": "cây bạch lê lô hoa trắng kịch độc"},
  {"id": "lex.en.200k.060281", "hw": "whomp up", "pos": "phrase", "ipa": "/wɑːmp ʌp/", "vi": "làm vội vàng; nấu nhanh qua loa"},
  {"id": "lex.en.200k.060282", "hw": "william hubbs rehnquist", "pos": "phrase", "ipa": "/ˈwɪljəm hʌbz ˈrɛŋkwɪst/", "vi": "Chánh án Tối cao William Rehnquist"},
  {"id": "lex.en.200k.060283", "hw": "wisteria chinensis", "pos": "phrase", "ipa": "/wɪˈstɪəriə tʃaɪˈnɛnsɪs/", "vi": "dây hoa tử đằng tím Trung Quốc"},
  {"id": "lex.en.200k.060284", "hw": "agones", "pos": "noun", "ipa": "/əˈɡoʊniːz/", "vi": "các cuộc tranh tài thể thao Hy Lạp"},
  {"id": "lex.en.200k.060285", "hw": "agons", "pos": "noun", "ipa": "/ˈæɡɑːnz/", "vi": "cuộc thi tài kịch nghệ Hy Lạp cổ"},
  {"id": "lex.en.200k.060286", "hw": "antacids", "pos": "noun", "ipa": "/æntˈæsɪdz/", "vi": "thuốc kháng axit trung hòa dạ dày"},
  {"id": "lex.en.200k.060287", "hw": "assessees", "pos": "noun", "ipa": "/ˌæsɛˈsiːz/", "vi": "người nộp thuế được định giá"},
  {"id": "lex.en.200k.060288", "hw": "bellarmines", "pos": "noun", "ipa": "/ˈbɛlərmɪnz/", "vi": "bình gốm cổ tráng men Bellarmine"},
  {"id": "lex.en.200k.060289", "hw": "bibliophiles", "pos": "noun", "ipa": "/ˈbɪblioʊfaɪlz/", "vi": "người say mê sưu tầm sách quý hiếm"},
  {"id": "lex.en.200k.060290", "hw": "bicennaries", "pos": "noun", "ipa": "/baɪˈsɛntənɛriz/", "vi": "đại lễ kỷ niệm hai trăm năm"},
  {"id": "lex.en.200k.060291", "hw": "bicentenaries", "pos": "noun", "ipa": "/ˌbaɪsɛnˈtɛnəriz/", "vi": "dịp kỷ niệm hai trăm năm"},
  {"id": "lex.en.200k.060292", "hw": "binets", "pos": "noun", "ipa": "/bɪˈneɪz/", "vi": "nhà tâm lý học Alfred Binet"},
  {"id": "lex.en.200k.060293", "hw": "bloodstones", "pos": "noun", "ipa": "/ˈblʌdstoʊnz/", "vi": "đá máu huyết thạch có đốm đỏ"},
  {"id": "lex.en.200k.060294", "hw": "bluefishes", "pos": "noun", "ipa": "/ˈbluːfɪʃɪz/", "vi": "loài cá ngàng xanh săn mồi hung dữ"},
  {"id": "lex.en.200k.060295", "hw": "boors", "pos": "noun", "ipa": "/bʊərz/", "vi": "kẻ cục cằn thô lỗ vụng về thô lậu"},
  {"id": "lex.en.200k.060296", "hw": "boules", "pos": "noun", "ipa": "/buːlz/", "vi": "khối tinh thể; quả bi sắt Pháp"},
  {"id": "lex.en.200k.060297", "hw": "brakemen", "pos": "noun", "ipa": "/ˈbreɪkmən/", "vi": "nhân viên phụ trách hãm phanh tàu"},
  {"id": "lex.en.200k.060298", "hw": "carpers", "pos": "noun", "ipa": "/ˈkɑːrpərz/", "vi": "kẻ chuyên bới lông tìm vết bắt bẻ"},
  {"id": "lex.en.200k.060299", "hw": "charlerois", "pos": "noun", "ipa": "/ˈʃɑːrlərwɑːz/", "vi": "thành phố công nghiệp Charleroi Bỉ"},
  {"id": "lex.en.200k.060300", "hw": "choirmasters", "pos": "noun", "ipa": "/ˈkwaɪərmæstərz/", "vi": "chỉ huy dàn hợp xướng ca đoàn"},
  {"id": "lex.en.200k.060301", "hw": "civets", "pos": "noun", "ipa": "/ˈsɪvɪts/", "vi": "con cầy hương; chất xạ hương cầy"},
  {"id": "lex.en.200k.060302", "hw": "closeouts", "pos": "noun", "ipa": "/ˈkloʊzaʊts/", "vi": "đợt xả hàng tồn kho thanh lý rẻ"}
]

with open('scratch/b33_r01_raw_p3.json') as f:
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

with open('scratch/b33_r01_p3.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Batch 33 Round 1 Part 3 validated and written successfully.")
