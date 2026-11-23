import json

items = [
  {"id": "lex.en.200k.063903", "hw": "josues", "pos": "noun", "ipa": "/ˈdʒɑːʃuːəz/", "vi": "sách Giô-suê trong Kinh Thánh"},
  {"id": "lex.en.200k.063904", "hw": "kalkis", "pos": "noun", "ipa": "/ˈkɑːlkiz/", "vi": "hóa thân cuối thần Vishnu Kalki"},
  {"id": "lex.en.200k.063905", "hw": "kazaks", "pos": "noun", "ipa": "/kəˈzɑːks/", "vi": "người dân tộc và tiếng Kazakh"},
  {"id": "lex.en.200k.063906", "hw": "kraals", "pos": "noun", "ipa": "/krɑːlz/", "vi": "làng tròn Nam Phi; chuồng rào kín"},
  {"id": "lex.en.200k.063907", "hw": "lashers", "pos": "noun", "ipa": "/ˈlæʃərz/", "vi": "người quất roi; thợ buộc dây neo"},
  {"id": "lex.en.200k.063908", "hw": "launderettes", "pos": "noun", "ipa": "/ˌlɔːndəˈrɛts/", "vi": "tiệm giặt là tự động bằng xu (Anh)"},
  {"id": "lex.en.200k.063909", "hw": "lepantos", "pos": "noun", "ipa": "/ləˈpæntoʊz/", "vi": "hải chiến Lepanto năm 1571 ở Hy Lạp"},
  {"id": "lex.en.200k.063910", "hw": "lungis", "pos": "noun", "ipa": "/ˈlʊŋɡiz/", "vi": "váy xà rông quấn eo nam giới Nam Á"},
  {"id": "lex.en.200k.063911", "hw": "lyssas", "pos": "noun", "ipa": "/ˈlɪsəz/", "vi": "bệnh dại virus; cơn cuồng nộ thần"},
  {"id": "lex.en.200k.063912", "hw": "magnificoes", "pos": "noun", "ipa": "/mæɡˈnɪfɪˌkoʊz/", "vi": "nhân vật quyền quý cao sang Venice"},
  {"id": "lex.en.200k.063913", "hw": "magnificos", "pos": "noun", "ipa": "/mæɡˈnɪfɪˌkoʊz/", "vi": "bậc quyền quý cao sang thời cổ"},
  {"id": "lex.en.200k.063914", "hw": "malamuds", "pos": "noun", "ipa": "/ˈmæləmədz/", "vi": "nhà văn Mỹ Bernard Malamud"},
  {"id": "lex.en.200k.063915", "hw": "matriculated", "pos": "verb", "ipa": "/məˈtrɪkjəˌleɪtɪd/", "vi": "đã ghi danh nhập học bậc đại học"},
  {"id": "lex.en.200k.063916", "hw": "matriculates", "pos": "noun", "ipa": "/məˈtrɪkjəlɪts/", "vi": "tân sinh viên ghi danh vào đại học"},
  {"id": "lex.en.200k.063917", "hw": "matriculating", "pos": "verb", "ipa": "/məˈtrɪkjəˌleɪtɪŋ/", "vi": "đang ghi danh nhập học vào đại học"},
  {"id": "lex.en.200k.063918", "hw": "menthas", "pos": "noun", "ipa": "/ˈmɛnθəz/", "vi": "chi cây bạc hà thơm Mentha"},
  {"id": "lex.en.200k.063919", "hw": "molieres", "pos": "noun", "ipa": "/moʊlˈjɛərz/", "vi": "nhà soạn hài kịch Pháp Molière"},
  {"id": "lex.en.200k.063920", "hw": "moonies", "pos": "noun", "ipa": "/ˈmuːniz/", "vi": "tín đồ Giáo hội Thống nhất Moon"},
  {"id": "lex.en.200k.063921", "hw": "neuromas", "pos": "noun", "ipa": "/njʊˈroʊməz/", "vi": "khối u lành tính mô dây thần kinh"},
  {"id": "lex.en.200k.063922", "hw": "neuromata", "pos": "noun", "ipa": "/njʊˈroʊmətə/", "vi": "các khối u dây thần kinh ngoại biên"},
  {"id": "lex.en.200k.063923", "hw": "nicotianas", "pos": "noun", "ipa": "/nɪˌkoʊʃiˈeɪnəz/", "vi": "chi cây thuốc lá Nicotiana họ Cà"},
  {"id": "lex.en.200k.063924", "hw": "ninnies", "pos": "noun", "ipa": "/ˈnɪniz/", "vi": "kẻ khờ dại ngốc nghếch ngu ngơ"},
  {"id": "lex.en.200k.063925", "hw": "overflights", "pos": "noun", "ipa": "/ˈoʊvərflaɪts/", "vi": "chuyến bay ngang qua không phận"},
  {"id": "lex.en.200k.063926", "hw": "pallettes", "pos": "noun", "ipa": "/ˈpælɪts/", "vi": "tấm giáp tròn che nách bộ áo giáp"},
  {"id": "lex.en.200k.063927", "hw": "paracletes", "pos": "noun", "ipa": "/ˈpærəˌkliːts/", "vi": "Đấng An Ủi bảo trợ; người biện hộ"},
  {"id": "lex.en.200k.063928", "hw": "pentacles", "pos": "noun", "ipa": "/ˈpɛntəkəlz/", "vi": "bùa ngôi sao năm cánh huyền bí"},
  {"id": "lex.en.200k.063929", "hw": "permanganates", "pos": "noun", "ipa": "/pərˈmæŋɡəˌneɪts/", "vi": "muối pemanganat; chất thuốc tím"},
  {"id": "lex.en.200k.063930", "hw": "phials", "pos": "noun", "ipa": "/ˈfaɪəlz/", "vi": "ống lọ thủy tinh nhỏ đựng thuốc"},
  {"id": "lex.en.200k.063931", "hw": "pirandellos", "pos": "noun", "ipa": "/ˌpɪrənˈdɛloʊz/", "vi": "nhà viết kịch Nobel Ý Pirandello"},
  {"id": "lex.en.200k.063932", "hw": "pocketknives", "pos": "noun", "ipa": "/ˈpɑːkɪtnaɪvz/", "vi": "dao gấp nhỏ đa năng bỏ túi"},
  {"id": "lex.en.200k.063933", "hw": "prunellas", "pos": "noun", "ipa": "/pruˈnɛləz/", "vi": "cây thuốc hạ khô thảo; vải len chéo"},
  {"id": "lex.en.200k.063934", "hw": "psycholinguisticses", "pos": "noun", "ipa": "/ˌsaɪkoʊlɪŋˈɡwɪstɪksɪz/", "vi": "ngành tâm lý ngôn ngữ học"},
  {"id": "lex.en.200k.063935", "hw": "reformisms", "pos": "noun", "ipa": "/rɪˈfɔːrmɪzəmz/", "vi": "chủ nghĩa cải cách ôn hòa xã hội"},
  {"id": "lex.en.200k.063936", "hw": "reptilias", "pos": "noun", "ipa": "/rɛpˈtɪliəz/", "vi": "lớp động vật Bò sát Reptilia"},
  {"id": "lex.en.200k.063937", "hw": "rigmaroles", "pos": "noun", "ipa": "/ˈrɪɡməˌroʊlz/", "vi": "chuyện dài dòng lằng nhằng rắc rối"},
  {"id": "lex.en.200k.063938", "hw": "ripcords", "pos": "noun", "ipa": "/ˈrɪpkɔːrdz/", "vi": "dây giật bung mở túi dù nhảy"},
  {"id": "lex.en.200k.063939", "hw": "saddlebags", "pos": "noun", "ipa": "/ˈsædəlˌbæɡz/", "vi": "túi đeo hai bên yên ngựa hoặc xe"},
  {"id": "lex.en.200k.063940", "hw": "scalers", "pos": "noun", "ipa": "/ˈskeɪlərz/", "vi": "máy đếm xung; dụng cụ cạo cao răng"},
  {"id": "lex.en.200k.063941", "hw": "scousers", "pos": "noun", "ipa": "/ˈskaʊsərz/", "vi": "người dân gốc thành phố Liverpool"},
  {"id": "lex.en.200k.063942", "hw": "scroungers", "pos": "noun", "ipa": "/ˈskraʊndʒərz/", "vi": "kẻ ăn bám chực chờ xin xỏ vặt"},
  {"id": "lex.en.200k.063943", "hw": "semitones", "pos": "noun", "ipa": "/ˈsɛmiˌtoʊnz/", "vi": "nửa cung quãng cao độ âm nhạc"},
  {"id": "lex.en.200k.063944", "hw": "sgmls", "pos": "noun", "ipa": "/ˌɛsˌdʒiːˌɛmˈɛlz/", "vi": "ngôn ngữ đánh dấu chuẩn SGML"},
  {"id": "lex.en.200k.063945", "hw": "simenons", "pos": "noun", "ipa": "/sɪməˈnɔːnz/", "vi": "nhà văn trinh thám Georges Simenon"},
  {"id": "lex.en.200k.063946", "hw": "stagehands", "pos": "noun", "ipa": "/ˈsteɪdʒhændz/", "vi": "nhân viên hậu trường dựng sân khấu"},
  {"id": "lex.en.200k.063947", "hw": "stayers", "pos": "noun", "ipa": "/ˈsteɪərz/", "vi": "người bền bỉ trụ lại; ngựa bền sức"},
  {"id": "lex.en.200k.063948", "hw": "stockyards", "pos": "noun", "ipa": "/ˈstɑːkjɑːrdz/", "vi": "bãi tập trung gia súc chờ xuất bán"},
  {"id": "lex.en.200k.063949", "hw": "stroppier", "pos": "adj", "ipa": "/ˈstrɑːpiər/", "vi": "bướng bỉnh cáu kỉnh hay gây gổ hơn"},
  {"id": "lex.en.200k.063950", "hw": "stroppiest", "pos": "adj", "ipa": "/ˈstrɑːpiɪst/", "vi": "bướng bỉnh cáu kỉnh khó chịu nhất"},
  {"id": "lex.en.200k.063951", "hw": "styrons", "pos": "noun", "ipa": "/ˈstaɪrənz/", "vi": "tiểu thuyết gia Mỹ William Styron"},
  {"id": "lex.en.200k.063952", "hw": "subrogations", "pos": "noun", "ipa": "/ˌsʌbrəˈɡeɪʃənz/", "vi": "quyền thế quyền bảo hiểm pháp lý"},
  {"id": "lex.en.200k.063953", "hw": "suffragists", "pos": "noun", "ipa": "/ˈsʌfrədʒɪsts/", "vi": "người đấu tranh đòi quyền bầu cử"},
  {"id": "lex.en.200k.063954", "hw": "swards", "pos": "noun", "ipa": "/swɔːrdz/", "vi": "bãi thảm cỏ xanh mượt rộng lớn"},
  {"id": "lex.en.200k.063955", "hw": "tanagers", "pos": "noun", "ipa": "/ˈtænədʒərz/", "vi": "chim sẻ màu sắc sặc sỡ châu Mỹ"},
  {"id": "lex.en.200k.063956", "hw": "terengganus", "pos": "noun", "ipa": "/təˈrɛŋɡɑːnuːz/", "vi": "bang Terengganu miền đông Malaysia"},
  {"id": "lex.en.200k.063957", "hw": "thrombolyses", "pos": "noun", "ipa": "/θrɑːmˈbɑːləsiːz/", "vi": "quá trình làm tan cục máu đông"},
  {"id": "lex.en.200k.063958", "hw": "tiresiases", "pos": "noun", "ipa": "/taɪˈriːsiəsɪz/", "vi": "nhà tiên tri mù Hy Lạp cổ Tiresias"},
  {"id": "lex.en.200k.063959", "hw": "toeholds", "pos": "noun", "ipa": "/ˈtoʊhoʊldz/", "vi": "chỗ bám mũi chân; thế khóa cổ chân"},
  {"id": "lex.en.200k.063960", "hw": "trms", "pos": "noun", "ipa": "/ˌtiːˌɑːrˈɛmz/", "vi": "mô-đun thu phát TRM; chuẩn TRM"},
  {"id": "lex.en.200k.063961", "hw": "turndowns", "pos": "noun", "ipa": "/ˈtɜːrndaʊnz/", "vi": "sự từ chối thẳng; cổ áo bẻ gập"},
  {"id": "lex.en.200k.063962", "hw": "usshers", "pos": "noun", "ipa": "/ˈʌʃərz/", "vi": "tổng giám mục sử gia James Ussher"},
  {"id": "lex.en.200k.063963", "hw": "vaqueros", "pos": "noun", "ipa": "/vɑːˈkɛroʊz/", "vi": "cao bồi chăn gia súc Mỹ gốc Tây"},
  {"id": "lex.en.200k.063964", "hw": "viequeses", "pos": "noun", "ipa": "/viˈeɪkɛsɪz/", "vi": "đảo Vieques thuộc vùng Puerto Rico"},
  {"id": "lex.en.200k.063965", "hw": "virtus", "pos": "noun", "ipa": "/vɜːrˈtuːz/", "vi": "niềm đam mê sưu tầm đồ mỹ nghệ cổ"},
  {"id": "lex.en.200k.063966", "hw": "walesas", "pos": "noun", "ipa": "/vɑːˈwɛnsəz/", "vi": "tổng thống Ba Lan Nobel Lech Wałęsa"},
  {"id": "lex.en.200k.063967", "hw": "wrongdoers", "pos": "noun", "ipa": "/ˈrɔːŋˌduːərz/", "vi": "kẻ làm điều sai trái; kẻ phạm pháp"},
  {"id": "lex.en.200k.063968", "hw": "acetylsalicylic acid", "pos": "phrase", "ipa": "/əˌsiːtəlˌsælɪˈsɪlɪk ˈæsɪd/", "vi": "hoạt chất thuốc giảm đau aspirin"},
  {"id": "lex.en.200k.063969", "hw": "aksa martyrs brigades", "pos": "phrase", "ipa": "/ˈɑːksə ˈmɑːrtərz brɪˈɡeɪdz/", "vi": "nhóm vũ trang Lữ đoàn Al-Aqsa"},
  {"id": "lex.en.200k.063970", "hw": "american bog asphodel", "pos": "phrase", "ipa": "/əˈmɛrɪkən bɑːɡ ˈæsfəˌdɛl/", "vi": "cây hoa sao đầm lầy vàng Bắc Mỹ"},
  {"id": "lex.en.200k.063971", "hw": "anton pavlovich chekov", "pos": "phrase", "ipa": "/ˈɑːntɔːn ˈpɑːvləvɪtʃ ˈtʃɛkɔːf/", "vi": "đại văn hào truyện ngắn Nga Chekhov"},
  {"id": "lex.en.200k.063972", "hw": "bacillus anthracis", "pos": "phrase", "ipa": "/bəˈsɪləs ænˈθreɪsɪs/", "vi": "trực khuẩn gây bệnh nhiệt than"},
  {"id": "lex.en.200k.063973", "hw": "battle of ivry", "pos": "phrase", "ipa": "/ˈbætəl əv ˈiːvri/", "vi": "trận chiến Ivry năm 1590 ở Pháp"},
  {"id": "lex.en.200k.063974", "hw": "berberis canadensis", "pos": "phrase", "ipa": "/ˈbɜːrbərɪs ˌkænəˈdɛnsɪs/", "vi": "cây hoàng liên gai Bắc Mỹ thân nhỏ"},
  {"id": "lex.en.200k.063975", "hw": "blackcap raspberry", "pos": "phrase", "ipa": "/ˈblækkæp ˈræzˌbɛri/", "vi": "cây quả mâm xôi đen dại Bắc Mỹ"},
  {"id": "lex.en.200k.063976", "hw": "bog asphodel", "pos": "phrase", "ipa": "/bɑːɡ ˈæsfəˌdɛl/", "vi": "cây hoa sao vàng vùng đầm lầy"},
  {"id": "lex.en.200k.063977", "hw": "ciliated protozoan", "pos": "phrase", "ipa": "/ˈsɪliˌeɪtɪd ˌproʊtəˈzoʊən/", "vi": "động vật đơn bào có lông tiêm mao"},
  {"id": "lex.en.200k.063978", "hw": "common spoonbill", "pos": "phrase", "ipa": "/ˈkɑːmən ˈspuːnbɪl/", "vi": "chim cò mỏ thìa trắng Á-Âu"},
  {"id": "lex.en.200k.063979", "hw": "coronoid process", "pos": "phrase", "ipa": "/ˈkɔːrənɔɪd ˈprɑːsɛs/", "vi": "mỏm vẹt ở xương hàm dưới và trụ"},
  {"id": "lex.en.200k.063980", "hw": "duple time", "pos": "phrase", "ipa": "/ˈduːpəl taɪm/", "vi": "nhịp chẵn hai phách mỗi ô nhịp nhạc"},
  {"id": "lex.en.200k.063981", "hw": "european bog asphodel", "pos": "phrase", "ipa": "/ˌjʊrəˈpiːən bɑːɡ ˈæsfəˌdɛl/", "vi": "cây hoa sao vàng đầm lầy châu Âu"},
  {"id": "lex.en.200k.063982", "hw": "family rosaceae", "pos": "phrase", "ipa": "/ˈfæməli roʊˈzeɪʃiˌiː/", "vi": "họ thực vật Hoa hồng Rosaceae"},
  {"id": "lex.en.200k.063983", "hw": "family solanaceae", "pos": "phrase", "ipa": "/ˈfæməli ˌsoʊləˈneɪʃiˌiː/", "vi": "họ thực vật Cà Solanaceae"},
  {"id": "lex.en.200k.063984", "hw": "fast of gedaliah", "pos": "phrase", "ipa": "/fæst əv ɡəˈdɑːljə/", "vi": "ngày lễ ăn chay Gedaliah Do Thái"},
  {"id": "lex.en.200k.063985", "hw": "fast of tammuz", "pos": "phrase", "ipa": "/fæst əv ˈtæmuːz/", "vi": "ngày ăn chay tháng Tammuz Do Thái"},
  {"id": "lex.en.200k.063986", "hw": "fibular vein", "pos": "phrase", "ipa": "/ˈfɪbjələr veɪn/", "vi": "tĩnh mạch mác sâu vùng cẳng chân"},
  {"id": "lex.en.200k.063987", "hw": "geniculate body", "pos": "phrase", "ipa": "/dʒəˈnɪkjəlɪt ˈbɑːdi/", "vi": "thể gối đồi thị xử lý thị thính"},
  {"id": "lex.en.200k.063988", "hw": "genus drosera", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈdrɑːsərə/", "vi": "chi cây ăn thịt bắt mồi Gọng vó"},
  {"id": "lex.en.200k.063989", "hw": "genus fringilla", "pos": "phrase", "ipa": "/ˈdʒiːnəs frɪŋˈɡɪlə/", "vi": "chi chim sẻ đồng Fringilla châu Âu"},
  {"id": "lex.en.200k.063990", "hw": "genus ipomoea", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌaɪpəˈmiːə/", "vi": "chi dây bìm bìm khoai lang Ipomoea"},
  {"id": "lex.en.200k.063991", "hw": "genus juncus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈdʒʌŋkəs/", "vi": "chi cây cói bấc làm bấc đèn Juncus"},
  {"id": "lex.en.200k.063992", "hw": "genus oxalis", "pos": "phrase", "ipa": "/ˈdʒiːnəs ɑːkˈseɪlɪs/", "vi": "chi cây chua me đất lá kép Oxalis"},
  {"id": "lex.en.200k.063993", "hw": "genus papaver", "pos": "phrase", "ipa": "/ˈdʒiːnəs pəˈpeɪvər/", "vi": "chi cây hoa anh túc mỹ lệ Papaver"},
  {"id": "lex.en.200k.063994", "hw": "genus phragmites", "pos": "phrase", "ipa": "/ˈdʒiːnəs fræɡˈmaɪtiːz/", "vi": "chi cây lau sậy cao mọc đầm lầy"},
  {"id": "lex.en.200k.063995", "hw": "genus sarda", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈsɑːrdə/", "vi": "chi cá ngừ đại dương Sarda"},
  {"id": "lex.en.200k.063996", "hw": "genus scilla", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈsɪlə/", "vi": "chi hoa chuông xanh hành củ Scilla"},
  {"id": "lex.en.200k.063997", "hw": "genus spartina", "pos": "phrase", "ipa": "/ˈdʒiːnəs spɑːrˈtaɪnə/", "vi": "chi cỏ đầm lầy ngập mặn Spartina"},
  {"id": "lex.en.200k.063998", "hw": "genus tilia", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈtɪliə/", "vi": "chi cây gỗ đoạn hoa thơm Tilia"},
  {"id": "lex.en.200k.063999", "hw": "george gamow", "pos": "phrase", "ipa": "/dʒɔːrdʒ ˈɡæmɑːf/", "vi": "nhà vật lý vũ trụ học George Gamow"},
  {"id": "lex.en.200k.064000", "hw": "hypoplastic anaemia", "pos": "phrase", "ipa": "/ˌhaɪpəˈplæstɪk əˈniːmiə/", "vi": "thiếu máu giảm sản tủy xương (Anh)"},
  {"id": "lex.en.200k.064001", "hw": "ilex glabra", "pos": "phrase", "ipa": "/ˈaɪlɛks ˈɡleɪbrə/", "vi": "cây nhựa ruồi quả đen Bắc Mỹ"},
  {"id": "lex.en.200k.064002", "hw": "inter vivos trust", "pos": "phrase", "ipa": "/ˌɪntər ˈvaɪvoʊz trʌst/", "vi": "quỹ tín thác lập khi còn sống"}
]

with open('scratch/b33_r08_raw_p5.json') as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100

for i, (item, r) in enumerate(zip(items, raw)):
    assert item['id'] == r['id'], f"Mismatch id at {i}: {item['id']} vs {r['id']}"
    assert item['hw'] == r['hw'], f"Mismatch hw at {i}: {item['hw']} vs {r['hw']}"
    assert len(item['vi']) <= 35, f"vi length > 35 at {i} ({item['hw']}): {len(item['vi'])}"
    assert item['pos'] in ['noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase'], f"Invalid pos at {i}: {item['pos']}"
    assert item['ipa'].startswith('/') and item['ipa'].endswith('/') and item['ipa'].count('/') == 2, f"Invalid ipa at {i}: {item['ipa']}"
    assert not item['ipa'][1:-1].startswith(' ') and not item['ipa'][1:-1].endswith(' '), f"Space in ipa at {i}: {item['ipa']}"
    r['pos'] = item['pos']
    r['ipa'] = item['ipa']
    r['vi'] = item['vi']
    r['status'] = 'reviewed'

with open('scratch/b33_r08_p5.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)
print("Saved scratch/b33_r08_p5.json OK")
