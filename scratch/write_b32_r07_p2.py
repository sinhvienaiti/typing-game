import json

records = [
    {"id": "lex.en.200k.058102", "hw": "whippets", "pos": "noun", "ipa": "/ˈwɪpɪts/", "vi": "giống chó săn cảnh nhỏ whippet"},
    {"id": "lex.en.200k.058103", "hw": "whorehouses", "pos": "noun", "ipa": "/ˈhɔːrhaʊsɪz/", "vi": "các nhà thổ chứa chấp gái mại dâm"},
    {"id": "lex.en.200k.058104", "hw": "wsws", "pos": "noun", "ipa": "/ˌdʌbəl.juː.ɛsˈdʌbəl.juːz/", "vi": "hướng tây-tây nam trên la bàn"},
    {"id": "lex.en.200k.058105", "hw": "yellow foxtail", "pos": "phrase", "ipa": "", "vi": "cây cỏ đuôi chồn hoa vàng dại"},
    {"id": "lex.en.200k.058106", "hw": "yellow jessamine", "pos": "phrase", "ipa": "", "vi": "loài cây hoa lài vàng Carolina"},
    {"id": "lex.en.200k.058107", "hw": "zhukovs", "pos": "noun", "ipa": "/ˈʒuːkɔːfs/", "vi": "nguyên soái Liên Xô Georgy Zhukov"},
    {"id": "lex.en.200k.058108", "hw": "affrays", "pos": "noun", "ipa": "/əˈfreɪz/", "vi": "vụ ẩu đả náo loạn nơi công cộng"},
    {"id": "lex.en.200k.058109", "hw": "agronomists", "pos": "noun", "ipa": "/əˈɡrɑːnəmɪsts/", "vi": "chuyên gia kỹ sư ngành nông học"},
    {"id": "lex.en.200k.058110", "hw": "ambos", "pos": "noun", "ipa": "/ˈæmboʊz/", "vi": "bục giảng đài trong nhà thờ cổ"},
    {"id": "lex.en.200k.058111", "hw": "astrolabes", "pos": "noun", "ipa": "/ˈæstrəleɪbz/", "vi": "thước trắc tinh đo thiên thể cổ"},
    {"id": "lex.en.200k.058112", "hw": "bellybuttons", "pos": "noun", "ipa": "/ˈbɛlibʌtənz/", "vi": "lỗ rốn ở giữa bụng người"},
    {"id": "lex.en.200k.058113", "hw": "bloks", "pos": "noun", "ipa": "/blɑːks/", "vi": "nhà thơ Nga Aleksandr Blok"},
    {"id": "lex.en.200k.058114", "hw": "bordellos", "pos": "noun", "ipa": "/bɔːrˈdɛloʊz/", "vi": "các nhà chứa lầu xanh kỹ nữ"},
    {"id": "lex.en.200k.058115", "hw": "brassicas", "pos": "noun", "ipa": "/ˈbræsɪkəz/", "vi": "các loại rau thuộc chi Cải bắp"},
    {"id": "lex.en.200k.058116", "hw": "brattleboros", "pos": "noun", "ipa": "/ˈbrætəlbɚroʊz/", "vi": "thị trấn cổ Brattleboro ở Vermont"},
    {"id": "lex.en.200k.058117", "hw": "brises", "pos": "noun", "ipa": "/ˈbrɪsɪz/", "vi": "lễ cắt bao quy đầu Do Thái"},
    {"id": "lex.en.200k.058118", "hw": "broodier", "pos": "adj", "ipa": "/ˈbruːdiər/", "vi": "thích ấp trứng hơn; trầm ngâm hơn"},
    {"id": "lex.en.200k.058119", "hw": "broodiest", "pos": "adj", "ipa": "/ˈbruːdiɪst/", "vi": "hay ấp trứng nhất; trầm ngâm nhất"},
    {"id": "lex.en.200k.058120", "hw": "bullas", "pos": "noun", "ipa": "/ˈbʊləz/", "vi": "các bọng nước phồng rộp trên da"},
    {"id": "lex.en.200k.058121", "hw": "bullfighters", "pos": "noun", "ipa": "/ˈbʊlfaɪtɚz/", "vi": "các đấu sĩ đấu bò tót Tây Ban Nha"},
    {"id": "lex.en.200k.058122", "hw": "bullrings", "pos": "noun", "ipa": "/ˈbʊlrɪŋz/", "vi": "các đấu trường giác đấu bò tót"},
    {"id": "lex.en.200k.058123", "hw": "buskers", "pos": "noun", "ipa": "/ˈbʌskɚz/", "vi": "những nghệ sĩ biểu diễn đường phố"},
    {"id": "lex.en.200k.058124", "hw": "butadienes", "pos": "noun", "ipa": "/ˌbjuːtəˈdaɪiːnz/", "vi": "chất butadien dùng sản xuất cao su"},
    {"id": "lex.en.200k.058125", "hw": "canutes", "pos": "noun", "ipa": "/kəˈnuːts/", "vi": "vua Canute Đại đế vùng Bắc Âu"},
    {"id": "lex.en.200k.058126", "hw": "cardholders", "pos": "noun", "ipa": "/ˈkɑːrdhoʊldɚz/", "vi": "các chủ sở hữu thẻ ngân hàng"},
    {"id": "lex.en.200k.058127", "hw": "chicaneries", "pos": "noun", "ipa": "/ʃɪˈkeɪnəriz/", "vi": "những mánh khóe lừa đảo xảo quyệt"},
    {"id": "lex.en.200k.058128", "hw": "cimarrons", "pos": "noun", "ipa": "/ˈsɪmərɑːnz/", "vi": "dòng sông Cimarron; bò hoang dại"},
    {"id": "lex.en.200k.058129", "hw": "commandeered", "pos": "verb", "ipa": "/ˌkɑːmənˈdɪrd/", "vi": "đã trưng thu; trưng dụng quân sự"},
    {"id": "lex.en.200k.058130", "hw": "commandeering", "pos": "verb", "ipa": "/ˌkɑːmənˈdɪrɪŋ/", "vi": "đang trưng dụng cưỡng chế"},
    {"id": "lex.en.200k.058131", "hw": "commandeers", "pos": "verb", "ipa": "/ˌkɑːmənˈdɪrz/", "vi": "trưng dụng; chiếm đoạt tài sản"},
    {"id": "lex.en.200k.058132", "hw": "dalliances", "pos": "noun", "ipa": "/ˈdæliənsɪz/", "vi": "mối tình thoảng qua; sự chần chừ"},
    {"id": "lex.en.200k.058133", "hw": "demonizations", "pos": "noun", "ipa": "/ˌdiːmənaɪˈzeɪʃənz/", "vi": "sự bôi nhọ biến ai thành quỷ dữ"},
    {"id": "lex.en.200k.058134", "hw": "dosimetries", "pos": "noun", "ipa": "/doʊˈsɪmətriːz/", "vi": "kỹ thuật đo liều lượng phóng xạ"},
    {"id": "lex.en.200k.058135", "hw": "doughier", "pos": "adj", "ipa": "/ˈdoʊiər/", "vi": "nhão dẻo như bột bánh hơn"},
    {"id": "lex.en.200k.058136", "hw": "doughiest", "pos": "adj", "ipa": "/ˈdoʊiɪst/", "vi": "nhão dẻo như bột bánh nhất"},
    {"id": "lex.en.200k.058137", "hw": "gansus", "pos": "noun", "ipa": "/ˈɡænsuːz/", "vi": "tỉnh Cam Túc ở miền tây Trung Quốc"},
    {"id": "lex.en.200k.058138", "hw": "glycerines", "pos": "noun", "ipa": "/ˈɡlɪsərɪnz/", "vi": "dung dịch glyxerin giữ ẩm ngọt dịu"},
    {"id": "lex.en.200k.058139", "hw": "gramas", "pos": "noun", "ipa": "/ˈɡrɑːməz/", "vi": "loài cỏ đồng cỏ chăn nuôi grama"},
    {"id": "lex.en.200k.058140", "hw": "hegelians", "pos": "noun", "ipa": "/heɪˈɡeɪliənz/", "vi": "những người theo triết học Hegel"},
    {"id": "lex.en.200k.058141", "hw": "husayns", "pos": "noun", "ipa": "/huːˈseɪnz/", "vi": "vua hoặc thủ lĩnh mang tên Husayn"},
    {"id": "lex.en.200k.058142", "hw": "ingratiated", "pos": "verb", "ipa": "/ɪnˈɡreɪʃieɪtɪd/", "vi": "đã khéo lấy lòng; luồn cúi bợ đỡ"},
    {"id": "lex.en.200k.058143", "hw": "irrawaddies", "pos": "noun", "ipa": "/ˌɪrəˈwɑːdiz/", "vi": "dòng sông Ayeyarwady ở Myanmar"},
    {"id": "lex.en.200k.058144", "hw": "karloffs", "pos": "noun", "ipa": "/ˈkɑːrlɔːfs/", "vi": "nam diễn viên kinh dị Boris Karloff"},
    {"id": "lex.en.200k.058145", "hw": "kartiks", "pos": "noun", "ipa": "/ˈkɑːrtɪks/", "vi": "tháng Kartik trong lịch tôn giáo Ấn"},
    {"id": "lex.en.200k.058146", "hw": "laconias", "pos": "noun", "ipa": "/ləˈkoʊniəz/", "vi": "vùng đất cổ Laconia của Sparta"},
    {"id": "lex.en.200k.058147", "hw": "lafittes", "pos": "noun", "ipa": "/ləˈfiːts/", "vi": "hải tặc danh tiếng Jean Lafitte"},
    {"id": "lex.en.200k.058148", "hw": "lorres", "pos": "noun", "ipa": "/ˈlɔːriz/", "vi": "nam diễn viên điện ảnh Peter Lorre"},
    {"id": "lex.en.200k.058149", "hw": "luddites", "pos": "noun", "ipa": "/ˈlʌdaɪts/", "vi": "kẻ bài xích phản đối công nghệ mới"},
    {"id": "lex.en.200k.058150", "hw": "magrittes", "pos": "noun", "ipa": "/məˈɡriːts/", "vi": "danh họa siêu thực René Magritte"},
    {"id": "lex.en.200k.058151", "hw": "menservants", "pos": "noun", "ipa": "/ˈmɛnsɜːrvənts/", "vi": "những người gia nhân đầy tớ nam"},
    {"id": "lex.en.200k.058152", "hw": "mesolithics", "pos": "noun", "ipa": "/ˌmɛzəˈlɪθɪks/", "vi": "thời kỳ văn hóa đồ đá giữa"},
    {"id": "lex.en.200k.058153", "hw": "modelers", "pos": "noun", "ipa": "/ˈmɑːdəlɚz/", "vi": "người làm mô hình; thợ đắp mẫu"},
    {"id": "lex.en.200k.058154", "hw": "moldavias", "pos": "noun", "ipa": "/mɑːlˈdeɪviəz/", "vi": "vương quốc lịch sử Moldavia Đông Âu"},
    {"id": "lex.en.200k.058155", "hw": "mutagens", "pos": "noun", "ipa": "/ˈmjuːtədʒənz/", "vi": "tác nhân sinh đột biến di truyền"},
    {"id": "lex.en.200k.058156", "hw": "neurophysiologies", "pos": "noun", "ipa": "/ˌnʊəroʊˌfɪziˈɑːlədʒiz/", "vi": "môn sinh lý học thần kinh"},
    {"id": "lex.en.200k.058157", "hw": "octets", "pos": "noun", "ipa": "/ɑːkˈtɛts/", "vi": "bộ tám; nhóm tám người; nhóm 8 bit"},
    {"id": "lex.en.200k.058158", "hw": "otherworlds", "pos": "noun", "ipa": "/ˈʌðɚwɜːrldz/", "vi": "cõi giới khác; thế giới bên kia"},
    {"id": "lex.en.200k.058159", "hw": "petroniuses", "pos": "noun", "ipa": "/pɪˈtroʊniəsɪz/", "vi": "nhà văn châm biếm La Mã Petronius"},
    {"id": "lex.en.200k.058160", "hw": "pluralists", "pos": "noun", "ipa": "/ˈplʊrəlɪsts/", "vi": "người theo chủ nghĩa đa nguyên"},
    {"id": "lex.en.200k.058161", "hw": "plutocracies", "pos": "noun", "ipa": "/pluːˈtɑːkrəsiz/", "vi": "chế độ chính trị tài phiệt cai trị"},
    {"id": "lex.en.200k.058162", "hw": "qaddafis", "pos": "noun", "ipa": "/ɡəˈdɑːfiz/", "vi": "nhà lãnh đạo Libya Muammar Gaddafi"},
    {"id": "lex.en.200k.058163", "hw": "qcds", "pos": "noun", "ipa": "/ˌkjuː.siːˈdiːz/", "vi": "thuyết sắc động lực học lượng tử"},
    {"id": "lex.en.200k.058164", "hw": "racoons", "pos": "noun", "ipa": "/ræˈkuːnz/", "vi": "các con gấu mèo Bắc Mỹ đuôi khoang"},
    {"id": "lex.en.200k.058165", "hw": "readjustments", "pos": "noun", "ipa": "/ˌriːəˈdʒʌstmənts/", "vi": "sự điều chỉnh thích nghi lại"},
    {"id": "lex.en.200k.058166", "hw": "recirculations", "pos": "noun", "ipa": "/ˌriːˌsɜːrkjʊˈleɪʃənz/", "vi": "sự tuần hoàn lưu thông khép kín"},
    {"id": "lex.en.200k.058167", "hw": "rectos", "pos": "noun", "ipa": "/ˈrɛktoʊz/", "vi": "trang bên phải sách; trang lẻ"},
    {"id": "lex.en.200k.058168", "hw": "repellants", "pos": "noun", "ipa": "/rɪˈpɛlənts/", "vi": "chất chống thấm; chất xua côn trùng"},
    {"id": "lex.en.200k.058169", "hw": "retells", "pos": "verb", "ipa": "/riːˈtɛlz/", "vi": "kể lại; thuật lại câu chuyện"},
    {"id": "lex.en.200k.058170", "hw": "rhds", "pos": "noun", "ipa": "/ˌɑːr.eɪtʃˈdiːz/", "vi": "bệnh thấp tim; nhóm máu RhD"},
    {"id": "lex.en.200k.058171", "hw": "sailfishes", "pos": "noun", "ipa": "/ˈseɪlfɪʃɪz/", "vi": "loài cá buồm biển bơi cực nhanh"},
    {"id": "lex.en.200k.058172", "hw": "sapirs", "pos": "noun", "ipa": "/səˈpɪərz/", "vi": "nhà ngôn ngữ học Edward Sapir"},
    {"id": "lex.en.200k.058173", "hw": "selznicks", "pos": "noun", "ipa": "/ˈsɛlznɪks/", "vi": "nhà sản xuất phim David O. Selznick"},
    {"id": "lex.en.200k.058174", "hw": "semarangs", "pos": "noun", "ipa": "/səmˈɑːrɑːŋz/", "vi": "thành phố cảng Semarang ở Indonesia"},
    {"id": "lex.en.200k.058175", "hw": "skagits", "pos": "noun", "ipa": "/ˈskædʒɪts/", "vi": "bộ tộc Skagit ở bang Washington"},
    {"id": "lex.en.200k.058176", "hw": "smarmier", "pos": "adj", "ipa": "/ˈsmɑːrmiər/", "vi": "nịnh nọt xun xoe trơn tráo hơn"},
    {"id": "lex.en.200k.058177", "hw": "smarmiest", "pos": "adj", "ipa": "/ˈsmɑːrmiɪst/", "vi": "nịnh nọt xun xoe trơn tráo nhất"},
    {"id": "lex.en.200k.058178", "hw": "smuttier", "pos": "adj", "ipa": "/ˈsmʌtiər/", "vi": "tục tĩu dâm ô hơn; nhọ nhem hơn"},
    {"id": "lex.en.200k.058179", "hw": "smuttiest", "pos": "adj", "ipa": "/ˈsmʌtiɪst/", "vi": "tục tĩu dâm ô nhất; nhọ nhem nhất"},
    {"id": "lex.en.200k.058180", "hw": "sunbathed", "pos": "verb", "ipa": "/ˈsʌnbeɪðd/", "vi": "đã phơi mình tắm nắng ngoài trời"},
    {"id": "lex.en.200k.058181", "hw": "sunbathes", "pos": "verb", "ipa": "/ˈsʌnbeɪðz/", "vi": "tắm nắng; phơi mình dưới ánh nắng"},
    {"id": "lex.en.200k.058182", "hw": "surinams", "pos": "noun", "ipa": "/ˌsʊrɪˈnɑːmz/", "vi": "quốc gia Nam Mỹ Suriname"},
    {"id": "lex.en.200k.058183", "hw": "talleyrands", "pos": "noun", "ipa": "/ˈtælirændz/", "vi": "nhà ngoại giao Pháp Talleyrand"},
    {"id": "lex.en.200k.058184", "hw": "tautologies", "pos": "noun", "ipa": "/tɔːˈtɑːlədʒiz/", "vi": "lỗi lặp ý thừa; mệnh đề hằng đúng"},
    {"id": "lex.en.200k.058185", "hw": "taxidermists", "pos": "noun", "ipa": "/ˈtæksɪdɜːrmɪsts/", "vi": "những người thợ nhồi xác thú bông"},
    {"id": "lex.en.200k.058186", "hw": "throatier", "pos": "adj", "ipa": "/ˈθroʊtiər/", "vi": "khàn ồm ồm hơn; trầm khàn hơn"},
    {"id": "lex.en.200k.058187", "hw": "throatiest", "pos": "adj", "ipa": "/ˈθroʊtiɪst/", "vi": "nghẹn ứ trong họng nhất; khàn nhất"},
    {"id": "lex.en.200k.058188", "hw": "thrombocytopenias", "pos": "noun", "ipa": "/ˌθrɑːmboʊˌsaɪtoʊˈpiːniəz/", "vi": "chứng bệnh giảm tiểu cầu trong máu"},
    {"id": "lex.en.200k.058189", "hw": "transcriptases", "pos": "noun", "ipa": "/trænˈskrɪpteɪsɪz/", "vi": "các enzym phiên mã sao chép mARN"},
    {"id": "lex.en.200k.058190", "hw": "ucas", "pos": "noun", "ipa": "/ˈjuːkæsɪz/", "vi": "tuyển sinh đại học UCAS của Anh"},
    {"id": "lex.en.200k.058191", "hw": "varicellas", "pos": "noun", "ipa": "/ˌværɪˈsɛləz/", "vi": "bệnh thủy đậu do nhiễm vi-rút"},
    {"id": "lex.en.200k.058192", "hw": "weatherproofed", "pos": "verb", "ipa": "/ˈwɛðɚpruːft/", "vi": "đã xử lý chống chịu thời tiết"},
    {"id": "lex.en.200k.058193", "hw": "weatherproofing", "pos": "verb", "ipa": "/ˈwɛðɚpruːfɪŋ/", "vi": "đang gia cố chống chịu thời tiết"},
    {"id": "lex.en.200k.058194", "hw": "weatherproofs", "pos": "verb", "ipa": "/ˈwɛðɚpruːfs/", "vi": "xử lý giúp chống chịu thời tiết"},
    {"id": "lex.en.200k.058195", "hw": "whitsundays", "pos": "noun", "ipa": "/ˈwɪtsəndeɪz/", "vi": "ngày lễ Chúa Thánh Thần Hiện Xuống"},
    {"id": "lex.en.200k.058196", "hw": "wnws", "pos": "noun", "ipa": "/ˌdʌbəl.juː.ɛnˈdʌbəl.juːz/", "vi": "hướng tây-tây bắc trên hải đồ"},
    {"id": "lex.en.200k.058197", "hw": "woodhulls", "pos": "noun", "ipa": "/ˈwʊdhʌlz/", "vi": "nhà nữ quyền Mỹ Victoria Woodhull"},
    {"id": "lex.en.200k.058198", "hw": "wordsmiths", "pos": "noun", "ipa": "/ˈwɜːrdsmɪθs/", "vi": "những bậc thầy ngôn từ điêu luyện"},
    {"id": "lex.en.200k.058199", "hw": "yugoslavians", "pos": "noun", "ipa": "/ˌjuːɡoʊˈslɑːviənz/", "vi": "người dân thuộc Liên bang Nam Tư"},
    {"id": "lex.en.200k.058200", "hw": "aedes aegypti", "pos": "phrase", "ipa": "", "vi": "loài muỗi vằn truyền sốt xuất huyết"},
    {"id": "lex.en.200k.058201", "hw": "amitriptyline hydrochloride", "pos": "phrase", "ipa": "", "vi": "thuốc chống trầm cảm amitriptylin"}
]

# Validation
with open('scratch/b32_r07_raw_p2.json') as f:
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
final_p2 = []
for r, raw_r in zip(records, raw):
    item = dict(raw_r)
    item['pos'] = r['pos']
    item['ipa'] = r['ipa']
    item['vi'] = r['vi']
    item['status'] = 'reviewed'
    final_p2.append(item)

with open('scratch/b32_r07_p2.json', 'w') as f:
    json.dump(final_p2, f, ensure_ascii=False, indent=2)
print("Part 2 validated and written successfully.")
