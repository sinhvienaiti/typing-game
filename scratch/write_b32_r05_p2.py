import json

records = [
    {"id": "lex.en.200k.057102", "hw": "phylum protozoa", "pos": "phrase", "ipa": "", "vi": "ngành động vật nguyên sinh"},
    {"id": "lex.en.200k.057103", "hw": "pku test", "pos": "phrase", "ipa": "", "vi": "xét nghiệm PKU sơ sinh"},
    {"id": "lex.en.200k.057104", "hw": "polyphemus moth", "pos": "phrase", "ipa": "", "vi": "bướm đêm Polyphemus khổng lồ"},
    {"id": "lex.en.200k.057105", "hw": "proterozoic aeon", "pos": "phrase", "ipa": "", "vi": "liên đại Nguyên sinh"},
    {"id": "lex.en.200k.057106", "hw": "racemic acid", "pos": "phrase", "ipa": "", "vi": "axit raxemic; axit racemic"},
    {"id": "lex.en.200k.057107", "hw": "regular convex polyhedron", "pos": "phrase", "ipa": "", "vi": "khối đa diện lồi đều"},
    {"id": "lex.en.200k.057108", "hw": "river lethe", "pos": "phrase", "ipa": "", "vi": "sông Quên Lethe trong thần thoại"},
    {"id": "lex.en.200k.057109", "hw": "salicylate poisoning", "pos": "phrase", "ipa": "", "vi": "ngộ độc axit salicylic"},
    {"id": "lex.en.200k.057110", "hw": "sergei diaghilev", "pos": "phrase", "ipa": "", "vi": "nhà tổ chức múa Sergei Diaghilev"},
    {"id": "lex.en.200k.057111", "hw": "sigmoid colon", "pos": "phrase", "ipa": "", "vi": "đại tràng xích-ma; kết tràng sigma"},
    {"id": "lex.en.200k.057112", "hw": "sigmoid vein", "pos": "phrase", "ipa": "", "vi": "tĩnh mạch sigma"},
    {"id": "lex.en.200k.057113", "hw": "skipjack tuna", "pos": "phrase", "ipa": "", "vi": "cá ngừ vằn; cá ngừ sọc dưa"},
    {"id": "lex.en.200k.057114", "hw": "snail darter", "pos": "phrase", "ipa": "", "vi": "cá bống nước ngọt snail darter"},
    {"id": "lex.en.200k.057115", "hw": "sodium salicylate", "pos": "phrase", "ipa": "", "vi": "muối natri salicylat"},
    {"id": "lex.en.200k.057116", "hw": "stovepipe iron", "pos": "phrase", "ipa": "", "vi": "tấm tôn mỏng cuốn ống khói"},
    {"id": "lex.en.200k.057117", "hw": "substantia alba", "pos": "phrase", "ipa": "", "vi": "chất trắng não tủy"},
    {"id": "lex.en.200k.057118", "hw": "tamil eelam", "pos": "phrase", "ipa": "", "vi": "nhà nước độc lập Tamil Eelam"},
    {"id": "lex.en.200k.057119", "hw": "testamentary trust", "pos": "phrase", "ipa": "", "vi": "quỹ tín thác theo di chúc"},
    {"id": "lex.en.200k.057120", "hw": "theodor mommsen", "pos": "phrase", "ipa": "", "vi": "nhà sử học Theodor Mommsen"},
    {"id": "lex.en.200k.057121", "hw": "tobacconist shop", "pos": "phrase", "ipa": "", "vi": "cửa hàng bán thuốc lá"},
    {"id": "lex.en.200k.057122", "hw": "trenching spade", "pos": "phrase", "ipa": "", "vi": "xẻng đào hào hẹp"},
    {"id": "lex.en.200k.057123", "hw": "tufted gentian", "pos": "phrase", "ipa": "", "vi": "hoa long đởm bụi"},
    {"id": "lex.en.200k.057124", "hw": "unicameral script", "pos": "phrase", "ipa": "", "vi": "hệ chữ chỉ có một cỡ viết hoa"},
    {"id": "lex.en.200k.057125", "hw": "valedictory oration", "pos": "phrase", "ipa": "", "vi": "bài diễn văn từ biệt tốt nghiệp"},
    {"id": "lex.en.200k.057126", "hw": "valvular heart disease", "pos": "phrase", "ipa": "", "vi": "bệnh lý hở hẹp van tim"},
    {"id": "lex.en.200k.057127", "hw": "vernier caliper", "pos": "phrase", "ipa": "", "vi": "thước cặp du xích; thước kẹp"},
    {"id": "lex.en.200k.057128", "hw": "vidalia onion", "pos": "phrase", "ipa": "", "vi": "hành tây ngọt Vidalia"},
    {"id": "lex.en.200k.057129", "hw": "windowpane oyster", "pos": "phrase", "ipa": "", "vi": "loài điệp trai ép vỏ cửa sổ"},
    {"id": "lex.en.200k.057130", "hw": "adductors", "pos": "noun", "ipa": "/æˈdʌktɚz/", "vi": "các cơ khép trong giải phẫu"},
    {"id": "lex.en.200k.057131", "hw": "arcadians", "pos": "noun", "ipa": "/ɑːrˈkeɪdiənz/", "vi": "người dân vùng Arcadia Hy Lạp"},
    {"id": "lex.en.200k.057132", "hw": "bemidjis", "pos": "noun", "ipa": "/bəˈmɪdʒiz/", "vi": "các địa danh thành phố Bemidji"},
    {"id": "lex.en.200k.057133", "hw": "blantyres", "pos": "noun", "ipa": "/blænˈtaɪərz/", "vi": "các thành phố tên Blantyre"},
    {"id": "lex.en.200k.057134", "hw": "brainwaves", "pos": "noun", "ipa": "/ˈbreɪnweɪvz/", "vi": "các sóng não; ý tưởng bất chợt"},
    {"id": "lex.en.200k.057135", "hw": "bratwursts", "pos": "noun", "ipa": "/ˈbrɑːtwɜːrsts/", "vi": "các xúc xích nướng bratwurst"},
    {"id": "lex.en.200k.057136", "hw": "brickyards", "pos": "noun", "ipa": "/ˈbrɪkjɑːrdz/", "vi": "các xưởng đóng gạch; bãi gạch"},
    {"id": "lex.en.200k.057137", "hw": "bryonies", "pos": "noun", "ipa": "/ˈbraɪəniz/", "vi": "cây dây leo chi Bryonia"},
    {"id": "lex.en.200k.057138", "hw": "buckaroos", "pos": "noun", "ipa": "/ˌbʌkəˈruːz/", "vi": "chàng cao bồi miền viễn Tây"},
    {"id": "lex.en.200k.057139", "hw": "burrier", "pos": "adj", "ipa": "/ˈbɜːriər/", "vi": "nhiều quả gai dính hơn"},
    {"id": "lex.en.200k.057140", "hw": "burriest", "pos": "adj", "ipa": "/ˈbɜːriɪst/", "vi": "nhiều quả gai dính nhất"},
    {"id": "lex.en.200k.057141", "hw": "caddos", "pos": "noun", "ipa": "/ˈkædoʊz/", "vi": "người bản địa Caddo Bắc Mỹ"},
    {"id": "lex.en.200k.057142", "hw": "centerfolds", "pos": "noun", "ipa": "/ˈsɛntɚfoʊldz/", "vi": "các bức ảnh gập đôi ở trang giữa"},
    {"id": "lex.en.200k.057143", "hw": "charterhouses", "pos": "noun", "ipa": "/ˈtʃɑːrtɚhaʊsɪz/", "vi": "các tu viện dòng Carthusian"},
    {"id": "lex.en.200k.057144", "hw": "chichis", "pos": "noun", "ipa": "/ˈʃiːʃiːz/", "vi": "kẻ đua đòi kiểu cách hào nhoáng"},
    {"id": "lex.en.200k.057145", "hw": "commodes", "pos": "noun", "ipa": "/kəˈmoʊdz/", "vi": "các tủ ngăn kéo; bồn vệ sinh"},
    {"id": "lex.en.200k.057146", "hw": "couturiers", "pos": "noun", "ipa": "/kuːˈtʊrieɪz/", "vi": "nhà may đo thời trang cao cấp"},
    {"id": "lex.en.200k.057147", "hw": "craigies", "pos": "noun", "ipa": "/ˈkreɪɡiz/", "vi": "các người dòng họ Craigie"},
    {"id": "lex.en.200k.057148", "hw": "cytoskeletons", "pos": "noun", "ipa": "/ˌsaɪtoʊˈskɛlɪtnz/", "vi": "các bộ khung xương tế bào chất"},
    {"id": "lex.en.200k.057149", "hw": "dioxins", "pos": "noun", "ipa": "/daɪˈɑːksɪnz/", "vi": "các hợp chất độc dioxin"},
    {"id": "lex.en.200k.057150", "hw": "docents", "pos": "noun", "ipa": "/ˈdoʊsənts/", "vi": "các hướng dẫn viên viện bảo tàng"},
    {"id": "lex.en.200k.057151", "hw": "dramatizing", "pos": "verb", "ipa": "/ˈdræmətaɪzɪŋ/", "vi": "soạn thành kịch; thổi phồng"},
    {"id": "lex.en.200k.057152", "hw": "dyads", "pos": "noun", "ipa": "/ˈdaɪædz/", "vi": "các bộ đôi; các cặp liên kết"},
    {"id": "lex.en.200k.057153", "hw": "earfuls", "pos": "noun", "ipa": "/ˈɪrfʊlz/", "vi": "những tràng mắng mỏ; lời rầy la"},
    {"id": "lex.en.200k.057154", "hw": "epicureans", "pos": "noun", "ipa": "/ˌɛpɪkjʊˈriːənz/", "vi": "người sành ăn uống hưởng lạc"},
    {"id": "lex.en.200k.057155", "hw": "esms", "pos": "noun", "ipa": "/ˌiː.ɛsˈɛmz/", "vi": "hệ thống hỗ trợ điện tử trinh sát"},
    {"id": "lex.en.200k.057156", "hw": "fiefdoms", "pos": "noun", "ipa": "/ˈfiːfdəmz/", "vi": "các thái ấp; lãnh địa phong kiến"},
    {"id": "lex.en.200k.057157", "hw": "foghorns", "pos": "noun", "ipa": "/ˈfɑːɡhɔːrnz/", "vi": "các còi hú cảnh báo sương mù"},
    {"id": "lex.en.200k.057158", "hw": "galileans", "pos": "noun", "ipa": "/ˌɡælɪˈliːənz/", "vi": "người dân vùng Ga-li-lê Do Thái"},
    {"id": "lex.en.200k.057159", "hw": "gautamas", "pos": "noun", "ipa": "/ɡaʊˈtɑːməz/", "vi": "dòng họ Cồ Đàm; Phật Gautama"},
    {"id": "lex.en.200k.057160", "hw": "granules", "pos": "noun", "ipa": "/ˈɡrænjuːlz/", "vi": "các hạt nhỏ li ti; hạt cốm"},
    {"id": "lex.en.200k.057161", "hw": "hankeys", "pos": "noun", "ipa": "/ˈhæŋkiz/", "vi": "các chiếc khăn mùi xoa; khăn tay"},
    {"id": "lex.en.200k.057162", "hw": "headwinds", "pos": "noun", "ipa": "/ˈhɛdwɪndz/", "vi": "những cơn gió ngược chiều"},
    {"id": "lex.en.200k.057163", "hw": "herthas", "pos": "noun", "ipa": "/ˈhɜːrθəz/", "vi": "các tượng Nữ thần đất Hertha"},
    {"id": "lex.en.200k.057164", "hw": "hollandaises", "pos": "noun", "ipa": "/ˌhɑːlənˈdeɪzɪz/", "vi": "các loại sốt bơ trứng béo ngậy"},
    {"id": "lex.en.200k.057165", "hw": "hypochondriacs", "pos": "noun", "ipa": "/ˌhaɪpoʊˈkɑːndriæks/", "vi": "những người mắc chứng nghi bệnh"},
    {"id": "lex.en.200k.057166", "hw": "idlers", "pos": "noun", "ipa": "/ˈaɪdlɚz/", "vi": "những kẻ nhàn rỗi lười biếng"},
    {"id": "lex.en.200k.057167", "hw": "iols", "pos": "noun", "ipa": "/ˌaɪ.oʊˈɛlz/", "vi": "thấu kính nội nhãn nhân tạo"},
    {"id": "lex.en.200k.057168", "hw": "keokuks", "pos": "noun", "ipa": "/ˈkiːəkʌks/", "vi": "thủ lĩnh bộ tộc Keokuk da đỏ"},
    {"id": "lex.en.200k.057169", "hw": "kerfuffles", "pos": "noun", "ipa": "/kɚˈfʌfəlz/", "vi": "các cuộc cãi cọ om sòm; lộn xộn"},
    {"id": "lex.en.200k.057170", "hw": "kilroys", "pos": "noun", "ipa": "/ˈkɪlrɔɪz/", "vi": "các hình vẽ ngộ nghĩnh Kilroy"},
    {"id": "lex.en.200k.057171", "hw": "kivus", "pos": "noun", "ipa": "/ˈkiːvuːz/", "vi": "vùng ven hồ lớn Kivu ở châu Phi"},
    {"id": "lex.en.200k.057172", "hw": "lanais", "pos": "noun", "ipa": "/ləˈnaɪz/", "vi": "hàng hiên có mái che ngoài trời"},
    {"id": "lex.en.200k.057173", "hw": "loesses", "pos": "noun", "ipa": "/ˈloʊ.əsɪz/", "vi": "các tầng hoàng thổ mịn màu mỡ"},
    {"id": "lex.en.200k.057174", "hw": "loudmouths", "pos": "noun", "ipa": "/ˈlaʊdmaʊðz/", "vi": "kẻ to mồm ba hoa khoác lác"},
    {"id": "lex.en.200k.057175", "hw": "lunts", "pos": "noun", "ipa": "/lʌnts/", "vi": "nghệ sĩ sân khấu nổi tiếng Lunt"},
    {"id": "lex.en.200k.057176", "hw": "microcomputers", "pos": "noun", "ipa": "/ˌmaɪkroʊkəmˈpjuːtɚz/", "vi": "các máy vi tính vi xử lý nhỏ"},
    {"id": "lex.en.200k.057177", "hw": "moccasins", "pos": "noun", "ipa": "/ˈmɑːkəsɪnz/", "vi": "đôi giày da đanh của thổ dân"},
    {"id": "lex.en.200k.057178", "hw": "monocultures", "pos": "noun", "ipa": "/ˈmɑːnəkʌltʃɚz/", "vi": "các nền nông nghiệp độc canh"},
    {"id": "lex.en.200k.057179", "hw": "moonwalks", "pos": "noun", "ipa": "/ˈmuːnwɔːks/", "vi": "điệu nhảy trượt lùi moonwalk"},
    {"id": "lex.en.200k.057180", "hw": "morrigans", "pos": "noun", "ipa": "/ˈmɔːrɪɡənz/", "vi": "nữ thần chiến trận Morrigan"},
    {"id": "lex.en.200k.057181", "hw": "nansens", "pos": "noun", "ipa": "/ˈnænsənz/", "vi": "nhà thám hiểm đoạt Nobel Nansen"},
    {"id": "lex.en.200k.057182", "hw": "nitriles", "pos": "noun", "ipa": "/ˈnaɪtrəlz/", "vi": "hợp chất hữu cơ nhóm nitril"},
    {"id": "lex.en.200k.057183", "hw": "noblesses", "pos": "noun", "ipa": "/noʊˈblɛsɪz/", "vi": "tầng lớp quý tộc dòng dõi danh giá"},
    {"id": "lex.en.200k.057184", "hw": "normandies", "pos": "noun", "ipa": "/ˈnɔːrməndiz/", "vi": "tàu biển hoặc vùng Normandie"},
    {"id": "lex.en.200k.057185", "hw": "nuncios", "pos": "noun", "ipa": "/ˈnʌnsioʊz/", "vi": "sứ thần ngoại giao Tòa thánh"},
    {"id": "lex.en.200k.057186", "hw": "oinked", "pos": "verb", "ipa": "/ɔɪŋkt/", "vi": "đã kêu ủn ỉn; đã eng éc"},
    {"id": "lex.en.200k.057187", "hw": "oinking", "pos": "verb", "ipa": "/ˈɔɪŋkɪŋ/", "vi": "đang kêu ủn ỉn tiếng heo lợn"},
    {"id": "lex.en.200k.057188", "hw": "oligopolies", "pos": "noun", "ipa": "/ˌɑːlɪˈɡɑːpəliz/", "vi": "thị trường độc quyền tập đoàn"},
    {"id": "lex.en.200k.057189", "hw": "otolaryngologies", "pos": "noun", "ipa": "/ˌoʊtoʊˌlærɪŋˈɡɑːlədʒiz/", "vi": "các chuyên khoa tai mũi họng y học"},
    {"id": "lex.en.200k.057190", "hw": "overeats", "pos": "verb", "ipa": "/ˌoʊvɚˈiːts/", "vi": "ăn quá nhiều; ăn quá độ bội thực"},
    {"id": "lex.en.200k.057191", "hw": "paisas", "pos": "noun", "ipa": "/paɪˈsɑːz/", "vi": "các đồng hào tiền lẻ paisa Ấn Độ"},
    {"id": "lex.en.200k.057192", "hw": "paise", "pos": "noun", "ipa": "/ˈpaɪseɪ/", "vi": "các đồng xu tiền tệ paise ở Nam Á"},
    {"id": "lex.en.200k.057193", "hw": "palaeontologies", "pos": "noun", "ipa": "/ˌpeɪliɑːnˈtɑːlədʒiz/", "vi": "các phân ngành cổ sinh vật học"},
    {"id": "lex.en.200k.057194", "hw": "patisseries", "pos": "noun", "ipa": "/pəˈtiːsəriz/", "vi": "các tiệm bánh ngọt kiểu Pháp"},
    {"id": "lex.en.200k.057195", "hw": "pernods", "pos": "noun", "ipa": "/pɛrˈnoʊz/", "vi": "các ly rượu khai vị hồi Pernod"},
    {"id": "lex.en.200k.057196", "hw": "philemons", "pos": "noun", "ipa": "/fɪˈliːmənz/", "vi": "thư Philêmôn trong Kinh Thánh"},
    {"id": "lex.en.200k.057197", "hw": "picots", "pos": "noun", "ipa": "/ˈpiːkoʊz/", "vi": "mũi kim đan viền răng cưa nhỏ"},
    {"id": "lex.en.200k.057198", "hw": "pileups", "pos": "noun", "ipa": "/ˈpaɪlʌps/", "vi": "vụ tai nạn giao thông liên hoàn"},
    {"id": "lex.en.200k.057199", "hw": "portents", "pos": "noun", "ipa": "/ˈpɔːrtɛnts/", "vi": "các điềm báo gở; dấu hiệu tương lai"},
    {"id": "lex.en.200k.057200", "hw": "prows", "pos": "noun", "ipa": "/praʊz/", "vi": "các mũi tàu thuyền; mũi thuyền"},
    {"id": "lex.en.200k.057201", "hw": "prunuses", "pos": "noun", "ipa": "/ˈpruːnəsɪz/", "vi": "loài cây mận mơ chi Prunus"}
]

