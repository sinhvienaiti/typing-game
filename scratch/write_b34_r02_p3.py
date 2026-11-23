import json

items = [
    ("065703", "zapotecs", "noun", "/zəˈpoʊtɛks/", "người dân tộc Zapotec Mexico"),
    ("065704", "abscessed tooth", "phrase", "/ˈæbsɛst tuːθ/", "răng bị áp xe sưng mủ"),
    ("065705", "actinic keratosis", "phrase", "/ækˈtɪnɪk ˌkɛrəˈtoʊsɪs/", "chứng dày sừng do ánh sáng"),
    ("065706", "aspergillus fumigatus", "phrase", "/ˌæspərˈdʒɪləs ˌfjuːmɪˈɡeɪtəs/", "nấm mốc Aspergillus fumigatus"),
    ("065707", "autotrophic organism", "phrase", "/ˌɔːtəˈtrɒfɪk ˈɔːrɡənɪzəm/", "sinh vật tự dưỡng"),
    ("065708", "bristlecone fir", "phrase", "/ˈbrɪsəlˌkoʊn fɜːr/", "cây linh sam lá bắc Santa Lucia"),
    ("065709", "chlamydia trachomatis", "phrase", "/kləˈmɪdiə trəˈkoʊmətɪs/", "vi khuẩn Chlamydia trachomatis"),
    ("065710", "deictic word", "phrase", "/ˈdaɪktɪk wɜːrd/", "từ chỉ xuất (ngôn ngữ học)"),
    ("065711", "doxepin hydrochloride", "phrase", "/ˈdɒksɪpɪn ˌhaɪdrəˈklɔːraɪd/", "thuốc chống trầm cảm doxepin"),
    ("065712", "erica arborea", "phrase", "/ˈɛrɪkə ɑːrˈbɔːriə/", "cây thạch nam thân gỗ làm tẩu"),
    ("065713", "erlenmeyer flask", "phrase", "/ˈɜːrlənˌmaɪər flæsk/", "bình tam giác thí nghiệm"),
    ("065714", "ethmoid sinus", "phrase", "/ˈɛθmɔɪd ˈsaɪnəs/", "xoang sàng trong hộp sọ"),
    ("065715", "feast of dormition", "phrase", "/fiːst əv dɔːrˈmɪʃən/", "lễ Đức Mẹ yên giấc về trời"),
    ("065716", "ficus elastica", "phrase", "/ˈfaɪkəs ɪˈlæstɪkə/", "cây đa búp đỏ; cây đa cao su"),
    ("065717", "foveal vision", "phrase", "/ˈfoʊviəl ˈvɪʒən/", "thị lực vùng hố trung tâm"),
    ("065718", "francesco petrarca", "phrase", "/frænˈtʃɛskoʊ pɛˈtrɑːrkə/", "nhà thơ Ý Francesco Petrarca"),
    ("065719", "genus babesia", "phrase", "/ˈdʒiːnəs bəˈbiːʒə/", "chi ký sinh trùng máu Babesia"),
    ("065720", "genus bombyx", "phrase", "/ˈdʒiːnəs ˈbɒmbɪks/", "chi ngài tằm Bombyx"),
    ("065721", "genus caretta", "phrase", "/ˈdʒiːnəs kəˈrɛtə/", "chi rùa biển Caretta"),
    ("065722", "genus larrea", "phrase", "/ˈdʒiːnəs ˈlɑːriə/", "chi cây bụi sa mạc Larrea"),
    ("065723", "genus lithops", "phrase", "/ˈdʒiːnəs ˈlɪθɒps/", "chi cây đá sống Lithops"),
    ("065724", "genus osmanthus", "phrase", "/ˈdʒiːnəs ɒzˈmænθəs/", "chi hoa mộc hương Osmanthus"),
    ("065725", "genus papio", "phrase", "/ˈdʒiːnəs ˈpeɪpioʊ/", "chi khỉ đầu chó Papio"),
    ("065726", "genus paspalum", "phrase", "/ˈdʒiːnəs ˈpæspələm/", "chi cỏ san hô Paspalum"),
    ("065727", "genus phalaris", "phrase", "/ˈdʒiːnəs ˈfælərɪs/", "chi cỏ hoàng yến Phalaris"),
    ("065728", "genus potamogeton", "phrase", "/ˈdʒiːnəs ˌpɒtəmoʊˈdʒiːtɒn/", "chi cây thủy sinh Potamogeton"),
    ("065729", "genus sison", "phrase", "/ˈdʒiːnəs ˈsaɪsɒn/", "chi thực vật họ hoa tán Sison"),
    ("065730", "giant fulmar", "phrase", "/ˈdʒaɪənt ˈfʊlmər/", "chim hải âu lớn phương Nam"),
    ("065731", "giovanni battista cibo", "phrase", "/dʒoʊˈvɑːni bɑːˈtiːstɑː ˈtʃiːboʊ/", "Giáo hoàng Innocent VIII"),
    ("065732", "gulf of bothnia", "phrase", "/ɡʌlf əv ˈbɒθniə/", "vịnh Bothnia (Biển Baltic)"),
    ("065733", "heliothis zia", "phrase", "/ˌhiːliˈoʊθɪs ˈziːə/", "sâu đục bắp ngô; sâu khoang"),
    ("065734", "hoagy carmichael", "phrase", "/ˈhoʊɡi ˈkɑːrmaɪkəl/", "nhạc sĩ Mỹ Hoagy Carmichael"),
    ("065735", "hydrangea paniculata", "phrase", "/haɪˈdreɪndʒə pəˌnɪkjəˈleɪtə/", "hoa cẩm tú cầu chùy nón"),
    ("065736", "ivry la bataille", "phrase", "/ˌiːvri lɑː bəˈtaɪ/", "trận đánh Ivry-la-Bataille Pháp"),
    ("065737", "john barleycorn", "phrase", "/dʒɒn ˈbɑːrlikɔːrn/", "rượu mạch nha; biểu tượng lúa mạch"),
    ("065738", "juniperus virginiana", "phrase", "/dʒuːˈnɪpərəs vərˌdʒɪniˈeɪnə/", "cây bách xù đỏ Virginia"),
    ("065739", "karakorum range", "phrase", "/ˌkærəˈkɔːrəm reɪndʒ/", "dãy núi Karakorum ở châu Á"),
    ("065740", "louis auchincloss", "phrase", "/ˈluːɪs ˈɔːkɪnklɒs/", "nhà văn Mỹ Louis Auchincloss"),
    ("065741", "musculus adductor longus", "phrase", "/ˈmʌskjələs əˈdʌktər ˈlɒŋɡəs/", "cơ khép dài ở đùi"),
    ("065742", "nicolas de malebranche", "phrase", "/ˌniːkoʊˈlɑː də ˌmɑːlˈbrɒ̃ʃ/", "triết gia Nicolas de Malebranche"),
    ("065743", "panax ginseng", "phrase", "/ˈpænæks ˈdʒɪnsɛŋ/", "cây nhân sâm Triều Tiên"),
    ("065744", "purslane speedwell", "phrase", "/ˈpɜːrsleɪn ˈspiːdwɛl/", "cỏ thủy tiên lá rau sam Bắc Mỹ"),
    ("065745", "rhodope mountains", "phrase", "/ˈrɒdəpi ˈmaʊntənz/", "dãy núi Rhodope vùng Balkan"),
    ("065746", "ribes rubrum", "phrase", "/ˈraɪbiːz ˈruːbrəm/", "cây lý chua đỏ"),
    ("065747", "ringlet butterfly", "phrase", "/ˈrɪŋlɪt ˈbʌtərflaɪ/", "bướm mắt vòng họ Bướm giáp"),
    ("065748", "rose chafer", "phrase", "/roʊz ˈtʃeɪfər/", "bọ hung xanh ăn hoa hồng"),
    ("065749", "salix humilis", "phrase", "/ˈseɪlɪks ˈhjuːmɪlɪs/", "cây liễu lùn đồng cỏ Bắc Mỹ"),
    ("065750", "sealskin tent", "phrase", "/ˈsiːlskɪn tɛnt/", "lều bằng da hải cẩu"),
    ("065751", "sitta canadensis", "phrase", "/ˈsɪtə ˌkænəˈdɛnsɪs/", "chim trèo cây ngực hung"),
    ("065752", "sundew family", "phrase", "/ˈsʌnduː ˈfæməli/", "họ thực vật ăn thịt gọng vó"),
    ("065753", "sundew plant", "phrase", "/ˈsʌnduː plænt/", "cây gọng vó bắt côn trùng"),
    ("065754", "syringa vulgaris", "phrase", "/sɪˈrɪŋɡə vʌlˈɡɛərɪs/", "cây tử đinh hương thường"),
    ("065755", "tansy ragwort", "phrase", "/ˈtænzi ˈræɡwɜːrt/", "cây cúc dại độc tansy ragwort"),
    ("065756", "whooper swan", "phrase", "/ˈhuːpər swɒn/", "thiên nga lớn tiếng kêu vang"),
    ("065757", "actiums", "noun", "/ˈæktiəmz/", "trận hải chiến Actium cổ đại"),
    ("065758", "adventuresses", "noun", "/ədˈvɛntʃərɪsɪz/", "nữ nhà thám hiểm; nữ phiêu lưu"),
    ("065759", "aeginas", "noun", "/ɪˈdʒaɪnəz/", "đảo Aegina của Hy Lạp"),
    ("065760", "almoners", "noun", "/ˈɑːlmənərz/", "người phát bố thí; nhân viên y tế"),
    ("065761", "amatis", "noun", "/əˈmɑːtiz/", "đàn vĩ cầm chế tác bởi Amati"),
    ("065762", "amphiboles", "noun", "/ˈæmfɪˌboʊlz/", "khoáng vật silicat amphibol"),
    ("065763", "arawaks", "noun", "/ˈærəwɒks/", "người bản địa Arawak Nam Mỹ"),
    ("065764", "arethusas", "noun", "/ˌærəˈθuːzəz/", "hoa lan đầm lầy Arethusa"),
    ("065765", "athars", "noun", "/ˈʌtərz/", "tinh dầu hoa hồng attar"),
    ("065766", "bedpans", "noun", "/ˈbɛdˌpænz/", "bô vệ sinh cho bệnh nhân nằm"),
    ("065767", "birlings", "noun", "/ˈbɜːrlɪŋz/", "trò xoay khúc gỗ trên mặt nước"),
    ("065768", "bouffants", "noun", "/buːˈfɒnts/", "kiểu tóc đánh phồng; váy phồng"),
    ("065769", "bramantes", "noun", "/brəˈmɑːnteɪz/", "kiến trúc sư Phục Hưng Bramante"),
    ("065770", "bricolages", "noun", "/ˌbriːkəˈlɑːʒɪz/", "tác phẩm ghép từ vật có sẵn"),
    ("065771", "briths", "noun", "/brɪθs/", "nghi lễ cắt bao quy đầu Do Thái"),
    ("065772", "bronchiolitides", "noun", "/ˌbrɒŋkioʊlɪˈtaɪdɪz/", "bệnh viêm tiểu phế quản"),
    ("065773", "broodmares", "noun", "/ˈbruːdˌmɛərz/", "ngựa cái nuôi để sinh sản"),
    ("065774", "bungholes", "noun", "/ˈbʌŋˌhoʊlz/", "lỗ đóng nút thùng gỗ đựng rượu"),
    ("065775", "caravannings", "noun", "/ˈkærəˌvænɪŋz/", "chuyến du lịch bằng xe nhà"),
    ("065776", "cattails", "noun", "/ˈkætˌteɪlz/", "cây hương bồ nến nước đầm lầy"),
    ("065777", "cedarwoods", "noun", "/ˈsiːdərˌwʊdz/", "gỗ tuyết tùng thơm"),
    ("065778", "churchgoers", "noun", "/ˈtʃɜːrtʃˌɡoʊərz/", "người đi lễ nhà thờ thường xuyên"),
    ("065779", "clambakes", "noun", "/ˈklæmˌbeɪks/", "tiệc nướng hải sản ngoài bãi biển"),
    ("065780", "clubfeet", "noun", "/ˈklʌbˌfiːt/", "dị tật bàn chân khoèo bẩm sinh"),
    ("065781", "cockcrofts", "noun", "/ˈkɒkˌkrɒfts/", "nhà vật lý hạt nhân Cockcroft"),
    ("065782", "cookhouses", "noun", "/ˈkʊkˌhaʊzɪz/", "nhà bếp dã chiến; gian bếp ngoài"),
    ("065783", "coverlets", "noun", "/ˈkʌvərlɪts/", "khăn phủ giường dệt trang trí"),
    ("065784", "crataeguses", "noun", "/krəˈtiːɡəsɪz/", "cây sơn tra thuộc chi Crataegus"),
    ("065785", "crystallisations", "noun", "/ˌkrɪstəlaɪˈzeɪʃənz/", "sự kết tinh thành tinh thể"),
    ("065786", "cystines", "noun", "/ˈsɪstiːnz/", "axit amin cystine"),
    ("065787", "daumiers", "noun", "/doʊˈmjɛərz/", "họa sĩ biếm họa Pháp Daumier"),
    ("065788", "dhahrans", "noun", "/dɑːˈrɑːnz/", "thành phố dầu mỏ Dhahran Ả Rập"),
    ("065789", "dhals", "noun", "/dɑːlz/", "đậu lăng tách đôi; món súp đậu Ấn"),
    ("065790", "dichlorides", "noun", "/daɪˈklɔːraɪdz/", "hợp chất hóa học điclorua"),
    ("065791", "drawbars", "noun", "/ˈdrɔːˌbɑːrz/", "thanh kéo nối móc rơ-moóc"),
    ("065792", "dreys", "noun", "/dreɪz/", "tổ cành lá trên cây của loài sóc"),
    ("065793", "durableses", "noun", "/ˈdʊrəbəlz/", "hàng tiêu dùng lâu bền lâu dài"),
    ("065794", "eiras", "noun", "/ˈeɪrəz/", "chi thú chồn tayra Nam Mỹ Eira"),
    ("065795", "encomia", "noun", "/ɛnˈkoʊmiə/", "bài văn hay lời ca tụng tán dương"),
    ("065796", "encomiums", "noun", "/ɛnˈkoʊmiəmz/", "bài phát biểu ca ngợi tán dương"),
    ("065797", "exactas", "noun", "/ɪɡˈzæktəz/", "vé cược đoán đúng hai ngựa về đầu"),
    ("065798", "foliations", "noun", "/ˌfoʊliˈeɪʃənz/", "sự ra lá non; cấu trúc phân phiến"),
    ("065799", "forelimbs", "noun", "/ˈfɔːrˌlɪmz/", "chi trước của động vật"),
    ("065800", "gabardines", "noun", "/ˈɡæbərˌdiːnz/", "vải chéo gabardin may áo khoác"),
    ("065801", "gumdrops", "noun", "/ˈɡʌmˌdrɒps/", "kẹo dẻo hình nón phủ đường"),
    ("065802", "headstands", "noun", "/ˈhɛdˌstændz/", "tư thế trồng cây chuối bằng đầu"),
]

with open("scratch/b34_r02_raw_p3.json") as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100
allowed_pos = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det", "phrase"}

out = []
for r, (rid, hw, pos, ipa, vi) in zip(raw, items):
    assert r["id"].endswith("." + rid), f"ID mismatch: {r['id']} != {rid}"
    assert r["hw"] == hw, f"HW mismatch: {r['hw']} != {hw}"
    assert pos in allowed_pos, f"Bad POS {pos} for {hw}"
    assert len(vi) <= 35, f"VI too long ({len(vi)}): {hw} -> {vi}"
    assert ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2, f"Bad IPA: {hw} -> {ipa}"
    inner = ipa[1:-1]
    assert inner and not inner.startswith(" ") and not inner.endswith(" "), f"Empty/space IPA: {hw} -> {ipa}"
    rec = dict(r)
    rec["pos"] = pos
    rec["ipa"] = ipa
    rec["vi"] = vi
    rec["status"] = "reviewed"
    out.append(rec)

with open("scratch/b34_r02_p3.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r02_p3.json OK")
