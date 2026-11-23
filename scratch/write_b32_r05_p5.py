import json

records = [
    {"id": "lex.en.200k.057402", "hw": "smallholders", "pos": "noun", "ipa": "/ˈsmɔːlhoʊldɚz/", "vi": "chủ tiểu nông trang trại nhỏ"},
    {"id": "lex.en.200k.057403", "hw": "smidgens", "pos": "noun", "ipa": "/ˈsmɪdʒənz/", "vi": "những mẩu nhỏ; lượng rất ít"},
    {"id": "lex.en.200k.057404", "hw": "sorters", "pos": "noun", "ipa": "/ˈsɔːrtɚz/", "vi": "máy phân loại; người phân loại"},
    {"id": "lex.en.200k.057405", "hw": "squibbed", "pos": "verb", "ipa": "/skwɪbd/", "vi": "đã nổ xịt; đã bắn ngắn xịt"},
    {"id": "lex.en.200k.057406", "hw": "squibbing", "pos": "verb", "ipa": "/ˈskwɪbɪŋ/", "vi": "đang nổ xịt; đang đá bóng ngắn"},
    {"id": "lex.en.200k.057407", "hw": "squibs", "pos": "noun", "ipa": "/skwɪbz/", "vi": "pháo xịt; bài châm biếm ngắn"},
    {"id": "lex.en.200k.057408", "hw": "susas", "pos": "noun", "ipa": "/ˈsuːsəz/", "vi": "thành phố cảng cổ Susa ở Tunisia"},
    {"id": "lex.en.200k.057409", "hw": "synchronisations", "pos": "noun", "ipa": "/ˌsɪŋkrənaɪˈzeɪʃənz/", "vi": "sự đồng bộ hóa dữ liệu thời gian"},
    {"id": "lex.en.200k.057410", "hw": "tapirs", "pos": "noun", "ipa": "/ˈteɪpɚz/", "vi": "loài thú lợn vòi mũi dài"},
    {"id": "lex.en.200k.057411", "hw": "tegucigalpas", "pos": "noun", "ipa": "/təˌɡuːsɪˈɡælpəz/", "vi": "thủ đô Tegucigalpa Honduras"},
    {"id": "lex.en.200k.057412", "hw": "teherans", "pos": "noun", "ipa": "/tɛəˈrɑːnz/", "vi": "thủ đô Tehran nước Iran"},
    {"id": "lex.en.200k.057413", "hw": "thruways", "pos": "noun", "ipa": "/ˈθruːweɪz/", "vi": "tuyến đường cao tốc thông xe"},
    {"id": "lex.en.200k.057414", "hw": "trigeminals", "pos": "noun", "ipa": "/traɪˈdʒɛmɪnəlz/", "vi": "các dây thần kinh sinh ba mặt"},
    {"id": "lex.en.200k.057415", "hw": "udas", "pos": "noun", "ipa": "/ˈjuː.diː.eɪz/", "vi": "hiệp hội phòng vệ Ulster UDA"},
    {"id": "lex.en.200k.057416", "hw": "unriper", "pos": "adj", "ipa": "/ʌnˈraɪpər/", "vi": "xanh non hơn; chưa chín muồi hơn"},
    {"id": "lex.en.200k.057417", "hw": "unripest", "pos": "adj", "ipa": "/ʌnˈraɪpɪst/", "vi": "xanh non nhất; chưa chín nhất"},
    {"id": "lex.en.200k.057418", "hw": "vasculitides", "pos": "noun", "ipa": "/ˌvæskjʊˈlɪtɪdiːz/", "vi": "các chứng viêm thành mạch máu"},
    {"id": "lex.en.200k.057419", "hw": "verners", "pos": "noun", "ipa": "/ˈvɛrnɚz/", "vi": "nhà ngôn ngữ học Karl Verner"},
    {"id": "lex.en.200k.057420", "hw": "wakened", "pos": "verb", "ipa": "/ˈweɪkənd/", "vi": "đã thức giấc; đã đánh thức dậy"},
    {"id": "lex.en.200k.057421", "hw": "wakens", "pos": "verb", "ipa": "/ˈweɪkənz/", "vi": "thức giấc; đánh thức dậy"},
    {"id": "lex.en.200k.057422", "hw": "windbreakers", "pos": "noun", "ipa": "/ˈwɪndbreɪkɚz/", "vi": "áo khoác gió chắn gió mỏng"},
    {"id": "lex.en.200k.057423", "hw": "wonks", "pos": "noun", "ipa": "/wɑːŋks/", "vi": "chuyên gia mọt sách chuyên tâm"},
    {"id": "lex.en.200k.057424", "hw": "wringers", "pos": "noun", "ipa": "/ˈrɪŋɚz/", "vi": "máy vắt trục lăn; thử thách cam go"},
    {"id": "lex.en.200k.057425", "hw": "zhuangs", "pos": "noun", "ipa": "/dʒwɑːŋz/", "vi": "người Tráng hoặc tiếng Tráng"},
    {"id": "lex.en.200k.057426", "hw": "adenosine diphosphate", "pos": "phrase", "ipa": "", "vi": "hợp chất phân tử sinh học ADP"},
    {"id": "lex.en.200k.057427", "hw": "alleghany plum", "pos": "phrase", "ipa": "", "vi": "loài cây mận dại Alleghany"},
    {"id": "lex.en.200k.057428", "hw": "andre malraux", "pos": "phrase", "ipa": "", "vi": "nhà văn Pháp André Malraux"},
    {"id": "lex.en.200k.057429", "hw": "anemone occidentalis", "pos": "phrase", "ipa": "", "vi": "cây hoa phong quỳ miền tây Mỹ"},
    {"id": "lex.en.200k.057430", "hw": "archibald percival wavell", "pos": "phrase", "ipa": "", "vi": "thống chế Archibald Wavell của Anh"},
    {"id": "lex.en.200k.057431", "hw": "arsenic trioxide", "pos": "phrase", "ipa": "", "vi": "asen trioxit; thạch tín độc"},
    {"id": "lex.en.200k.057432", "hw": "banksia rose", "pos": "phrase", "ipa": "", "vi": "hoa hồng leo Banksia thơm nhẹ"},
    {"id": "lex.en.200k.057433", "hw": "bete noire", "pos": "phrase", "ipa": "", "vi": "mối ác cảm; kẻ bị căm ghét"},
    {"id": "lex.en.200k.057434", "hw": "book of tobit", "pos": "phrase", "ipa": "", "vi": "sách Tôbia trong Cựu Ước"},
    {"id": "lex.en.200k.057435", "hw": "canyonlands national park", "pos": "phrase", "ipa": "", "vi": "Vườn quốc gia Canyonlands"},
    {"id": "lex.en.200k.057436", "hw": "cervantes saavedra", "pos": "phrase", "ipa": "", "vi": "đại văn hào Miguel de Cervantes"},
    {"id": "lex.en.200k.057437", "hw": "cichlid fish", "pos": "phrase", "ipa": "", "vi": "cá thuộc họ Cá hoàng đế"},
    {"id": "lex.en.200k.057438", "hw": "coast banksia", "pos": "phrase", "ipa": "", "vi": "cây tràm hoa vàng bờ biển"},
    {"id": "lex.en.200k.057439", "hw": "concave polyhedron", "pos": "phrase", "ipa": "", "vi": "khối đa diện lõm trong hình học"},
    {"id": "lex.en.200k.057440", "hw": "creeping zinnia", "pos": "phrase", "ipa": "", "vi": "hoa cúc cúc zinnia bò lan"},
    {"id": "lex.en.200k.057441", "hw": "de rigueur", "pos": "phrase", "ipa": "", "vi": "theo đúng phép tắc; bắt buộc"},
    {"id": "lex.en.200k.057442", "hw": "digital voltmeter", "pos": "phrase", "ipa": "", "vi": "vôn kế hiện số điện tử"},
    {"id": "lex.en.200k.057443", "hw": "dolman sleeve", "pos": "phrase", "ipa": "", "vi": "tay áo cánh dơi rộng dolman"},
    {"id": "lex.en.200k.057444", "hw": "electronic voltmeter", "pos": "phrase", "ipa": "", "vi": "vôn kế điện tử chính xác"},
    {"id": "lex.en.200k.057445", "hw": "extreme unction", "pos": "phrase", "ipa": "", "vi": "bí tích xức dầu bệnh nhân"},
    {"id": "lex.en.200k.057446", "hw": "filthy lucre", "pos": "phrase", "ipa": "", "vi": "tiền kiếm bất chính bẩn thỉu"},
    {"id": "lex.en.200k.057447", "hw": "frank morrison spillane", "pos": "phrase", "ipa": "", "vi": "tiểu thuyết gia Mickey Spillane"},
    {"id": "lex.en.200k.057448", "hw": "frederico garcia lorca", "pos": "phrase", "ipa": "", "vi": "nhà thơ Federico García Lorca"},
    {"id": "lex.en.200k.057449", "hw": "gas guzzler", "pos": "phrase", "ipa": "", "vi": "xe ô tô uống xăng ngốn nhiên liệu"},
    {"id": "lex.en.200k.057450", "hw": "genitourinary apparatus", "pos": "phrase", "ipa": "", "vi": "bộ máy sinh dục và tiết niệu"},
    {"id": "lex.en.200k.057451", "hw": "genus daphnia", "pos": "phrase", "ipa": "", "vi": "chi bọ nước Daphnia giáp xác"},
    {"id": "lex.en.200k.057452", "hw": "genus rubus", "pos": "phrase", "ipa": "", "vi": "chi Mâm xôi quả phúc bồn tử"},
    {"id": "lex.en.200k.057453", "hw": "genus zinnia", "pos": "phrase", "ipa": "", "vi": "chi Cúc cánh giấy hoa duyên cúc"},
    {"id": "lex.en.200k.057454", "hw": "georg wilhelm steller", "pos": "phrase", "ipa": "", "vi": "nhà thám hiểm Georg Steller"},
    {"id": "lex.en.200k.057455", "hw": "georges henri lemaitre", "pos": "phrase", "ipa": "", "vi": "nhà vật lý Georges Lemaître"},
    {"id": "lex.en.200k.057456", "hw": "gummed label", "pos": "phrase", "ipa": "", "vi": "nhãn dán có sẵn keo dính"},
    {"id": "lex.en.200k.057457", "hw": "housatonic river", "pos": "phrase", "ipa": "", "vi": "dòng sông Housatonic New England"},
    {"id": "lex.en.200k.057458", "hw": "hugo grotius", "pos": "phrase", "ipa": "", "vi": "luật gia cha đẻ luật quốc tế"},
    {"id": "lex.en.200k.057459", "hw": "infectious mononucleosis", "pos": "phrase", "ipa": "", "vi": "bệnh tăng bạch cầu đơn nhân nhiễm"},
    {"id": "lex.en.200k.057460", "hw": "kahane chai", "pos": "phrase", "ipa": "", "vi": "tổ chức Do Thái chính thống"},
    {"id": "lex.en.200k.057461", "hw": "labia majora", "pos": "phrase", "ipa": "", "vi": "môi lớn âm hộ giải phẫu nữ"},
    {"id": "lex.en.200k.057462", "hw": "meccano set", "pos": "phrase", "ipa": "", "vi": "bộ đồ chơi cơ khí Meccano"},
    {"id": "lex.en.200k.057463", "hw": "mickey spillane", "pos": "phrase", "ipa": "", "vi": "nhà văn trinh thám Spillane"},
    {"id": "lex.en.200k.057464", "hw": "organ of corti", "pos": "phrase", "ipa": "", "vi": "cơ quan Corti thụ cảm thính giác"},
    {"id": "lex.en.200k.057465", "hw": "pierre boulez", "pos": "phrase", "ipa": "", "vi": "nhạc trưởng tài ba Pierre Boulez"},
    {"id": "lex.en.200k.057466", "hw": "polecat weed", "pos": "phrase", "ipa": "", "vi": "cây bắp cải hôi chồn hôi đầm lầy"},
    {"id": "lex.en.200k.057467", "hw": "pruritus ani", "pos": "phrase", "ipa": "", "vi": "chứng ngứa rát hậu môn kéo dài"},
    {"id": "lex.en.200k.057468", "hw": "psychogenic fugue", "pos": "phrase", "ipa": "", "vi": "chứng trốn chạy do tâm lý"},
    {"id": "lex.en.200k.057469", "hw": "quetzal bird", "pos": "phrase", "ipa": "", "vi": "loài chim ngọc bích quetzal"},
    {"id": "lex.en.200k.057470", "hw": "ray cattell", "pos": "phrase", "ipa": "", "vi": "nhà tâm lý học Raymond Cattell"},
    {"id": "lex.en.200k.057471", "hw": "sapphic ode", "pos": "phrase", "ipa": "", "vi": "thơ ca thể tứ tuyệt Sappho"},
    {"id": "lex.en.200k.057472", "hw": "scipio africanus", "pos": "phrase", "ipa": "", "vi": "đại tướng La Mã Scipio Africanus"},
    {"id": "lex.en.200k.057473", "hw": "scipio africanus major", "pos": "phrase", "ipa": "", "vi": "danh tướng La Mã Scipio Già"},
    {"id": "lex.en.200k.057474", "hw": "sundial lupine", "pos": "phrase", "ipa": "", "vi": "cây đậu lupin hoa dại đồng cỏ"},
    {"id": "lex.en.200k.057475", "hw": "turbofan engine", "pos": "phrase", "ipa": "", "vi": "động cơ phản lực cánh quạt gió"},
    {"id": "lex.en.200k.057476", "hw": "tussock caterpillar", "pos": "phrase", "ipa": "", "vi": "sâu róm nhiều chùm lông ngứa"},
    {"id": "lex.en.200k.057477", "hw": "valvular incompetence", "pos": "phrase", "ipa": "", "vi": "tình trạng suy hở van tim"},
    {"id": "lex.en.200k.057478", "hw": "van de graaff", "pos": "phrase", "ipa": "", "vi": "nhà vật lý Robert Van de Graaff"},
    {"id": "lex.en.200k.057479", "hw": "whitsun monday", "pos": "phrase", "ipa": "", "vi": "thứ Hai lễ Hiện Xuống Hạ Trần"},
    {"id": "lex.en.200k.057480", "hw": "whitsun tuesday", "pos": "phrase", "ipa": "", "vi": "thứ Ba lễ Hiện Xuống tuần thánh"},
    {"id": "lex.en.200k.057481", "hw": "woolly manzanita", "pos": "phrase", "ipa": "", "vi": "cây bụi manzanita lông mềm"},
    {"id": "lex.en.200k.057482", "hw": "antiheroes", "pos": "noun", "ipa": "/ˌæntiˈhɪroʊz/", "vi": "các nhân vật phản anh hùng"},
    {"id": "lex.en.200k.057483", "hw": "asches", "pos": "noun", "ipa": "/ˈæʃɪz/", "vi": "nhà tâm lý học Solomon Asch"},
    {"id": "lex.en.200k.057484", "hw": "athenes", "pos": "noun", "ipa": "/əˈθiːniz/", "vi": "tượng Nữ thần trí tuệ Athene"},
    {"id": "lex.en.200k.057485", "hw": "ayahs", "pos": "noun", "ipa": "/ˈaɪəz/", "vi": "vú em trông trẻ bản xứ Ấn Độ"},
    {"id": "lex.en.200k.057486", "hw": "biogeographies", "pos": "noun", "ipa": "/ˌbaɪoʊdʒiˈɑːɡrəfiz/", "vi": "các phân ngành địa lý sinh học"},
    {"id": "lex.en.200k.057487", "hw": "birthrates", "pos": "noun", "ipa": "/ˈbɜːrθreɪts/", "vi": "các tỉ lệ sinh sản dân số"},
    {"id": "lex.en.200k.057488", "hw": "boneheads", "pos": "noun", "ipa": "/ˈboʊnhɛdz/", "vi": "những kẻ đần độn ngốc nghếch"},
    {"id": "lex.en.200k.057489", "hw": "bonhoeffers", "pos": "noun", "ipa": "/ˈbɑːnhoʊfɚz/", "vi": "mục sư chống phát xít Bonhoeffer"},
    {"id": "lex.en.200k.057490", "hw": "bridgetowns", "pos": "noun", "ipa": "/ˈbrɪdʒtaʊnz/", "vi": "thủ đô đảo quốc Bridgetown"},
    {"id": "lex.en.200k.057491", "hw": "bushidos", "pos": "noun", "ipa": "/buːˈʃiːdoʊz/", "vi": "các chuẩn mực võ sĩ đạo Bushido"},
    {"id": "lex.en.200k.057492", "hw": "canucks", "pos": "noun", "ipa": "/kəˈnʌks/", "vi": "tiếng lóng người dân Canada"},
    {"id": "lex.en.200k.057493", "hw": "carolingians", "pos": "noun", "ipa": "/ˌkærəˈlɪndʒiənz/", "vi": "người triều đại Carolingian"},
    {"id": "lex.en.200k.057494", "hw": "categorises", "pos": "verb", "ipa": "/ˈkætəɡəraɪzɪz/", "vi": "phân loại; xếp vào từng nhóm"},
    {"id": "lex.en.200k.057495", "hw": "categorising", "pos": "verb", "ipa": "/ˈkætəɡəraɪzɪŋ/", "vi": "đang phân loại; đang xếp nhóm"},
    {"id": "lex.en.200k.057496", "hw": "clothiers", "pos": "noun", "ipa": "/ˈkloʊðiɚz/", "vi": "người may bán trang phục y phục"},
    {"id": "lex.en.200k.057497", "hw": "confits", "pos": "noun", "ipa": "/kɑːnˈfiːz/", "vi": "các món ninh nhừ ngâm mỡ confit"},
    {"id": "lex.en.200k.057498", "hw": "conglomerations", "pos": "noun", "ipa": "/kənˌɡlɑːməˈreɪʃənz/", "vi": "sự tập hợp hỗn hợp nhiều loại"},
    {"id": "lex.en.200k.057499", "hw": "contrivances", "pos": "noun", "ipa": "/kənˈtraɪvənsɪz/", "vi": "mưu kế tinh xảo; thiết bị khéo"},
    {"id": "lex.en.200k.057500", "hw": "copperheads", "pos": "noun", "ipa": "/ˈkɑːpɚhɛdz/", "vi": "loài rắn độc đầu đồng Bắc Mỹ"},
    {"id": "lex.en.200k.057501", "hw": "crisscrosses", "pos": "noun", "ipa": "/ˈkrɪskrɔːsɪz/", "vi": "hoa văn hình chữ thập đan chéo"}
]