# Validation
with open('scratch/b32_r05_raw_p2.json') as f:
    raw = json.load(f)

assert len(records) == 100, f"Expected 100 records, got {len(records)}"
for i, (r, raw_r) in enumerate(zip(records, raw)):
    assert r['id'] == raw_r['id'], f"Mismatch id at {i}: {r['id']} vs {raw_r['id']}"
    assert r['hw'] == raw_r['hw'], f"Mismatch hw at {i}: {r['hw']} vs {raw_r['hw']}"
    assert len(r['vi']) <= 35, f"Length violation at {i} ({r['hw']}): len={len(r['vi'])}: {r['vi']}"
    assert r['pos'] in ['noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'], f"Invalid pos at {i}: {r['pos']}"
    if ' ' not in r['hw']:
        assert r['ipa'].startswith('/') and r['ipa'].endswith('/') and r['ipa'].count('/') == 2, f"Invalid ipa at {i}: {r['ipa']}"

# Merge with raw to preserve cefr, tier, etc.
final_p2 = []
for r, raw_r in zip(records, raw):
    item = dict(raw_r)
    item['pos'] = r['pos']
    item['ipa'] = r['ipa']
    item['vi'] = r['vi']
    item['status'] = 'reviewed'
    final_p2.append(item)

with open('scratch/b32_r05_p2.json', 'w') as f:
    json.dump(final_p2, f, ensure_ascii=False, indent=2)
print("Part 2 validated and written successfully.")
