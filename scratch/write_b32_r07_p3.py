import json

records = [
    {"id": "lex.en.200k.058202", "hw": "angstrom unit", "pos": "phrase", "ipa": "", "vi": "đơn vị đo độ dài quang học Å"},
    {"id": "lex.en.200k.058203", "hw": "aplastic anemia", "pos": "phrase", "ipa": "", "vi": "chứng thiếu máu do suy tủy bất sản"},
    {"id": "lex.en.200k.058204", "hw": "auricular appendix", "pos": "phrase", "ipa": "", "vi": "tiểu nhĩ của tâm nhĩ buồng tim"},
    {"id": "lex.en.200k.058205", "hw": "auricular artery", "pos": "phrase", "ipa": "", "vi": "động mạch cấp máu vành tai"},
    {"id": "lex.en.200k.058206", "hw": "auricular vein", "pos": "phrase", "ipa": "", "vi": "tĩnh mạch dẫn máu vành tai"},
    {"id": "lex.en.200k.058207", "hw": "benzoic acid", "pos": "phrase", "ipa": "", "vi": "axit benzoic bảo quản thực phẩm"},
    {"id": "lex.en.200k.058208", "hw": "beta vulgaris rubra", "pos": "phrase", "ipa": "", "vi": "củ cải dền đỏ ngọt nấu súp"},
    {"id": "lex.en.200k.058209", "hw": "bill mauldin", "pos": "phrase", "ipa": "", "vi": "họa sĩ biếm họa Bill Mauldin"},
    {"id": "lex.en.200k.058210", "hw": "borage family", "pos": "phrase", "ipa": "", "vi": "họ thực vật Mồ hôi Boraginaceae"},
    {"id": "lex.en.200k.058211", "hw": "brer rabbit", "pos": "phrase", "ipa": "", "vi": "chú thỏ tinh khôn Br'er Rabbit"},
    {"id": "lex.en.200k.058212", "hw": "camphor dune tansy", "pos": "phrase", "ipa": "", "vi": "cây cúc thơm cồn cát mùi long não"},
    {"id": "lex.en.200k.058213", "hw": "cassia grandis", "pos": "phrase", "ipa": "", "vi": "cây muồng hoa hồng trâu ngát hương"},
    {"id": "lex.en.200k.058214", "hw": "chiricahua apache", "pos": "phrase", "ipa": "", "vi": "bộ tộc thổ dân Chiricahua Apache"},
    {"id": "lex.en.200k.058215", "hw": "choroid coat", "pos": "phrase", "ipa": "", "vi": "màng mạch giác mạc trong cầu mắt"},
    {"id": "lex.en.200k.058216", "hw": "circumflex iliac artery", "pos": "phrase", "ipa": "", "vi": "động mạch chậu nông vòng đùi"},
    {"id": "lex.en.200k.058217", "hw": "class mammalia", "pos": "phrase", "ipa": "", "vi": "lớp Động vật có vú lớp Thú"},
    {"id": "lex.en.200k.058218", "hw": "colorimetric analysis", "pos": "phrase", "ipa": "", "vi": "phương pháp phân tích so màu quang"},
    {"id": "lex.en.200k.058219", "hw": "corrosive sublimate", "pos": "phrase", "ipa": "", "vi": "thủy ngân clorua độc tính cao"},
    {"id": "lex.en.200k.058220", "hw": "country borage", "pos": "phrase", "ipa": "", "vi": "cây húng chanh rau tần dày lá thơm"},
    {"id": "lex.en.200k.058221", "hw": "dashiell hammett", "pos": "phrase", "ipa": "", "vi": "nhà văn trinh thám Hammett Mỹ"},
    {"id": "lex.en.200k.058222", "hw": "disjunctive conjunction", "pos": "phrase", "ipa": "", "vi": "liên từ phân tách lựa chọn"},
    {"id": "lex.en.200k.058223", "hw": "edouard lemaitre", "pos": "phrase", "ipa": "", "vi": "diễn viên kịch Frédérick Lemaître"},
    {"id": "lex.en.200k.058224", "hw": "empiricist philosophy", "pos": "phrase", "ipa": "", "vi": "triết học chủ nghĩa kinh nghiệm"},
    {"id": "lex.en.200k.058225", "hw": "enderby land", "pos": "phrase", "ipa": "", "vi": "vùng băng giá Enderby Land Nam Cực"},
    {"id": "lex.en.200k.058226", "hw": "excretory organ", "pos": "phrase", "ipa": "", "vi": "cơ quan bài tiết chất thải cơ thể"},
    {"id": "lex.en.200k.058227", "hw": "excretory product", "pos": "phrase", "ipa": "", "vi": "sản phẩm chất cặn bã bài tiết"},
    {"id": "lex.en.200k.058228", "hw": "extrasensory perception", "pos": "phrase", "ipa": "", "vi": "giác quan thứ sáu ngoại cảm ESP"},
    {"id": "lex.en.200k.058229", "hw": "fagot stitch", "pos": "phrase", "ipa": "", "vi": "mũi may thêu ren ô thoáng hình bó"},
    {"id": "lex.en.200k.058230", "hw": "foxtail barley", "pos": "phrase", "ipa": "", "vi": "loài lúa mạch đuôi chồn hoang dại"},
    {"id": "lex.en.200k.058231", "hw": "fusible metal", "pos": "phrase", "ipa": "", "vi": "hợp kim có nhiệt độ nóng chảy thấp"},
    {"id": "lex.en.200k.058232", "hw": "garden heliotrope", "pos": "phrase", "ipa": "", "vi": "cây hoa vòi voi thơm trồng vườn"},
    {"id": "lex.en.200k.058233", "hw": "genus agama", "pos": "phrase", "ipa": "", "vi": "chi thằn lằn vảy nhám agama"},
    {"id": "lex.en.200k.058234", "hw": "genus bufo", "pos": "phrase", "ipa": "", "vi": "chi cóc thông thường Bufonidae"},
    {"id": "lex.en.200k.058235", "hw": "genus dugong", "pos": "phrase", "ipa": "", "vi": "chi bò biển cá nược chi Dugong"},
    {"id": "lex.en.200k.058236", "hw": "genus ephedra", "pos": "phrase", "ipa": "", "vi": "chi ma hoàng thảo mộc phế quản"},
    {"id": "lex.en.200k.058237", "hw": "genus macaca", "pos": "phrase", "ipa": "", "vi": "chi khỉ đuôi dài khỉ mác-cắc"},
    {"id": "lex.en.200k.058238", "hw": "genus oncorhynchus", "pos": "phrase", "ipa": "", "vi": "chi cá hồi đỏ Thái Bình Dương"},
    {"id": "lex.en.200k.058239", "hw": "genus panicum", "pos": "phrase", "ipa": "", "vi": "chi thực vật cỏ kê chi Panicum"},
    {"id": "lex.en.200k.058240", "hw": "genus shigella", "pos": "phrase", "ipa": "", "vi": "chi trực khuẩn lỵ Shigella"},
    {"id": "lex.en.200k.058241", "hw": "gerhard herzberg", "pos": "phrase", "ipa": "", "vi": "nhà hóa học Nobel Gerhard Herzberg"},
    {"id": "lex.en.200k.058242", "hw": "giant hyssop", "pos": "phrase", "ipa": "", "vi": "cây bạc hà hoang khổng lồ hoa tím"},
    {"id": "lex.en.200k.058243", "hw": "great bustard", "pos": "phrase", "ipa": "", "vi": "loài chim ô tác lớn đồng cỏ"},
    {"id": "lex.en.200k.058244", "hw": "gustatory cell", "pos": "phrase", "ipa": "", "vi": "tế bào vị giác thụ cảm gai lưỡi"},
    {"id": "lex.en.200k.058245", "hw": "gustatory organ", "pos": "phrase", "ipa": "", "vi": "cơ quan tiếp nhận vị giác nụ nếm"},
    {"id": "lex.en.200k.058246", "hw": "gustatory perception", "pos": "phrase", "ipa": "", "vi": "sự thụ cảm và phân biệt vị giác"},
    {"id": "lex.en.200k.058247", "hw": "halftone engraving", "pos": "phrase", "ipa": "", "vi": "kỹ thuật khắc in ảnh nửa tông"},
    {"id": "lex.en.200k.058248", "hw": "hyssop oil", "pos": "phrase", "ipa": "", "vi": "tinh dầu cây bài hương chữa bệnh"},
    {"id": "lex.en.200k.058249", "hw": "interlocutory injunction", "pos": "phrase", "ipa": "", "vi": "lệnh đình chỉ tạm thời của tòa án"},
    {"id": "lex.en.200k.058250", "hw": "isles of langerhans", "pos": "phrase", "ipa": "", "vi": "các đảo tế bào tụy tiết insulin"},
    {"id": "lex.en.200k.058251", "hw": "joseph schumpeter", "pos": "phrase", "ipa": "", "vi": "nhà kinh tế học Joseph Schumpeter"},
    {"id": "lex.en.200k.058252", "hw": "kuwaiti dirham", "pos": "phrase", "ipa": "", "vi": "đồng tiền tệ dirham của Kuwait"},
    {"id": "lex.en.200k.058253", "hw": "loggerhead shrike", "pos": "phrase", "ipa": "", "vi": "chim bách thanh đầu to đồ tể"},
    {"id": "lex.en.200k.058254", "hw": "mantled ground squirrel", "pos": "phrase", "ipa": "", "vi": "sóc đất lông vàng có sọc lưng"},
    {"id": "lex.en.200k.058255", "hw": "meadow foxtail", "pos": "phrase", "ipa": "", "vi": "cỏ đuôi chồn đồng cỏ chăn nuôi"},
    {"id": "lex.en.200k.058256", "hw": "mexican hyssop", "pos": "phrase", "ipa": "", "vi": "cây bài hương thảo dược Mexico"},
    {"id": "lex.en.200k.058257", "hw": "nova scotian", "pos": "phrase", "ipa": "", "vi": "người dân bang Nova Scotia Canada"},
    {"id": "lex.en.200k.058258", "hw": "oleo oil", "pos": "phrase", "ipa": "", "vi": "dầu mỡ bò dùng làm bơ thực vật"},
    {"id": "lex.en.200k.058259", "hw": "omar khayyam", "pos": "phrase", "ipa": "", "vi": "thi hào Ba Tư đại thụ Omar Khayyam"},
    {"id": "lex.en.200k.058260", "hw": "panthera leo", "pos": "phrase", "ipa": "", "vi": "loài sư tử châu Phi mãnh thú"},
    {"id": "lex.en.200k.058261", "hw": "paul tillich", "pos": "phrase", "ipa": "", "vi": "nhà thần học triết gia Paul Tillich"},
    {"id": "lex.en.200k.058262", "hw": "percy bysshe shelley", "pos": "phrase", "ipa": "", "vi": "thi hào lãng mạn Anh Percy Shelley"},
    {"id": "lex.en.200k.058263", "hw": "perfective aspect", "pos": "phrase", "ipa": "", "vi": "thể hoàn thành trọn vẹn ngữ pháp"},
    {"id": "lex.en.200k.058264", "hw": "perfective tense", "pos": "phrase", "ipa": "", "vi": "thì hoàn thành ngữ pháp tiếng Anh"},
    {"id": "lex.en.200k.058265", "hw": "philipp melanchthon", "pos": "phrase", "ipa": "", "vi": "nhà cải cách tôn giáo Melanchthon"},
    {"id": "lex.en.200k.058266", "hw": "plasminogen activator", "pos": "phrase", "ipa": "", "vi": "chất kích hoạt tan cục máu đông"},
    {"id": "lex.en.200k.058267", "hw": "pronghorn antelope", "pos": "phrase", "ipa": "", "vi": "linh dương sừng nhánh Bắc Mỹ"},
    {"id": "lex.en.200k.058268", "hw": "pygmy marmoset", "pos": "phrase", "ipa": "", "vi": "loài khỉ đuôi sóc tí hon Amazon"},
    {"id": "lex.en.200k.058269", "hw": "qatari dirham", "pos": "phrase", "ipa": "", "vi": "đồng tiền tệ dirham nước Qatar"},
    {"id": "lex.en.200k.058270", "hw": "rana palustris", "pos": "phrase", "ipa": "", "vi": "loài ếch đầm lầy hoa văn kẻ sọc"},
    {"id": "lex.en.200k.058271", "hw": "restriction endonuclease", "pos": "phrase", "ipa": "", "vi": "enzym cắt giới hạn ADN phân tử"},
    {"id": "lex.en.200k.058272", "hw": "retarding force", "pos": "phrase", "ipa": "", "vi": "lực cản trở chuyển động; lực hãm"},
    {"id": "lex.en.200k.058273", "hw": "saint polycarp", "pos": "phrase", "ipa": "", "vi": "Thánh tử đạo Polycarp thành Smyrna"},
    {"id": "lex.en.200k.058274", "hw": "samuel dashiell hammett", "pos": "phrase", "ipa": "", "vi": "nhà văn trinh thám Dashiell Hammett"},
    {"id": "lex.en.200k.058275", "hw": "sea squab", "pos": "phrase", "ipa": "", "vi": "thịt cá nóc lột da phi lê hải sản"},
    {"id": "lex.en.200k.058276", "hw": "soja bean", "pos": "phrase", "ipa": "", "vi": "hạt đậu tương; cây đậu nành"},
    {"id": "lex.en.200k.058277", "hw": "streptomyces scabies", "pos": "phrase", "ipa": "", "vi": "xạ khuẩn gây bệnh ghẻ khoai tây"},
    {"id": "lex.en.200k.058278", "hw": "tibialis muscle", "pos": "phrase", "ipa": "", "vi": "nhóm cơ xương chày ống quyển chân"},
    {"id": "lex.en.200k.058279", "hw": "tissue plasminogen activator", "pos": "phrase", "ipa": "", "vi": "chất t-PA làm tan huyết khối cấp"},
    {"id": "lex.en.200k.058280", "hw": "urogenital medicine", "pos": "phrase", "ipa": "", "vi": "chuyên khoa niệu sinh dục y học"},
    {"id": "lex.en.200k.058281", "hw": "urogenital system", "pos": "phrase", "ipa": "", "vi": "hệ cơ quan tiết niệu và sinh dục"},
    {"id": "lex.en.200k.058282", "hw": "vas deferens", "pos": "phrase", "ipa": "", "vi": "ống dẫn tinh trùng từ tinh hoàn"},
    {"id": "lex.en.200k.058283", "hw": "vitus behring", "pos": "phrase", "ipa": "", "vi": "nhà thám hiểm biển Vitus Bering"},
    {"id": "lex.en.200k.058284", "hw": "wiffle ball", "pos": "phrase", "ipa": "", "vi": "quả bóng nhựa rỗng có lỗ wiffle"},
    {"id": "lex.en.200k.058285", "hw": "william henry mauldin", "pos": "phrase", "ipa": "", "vi": "họa sĩ truyện tranh Bill Mauldin"},
    {"id": "lex.en.200k.058286", "hw": "winter heliotrope", "pos": "phrase", "ipa": "", "vi": "cây cúc thơm vòi voi nở mùa đông"},
    {"id": "lex.en.200k.058287", "hw": "yellow giant hyssop", "pos": "phrase", "ipa": "", "vi": "cây hoa hồi hoa vàng thơm cao lớn"},
    {"id": "lex.en.200k.058288", "hw": "abieses", "pos": "noun", "ipa": "/ˈeɪbiːˌiːz/", "vi": "cây linh sam lá kim chi Abies"},
    {"id": "lex.en.200k.058289", "hw": "afterburners", "pos": "noun", "ipa": "/ˈæftɚbɜːrnɚz/", "vi": "bộ phận đốt tăng lực máy bay"},
    {"id": "lex.en.200k.058290", "hw": "albacores", "pos": "noun", "ipa": "/ˈælbəkɔːrz/", "vi": "cá ngừ vây dài thịt trắng béo ngậy"},
    {"id": "lex.en.200k.058291", "hw": "alliums", "pos": "noun", "ipa": "/ˈæliəmz/", "vi": "cây thuộc chi Hành tỏi hoa tím"},
    {"id": "lex.en.200k.058292", "hw": "amuns", "pos": "noun", "ipa": "/ˈɑːmuːnz/", "vi": "thần mặt trời Amun Ai Cập cổ"},
    {"id": "lex.en.200k.058293", "hw": "anaesthetists", "pos": "noun", "ipa": "/əˈniːsθətɪsts/", "vi": "bác sĩ chuyên khoa gây mê hồi sức"},
    {"id": "lex.en.200k.058294", "hw": "asanas", "pos": "noun", "ipa": "/ˈɑːsənəz/", "vi": "các tư thế tập yoga giữ tĩnh thân"},
    {"id": "lex.en.200k.058295", "hw": "astrodomes", "pos": "noun", "ipa": "/ˈæstroʊdoʊmz/", "vi": "mái vòm kính quan sát thiên văn"},
    {"id": "lex.en.200k.058296", "hw": "asuncions", "pos": "noun", "ipa": "/ɑːsuːnˈsjoʊnz/", "vi": "thủ đô Asunción của nước Paraguay"},
    {"id": "lex.en.200k.058297", "hw": "baobabs", "pos": "noun", "ipa": "/ˈbaʊbæbz/", "vi": "cây bao báp khổng lồ thân trữ nước"},
    {"id": "lex.en.200k.058298", "hw": "bellflowers", "pos": "noun", "ipa": "/ˈbɛlflaʊɚz/", "vi": "hoa chuông rủ cánh màu lam biếc"},
    {"id": "lex.en.200k.058299", "hw": "bessels", "pos": "noun", "ipa": "/ˈbɛsəlz/", "vi": "nhà toán học Friedrich Bessel"},
    {"id": "lex.en.200k.058300", "hw": "bmrs", "pos": "noun", "ipa": "/ˌbiː.ɛmˈɑːrz/", "vi": "tỉ lệ trao đổi chất cơ bản BMR"},
    {"id": "lex.en.200k.058301", "hw": "bnses", "pos": "noun", "ipa": "/ˌbiː.ɛnˈɛsɪz/", "vi": "bằng cử nhân khoa học hải quân BNS"}
]

# Validation
with open('scratch/b32_r07_raw_p3.json') as f:
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
final_p3 = []
for r, raw_r in zip(records, raw):
    item = dict(raw_r)
    item['pos'] = r['pos']
    item['ipa'] = r['ipa']
    item['vi'] = r['vi']
    item['status'] = 'reviewed'
    final_p3.append(item)

with open('scratch/b32_r07_p3.json', 'w') as f:
    json.dump(final_p3, f, ensure_ascii=False, indent=2)
print("Part 3 validated and written successfully.")