# Validation
with open('scratch/b32_r05_raw_p5.json') as f:
    raw = json.load(f)

assert len(records) == 100, f"Expected 100 records, got {len(records)}"
for i, (r, raw_r) in enumerate(zip(records, raw)):
    assert r['id'] == raw_r['id'], f"Mismatch id at {i}: {r['id']} vs {raw_r['id']}"
    assert r['hw'] == raw_r['hw'], f"Mismatch hw at {i}: {r['hw']} vs {raw_r['hw']}"
    assert len(r['vi']) <= 35, f"Length violation at {i} ({r['hw']}): len={len(r['vi'])}: {r['vi']}"
    assert r['pos'] in ['noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'], f"Invalid pos at {i}: {r['pos']}"
    if ' ' not in r['hw']:
        assert r['ipa'].startswith('/') and r['ipa'].endswith('/') and r['ipa'].count('/') == 2, f"Invalid ipa at {i}: {r['ipa']}"

# Merge with raw
final_p5 = []
for r, raw_r in zip(records, raw):
    item = dict(raw_r)
    item['pos'] = r['pos']
    item['ipa'] = r['ipa']
    item['vi'] = r['vi']
    item['status'] = 'reviewed'
    final_p5.append(item)

with open('scratch/b32_r05_p5.json', 'w') as f:
    json.dump(final_p5, f, ensure_ascii=False, indent=2)
print("Part 5 validated and written successfully.")
