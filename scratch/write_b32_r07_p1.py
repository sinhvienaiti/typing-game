import json

records = [
    {"id": "lex.en.200k.058002", "hw": "glengarries", "pos": "noun", "ipa": "/ɡlɛnˈɡæriz/", "vi": "mũ ca-lô Glengarry của Scotland"},
    {"id": "lex.en.200k.058003", "hw": "glimmerings", "pos": "noun", "ipa": "/ˈɡlɪmərɪŋz/", "vi": "tia sáng le lói; manh mối mờ nhạt"},
    {"id": "lex.en.200k.058004", "hw": "goldsboros", "pos": "noun", "ipa": "/ˈɡoʊldzbɚroʊz/", "vi": "địa danh thành phố Goldsboro ở Mỹ"},
    {"id": "lex.en.200k.058005", "hw": "gravediggers", "pos": "noun", "ipa": "/ˈɡreɪvdɪɡɚz/", "vi": "những người chuyên đào huyệt mộ"},
    {"id": "lex.en.200k.058006", "hw": "green foxtail", "pos": "phrase", "ipa": "", "vi": "loài cỏ đuôi chồn xanh lục mọc dại"},
    {"id": "lex.en.200k.058007", "hw": "greeters", "pos": "noun", "ipa": "/ˈɡriːtɚz/", "vi": "nhân viên đứng chào đón khách hàng"},
    {"id": "lex.en.200k.058008", "hw": "gurkhas", "pos": "noun", "ipa": "/ˈɡʊrkəz/", "vi": "các chiến binh dũng cảm Gurkha"},
    {"id": "lex.en.200k.058009", "hw": "hesiods", "pos": "noun", "ipa": "/ˈhiːsiədz/", "vi": "nhà thơ Hy Lạp cổ đại Hesiod"},
    {"id": "lex.en.200k.058010", "hw": "histidines", "pos": "noun", "ipa": "/ˈhɪstɪdiːnz/", "vi": "các phân tử axit amin histidine"},
    {"id": "lex.en.200k.058011", "hw": "hoars", "pos": "noun", "ipa": "/hɔːrz/", "vi": "lớp sương muối trắng đóng băng"},
    {"id": "lex.en.200k.058012", "hw": "homebounds", "pos": "noun", "ipa": "/ˈhoʊmbaʊndz/", "vi": "người ốm liệt giường không ra ngoài"},
    {"id": "lex.en.200k.058013", "hw": "homunculi", "pos": "noun", "ipa": "/hoʊˈmʌŋkjʊlaɪ/", "vi": "người tí hon; hình nhân thu nhỏ"},
    {"id": "lex.en.200k.058014", "hw": "homunculuses", "pos": "noun", "ipa": "/hoʊˈmʌŋkjʊləsɪz/", "vi": "các hình nhân người tí hon giả kim"},
    {"id": "lex.en.200k.058015", "hw": "hyalines", "pos": "noun", "ipa": "/ˈhaɪəlɪnz/", "vi": "chất nền hyalin trong suốt"},
    {"id": "lex.en.200k.058016", "hw": "hydrazines", "pos": "noun", "ipa": "/ˈhaɪdrəziːnz/", "vi": "nhiên liệu tên lửa hydrazine"},
    {"id": "lex.en.200k.058017", "hw": "hyoids", "pos": "noun", "ipa": "/ˈhaɪɔɪdz/", "vi": "xương móng hình móng ngựa ở cổ"},
    {"id": "lex.en.200k.058018", "hw": "indexations", "pos": "noun", "ipa": "/ˌɪndɛkˈseɪʃənz/", "vi": "sự điều chỉnh theo chỉ số giá cả"},
    {"id": "lex.en.200k.058019", "hw": "inducted", "pos": "verb", "ipa": "/ɪnˈdʌktɪd/", "vi": "đã kết nạp; đã tuyên thệ nhậm chức"},
    {"id": "lex.en.200k.058020", "hw": "inducting", "pos": "verb", "ipa": "/ɪnˈdʌktɪŋ/", "vi": "đang kết nạp; làm lễ tuyên thệ"},
    {"id": "lex.en.200k.058021", "hw": "inducts", "pos": "verb", "ipa": "/ɪnˈdʌkts/", "vi": "kết nạp; làm lễ nhậm chức cho ai"},
    {"id": "lex.en.200k.058022", "hw": "islands of langerhans", "pos": "phrase", "ipa": "", "vi": "các tiểu đảo tụy Langerhans"},
    {"id": "lex.en.200k.058023", "hw": "jackrabbits", "pos": "noun", "ipa": "/ˈdʒækræbɪts/", "vi": "loài thỏ rừng tai dài Bắc Mỹ"},
    {"id": "lex.en.200k.058024", "hw": "john augustus roebling", "pos": "phrase", "ipa": "", "vi": "kỹ sư thiết kế cầu John Roebling"},
    {"id": "lex.en.200k.058025", "hw": "laughingstocks", "pos": "noun", "ipa": "/ˈlæfɪŋstɑːks/", "vi": "những trò hề trò cười cho thiên hạ"},
    {"id": "lex.en.200k.058026", "hw": "limpets", "pos": "noun", "ipa": "/ˈlɪmpɪts/", "vi": "các con ốc nón sao sao bám chặt đá"},
    {"id": "lex.en.200k.058027", "hw": "lorazepams", "pos": "noun", "ipa": "/ləˈræzəpæmz/", "vi": "thuốc an thần giải lo âu lorazepam"},
    {"id": "lex.en.200k.058028", "hw": "lunchrooms", "pos": "noun", "ipa": "/ˈlʌntʃruːmz/", "vi": "các phòng ăn trưa tập thể công sở"},
    {"id": "lex.en.200k.058029", "hw": "lychees", "pos": "noun", "ipa": "/ˈliːtʃiːz/", "vi": "các quả vải thiều; cây vải thiều"},
    {"id": "lex.en.200k.058030", "hw": "macdowells", "pos": "noun", "ipa": "/məkˈdaʊəlz/", "vi": "nhạc sĩ Mỹ Edward MacDowell"},
    {"id": "lex.en.200k.058031", "hw": "manticores", "pos": "noun", "ipa": "/ˈmæntɪkɔːrz/", "vi": "quái thú huyền thoại manticore"},
    {"id": "lex.en.200k.058032", "hw": "marceaus", "pos": "noun", "ipa": "/mɑːrˈsoʊz/", "vi": "nghệ sĩ kịch câm Marcel Marceau"},
    {"id": "lex.en.200k.058033", "hw": "marduks", "pos": "noun", "ipa": "/ˈmɑːrdʊks/", "vi": "thần tối cao Marduk xứ Babylon"},
    {"id": "lex.en.200k.058034", "hw": "matrilineal sib", "pos": "phrase", "ipa": "", "vi": "thị tộc quan hệ theo dòng mẹ"},
    {"id": "lex.en.200k.058035", "hw": "mesmers", "pos": "noun", "ipa": "/ˈmɛzmɚz/", "vi": "bác sĩ thôi miên Franz Mesmer"},
    {"id": "lex.en.200k.058036", "hw": "micheners", "pos": "noun", "ipa": "/ˈmɪtʃənɚz/", "vi": "nhà văn Mỹ James Michener"},
    {"id": "lex.en.200k.058037", "hw": "minkowskis", "pos": "noun", "ipa": "/mɪŋˈkɔːfskiz/", "vi": "nhà toán học Hermann Minkowski"},
    {"id": "lex.en.200k.058038", "hw": "mohammedans", "pos": "noun", "ipa": "/moʊˈhæmədənz/", "vi": "tín đồ theo đạo Hồi Hồi giáo"},
    {"id": "lex.en.200k.058039", "hw": "moping", "pos": "verb", "ipa": "/ˈmoʊpɪŋ/", "vi": "đang ủ rũ buồn bã; rầu rĩ chán nản"},
    {"id": "lex.en.200k.058040", "hw": "mordants", "pos": "noun", "ipa": "/ˈmɔːrdənts/", "vi": "chất cắn màu định hình nhuộm"},
    {"id": "lex.en.200k.058041", "hw": "morses", "pos": "noun", "ipa": "/ˈmɔːrsɪz/", "vi": "mã điện tín Morse; Samuel Morse"},
    {"id": "lex.en.200k.058042", "hw": "muscovies", "pos": "noun", "ipa": "/ˈmʌskəviz/", "vi": "đại công quốc Moskva; vịt xiêm"},
    {"id": "lex.en.200k.058043", "hw": "nakurus", "pos": "noun", "ipa": "/nɑːˈkuːruːz/", "vi": "thành phố và hồ nước kiềm Nakuru"},
    {"id": "lex.en.200k.058044", "hw": "nativists", "pos": "noun", "ipa": "/ˈneɪtɪvɪsts/", "vi": "người bảo vệ quyền lợi dân bản xứ"},
    {"id": "lex.en.200k.058045", "hw": "neoplasms", "pos": "noun", "ipa": "/ˈniːoʊplæzəmz/", "vi": "các khối u tân sinh bất thường"},
    {"id": "lex.en.200k.058046", "hw": "nervier", "pos": "adj", "ipa": "/ˈnɜːrviər/", "vi": "căng thẳng bồn chồn hơn; cả gan hơn"},
    {"id": "lex.en.200k.058047", "hw": "nerviest", "pos": "adj", "ipa": "/ˈnɜːrviɪst/", "vi": "căng thẳng nhất; cả gan nhất"},
    {"id": "lex.en.200k.058048", "hw": "nestorian church", "pos": "phrase", "ipa": "", "vi": "Giáo hội Đông phương Cảnh giáo"},
    {"id": "lex.en.200k.058049", "hw": "night jessamine", "pos": "phrase", "ipa": "", "vi": "hoa dạ lý hương ngát hương đêm"},
    {"id": "lex.en.200k.058050", "hw": "noguchis", "pos": "noun", "ipa": "/noʊˈɡuːtʃiz/", "vi": "nhà điêu khắc Isamu Noguchi"},
    {"id": "lex.en.200k.058051", "hw": "oafs", "pos": "noun", "ipa": "/oʊfs/", "vi": "những kẻ vụng về cục mịch đần độn"},
    {"id": "lex.en.200k.058052", "hw": "oocytes", "pos": "noun", "ipa": "/ˈoʊəsaɪts/", "vi": "các tế bào noãn bào nguyên thủy"},
    {"id": "lex.en.200k.058053", "hw": "othos", "pos": "noun", "ipa": "/ˈoʊθoʊz/", "vi": "hoàng đế La Mã Otho trị vì ngắn"},
    {"id": "lex.en.200k.058054", "hw": "oven stuffer roaster", "pos": "phrase", "ipa": "", "vi": "gà béo chuyên nướng lò nguyên con"},
    {"id": "lex.en.200k.058055", "hw": "paediatricians", "pos": "noun", "ipa": "/ˌpiːdiəˈtrɪʃənz/", "vi": "các bác sĩ chuyên khoa nhi đồng"},
    {"id": "lex.en.200k.058056", "hw": "pamir mountains", "pos": "phrase", "ipa": "", "vi": "dãy núi cao hiểm trở Pamir Trung Á"},
    {"id": "lex.en.200k.058057", "hw": "pdls", "pos": "noun", "ipa": "/ˌpiː.diːˈɛlz/", "vi": "đơn vị đo lực poundal trong hệ Anh"},
    {"id": "lex.en.200k.058058", "hw": "per centum", "pos": "phrase", "ipa": "", "vi": "tỷ lệ phần trăm; mỗi một trăm"},
    {"id": "lex.en.200k.058059", "hw": "perennial ryegrass", "pos": "phrase", "ipa": "", "vi": "cỏ lúa mạch đen sống lâu năm"},
    {"id": "lex.en.200k.058060", "hw": "phoboses", "pos": "noun", "ipa": "/ˈfoʊbɑːsɪz/", "vi": "vệ tinh Phobos của sao Hỏa"},
    {"id": "lex.en.200k.058061", "hw": "phoenicias", "pos": "noun", "ipa": "/fəˈnɪʃiəz/", "vi": "nền văn minh cổ đại Phoenicia"},
    {"id": "lex.en.200k.058062", "hw": "phrasal idiom", "pos": "phrase", "ipa": "", "vi": "cụm ngữ thành ngữ cố định"},
    {"id": "lex.en.200k.058063", "hw": "pipas", "pos": "noun", "ipa": "/ˈpiːpəz/", "vi": "đàn tỳ bà cổ truyền phương Đông"},
    {"id": "lex.en.200k.058064", "hw": "pomfrets", "pos": "noun", "ipa": "/ˈpɑːmfrɪts/", "vi": "các loài cá chim trắng đại dương"},
    {"id": "lex.en.200k.058065", "hw": "porgies", "pos": "noun", "ipa": "/ˈpɔːrdʒiz/", "vi": "loài cá tráp biển ăn ngon thịt"},
    {"id": "lex.en.200k.058066", "hw": "pupillary reflex", "pos": "phrase", "ipa": "", "vi": "phản xạ co giãn đồng tử mắt"},
    {"id": "lex.en.200k.058067", "hw": "radixes", "pos": "noun", "ipa": "/ˈreɪdɪksɪz/", "vi": "các cơ số của hệ đếm toán học"},
    {"id": "lex.en.200k.058068", "hw": "rembrandt van ryn", "pos": "phrase", "ipa": "", "vi": "danh họa Rembrandt van Rijn"},
    {"id": "lex.en.200k.058069", "hw": "repercussions", "pos": "noun", "ipa": "/ˌriːpɚˈkʌʃənz/", "vi": "hậu quả tiêu cực dội lại lâu dài"},
    {"id": "lex.en.200k.058070", "hw": "rooter skunk", "pos": "phrase", "ipa": "", "vi": "loài chồn hôi mõm lợn đào bới"},
    {"id": "lex.en.200k.058071", "hw": "sarcoidoses", "pos": "noun", "ipa": "/ˌsɑːrkɔɪˈdoʊsiːz/", "vi": "bệnh u hạt sarcoidosis toàn thân"},
    {"id": "lex.en.200k.058072", "hw": "schnabels", "pos": "noun", "ipa": "/ˈʃnɑːbəlz/", "vi": "nghệ sĩ dương cầm vĩ đại Schnabel"},
    {"id": "lex.en.200k.058073", "hw": "scythians", "pos": "noun", "ipa": "/ˈsɪðiənz/", "vi": "người du mục du mục Scythia cổ"},
    {"id": "lex.en.200k.058074", "hw": "shallow fording", "pos": "phrase", "ipa": "", "vi": "chỗ lội cạn an toàn qua sông"},
    {"id": "lex.en.200k.058075", "hw": "shockleys", "pos": "noun", "ipa": "/ˈʃɑːkliz/", "vi": "nhà vật lý Nobel William Shockley"},
    {"id": "lex.en.200k.058076", "hw": "sibilant consonant", "pos": "phrase", "ipa": "", "vi": "phụ âm xuýt rít gió trong ngữ âm"},
    {"id": "lex.en.200k.058077", "hw": "skylabs", "pos": "noun", "ipa": "/ˈskaɪlæbz/", "vi": "trạm không gian Skylab của NASA"},
    {"id": "lex.en.200k.058078", "hw": "sohs", "pos": "noun", "ipa": "/soʊz/", "vi": "các nốt sol trong xướng âm giọng"},
    {"id": "lex.en.200k.058079", "hw": "solitary vireo", "pos": "phrase", "ipa": "", "vi": "loài chim hót vireo đơn độc"},
    {"id": "lex.en.200k.058080", "hw": "sorptions", "pos": "noun", "ipa": "/ˈsɔːrpʃənz/", "vi": "quá trình hấp phụ và hấp thụ chất"},
    {"id": "lex.en.200k.058081", "hw": "spyglasses", "pos": "noun", "ipa": "/ˈspaɪɡlæsɪz/", "vi": "ống nhòm hải tặc thu gọn cầm tay"},
    {"id": "lex.en.200k.058082", "hw": "squeakers", "pos": "noun", "ipa": "/ˈskwiːkɚz/", "vi": "đồ chơi kêu chít chít; chim non"},
    {"id": "lex.en.200k.058083", "hw": "stony tunguska", "pos": "phrase", "ipa": "", "vi": "dòng sông Stony Tunguska nước Nga"},
    {"id": "lex.en.200k.058084", "hw": "strix varia", "pos": "phrase", "ipa": "", "vi": "loài cú mèo vằn sọc Bắc Mỹ"},
    {"id": "lex.en.200k.058085", "hw": "stylers", "pos": "noun", "ipa": "/ˈstaɪlɚz/", "vi": "nhà tạo mẫu tóc; dụng cụ tạo kiểu"},
    {"id": "lex.en.200k.058086", "hw": "synesthesias", "pos": "noun", "ipa": "/ˌsɪnəsˈθiːziəz/", "vi": "hiện tượng cảm giác kèm giác quan"},
    {"id": "lex.en.200k.058087", "hw": "taxiways", "pos": "noun", "ipa": "/ˈtæksiweɪz/", "vi": "đường lăn máy bay nối ra đường băng"},
    {"id": "lex.en.200k.058088", "hw": "teepees", "pos": "noun", "ipa": "/ˈtiːpiːz/", "vi": "lều nón da thú của thổ dân Mỹ"},
    {"id": "lex.en.200k.058089", "hw": "theodor schwann", "pos": "phrase", "ipa": "", "vi": "nhà sinh lý học Theodor Schwann"},
    {"id": "lex.en.200k.058090", "hw": "thripses", "pos": "noun", "ipa": "/ˈθrɪpsɪz/", "vi": "các con bọ trĩ phá hoại cây trồng"},
    {"id": "lex.en.200k.058091", "hw": "tipus", "pos": "noun", "ipa": "/ˈtiːpuːz/", "vi": "cây hoa vàng cảnh quan chi Tipuana"},
    {"id": "lex.en.200k.058092", "hw": "tokamaks", "pos": "noun", "ipa": "/ˈtoʊkəmæks/", "vi": "lò phản ứng nhiệt hạch tokamak"},
    {"id": "lex.en.200k.058093", "hw": "tolu tree", "pos": "phrase", "ipa": "", "vi": "cây dầu nhựa thơm Tolu Peru"},
    {"id": "lex.en.200k.058094", "hw": "transferases", "pos": "noun", "ipa": "/trænsˈfɜːreɪsɪz/", "vi": "loại men chuyển nhóm transferase"},
    {"id": "lex.en.200k.058095", "hw": "truelove knot", "pos": "phrase", "ipa": "", "vi": "nút thắt tình duyên trọn đời"},
    {"id": "lex.en.200k.058096", "hw": "turkis", "pos": "noun", "ipa": "/ˈtɜːrkɪz/", "vi": "người Thổ hoặc ngữ hệ Turkic"},
    {"id": "lex.en.200k.058097", "hw": "turncoats", "pos": "noun", "ipa": "/ˈtɜːrnkoʊts/", "vi": "những kẻ trở cờ phản bội đồng đội"},
    {"id": "lex.en.200k.058098", "hw": "tushes", "pos": "noun", "ipa": "/ˈtʌʃɪz/", "vi": "cặp mông; ngà voi; răng nanh ngựa"},
    {"id": "lex.en.200k.058099", "hw": "ulamas", "pos": "noun", "ipa": "/ˈuːləmɑːz/", "vi": "các học giả giáo sĩ Hồi giáo"},
    {"id": "lex.en.200k.058100", "hw": "unconditioned reflex", "pos": "phrase", "ipa": "", "vi": "phản xạ không điều kiện bẩm sinh"},
    {"id": "lex.en.200k.058101", "hw": "wernher von braun", "pos": "phrase", "ipa": "", "vi": "kỹ sư tên lửa Wernher von Braun"}
]

# Validation
with open('scratch/b32_r07_raw_p1.json') as f:
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
final_p1 = []
for r, raw_r in zip(records, raw):
    item = dict(raw_r)
    item['pos'] = r['pos']
    item['ipa'] = r['ipa']
    item['vi'] = r['vi']
    item['status'] = 'reviewed'
    final_p1.append(item)

with open('scratch/b32_r07_p1.json', 'w') as f:
    json.dump(final_p1, f, ensure_ascii=False, indent=2)
print("Part 1 validated and written successfully.")
