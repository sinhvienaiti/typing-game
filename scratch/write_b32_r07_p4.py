import json

records = [
    {"id": "lex.en.200k.058302", "hw": "bolingbrokes", "pos": "noun", "ipa": "/ˈbɑːlɪŋbrʊks/", "vi": "vua Henry IV Bolingbroke nước Anh"},
    {"id": "lex.en.200k.058303", "hw": "bycatches", "pos": "noun", "ipa": "/ˈbaɪkætʃɪz/", "vi": "sản phẩm đánh bắt phụ ngoài ý muốn"},
    {"id": "lex.en.200k.058304", "hw": "byways", "pos": "noun", "ipa": "/ˈbaɪweɪz/", "vi": "đường nhánh phụ; ngõ ngách vắng vẻ"},
    {"id": "lex.en.200k.058305", "hw": "carmakers", "pos": "noun", "ipa": "/ˈkɑːrmeɪkɚz/", "vi": "các hãng sản xuất chế tạo ô tô"},
    {"id": "lex.en.200k.058306", "hw": "cassocks", "pos": "noun", "ipa": "/ˈkæsəks/", "vi": "áo chùng đen của giáo sĩ tu sĩ"},
    {"id": "lex.en.200k.058307", "hw": "chapeaus", "pos": "noun", "ipa": "/ʃæˈpoʊz/", "vi": "chiếc mũ đội đầu quý phái"},
    {"id": "lex.en.200k.058308", "hw": "chapeaux", "pos": "noun", "ipa": "/ʃæˈpoʊz/", "vi": "các kiểu mũ nón thời trang"},
    {"id": "lex.en.200k.058309", "hw": "chirpier", "pos": "adj", "ipa": "/ˈtʃɜːrpiər/", "vi": "líu lo vui vẻ hơn; tươi tỉnh hơn"},
    {"id": "lex.en.200k.058310", "hw": "chirpiest", "pos": "adj", "ipa": "/ˈtʃɜːrpiɪst/", "vi": "líu lo vui vẻ nhất; tươi tỉnh nhất"},
    {"id": "lex.en.200k.058311", "hw": "clunked", "pos": "verb", "ipa": "/klʌŋkt/", "vi": "đã va chạm kêu lộc cộc cồng cộc"},
    {"id": "lex.en.200k.058312", "hw": "clunks", "pos": "noun", "ipa": "/klʌŋks/", "vi": "tiếng kim loại va chạm lộc cộc"},
    {"id": "lex.en.200k.058313", "hw": "corneilles", "pos": "noun", "ipa": "/kɔːrˈneɪz/", "vi": "kịch tác gia Pierre Corneille Pháp"},
    {"id": "lex.en.200k.058314", "hw": "curtailments", "pos": "noun", "ipa": "/kɚˈteɪlmənts/", "vi": "sự cắt bớt hạn chế quyền lợi"},
    {"id": "lex.en.200k.058315", "hw": "deaneries", "pos": "noun", "ipa": "/ˈdiːnəriz/", "vi": "giáo hạt giáo phận; dinh trưởng hạt"},
    {"id": "lex.en.200k.058316", "hw": "effendis", "pos": "noun", "ipa": "/ɛˈfɛndiz/", "vi": "danh xưng tôn kính ngài ở Thổ"},
    {"id": "lex.en.200k.058317", "hw": "eisteddfodau", "pos": "noun", "ipa": "/eɪstɛðˈvɔːdaɪ/", "vi": "đại hội thi ca âm nhạc xứ Wales"},
    {"id": "lex.en.200k.058318", "hw": "eisteddfods", "pos": "noun", "ipa": "/eɪstɛðˈvɔːdz/", "vi": "ngày hội nghệ thuật thi ca xứ Wales"},
    {"id": "lex.en.200k.058319", "hw": "electromagnets", "pos": "noun", "ipa": "/ɪˌlɛktroʊˈmæɡnəts/", "vi": "các cuộn nam châm điện cảm ứng"},
    {"id": "lex.en.200k.058320", "hw": "europols", "pos": "noun", "ipa": "/ˈjʊrəpɑːlz/", "vi": "cơ quan cảnh sát châu Âu Europol"},
    {"id": "lex.en.200k.058321", "hw": "exhorted", "pos": "verb", "ipa": "/ɪɡˈzɔːrtɪd/", "vi": "đã khuyên can tha thiết; cổ vũ"},
    {"id": "lex.en.200k.058322", "hw": "exhorting", "pos": "verb", "ipa": "/ɪɡˈzɔːrtɪŋ/", "vi": "đang khuyên nhủ tha thiết cổ vũ"},
    {"id": "lex.en.200k.058323", "hw": "festschriften", "pos": "noun", "ipa": "/ˈfɛstʃrɪftən/", "vi": "tập kỷ yếu mừng thọ học giả"},
    {"id": "lex.en.200k.058324", "hw": "festschrifts", "pos": "noun", "ipa": "/ˈfɛstʃrɪfts/", "vi": "các tập kỷ yếu học thuật tri ân"},
    {"id": "lex.en.200k.058325", "hw": "fronds", "pos": "noun", "ipa": "/frɑːndz/", "vi": "lá cây dương xỉ cọ xẻ phiến lớn"},
    {"id": "lex.en.200k.058326", "hw": "funiculars", "pos": "noun", "ipa": "/fjuːˈnɪkjʊlɚz/", "vi": "đường sắt dây cáp kéo sườn núi"},
    {"id": "lex.en.200k.058327", "hw": "gallianos", "pos": "noun", "ipa": "/ɡæliˈɑːnoʊz/", "vi": "rượu mùi thảo mộc Galliano vàng"},
    {"id": "lex.en.200k.058328", "hw": "gielguds", "pos": "noun", "ipa": "/ˈɡiːlɡʊdz/", "vi": "nam diễn viên kịch John Gielgud"},
    {"id": "lex.en.200k.058329", "hw": "grantors", "pos": "noun", "ipa": "/ˈɡræntɚz/", "vi": "người chuyển nhượng tài sản quyền"},
    {"id": "lex.en.200k.058330", "hw": "groundskeepers", "pos": "noun", "ipa": "/ˈɡraʊndskiːpɚz/", "vi": "người coi sóc khuôn viên sân cỏ"},
    {"id": "lex.en.200k.058331", "hw": "guaranis", "pos": "noun", "ipa": "/ˌɡwɑːrəˈniːz/", "vi": "đồng tiền guarani; người Guarani"},
    {"id": "lex.en.200k.058332", "hw": "hadjis", "pos": "noun", "ipa": "/ˈhædʒiz/", "vi": "những tín đồ hành hương tới Mecca"},
    {"id": "lex.en.200k.058333", "hw": "heterocyclics", "pos": "noun", "ipa": "/ˌhɛtəroʊˈsaɪklɪks/", "vi": "các hợp chất vòng dị tố hữu cơ"},
    {"id": "lex.en.200k.058334", "hw": "hijinkses", "pos": "noun", "ipa": "/ˈhaɪdʒɪŋksɪz/", "vi": "trò đùa tinh quái tiệc tùng ồn ào"},
    {"id": "lex.en.200k.058335", "hw": "intis", "pos": "noun", "ipa": "/ˈɪntiz/", "vi": "đồng tiền inti trước đây của Peru"},
    {"id": "lex.en.200k.058336", "hw": "irenaeuses", "pos": "noun", "ipa": "/aɪrəˈniːəsɪz/", "vi": "Thánh giám mục Irenaeus thành Lyon"},
    {"id": "lex.en.200k.058337", "hw": "jaffars", "pos": "noun", "ipa": "/ˈdʒæfɑːrz/", "vi": "các nhân vật tể tướng tên Ja'far"},
    {"id": "lex.en.200k.058338", "hw": "jocastas", "pos": "noun", "ipa": "/dʒoʊˈkæstəz/", "vi": "hoàng hậu Jocasta mẹ của Oedipus"},
    {"id": "lex.en.200k.058339", "hw": "lamarcks", "pos": "noun", "ipa": "/ləˈmɑːrks/", "vi": "nhà tiến hóa học Jean Lamarck"},
    {"id": "lex.en.200k.058340", "hw": "ligers", "pos": "noun", "ipa": "/ˈlaɪɡɚz/", "vi": "con lai sư tử đực và hổ cái liger"},
    {"id": "lex.en.200k.058341", "hw": "lippmanns", "pos": "noun", "ipa": "/ˈlɪpmənz/", "vi": "nhà báo bình luận Walter Lippmann"},
    {"id": "lex.en.200k.058342", "hw": "lubas", "pos": "noun", "ipa": "/ˈluːbəz/", "vi": "người Luba bản địa miền trung Phi"},
    {"id": "lex.en.200k.058343", "hw": "lugosis", "pos": "noun", "ipa": "/lʊˈɡoʊsiz/", "vi": "diễn viên Dracula Bela Lugosi"},
    {"id": "lex.en.200k.058344", "hw": "lysols", "pos": "noun", "ipa": "/ˈlaɪsɔːlz/", "vi": "dung dịch thuốc tẩy sát trùng Lysol"},
    {"id": "lex.en.200k.058345", "hw": "madrasas", "pos": "noun", "ipa": "/məˈdræsəz/", "vi": "trường dòng tôn giáo Hồi giáo"},
    {"id": "lex.en.200k.058346", "hw": "mallees", "pos": "noun", "ipa": "/ˈmæliːz/", "vi": "bụi cây bạch đàn lùn nước Úc"},
    {"id": "lex.en.200k.058347", "hw": "manises", "pos": "noun", "ipa": "/ˈmænɪsɪz/", "vi": "loài tê tê vảy thuộc chi Manis"},
    {"id": "lex.en.200k.058348", "hw": "marmaras", "pos": "noun", "ipa": "/ˈmɑːrmərəz/", "vi": "vùng biển nội địa hẹp Marmara Thổ"},
    {"id": "lex.en.200k.058349", "hw": "maypoles", "pos": "noun", "ipa": "/ˈmeɪpoʊlz/", "vi": "cột gỗ lễ hội tháng Năm Maypole"},
    {"id": "lex.en.200k.058350", "hw": "medevacs", "pos": "noun", "ipa": "/ˈmɛdɪvæks/", "vi": "chuyến trực thăng sơ tán cứu thương"},
    {"id": "lex.en.200k.058351", "hw": "megabytes", "pos": "noun", "ipa": "/ˈmɛɡəbaɪts/", "vi": "đơn vị đo dung lượng mê-ga-bai MB"},
    {"id": "lex.en.200k.058352", "hw": "melchiors", "pos": "noun", "ipa": "/ˈmɛlkiɔːrz/", "vi": "vua thông thái Melchior Giáng sinh"},
    {"id": "lex.en.200k.058353", "hw": "mephistopheleses", "pos": "noun", "ipa": "/ˌmɛfɪˈstɑːfəliːzɪz/", "vi": "ác quỷ cám dỗ Mephistopheles kịch"},
    {"id": "lex.en.200k.058354", "hw": "middens", "pos": "noun", "ipa": "/ˈmɪdənz/", "vi": "đống rác vỏ sò thời tiền sử cổ"},
    {"id": "lex.en.200k.058355", "hw": "morphogeneses", "pos": "noun", "ipa": "/ˌmɔːrfoʊˈdʒɛnəsɪsɪz/", "vi": "quá trình sinh hình thái sinh học"},
    {"id": "lex.en.200k.058356", "hw": "mudras", "pos": "noun", "ipa": "/ˈmuːdrəz/", "vi": "thủ ấn biểu tượng tay trong yoga"},
    {"id": "lex.en.200k.058357", "hw": "munchausens", "pos": "noun", "ipa": "/ˈmʌntʃaʊzənz/", "vi": "bá tước nói khoác Münchhausen"},
    {"id": "lex.en.200k.058358", "hw": "murks", "pos": "noun", "ipa": "/mɜːrks/", "vi": "bóng đêm dày đặc; màn sương mù mịt"},
    {"id": "lex.en.200k.058359", "hw": "nebos", "pos": "noun", "ipa": "/ˈniːboʊz/", "vi": "núi Nebo nơi Moses nhìn đất hứa"},
    {"id": "lex.en.200k.058360", "hw": "nonresidents", "pos": "noun", "ipa": "/nɑːnˈrɛzɪdənts/", "vi": "người không có hộ khẩu thường trú"},
    {"id": "lex.en.200k.058361", "hw": "nonsteroidals", "pos": "noun", "ipa": "/ˌnɑːnstəˈrɔɪdəlz/", "vi": "thuốc giảm đau kháng viêm NSAID"},
    {"id": "lex.en.200k.058362", "hw": "nros", "pos": "noun", "ipa": "/ˌɛn.ɑːrˈoʊz/", "vi": "văn phòng trinh sát vũ trụ NRO Mỹ"},
    {"id": "lex.en.200k.058363", "hw": "omnivores", "pos": "noun", "ipa": "/ˈɑːmnɪvɔːrz/", "vi": "các loài động vật ăn tạp đa dạng"},
    {"id": "lex.en.200k.058364", "hw": "orpingtons", "pos": "noun", "ipa": "/ˈɔːrpɪŋtənz/", "vi": "giống gà thả vườn béo Orpington"},
    {"id": "lex.en.200k.058365", "hw": "overspending", "pos": "verb", "ipa": "/ˌoʊvɚˈspɛndɪŋ/", "vi": "đang chi tiêu quá tay; lãng phí"},
    {"id": "lex.en.200k.058366", "hw": "overspends", "pos": "verb", "ipa": "/ˌoʊvɚˈspɛndz/", "vi": "chi tiêu quá tay; tiêu vượt mức"},
    {"id": "lex.en.200k.058367", "hw": "pahangs", "pos": "noun", "ipa": "/pəˈhɑːŋz/", "vi": "tiểu bang lớn Pahang ở Malaysia"},
    {"id": "lex.en.200k.058368", "hw": "parthians", "pos": "noun", "ipa": "/ˈpɑːrθiənz/", "vi": "người dân đế chế Parthia Ba Tư cổ"},
    {"id": "lex.en.200k.058369", "hw": "pinners", "pos": "noun", "ipa": "/ˈpɪnɚz/", "vi": "người gài ghim; mũ vải gài ghim"},
    {"id": "lex.en.200k.058370", "hw": "polluters", "pos": "noun", "ipa": "/pəˈluːtɚz/", "vi": "kẻ gây ô nhiễm hủy hoại môi trường"},
    {"id": "lex.en.200k.058371", "hw": "prepaying", "pos": "verb", "ipa": "/ˌpriːˈpeɪɪŋ/", "vi": "đang thanh toán tiền trả trước"},
    {"id": "lex.en.200k.058372", "hw": "prepays", "pos": "verb", "ipa": "/ˌpriːˈpeɪz/", "vi": "thanh toán trả trước cho dịch vụ"},
    {"id": "lex.en.200k.058373", "hw": "pudges", "pos": "noun", "ipa": "/ˈpʌdʒɪz/", "vi": "những người lùn mập mạp béo tròn"},
    {"id": "lex.en.200k.058374", "hw": "pulpier", "pos": "adj", "ipa": "/ˈpʌlpiər/", "vi": "nhiều múi thịt thịt quả nhão hơn"},
    {"id": "lex.en.200k.058375", "hw": "pulpiest", "pos": "adj", "ipa": "/ˈpʌlpiɪst/", "vi": "nhiều múi thịt thịt quả nhão nhất"},
    {"id": "lex.en.200k.058376", "hw": "pulsations", "pos": "noun", "ipa": "/pʌlˈseɪʃənz/", "vi": "nhịp đập mạch máu; dao động mạch"},
    {"id": "lex.en.200k.058377", "hw": "rachmaninoffs", "pos": "noun", "ipa": "/rɑːkˈmɑːnɪnɔːfs/", "vi": "nhạc sĩ vĩ đại Sergei Rachmaninoff"},
    {"id": "lex.en.200k.058378", "hw": "rappelled", "pos": "verb", "ipa": "/rəˈpɛld/", "vi": "đã đu dây tụt dốc vách núi đứng"},
    {"id": "lex.en.200k.058379", "hw": "rappelling", "pos": "verb", "ipa": "/rəˈpɛlɪŋ/", "vi": "kỹ thuật đu dây tụt dốc vách đá"},
    {"id": "lex.en.200k.058380", "hw": "rappels", "pos": "noun", "ipa": "/rəˈpɛlz/", "vi": "những lần đu dây tụt vách đá"},
    {"id": "lex.en.200k.058381", "hw": "riels", "pos": "noun", "ipa": "/riːˈɛlz/", "vi": "đồng tiền tệ riel của Campuchia"},
    {"id": "lex.en.200k.058382", "hw": "ritzier", "pos": "adj", "ipa": "/ˈrɪtsiər/", "vi": "xa hoa lộng lẫy sang trọng hơn"},
    {"id": "lex.en.200k.058383", "hw": "ritziest", "pos": "adj", "ipa": "/ˈrɪtsiɪst/", "vi": "xa hoa lộng lẫy sang trọng nhất"},
    {"id": "lex.en.200k.058384", "hw": "rockfishes", "pos": "noun", "ipa": "/ˈrɑːkfɪʃɪz/", "vi": "cá sống rạn đá san hô biển sâu"},
    {"id": "lex.en.200k.058385", "hw": "satyagrahas", "pos": "noun", "ipa": "/ˌsʌtiˈɑːɡrəhəz/", "vi": "phong trào bất bạo động Satyagraha"},
    {"id": "lex.en.200k.058386", "hw": "scapulars", "pos": "noun", "ipa": "/ˈskæpjʊlɚz/", "vi": "áo vai tu sĩ; áo Đức Bà hộ mạng"},
    {"id": "lex.en.200k.058387", "hw": "sigints", "pos": "noun", "ipa": "/ˈsɪɡɪnts/", "vi": "ngành tình báo tín hiệu điện tử"},
    {"id": "lex.en.200k.058388", "hw": "silversmiths", "pos": "noun", "ipa": "/ˈsɪlvɚsmɪθs/", "vi": "thợ chế tác kim hoàn đồ bạc"},
    {"id": "lex.en.200k.058389", "hw": "slathered", "pos": "verb", "ipa": "/ˈslæðɚd/", "vi": "đã phết trét bôi một lớp thật dày"},
    {"id": "lex.en.200k.058390", "hw": "socialisations", "pos": "noun", "ipa": "/ˌsoʊʃəlaɪˈzeɪʃənz/", "vi": "quá trình xã hội hóa con người"},
    {"id": "lex.en.200k.058391", "hw": "solvays", "pos": "noun", "ipa": "/ˈsɑːlveɪz/", "vi": "phương pháp Solvay sản xuất soda"},
    {"id": "lex.en.200k.058392", "hw": "southeys", "pos": "noun", "ipa": "/ˈsaʊðiz/", "vi": "nhà thơ nước Anh Robert Southey"},
    {"id": "lex.en.200k.058393", "hw": "spendthrifts", "pos": "noun", "ipa": "/ˈspɛndθrɪfts/", "vi": "những kẻ tiêu xài hoang phí vô độ"},
    {"id": "lex.en.200k.058394", "hw": "substrasta", "pos": "noun", "ipa": "/sʌbˈstreɪtə/", "vi": "lớp nền móng cơ sở bên dưới"},
    {"id": "lex.en.200k.058395", "hw": "thalassemias", "pos": "noun", "ipa": "/ˌθæləˈsiːmiəz/", "vi": "bệnh tan máu bẩm sinh di truyền"},
    {"id": "lex.en.200k.058396", "hw": "timberlines", "pos": "noun", "ipa": "/ˈtɪmbɚlaɪnz/", "vi": "ranh giới độ cao cây rừng mọc"},
    {"id": "lex.en.200k.058397", "hw": "tomfooleries", "pos": "noun", "ipa": "/tɑːmˈfuːləriz/", "vi": "những trò hề nghịch ngợm ngớ ngẩn"},
    {"id": "lex.en.200k.058398", "hw": "trefoils", "pos": "noun", "ipa": "/ˈtriːfɔɪlz/", "vi": "cỏ ba lá; họa tiết cánh ba hoa"},
    {"id": "lex.en.200k.058399", "hw": "ultrasonographies", "pos": "noun", "ipa": "/ˌʌltrəsəˈnɑːɡrəfiz/", "vi": "kỹ thuật thăm dò siêu âm y khoa"},
    {"id": "lex.en.200k.058400", "hw": "vampirisms", "pos": "noun", "ipa": "/ˈvæmpaɪərɪzəmz/", "vi": "hiện tượng hút máu ma cà rồng"},
    {"id": "lex.en.200k.058401", "hw": "varas", "pos": "noun", "ipa": "/ˈvɑːrəz/", "vi": "đơn vị đo chiều dài thước vara"}
]

# Validation
with open('scratch/b32_r07_raw_p4.json') as f:
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
final_p4 = []
for r, raw_r in zip(records, raw):
    item = dict(raw_r)
    item['pos'] = r['pos']
    item['ipa'] = r['ipa']
    item['vi'] = r['vi']
    item['status'] = 'reviewed'
    final_p4.append(item)

with open('scratch/b32_r07_p4.json', 'w') as f:
    json.dump(final_p4, f, ensure_ascii=False, indent=2)
print("Part 4 validated and written successfully.")
