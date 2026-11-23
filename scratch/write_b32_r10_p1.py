import json

items = [
  {"id": "lex.en.200k.059503", "hw": "pongos", "pos": "noun", "ipa": "/pˈɑːŋɡoʊz/", "vi": "chi vượn người đười ươi Pongo"},
  {"id": "lex.en.200k.059504", "hw": "powerboats", "pos": "noun", "ipa": "/pˈaʊɚbˌoʊts/", "vi": "thuyền máy cao tốc; ca nô đua"},
  {"id": "lex.en.200k.059505", "hw": "proserpines", "pos": "noun", "ipa": "/prəzˈɜːrpɪniz/", "vi": "nữ thần mùa xuân Proserpina"},
  {"id": "lex.en.200k.059506", "hw": "pushchairs", "pos": "noun", "ipa": "/pˈʊʃtʃɛrz/", "vi": "xe đẩy em bé gập được"},
  {"id": "lex.en.200k.059507", "hw": "regicides", "pos": "noun", "ipa": "/rˈɛdʒɪsaɪdz/", "vi": "kẻ giết vua; tội sát hại vua"},
  {"id": "lex.en.200k.059508", "hw": "shiitakes", "pos": "noun", "ipa": "/ʃiːtˈɑːkeɪz/", "vi": "nấm đông cô; nấm hương Nhật"},
  {"id": "lex.en.200k.059509", "hw": "sicilias", "pos": "noun", "ipa": "/sɪsˈɪliəz/", "vi": "đảo Sicilia của nước Ý"},
  {"id": "lex.en.200k.059510", "hw": "snowbirds", "pos": "noun", "ipa": "/snˈoʊbˌɜːrdz/", "vi": "người tránh rét; chim sẻ tuyết"},
  {"id": "lex.en.200k.059511", "hw": "sowers", "pos": "noun", "ipa": "/sˈoʊɚz/", "vi": "người gieo hạt giống"},
  {"id": "lex.en.200k.059512", "hw": "specialisms", "pos": "noun", "ipa": "/spˈɛʃəlɪzəmz/", "vi": "lĩnh vực chuyên môn sâu"},
  {"id": "lex.en.200k.059513", "hw": "spekes", "pos": "noun", "ipa": "/spˈiːks/", "vi": "nhà thám hiểm John Speke"},
  {"id": "lex.en.200k.059514", "hw": "stabilisers", "pos": "noun", "ipa": "/stˈeɪbəlaɪzɚz/", "vi": "bộ ổn định cân bằng; chất ổn định"},
  {"id": "lex.en.200k.059515", "hw": "supersymmetries", "pos": "noun", "ipa": "/sˌuːpərsˈɪmətriːz/", "vi": "thuyết siêu đối xứng vật lý"},
  {"id": "lex.en.200k.059516", "hw": "suspenders", "pos": "noun", "ipa": "/səspˈɛndɚz/", "vi": "dây đai đeo quần chữ Y"},
  {"id": "lex.en.200k.059517", "hw": "swarthier", "pos": "adj", "ipa": "/swˈɔːrðiɚ/", "vi": "da ngăm đen hơn; sạm nắng hơn"},
  {"id": "lex.en.200k.059518", "hw": "swarthiest", "pos": "adj", "ipa": "/swˈɔːrðiɪst/", "vi": "da ngăm đen nhất; sạm nhất"},
  {"id": "lex.en.200k.059519", "hw": "symbolisings", "pos": "noun", "ipa": "/sˈɪmbəlaɪzɪŋz/", "vi": "hành vi biểu tượng hóa tượng trưng"},
  {"id": "lex.en.200k.059520", "hw": "tearooms", "pos": "noun", "ipa": "/tˈiːruːmz/", "vi": "quán trà chiều; phòng uống trà"},
  {"id": "lex.en.200k.059521", "hw": "tipis", "pos": "noun", "ipa": "/tˈiːpiːz/", "vi": "lều da hình nón người da đỏ"},
  {"id": "lex.en.200k.059522", "hw": "toffs", "pos": "noun", "ipa": "/tˈɑːfs/", "vi": "người thuộc tầng lớp thượng lưu"},
  {"id": "lex.en.200k.059523", "hw": "tracheotomies", "pos": "noun", "ipa": "/trˌeɪkiˈɑːtəmiz/", "vi": "thủ thuật mở khí quản cổ"},
  {"id": "lex.en.200k.059524", "hw": "treetops", "pos": "noun", "ipa": "/trˈitˌɔps/", "vi": "ngọn cây cao; tán ngọn cây"},
  {"id": "lex.en.200k.059525", "hw": "trentos", "pos": "noun", "ipa": "/trˈɛntoʊz/", "vi": "thành phố Trento nước Ý"},
  {"id": "lex.en.200k.059526", "hw": "ursuses", "pos": "noun", "ipa": "/ˈɜːrsəsɪz/", "vi": "chi động vật gấu lớn Ursus"},
  {"id": "lex.en.200k.059527", "hw": "valedictories", "pos": "noun", "ipa": "/vˌælədˈɪktəriz/", "vi": "diễn văn từ biệt lễ tốt nghiệp"},
  {"id": "lex.en.200k.059528", "hw": "warszawas", "pos": "noun", "ipa": "/vɑːrʃˈɑːvəz/", "vi": "thủ đô Warszawa của Ba Lan"},
  {"id": "lex.en.200k.059529", "hw": "whiners", "pos": "noun", "ipa": "/wˈaɪnɚz/", "vi": "kẻ hay than vãn rên rỉ mè nheo"},
  {"id": "lex.en.200k.059530", "hw": "woofers", "pos": "noun", "ipa": "/wˈʊfɚz/", "vi": "loa trầm tái tạo âm trầm"},
  {"id": "lex.en.200k.059531", "hw": "worriers", "pos": "noun", "ipa": "/wˈɜːriɚz/", "vi": "người hay lo âu thấp thỏm"},
  {"id": "lex.en.200k.059532", "hw": "aberdares", "pos": "noun", "ipa": "/ˌæbərdˈɛərz/", "vi": "thị trấn Aberdare ở xứ Wales"},
  {"id": "lex.en.200k.059533", "hw": "acths", "pos": "noun", "ipa": "/ˌeɪsiːtiːˈeɪtʃɪz/", "vi": "hoóc-môn hướng vỏ thượng thận"},
  {"id": "lex.en.200k.059534", "hw": "alluviums", "pos": "noun", "ipa": "/əlˈuːviəmz/", "vi": "lớp đất phù sa bồi tích sông"},
  {"id": "lex.en.200k.059535", "hw": "anasazis", "pos": "noun", "ipa": "/ˌænəsˈɑːziz/", "vi": "bộ tộc bản địa cổ Anasazi"},
  {"id": "lex.en.200k.059536", "hw": "argonauts", "pos": "noun", "ipa": "/ˈɑrɡənˌɔts/", "vi": "dũng sĩ tàu Argo; ốc anh vũ giấy"},
  {"id": "lex.en.200k.059537", "hw": "armoires", "pos": "noun", "ipa": "/ˈɑmwɑrz/", "vi": "tủ gỗ lớn đựng quần áo kiểu cổ"},
  {"id": "lex.en.200k.059538", "hw": "auberges", "pos": "noun", "ipa": "/oʊbˈɛərʒɪz/", "vi": "quán trọ nhà hàng kiểu Pháp"},
  {"id": "lex.en.200k.059539", "hw": "authenticators", "pos": "noun", "ipa": "/ɔːθˈɛntɪkeɪtɚz/", "vi": "người xác thực; thiết bị xác thực"},
  {"id": "lex.en.200k.059540", "hw": "azts", "pos": "noun", "ipa": "/ˌeɪzɛttiːz/", "vi": "thuốc kháng vi-rút HIV AZT"},
  {"id": "lex.en.200k.059541", "hw": "baseboards", "pos": "noun", "ipa": "/bˈeɪsbˌɔrdz/", "vi": "ván ốp chân tường; len chân tường"},
  {"id": "lex.en.200k.059542", "hw": "believabilities", "pos": "noun", "ipa": "/bəlˌiːvəbˈɪlətiz/", "vi": "độ tin cậy; tính xác thực"},
  {"id": "lex.en.200k.059543", "hw": "bellerophons", "pos": "noun", "ipa": "/bəlˈɛrəfɑːnz/", "vi": "dũng sĩ Bellerophon cưỡi Pegasus"},
  {"id": "lex.en.200k.059544", "hw": "bluegills", "pos": "noun", "ipa": "/blˈuːɡɪlz/", "vi": "loài cá mang xanh bluegill"},
  {"id": "lex.en.200k.059545", "hw": "bottlers", "pos": "noun", "ipa": "/bˈɑtlɚz/", "vi": "nhà máy đóng chai nước giải khát"},
  {"id": "lex.en.200k.059546", "hw": "bourns", "pos": "noun", "ipa": "/bˈɔːrnz/", "vi": "ranh giới hạn độ; dòng suối nhỏ"},
  {"id": "lex.en.200k.059547", "hw": "braques", "pos": "noun", "ipa": "/brˈɑːks/", "vi": "danh họa Georges Braque"},
  {"id": "lex.en.200k.059548", "hw": "brewpubs", "pos": "noun", "ipa": "/brˈuːpʌbz/", "vi": "quán bia tự ủ thủ công"},
  {"id": "lex.en.200k.059549", "hw": "brontosauruses", "pos": "noun", "ipa": "/brˌɑːntəsˈɔːrəsɪz/", "vi": "khủng long sấm sét brontosaurus"},
  {"id": "lex.en.200k.059550", "hw": "brouhahas", "pos": "noun", "ipa": "/brˈuːhɑːhɑːz/", "vi": "vụ lùm xùm ồn ào náo động"},
  {"id": "lex.en.200k.059551", "hw": "camerouns", "pos": "noun", "ipa": "/kˌæmərˈuːnz/", "vi": "quốc gia Cameroon ở châu Phi"},
  {"id": "lex.en.200k.059552", "hw": "carafes", "pos": "noun", "ipa": "/kərˈæfs/", "vi": "bình thủy tinh rót rượu nước"},
  {"id": "lex.en.200k.059553", "hw": "carburettors", "pos": "noun", "ipa": "/kɑːrbjʊrˈɛtɚz/", "vi": "bộ chế hòa khí động cơ"},
  {"id": "lex.en.200k.059554", "hw": "carpathianses", "pos": "noun", "ipa": "/kɑːrpˈeɪθiənzɪz/", "vi": "dãy núi Carpath ở Đông Âu"},
  {"id": "lex.en.200k.059555", "hw": "catulli", "pos": "noun", "ipa": "/kətˈʌlaɪ/", "vi": "nhà thơ La Mã cổ Catullus"},
  {"id": "lex.en.200k.059556", "hw": "cebuanos", "pos": "noun", "ipa": "/sɛbwˈɑːnoʊz/", "vi": "tiếng Cebuano của Philippines"},
  {"id": "lex.en.200k.059557", "hw": "cloacae", "pos": "noun", "ipa": "/kloʊˈeɪsiː/", "vi": "lỗ huyệt chung tiêu hóa niệu"},
  {"id": "lex.en.200k.059558", "hw": "codfishes", "pos": "noun", "ipa": "/kˈɑːdfˌɪʃɪz/", "vi": "các loài cá tuyết biển sâu"},
  {"id": "lex.en.200k.059559", "hw": "contralti", "pos": "noun", "ipa": "/kəntrˈæltiː/", "vi": "các giọng ca nữ trầm opera"},
  {"id": "lex.en.200k.059560", "hw": "contraltos", "pos": "noun", "ipa": "/kəntrˈæltoʊz/", "vi": "nữ ca sĩ sở hữu giọng trầm"},
  {"id": "lex.en.200k.059561", "hw": "correlatives", "pos": "noun", "ipa": "/kərˈɛlətɪvz/", "vi": "từ tương liên; yếu tố liên đới"},
  {"id": "lex.en.200k.059562", "hw": "coxswains", "pos": "noun", "ipa": "/kˈɑːksənz/", "vi": "người cầm lái thuyền đua chèo"},
  {"id": "lex.en.200k.059563", "hw": "crans", "pos": "noun", "ipa": "/krˈænz/", "vi": "thùng đong cá trích cran"},
  {"id": "lex.en.200k.059564", "hw": "daccas", "pos": "noun", "ipa": "/dˈækəz/", "vi": "thành phố Dhaka của Bangladesh"},
  {"id": "lex.en.200k.059565", "hw": "dirigibles", "pos": "noun", "ipa": "/dɪrˈɪdʒəbəlz/", "vi": "khí cầu có động cơ điều khiển"},
  {"id": "lex.en.200k.059566", "hw": "doorstops", "pos": "noun", "ipa": "/dˈɔːrstɑːps/", "vi": "cục chặn cửa; chêm giữ cửa"},
  {"id": "lex.en.200k.059567", "hw": "dyspneas", "pos": "noun", "ipa": "/dɪspnˈiːəz/", "vi": "chứng khó thở do bệnh lý"},
  {"id": "lex.en.200k.059568", "hw": "ebits", "pos": "noun", "ipa": "/ˌiːbˈɪts/", "vi": "lợi nhuận trước lãi vay và thuế"},
  {"id": "lex.en.200k.059569", "hw": "folktales", "pos": "noun", "ipa": "/fˈoʊkteɪlz/", "vi": "truyện cổ tích dân gian truyền khẩu"},
  {"id": "lex.en.200k.059570", "hw": "galateas", "pos": "noun", "ipa": "/ɡˌælətˈiːəz/", "vi": "nàng Galatea trong thần thoại"},
  {"id": "lex.en.200k.059571", "hw": "garis", "pos": "noun", "ipa": "/ɡˈærɪs/", "vi": "bột sắn lên men gari Tây Phi"},
  {"id": "lex.en.200k.059572", "hw": "gauzier", "pos": "adj", "ipa": "/ɡˈɔːziɚ/", "vi": "mỏng như gạc hơn; mờ sương hơn"},
  {"id": "lex.en.200k.059573", "hw": "gauziest", "pos": "adj", "ipa": "/ɡˈɔːziɪst/", "vi": "mỏng như vải gạc nhất"},
  {"id": "lex.en.200k.059574", "hw": "gluons", "pos": "noun", "ipa": "/ɡlˈuːɑːnz/", "vi": "hạt gluon truyền tương tác mạnh"},
  {"id": "lex.en.200k.059575", "hw": "glutei", "pos": "noun", "ipa": "/ɡluːtˈiːaɪ/", "vi": "các cơ mông lớn nhỡ bé"},
  {"id": "lex.en.200k.059576", "hw": "gluteuses", "pos": "noun", "ipa": "/ɡluːtˈiːəsɪz/", "vi": "nhóm các cơ mông trong giải phẫu"},
  {"id": "lex.en.200k.059577", "hw": "gourmands", "pos": "noun", "ipa": "/ɡʊərmˈɑːndz/", "vi": "người thích ăn ngon số nhiều"},
  {"id": "lex.en.200k.059578", "hw": "granths", "pos": "noun", "ipa": "/ɡrˈɑːnθs/", "vi": "kinh thánh Granth của đạo Sikh"},
  {"id": "lex.en.200k.059579", "hw": "grapplers", "pos": "noun", "ipa": "/ɡrˈæplɚz/", "vi": "võ sĩ vật cận chiến grappler"},
  {"id": "lex.en.200k.059580", "hw": "hajjis", "pos": "noun", "ipa": "/hˈɑːdʒiz/", "vi": "tín đồ hành hương Mecca"},
  {"id": "lex.en.200k.059581", "hw": "hypotenuses", "pos": "noun", "ipa": "/haɪpˈɑːtənˌuːsɪz/", "vi": "cạnh huyền tam giác vuông"},
  {"id": "lex.en.200k.059582", "hw": "interjections", "pos": "noun", "ipa": "/ˌɪntɚdʒˈɛkʃənz/", "vi": "thán từ cảm thán trong ngữ pháp"},
  {"id": "lex.en.200k.059583", "hw": "jabalpurs", "pos": "noun", "ipa": "/dʒˈæbəlpʊərz/", "vi": "thành phố Jabalpur Ấn Độ"},
  {"id": "lex.en.200k.059584", "hw": "knossoses", "pos": "noun", "ipa": "/nˈɑːsəsɪz/", "vi": "cung điện cổ Knossos ở đảo Crete"},
  {"id": "lex.en.200k.059585", "hw": "lectureships", "pos": "noun", "ipa": "/lˈɛktʃɚʃɪps/", "vi": "chức danh giảng viên đại học"},
  {"id": "lex.en.200k.059586", "hw": "locatives", "pos": "noun", "ipa": "/lˈɑːkətɪvz/", "vi": "vị cách chỉ nơi chốn ngữ pháp"},
  {"id": "lex.en.200k.059587", "hw": "ltms", "pos": "noun", "ipa": "/ˌɛltiːˈɛmz/", "vi": "trí nhớ dài hạn trong tâm lý học"},
  {"id": "lex.en.200k.059588", "hw": "lucites", "pos": "noun", "ipa": "/lˈuːsaɪts/", "vi": "nhựa acrylic trong suốt lucite"},
  {"id": "lex.en.200k.059589", "hw": "maculas", "pos": "noun", "ipa": "/mˈækjʊləz/", "vi": "hoàng điểm mắt; đốm sắc tố da"},
  {"id": "lex.en.200k.059590", "hw": "maracaibos", "pos": "noun", "ipa": "/ˌmærəkˈaɪboʊz/", "vi": "thành phố cảng Maracaibo"},
  {"id": "lex.en.200k.059591", "hw": "meleses", "pos": "noun", "ipa": "/mˈiːliːzɪz/", "vi": "chi loài lửng ăn thịt meles"},
  {"id": "lex.en.200k.059592", "hw": "mendelians", "pos": "noun", "ipa": "/mɛndˈiːliənz/", "vi": "người theo học thuyết gen Mendel"},
  {"id": "lex.en.200k.059593", "hw": "metallurgists", "pos": "noun", "ipa": "/mˈɛtəlɜːrdʒɪsts/", "vi": "kỹ sư chuyên gia ngành luyện kim"},
  {"id": "lex.en.200k.059594", "hw": "naproxens", "pos": "noun", "ipa": "/nəprˈɑːksɪnz/", "vi": "thuốc chống viêm giảm đau naproxen"},
  {"id": "lex.en.200k.059595", "hw": "neutropenias", "pos": "noun", "ipa": "/nˌuːtroʊpˈiːniəz/", "vi": "chứng giảm số lượng bạch cầu hạt"},
  {"id": "lex.en.200k.059596", "hw": "nicaeas", "pos": "noun", "ipa": "/naɪsˈiːəz/", "vi": "thành phố cổ Nicaea công đồng"},
  {"id": "lex.en.200k.059597", "hw": "nnws", "pos": "noun", "ipa": "/ˌɛnɛndˈʌbəljuːz/", "vi": "hướng bắc tây bắc la bàn"},
  {"id": "lex.en.200k.059598", "hw": "octogenarians", "pos": "noun", "ipa": "/ˌɑːktədʒənˈɛəriənz/", "vi": "người ở độ tuổi tám mươi"},
  {"id": "lex.en.200k.059599", "hw": "oedemas", "pos": "noun", "ipa": "/ɪdˈiːməz/", "vi": "chứng phù nề sưng ứ dịch mô"},
  {"id": "lex.en.200k.059600", "hw": "olefins", "pos": "noun", "ipa": "/ˈoʊləfɪnz/", "vi": "hợp chất anken olefin không no"},
  {"id": "lex.en.200k.059601", "hw": "omsks", "pos": "noun", "ipa": "/ˈɑːmsks/", "vi": "thành phố Omsk ở Siberia nước Nga"},
  {"id": "lex.en.200k.059602", "hw": "otitises", "pos": "noun", "ipa": "/oʊtˈaɪtɪsɪz/", "vi": "chứng bệnh viêm tai trong ngoài"}
]

with open('scratch/b32_r10_raw_p1.json') as f:
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

with open('scratch/b32_r10_p1.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Part 1 validated and written successfully.")
