import json

items = [
  {"id": "lex.en.200k.060703", "hw": "ahimsas", "pos": "noun", "ipa": "/əˈhɪmsəz/", "vi": "triết lý bất bạo động ahimsa"},
  {"id": "lex.en.200k.060704", "hw": "aileys", "pos": "noun", "ipa": "/ˈeɪliz/", "vi": "biên đạo múa Mỹ Alvin Ailey"},
  {"id": "lex.en.200k.060705", "hw": "alprazolams", "pos": "noun", "ipa": "/ælˈpræzəlæmz/", "vi": "thuốc an thần trị lo âu alprazolam"},
  {"id": "lex.en.200k.060706", "hw": "anticonvulsants", "pos": "noun", "ipa": "/ˌæntikənˈvʌlsənts/", "vi": "thuốc chống co giật động kinh"},
  {"id": "lex.en.200k.060707", "hw": "apennineses", "pos": "noun", "ipa": "/ˌæpəˈnaɪnzɪz/", "vi": "dãy núi xương sống Apennine Ý"},
  {"id": "lex.en.200k.060708", "hw": "arcturuses", "pos": "noun", "ipa": "/ɑːrkˈtʊərəsɪz/", "vi": "ngôi sao khổng lồ đỏ Arcturus"},
  {"id": "lex.en.200k.060709", "hw": "arminians", "pos": "noun", "ipa": "/ɑːrˈmɪniənz/", "vi": "tín đồ phái thần học Arminius"},
  {"id": "lex.en.200k.060710", "hw": "asmaras", "pos": "noun", "ipa": "/æzˈmɑːrəz/", "vi": "thủ đô Asmara của nước Eritrea"},
  {"id": "lex.en.200k.060711", "hw": "athelstans", "pos": "noun", "ipa": "/ˈæθəlstənz/", "vi": "quốc vương Anh Athelstan cổ đại"},
  {"id": "lex.en.200k.060712", "hw": "atreuses", "pos": "noun", "ipa": "/ˈeɪtriəsɪz/", "vi": "vua Atreus trong thần thoại Hy Lạp"},
  {"id": "lex.en.200k.060713", "hw": "bacteriologists", "pos": "noun", "ipa": "/bækˌtɪriˈɑːlədʒɪsts/", "vi": "nhà nghiên cứu vi khuẩn học"},
  {"id": "lex.en.200k.060714", "hw": "bazillions", "pos": "noun", "ipa": "/bəˈzɪljənz/", "vi": "vô vàn vô số kể; hàng tỷ tỷ"},
  {"id": "lex.en.200k.060715", "hw": "bioremediations", "pos": "noun", "ipa": "/ˌbaɪoʊrɪˌmiːdiˈeɪʃənz/", "vi": "xử lý môi trường bằng sinh học"},
  {"id": "lex.en.200k.060716", "hw": "birred", "pos": "verb", "ipa": "/bɜːrd/", "vi": "đã kêu vù vù; rít lên lanh lảnh"},
  {"id": "lex.en.200k.060717", "hw": "birring", "pos": "verb", "ipa": "/ˈbɜːrɪŋ/", "vi": "đang kêu vù vù; phát tiếng rít gió"},
  {"id": "lex.en.200k.060718", "hw": "birrs", "pos": "noun", "ipa": "/bɜːrz/", "vi": "tiền tệ Ethiopia; lực đẩy vù vù"},
  {"id": "lex.en.200k.060719", "hw": "bismarks", "pos": "noun", "ipa": "/ˈbɪzmɑːrks/", "vi": "bánh rán nhân mứt ngọt Bismarck"},
  {"id": "lex.en.200k.060720", "hw": "blunderbusses", "pos": "noun", "ipa": "/ˈblʌndərbʌsɪz/", "vi": "súng kíp cổ họng loe; kẻ vụng về"},
  {"id": "lex.en.200k.060721", "hw": "borstals", "pos": "noun", "ipa": "/ˈbɔːrstlz/", "vi": "trại giáo dưỡng cải tạo thiếu niên"},
  {"id": "lex.en.200k.060722", "hw": "calligraphers", "pos": "noun", "ipa": "/kəˈlɪɡrəfərz/", "vi": "nghệ nhân viết chữ đẹp thư pháp"},
  {"id": "lex.en.200k.060723", "hw": "cannibalized", "pos": "verb", "ipa": "/ˈkænəbəlaɪzd/", "vi": "đã ăn thịt đồng loại; tháo đồ dùng"},
  {"id": "lex.en.200k.060724", "hw": "cannibalizes", "pos": "verb", "ipa": "/ˈkænəbəlaɪzɪz/", "vi": "ăn thịt đồng loại; tháo tận dụng"},
  {"id": "lex.en.200k.060725", "hw": "cannibalizing", "pos": "verb", "ipa": "/ˈkænəbəlaɪzɪŋ/", "vi": "đang ăn thịt đồng loại; tháo lấy đồ"},
  {"id": "lex.en.200k.060726", "hw": "cauls", "pos": "noun", "ipa": "/kɔːlz/", "vi": "màng ối bọc đầu; màng mỡ bụng"},
  {"id": "lex.en.200k.060727", "hw": "chukkas", "pos": "noun", "ipa": "/ˈtʃʌkəz/", "vi": "hiệp đấu polo; bốt da lộn cổ lửng"},
  {"id": "lex.en.200k.060728", "hw": "ciprofloxacins", "pos": "noun", "ipa": "/ˌsɪproʊˈflɑːksəsɪnz/", "vi": "thuốc kháng sinh ciprofloxacin"},
  {"id": "lex.en.200k.060729", "hw": "compartmentalizes", "pos": "verb", "ipa": "/kəmˌpɑːrtˈmɛntəlaɪzɪz/", "vi": "chia thành từng ngăn; tách biệt rõ"},
  {"id": "lex.en.200k.060730", "hw": "compartmentalizing", "pos": "verb", "ipa": "/kəmˌpɑːrtˈmɛntəlaɪzɪŋ/", "vi": "đang chia ngăn; tách biệt cảm xúc"},
  {"id": "lex.en.200k.060731", "hw": "condorcets", "pos": "noun", "ipa": "/kɔːndɔːrˈseɪz/", "vi": "triết gia Khai sáng Condorcet Pháp"},
  {"id": "lex.en.200k.060732", "hw": "congreves", "pos": "noun", "ipa": "/ˈkɑːŋɡriːvz/", "vi": "nhà soạn kịch Anh William Congreve"},
  {"id": "lex.en.200k.060733", "hw": "cotillions", "pos": "noun", "ipa": "/kəˈtɪljənz/", "vi": "vũ điệu tập thể cổ; dạ hội ra mắt"},
  {"id": "lex.en.200k.060734", "hw": "courbets", "pos": "noun", "ipa": "/kʊərˈbeɪz/", "vi": "họa sĩ hiện thực Gustave Courbet"},
  {"id": "lex.en.200k.060735", "hw": "crookeses", "pos": "noun", "ipa": "/ˈkrʊksɪz/", "vi": "nhà vật lý hóa học William Crookes"},
  {"id": "lex.en.200k.060736", "hw": "crumpets", "pos": "noun", "ipa": "/ˈkrʌmpɪts/", "vi": "bánh nướng xốp nhiều lỗ tổ ong Anh"},
  {"id": "lex.en.200k.060737", "hw": "cycladeses", "pos": "noun", "ipa": "/ˈsɪklədiːzɪz/", "vi": "nền văn minh đảo Cyclades Hy Lạp"},
  {"id": "lex.en.200k.060738", "hw": "damascened", "pos": "verb", "ipa": "/ˈdæməsiːnd/", "vi": "đã khảm vàng bạc lên thép rèn"},
  {"id": "lex.en.200k.060739", "hw": "damascenes", "pos": "noun", "ipa": "/ˈdæməsiːnz/", "vi": "người dân thành phố Damascus"},
  {"id": "lex.en.200k.060740", "hw": "damascening", "pos": "verb", "ipa": "/ˈdæməsiːnɪŋ/", "vi": "đang khảm vàng bạc lên kim loại"},
  {"id": "lex.en.200k.060741", "hw": "decoctions", "pos": "noun", "ipa": "/dɪˈkɑːkʃənz/", "vi": "nước thuốc sắc từ thảo mộc cô đặc"},
  {"id": "lex.en.200k.060742", "hw": "diatoms", "pos": "noun", "ipa": "/ˈdaɪətɑːmz/", "vi": "tảo khuê đơn bào có vỏ silic"},
  {"id": "lex.en.200k.060743", "hw": "eigens", "pos": "noun", "ipa": "/ˈaɪɡənz/", "vi": "nhà hóa học Nobel Manfred Eigen"},
  {"id": "lex.en.200k.060744", "hw": "emptors", "pos": "noun", "ipa": "/ˈɛmptɔːrz/", "vi": "người mua hàng; khách mua tài sản"},
  {"id": "lex.en.200k.060745", "hw": "erythrocytes", "pos": "noun", "ipa": "/ɪˈrɪθrəsaɪts/", "vi": "tế bào hồng cầu mang oxy trong máu"},
  {"id": "lex.en.200k.060746", "hw": "etrurias", "pos": "noun", "ipa": "/ɪˈtrʊəriəz/", "vi": "vùng đất Etruria cổ đại ở nước Ý"},
  {"id": "lex.en.200k.060747", "hw": "eurythmicses", "pos": "noun", "ipa": "/jʊˈrɪðmɪksɪz/", "vi": "nghệ thuật nhịp điệu cơ thể âm nhạc"},
  {"id": "lex.en.200k.060748", "hw": "fallas", "pos": "noun", "ipa": "/ˈfɑːjəz/", "vi": "nhạc sĩ Tây Ban Nha Manuel de Falla"},
  {"id": "lex.en.200k.060749", "hw": "faubourgs", "pos": "noun", "ipa": "/ˈfoʊbʊərɡz/", "vi": "vùng ngoại ô sát nội thành Pháp"},
  {"id": "lex.en.200k.060750", "hw": "femtoseconds", "pos": "noun", "ipa": "/ˈfɛmtoʊsɛkəndz/", "vi": "đơn vị một phần triệu tỷ giây"},
  {"id": "lex.en.200k.060751", "hw": "flutists", "pos": "noun", "ipa": "/ˈfluːtɪsts/", "vi": "nhạc công chuyên biểu diễn thổi sáo"},
  {"id": "lex.en.200k.060752", "hw": "gebs", "pos": "noun", "ipa": "/ɡɛbz/", "vi": "vị thần Trái Đất Geb của Ai Cập"},
  {"id": "lex.en.200k.060753", "hw": "gillies", "pos": "noun", "ipa": "/ˈɡɪliz/", "vi": "người dẫn đường săn bắn câu cá"},
  {"id": "lex.en.200k.060754", "hw": "goshawks", "pos": "noun", "ipa": "/ˈɡɑːshɔːks/", "vi": "chim ó ngỗng săn mồi rừng sâu"},
  {"id": "lex.en.200k.060755", "hw": "grommets", "pos": "noun", "ipa": "/ˈɡrɑːmɪts/", "vi": "khoen đệm tròn bọc lỗ dây cáp"},
  {"id": "lex.en.200k.060756", "hw": "hairpieces", "pos": "noun", "ipa": "/ˈhɛərpiːsɪz/", "vi": "mảnh tóc giả đội nối thêm vào tóc"},
  {"id": "lex.en.200k.060757", "hw": "hakkas", "pos": "noun", "ipa": "/ˈhɑːkəz/", "vi": "người Khách Gia; tiếng Khách Gia"},
  {"id": "lex.en.200k.060758", "hw": "heloises", "pos": "noun", "ipa": "/ɛloʊˈiːzɪz/", "vi": "nữ học giả Pháp nổi tiếng Héloïse"},
  {"id": "lex.en.200k.060759", "hw": "hizbullahs", "pos": "noun", "ipa": "/ˌhɪzbəˈlɑːz/", "vi": "phong trào vũ trang Hezbollah"},
  {"id": "lex.en.200k.060760", "hw": "hyperpigmentations", "pos": "noun", "ipa": "/ˌhaɪpərˌpɪɡmənˈteɪʃənz/", "vi": "tình trạng tăng sắc tố sạm nám da"},
  {"id": "lex.en.200k.060761", "hw": "imposts", "pos": "noun", "ipa": "/ˈɪmpoʊsts/", "vi": "thuế nhập khẩu; chân vòm cột đá"},
  {"id": "lex.en.200k.060762", "hw": "incivilities", "pos": "noun", "ipa": "/ˌɪnsɪˈvɪlətiz/", "vi": "thái độ khiếm nhã; sự bất lịch sự"},
  {"id": "lex.en.200k.060763", "hw": "kinfolks", "pos": "noun", "ipa": "/ˈkɪnfoʊks/", "vi": "bà con họ hàng thân thích gia tộc"},
  {"id": "lex.en.200k.060764", "hw": "kirchhoffs", "pos": "noun", "ipa": "/ˈkɪərkhɔːfs/", "vi": "nhà vật lý Đức Gustav Kirchhoff"},
  {"id": "lex.en.200k.060765", "hw": "lotas", "pos": "noun", "ipa": "/ˈloʊtəz/", "vi": "bình đựng nước đồng nhỏ ở Ấn Độ"},
  {"id": "lex.en.200k.060766", "hw": "lucretiuses", "pos": "noun", "ipa": "/luːˈkriːʃəsɪz/", "vi": "nhà thơ triết học La Mã Lucretius"},
  {"id": "lex.en.200k.060767", "hw": "luthiers", "pos": "noun", "ipa": "/ˈluːtiərz/", "vi": "nghệ nhân đóng chế tác đàn dây gỗ"},
  {"id": "lex.en.200k.060768", "hw": "malabsorptions", "pos": "noun", "ipa": "/ˌmæləbˈzɔːrpʃənz/", "vi": "hội chứng kém hấp thu dinh dưỡng"},
  {"id": "lex.en.200k.060769", "hw": "mangier", "pos": "adj", "ipa": "/ˈmeɪndʒiər/", "vi": "bị ghẻ lở trụi lông hơn; tiều tụy"},
  {"id": "lex.en.200k.060770", "hw": "mangiest", "pos": "adj", "ipa": "/ˈmeɪndʒiɪst/", "vi": "bị ghẻ trụi lông nhất; xơ xác nhất"},
  {"id": "lex.en.200k.060771", "hw": "manoeuvrabilities", "pos": "noun", "ipa": "/məˌnuːvrəˈbɪlətiz/", "vi": "tính cơ động linh hoạt điều khiển"},
  {"id": "lex.en.200k.060772", "hw": "mazzinis", "pos": "noun", "ipa": "/mɑːtˈsiːniz/", "vi": "nhà cách mạng Ý Giuseppe Mazzini"},
  {"id": "lex.en.200k.060773", "hw": "microbreweries", "pos": "noun", "ipa": "/ˈmaɪkroʊˌbruːəriz/", "vi": "xưởng nấu bia thủ công quy mô nhỏ"},
  {"id": "lex.en.200k.060774", "hw": "minimisations", "pos": "noun", "ipa": "/ˌmɪnɪmaɪˈzeɪʃənz/", "vi": "sự giảm thiểu tới mức tối thiểu"},
  {"id": "lex.en.200k.060775", "hw": "mithrases", "pos": "noun", "ipa": "/ˈmɪθrəsɪz/", "vi": "thần ánh sáng Mặt Trời Mithras"},
  {"id": "lex.en.200k.060776", "hw": "nativisms", "pos": "noun", "ipa": "/ˈneɪtɪvɪzəmz/", "vi": "chủ nghĩa bài ngoại đề cao bản địa"},
  {"id": "lex.en.200k.060777", "hw": "obeisances", "pos": "noun", "ipa": "/oʊˈbeɪsənsɪz/", "vi": "lễ cúi chào cung kính; sự tôn sùng"},
  {"id": "lex.en.200k.060778", "hw": "operons", "pos": "noun", "ipa": "/ˈɑːpərɑːnz/", "vi": "cụm gen điều hòa operon sinh học"},
  {"id": "lex.en.200k.060779", "hw": "orchestrators", "pos": "noun", "ipa": "/ˈɔːrkəstreɪtərz/", "vi": "người phối khí; kẻ giật dây mưu đồ"},
  {"id": "lex.en.200k.060780", "hw": "oronos", "pos": "noun", "ipa": "/ˈɔːrənoʊz/", "vi": "thị trấn đại học Orono bang Maine"},
  {"id": "lex.en.200k.060781", "hw": "osteopaths", "pos": "noun", "ipa": "/ˈɑːstioʊpæθs/", "vi": "bác sĩ trị liệu nắn chỉnh cơ xương"},
  {"id": "lex.en.200k.060782", "hw": "physiognomies", "pos": "noun", "ipa": "/ˌfɪziˈɑːɡnəmiz/", "vi": "nhân tướng học; diện mạo khuôn mặt"},
  {"id": "lex.en.200k.060783", "hw": "pinnas", "pos": "noun", "ipa": "/ˈpɪnəz/", "vi": "vành tai ngoài; lá chét lá kép"},
  {"id": "lex.en.200k.060784", "hw": "piquets", "pos": "noun", "ipa": "/pɪˈkɛts/", "vi": "trò đánh bài tây piquet hai người"},
  {"id": "lex.en.200k.060785", "hw": "platonisms", "pos": "noun", "ipa": "/ˈpleɪtənɪzəmz/", "vi": "học thuyết triết học của Platon"},
  {"id": "lex.en.200k.060786", "hw": "protozoans", "pos": "noun", "ipa": "/ˌproʊtəˈzoʊənz/", "vi": "động vật nguyên sinh đơn bào"},
  {"id": "lex.en.200k.060787", "hw": "purpuras", "pos": "noun", "ipa": "/ˈpɜːrpjʊrəz/", "vi": "ban xuất huyết tím bầm dưới da"},
  {"id": "lex.en.200k.060788", "hw": "reductionisms", "pos": "noun", "ipa": "/rɪˈdʌkʃənɪzəmz/", "vi": "chủ nghĩa giản lược hóa vấn đề"},
  {"id": "lex.en.200k.060789", "hw": "rnases", "pos": "noun", "ipa": "/ɑːr ɛn ˈeɪsɪz/", "vi": "men enzyme phân giải chuỗi ARN"},
  {"id": "lex.en.200k.060790", "hw": "roqueforts", "pos": "noun", "ipa": "/ˈroʊkfɔːrts/", "vi": "phô mai mốc xanh Roquefort Pháp"},
  {"id": "lex.en.200k.060791", "hw": "savourings", "pos": "noun", "ipa": "/ˈseɪvərɪŋz/", "vi": "sự nhâm nhi thưởng thức hương vị"},
  {"id": "lex.en.200k.060792", "hw": "selloffs", "pos": "noun", "ipa": "/ˈsɛlɔːfs/", "vi": "đợt bán tháo cổ phiếu ồ ạt giá rẻ"},
  {"id": "lex.en.200k.060793", "hw": "senoritas", "pos": "noun", "ipa": "/ˌsɛnjəˈriːtəz/", "vi": "cô tiểu thư trẻ tiếng Tây Ban Nha"},
  {"id": "lex.en.200k.060794", "hw": "shabus", "pos": "noun", "ipa": "/ˈʃɑːbuːz/", "vi": "ma túy tổng hợp đá methamphetamine"},
  {"id": "lex.en.200k.060795", "hw": "silkscreens", "pos": "noun", "ipa": "/ˈsɪlkskriːnz/", "vi": "kỹ thuật in lụa lưới thủ công"},
  {"id": "lex.en.200k.060796", "hw": "skywalks", "pos": "noun", "ipa": "/ˈskaɪwɔːks/", "vi": "cầu kính đi bộ nối trên không cao"},
  {"id": "lex.en.200k.060797", "hw": "soporifics", "pos": "noun", "ipa": "/ˌsɑːpəˈrɪfɪks/", "vi": "thuốc ngủ gây buồn ngủ sâu"},
  {"id": "lex.en.200k.060798", "hw": "stockrooms", "pos": "noun", "ipa": "/ˈstɑːkruːmz/", "vi": "kho chứa hàng hóa sau cửa hiệu"},
  {"id": "lex.en.200k.060799", "hw": "strawmans", "pos": "noun", "ipa": "/ˈstrɔːmənz/", "vi": "người rơm; kẻ đứng tên bình phong"},
  {"id": "lex.en.200k.060800", "hw": "sveriges", "pos": "noun", "ipa": "/ˈsvɛrɪɡəz/", "vi": "tên quốc gia Thụy Điển bản ngữ"},
  {"id": "lex.en.200k.060801", "hw": "sylvanuses", "pos": "noun", "ipa": "/sɪlˈveɪnəsɪz/", "vi": "thần bảo hộ rừng đồng Silvanus"},
  {"id": "lex.en.200k.060802", "hw": "synges", "pos": "noun", "ipa": "/sɪŋz/", "vi": "nhà viết kịch Ireland John Synge"}
]

with open('scratch/b33_r02_raw_p3.json') as f:
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

with open('scratch/b33_r02_p3.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Batch 33 Round 2 Part 3 validated and written successfully.")
