import json

records = [
    {"id": "lex.en.200k.057902", "hw": "polychroming", "pos": "verb", "ipa": "/ˈpɑːlikroʊmɪŋ/", "vi": "đang tô vẽ trang trí nhiều màu"},
    {"id": "lex.en.200k.057903", "hw": "poussins", "pos": "noun", "ipa": "/puːˈsæ̃z/", "vi": "danh họa Nicolas Poussin; gà giò"},
    {"id": "lex.en.200k.057904", "hw": "privets", "pos": "noun", "ipa": "/ˈprɪvɪts/", "vi": "các bụi cây thủy lạp viền rào"},
    {"id": "lex.en.200k.057905", "hw": "putzes", "pos": "noun", "ipa": "/ˈpʌtsɪz/", "vi": "những kẻ đần độn ngớ ngẩn vô dụng"},
    {"id": "lex.en.200k.057906", "hw": "pyrrhics", "pos": "noun", "ipa": "/ˈpɪrɪks/", "vi": "các bước nhịp đôi ngắn trong thơ"},
    {"id": "lex.en.200k.057907", "hw": "rajabs", "pos": "noun", "ipa": "/rəˈdʒɑːbz/", "vi": "tháng Rajab trong lịch Hồi giáo"},
    {"id": "lex.en.200k.057908", "hw": "reactants", "pos": "noun", "ipa": "/riˈæktənts/", "vi": "các chất tham gia phản ứng hóa học"},
    {"id": "lex.en.200k.057909", "hw": "redoubles", "pos": "verb", "ipa": "/riːˈdʌbəlz/", "vi": "tăng gấp đôi; nhân lên gấp bội"},
    {"id": "lex.en.200k.057910", "hw": "redoubling", "pos": "verb", "ipa": "/riːˈdʌbəlɪŋ/", "vi": "đang tăng gấp bội; tăng gấp đôi"},
    {"id": "lex.en.200k.057911", "hw": "reinterpreted", "pos": "verb", "ipa": "/ˌriːɪnˈtɜːrprətɪd/", "vi": "đã tái diễn giải; đã hiểu lại"},
    {"id": "lex.en.200k.057912", "hw": "reinterpreting", "pos": "verb", "ipa": "/ˌriːɪnˈtɜːrprətɪŋ/", "vi": "đang tái diễn giải theo cách mới"},
    {"id": "lex.en.200k.057913", "hw": "reinterprets", "pos": "verb", "ipa": "/ˌriːɪnˈtɜːrprəts/", "vi": "tái diễn giải; hiểu theo cách mới"},
    {"id": "lex.en.200k.057914", "hw": "relaxants", "pos": "noun", "ipa": "/rɪˈlæksənts/", "vi": "các loại thuốc làm giãn cơ bắp"},
    {"id": "lex.en.200k.057915", "hw": "reneged", "pos": "verb", "ipa": "/rɪˈnɪɡd/", "vi": "đã nuốt lời; đã bội ước bội hứa"},
    {"id": "lex.en.200k.057916", "hw": "reneges", "pos": "verb", "ipa": "/rɪˈnɪɡz/", "vi": "nuốt lời; bội ước không giữ lời"},
    {"id": "lex.en.200k.057917", "hw": "reneging", "pos": "verb", "ipa": "/rɪˈnɪɡɪŋ/", "vi": "đang nuốt lời; đang bội hứa"},
    {"id": "lex.en.200k.057918", "hw": "rheimses", "pos": "noun", "ipa": "/ræ̃zɪz/", "vi": "thành phố Reims lịch sử nước Pháp"},
    {"id": "lex.en.200k.057919", "hw": "romanoffs", "pos": "noun", "ipa": "/ˈroʊmənɔːfs/", "vi": "các thành viên hoàng tộc Romanov"},
    {"id": "lex.en.200k.057920", "hw": "roomfuls", "pos": "noun", "ipa": "/ˈruːmfʊlz/", "vi": "lượng người chứa đầy một căn phòng"},
    {"id": "lex.en.200k.057921", "hw": "rotaviruses", "pos": "noun", "ipa": "/ˈroʊtəvaɪrəsɪz/", "vi": "vi-rút rota gây tiêu chảy trẻ nhỏ"},
    {"id": "lex.en.200k.057922", "hw": "sacristies", "pos": "noun", "ipa": "/ˈsækrɪstiz/", "vi": "các phòng giữ thánh tích đồ lễ"},
    {"id": "lex.en.200k.057923", "hw": "seigneurs", "pos": "noun", "ipa": "/seɪnˈjɜːrz/", "vi": "lãnh chúa cai quản thái ấp"},
    {"id": "lex.en.200k.057924", "hw": "singalongs", "pos": "noun", "ipa": "/ˈsɪŋəlɔːŋz/", "vi": "buổi hòa ca hát tập thể cùng nhau"},
    {"id": "lex.en.200k.057925", "hw": "slappers", "pos": "noun", "ipa": "/ˈslæpɚz/", "vi": "kẻ tát tay; người phụ nữ buông thả"},
    {"id": "lex.en.200k.057926", "hw": "slowpokes", "pos": "noun", "ipa": "/ˈsloʊpoʊks/", "vi": "những kẻ chậm chạp lề mề rề rà"},
    {"id": "lex.en.200k.057927", "hw": "spammers", "pos": "noun", "ipa": "/ˈspæmɚz/", "vi": "những kẻ chuyên gửi tin nhắn rác"},
    {"id": "lex.en.200k.057928", "hw": "sphagnums", "pos": "noun", "ipa": "/ˈsfæɡnəmz/", "vi": "rêu than bùn chi Sphagnum đầm lầy"},
    {"id": "lex.en.200k.057929", "hw": "spinnakers", "pos": "noun", "ipa": "/ˈspɪnəkɚz/", "vi": "cánh buồm phồng mũi thuyền buồm"},
    {"id": "lex.en.200k.057930", "hw": "sportswriters", "pos": "noun", "ipa": "/ˈspɔːrtsraɪtɚz/", "vi": "các nhà báo phóng viên thể thao"},
    {"id": "lex.en.200k.057931", "hw": "stracheys", "pos": "noun", "ipa": "/ˈstreɪtʃiz/", "vi": "nhà văn Anh Lytton Strachey"},
    {"id": "lex.en.200k.057932", "hw": "stromas", "pos": "noun", "ipa": "/ˈstroʊməz/", "vi": "chất nền lục lạp; mô liên kết đệm"},
    {"id": "lex.en.200k.057933", "hw": "superegos", "pos": "noun", "ipa": "/ˌsuːpɚˈiːɡoʊz/", "vi": "các siêu bản ngã trong phân tâm học"},
    {"id": "lex.en.200k.057934", "hw": "taillights", "pos": "noun", "ipa": "/ˈteɪllaɪts/", "vi": "đèn báo hiệu phía đuôi xe cơ giới"},
    {"id": "lex.en.200k.057935", "hw": "taneys", "pos": "noun", "ipa": "/ˈteɪniz/", "vi": "Chánh án Tối cao Mỹ Roger B. Taney"},
    {"id": "lex.en.200k.057936", "hw": "tertullians", "pos": "noun", "ipa": "/tɚˈtʌliənz/", "vi": "nhà thần học sơ khai Tertullian"},
    {"id": "lex.en.200k.057937", "hw": "traceries", "pos": "noun", "ipa": "/ˈtreɪsəriz/", "vi": "hoa văn đan vòm đá gothic cửa sổ"},
    {"id": "lex.en.200k.057938", "hw": "triodes", "pos": "noun", "ipa": "/ˈtraɪoʊdz/", "vi": "các đèn điện tử ba cực chân không"},
    {"id": "lex.en.200k.057939", "hw": "tsetses", "pos": "noun", "ipa": "/ˈtsɛtsiz/", "vi": "loài ruồi xê-xê truyền bệnh ngủ"},
    {"id": "lex.en.200k.057940", "hw": "tunneys", "pos": "noun", "ipa": "/ˈtʌniz/", "vi": "nhà vô địch quyền anh Gene Tunney"},
    {"id": "lex.en.200k.057941", "hw": "ummata", "pos": "noun", "ipa": "/ʊmˈmɑːtə/", "vi": "toàn thể cộng đồng tín đồ Hồi giáo"},
    {"id": "lex.en.200k.057942", "hw": "upends", "pos": "verb", "ipa": "/ʌpˈɛndz/", "vi": "lật ngược; đảo lộn trật tự"},
    {"id": "lex.en.200k.057943", "hw": "varros", "pos": "noun", "ipa": "/ˈværoʊz/", "vi": "học giả uyên bác La Mã cổ Varro"},
    {"id": "lex.en.200k.057944", "hw": "venetias", "pos": "noun", "ipa": "/vəˈniːʃiəz/", "vi": "vùng lãnh thổ lịch sử Venetia Ý"},
    {"id": "lex.en.200k.057945", "hw": "vocalizations", "pos": "noun", "ipa": "/ˌvoʊkəlaɪˈzeɪʃənz/", "vi": "sự phát âm; tiếng kêu thành tiếng"},
    {"id": "lex.en.200k.057946", "hw": "wollstonecrafts", "pos": "noun", "ipa": "/ˈwʊlstənkræfts/", "vi": "nhà nữ quyền Mary Wollstonecraft"},
    {"id": "lex.en.200k.057947", "hw": "zoroastrianisms", "pos": "noun", "ipa": "/ˌzɔːroʊˈæstriənɪzəmz/", "vi": "tôn giáo thờ lửa Bái Hỏa giáo"},
    {"id": "lex.en.200k.057948", "hw": "acetylations", "pos": "noun", "ipa": "/əˌsɛtəlˈeɪʃənz/", "vi": "quá trình phản ứng axetyl hóa"},
    {"id": "lex.en.200k.057949", "hw": "ad libitum", "pos": "phrase", "ipa": "", "vi": "tùy ý; ứng khẩu ngẫu hứng"},
    {"id": "lex.en.200k.057950", "hw": "andantes", "pos": "noun", "ipa": "/ɑːnˈdɑːnteɪz/", "vi": "nhịp thong thả vừa phải andante"},
    {"id": "lex.en.200k.057951", "hw": "animatronicses", "pos": "noun", "ipa": "/ˌænɪməˈtrɑːnɪksɪz/", "vi": "nghệ thuật cơ điện tử mô phỏng"},
    {"id": "lex.en.200k.057952", "hw": "arbours", "pos": "noun", "ipa": "/ˈɑːrbɚz/", "vi": "các giàn che bóng mát râm leo cây"},
    {"id": "lex.en.200k.057953", "hw": "ardours", "pos": "noun", "ipa": "/ˈɑːrdɚz/", "vi": "sự hăng hái nhiệt tình nồng cháy"},
    {"id": "lex.en.200k.057954", "hw": "attractors", "pos": "noun", "ipa": "/əˈtræktɚz/", "vi": "điểm hấp dẫn; vùng thu hút quỹ đạo"},
    {"id": "lex.en.200k.057955", "hw": "auricular point", "pos": "phrase", "ipa": "", "vi": "điểm mốc giải phẫu lỗ tai ngoài"},
    {"id": "lex.en.200k.057956", "hw": "bartoks", "pos": "noun", "ipa": "/ˈbɑːrtɔːks/", "vi": "nhạc sĩ Béla Bartók người Hungary"},
    {"id": "lex.en.200k.057957", "hw": "battlers", "pos": "noun", "ipa": "/ˈbætlɚz/", "vi": "người kiên cường chiến đấu vượt khó"},
    {"id": "lex.en.200k.057958", "hw": "benzoates", "pos": "noun", "ipa": "/ˈbɛnzoʊeɪts/", "vi": "muối hoặc este của axit benzoic"},
    {"id": "lex.en.200k.057959", "hw": "blackheart cherry", "pos": "phrase", "ipa": "", "vi": "loài anh đào đen ngọt hình trái tim"},
    {"id": "lex.en.200k.057960", "hw": "blue jessamine", "pos": "phrase", "ipa": "", "vi": "loài cây hoa lài xanh hoa lam"},
    {"id": "lex.en.200k.057961", "hw": "boldfaced", "pos": "verb", "ipa": "/ˈboʊldfeɪst/", "vi": "đã in chữ đậm; trơ tráo mặt dày"},
    {"id": "lex.en.200k.057962", "hw": "booties", "pos": "noun", "ipa": "/ˈbuːtiz/", "vi": "giày len cổ ngắn cho em bé"},
    {"id": "lex.en.200k.057963", "hw": "buglers", "pos": "noun", "ipa": "/ˈbjuːɡlɚz/", "vi": "người lính thổi kèn quân hiệu lệnh"},
    {"id": "lex.en.200k.057964", "hw": "camemberts", "pos": "noun", "ipa": "/ˈkæməmbɛrz/", "vi": "các miếng phô mai mềm béo Camembert"},
    {"id": "lex.en.200k.057965", "hw": "cape jessamine", "pos": "phrase", "ipa": "", "vi": "cây hoa dành dành hoa trắng ngát"},
    {"id": "lex.en.200k.057966", "hw": "carmelites", "pos": "noun", "ipa": "/ˈkɑːrməlaɪts/", "vi": "các tu sĩ thuộc dòng Cát Minh"},
    {"id": "lex.en.200k.057967", "hw": "carports", "pos": "noun", "ipa": "/ˈkɑːrpɔːrts/", "vi": "mái che để xe hơi ngoài trời"},
    {"id": "lex.en.200k.057968", "hw": "cathers", "pos": "noun", "ipa": "/ˈkæðɚz/", "vi": "nữ văn sĩ người Mỹ Willa Cather"},
    {"id": "lex.en.200k.057969", "hw": "caudate nucleus", "pos": "phrase", "ipa": "", "vi": "nhân đuôi thể vân sâu trong não"},
    {"id": "lex.en.200k.057970", "hw": "cellinis", "pos": "noun", "ipa": "/tʃɛˈliːniz/", "vi": "nhà kim hoàn danh họa Cellini"},
    {"id": "lex.en.200k.057971", "hw": "chablises", "pos": "noun", "ipa": "/ʃæˈbliːzɪz/", "vi": "rượu vang trắng Chablis của Pháp"},
    {"id": "lex.en.200k.057972", "hw": "charcots", "pos": "noun", "ipa": "/ʃɑːrˈkoʊz/", "vi": "bác sĩ thần kinh học Jean Charcot"},
    {"id": "lex.en.200k.057973", "hw": "chu kiang", "pos": "phrase", "ipa": "", "vi": "sông Châu Giang miền nam Trung Hoa"},
    {"id": "lex.en.200k.057974", "hw": "circumflex iliac vein", "pos": "phrase", "ipa": "", "vi": "tĩnh mạch chậu nông vòng đùi"},
    {"id": "lex.en.200k.057975", "hw": "cochineal insect", "pos": "phrase", "ipa": "", "vi": "loài rệp son ký sinh xương rồng"},
    {"id": "lex.en.200k.057976", "hw": "conestogas", "pos": "noun", "ipa": "/ˌkɑːnəˈstoʊɡəz/", "vi": "xe ngựa kéo hàng lớn Conestoga"},
    {"id": "lex.en.200k.057977", "hw": "cronked", "pos": "verb", "ipa": "/krɑːŋkt/", "vi": "đã kêu quạ quạ khàn đặc cổ họng"},
    {"id": "lex.en.200k.057978", "hw": "cronking", "pos": "verb", "ipa": "/ˈkrɑːŋkɪŋ/", "vi": "đang kêu quạ quạ tiếng ngỗng trời"},
    {"id": "lex.en.200k.057979", "hw": "cronks", "pos": "verb", "ipa": "/krɑːŋks/", "vi": "kêu quạ quạ tiếng sếu ngỗng"},
    {"id": "lex.en.200k.057980", "hw": "day jessamine", "pos": "phrase", "ipa": "", "vi": "cây hoa dạ lý hương nở ban ngày"},
    {"id": "lex.en.200k.057981", "hw": "deep fording", "pos": "phrase", "ipa": "", "vi": "vượt lội qua đoạn nước ngập sâu"},
    {"id": "lex.en.200k.057982", "hw": "democratisations", "pos": "noun", "ipa": "/dɪˌmɑːkrətaɪˈzeɪʃənz/", "vi": "tiến trình dân chủ hóa xã hội"},
    {"id": "lex.en.200k.057983", "hw": "digressions", "pos": "noun", "ipa": "/daɪˈɡrɛʃənz/", "vi": "những đoạn nói lan man lạc đề"},
    {"id": "lex.en.200k.057984", "hw": "disas", "pos": "noun", "ipa": "/ˈdiːsəz/", "vi": "loài hoa phong lan châu Phi Disa"},
    {"id": "lex.en.200k.057985", "hw": "doxycyclines", "pos": "noun", "ipa": "/ˌdɑːksɪˈsaɪkliːnz/", "vi": "thuốc kháng sinh uống doxycycline"},
    {"id": "lex.en.200k.057986", "hw": "doyens", "pos": "noun", "ipa": "/dɔɪˈɛnz/", "vi": "bậc trưởng lão lão làng thâm niên"},
    {"id": "lex.en.200k.057987", "hw": "drogue parachute", "pos": "phrase", "ipa": "", "vi": "dù hãm phanh tốc độ máy bay"},
    {"id": "lex.en.200k.057988", "hw": "drovers", "pos": "noun", "ipa": "/ˈdroʊvɚz/", "vi": "người lùa đàn gia súc ra chợ bán"},
    {"id": "lex.en.200k.057989", "hw": "durrells", "pos": "noun", "ipa": "/ˈdɜːrəlz/", "vi": "nhà văn nhà tự nhiên học Durrell"},
    {"id": "lex.en.200k.057990", "hw": "endorphins", "pos": "noun", "ipa": "/ɛnˈdɔːrfɪnz/", "vi": "hoóc-môn giảm đau endorphin"},
    {"id": "lex.en.200k.057991", "hw": "epictetuses", "pos": "noun", "ipa": "/ˌɛpɪkˈtiːtəsɪz/", "vi": "triết gia khắc kỷ Hy Lạp Epictetus"},
    {"id": "lex.en.200k.057992", "hw": "erythemas", "pos": "noun", "ipa": "/ˌɛrɪˈθiːməz/", "vi": "chứng ban đỏ xung huyết dưới da"},
    {"id": "lex.en.200k.057993", "hw": "eycks", "pos": "noun", "ipa": "/aɪks/", "vi": "danh họa Hà Lan Jan van Eyck"},
    {"id": "lex.en.200k.057994", "hw": "faisalabads", "pos": "noun", "ipa": "/faɪˌsɑːləˈbɑːdz/", "vi": "thành phố công nghiệp Faisalabad"},
    {"id": "lex.en.200k.057995", "hw": "ferdinand de lesseps", "pos": "phrase", "ipa": "", "vi": "kỹ sư kênh đào Ferdinand de Lesseps"},
    {"id": "lex.en.200k.057996", "hw": "firebases", "pos": "noun", "ipa": "/ˈfaɪɚbeɪsɪz/", "vi": "căn cứ hỏa lực pháo binh dã chiến"},
    {"id": "lex.en.200k.057997", "hw": "formularies", "pos": "noun", "ipa": "/ˈfɔːrmjʊlɛriz/", "vi": "dược thư tổng hợp công thức thuốc"},
    {"id": "lex.en.200k.057998", "hw": "foxtail grass", "pos": "phrase", "ipa": "", "vi": "loài cỏ hoa đuôi chồn mọc dại"},
    {"id": "lex.en.200k.057999", "hw": "gendarmes", "pos": "noun", "ipa": "/ˈʒɑːndɑːrmz/", "vi": "những người lính sen đầm hiến binh"},
    {"id": "lex.en.200k.058000", "hw": "genus vireo", "pos": "phrase", "ipa": "", "vi": "chi chim hót đuôi chét nhỏ Vireo"},
    {"id": "lex.en.200k.058001", "hw": "giant foxtail", "pos": "phrase", "ipa": "", "vi": "loài cỏ đuôi chồn khổng lồ thân to"}
]

# Validation
with open('scratch/b32_r06_raw_p5.json') as f:
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

with open('scratch/b32_r06_p5.json', 'w') as f:
    json.dump(final_p5, f, ensure_ascii=False, indent=2)
print("Part 5 validated and written successfully.")
