import json

items = [
  {"id": "lex.en.200k.061003", "hw": "sleepwalks", "pos": "verb", "ipa": "/ˈsliːpwɔːks/", "vi": "đi mộng du trong lúc ngủ"},
  {"id": "lex.en.200k.061004", "hw": "slipways", "pos": "noun", "ipa": "/ˈslɪpweɪz/", "vi": "đường triền dốc hạ thủy tàu thuyền"},
  {"id": "lex.en.200k.061005", "hw": "splayed", "pos": "verb", "ipa": "/spleɪd/", "vi": "đã xòe rộng ra; vát xiên cạnh"},
  {"id": "lex.en.200k.061006", "hw": "splaying", "pos": "verb", "ipa": "/ˈspleɪɪŋ/", "vi": "đang xòe banh rộng ra các phía"},
  {"id": "lex.en.200k.061007", "hw": "splays", "pos": "noun", "ipa": "/spleɪz/", "vi": "mặt vát xiên khuôn cửa; sự xòe ra"},
  {"id": "lex.en.200k.061008", "hw": "squiggles", "pos": "noun", "ipa": "/ˈskwɪɡəlz/", "vi": "nét vẽ ngoằn ngoèo uốn lượn"},
  {"id": "lex.en.200k.061009", "hw": "stomachaches", "pos": "noun", "ipa": "/ˈstʌməkˌeɪks/", "vi": "cơn đau bụng; chứng đau dạ dày"},
  {"id": "lex.en.200k.061010", "hw": "subluxations", "pos": "noun", "ipa": "/ˌsʌblʌkˈseɪʃənz/", "vi": "tình trạng bán trật khớp xương"},
  {"id": "lex.en.200k.061011", "hw": "sumpters", "pos": "noun", "ipa": "/ˈsʌmptərz/", "vi": "ngựa thồ hàng; la chở hành lý"},
  {"id": "lex.en.200k.061012", "hw": "sunnas", "pos": "noun", "ipa": "/ˈsʊnəz/", "vi": "kinh truyền thống Sunnah Hồi giáo"},
  {"id": "lex.en.200k.061013", "hw": "taguses", "pos": "noun", "ipa": "/ˈteɪɡəsɪz/", "vi": "dòng sông Tagus vùng Iberia"},
  {"id": "lex.en.200k.061014", "hw": "tamerlanes", "pos": "noun", "ipa": "/ˈtæmərleɪnz/", "vi": "hoàng đế chinh phạt Thiếp Mộc Nhi"},
  {"id": "lex.en.200k.061015", "hw": "tantaluses", "pos": "noun", "ipa": "/ˈtæntələsɪz/", "vi": "vua Tantalus bị đày thần thoại"},
  {"id": "lex.en.200k.061016", "hw": "tartus", "pos": "noun", "ipa": "/ˈtɑːrtuz/", "vi": "thành phố đại học Tartu Estonia"},
  {"id": "lex.en.200k.061017", "hw": "togoleses", "pos": "noun", "ipa": "/ˌtoʊɡəˈliːzɪz/", "vi": "người dân quốc gia Togo Tây Phi"},
  {"id": "lex.en.200k.061018", "hw": "tonsillectomies", "pos": "noun", "ipa": "/ˌtɑːnsəˈlɛktəmiz/", "vi": "phẫu thuật cắt bỏ amiđan họng"},
  {"id": "lex.en.200k.061019", "hw": "toscaninis", "pos": "noun", "ipa": "/ˌtɑːskəˈniːniz/", "vi": "nhạc trưởng Ý Arturo Toscanini"},
  {"id": "lex.en.200k.061020", "hw": "unmanlier", "pos": "adj", "ipa": "/ʌnˈmænliər/", "vi": "yếu đuối hèn nhát kém nam tính hơn"},
  {"id": "lex.en.200k.061021", "hw": "unmanliest", "pos": "adj", "ipa": "/ʌnˈmænliɪst/", "vi": "kém nam tính nhất; nhu nhược nhất"},
  {"id": "lex.en.200k.061022", "hw": "unquieter", "pos": "adj", "ipa": "/ʌnˈkwaɪətər/", "vi": "bồn chồn lo âu hơn; bất an hơn"},
  {"id": "lex.en.200k.061023", "hw": "unquietest", "pos": "adj", "ipa": "/ʌnˈkwaɪətɪst/", "vi": "bất an xáo trộn nhất; bất ổn nhất"},
  {"id": "lex.en.200k.061024", "hw": "verifiers", "pos": "noun", "ipa": "/ˈvɛrɪfaɪərz/", "vi": "người xác minh; bộ kiểm chứng lỗi"},
  {"id": "lex.en.200k.061025", "hw": "vulpeses", "pos": "noun", "ipa": "/ˈvʌlpiːzɪz/", "vi": "chi cáo đỏ thông minh Vulpes"},
  {"id": "lex.en.200k.061026", "hw": "waggons", "pos": "noun", "ipa": "/ˈwæɡənz/", "vi": "xe ngựa bốn bánh chở hàng hóa"},
  {"id": "lex.en.200k.061027", "hw": "zanucks", "pos": "noun", "ipa": "/ˈzænəks/", "vi": "nhà sản xuất phim Darryl Zanuck"},
  {"id": "lex.en.200k.061028", "hw": "zoroasters", "pos": "noun", "ipa": "/ˌzɔːroʊˈæstərz/", "vi": "nhà tiên tri Ba Tư Zarathustra"},
  {"id": "lex.en.200k.061029", "hw": "acanthuses", "pos": "noun", "ipa": "/əˈkænθəsɪz/", "vi": "cây ô rô lá gai; họa tiết ô rô"},
  {"id": "lex.en.200k.061030", "hw": "acherons", "pos": "noun", "ipa": "/ˈækərɑːnz/", "vi": "con sông sầu Acheron cõi âm ti"},
  {"id": "lex.en.200k.061031", "hw": "acrylates", "pos": "noun", "ipa": "/ˈækrəleɪts/", "vi": "nhựa tổng hợp polyme acrylat"},
  {"id": "lex.en.200k.061032", "hw": "amharas", "pos": "noun", "ipa": "/æmˈhɑːrəz/", "vi": "dân tộc chính Amhara ở Ethiopia"},
  {"id": "lex.en.200k.061033", "hw": "anxiolytics", "pos": "noun", "ipa": "/ˌæŋkzioʊˈlɪtɪks/", "vi": "thuốc giảm lo âu an thần"},
  {"id": "lex.en.200k.061034", "hw": "arpeggios", "pos": "noun", "ipa": "/ɑːrˈpɛdʒioʊz/", "vi": "hợp âm rải nốt nhạc lần lượt"},
  {"id": "lex.en.200k.061035", "hw": "askers", "pos": "noun", "ipa": "/ˈæskərz/", "vi": "người đặt câu hỏi; người thỉnh cầu"},
  {"id": "lex.en.200k.061036", "hw": "bantings", "pos": "noun", "ipa": "/ˈbæntɪŋz/", "vi": "bác sĩ tìm insulin Banting"},
  {"id": "lex.en.200k.061037", "hw": "batwings", "pos": "noun", "ipa": "/ˈbætwɪŋz/", "vi": "cánh dơi; cửa lùa đôi quán rượu"},
  {"id": "lex.en.200k.061038", "hw": "benedicks", "pos": "noun", "ipa": "/ˈbɛnədɪks/", "vi": "người đàn ông mới cưới vợ"},
  {"id": "lex.en.200k.061039", "hw": "blighties", "pos": "noun", "ipa": "/ˈblaɪtiz/", "vi": "tên thân mật quê hương nước Anh"},
  {"id": "lex.en.200k.061040", "hw": "broglies", "pos": "noun", "ipa": "/də ˈbrɔɪz/", "vi": "nhà vật lý lượng tử de Broglie"},
  {"id": "lex.en.200k.061041", "hw": "bruegels", "pos": "noun", "ipa": "/ˈbrɔɪɡəlz/", "vi": "danh họa Phục hưng Pieter Bruegel"},
  {"id": "lex.en.200k.061042", "hw": "bubblers", "pos": "noun", "ipa": "/ˈbʌblərz/", "vi": "vòi phun nước uống công cộng"},
  {"id": "lex.en.200k.061043", "hw": "buckthorns", "pos": "noun", "ipa": "/ˈbʌkθɔːrnz/", "vi": "cây bụi gai hắc mai quả đen"},
  {"id": "lex.en.200k.061044", "hw": "buhls", "pos": "noun", "ipa": "/buːlz/", "vi": "đồ gỗ khảm kim loại kiểu Boulle"},
  {"id": "lex.en.200k.061045", "hw": "cadenzas", "pos": "noun", "ipa": "/kəˈdɛnzəz/", "vi": "đoạn nhạc độc tấu cuối bản nhạc"},
  {"id": "lex.en.200k.061046", "hw": "camisoles", "pos": "noun", "ipa": "/ˈkæmɪsoʊlz/", "vi": "áo lót hai dây mỏng của phụ nữ"},
  {"id": "lex.en.200k.061047", "hw": "caputs", "pos": "noun", "ipa": "/ˈkæpəts/", "vi": "chỏm đầu xương; hội đồng đại học"},
  {"id": "lex.en.200k.061048", "hw": "cephalopods", "pos": "noun", "ipa": "/ˈsɛfələpɑːdz/", "vi": "động vật thân mềm lớp chân đầu"},
  {"id": "lex.en.200k.061049", "hw": "chalcedons", "pos": "noun", "ipa": "/kælˈsiːdənz/", "vi": "thành phố cổ Chalcedon Thổ Nhĩ Kỳ"},
  {"id": "lex.en.200k.061050", "hw": "chancellorsvilles", "pos": "noun", "ipa": "/ˈtʃænsələrzvɪlz/", "vi": "trận Chancellorsville Nội chiến Mỹ"},
  {"id": "lex.en.200k.061051", "hw": "chisinaus", "pos": "noun", "ipa": "/ˌkiːʃɪˈnaʊz/", "vi": "thủ đô Chișinău của nước Moldova"},
  {"id": "lex.en.200k.061052", "hw": "clomids", "pos": "noun", "ipa": "/ˈkloʊmɪdz/", "vi": "thuốc kích thích rụng trứng Clomid"},
  {"id": "lex.en.200k.061053", "hw": "cordays", "pos": "noun", "ipa": "/kɔːrˈdeɪz/", "vi": "nữ sát thủ Charlotte Corday Pháp"},
  {"id": "lex.en.200k.061054", "hw": "counterrevolutionaries", "pos": "noun", "ipa": "/ˌkaʊntərˌrɛvəˈluːʃənɛriz/", "vi": "phần tử phản cách mạng chống đối"},
  {"id": "lex.en.200k.061055", "hw": "debasements", "pos": "noun", "ipa": "/dɪˈbeɪsmənts/", "vi": "sự làm giảm giá trị; sự suy đồi"},
  {"id": "lex.en.200k.061056", "hw": "dermas", "pos": "noun", "ipa": "/ˈdɜːrməz/", "vi": "lớp trung bì nằm dưới biểu bì da"},
  {"id": "lex.en.200k.061057", "hw": "detents", "pos": "noun", "ipa": "/dɪˈtɛnts/", "vi": "chốt hãm định vị cơ khí lò xo"},
  {"id": "lex.en.200k.061058", "hw": "disputations", "pos": "noun", "ipa": "/ˌdɪspjʊˈteɪʃənz/", "vi": "cuộc tranh luận học thuật gay gắt"},
  {"id": "lex.en.200k.061059", "hw": "doualas", "pos": "noun", "ipa": "/duːˈɑːləz/", "vi": "thành phố cảng lớn Douala Cameroon"},
  {"id": "lex.en.200k.061060", "hw": "doubletrees", "pos": "noun", "ipa": "/ˈdʌbltriːz/", "vi": "đòn ngang nối hai ngựa kéo xe"},
  {"id": "lex.en.200k.061061", "hw": "duelists", "pos": "noun", "ipa": "/ˈduːəlɪsts/", "vi": "người đấu súng đấu kiếm tay đôi"},
  {"id": "lex.en.200k.061062", "hw": "ephemerises", "pos": "noun", "ipa": "/ɪˈfɛmərɪsɪz/", "vi": "lịch thiên văn quỹ đạo hành tinh"},
  {"id": "lex.en.200k.061063", "hw": "eyepatches", "pos": "noun", "ipa": "/ˈaɪpætʃɪz/", "vi": "miếng băng che mắt bị thương"},
  {"id": "lex.en.200k.061064", "hw": "faberges", "pos": "noun", "ipa": "/ˌfæbərˈʒeɪz/", "vi": "nghệ nhân kim hoàn trứng Fabergé"},
  {"id": "lex.en.200k.061065", "hw": "folies", "pos": "noun", "ipa": "/ˈfoʊliz/", "vi": "chứng hoang tưởng tâm thần"},
  {"id": "lex.en.200k.061066", "hw": "gastrectomies", "pos": "noun", "ipa": "/ɡæsˈtrɛktəmiz/", "vi": "phẫu thuật cắt bỏ phần dạ dày"},
  {"id": "lex.en.200k.061067", "hw": "glugged", "pos": "verb", "ipa": "/ɡlʌɡd/", "vi": "đã chảy òng ọc qua cổ chai hẹp"},
  {"id": "lex.en.200k.061068", "hw": "glugging", "pos": "verb", "ipa": "/ˈɡlʌɡɪŋ/", "vi": "đang chảy kêu òng ọc từng ngụm"},
  {"id": "lex.en.200k.061069", "hw": "glugs", "pos": "verb", "ipa": "/ɡlʌɡz/", "vi": "chảy kêu òng ọc; uống từng ngụm lớn"},
  {"id": "lex.en.200k.061070", "hw": "glutes", "pos": "noun", "ipa": "/ɡluːts/", "vi": "nhóm cơ mông lớn nâng đỡ đùi"},
  {"id": "lex.en.200k.061071", "hw": "haeckels", "pos": "noun", "ipa": "/ˈhɛkəlz/", "vi": "nhà sinh vật học Đức Ernst Haeckel"},
  {"id": "lex.en.200k.061072", "hw": "handicappers", "pos": "noun", "ipa": "/ˈhændikæpərz/", "vi": "chuyên gia phân hạng chấp cá cược"},
  {"id": "lex.en.200k.061073", "hw": "harrods", "pos": "noun", "ipa": "/ˈhærədz/", "vi": "trung tâm bách hóa cao cấp Harrods"},
  {"id": "lex.en.200k.061074", "hw": "hibbings", "pos": "noun", "ipa": "/ˈhɪbɪŋz/", "vi": "thị trấn mỏ sắt Hibbing Minnesota"},
  {"id": "lex.en.200k.061075", "hw": "hibernias", "pos": "noun", "ipa": "/haɪˈbɜːrniəz/", "vi": "tên gọi cổ điển đảo Ireland"},
  {"id": "lex.en.200k.061076", "hw": "hotpots", "pos": "noun", "ipa": "/ˈhɑːtpɑːts/", "vi": "món lẩu nóng; thịt hầm khoai tây"},
  {"id": "lex.en.200k.061077", "hw": "houseplants", "pos": "noun", "ipa": "/ˈhaʊsplænts/", "vi": "cây cảnh trồng chậu trong nhà"},
  {"id": "lex.en.200k.061078", "hw": "hydrographies", "pos": "noun", "ipa": "/haɪˈdrɑːɡrəfiz/", "vi": "ngành thủy đạc học đo vẽ vùng nước"},
  {"id": "lex.en.200k.061079", "hw": "hypogonadisms", "pos": "noun", "ipa": "/ˌhaɪpoʊˈɡoʊnædɪzəmz/", "vi": "chứng suy giảm chức năng sinh dục"},
  {"id": "lex.en.200k.061080", "hw": "intagli", "pos": "noun", "ipa": "/ɪnˈtɑːli/", "vi": "kỹ thuật khắc chìm đá quý bản in"},
  {"id": "lex.en.200k.061081", "hw": "intaglios", "pos": "noun", "ipa": "/ɪnˈtɑːlioʊz/", "vi": "tác phẩm khắc chìm nghệ thuật"},
  {"id": "lex.en.200k.061082", "hw": "ischias", "pos": "noun", "ipa": "/ˈɪskiəz/", "vi": "đảo núi lửa suối khoáng Ischia Ý"},
  {"id": "lex.en.200k.061083", "hw": "jawbreakers", "pos": "noun", "ipa": "/ˈdʒɔːbreɪkərz/", "vi": "viên kẹo cứng tròn; từ khó phát âm"},
  {"id": "lex.en.200k.061084", "hw": "jowetts", "pos": "noun", "ipa": "/ˈdʒaʊɪts/", "vi": "học giả Oxford Benjamin Jowett"},
  {"id": "lex.en.200k.061085", "hw": "kasbahs", "pos": "noun", "ipa": "/ˈkæzbɑːz/", "vi": "khu thành cổ Bắc Phi; pháo đài cổ"},
  {"id": "lex.en.200k.061086", "hw": "klaxons", "pos": "noun", "ipa": "/ˈklæksənz/", "vi": "còi bóp ô tô kêu to; còi báo động"},
  {"id": "lex.en.200k.061087", "hw": "krakatoas", "pos": "noun", "ipa": "/ˌkrækəˈtoʊəz/", "vi": "đảo núi lửa Krakatoa Indonesia"},
  {"id": "lex.en.200k.061088", "hw": "lectins", "pos": "noun", "ipa": "/ˈlɛktɪnz/", "vi": "protein gắn kết đường lectin"},
  {"id": "lex.en.200k.061089", "hw": "lobelias", "pos": "noun", "ipa": "/loʊˈbiːliəz/", "vi": "cây hoa lobelia cánh xanh tím rũ"},
  {"id": "lex.en.200k.061090", "hw": "lodgepoles", "pos": "noun", "ipa": "/ˈlɑːdʒpoʊlz/", "vi": "cây thông thân thẳng làm cột lều"},
  {"id": "lex.en.200k.061091", "hw": "lyonnaises", "pos": "noun", "ipa": "/ˌlaɪəˈneɪzɪz/", "vi": "món ăn kiểu vùng Lyon Pháp"},
  {"id": "lex.en.200k.061092", "hw": "macleishes", "pos": "noun", "ipa": "/məˈkliːʃɪz/", "vi": "nhà thơ Mỹ Archibald MacLeish"},
  {"id": "lex.en.200k.061093", "hw": "maidservants", "pos": "noun", "ipa": "/ˈmeɪdsɜːrvənts/", "vi": "nữ hầu gái giúp việc trong nhà"},
  {"id": "lex.en.200k.061094", "hw": "marquands", "pos": "noun", "ipa": "/ˈmɑːrkwɑːndz/", "vi": "tiểu thuyết gia Mỹ John Marquand"},
  {"id": "lex.en.200k.061095", "hw": "marris", "pos": "noun", "ipa": "/ˈmærɪs/", "vi": "cây bạch đàn đỏ marri nước Úc"},
  {"id": "lex.en.200k.061096", "hw": "masturbators", "pos": "noun", "ipa": "/ˈmæstərbeɪtərz/", "vi": "người tự kích thích sinh lý"},
  {"id": "lex.en.200k.061097", "hw": "minicabs", "pos": "noun", "ipa": "/ˈmɪnikæbz/", "vi": "xe taxi đặt trước ở nước Anh"},
  {"id": "lex.en.200k.061098", "hw": "monoplanes", "pos": "noun", "ipa": "/ˈmɑːnəpleɪnz/", "vi": "máy bay thiết kế một tầng cánh"},
  {"id": "lex.en.200k.061099", "hw": "multiplexers", "pos": "noun", "ipa": "/ˈmʌltɪplɛksərz/", "vi": "bộ dồn ghép kênh tín hiệu điện tử"},
  {"id": "lex.en.200k.061100", "hw": "naturalisations", "pos": "noun", "ipa": "/ˌnætʃərəlaɪˈzeɪʃənz/", "vi": "quá trình nhập quốc tịch công dân"},
  {"id": "lex.en.200k.061101", "hw": "nectarines", "pos": "noun", "ipa": "/ˌnɛktəˈriːnz/", "vi": "quả xuân đào vỏ nhẵn ruột ngọt"},
  {"id": "lex.en.200k.061102", "hw": "newsboys", "pos": "noun", "ipa": "/ˈnuːzbɔɪz/", "vi": "cậu bé bán báo dạo trên đường phố"}
]

with open('scratch/b33_r03_raw_p1.json') as f:
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

with open('scratch/b33_r03_p1.json', 'w') as f:
    json.dump(raw, f, ensure_ascii=False, indent=2)

print("Batch 33 Round 3 Part 1 validated and written successfully.")
