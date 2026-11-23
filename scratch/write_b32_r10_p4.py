import json

items = [
  {"id": "lex.en.200k.059803", "hw": "offenbaches", "pos": "noun", "ipa": "/ˈɑːfənbɑːks/", "vi": "nhà soạn nhạc Jacques Offenbach"},
  {"id": "lex.en.200k.059804", "hw": "percolated", "pos": "verb", "ipa": "/pˈɜːrkəlˌeɪtɪd/", "vi": "đã lọc qua phin; lan tỏa dần"},
  {"id": "lex.en.200k.059805", "hw": "pesaches", "pos": "noun", "ipa": "/pˈɛsɑːxs/", "vi": "đại lễ Vượt Qua Pesach Do Thái"},
  {"id": "lex.en.200k.059806", "hw": "phytophthoras", "pos": "noun", "ipa": "/fˌaɪtoʊfˈθɔːrəz/", "vi": "chi nấm mốc nước thối rễ cây"},
  {"id": "lex.en.200k.059807", "hw": "pilsens", "pos": "noun", "ipa": "/pˈɪlzənz/", "vi": "thành phố bia Pilsen ở Séc"},
  {"id": "lex.en.200k.059808", "hw": "prophetesses", "pos": "noun", "ipa": "/prˈɑːfətəsɪz/", "vi": "nữ tiên tri trong tôn giáo"},
  {"id": "lex.en.200k.059809", "hw": "prostatectomies", "pos": "noun", "ipa": "/ˌprɑːstətˈɛktəmiz/", "vi": "phẫu thuật cắt bỏ tuyến tiền liệt"},
  {"id": "lex.en.200k.059810", "hw": "proterozoics", "pos": "noun", "ipa": "/ˌprɑːtərəzˈoʊɪks/", "vi": "liên đại Nguyên Sinh vỏ Trái Đất"},
  {"id": "lex.en.200k.059811", "hw": "radhakrishnans", "pos": "noun", "ipa": "/ˌrɑːdəkˈrɪʃnənz/", "vi": "triết gia tổng thống Radhakrishnan"},
  {"id": "lex.en.200k.059812", "hw": "ramesseses", "pos": "noun", "ipa": "/rˈæməsiːzɪz/", "vi": "các Pharaon vĩ đại Ramesses"},
  {"id": "lex.en.200k.059813", "hw": "rancours", "pos": "noun", "ipa": "/rˈæŋkɚz/", "vi": "mối căm thù hằn học sâu cay"},
  {"id": "lex.en.200k.059814", "hw": "rhyolites", "pos": "noun", "ipa": "/rˈaɪəlaɪts/", "vi": "loại đá macma phun trào riolit"},
  {"id": "lex.en.200k.059815", "hw": "rotters", "pos": "noun", "ipa": "/rˈɑːtɚz/", "vi": "kẻ xấu xa tồi tệ đê tiện"},
  {"id": "lex.en.200k.059816", "hw": "roubles", "pos": "noun", "ipa": "/rˈuːbəlz/", "vi": "đồng tiền rúp nước Nga"},
  {"id": "lex.en.200k.059817", "hw": "salwars", "pos": "noun", "ipa": "/sˈælwaːrz/", "vi": "quần thụng truyền thống salwar"},
  {"id": "lex.en.200k.059818", "hw": "scids", "pos": "noun", "ipa": "/skˈɪdz/", "vi": "suy giảm miễn dịch kết hợp nặng"},
  {"id": "lex.en.200k.059819", "hw": "selectmen", "pos": "noun", "ipa": "/sɪlˈɛktmən/", "vi": "ủy viên hội đồng quản trị thị trấn"},
  {"id": "lex.en.200k.059820", "hw": "shoehorned", "pos": "verb", "ipa": "/ʃˈuhɔrnd/", "vi": "đã nhét gượng gạo; chèn ép vào"},
  {"id": "lex.en.200k.059821", "hw": "shoehorning", "pos": "verb", "ipa": "/ʃˈuːhɔːrnɪŋ/", "vi": "đang nhét gượng gạo; chèn ép vào"},
  {"id": "lex.en.200k.059822", "hw": "shoehorns", "pos": "noun", "ipa": "/ʃˈuːhɔːrnz/", "vi": "cái đón gót giày; muỗng xỏ giày"},
  {"id": "lex.en.200k.059823", "hw": "shrubbier", "pos": "adj", "ipa": "/ʃrˈʌbiɚ/", "vi": "nhiều bụi rậm hơn; rậm rạp hơn"},
  {"id": "lex.en.200k.059824", "hw": "shrubbiest", "pos": "adj", "ipa": "/ʃrˈʌbiɪst/", "vi": "nhiều bụi rậm nhất; rậm rạp nhất"},
  {"id": "lex.en.200k.059825", "hw": "sidas", "pos": "noun", "ipa": "/sˈiːdəz/", "vi": "chi thực vật cây ké hoa sida"},
  {"id": "lex.en.200k.059826", "hw": "sixtieths", "pos": "noun", "ipa": "/sˈɪkstiɪθs/", "vi": "phần thứ sáu mươi; một phần 60"},
  {"id": "lex.en.200k.059827", "hw": "sophistries", "pos": "noun", "ipa": "/sˈɑːfɪstriz/", "vi": "lập luận ngụy biện xảo trá"},
  {"id": "lex.en.200k.059828", "hw": "stoichiometries", "pos": "noun", "ipa": "/ˌstɔɪkiˈɑːmətriːz/", "vi": "tính toán tỷ lượng hóa học"},
  {"id": "lex.en.200k.059829", "hw": "stuffers", "pos": "noun", "ipa": "/stˈʌfɚz/", "vi": "dụng cụ nhồi xúc xích; tờ rơi chèn"},
  {"id": "lex.en.200k.059830", "hw": "supernumeraries", "pos": "noun", "ipa": "/sˌuːpərnˈuːmərɛriz/", "vi": "diễn viên phụ quần chúng; người dôi"},
  {"id": "lex.en.200k.059831", "hw": "syncretisms", "pos": "noun", "ipa": "/sˈɪŋkrətɪzəmz/", "vi": "sự dung hợp tôn giáo tín ngưỡng"},
  {"id": "lex.en.200k.059832", "hw": "telluses", "pos": "noun", "ipa": "/tˈɛləsɪz/", "vi": "nữ thần Đất Mẹ Tellus La Mã"},
  {"id": "lex.en.200k.059833", "hw": "tottered", "pos": "verb", "ipa": "/tˈɑːtɚd/", "vi": "đã bước đi loạng choạng lảo đảo"},
  {"id": "lex.en.200k.059834", "hw": "totters", "pos": "verb", "ipa": "/tˈɑːtɚz/", "vi": "bước đi lảo đảo; sắp sụp đổ"},
  {"id": "lex.en.200k.059835", "hw": "tykes", "pos": "noun", "ipa": "/tˈaɪks/", "vi": "đứa trẻ tinh nghịch; người xứ York"},
  {"id": "lex.en.200k.059836", "hw": "ulemas", "pos": "noun", "ipa": "/uːləmˈɑːz/", "vi": "học giả giáo luật Hồi giáo"},
  {"id": "lex.en.200k.059837", "hw": "varmints", "pos": "noun", "ipa": "/vˈɑːrmɪnts/", "vi": "thú gây hại mùa màng; kẻ quấy rối"},
  {"id": "lex.en.200k.059838", "hw": "verniers", "pos": "noun", "ipa": "/vˈɜːrniɚz/", "vi": "thước cặp đo cơ khí du xích"},
  {"id": "lex.en.200k.059839", "hw": "vitides", "pos": "noun", "ipa": "/vaɪtˈaɪdiːz/", "vi": "các loài thuộc họ dây leo Nho"},
  {"id": "lex.en.200k.059840", "hw": "weaponized", "pos": "verb", "ipa": "/wˈɛpənaɪzd/", "vi": "đã quân sự hóa; biến thành vũ khí"},
  {"id": "lex.en.200k.059841", "hw": "weaponizes", "pos": "verb", "ipa": "/wˈɛpənaɪzɪz/", "vi": "biến thành vũ khí tấn công"},
  {"id": "lex.en.200k.059842", "hw": "weaponizing", "pos": "verb", "ipa": "/wˈɛpənaɪzɪŋ/", "vi": "đang vũ khí hóa công nghệ"},
  {"id": "lex.en.200k.059843", "hw": "woodsier", "pos": "adj", "ipa": "/wˈʊdziɚ/", "vi": "đậm chất hương rừng hơn"},
  {"id": "lex.en.200k.059844", "hw": "woodsiest", "pos": "adj", "ipa": "/wˈʊdziɪst/", "vi": "đậm chất hương vị rừng nhất"},
  {"id": "lex.en.200k.059845", "hw": "yagis", "pos": "noun", "ipa": "/jˈɑːɡiz/", "vi": "loại ăng-ten định hướng Yagi"},
  {"id": "lex.en.200k.059846", "hw": "agglutination test", "pos": "phrase", "ipa": "/əˌɡluːtɪˈneɪʃən tɛst/", "vi": "xét nghiệm phản ứng ngưng kết"},
  {"id": "lex.en.200k.059847", "hw": "american hackberry", "pos": "phrase", "ipa": "/əˈmɛrɪkən ˈhækˌbɛri/", "vi": "cây sếu Mỹ; cây cơm nguội Bắc Mỹ"},
  {"id": "lex.en.200k.059848", "hw": "anise hyssop", "pos": "phrase", "ipa": "/ˈænɪs ˈhɪsəp/", "vi": "cây bạc hà hồi hoa tím"},
  {"id": "lex.en.200k.059849", "hw": "anterior meningeal artery", "pos": "phrase", "ipa": "/ænˈtɪəriər mɪˈnɪndʒiəl ˈɑːrtəri/", "vi": "động mạch màng não trước"},
  {"id": "lex.en.200k.059850", "hw": "atrium cordis", "pos": "phrase", "ipa": "/ˈeɪtriəm ˈkɔːrdɪs/", "vi": "tâm nhĩ của quả tim"},
  {"id": "lex.en.200k.059851", "hw": "bartle frere", "pos": "phrase", "ipa": "/ˈbɑːrtl frɪər/", "vi": "đỉnh núi Bartle Frere ở Queensland"},
  {"id": "lex.en.200k.059852", "hw": "battle of panipat", "pos": "phrase", "ipa": "/ˈbætl əv ˈpɑːniːpət/", "vi": "trận đại chiến Panipat Ấn Độ"},
  {"id": "lex.en.200k.059853", "hw": "belly flopper", "pos": "phrase", "ipa": "/ˈbɛli ˈflɑːpər/", "vi": "cú nhảy đập bụng xuống mặt nước"},
  {"id": "lex.en.200k.059854", "hw": "bimetallic strip", "pos": "phrase", "ipa": "/ˌbaɪmɪˈtælɪk strɪp/", "vi": "thanh lưỡng kim rơ-le nhiệt"},
  {"id": "lex.en.200k.059855", "hw": "birdseed grass", "pos": "phrase", "ipa": "/ˈbɜːrdsiːd ɡræs/", "vi": "cây cỏ yến mạch hạt nuôi chim"},
  {"id": "lex.en.200k.059856", "hw": "brassica rapa", "pos": "phrase", "ipa": "/ˈbræsɪkə ˈrɑːpə/", "vi": "loài cải củ tròn cải dầu"},
  {"id": "lex.en.200k.059857", "hw": "canary whitewood", "pos": "phrase", "ipa": "/kəˈnɛəri ˈwaɪtwʊd/", "vi": "cây ngô đồng vàng gỗ trắng"},
  {"id": "lex.en.200k.059858", "hw": "chicken roundworm", "pos": "phrase", "ipa": "/ˈtʃɪkən ˈraʊndwɜːrm/", "vi": "giun đũa ký sinh đường ruột gà"},
  {"id": "lex.en.200k.059859", "hw": "common horsetail", "pos": "phrase", "ipa": "/ˈkɑːmən ˈhɔːrsteɪl/", "vi": "cỏ tháp bút mộc tặc đuôi ngựa"},
  {"id": "lex.en.200k.059860", "hw": "common roundworm", "pos": "phrase", "ipa": "/ˈkɑːmən ˈraʊndwɜːrm/", "vi": "giun đũa ký sinh đường ruột người"},
  {"id": "lex.en.200k.059861", "hw": "conk out", "pos": "phrase", "ipa": "/kɑːŋk aʊt/", "vi": "chết máy hỏng đột ngột; kiệt sức"},
  {"id": "lex.en.200k.059862", "hw": "cottonmouth moccasin", "pos": "phrase", "ipa": "/ˈkɑːtnmaʊθ ˈmɑːkəsɪn/", "vi": "rắn hổ mang nước miệng bông độc"},
  {"id": "lex.en.200k.059863", "hw": "douay bible", "pos": "phrase", "ipa": "/duːˈeɪ ˈbaɪbl/", "vi": "Kinh Thánh Công giáo Douay"},
  {"id": "lex.en.200k.059864", "hw": "douay version", "pos": "phrase", "ipa": "/duːˈeɪ ˈvɜːrʒən/", "vi": "Kinh Thánh tiếng Anh Douay"},
  {"id": "lex.en.200k.059865", "hw": "emesis basin", "pos": "phrase", "ipa": "/ˈɛməsɪs ˈbeɪsn/", "vi": "chậu hạt đậu hứng chất nôn y tế"},
  {"id": "lex.en.200k.059866", "hw": "european flatfish", "pos": "phrase", "ipa": "/ˌjʊərəˈpiːən ˈflætfɪʃ/", "vi": "loài cá bơn mắt phẳng châu Âu"},
  {"id": "lex.en.200k.059867", "hw": "european hackberry", "pos": "phrase", "ipa": "/ˌjʊərəˈpiːən ˈhækˌbɛri/", "vi": "cây sếu cơm nguội châu Âu"},
  {"id": "lex.en.200k.059868", "hw": "exocrine gland", "pos": "phrase", "ipa": "/ˈɛksoʊkrɪn ɡlænd/", "vi": "tuyến ngoại tiết tiết dịch cơ thể"},
  {"id": "lex.en.200k.059869", "hw": "fecal impaction", "pos": "phrase", "ipa": "/ˈfiːkəl ɪmˈpækʃən/", "vi": "chứng ứ đọng khối phân tắc ruột"},
  {"id": "lex.en.200k.059870", "hw": "field horsetail", "pos": "phrase", "ipa": "/fiːld ˈhɔːrsteɪl/", "vi": "cây cỏ tháp bút mọc đồng ruộng"},
  {"id": "lex.en.200k.059871", "hw": "flame tokay", "pos": "phrase", "ipa": "/fleɪm toʊˈkeɪ/", "vi": "giống nho đỏ tokay ngọt đậm"},
  {"id": "lex.en.200k.059872", "hw": "genus calamus", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈkæləməs/", "vi": "chi mây tre mộc song Calamus"},
  {"id": "lex.en.200k.059873", "hw": "genus fabiana", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˌfæbiˈɑːnə/", "vi": "chi cây bụi hoa ống Fabiana"},
  {"id": "lex.en.200k.059874", "hw": "genus galax", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈɡeɪlæks/", "vi": "chi cỏ thường xanh lá tròn Galax"},
  {"id": "lex.en.200k.059875", "hw": "genus nipa", "pos": "phrase", "ipa": "/ˈdʒiːnəs ˈniːpə/", "vi": "chi thực vật cây dừa nước Nypa"},
  {"id": "lex.en.200k.059876", "hw": "george catlett marshall", "pos": "phrase", "ipa": "/dʒɔːrdʒ ˈkætlət ˈmɑːrʃəl/", "vi": "Đại tướng Mỹ George Marshall"},
  {"id": "lex.en.200k.059877", "hw": "golfo de mexico", "pos": "phrase", "ipa": "/ˈɡɔːlfoʊ deɪ ˈmɛksɪkoʊ/", "vi": "vịnh Mexico ở Bắc Mỹ"},
  {"id": "lex.en.200k.059878", "hw": "horsetail family", "pos": "phrase", "ipa": "/ˈhɔːrsteɪl ˈfæməli/", "vi": "họ thực vật cỏ tháp bút mộc tặc"},
  {"id": "lex.en.200k.059879", "hw": "hydromorphone hydrochloride", "pos": "phrase", "ipa": "/ˌhaɪdroʊˈmɔːrfoʊn ˌhaɪdrəˈklɔːraɪd/", "vi": "thuốc giảm đau gây nghiện mạnh"},
  {"id": "lex.en.200k.059880", "hw": "igor tamm", "pos": "phrase", "ipa": "/ˈiːɡɔːr tæm/", "vi": "nhà vật lý Nobel Igor Tamm"},
  {"id": "lex.en.200k.059881", "hw": "ii esdras", "pos": "phrase", "ipa": "/tuː ˈɛzdrəs/", "vi": "sách ngụy thư Kinh Thánh Esdras 2"},
  {"id": "lex.en.200k.059882", "hw": "jointing plane", "pos": "phrase", "ipa": "/ˈdʒɔɪntɪŋ pleɪn/", "vi": "bào dài làm phẳng mối ghép mộc"},
  {"id": "lex.en.200k.059883", "hw": "katmai national park", "pos": "phrase", "ipa": "/ˈkætmaɪ ˈnæʃənəl pɑːrk/", "vi": "Vườn quốc gia núi lửa Katmai"},
  {"id": "lex.en.200k.059884", "hw": "lanthanide series", "pos": "phrase", "ipa": "/ˈlænθənaɪd ˈsɪriːz/", "vi": "dãy nguyên tố đất hiếm lantan"},
  {"id": "lex.en.200k.059885", "hw": "lee strasberg", "pos": "phrase", "ipa": "/liː ˈstræsbɜːrɡ/", "vi": "đạo diễn kịch nghệ Lee Strasberg"},
  {"id": "lex.en.200k.059886", "hw": "lese majesty", "pos": "phrase", "ipa": "/liːz ˈmædʒəsti/", "vi": "tội khi quân xúc phạm hoàng gia"},
  {"id": "lex.en.200k.059887", "hw": "lillie langtry", "pos": "phrase", "ipa": "/ˈlɪli ˈlæŋtri/", "vi": "nữ diễn viên Lillie Langtry"},
  {"id": "lex.en.200k.059888", "hw": "loblolly pine", "pos": "phrase", "ipa": "/lɑːbˈlɑːli paɪn/", "vi": "cây thông loblolly lá dài nam"},
  {"id": "lex.en.200k.059889", "hw": "locum tenens", "pos": "phrase", "ipa": "/ˈloʊkəm ˈtiːnɛnz/", "vi": "bác sĩ phụ trách thay tạm thời"},
  {"id": "lex.en.200k.059890", "hw": "luteinizing hormone", "pos": "phrase", "ipa": "/ˈluːtiənaɪzɪŋ ˈhɔːrmoʊn/", "vi": "hoóc-môn tạo hoàng thể rụng trứng"},
  {"id": "lex.en.200k.059891", "hw": "marsh horsetail", "pos": "phrase", "ipa": "/mɑːrʃ ˈhɔːrsteɪl/", "vi": "cỏ tháp bút mọc vùng đầm lầy"},
  {"id": "lex.en.200k.059892", "hw": "mediterranean hackberry", "pos": "phrase", "ipa": "/ˌmɛdɪtəˈreɪniən ˈhækˌbɛri/", "vi": "cây cơm nguội Địa Trung Hải"},
  {"id": "lex.en.200k.059893", "hw": "miniature pinscher", "pos": "phrase", "ipa": "/ˈmɪnətʃʊər ˈpɪntʃər/", "vi": "giống chó phốc pinscher lùn"},
  {"id": "lex.en.200k.059894", "hw": "mount bartle frere", "pos": "phrase", "ipa": "/maʊnt ˈbɑːrtl frɪər/", "vi": "đỉnh núi cao Bartle Frere Úc"},
  {"id": "lex.en.200k.059895", "hw": "mount pinatubo", "pos": "phrase", "ipa": "/maʊnt ˌpɪnəˈtuːboʊ/", "vi": "núi lửa phun trào Pinatubo"},
  {"id": "lex.en.200k.059896", "hw": "multiple neuritis", "pos": "phrase", "ipa": "/ˈmʌltɪpl njʊˈraɪtɪs/", "vi": "viêm nhiều dây thần kinh ngoại vi"},
  {"id": "lex.en.200k.059897", "hw": "mus musculus", "pos": "phrase", "ipa": "/mʌs ˈmʌskjʊləs/", "vi": "loài chuột nhắt nhà thí nghiệm"},
  {"id": "lex.en.200k.059898", "hw": "nitrogen narcosis", "pos": "phrase", "ipa": "/ˈnaɪtrədʒən nɑːrˈkoʊsɪs/", "vi": "say khí nitơ khi lặn biển sâu"},
  {"id": "lex.en.200k.059899", "hw": "northern barramundi", "pos": "phrase", "ipa": "/ˈnɔːrðərn ˌbærəˈmʌndi/", "vi": "loài cá vược chẽm khổng lồ bắc"},
  {"id": "lex.en.200k.059900", "hw": "nullarbor plain", "pos": "phrase", "ipa": "/ˈnʌlərbɔːr pleɪn/", "vi": "đồng bằng hoang mạc Nullarbor Úc"},
  {"id": "lex.en.200k.059901", "hw": "obturator vein", "pos": "phrase", "ipa": "/ˈɑːbtʃʊreɪtər veɪn/", "vi": "tĩnh mạch bịt dẫn máu khoang chậu"},
  {"id": "lex.en.200k.059902", "hw": "peptic ulceration", "pos": "phrase", "ipa": "/ˈpɛptɪk ˌʌlsəˈreɪʃən/", "vi": "vết loét niêm mạc dạ dày tá tràng"}
]

with open('scratch/b32_r10_raw_p4.json') as f:
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

with open('scratch/b32_r10_p4.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Part 4 validated and written successfully.")
