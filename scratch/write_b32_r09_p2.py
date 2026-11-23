import json

items = [
  {"id": "lex.en.200k.059103", "hw": "peepholes", "pos": "noun", "ipa": "/pˈiːphoʊlz/", "vi": "mắt thần gắn cửa; lỗ nhòm cửa"},
  {"id": "lex.en.200k.059104", "hw": "phospholipids", "pos": "noun", "ipa": "/ˌfɑːsfoʊlˈɪpɪdz/", "vi": "chất béo màng phospholipid"},
  {"id": "lex.en.200k.059105", "hw": "pocking", "pos": "verb", "ipa": "/pˈɑːkɪŋ/", "vi": "đang làm rỗ mặt; để lại sẹo"},
  {"id": "lex.en.200k.059106", "hw": "pocks", "pos": "noun", "ipa": "/pˈɑks/", "vi": "vết rỗ sẹo; mụn mủ đầu mùa"},
  {"id": "lex.en.200k.059107", "hw": "projectionists", "pos": "noun", "ipa": "/prədʒˈɛkʃənɪsts/", "vi": "người vận hành máy chiếu phim"},
  {"id": "lex.en.200k.059108", "hw": "prosceniums", "pos": "noun", "ipa": "/proʊsˈiːniəmz/", "vi": "vòm khung sân khấu kịch"},
  {"id": "lex.en.200k.059109", "hw": "pseudoephedrines", "pos": "noun", "ipa": "/sˌuːdoʊɪfˈɛdrɪnz/", "vi": "thuốc thông mũi pseudoephedrine"},
  {"id": "lex.en.200k.059110", "hw": "putrajayas", "pos": "noun", "ipa": "/pˌuːtrədʒˈaɪəz/", "vi": "thành phố Putrajaya Malaysia"},
  {"id": "lex.en.200k.059111", "hw": "ravers", "pos": "noun", "ipa": "/rˈeɪvɚz/", "vi": "người đi tiệc quẩy nhạc điện tử"},
  {"id": "lex.en.200k.059112", "hw": "recitatives", "pos": "noun", "ipa": "/rˌɛsətətˈivz/", "vi": "đoạn hát nói kể trong nhạc kịch"},
  {"id": "lex.en.200k.059113", "hw": "recti", "pos": "noun", "ipa": "/rˈɛktaɪ/", "vi": "các cơ thẳng trong giải phẫu"},
  {"id": "lex.en.200k.059114", "hw": "rectuses", "pos": "noun", "ipa": "/rˈɛktəsɪz/", "vi": "nhóm cơ thẳng thành bụng"},
  {"id": "lex.en.200k.059115", "hw": "repressors", "pos": "noun", "ipa": "/rɪprˈɛsɚz/", "vi": "protein ức chế phiên mã gen"},
  {"id": "lex.en.200k.059116", "hw": "retouched", "pos": "verb", "ipa": "/ritˈʌtʃt/", "vi": "đã chỉnh sửa ảnh; dặm lại màu"},
  {"id": "lex.en.200k.059117", "hw": "retouches", "pos": "verb", "ipa": "/ritˈʌtʃɪz/", "vi": "chỉnh sửa chi tiết; dặm lại"},
  {"id": "lex.en.200k.059118", "hw": "retouching", "pos": "verb", "ipa": "/ritˈʌtʃɪŋ/", "vi": "chỉnh sửa ảnh; kỹ thuật tút lại"},
  {"id": "lex.en.200k.059119", "hw": "rootstocks", "pos": "noun", "ipa": "/rˈuːtstɑːks/", "vi": "gốc cây ghép giống; thân rễ củ"},
  {"id": "lex.en.200k.059120", "hw": "rutas", "pos": "noun", "ipa": "/rˈuːtəz/", "vi": "chi cây cửu lý hương ruta"},
  {"id": "lex.en.200k.059121", "hw": "rutiles", "pos": "noun", "ipa": "/rˈuːtaɪlz/", "vi": "khoáng vật titan oxit rutin"},
  {"id": "lex.en.200k.059122", "hw": "salishes", "pos": "noun", "ipa": "/sˈælɪʃɪz/", "vi": "ngữ tộc bản địa Salish châu Mỹ"},
  {"id": "lex.en.200k.059123", "hw": "samias", "pos": "noun", "ipa": "/sˈeɪmiəz/", "vi": "chi bướm đêm tằm sồi samia"},
  {"id": "lex.en.200k.059124", "hw": "sedalias", "pos": "noun", "ipa": "/sɪdˈeɪliəz/", "vi": "thành phố Sedalia bang Missouri"},
  {"id": "lex.en.200k.059125", "hw": "selvas", "pos": "noun", "ipa": "/sˈɛlvəz/", "vi": "rừng mưa nhiệt đới selva Amazon"},
  {"id": "lex.en.200k.059126", "hw": "senoras", "pos": "noun", "ipa": "/seɪnjˈɔːrəz/", "vi": "quý bà; phu nhân Tây Ban Nha"},
  {"id": "lex.en.200k.059127", "hw": "shikokus", "pos": "noun", "ipa": "/ʃɪkˈoʊkuːz/", "vi": "đảo Shikoku của Nhật Bản"},
  {"id": "lex.en.200k.059128", "hw": "sightednesses", "pos": "noun", "ipa": "/sˈaɪtədnəsɪz/", "vi": "khả năng thị lực nhìn thấy"},
  {"id": "lex.en.200k.059129", "hw": "spitsbergens", "pos": "noun", "ipa": "/spˈɪtsbɜːrɡənz/", "vi": "đảo Spitsbergen ở Bắc Cực"},
  {"id": "lex.en.200k.059130", "hw": "stepchildren", "pos": "noun", "ipa": "/stˈɛptʃˈɪldrən/", "vi": "các con riêng của vợ hoặc chồng"},
  {"id": "lex.en.200k.059131", "hw": "stodgier", "pos": "adj", "ipa": "/stˈɑːdʒiɚ/", "vi": "nặng bụng khó tiêu hơn; tẻ nhạt hơn"},
  {"id": "lex.en.200k.059132", "hw": "stodgiest", "pos": "adj", "ipa": "/stˈɑːdʒiɪst/", "vi": "nặng bụng nhất; tẻ nhạt nhất"},
  {"id": "lex.en.200k.059133", "hw": "syndicalists", "pos": "noun", "ipa": "/sˈɪndɪkəlɪsts/", "vi": "người theo chủ nghĩa công đoàn"},
  {"id": "lex.en.200k.059134", "hw": "tabrizes", "pos": "noun", "ipa": "/tæbrˈiːzɪz/", "vi": "thành phố Tabriz của Iran"},
  {"id": "lex.en.200k.059135", "hw": "tattier", "pos": "adj", "ipa": "/tˈætiɚ/", "vi": "tồi tàn xơ xác hơn; cũ rách hơn"},
  {"id": "lex.en.200k.059136", "hw": "tattiest", "pos": "adj", "ipa": "/tˈætiɪst/", "vi": "tồi tàn xơ xác nhất; cũ nát nhất"},
  {"id": "lex.en.200k.059137", "hw": "teamsters", "pos": "noun", "ipa": "/tˈimstɚz/", "vi": "tài xế xe tải hàng đường dài"},
  {"id": "lex.en.200k.059138", "hw": "tenons", "pos": "noun", "ipa": "/tˈɛnənz/", "vi": "đầu mộng gỗ để ghép nối"},
  {"id": "lex.en.200k.059139", "hw": "tubercles", "pos": "noun", "ipa": "/tˈuːbərklz/", "vi": "gờ củ xương; nốt hạt củ lao"},
  {"id": "lex.en.200k.059140", "hw": "turbots", "pos": "noun", "ipa": "/tˈɜːrbəts/", "vi": "loài cá bơn tròn turbot biển"},
  {"id": "lex.en.200k.059141", "hw": "twosomes", "pos": "noun", "ipa": "/tˈuːsəmz/", "vi": "bộ đôi; cặp hai người cùng chơi"},
  {"id": "lex.en.200k.059142", "hw": "unfreezes", "pos": "verb", "ipa": "/ʌnfrˈiːzɪz/", "vi": "rã đông thực phẩm; giải tỏa cấm"},
  {"id": "lex.en.200k.059143", "hw": "unfreezing", "pos": "verb", "ipa": "/ʌnfrˈiːzɪŋ/", "vi": "đang rã đông; giải tỏa tài sản"},
  {"id": "lex.en.200k.059144", "hw": "unfroze", "pos": "verb", "ipa": "/ʌnfrˈoʊz/", "vi": "đã rã đông; đã giải tỏa phong tỏa"},
  {"id": "lex.en.200k.059145", "hw": "vasopressins", "pos": "noun", "ipa": "/vˌeɪzoʊprˈɛsɪnz/", "vi": "hoóc-môn chống bài niệu"},
  {"id": "lex.en.200k.059146", "hw": "woodsheds", "pos": "noun", "ipa": "/wˈʊdʃˌɛdz/", "vi": "nhà kho chứa củi đốt"},
  {"id": "lex.en.200k.059147", "hw": "wotans", "pos": "noun", "ipa": "/vˈoʊtɑːnz/", "vi": "thần tối cao Wotan thần thoại Đức"},
  {"id": "lex.en.200k.059148", "hw": "zappers", "pos": "noun", "ipa": "/zˈæpɚz/", "vi": "vợt bắt muỗi điện; đồ diệt bọ"},
  {"id": "lex.en.200k.059149", "hw": "zeas", "pos": "noun", "ipa": "/zˈiːəz/", "vi": "chi thực vật ngô bắp zea"},
  {"id": "lex.en.200k.059150", "hw": "acuminate leaf", "pos": "phrase", "ipa": "/əˈkjuːmɪneɪt liːf/", "vi": "lá cây có đầu nhọn vuốt dài"},
  {"id": "lex.en.200k.059151", "hw": "alfred kroeber", "pos": "phrase", "ipa": "/ˈælfrɪd ˈkroʊbər/", "vi": "nhà nhân học Alfred Kroeber"},
  {"id": "lex.en.200k.059152", "hw": "alfred louis kroeber", "pos": "phrase", "ipa": "/ˈælfrɪd ˈluːɪs ˈkroʊbər/", "vi": "học giả Alfred Louis Kroeber"},
  {"id": "lex.en.200k.059153", "hw": "alkylating agent", "pos": "phrase", "ipa": "/ˈælkəleɪtɪŋ ˈeɪdʒənt/", "vi": "tác nhân ankyl hóa trị ung thư"},
  {"id": "lex.en.200k.059154", "hw": "american arrowroot", "pos": "phrase", "ipa": "/əˈmɛrɪkən ˈæroʊruːt/", "vi": "cây dong củ dong riềng Mỹ"},
  {"id": "lex.en.200k.059155", "hw": "american hornbeam", "pos": "phrase", "ipa": "/əˈmɛrɪkən ˈhɔːrnbiːm/", "vi": "cây trăn Mỹ gỗ rắn chắc"},
  {"id": "lex.en.200k.059156", "hw": "angelica sylvestris", "pos": "phrase", "ipa": "/ænˈdʒɛlɪkə sɪlˈvɛstrɪs/", "vi": "loài bạch chỉ dại châu Âu"},
  {"id": "lex.en.200k.059157", "hw": "antonio stradivari", "pos": "phrase", "ipa": "/ænˈtoʊnioʊ ˌstrædəˈvɑːri/", "vi": "nghệ nhân đàn Antonio Stradivari"},
  {"id": "lex.en.200k.059158", "hw": "arrowroot family", "pos": "phrase", "ipa": "/ˈæroʊruːt ˈfæməli/", "vi": "họ thực vật dong riềng củ"},
  {"id": "lex.en.200k.059159", "hw": "austenitic manganese steel", "pos": "phrase", "ipa": "/ɔːstəˈnɪtɪk ˈmæŋɡəniːz stiːl/", "vi": "thép mangan austenit chịu mài mòn"},
  {"id": "lex.en.200k.059160", "hw": "betula nigra", "pos": "phrase", "ipa": "/ˈbɛtjʊlə ˈnaɪɡrə/", "vi": "loài cây bạch dương sông đen"},
  {"id": "lex.en.200k.059161", "hw": "blanching agent", "pos": "phrase", "ipa": "/ˈblæntʃɪŋ ˈeɪdʒənt/", "vi": "hóa chất tẩy trắng nguyên liệu"},
  {"id": "lex.en.200k.059162", "hw": "chloral hydrate", "pos": "phrase", "ipa": "/ˈklɔːrəl ˈhaɪdreɪt/", "vi": "thuốc an thần chloral hydrate"},
  {"id": "lex.en.200k.059163", "hw": "circumflex scapular artery", "pos": "phrase", "ipa": "/ˈsɜːrkəmflɛks ˈskæpjʊlər ˈɑːrtəri/", "vi": "động mạch mũ bả vai"},
  {"id": "lex.en.200k.059164", "hw": "common purslane", "pos": "phrase", "ipa": "/ˈkɑːmən ˈpɜːrsleɪn/", "vi": "cây rau sam ăn lá quen thuộc"},
  {"id": "lex.en.200k.059165", "hw": "eastern hop hornbeam", "pos": "phrase", "ipa": "/ˈiːstərn hɑːp ˈhɔːrnbiːm/", "vi": "cây trăn nhảy hoa bia đông Mỹ"},
  {"id": "lex.en.200k.059166", "hw": "eudora welty", "pos": "phrase", "ipa": "/juːˈdɔːrə ˈwɛlti/", "vi": "nữ nhà văn Eudora Welty"},
  {"id": "lex.en.200k.059167", "hw": "european hornbeam", "pos": "phrase", "ipa": "/ˌjʊərəˈpiːən ˈhɔːrnbiːm/", "vi": "cây trăn châu Âu gỗ đặc"},
  {"id": "lex.en.200k.059168", "hw": "ficus aurea", "pos": "phrase", "ipa": "/ˈfaɪkəs ˈɔːriə/", "vi": "cây đa bóp cổ si vàng Florida"},
  {"id": "lex.en.200k.059169", "hw": "florida arrowroot", "pos": "phrase", "ipa": "/ˈflɔːrɪdə ˈæroʊruːt/", "vi": "cây cọ giả dong Florida"},
  {"id": "lex.en.200k.059170", "hw": "gamma aminobutyric acid", "pos": "phrase", "ipa": "/ˈɡæmə əˌmiːnoʊbjuːˈtɪrɪk ˈæsɪd/", "vi": "chất dẫn truyền thần kinh GABA"},
  {"id": "lex.en.200k.059171", "hw": "gangrenous emphysema", "pos": "phrase", "ipa": "/ˈɡæŋɡrənəs ˌɛmfəˈsiːmə/", "vi": "hoại thư sinh hơi khí thũng"},
  {"id": "lex.en.200k.059172", "hw": "genus areca", "pos": "phrase", "ipa": "/ˈdʒiːnəs əˈriːkə/", "vi": "chi thực vật cau ăn trầu"},
  {"id": "lex.en.200k.059173", "hw": "genus cattleya", "pos": "phrase", "ipa": "/ˈdʒiːnəs kætˈleɪə/", "vi": "chi hoa lan hoàng hậu Cattleya"},
  {"id": "lex.en.200k.059174", "hw": "genus mentha", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈmɛnθə/", "vi": "chi thực vật cây bạc hà"},
  {"id": "lex.en.200k.059175", "hw": "genus nicotiana", "pos": "phrase", "ipa": "/ˈdʒiːnəs nɪˌkoʊʃiˈeɪnə/", "vi": "chi cây thuốc lá Nicotiana"},
  {"id": "lex.en.200k.059176", "hw": "genus prunella", "pos": "phrase", "ipa": "/ˈdʒiːnəs pruːˈnɛlə/", "vi": "chi cỏ hạ khô thảo Prunella"},
  {"id": "lex.en.200k.059177", "hw": "georges simenon", "pos": "phrase", "ipa": "/ʒɔːrʒ siːmənˈɔːn/", "vi": "nhà văn trinh thám Georges Simenon"},
  {"id": "lex.en.200k.059178", "hw": "gudgeon pin", "pos": "phrase", "ipa": "/ˈɡʌdʒən pɪn/", "vi": "chốt nối pít-tông đầu nhỏ"},
  {"id": "lex.en.200k.059179", "hw": "guillaume apollinaire", "pos": "phrase", "ipa": "/ɡiːˈjoʊm əˌpɑːləˈnɛər/", "vi": "nhà thơ Guillaume Apollinaire"},
  {"id": "lex.en.200k.059180", "hw": "hop hornbeam", "pos": "phrase", "ipa": "/hɑːp ˈhɔːrnbiːm/", "vi": "cây trăn hoa bia chi Ostrya"},
  {"id": "lex.en.200k.059181", "hw": "inclusion body myositis", "pos": "phrase", "ipa": "/ɪnˈkluːʒən ˈbɑːdi ˌmaɪəˈsaɪtɪs/", "vi": "bệnh viêm cơ thể vùi mạn tính"},
  {"id": "lex.en.200k.059182", "hw": "indian arrowroot", "pos": "phrase", "ipa": "/ˈɪndiən ˈæroʊruːt/", "vi": "củ dong riềng Ấn Độ lấy bột"},
  {"id": "lex.en.200k.059183", "hw": "jean antoine watteau", "pos": "phrase", "ipa": "/ʒɑːn ɑːnˈtwɑːn wɑːˈtoʊ/", "vi": "danh họa Jean-Antoine Watteau"},
  {"id": "lex.en.200k.059184", "hw": "jus civile", "pos": "phrase", "ipa": "/dʒʌs sɪˈvɪliː/", "vi": "luật công dân La Mã cổ đại"},
  {"id": "lex.en.200k.059185", "hw": "king protea", "pos": "phrase", "ipa": "/kɪŋ proʊˈtiːə/", "vi": "hoa đường bệ hoàng đế king protea"},
  {"id": "lex.en.200k.059186", "hw": "lebanese hizballah", "pos": "phrase", "ipa": "/ˌlɛbəˈniːz ˌhɪzbəˈlɑː/", "vi": "phong trào Hezbollah tại Liban"},
  {"id": "lex.en.200k.059187", "hw": "leroi jones", "pos": "phrase", "ipa": "/ləˈrɔɪ dʒoʊnz/", "vi": "nhà văn Amiri Baraka Leroi Jones"},
  {"id": "lex.en.200k.059188", "hw": "lye hominy", "pos": "phrase", "ipa": "/laɪ ˈhɑːməni/", "vi": "hạt ngô ngâm nước vôi kiềm"},
  {"id": "lex.en.200k.059189", "hw": "malvina hoffman", "pos": "phrase", "ipa": "/mælˈviːnə ˈhɑːfmən/", "vi": "nữ điêu khắc gia Malvina Hoffman"},
  {"id": "lex.en.200k.059190", "hw": "medgar evers", "pos": "phrase", "ipa": "/ˈmɛdɡər ˈɛvərz/", "vi": "nhà nhân quyền Medgar Evers"},
  {"id": "lex.en.200k.059191", "hw": "medial condyle", "pos": "phrase", "ipa": "/ˈmiːdiəl ˈkɑːndaɪl/", "vi": "lồi cầu trong khớp đầu gối"},
  {"id": "lex.en.200k.059192", "hw": "mescal bean", "pos": "phrase", "ipa": "/mɛsˈkæl biːn/", "vi": "hạt đậu đỏ mescal có độc"},
  {"id": "lex.en.200k.059193", "hw": "mescal button", "pos": "phrase", "ipa": "/mɛsˈkæl ˈbʌtn/", "vi": "mẩu xương rồng peyote chứa ma túy"},
  {"id": "lex.en.200k.059194", "hw": "monosodium glutamate", "pos": "phrase", "ipa": "/ˌmɑːnoʊˈsoʊdiəm ˈɡluːtəmeɪt/", "vi": "bột ngọt mì chính gia vị"},
  {"id": "lex.en.200k.059195", "hw": "naja hannah", "pos": "phrase", "ipa": "/ˈneɪdʒə ˈhænə/", "vi": "loài rắn hổ mang chúa cực độc"},
  {"id": "lex.en.200k.059196", "hw": "nonesuch clover", "pos": "phrase", "ipa": "/ˈnʌnsʌtʃ ˈkloʊvər/", "vi": "cỏ linh lăng cúc đen hoa vàng"},
  {"id": "lex.en.200k.059197", "hw": "order orthoptera", "pos": "phrase", "ipa": "/ˈɔːrdər ɔːrˈθɑːptərə/", "vi": "bộ côn trùng Cánh thẳng"},
  {"id": "lex.en.200k.059198", "hw": "potassium permanganate", "pos": "phrase", "ipa": "/pəˈtæsiəm pərˈmæŋɡəneɪt/", "vi": "thuốc tím sát trùng pemanganat"},
  {"id": "lex.en.200k.059199", "hw": "prickle cell", "pos": "phrase", "ipa": "/ˈprɪkl sɛl/", "vi": "tế bào gai của lớp biểu bì da"},
  {"id": "lex.en.200k.059200", "hw": "protea family", "pos": "phrase", "ipa": "/proʊˈtiːə ˈfæməli/", "vi": "họ thực vật hoa đường bệ Protea"},
  {"id": "lex.en.200k.059201", "hw": "purslane family", "pos": "phrase", "ipa": "/ˈpɜːrsleɪn ˈfæməli/", "vi": "họ thực vật rau sam lá mọng"},
  {"id": "lex.en.200k.059202", "hw": "ramjet engine", "pos": "phrase", "ipa": "/ˈræmdʒɛt ˈɛndʒɪn/", "vi": "động cơ phản lực luồng tĩnh ramjet"}
]

with open('scratch/b32_r09_raw_p2.json') as f:
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

with open('scratch/b32_r09_p2.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Part 2 validated and written successfully.")
