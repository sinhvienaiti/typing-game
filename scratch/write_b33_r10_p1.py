import json

items = [
  {"id": "lex.en.200k.064503", "hw": "hydroxyzine hydrochloride", "pos": "phrase", "ipa": "/haɪˈdrɑːksəziːn ˌhaɪdrəˈklɔːraɪd/", "vi": "thuốc kháng histamin hydroxyzine"},
  {"id": "lex.en.200k.064504", "hw": "iroquoian language", "pos": "phrase", "ipa": "/ˌɪrəˈkwɔɪən ˈlæŋɡwɪdʒ/", "vi": "ngôn ngữ hệ bản địa Iroquois Mỹ"},
  {"id": "lex.en.200k.064505", "hw": "johann joachim winckelmann", "pos": "phrase", "ipa": "/ˈjoʊhɑːn ˈjoʊɑːxɪm ˈvɪŋkəlmɑːn/", "vi": "nhà khảo cổ học nghệ thuật Đức"},
  {"id": "lex.en.200k.064506", "hw": "juglans nigra", "pos": "phrase", "ipa": "/ˈdʒuːɡlænz ˈnaɪɡrə/", "vi": "cây óc chó đen gỗ quý Bắc Mỹ"},
  {"id": "lex.en.200k.064507", "hw": "malaysian mujahidin group", "pos": "phrase", "ipa": "/məˈleɪʒən ˌmuːdʒɑːhɪˈdiːn ɡruːp/", "vi": "nhóm vũ trang Hồi giáo Malaysia"},
  {"id": "lex.en.200k.064508", "hw": "malus angustifolia", "pos": "phrase", "ipa": "/ˈmeɪləs æŋˌɡʌstɪˈfoʊliə/", "vi": "cây táo dại hoa hồng miền nam Mỹ"},
  {"id": "lex.en.200k.064509", "hw": "marquise de maintenon", "pos": "phrase", "ipa": "/mɑːrˈkiːz də ˌmæntəˈnɔːn/", "vi": "Nữ hầu tước Maintenon nước Pháp"},
  {"id": "lex.en.200k.064510", "hw": "meadow salsify", "pos": "phrase", "ipa": "/ˈmɛdoʊ ˈsælsəfi/", "vi": "cây hoa cúc rễ đồng cỏ vàng"},
  {"id": "lex.en.200k.064511", "hw": "musette pipe", "pos": "phrase", "ipa": "/mjuːˈzɛt paɪp/", "vi": "kèn túi nhỏ hoặc kèn dăm đôi Pháp"},
  {"id": "lex.en.200k.064512", "hw": "myoclonus epilepsy", "pos": "phrase", "ipa": "/ˌmaɪəˈkloʊnəs ˈɛpəˌlɛpsi/", "vi": "chứng động kinh giật rung cơ"},
  {"id": "lex.en.200k.064513", "hw": "okefenokee swamp", "pos": "phrase", "ipa": "/ˌoʊkɪfəˈnoʊki swɑːmp/", "vi": "đầm lầy than bùn Okefenokee Mỹ"},
  {"id": "lex.en.200k.064514", "hw": "optative mood", "pos": "phrase", "ipa": "/ˈɑːptətɪv muːd/", "vi": "thức cầu chúc mong ước (ngữ pháp)"},
  {"id": "lex.en.200k.064515", "hw": "osteogenesis imperfecta", "pos": "phrase", "ipa": "/ˌɑːstioʊˈdʒɛnəsɪs ˌɪmpərˈfɛktə/", "vi": "bệnh xương thủy tinh giòn dễ gãy"},
  {"id": "lex.en.200k.064516", "hw": "otis tarda", "pos": "phrase", "ipa": "/ˈoʊtɪs ˈtɑːrdə/", "vi": "chim ô tác lớn nặng vùng Á-Âu"},
  {"id": "lex.en.200k.064517", "hw": "piltdown hoax", "pos": "phrase", "ipa": "/ˈpɪltdaʊn hoʊks/", "vi": "trò bịp hóa thạch người Piltdown"},
  {"id": "lex.en.200k.064518", "hw": "plosive speech sound", "pos": "phrase", "ipa": "/ˈploʊsɪv spiːtʃ saʊnd/", "vi": "âm phụ âm bật tắc thanh quản"},
  {"id": "lex.en.200k.064519", "hw": "portuguese escudo", "pos": "phrase", "ipa": "/ˈpɔːrtʃəˌɡiːz ɛˈskuːduː/", "vi": "đồng tiền escudo cũ Bồ Đào Nha"},
  {"id": "lex.en.200k.064520", "hw": "pouched mammal", "pos": "phrase", "ipa": "/paʊtʃt ˈmæməl/", "vi": "động vật có vú nuôi con trong túi"},
  {"id": "lex.en.200k.064521", "hw": "purus river", "pos": "phrase", "ipa": "/ˈpʊrəs ˈrɪvər/", "vi": "sông Purus phụ lưu sông Amazon"},
  {"id": "lex.en.200k.064522", "hw": "pyrus communis", "pos": "phrase", "ipa": "/ˈpaɪrəs kəˈmjuːnɪs/", "vi": "cây lê ăn quả phổ biến châu Âu"},
  {"id": "lex.en.200k.064523", "hw": "red dagga", "pos": "phrase", "ipa": "/rɛd ˈdæɡə/", "vi": "cây tai sư tử hoa đỏ Nam Phi"},
  {"id": "lex.en.200k.064524", "hw": "saint emilion", "pos": "phrase", "ipa": "/sænt eɪmiˈjɔːn/", "vi": "rượu vang đỏ vùng Saint-Émilion"},
  {"id": "lex.en.200k.064525", "hw": "samian ware", "pos": "phrase", "ipa": "/ˈseɪmiən wɛər/", "vi": "đồ gốm đỏ bóng La Mã cổ đại"},
  {"id": "lex.en.200k.064526", "hw": "silicic acid", "pos": "phrase", "ipa": "/səˈlɪsɪk ˈæsɪd/", "vi": "axit yếu chứa silic trong tự nhiên"},
  {"id": "lex.en.200k.064527", "hw": "soleus muscle", "pos": "phrase", "ipa": "/ˈsoʊliəs ˈmʌsəl/", "vi": "cơ dép bắp chân giúp duỗi cổ chân"},
  {"id": "lex.en.200k.064528", "hw": "stockinette stitch", "pos": "phrase", "ipa": "/ˌstɑːkəˈnɛt stɪtʃ/", "vi": "kiểu mũi đan len trơn mặt phải"},
  {"id": "lex.en.200k.064529", "hw": "superconducting supercollider", "pos": "phrase", "ipa": "/ˌsuːpərkənˈdʌktɪŋ ˈsuːpərkəˌlaɪdər/", "vi": "máy gia tốc va chạm siêu dẫn Mỹ"},
  {"id": "lex.en.200k.064530", "hw": "ulmus rubra", "pos": "phrase", "ipa": "/ˈʌlməs ˈruːbrə/", "vi": "cây du đỏ Bắc Mỹ vỏ trơn làm thuốc"},
  {"id": "lex.en.200k.064531", "hw": "vachel lindsay", "pos": "phrase", "ipa": "/ˈveɪtʃəl ˈlɪndzi/", "vi": "nhà thơ hiện đại Mỹ Vachel Lindsay"},
  {"id": "lex.en.200k.064532", "hw": "walther hermann nernst", "pos": "phrase", "ipa": "/ˈvɑːltər ˈhɛrmɑːn nɛrnst/", "vi": "nhà hóa lý Nobel Đức Nernst"},
  {"id": "lex.en.200k.064533", "hw": "abseiled", "pos": "verb", "ipa": "/ˈæbseɪld/", "vi": "đã leo tụt xuống vách núi bằng dây"},
  {"id": "lex.en.200k.064534", "hw": "aconcaguas", "pos": "noun", "ipa": "/ˌækənˈkɑːɡwəz/", "vi": "đỉnh núi cao nhất Nam Mỹ Aconcagua"},
  {"id": "lex.en.200k.064535", "hw": "aerators", "pos": "noun", "ipa": "/ˈɛəˌreɪtərz/", "vi": "máy sục khí; đầu tạo bọt vòi nước"},
  {"id": "lex.en.200k.064536", "hw": "agglutinations", "pos": "noun", "ipa": "/əˌɡluːtəˈneɪʃənz/", "vi": "sự ngưng kết tế bào; ghép phụ tố"},
  {"id": "lex.en.200k.064537", "hw": "allopurinols", "pos": "noun", "ipa": "/ˌæləˈpjʊrəˌnɔːlz/", "vi": "thuốc hạ axit uric trị gút"},
  {"id": "lex.en.200k.064538", "hw": "assurs", "pos": "noun", "ipa": "/ˈæsʊərz/", "vi": "thành phố cổ Assur thủ đô Assyria"},
  {"id": "lex.en.200k.064539", "hw": "bacteremias", "pos": "noun", "ipa": "/ˌbæktəˈriːmiəz/", "vi": "tình trạng vi khuẩn xâm nhập máu"},
  {"id": "lex.en.200k.064540", "hw": "balalaikas", "pos": "noun", "ipa": "/ˌbæləˈlaɪkəz/", "vi": "đàn dây tam giác ba dây Nga"},
  {"id": "lex.en.200k.064541", "hw": "barramundies", "pos": "noun", "ipa": "/ˌbærəˈmʌndiz/", "vi": "cá chẽm lớn vùng nước ngọt và biển"},
  {"id": "lex.en.200k.064542", "hw": "barramundis", "pos": "noun", "ipa": "/ˌbærəˈmʌndiz/", "vi": "cá vược chẽm Úc thịt trắng ngon"},
  {"id": "lex.en.200k.064543", "hw": "beaners", "pos": "noun", "ipa": "/ˈbiːnərz/", "vi": "cú ném bóng chày trúng đầu; từ lóng"},
  {"id": "lex.en.200k.064544", "hw": "beefeaters", "pos": "noun", "ipa": "/ˈbiːfˌiːtərz/", "vi": "lính gác Tháp Luân Đôn mặc lễ phục"},
  {"id": "lex.en.200k.064545", "hw": "berits", "pos": "noun", "ipa": "/bəˈriːts/", "vi": "nghi lễ cắt bao quy đầu Do Thái"},
  {"id": "lex.en.200k.064546", "hw": "bibliographers", "pos": "noun", "ipa": "/ˌbɪbliˈɑːɡrəfərz/", "vi": "chuyên gia biên soạn thư mục sách"},
  {"id": "lex.en.200k.064547", "hw": "bithynias", "pos": "noun", "ipa": "/bɪˈθɪniəz/", "vi": "vương quốc cổ Bithynia vùng Tiểu Á"},
  {"id": "lex.en.200k.064548", "hw": "bobbers", "pos": "noun", "ipa": "/ˈbɑːbərz/", "vi": "phao câu nổi; xe mô tô độ cắt gọn"},
  {"id": "lex.en.200k.064549", "hw": "bosuns", "pos": "noun", "ipa": "/ˈboʊsənz/", "vi": "thủy thủ trưởng phụ trách boong tàu"},
  {"id": "lex.en.200k.064550", "hw": "bouillabaisses", "pos": "noun", "ipa": "/ˌbuːjəˈbɛsɪz/", "vi": "súp hầm hải sản truyền thống Pháp"},
  {"id": "lex.en.200k.064551", "hw": "brahmis", "pos": "noun", "ipa": "/ˈbrɑːmiz/", "vi": "chữ viết cổ Ấn Độ Brahmi tổ tiên"},
  {"id": "lex.en.200k.064552", "hw": "byelorussians", "pos": "noun", "ipa": "/ˌbjɛloʊˈrʌʃənz/", "vi": "người dân Belarus (cách gọi cũ)"},
  {"id": "lex.en.200k.064553", "hw": "carrizos", "pos": "noun", "ipa": "/kəˈriːzoʊz/", "vi": "cây sậy lớn mọc dọc bờ sông tây Mỹ"},
  {"id": "lex.en.200k.064554", "hw": "ceftriaxones", "pos": "noun", "ipa": "/ˌsɛftraɪˈæksoʊnz/", "vi": "kháng sinh tiêm mạnh ceftriaxone"},
  {"id": "lex.en.200k.064555", "hw": "cheopses", "pos": "noun", "ipa": "/ˈkiːɑːpsɪz/", "vi": "pharaon Ai Cập xây đại kim tự tháp"},
  {"id": "lex.en.200k.064556", "hw": "choirboys", "pos": "noun", "ipa": "/ˈkwaɪərˌbɔɪz/", "vi": "bé trai hát trong dàn đồng ca thờ"},
  {"id": "lex.en.200k.064557", "hw": "christianizations", "pos": "noun", "ipa": "/ˌkrɪstʃənaɪˈzeɪʃənz/", "vi": "quá trình cải đạo sang Cơ Đốc giáo"},
  {"id": "lex.en.200k.064558", "hw": "coltans", "pos": "noun", "ipa": "/ˈkɑːltænz/", "vi": "quặng khoáng hiếm điện tử coltan"},
  {"id": "lex.en.200k.064559", "hw": "contrails", "pos": "noun", "ipa": "/ˈkɑːntreɪlz/", "vi": "vệt mây ngưng tụ sau đuôi máy bay"},
  {"id": "lex.en.200k.064560", "hw": "contraindications", "pos": "noun", "ipa": "/ˌkɑːntrəˌɪndɪˈkeɪʃənz/", "vi": "chống chỉ định không được phép dùng"},
  {"id": "lex.en.200k.064561", "hw": "cosmetologists", "pos": "noun", "ipa": "/ˌkɑːzməˈtɑːlədʒɪsts/", "vi": "chuyên viên trang điểm làm tóc da"},
  {"id": "lex.en.200k.064562", "hw": "crabmeats", "pos": "noun", "ipa": "/ˈkræbmiːts/", "vi": "thịt cua gỡ sẵn chế biến món ăn"},
  {"id": "lex.en.200k.064563", "hw": "cryptographers", "pos": "noun", "ipa": "/krɪpˈtɑːɡrəfərz/", "vi": "chuyên gia mật mã học mã hóa tin"},
  {"id": "lex.en.200k.064564", "hw": "davits", "pos": "noun", "ipa": "/ˈdævɪts/", "vi": "cần trục nhỏ nâng hạ xuồng cứu sinh"},
  {"id": "lex.en.200k.064565", "hw": "declamations", "pos": "noun", "ipa": "/ˌdɛkləˈmeɪʃənz/", "vi": "bài diễn thuyết hùng biện cảm xúc"},
  {"id": "lex.en.200k.064566", "hw": "demobilisations", "pos": "noun", "ipa": "/diːˌmoʊbələˈzeɪʃənz/", "vi": "lệnh giải ngũ quân nhân (cách Anh)"},
  {"id": "lex.en.200k.064567", "hw": "digraphs", "pos": "noun", "ipa": "/ˈdaɪɡræfs/", "vi": "tổ hợp hai chữ cái ghi một âm vị"},
  {"id": "lex.en.200k.064568", "hw": "effectuated", "pos": "verb", "ipa": "/ɪˈfɛktʃuˌeɪtɪd/", "vi": "đã thực hiện hoàn thành hiệu quả"},
  {"id": "lex.en.200k.064569", "hw": "effectuates", "pos": "verb", "ipa": "/ɪˈfɛktʃuˌeɪts/", "vi": "thực hiện thành công mang lại quả"},
  {"id": "lex.en.200k.064570", "hw": "effectuating", "pos": "verb", "ipa": "/ɪˈfɛktʃuˌeɪtɪŋ/", "vi": "đang thực hiện mang lại kết quả"},
  {"id": "lex.en.200k.064571", "hw": "electromyographies", "pos": "noun", "ipa": "/ɪˌlɛktroʊmaɪˈɑːɡrəfiz/", "vi": "kỹ thuật đo điện cơ chẩn đoán bệnh"},
  {"id": "lex.en.200k.064572", "hw": "emeses", "pos": "noun", "ipa": "/ˈɛməsiːz/", "vi": "hiện tượng nôn mửa (thuật ngữ y)"},
  {"id": "lex.en.200k.064573", "hw": "epiglottides", "pos": "noun", "ipa": "/ˌɛpɪˈɡlɑːtədiːz/", "vi": "sụn nắp thanh quản khi nuốt thức ăn"},
  {"id": "lex.en.200k.064574", "hw": "epiglottises", "pos": "noun", "ipa": "/ˌɛpɪˈɡlɑːtəsɪz/", "vi": "nắp thanh quản ngăn sặc vào phổi"},
  {"id": "lex.en.200k.064575", "hw": "expediences", "pos": "noun", "ipa": "/ɪkˈspiːdiənsɪz/", "vi": "tính thực dụng lợi thế trước mắt"},
  {"id": "lex.en.200k.064576", "hw": "flexures", "pos": "noun", "ipa": "/ˈflɛkʃərz/", "vi": "độ uốn cong; chỗ gập góc đại tràng"},
  {"id": "lex.en.200k.064577", "hw": "flocculations", "pos": "noun", "ipa": "/ˌflɑːkjəˈleɪʃənz/", "vi": "hiện tượng kết bông keo tụ lắng cặn"},
  {"id": "lex.en.200k.064578", "hw": "floddens", "pos": "noun", "ipa": "/ˈflɑːdənz/", "vi": "trận chiến đồi Flodden Anh-Scotland"},
  {"id": "lex.en.200k.064579", "hw": "furriers", "pos": "noun", "ipa": "/ˈfɜːriərz/", "vi": "thợ may buôn bán áo choàng lông thú"},
  {"id": "lex.en.200k.064580", "hw": "gabbros", "pos": "noun", "ipa": "/ˈɡæbroʊz/", "vi": "đá mácma hạt thô màu sẫm gabbro"},
  {"id": "lex.en.200k.064581", "hw": "gigantisms", "pos": "noun", "ipa": "/dʒaɪˈɡæntɪzəmz/", "vi": "bệnh khổng lồ do thừa hoóc môn tăng"},
  {"id": "lex.en.200k.064582", "hw": "glabellae", "pos": "noun", "ipa": "/ɡləˈbɛliː/", "vi": "vùng ấn đường phẳng giữa hai mày"},
  {"id": "lex.en.200k.064583", "hw": "glabellas", "pos": "noun", "ipa": "/ɡləˈbɛləz/", "vi": "phần ấn đường giữa hai lông mày"},
  {"id": "lex.en.200k.064584", "hw": "goncourts", "pos": "noun", "ipa": "/ɡɔːnˈkʊərz/", "vi": "nhà văn Pháp anh em nhà Goncourt"},
  {"id": "lex.en.200k.064585", "hw": "goodbies", "pos": "noun", "ipa": "/ɡʊdˈbaɪz/", "vi": "lời chào tạm biệt lúc chia tay"},
  {"id": "lex.en.200k.064586", "hw": "grots", "pos": "noun", "ipa": "/ɡrɑːts/", "vi": "hang động nhỏ ven đá tự nhiên (thơ)"},
  {"id": "lex.en.200k.064587", "hw": "haarts", "pos": "noun", "ipa": "/hɑːrts/", "vi": "liệu pháp điều trị HIV HAART"},
  {"id": "lex.en.200k.064588", "hw": "hackberries", "pos": "noun", "ipa": "/ˈhækˌbɛriz/", "vi": "cây cơm nguội vỏ xù quả mọng ngọt"},
  {"id": "lex.en.200k.064589", "hw": "handbills", "pos": "noun", "ipa": "/ˈhændbɪlz/", "vi": "tờ rơi quảng cáo phát tận tay"},
  {"id": "lex.en.200k.064590", "hw": "handcarts", "pos": "noun", "ipa": "/ˈhændkɑːrts/", "vi": "xe kéo đẩy hàng hóa nhỏ bằng tay"},
  {"id": "lex.en.200k.064591", "hw": "helianthuses", "pos": "noun", "ipa": "/ˌhiːliˈænθəsɪz/", "vi": "chi thực vật cây hoa hướng dương"},
  {"id": "lex.en.200k.064592", "hw": "hermosillos", "pos": "noun", "ipa": "/ˌɛrmoʊˈsiːoʊz/", "vi": "thành phố Hermosillo bang Sonora"},
  {"id": "lex.en.200k.064593", "hw": "hogsheads", "pos": "noun", "ipa": "/ˈhɔːɡzhɛdz/", "vi": "thùng gỗ sồi lớn đựng rượu vang bia"},
  {"id": "lex.en.200k.064594", "hw": "horsetails", "pos": "noun", "ipa": "/ˈhɔːrsteɪlz/", "vi": "cây cỏ tháp bút (đuôi ngựa) cổ đại"},
  {"id": "lex.en.200k.064595", "hw": "hypericums", "pos": "noun", "ipa": "/haɪˈpɛrɪkəmz/", "vi": "chi cây hoa ban Hypericum dược liệu"},
  {"id": "lex.en.200k.064596", "hw": "interrelations", "pos": "noun", "ipa": "/ˌɪntərɪˈleɪʃənz/", "vi": "mối tương quan qua lại với nhau"},
  {"id": "lex.en.200k.064597", "hw": "isomerizations", "pos": "noun", "ipa": "/aɪˌsɑːməraɪˈzeɪʃənz/", "vi": "quá trình đồng phân hóa hóa học"},
  {"id": "lex.en.200k.064598", "hw": "jawans", "pos": "noun", "ipa": "/dʒəˈwɑːnz/", "vi": "binh sĩ bộ binh cấp thấp Ấn Độ"},
  {"id": "lex.en.200k.064599", "hw": "karelians", "pos": "noun", "ipa": "/kəˈriːliənz/", "vi": "người dân và tiếng vùng Karelia"},
  {"id": "lex.en.200k.064600", "hw": "katmandus", "pos": "noun", "ipa": "/ˌkætmænˈduːz/", "vi": "thủ đô Kathmandu của nước Nepal"},
  {"id": "lex.en.200k.064601", "hw": "khufus", "pos": "noun", "ipa": "/ˈkuːfuːz/", "vi": "pharaon Khufu xây đại kim tự tháp"},
  {"id": "lex.en.200k.064602", "hw": "kineses", "pos": "noun", "ipa": "/kɪˈniːsiːz/", "vi": "phản ứng vận động vô hướng sinh vật"}
]

with open('scratch/b33_r10_raw_p1.json') as f:
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

with open('scratch/b33_r10_p1.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)
print("Saved scratch/b33_r10_p1.json OK")
