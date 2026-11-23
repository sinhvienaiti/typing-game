import json

items = [
  {"id": "lex.en.200k.062403", "hw": "thermic fever", "pos": "phrase", "ipa": "/ˈθɜːrmɪk ˈfiːvər/", "vi": "chứng say nắng; sốc nhiệt độ cao"},
  {"id": "lex.en.200k.062404", "hw": "true puffball", "pos": "phrase", "ipa": "/truː ˈpʌfbɔːl/", "vi": "nấm trứng tròn trắng mọc đồng cỏ"},
  {"id": "lex.en.200k.062405", "hw": "vicia sativa", "pos": "phrase", "ipa": "/ˈvɪʃə səˈtaɪvə/", "vi": "cây đậu tằm trồng làm phân xanh"},
  {"id": "lex.en.200k.062406", "hw": "vitis vinifera", "pos": "phrase", "ipa": "/ˈvaɪtɪs vɪˈnɪfərə/", "vi": "cây nho làm rượu vang châu Âu"},
  {"id": "lex.en.200k.062407", "hw": "wankel engine", "pos": "phrase", "ipa": "/ˈvɑːŋkl ˈɛndʒɪn/", "vi": "động cơ quay rô-to tam giác Wankel"},
  {"id": "lex.en.200k.062408", "hw": "wastepaper basket", "pos": "phrase", "ipa": "/ˈweɪstpeɪpər ˈbæskɪt/", "vi": "giỏ đựng giấy loại; sọt rác giấy"},
  {"id": "lex.en.200k.062409", "hw": "whited sepulchre", "pos": "phrase", "ipa": "/ˈwaɪtɪd ˈsɛpəlkər/", "vi": "kẻ đạo đức giả ngoài đẹp trong xấu"},
  {"id": "lex.en.200k.062410", "hw": "wilkins micawber", "pos": "phrase", "ipa": "/ˈwɪlkɪnz mɪˈkɔːbər/", "vi": "nhân vật lạc quan tếu Micawber"},
  {"id": "lex.en.200k.062411", "hw": "acrylonitriles", "pos": "noun", "ipa": "/ˌækrɪloʊˈnaɪtrɪlz/", "vi": "hợp chất hóa học tạo sợi tổng hợp"},
  {"id": "lex.en.200k.062412", "hw": "admonishments", "pos": "noun", "ipa": "/ædˈmɑːnɪʃmənts/", "vi": "lời khuyên răn; lời quở trách nhẹ"},
  {"id": "lex.en.200k.062413", "hw": "aldebarans", "pos": "noun", "ipa": "/ælˈdɛbərənz/", "vi": "ngôi sao khổng lồ đỏ Aldebaran"},
  {"id": "lex.en.200k.062414", "hw": "anthills", "pos": "noun", "ipa": "/ˈænthɪlz/", "vi": "ụ đất tổ kiến đùn lên mặt đất"},
  {"id": "lex.en.200k.062415", "hw": "banksias", "pos": "noun", "ipa": "/ˈbæŋksiəz/", "vi": "cây bụi hoa nụ chùm banksia Úc"},
  {"id": "lex.en.200k.062416", "hw": "berias", "pos": "noun", "ipa": "/ˈbɛriəz/", "vi": "lãnh đạo mật vụ Liên Xô Beria"},
  {"id": "lex.en.200k.062417", "hw": "bipeds", "pos": "noun", "ipa": "/ˈbaɪpɛdz/", "vi": "loài động vật đi bằng hai chân"},
  {"id": "lex.en.200k.062418", "hw": "blastocysts", "pos": "noun", "ipa": "/ˈblæstəsɪsts/", "vi": "phôi nang giai đoạn sớm làm tổ"},
  {"id": "lex.en.200k.062419", "hw": "boffins", "pos": "noun", "ipa": "/ˈbɑːfɪnz/", "vi": "nhà khoa học nghiên cứu (lóng Anh)"},
  {"id": "lex.en.200k.062420", "hw": "calendulas", "pos": "noun", "ipa": "/kəˈlɛndjʊləz/", "vi": "cây hoa cúc xu xi vàng dược liệu"},
  {"id": "lex.en.200k.062421", "hw": "cassowaries", "pos": "noun", "ipa": "/ˈkæsəwɛriz/", "vi": "loài chim đà điểu đầu mào hung dữ"},
  {"id": "lex.en.200k.062422", "hw": "cattells", "pos": "noun", "ipa": "/kəˈtɛlz/", "vi": "nhà tâm lý học James Cattell Mỹ"},
  {"id": "lex.en.200k.062423", "hw": "cetuses", "pos": "noun", "ipa": "/ˈsiːtəsɪz/", "vi": "chòm sao Kình Ngư bầu trời đêm"},
  {"id": "lex.en.200k.062424", "hw": "chawed", "pos": "verb", "ipa": "/tʃɔːd/", "vi": "đã nhai tóp tép (thuốc lá sợi)"},
  {"id": "lex.en.200k.062425", "hw": "chawing", "pos": "verb", "ipa": "/ˈtʃɔːɪŋ/", "vi": "đang nhai tóp tép trầu thuốc lá"},
  {"id": "lex.en.200k.062426", "hw": "chaws", "pos": "noun", "ipa": "/tʃɔːz/", "vi": "miếng thuốc lá nhai; cú nhai ngấu"},
  {"id": "lex.en.200k.062427", "hw": "chlorellas", "pos": "noun", "ipa": "/kləˈrɛləz/", "vi": "vi tảo lục đơn bào giàu đạm"},
  {"id": "lex.en.200k.062428", "hw": "cichlids", "pos": "noun", "ipa": "/ˈsɪklɪdz/", "vi": "họ cá hoàng đế cá rô phi sặc sỡ"},
  {"id": "lex.en.200k.062429", "hw": "cjds", "pos": "noun", "ipa": "/siː dʒeɪ diːz/", "vi": "bệnh thoái hóa não bò điên CJD"},
  {"id": "lex.en.200k.062430", "hw": "coiffured", "pos": "verb", "ipa": "/kwɑːˈfjʊərd/", "vi": "đã chải bới tạo kiểu tóc cầu kỳ"},
  {"id": "lex.en.200k.062431", "hw": "coiffures", "pos": "noun", "ipa": "/kwɑːˈfjʊərz/", "vi": "kiểu đầu tóc chải bới công phu"},
  {"id": "lex.en.200k.062432", "hw": "coiffuring", "pos": "verb", "ipa": "/kwɑːˈfjʊərɪŋ/", "vi": "đang chải vấn tạo kiểu tóc sang"},
  {"id": "lex.en.200k.062433", "hw": "compressibilities", "pos": "noun", "ipa": "/kəmˌprɛsəˈbɪlətiz/", "vi": "tính chịu nén; hệ số nén chất khí"},
  {"id": "lex.en.200k.062434", "hw": "contortions", "pos": "noun", "ipa": "/kənˈtɔːrʃənz/", "vi": "sự vặn xoắn méo mó; sự xuyên tạc"},
  {"id": "lex.en.200k.062435", "hw": "counterpunches", "pos": "noun", "ipa": "/ˈkaʊntərpʌntʃɪz/", "vi": "cú đấm phản công; lời đáp trả sắc"},
  {"id": "lex.en.200k.062436", "hw": "counterstriked", "pos": "verb", "ipa": "/ˌkaʊntərˈstraɪkt/", "vi": "đã tung đòn phản công đánh trả"},
  {"id": "lex.en.200k.062437", "hw": "counterstrikes", "pos": "verb", "ipa": "/ˈkaʊntərstraɪks/", "vi": "tung đòn đánh trả phản công mạnh"},
  {"id": "lex.en.200k.062438", "hw": "counterstriking", "pos": "verb", "ipa": "/ˈkaʊntərstraɪkɪŋ/", "vi": "đang giáng đòn phản công lại"},
  {"id": "lex.en.200k.062439", "hw": "criminalised", "pos": "verb", "ipa": "/ˈkrɪmɪnəlaɪzd/", "vi": "đã hình sự hóa quy kết phạm tội"},
  {"id": "lex.en.200k.062440", "hw": "criminalises", "pos": "verb", "ipa": "/ˈkrɪmɪnəlaɪzɪz/", "vi": "hình sự hóa hành vi phạm luật"},
  {"id": "lex.en.200k.062441", "hw": "criminalising", "pos": "verb", "ipa": "/ˈkrɪmɪnəlaɪzɪŋ/", "vi": "đang hình sự hóa; coi là phạm tội"},
  {"id": "lex.en.200k.062442", "hw": "cryptologies", "pos": "noun", "ipa": "/krɪpˈtɑːlədʒiz/", "vi": "khoa học mật mã và giải mã tin"},
  {"id": "lex.en.200k.062443", "hw": "dendrites", "pos": "noun", "ipa": "/ˈdɛndraɪts/", "vi": "sợi nhánh nơ-ron; tinh thể nhánh"},
  {"id": "lex.en.200k.062444", "hw": "downswings", "pos": "noun", "ipa": "/ˈdaʊnswɪŋz/", "vi": "giai đoạn suy giảm; cú vung xuống"},
  {"id": "lex.en.200k.062445", "hw": "emotionalities", "pos": "noun", "ipa": "/ɪˌmoʊʃəˈnælətiz/", "vi": "trạng thái dễ xúc động cảm tính"},
  {"id": "lex.en.200k.062446", "hw": "enthronements", "pos": "noun", "ipa": "/ɪnˈθroʊnmənts/", "vi": "nghi lễ đăng quang lên ngôi vua"},
  {"id": "lex.en.200k.062447", "hw": "estruses", "pos": "noun", "ipa": "/ˈɛstrəsɪz/", "vi": "chu kỳ động dục sinh sản ở thú"},
  {"id": "lex.en.200k.062448", "hw": "fados", "pos": "noun", "ipa": "/ˈfɑːdoʊz/", "vi": "nhạc buồn dân gian fado Bồ Đào Nha"},
  {"id": "lex.en.200k.062449", "hw": "fantasists", "pos": "noun", "ipa": "/ˈfæntəsɪsts/", "vi": "người ảo tưởng; tác giả kỳ ảo"},
  {"id": "lex.en.200k.062450", "hw": "fieldstones", "pos": "noun", "ipa": "/ˈfiːldstoʊnz/", "vi": "đá cuội tự nhiên nhặt trên đồng"},
  {"id": "lex.en.200k.062451", "hw": "flagons", "pos": "noun", "ipa": "/ˈflæɡənz/", "vi": "bình cổ hẹp có quai rót rượu vang"},
  {"id": "lex.en.200k.062452", "hw": "forbears", "pos": "noun", "ipa": "/ˈfɔːrbɛərz/", "vi": "ông bà tổ tiên các thế hệ trước"},
  {"id": "lex.en.200k.062453", "hw": "frontiersmen", "pos": "noun", "ipa": "/frʌnˈtɪərzmən/", "vi": "người khai phá vùng biên cương"},
  {"id": "lex.en.200k.062454", "hw": "gasconies", "pos": "noun", "ipa": "/ˈɡæskəniz/", "vi": "xứ Gascony cổ miền tây nam Pháp"},
  {"id": "lex.en.200k.062455", "hw": "granulomata", "pos": "noun", "ipa": "/ˌɡrænjʊˈloʊmətə/", "vi": "các nốt u hạt viêm mô mạn tính"},
  {"id": "lex.en.200k.062456", "hw": "grottier", "pos": "adj", "ipa": "/ˈɡrɑːtiər/", "vi": "dơ bẩn tồi tàn hơn; tồi tệ hơn"},
  {"id": "lex.en.200k.062457", "hw": "grottiest", "pos": "adj", "ipa": "/ˈɡrɑːtiɪst/", "vi": "bẩn thỉu tồi tàn nhất; tệ hại nhất"},
  {"id": "lex.en.200k.062458", "hw": "guffawed", "pos": "verb", "ipa": "/ɡəˈfɔːd/", "vi": "đã cười ha hả ồn ào khoái trá"},
  {"id": "lex.en.200k.062459", "hw": "guffawing", "pos": "verb", "ipa": "/ɡəˈfɔːɪŋ/", "vi": "đang cười phá lên ha hả vang rền"},
  {"id": "lex.en.200k.062460", "hw": "guffaws", "pos": "noun", "ipa": "/ɡəˈfɔːz/", "vi": "tràng cười ha hả sảng khoái ồn ào"},
  {"id": "lex.en.200k.062461", "hw": "guzzlers", "pos": "noun", "ipa": "/ˈɡʌzlərz/", "vi": "kẻ nốc rượu say sưa; xe ngốn xăng"},
  {"id": "lex.en.200k.062462", "hw": "headwaters", "pos": "noun", "ipa": "/ˈhɛdwɔːtərz/", "vi": "vùng đầu nguồn khởi phát dòng sông"},
  {"id": "lex.en.200k.062463", "hw": "housatonics", "pos": "noun", "ipa": "/ˌhaʊsəˈtɑːnɪks/", "vi": "sông Housatonic miền Đông Bắc Mỹ"},
  {"id": "lex.en.200k.062464", "hw": "housefuls", "pos": "noun", "ipa": "/ˈhaʊsfʊlz/", "vi": "lượng người đồ vật chật kín cả nhà"},
  {"id": "lex.en.200k.062465", "hw": "immunoassays", "pos": "noun", "ipa": "/ˌɪmjʊnoʊˈæseɪz/", "vi": "xét nghiệm định lượng miễn dịch"},
  {"id": "lex.en.200k.062466", "hw": "immunogenicities", "pos": "noun", "ipa": "/ɪˌmjuːnoʊdʒəˈnɪsətiz/", "vi": "tính sinh đáp ứng miễn dịch học"},
  {"id": "lex.en.200k.062467", "hw": "intermezzos", "pos": "noun", "ipa": "/ˌɪntərˈmɛtsoʊz/", "vi": "khúc nhạc xen ngắn giữa hồi kịch"},
  {"id": "lex.en.200k.062468", "hw": "jabberwockies", "pos": "noun", "ipa": "/ˈdʒæbərwɑːkiz/", "vi": "lời nói nhảm vô nghĩa; quái vật thơ"},
  {"id": "lex.en.200k.062469", "hw": "jatis", "pos": "noun", "ipa": "/ˈdʒɑːtiz/", "vi": "hệ thống phân chia đẳng cấp jati Ấn"},
  {"id": "lex.en.200k.062470", "hw": "kobs", "pos": "noun", "ipa": "/kɑːbz/", "vi": "loài linh dương nước Kob châu Phi"},
  {"id": "lex.en.200k.062471", "hw": "ladinos", "pos": "noun", "ipa": "/ləˈdiːnoʊz/", "vi": "người nói tiếng Do Thái Tây Ban Nha"},
  {"id": "lex.en.200k.062472", "hw": "laundresses", "pos": "noun", "ipa": "/ˈlɔːndrəsɪz/", "vi": "cô thợ giặt giũ quần áo thuê"},
  {"id": "lex.en.200k.062473", "hw": "levodopas", "pos": "noun", "ipa": "/ˌlɛvəˈdoʊpəz/", "vi": "thuốc điều trị Parkinson levodopa"},
  {"id": "lex.en.200k.062474", "hw": "lingams", "pos": "noun", "ipa": "/ˈlɪŋɡəmz/", "vi": "tượng thờ thần Shiva Linga Ấn Độ"},
  {"id": "lex.en.200k.062475", "hw": "linkups", "pos": "noun", "ipa": "/ˈlɪŋkʌps/", "vi": "sự liên kết nối mạng; buổi hẹn gặp"},
  {"id": "lex.en.200k.062476", "hw": "lirs", "pos": "noun", "ipa": "/lɪərz/", "vi": "thần biển Lir thần thoại Ireland"},
  {"id": "lex.en.200k.062477", "hw": "llds", "pos": "noun", "ipa": "/ɛl ɛl diːz/", "vi": "học vị Tiến sĩ Luật danh dự LL.D"},
  {"id": "lex.en.200k.062478", "hw": "mandamuses", "pos": "noun", "ipa": "/mænˈdeɪməsɪz/", "vi": "án lệnh tòa buộc quan chức thi hành"},
  {"id": "lex.en.200k.062479", "hw": "matchbooks", "pos": "noun", "ipa": "/ˈmætʃbʊks/", "vi": "tệp diêm giấy gấp nắp quảng cáo"},
  {"id": "lex.en.200k.062480", "hw": "meccanos", "pos": "noun", "ipa": "/məˈkɑːnoʊz/", "vi": "bộ đồ chơi lắp ghép cơ khí Meccano"},
  {"id": "lex.en.200k.062481", "hw": "millikans", "pos": "noun", "ipa": "/ˈmɪlɪkənz/", "vi": "nhà vật lý Nobel Robert Millikan"},
  {"id": "lex.en.200k.062482", "hw": "millwrights", "pos": "noun", "ipa": "/ˈmɪlraɪts/", "vi": "thợ cơ khí lắp đặt bảo trì cối xay"},
  {"id": "lex.en.200k.062483", "hw": "mixologists", "pos": "noun", "ipa": "/mɪkˈsɑːlədʒɪsts/", "vi": "nghệ nhân pha chế rượu cocktail"},
  {"id": "lex.en.200k.062484", "hw": "mousier", "pos": "adj", "ipa": "/ˈmaʊsiər/", "vi": "rụt rè nhút nhát hơn; xám xịt hơn"},
  {"id": "lex.en.200k.062485", "hw": "mousiest", "pos": "adj", "ipa": "/ˈmaʊsiɪst/", "vi": "nhút nhát nhất; xám xịt nhạt nhất"},
  {"id": "lex.en.200k.062486", "hw": "nebulizers", "pos": "noun", "ipa": "/ˈnɛbjʊlaɪzərz/", "vi": "máy xông khí dung phun sương y tế"},
  {"id": "lex.en.200k.062487", "hw": "ologies", "pos": "noun", "ipa": "/ˈɑːlədʒiz/", "vi": "các bộ môn khoa học (lối nói đùa)"},
  {"id": "lex.en.200k.062488", "hw": "parisiennes", "pos": "noun", "ipa": "/pəˌriːziˈɛnz/", "vi": "phụ nữ quý cô thành phố Paris"},
  {"id": "lex.en.200k.062489", "hw": "parrotfishes", "pos": "noun", "ipa": "/ˈpærətfɪʃɪz/", "vi": "loài cá mó biển mỏ giống mỏ vẹt"},
  {"id": "lex.en.200k.062490", "hw": "pegboards", "pos": "noun", "ipa": "/ˈpɛɡbɔːrdz/", "vi": "tấm bảng đục lỗ cài chốt treo đồ"},
  {"id": "lex.en.200k.062491", "hw": "philanderers", "pos": "noun", "ipa": "/fɪˈlændərərz/", "vi": "gã đàn ông lăng nhăng trăng hoa"},
  {"id": "lex.en.200k.062492", "hw": "pietas", "pos": "noun", "ipa": "/piˈeɪtɑːz/", "vi": "tượng Đức Mẹ sầu bi ôm xác Chúa"},
  {"id": "lex.en.200k.062493", "hw": "plutons", "pos": "noun", "ipa": "/ˈpluːtɑːnz/", "vi": "khối đá macma xâm nhập dưới sâu đất"},
  {"id": "lex.en.200k.062494", "hw": "poetesses", "pos": "noun", "ipa": "/ˈpoʊətəsɪz/", "vi": "nữ thi sĩ; nữ nhà thơ sáng tác"},
  {"id": "lex.en.200k.062495", "hw": "polecats", "pos": "noun", "ipa": "/ˈpoʊlkæts/", "vi": "loài chồn hôi châu Âu; chồn marten"},
  {"id": "lex.en.200k.062496", "hw": "presbyterianisms", "pos": "noun", "ipa": "/ˌprɛzbɪˈtɪriənɪzəmz/", "vi": "hệ phái Tin Lành Trưởng Lão giáo"},
  {"id": "lex.en.200k.062497", "hw": "promethazines", "pos": "noun", "ipa": "/proʊˈmɛθəziːnz/", "vi": "thuốc kháng dị ứng buồn nôn ngủ"},
  {"id": "lex.en.200k.062498", "hw": "provencals", "pos": "noun", "ipa": "/ˌprɑːvənˈsɑːlz/", "vi": "người dân hoặc tiếng vùng Provence"},
  {"id": "lex.en.200k.062499", "hw": "proveras", "pos": "noun", "ipa": "/proʊˈvɛrəz/", "vi": "thuốc nội tiết tố nữ Provera"},
  {"id": "lex.en.200k.062500", "hw": "pyrimidines", "pos": "noun", "ipa": "/paɪˈrɪmədiːnz/", "vi": "hợp chất vòng nitơ bazơ pyrimidine"},
  {"id": "lex.en.200k.062501", "hw": "quadrupeds", "pos": "noun", "ipa": "/ˈkwɑːdrəpɛdz/", "vi": "loài động vật đi bằng bốn chân"},
  {"id": "lex.en.200k.062502", "hw": "quarterdecks", "pos": "noun", "ipa": "/ˈkwɔːrtərdɛks/", "vi": "boong sau đuôi tàu dành cho sĩ quan"}
]

with open('scratch/b33_r05_raw_p5.json') as f:
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

with open('scratch/b33_r05_p5.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Batch 33 Round 5 Part 5 validated and written successfully.")
