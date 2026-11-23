import json

records = [
    {"id": "lex.en.200k.057302", "hw": "adanas", "pos": "noun", "ipa": "/ˈɑːdənəz/", "vi": "các địa danh thành phố Adana"},
    {"id": "lex.en.200k.057303", "hw": "altarpieces", "pos": "noun", "ipa": "/ˈɔːltɚpiːsɪz/", "vi": "bức tranh thờ sau bàn thờ"},
    {"id": "lex.en.200k.057304", "hw": "andalucias", "pos": "noun", "ipa": "/ˌændəluːˈsiːəz/", "vi": "vùng Andalusia Tây Ban Nha"},
    {"id": "lex.en.200k.057305", "hw": "anthers", "pos": "noun", "ipa": "/ˈænθɚz/", "vi": "các bao phấn chứa phấn hoa"},
    {"id": "lex.en.200k.057306", "hw": "appliqued", "pos": "verb", "ipa": "/ˌæplɪˈkeɪd/", "vi": "đã đắp ren; đã may đắp nổi hoa văn"},
    {"id": "lex.en.200k.057307", "hw": "appliques", "pos": "noun", "ipa": "/ˌæplɪˈkeɪz/", "vi": "các hoa văn thêu đắp nổi"},
    {"id": "lex.en.200k.057308", "hw": "araks", "pos": "noun", "ipa": "/ˈærəks/", "vi": "các loại rượu arak mùi hồi"},
    {"id": "lex.en.200k.057309", "hw": "balancers", "pos": "noun", "ipa": "/ˈbælənsɚz/", "vi": "người làm xiếc thăng bằng"},
    {"id": "lex.en.200k.057310", "hw": "beefcakes", "pos": "noun", "ipa": "/ˈbiːfkeɪks/", "vi": "người đàn ông cơ bắp cuồn cuộn"},
    {"id": "lex.en.200k.057311", "hw": "behrenses", "pos": "noun", "ipa": "/ˈbɛrənzɪz/", "vi": "những người thuộc họ Behrens"},
    {"id": "lex.en.200k.057312", "hw": "benets", "pos": "noun", "ipa": "/bəˈneɪts/", "vi": "các người mang dòng họ Benét"},
    {"id": "lex.en.200k.057313", "hw": "bioterrorisms", "pos": "noun", "ipa": "/ˌbaɪoʊˈtɛrərɪzəmz/", "vi": "các hành vi khủng bố sinh học"},
    {"id": "lex.en.200k.057314", "hw": "blowfishes", "pos": "noun", "ipa": "/ˈbloʊfɪʃɪz/", "vi": "các loài cá nóc phồng mình"},
    {"id": "lex.en.200k.057315", "hw": "bondsmen", "pos": "noun", "ipa": "/ˈbɑːndzmən/", "vi": "người bảo lãnh tại ngoại"},
    {"id": "lex.en.200k.057316", "hw": "broadswords", "pos": "noun", "ipa": "/ˈbrɔːdsɔːrdz/", "vi": "thanh đại đao kiếm lưỡi rộng"},
    {"id": "lex.en.200k.057317", "hw": "brogues", "pos": "noun", "ipa": "/broʊɡz/", "vi": "giày da đục lỗ brogue; giọng mũi"},
    {"id": "lex.en.200k.057318", "hw": "carissas", "pos": "noun", "ipa": "/kəˈrɪsəz/", "vi": "bụi cây mận gai chi Carissa"},
    {"id": "lex.en.200k.057319", "hw": "chancelleries", "pos": "noun", "ipa": "/ˈtʃænsəlriz/", "vi": "văn phòng thủ tướng; tòa đại sứ"},
    {"id": "lex.en.200k.057320", "hw": "chitchats", "pos": "noun", "ipa": "/ˈtʃɪttʃæts/", "vi": "những câu chuyện phiếm gẫu"},
    {"id": "lex.en.200k.057321", "hw": "chitchatted", "pos": "verb", "ipa": "/ˈtʃɪttʃætɪd/", "vi": "đã trò chuyện phiếm gẫu vui vẻ"},
    {"id": "lex.en.200k.057322", "hw": "chitchatting", "pos": "verb", "ipa": "/ˈtʃɪttʃætɪŋ/", "vi": "đang chuyện trò tán gẫu"},
    {"id": "lex.en.200k.057323", "hw": "chokeholds", "pos": "noun", "ipa": "/ˈtʃoʊkhoʊldz/", "vi": "những đòn siết cổ khóa họng"},
    {"id": "lex.en.200k.057324", "hw": "cobwebs", "pos": "noun", "ipa": "/ˈkɑːbwɛbz/", "vi": "những màng tơ nhện bám bụi"},
    {"id": "lex.en.200k.057325", "hw": "complementarities", "pos": "noun", "ipa": "/ˌkɑːmpləmɛnˈtærətiz/", "vi": "tính bổ sung tương hỗ lẫn nhau"},
    {"id": "lex.en.200k.057326", "hw": "conakries", "pos": "noun", "ipa": "/kəˈnækriz/", "vi": "các thủ đô Conakry ở Guinea"},
    {"id": "lex.en.200k.057327", "hw": "daiquiris", "pos": "noun", "ipa": "/ˈdaɪkəriz/", "vi": "ly cocktail rượu rum daiquiri"},
    {"id": "lex.en.200k.057328", "hw": "demeraras", "pos": "noun", "ipa": "/ˌdɛməˈrærəz/", "vi": "các loại đường mía thô Demerara"},
    {"id": "lex.en.200k.057329", "hw": "digitizers", "pos": "noun", "ipa": "/ˈdɪdʒɪtaɪzɚz/", "vi": "các thiết bị số hóa bản vẽ"},
    {"id": "lex.en.200k.057330", "hw": "diwans", "pos": "noun", "ipa": "/dɪˈwɑːnz/", "vi": "hội đồng quốc vụ; ghế trường kỷ"},
    {"id": "lex.en.200k.057331", "hw": "elopements", "pos": "noun", "ipa": "/ɪˈloʊpmənts/", "vi": "những vụ trốn nhà đi theo tình yêu"},
    {"id": "lex.en.200k.057332", "hw": "elucidations", "pos": "noun", "ipa": "/ɪˌluːsɪˈdeɪʃənz/", "vi": "sự làm sáng tỏ; lời giải thích rõ"},
    {"id": "lex.en.200k.057333", "hw": "equivocations", "pos": "noun", "ipa": "/ɪˌkwɪvəˈkeɪʃənz/", "vi": "những lời nói nước đôi mập mờ"},
    {"id": "lex.en.200k.057334", "hw": "erlangs", "pos": "noun", "ipa": "/ˈɜːrlæŋz/", "vi": "đơn vị cường độ lưu lượng thoại"},
    {"id": "lex.en.200k.057335", "hw": "fagins", "pos": "noun", "ipa": "/ˈfeɪɡɪnz/", "vi": "kẻ đầu sỏ dạy trẻ con ăn cắp"},
    {"id": "lex.en.200k.057336", "hw": "fahds", "pos": "noun", "ipa": "/fɑːdz/", "vi": "các vị quốc vương mang tên Fahd"},
    {"id": "lex.en.200k.057337", "hw": "ficas", "pos": "noun", "ipa": "/ˈfaɪkəz/", "vi": "các khoản thuế bảo hiểm FICA Mỹ"},
    {"id": "lex.en.200k.057338", "hw": "frisches", "pos": "noun", "ipa": "/ˈfrɪʃɪz/", "vi": "các nhà khoa học mang họ Frisch"},
    {"id": "lex.en.200k.057339", "hw": "frisians", "pos": "noun", "ipa": "/ˈfrɪʒənz/", "vi": "người dân vùng Frisia ven biển"},
    {"id": "lex.en.200k.057340", "hw": "fuckheads", "pos": "noun", "ipa": "/ˈfʌkhɛdz/", "vi": "những kẻ ngu xuẩn; đồ đầu đất"},
    {"id": "lex.en.200k.057341", "hw": "generalissimos", "pos": "noun", "ipa": "/ˌdʒɛnərəˈlɪsɪmoʊz/", "vi": "đại thống soái tổng tư lệnh"},
    {"id": "lex.en.200k.057342", "hw": "gooks", "pos": "noun", "ipa": "/ɡuːks/", "vi": "từ miệt thị người phương Đông"},
    {"id": "lex.en.200k.057343", "hw": "goyim", "pos": "noun", "ipa": "/ˈɡɔɪɪm/", "vi": "người không theo đạo Do Thái"},
    {"id": "lex.en.200k.057344", "hw": "goys", "pos": "noun", "ipa": "/ɡɔɪz/", "vi": "người ngoài Do Thái; kẻ ngoại đạo"},
    {"id": "lex.en.200k.057345", "hw": "groundnuts", "pos": "noun", "ipa": "/ˈɡraʊndnʌts/", "vi": "củ lạc củ đậu phộng dưới đất"},
    {"id": "lex.en.200k.057346", "hw": "grumps", "pos": "noun", "ipa": "/ɡrʌmps/", "vi": "những người hay càu nhàu gắt gỏng"},
    {"id": "lex.en.200k.057347", "hw": "hoarier", "pos": "adj", "ipa": "/ˈhɔːriər/", "vi": "bạc trắng hơn; cổ hủ lâu đời hơn"},
    {"id": "lex.en.200k.057348", "hw": "hoariest", "pos": "adj", "ipa": "/ˈhɔːriɪst/", "vi": "bạc trắng nhất; cổ lỗ sĩ nhất"},
    {"id": "lex.en.200k.057349", "hw": "hoodlums", "pos": "noun", "ipa": "/ˈhʊdləmz/", "vi": "tên côn đồ lưu manh đầu gấu"},
    {"id": "lex.en.200k.057350", "hw": "hydrogels", "pos": "noun", "ipa": "/ˈhaɪdroʊdʒɛlz/", "vi": "các loại hydrogel ngậm nước"},
    {"id": "lex.en.200k.057351", "hw": "immensities", "pos": "noun", "ipa": "/ɪˈmɛnsətiz/", "vi": "sự bao la vô tận; cõi mênh mông"},
    {"id": "lex.en.200k.057352", "hw": "imputations", "pos": "noun", "ipa": "/ˌɪmpjʊˈteɪʃənz/", "vi": "sự quy kết tội lỗi; lời đổ tội"},
    {"id": "lex.en.200k.057353", "hw": "izzards", "pos": "noun", "ipa": "/ˈɪzɚdz/", "vi": "chữ cái Z; tên gọi cổ của chữ Z"},
    {"id": "lex.en.200k.057354", "hw": "jammieses", "pos": "noun", "ipa": "/ˈdʒæmizɪz/", "vi": "những bộ quần áo ngủ ấm áp"},
    {"id": "lex.en.200k.057355", "hw": "kongos", "pos": "noun", "ipa": "/ˈkɑːŋɡoʊz/", "vi": "người hoặc tiếng Congo ở châu Phi"},
    {"id": "lex.en.200k.057356", "hw": "largemouths", "pos": "noun", "ipa": "/ˈlɑːrdʒmaʊðz/", "vi": "cá vược đen miệng rộng"},
    {"id": "lex.en.200k.057357", "hw": "leukocytes", "pos": "noun", "ipa": "/ˈluːkəsaɪts/", "vi": "các tế bào bạch cầu trong máu"},
    {"id": "lex.en.200k.057358", "hw": "lipases", "pos": "noun", "ipa": "/ˈlɪpeɪsɪz/", "vi": "loại enzym phân giải mỡ lipase"},
    {"id": "lex.en.200k.057359", "hw": "lippis", "pos": "noun", "ipa": "/ˈlɪpiz/", "vi": "danh họa người Ý dòng họ Lippi"},
    {"id": "lex.en.200k.057360", "hw": "llms", "pos": "noun", "ipa": "/ˌɛl.ɛlˈɛmz/", "vi": "các văn bằng thạc sĩ luật học"},
    {"id": "lex.en.200k.057361", "hw": "lusitanias", "pos": "noun", "ipa": "/ˌluːsɪˈteɪniəz/", "vi": "tàu khách huyền thoại Lusitania"},
    {"id": "lex.en.200k.057362", "hw": "mafiosi", "pos": "noun", "ipa": "/ˌmɑːfiˈoʊsi/", "vi": "tay chân trùm băng đảng Mafia"},
    {"id": "lex.en.200k.057363", "hw": "manufactories", "pos": "noun", "ipa": "/ˌmænjʊˈfæktəriz/", "vi": "xưởng sản xuất chế tạo thủ công"},
    {"id": "lex.en.200k.057364", "hw": "marimbas", "pos": "noun", "ipa": "/məˈrɪmbəz/", "vi": "bộ đàn gõ phiến gỗ marimba"},
    {"id": "lex.en.200k.057365", "hw": "mauritanians", "pos": "noun", "ipa": "/ˌmɔːrɪˈteɪniənz/", "vi": "người dân quốc gia Mauritania"},
    {"id": "lex.en.200k.057366", "hw": "mestizoes", "pos": "noun", "ipa": "/mɛˈstiːzoʊz/", "vi": "người lai da trắng và thổ dân Mỹ"},
    {"id": "lex.en.200k.057367", "hw": "mestizos", "pos": "noun", "ipa": "/mɛˈstiːzoʊz/", "vi": "người lai dòng máu Tây Ban Nha"},
    {"id": "lex.en.200k.057368", "hw": "michaelmases", "pos": "noun", "ipa": "/ˈmɪkəlməsɪz/", "vi": "lễ hội Tổng Lãnh Thiên Thần"},
    {"id": "lex.en.200k.057369", "hw": "muckier", "pos": "adj", "ipa": "/ˈmʌkiər/", "vi": "nhớp nháp bùn lầy hơn; dơ dáy hơn"},
    {"id": "lex.en.200k.057370", "hw": "muckiest", "pos": "adj", "ipa": "/ˈmʌkiɪst/", "vi": "bùn lầy nhớp nháp nhất; dơ nhất"},
    {"id": "lex.en.200k.057371", "hw": "mudders", "pos": "noun", "ipa": "/ˈmʌdɚz/", "vi": "ngựa chạy giỏi trên đường bùn lầy"},
    {"id": "lex.en.200k.057372", "hw": "nationalized", "pos": "verb", "ipa": "/ˈnæʃnəlaɪzd/", "vi": "đã quốc hữu hóa tài sản xí nghiệp"},
    {"id": "lex.en.200k.057373", "hw": "nigellas", "pos": "noun", "ipa": "/naɪˈdʒɛləz/", "vi": "cây hoa thì là đen chi Nigella"},
    {"id": "lex.en.200k.057374", "hw": "numerators", "pos": "noun", "ipa": "/ˈnuːməreɪtɚz/", "vi": "chữ số tử số trong phân số"},
    {"id": "lex.en.200k.057375", "hw": "oises", "pos": "noun", "ipa": "/wɑːzɪz/", "vi": "dòng sông Oise ở miền bắc Pháp"},
    {"id": "lex.en.200k.057376", "hw": "oncogenes", "pos": "noun", "ipa": "/ˈɑːŋkoʊdʒiːnz/", "vi": "các gen đột biến sinh ung thư"},
    {"id": "lex.en.200k.057377", "hw": "outriggers", "pos": "noun", "ipa": "/ˈaʊtrɪɡɚz/", "vi": "càng phao cân bằng mạn thuyền"},
    {"id": "lex.en.200k.057378", "hw": "palominos", "pos": "noun", "ipa": "/ˌpæləˈmiːnoʊz/", "vi": "những con ngựa lông vàng bạch kim"},
    {"id": "lex.en.200k.057379", "hw": "pappi", "pos": "noun", "ipa": "/ˈpæpaɪ/", "vi": "mào lông tơ quả bồ công anh"},
    {"id": "lex.en.200k.057380", "hw": "pappuses", "pos": "noun", "ipa": "/ˈpæpəsɪz/", "vi": "mào lông tơ phát tán ở hạt hoa"},
    {"id": "lex.en.200k.057381", "hw": "pawnbrokers", "pos": "noun", "ipa": "/ˈpɔːnbroʊkɚz/", "vi": "chủ tiệm hiệu cầm đồ thế chấp"},
    {"id": "lex.en.200k.057382", "hw": "payees", "pos": "noun", "ipa": "/peɪˈiːz/", "vi": "người nhận tiền; người thụ hưởng"},
    {"id": "lex.en.200k.057383", "hw": "peatier", "pos": "adj", "ipa": "/ˈpiːtiər/", "vi": "chứa nhiều than bùn mục hơn"},
    {"id": "lex.en.200k.057384", "hw": "peatiest", "pos": "adj", "ipa": "/ˈpiːtiɪst/", "vi": "chứa nhiều than bùn mục nhất"},
    {"id": "lex.en.200k.057385", "hw": "perigees", "pos": "noun", "ipa": "/ˈpɛrɪdʒiːz/", "vi": "vị trí cận địa trong thiên văn"},
    {"id": "lex.en.200k.057386", "hw": "phenylalanines", "pos": "noun", "ipa": "/ˌfɛnəlˈæləniːnz/", "vi": "các axit amin phenylalanine"},
    {"id": "lex.en.200k.057387", "hw": "pinwheels", "pos": "noun", "ipa": "/ˈpɪnwiːlz/", "vi": "bánh xe chong chóng quay tròn"},
    {"id": "lex.en.200k.057388", "hw": "plexiglasses", "pos": "noun", "ipa": "/ˈplɛksɪɡlæsɪz/", "vi": "những tấm kính nhựa hữu cơ dẻo"},
    {"id": "lex.en.200k.057389", "hw": "preceptors", "pos": "noun", "ipa": "/prɪˈsɛptɚz/", "vi": "các giảng viên hướng dẫn sư phạm"},
    {"id": "lex.en.200k.057390", "hw": "prosodies", "pos": "noun", "ipa": "/ˈprɑːsədiz/", "vi": "phong cách thi luật ngữ điệu"},
    {"id": "lex.en.200k.057391", "hw": "pterodactyls", "pos": "noun", "ipa": "/ˌtɛrəˈdæktɪlz/", "vi": "loài thằn lằn bay tiền sử có cánh"},
    {"id": "lex.en.200k.057392", "hw": "rappahannocks", "pos": "noun", "ipa": "/ˌræpəˈhænəks/", "vi": "dòng sông Rappahannock ở Virginia"},
    {"id": "lex.en.200k.057393", "hw": "refectories", "pos": "noun", "ipa": "/rɪˈfɛktəriz/", "vi": "phòng ăn tập thể trong tu viện"},
    {"id": "lex.en.200k.057394", "hw": "roofers", "pos": "noun", "ipa": "/ˈruːfɚz/", "vi": "những người thợ lợp mái nhà"},
    {"id": "lex.en.200k.057395", "hw": "ruminations", "pos": "noun", "ipa": "/ˌruːmɪˈneɪʃənz/", "vi": "sự trầm ngâm suy tư sâu sắc"},
    {"id": "lex.en.200k.057396", "hw": "scrunched", "pos": "verb", "ipa": "/skrʌntʃt/", "vi": "đã vò nhàu nát; co rúm lại"},
    {"id": "lex.en.200k.057397", "hw": "scrunches", "pos": "noun", "ipa": "/ˈskrʌntʃɪz/", "vi": "tiếng cót két giòn; động tác gập"},
    {"id": "lex.en.200k.057398", "hw": "scrunching", "pos": "verb", "ipa": "/ˈskrʌntʃɪŋ/", "vi": "đang vò bẹp dí; nhăn nhúm lại"},
    {"id": "lex.en.200k.057399", "hw": "slippier", "pos": "adj", "ipa": "/ˈslɪpiər/", "vi": "trơn trượt dễ ngã hơn"},
    {"id": "lex.en.200k.057400", "hw": "slippiest", "pos": "adj", "ipa": "/ˈslɪpiɪst/", "vi": "trơn trượt dễ ngã nhất"},
    {"id": "lex.en.200k.057401", "hw": "slovenes", "pos": "noun", "ipa": "/ˈsloʊviːnz/", "vi": "người dân thuộc quốc gia Slovenia"}
]

# Validation
with open('scratch/b32_r05_raw_p4.json') as f:
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

with open('scratch/b32_r05_p4.json', 'w') as f:
    json.dump(final_p4, f, ensure_ascii=False, indent=2)
print("Part 4 validated and written successfully.")
