import json

records = [
    {"id": "lex.en.200k.057202", "hw": "rapers", "pos": "noun", "ipa": "/ˈreɪpɚz/", "vi": "kẻ hiếp dâm; kẻ cưỡng bức"},
    {"id": "lex.en.200k.057203", "hw": "reassigned", "pos": "verb", "ipa": "/ˌriːəˈsaɪnd/", "vi": "đã phân công lại; đã điều chuyển"},
    {"id": "lex.en.200k.057204", "hw": "reassigning", "pos": "verb", "ipa": "/ˌriːəˈsaɪnɪŋ/", "vi": "đang phân công lại; điều chuyển"},
    {"id": "lex.en.200k.057205", "hw": "reassigns", "pos": "verb", "ipa": "/ˌriːəˈsaɪnz/", "vi": "phân công lại; điều chuyển"},
    {"id": "lex.en.200k.057206", "hw": "reevaluations", "pos": "noun", "ipa": "/ˌriːɪˌvæljuˈeɪʃənz/", "vi": "sự đánh giá lại; thẩm định lại"},
    {"id": "lex.en.200k.057207", "hw": "reliquaries", "pos": "noun", "ipa": "/ˈrɛlɪkwɛriz/", "vi": "hòm đựng thánh tích tôn giáo"},
    {"id": "lex.en.200k.057208", "hw": "romanticized", "pos": "verb", "ipa": "/roʊˈmæntɪsaɪzd/", "vi": "đã lãng mạn hóa; lý tưởng hóa"},
    {"id": "lex.en.200k.057209", "hw": "romanticizes", "pos": "verb", "ipa": "/roʊˈmæntɪsaɪzɪz/", "vi": "lãng mạn hóa; lý tưởng hóa"},
    {"id": "lex.en.200k.057210", "hw": "romanticizing", "pos": "verb", "ipa": "/roʊˈmæntɪsaɪzɪŋ/", "vi": "đang lãng mạn hóa; lý tưởng hóa"},
    {"id": "lex.en.200k.057211", "hw": "rumens", "pos": "noun", "ipa": "/ˈruːmənz/", "vi": "các dạ cỏ của động vật nhai lại"},
    {"id": "lex.en.200k.057212", "hw": "rumina", "pos": "noun", "ipa": "/ˈruːmɪnə/", "vi": "dạ cỏ ở động vật nhai lại"},
    {"id": "lex.en.200k.057213", "hw": "samarkands", "pos": "noun", "ipa": "/ˈsæmɚkændz/", "vi": "thành phố cổ Samarkand"},
    {"id": "lex.en.200k.057214", "hw": "sardinians", "pos": "noun", "ipa": "/sɑːrˈdɪniənz/", "vi": "người dân vùng đảo Sardinia Ý"},
    {"id": "lex.en.200k.057215", "hw": "schizoids", "pos": "noun", "ipa": "/ˈskɪzɔɪdz/", "vi": "người rối loạn nhân cách phân liệt"},
    {"id": "lex.en.200k.057216", "hw": "screeners", "pos": "noun", "ipa": "/ˈskriːnɚz/", "vi": "nhân viên soi chiếu an ninh"},
    {"id": "lex.en.200k.057217", "hw": "seppukus", "pos": "noun", "ipa": "/sɛˈpuːkuːz/", "vi": "nghi thức mổ bụng tự sát seppuku"},
    {"id": "lex.en.200k.057218", "hw": "sexts", "pos": "noun", "ipa": "/sɛksts/", "vi": "giờ kinh thứ sáu; tin nhắn gợi dục"},
    {"id": "lex.en.200k.057219", "hw": "softwoods", "pos": "noun", "ipa": "/ˈsɔːftwʊdz/", "vi": "các loại gỗ mềm; gỗ cây lá kim"},
    {"id": "lex.en.200k.057220", "hw": "sojourners", "pos": "noun", "ipa": "/ˈsoʊdʒɜːrnɚz/", "vi": "những người tạm trú chân qua đường"},
    {"id": "lex.en.200k.057221", "hw": "soppier", "pos": "adj", "ipa": "/ˈsɑːpiər/", "vi": "ẩm ướt hơn; ủy mị ướt át hơn"},
    {"id": "lex.en.200k.057222", "hw": "soppiest", "pos": "adj", "ipa": "/ˈsɑːpiɪst/", "vi": "ẩm ướt nhất; ủy mị ướt át nhất"},
    {"id": "lex.en.200k.057223", "hw": "soundboards", "pos": "noun", "ipa": "/ˈsaʊndbɔːrdz/", "vi": "bảng cộng hưởng; bàn trộn âm thanh"},
    {"id": "lex.en.200k.057224", "hw": "ssris", "pos": "noun", "ipa": "/ˌɛs.ɛs.ɑːrˈaɪz/", "vi": "thuốc ức chế tái hấp thu serotonin"},
    {"id": "lex.en.200k.057225", "hw": "stumpier", "pos": "adj", "ipa": "/ˈstʌmpiər/", "vi": "ngắn ngủn mập mạp hơn"},
    {"id": "lex.en.200k.057226", "hw": "stumpiest", "pos": "adj", "ipa": "/ˈstʌmpiɪst/", "vi": "ngắn ngủn mập mạp nhất"},
    {"id": "lex.en.200k.057227", "hw": "subcompacts", "pos": "noun", "ipa": "/sʌbˈkɑːmpækts/", "vi": "các xe ô tô cỡ nhỏ subcompact"},
    {"id": "lex.en.200k.057228", "hw": "sulci", "pos": "noun", "ipa": "/ˈsʌlsaɪ/", "vi": "các rãnh trên bề mặt vỏ não"},
    {"id": "lex.en.200k.057229", "hw": "sulcuses", "pos": "noun", "ipa": "/ˈsʌlkəsɪz/", "vi": "các rãnh giải phẫu; khe nứt"},
    {"id": "lex.en.200k.057230", "hw": "telecasters", "pos": "noun", "ipa": "/ˈtɛlikæstɚz/", "vi": "người dẫn chương trình truyền hình"},
    {"id": "lex.en.200k.057231", "hw": "tetrahedra", "pos": "noun", "ipa": "/ˌtɛtrəˈhiːdrə/", "vi": "các khối hình tứ diện đều"},
    {"id": "lex.en.200k.057232", "hw": "tetrahedrons", "pos": "noun", "ipa": "/ˌtɛtrəˈhiːdrənz/", "vi": "các hình khối tứ diện"},
    {"id": "lex.en.200k.057233", "hw": "trevinos", "pos": "noun", "ipa": "/trəˈviːnjoʊz/", "vi": "những người mang họ Trevino"},
    {"id": "lex.en.200k.057234", "hw": "tricolours", "pos": "noun", "ipa": "/ˈtraɪkʌlɚz/", "vi": "các lá cờ tam tài ba màu"},
    {"id": "lex.en.200k.057235", "hw": "turnabouts", "pos": "noun", "ipa": "/ˈtɜːrnəbaʊts/", "vi": "sự quay ngoắt; đổi chiều thái độ"},
    {"id": "lex.en.200k.057236", "hw": "vandas", "pos": "noun", "ipa": "/ˈvændəz/", "vi": "hoa lan Vanda nhiệt đới"},
    {"id": "lex.en.200k.057237", "hw": "vapourses", "pos": "noun", "ipa": "/ˈveɪpɚsɪz/", "vi": "chứng u uất; sự ủ rũ buồn phiền"},
    {"id": "lex.en.200k.057238", "hw": "vauxes", "pos": "noun", "ipa": "/vɔːksɪz/", "vi": "các địa danh hoặc gia tộc Vaux"},
    {"id": "lex.en.200k.057239", "hw": "velars", "pos": "noun", "ipa": "/ˈviːlɚz/", "vi": "phụ âm ngạc mềm trong ngữ âm"},
    {"id": "lex.en.200k.057240", "hw": "verbenas", "pos": "noun", "ipa": "/vɚˈbiːnəz/", "vi": "cây cỏ roi ngựa hoa tím"},
    {"id": "lex.en.200k.057241", "hw": "wealds", "pos": "noun", "ipa": "/wiːldz/", "vi": "vùng đồng hoang cỏ và rừng cây"},
    {"id": "lex.en.200k.057242", "hw": "wheatgrasses", "pos": "noun", "ipa": "/ˈwiːtɡræsɪz/", "vi": "cỏ lúa mì non dinh dưỡng"},
    {"id": "lex.en.200k.057243", "hw": "woodchucks", "pos": "noun", "ipa": "/ˈwʊdtʃʌks/", "vi": "sóc đất mac-mốt châu Mỹ"},
    {"id": "lex.en.200k.057244", "hw": "aland islands", "pos": "phrase", "ipa": "", "vi": "quần đảo tự trị Åland Phần Lan"},
    {"id": "lex.en.200k.057245", "hw": "antigonus cyclops", "pos": "phrase", "ipa": "", "vi": "tướng Antigonus Một Mắt Macedonia"},
    {"id": "lex.en.200k.057246", "hw": "artaxerxes ii", "pos": "phrase", "ipa": "", "vi": "vua Ba Tư Artaxerxes II cổ đại"},
    {"id": "lex.en.200k.057247", "hw": "arthur koestler", "pos": "phrase", "ipa": "", "vi": "nhà văn Arthur Koestler"},
    {"id": "lex.en.200k.057248", "hw": "asian seabass", "pos": "phrase", "ipa": "", "vi": "cá chẽm châu Á; cá vược chẽm"},
    {"id": "lex.en.200k.057249", "hw": "aspartic acid", "pos": "phrase", "ipa": "", "vi": "axit aspartic; axit amin aspartic"},
    {"id": "lex.en.200k.057250", "hw": "bacteriological warfare", "pos": "phrase", "ipa": "", "vi": "chiến tranh vũ khí vi khuẩn"},
    {"id": "lex.en.200k.057251", "hw": "baryon number", "pos": "phrase", "ipa": "", "vi": "số lượng tử baryon trong vật lý"},
    {"id": "lex.en.200k.057252", "hw": "bayt lahm", "pos": "phrase", "ipa": "", "vi": "thành phố Bethlehem Đất Thánh"},
    {"id": "lex.en.200k.057253", "hw": "belgian endive", "pos": "phrase", "ipa": "", "vi": "rau diếp xoăn Bỉ búp trắng"},
    {"id": "lex.en.200k.057254", "hw": "coosa river", "pos": "phrase", "ipa": "", "vi": "dòng sông Coosa ở miền nam Mỹ"},
    {"id": "lex.en.200k.057255", "hw": "cuboid bone", "pos": "phrase", "ipa": "", "vi": "xương hộp ở cổ chân bàn chân"},
    {"id": "lex.en.200k.057256", "hw": "curly endive", "pos": "phrase", "ipa": "", "vi": "rau diếp xoăn lá xoăn"},
    {"id": "lex.en.200k.057257", "hw": "darkling beetle", "pos": "phrase", "ipa": "", "vi": "bọ cánh cứng bóng tối bọ hắc ám"},
    {"id": "lex.en.200k.057258", "hw": "demotic script", "pos": "phrase", "ipa": "", "vi": "chữ viết Demotic Ai Cập cổ đại"},
    {"id": "lex.en.200k.057259", "hw": "divina commedia", "pos": "phrase", "ipa": "", "vi": "thi phẩm trường ca Thần khúc Dante"},
    {"id": "lex.en.200k.057260", "hw": "dolman jacket", "pos": "phrase", "ipa": "", "vi": "áo khoác ngắn quân đội kỵ binh"},
    {"id": "lex.en.200k.057261", "hw": "dugald stewart", "pos": "phrase", "ipa": "", "vi": "triết gia người Scotland Stewart"},
    {"id": "lex.en.200k.057262", "hw": "european nightjar", "pos": "phrase", "ipa": "", "vi": "loài chim cú muỗi châu Âu"},
    {"id": "lex.en.200k.057263", "hw": "fricative consonant", "pos": "phrase", "ipa": "", "vi": "phụ âm xát trong ngữ âm học"},
    {"id": "lex.en.200k.057264", "hw": "genitourinary system", "pos": "phrase", "ipa": "", "vi": "hệ cơ quan sinh dục và tiết niệu"},
    {"id": "lex.en.200k.057265", "hw": "genus primula", "pos": "phrase", "ipa": "", "vi": "chi Anh thảo trong thực vật học"},
    {"id": "lex.en.200k.057266", "hw": "genus ranunculus", "pos": "phrase", "ipa": "", "vi": "chi Mao lương hoa vàng"},
    {"id": "lex.en.200k.057267", "hw": "genus salmo", "pos": "phrase", "ipa": "", "vi": "chi Cá hồi Đại Tây Dương"},
    {"id": "lex.en.200k.057268", "hw": "genus vigna", "pos": "phrase", "ipa": "", "vi": "chi thực vật Đậu đỗ Vigna"},
    {"id": "lex.en.200k.057269", "hw": "greek drachma", "pos": "phrase", "ipa": "", "vi": "đồng tiền drachma Hy Lạp cổ"},
    {"id": "lex.en.200k.057270", "hw": "hoagland howard carmichael", "pos": "phrase", "ipa": "", "vi": "nhạc sĩ Hoagy Carmichael Mỹ"},
    {"id": "lex.en.200k.057271", "hw": "indeterminacy principle", "pos": "phrase", "ipa": "", "vi": "nguyên lý bất định Heisenberg"},
    {"id": "lex.en.200k.057272", "hw": "inflectional suffix", "pos": "phrase", "ipa": "", "vi": "hậu tố biến cách ngữ pháp"},
    {"id": "lex.en.200k.057273", "hw": "insurable interest", "pos": "phrase", "ipa": "", "vi": "quyền lợi có thể bảo hiểm được"},
    {"id": "lex.en.200k.057274", "hw": "isotonic exercise", "pos": "phrase", "ipa": "", "vi": "bài tập vận động đẳng trương"},
    {"id": "lex.en.200k.057275", "hw": "isotonic solution", "pos": "phrase", "ipa": "", "vi": "dung dịch đẳng trương sinh lý"},
    {"id": "lex.en.200k.057276", "hw": "kam muang", "pos": "phrase", "ipa": "", "vi": "tiếng miền Bắc Thái Lan Kam Muang"},
    {"id": "lex.en.200k.057277", "hw": "ken kesey", "pos": "phrase", "ipa": "", "vi": "tiểu thuyết gia người Mỹ Ken Kesey"},
    {"id": "lex.en.200k.057278", "hw": "little golden zinnia", "pos": "phrase", "ipa": "", "vi": "hoa cúc zinnia nhỏ hoa vàng"},
    {"id": "lex.en.200k.057279", "hw": "mario vargas llosa", "pos": "phrase", "ipa": "", "vi": "nhà văn đoạt Nobel Vargas Llosa"},
    {"id": "lex.en.200k.057280", "hw": "maundy money", "pos": "phrase", "ipa": "", "vi": "tiền bố thí Thứ Năm Tuần Thánh"},
    {"id": "lex.en.200k.057281", "hw": "maundy thursday", "pos": "phrase", "ipa": "", "vi": "Thứ Năm Tuần Thánh; lễ Tiệc Ly"},
    {"id": "lex.en.200k.057282", "hw": "mornay sauce", "pos": "phrase", "ipa": "", "vi": "sốt phô mai Mornay kiểu Pháp"},
    {"id": "lex.en.200k.057283", "hw": "niobrara river", "pos": "phrase", "ipa": "", "vi": "dòng sông Niobrara ở bang Nebraska"},
    {"id": "lex.en.200k.057284", "hw": "parietal pericardium", "pos": "phrase", "ipa": "", "vi": "lá thành màng ngoài tim"},
    {"id": "lex.en.200k.057285", "hw": "phrasal verb", "pos": "phrase", "ipa": "", "vi": "cụm động từ trong ngữ pháp Anh"},
    {"id": "lex.en.200k.057286", "hw": "plutonic rock", "pos": "phrase", "ipa": "", "vi": "đá magma xâm nhập sâu"},
    {"id": "lex.en.200k.057287", "hw": "prosodic system", "pos": "phrase", "ipa": "", "vi": "hệ thống ngữ điệu trọng âm"},
    {"id": "lex.en.200k.057288", "hw": "reinhold niebuhr", "pos": "phrase", "ipa": "", "vi": "nhà thần học Mỹ Reinhold Niebuhr"},
    {"id": "lex.en.200k.057289", "hw": "rudolf nureyev", "pos": "phrase", "ipa": "", "vi": "vũ công ba lê Rudolf Nureyev"},
    {"id": "lex.en.200k.057290", "hw": "sanctum sanctorum", "pos": "phrase", "ipa": "", "vi": "nơi cực thánh; chốn riêng tư nhất"},
    {"id": "lex.en.200k.057291", "hw": "scheldt river", "pos": "phrase", "ipa": "", "vi": "dòng sông Scheldt ở Tây Âu"},
    {"id": "lex.en.200k.057292", "hw": "sigmoid sinus", "pos": "phrase", "ipa": "", "vi": "xoang tĩnh mạch sigma màng cứng"},
    {"id": "lex.en.200k.057293", "hw": "sturm und drang", "pos": "phrase", "ipa": "", "vi": "phong trào Bão táp và Xung kích"},
    {"id": "lex.en.200k.057294", "hw": "sunray lamp", "pos": "phrase", "ipa": "", "vi": "đèn chiếu tia cực tím y tế"},
    {"id": "lex.en.200k.057295", "hw": "tubeless tire", "pos": "phrase", "ipa": "", "vi": "lốp xe không săm; vỏ không ruột"},
    {"id": "lex.en.200k.057296", "hw": "tussock moth", "pos": "phrase", "ipa": "", "vi": "bướm đêm họ sâu róm chùm lông"},
    {"id": "lex.en.200k.057297", "hw": "ulrich zwingli", "pos": "phrase", "ipa": "", "vi": "nhà cải cách Thụy Sĩ Zwingli"},
    {"id": "lex.en.200k.057298", "hw": "ultra vires", "pos": "phrase", "ipa": "", "vi": "vượt quá thẩm quyền pháp lý"},
    {"id": "lex.en.200k.057299", "hw": "vargas llosa", "pos": "phrase", "ipa": "", "vi": "văn hào Peru Mario Vargas Llosa"},
    {"id": "lex.en.200k.057300", "hw": "white seabass", "pos": "phrase", "ipa": "", "vi": "loài cá lù đù cá vược trắng"},
    {"id": "lex.en.200k.057301", "hw": "white zinnia", "pos": "phrase", "ipa": "", "vi": "hoa cúc cúc zinnia trắng"}
]

# Validation
with open('scratch/b32_r05_raw_p3.json') as f:
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

with open('scratch/b32_r05_p3.json', 'w') as f:
    json.dump(final_p3, f, ensure_ascii=False, indent=2)
print("Part 3 validated and written successfully.")
