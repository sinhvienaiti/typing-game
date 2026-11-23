import json

records = [
    {"id": "lex.en.200k.057702", "hw": "divestitures", "pos": "noun", "ipa": "/daɪˈvɛstɪtʃɚz/", "vi": "sự thoái vốn; sự bán bớt tài sản"},
    {"id": "lex.en.200k.057703", "hw": "donbases", "pos": "noun", "ipa": "/ˈdɑːnbæsɪz/", "vi": "vùng bồn trũng than đá Donbas"},
    {"id": "lex.en.200k.057704", "hw": "earlobes", "pos": "noun", "ipa": "/ˈɪrloʊbz/", "vi": "các dái tai mềm ở vành tai"},
    {"id": "lex.en.200k.057705", "hw": "echidnae", "pos": "noun", "ipa": "/ɪˈkɪdniː/", "vi": "các con thú lông nhím mỏ vịt Úc"},
    {"id": "lex.en.200k.057706", "hw": "ervings", "pos": "noun", "ipa": "/ˈɜːrvɪŋz/", "vi": "huyền thoại bóng rổ Julius Erving"},
    {"id": "lex.en.200k.057707", "hw": "fuckups", "pos": "noun", "ipa": "/ˈfʌkʌps/", "vi": "những sai lầm tai hại ngớ ngẩn"},
    {"id": "lex.en.200k.057708", "hw": "gambians", "pos": "noun", "ipa": "/ˈɡæmbiənz/", "vi": "người dân quốc gia Gambia châu Phi"},
    {"id": "lex.en.200k.057709", "hw": "gamekeepers", "pos": "noun", "ipa": "/ˈɡeɪmkiːpɚz/", "vi": "những người coi sóc rừng săn bắn"},
    {"id": "lex.en.200k.057710", "hw": "hamelins", "pos": "noun", "ipa": "/ˈhæməlɪnz/", "vi": "thị trấn Hamelin cổ tích nước Đức"},
    {"id": "lex.en.200k.057711", "hw": "imus", "pos": "noun", "ipa": "/ˈaɪ.ɛmˈjuːz/", "vi": "phong trào Hồi giáo IMU Trung Á"},
    {"id": "lex.en.200k.057712", "hw": "intentionalities", "pos": "noun", "ipa": "/ɪnˌtɛnʃəˈnælətiz/", "vi": "tính chủ ý; tính định hướng ý thức"},
    {"id": "lex.en.200k.057713", "hw": "kaabas", "pos": "noun", "ipa": "/ˈkɑːbəz/", "vi": "đền thờ hình khối vuông Kaaba Mecca"},
    {"id": "lex.en.200k.057714", "hw": "lapdogs", "pos": "noun", "ipa": "/ˈlæpdɔːɡz/", "vi": "chó cưng ẵm lòng; kẻ phục tùng"},
    {"id": "lex.en.200k.057715", "hw": "laterans", "pos": "noun", "ipa": "/ˈlætərənz/", "vi": "vương cung thánh đường Lateran"},
    {"id": "lex.en.200k.057716", "hw": "magnifiers", "pos": "noun", "ipa": "/ˈmæɡnɪfaɪɚz/", "vi": "kính lúp cầm tay; thấu kính phóng"},
    {"id": "lex.en.200k.057717", "hw": "manillas", "pos": "noun", "ipa": "/məˈnɪləz/", "vi": "giấy bìa manila dẻo; xì gà Manila"},
    {"id": "lex.en.200k.057718", "hw": "marseillaises", "pos": "noun", "ipa": "/ˌmɑːrsəˈjeɪzɪz/", "vi": "bản quốc ca Pháp La Marseillaise"},
    {"id": "lex.en.200k.057719", "hw": "miladies", "pos": "noun", "ipa": "/mɪˈleɪdiz/", "vi": "tiếng xưng hô các lệnh bà phu nhân"},
    {"id": "lex.en.200k.057720", "hw": "mudslides", "pos": "noun", "ipa": "/ˈmʌdslaɪdz/", "vi": "các vụ lở bùn đất sạt lở dữ dội"},
    {"id": "lex.en.200k.057721", "hw": "mujahids", "pos": "noun", "ipa": "/mʊˈdʒɑːhɪdz/", "vi": "các chiến binh thánh chiến Hồi giáo"},
    {"id": "lex.en.200k.057722", "hw": "neurogeneses", "pos": "noun", "ipa": "/ˌnʊəroʊˈdʒɛnəsɪsɪz/", "vi": "quá trình sinh tế bào thần kinh mới"},
    {"id": "lex.en.200k.057723", "hw": "neutrophils", "pos": "noun", "ipa": "/ˈnuːtrəfɪlz/", "vi": "các bạch cầu trung tính miễn dịch"},
    {"id": "lex.en.200k.057724", "hw": "particularities", "pos": "noun", "ipa": "/pɚˌtɪkjʊˈlærətiz/", "vi": "đặc thù riêng biệt; chi tiết cụ thể"},
    {"id": "lex.en.200k.057725", "hw": "peppercorns", "pos": "noun", "ipa": "/ˈpɛpɚkɔːrnz/", "vi": "hạt hồ tiêu khô; tiền tượng trưng"},
    {"id": "lex.en.200k.057726", "hw": "perfumeries", "pos": "noun", "ipa": "/pɚˈfjuːməriz/", "vi": "cửa hiệu bán nước hoa tinh dầu"},
    {"id": "lex.en.200k.057727", "hw": "pharisees", "pos": "noun", "ipa": "/ˈfærɪsiːz/", "vi": "người Pha-ri-si; kẻ đạo đức giả"},
    {"id": "lex.en.200k.057728", "hw": "pocatellos", "pos": "noun", "ipa": "/ˌpoʊkəˈtɛloʊz/", "vi": "địa danh thành phố Pocatello Idaho"},
    {"id": "lex.en.200k.057729", "hw": "podiatrists", "pos": "noun", "ipa": "/poʊˈdaɪətrɪsts/", "vi": "bác sĩ chuyên khoa chữa bàn chân"},
    {"id": "lex.en.200k.057730", "hw": "polysaccharides", "pos": "noun", "ipa": "/ˌpɑːliˈsækəraɪdz/", "vi": "các hợp chất đa đường polysaccarit"},
    {"id": "lex.en.200k.057731", "hw": "potemkins", "pos": "noun", "ipa": "/poʊˈtɛmkɪnz/", "vi": "chiến hạm Potemkin; vỏ bọc giả tạo"},
    {"id": "lex.en.200k.057732", "hw": "powhatans", "pos": "noun", "ipa": "/ˈpaʊhətænz/", "vi": "tù trưởng Powhatan thổ dân Virginia"},
    {"id": "lex.en.200k.057733", "hw": "quebecoides", "pos": "noun", "ipa": "/keɪˌbɛkˈwɑːz/", "vi": "người Québec nói tiếng Pháp"},
    {"id": "lex.en.200k.057734", "hw": "redeyes", "pos": "noun", "ipa": "/ˈrɛdaɪz/", "vi": "chuyến bay đêm muộn; rượu mạnh"},
    {"id": "lex.en.200k.057735", "hw": "resounded", "pos": "verb", "ipa": "/rɪˈzaʊndɪd/", "vi": "đã vang dội rền vang; đã nổi tiếng"},
    {"id": "lex.en.200k.057736", "hw": "resounds", "pos": "verb", "ipa": "/rɪˈzaʊndz/", "vi": "vang dội rền vang; nổi tiếng khắp"},
    {"id": "lex.en.200k.057737", "hw": "rheins", "pos": "noun", "ipa": "/raɪnz/", "vi": "các con sông Rhein; hợp chất rhein"},
    {"id": "lex.en.200k.057738", "hw": "romanies", "pos": "noun", "ipa": "/ˈroʊməniz/", "vi": "người Di-gan; ngôn ngữ Romani"},
    {"id": "lex.en.200k.057739", "hw": "runabouts", "pos": "noun", "ipa": "/ˈrʌnəbaʊts/", "vi": "xe ô tô cỡ nhỏ gọn; ca nô du ngoạn"},
    {"id": "lex.en.200k.057740", "hw": "sardises", "pos": "noun", "ipa": "/ˈsɑːrdɪsɪz/", "vi": "thành phố cổ Sardis xứ Lydia"},
    {"id": "lex.en.200k.057741", "hw": "saussures", "pos": "noun", "ipa": "/soʊˈsjʊrz/", "vi": "nhà ngôn ngữ học Thụy Sĩ Saussure"},
    {"id": "lex.en.200k.057742", "hw": "schnauzers", "pos": "noun", "ipa": "/ˈʃnaʊzɚz/", "vi": "loài chó sục có râu mép Schnauzer"},
    {"id": "lex.en.200k.057743", "hw": "schoolrooms", "pos": "noun", "ipa": "/ˈskuːlruːmz/", "vi": "các phòng học lớp học ở trường"},
    {"id": "lex.en.200k.057744", "hw": "semicircles", "pos": "noun", "ipa": "/ˈsɛmisɜːrkəlz/", "vi": "các hình bán nguyệt nửa vòng tròn"},
    {"id": "lex.en.200k.057745", "hw": "setts", "pos": "noun", "ipa": "/sɛts/", "vi": "khối đá chữ nhật lát đường phố"},
    {"id": "lex.en.200k.057746", "hw": "sextets", "pos": "noun", "ipa": "/sɛksˈtɛts/", "vi": "các ban nhạc nhóm nhạc sáu người"},
    {"id": "lex.en.200k.057747", "hw": "shojis", "pos": "noun", "ipa": "/ˈʃoʊdʒiːz/", "vi": "cửa trượt giấy mờ shoji Nhật Bản"},
    {"id": "lex.en.200k.057748", "hw": "souffles", "pos": "noun", "ipa": "/ˈsuːfleɪz/", "vi": "món bánh phồng nướng xốp xúp-lê"},
    {"id": "lex.en.200k.057749", "hw": "spandaus", "pos": "noun", "ipa": "/ˈʃpændaʊz/", "vi": "súng máy Spandau; nhà tù Spandau"},
    {"id": "lex.en.200k.057750", "hw": "speeders", "pos": "noun", "ipa": "/ˈspiːdɚz/", "vi": "tài xế lái xe vượt quá tốc độ"},
    {"id": "lex.en.200k.057751", "hw": "straighteners", "pos": "noun", "ipa": "/ˈstreɪtənɚz/", "vi": "máy kẹp duỗi tóc; dụng cụ làm thẳng"},
    {"id": "lex.en.200k.057752", "hw": "strindbergs", "pos": "noun", "ipa": "/ˈstrɪndbɜːrɡz/", "vi": "kịch gia Thụy Điển Strindberg"},
    {"id": "lex.en.200k.057753", "hw": "sukarnos", "pos": "noun", "ipa": "/suːˈkɑːrnoʊz/", "vi": "tổng thống lập quốc Sukarno"},
    {"id": "lex.en.200k.057754", "hw": "suppositories", "pos": "noun", "ipa": "/səˈpɑːzɪtɔːriz/", "vi": "các viên thuốc đạn đặt hậu môn"},
    {"id": "lex.en.200k.057755", "hw": "tamperes", "pos": "noun", "ipa": "/ˈtɑːmpəreɪz/", "vi": "thành phố lớn Tampere Phần Lan"},
    {"id": "lex.en.200k.057756", "hw": "tangas", "pos": "noun", "ipa": "/ˈtæŋɡəz/", "vi": "quần lót dây tanga; đồng tiền tanga"},
    {"id": "lex.en.200k.057757", "hw": "teargases", "pos": "noun", "ipa": "/ˈtɪrɡæsɪz/", "vi": "các loại khí hơi cay giải tán"},
    {"id": "lex.en.200k.057758", "hw": "threonines", "pos": "noun", "ipa": "/ˈθriːəniːnz/", "vi": "các phân tử axit amin threonine"},
    {"id": "lex.en.200k.057759", "hw": "timekeepers", "pos": "noun", "ipa": "/ˈtaɪmkiːpɚz/", "vi": "nhân viên bấm giờ; người chấm công"},
    {"id": "lex.en.200k.057760", "hw": "tizzies", "pos": "noun", "ipa": "/ˈtɪziz/", "vi": "trạng thái cuống cuồng cuống quýt"},
    {"id": "lex.en.200k.057761", "hw": "tourettes", "pos": "noun", "ipa": "/tʊˈrɛts/", "vi": "hội chứng rối loạn Tic Tourette"},
    {"id": "lex.en.200k.057762", "hw": "towners", "pos": "noun", "ipa": "/ˈtaʊnɚz/", "vi": "cư dân sống lâu năm ở thị trấn"},
    {"id": "lex.en.200k.057763", "hw": "trapezoids", "pos": "noun", "ipa": "/ˈtræpəzɔɪdz/", "vi": "hình thang; xương thang ở bàn tay"},
    {"id": "lex.en.200k.057764", "hw": "waggoners", "pos": "noun", "ipa": "/ˈwæɡənɚz/", "vi": "người đánh xe ngựa kéo chở hàng"},
    {"id": "lex.en.200k.057765", "hw": "wahhabisms", "pos": "noun", "ipa": "/wəˈhɑːbɪzəmz/", "vi": "phong trào Hồi giáo bảo thủ Wahhabi"},
    {"id": "lex.en.200k.057766", "hw": "zarias", "pos": "noun", "ipa": "/zɑːˈriːəz/", "vi": "thành phố Zaria ở miền bắc Nigeria"},
    {"id": "lex.en.200k.057767", "hw": "achromatic color", "pos": "phrase", "ipa": "", "vi": "màu vô sắc; màu đen trắng xám"},
    {"id": "lex.en.200k.057768", "hw": "achromatic colour", "pos": "phrase", "ipa": "", "vi": "màu không sắc không có sắc tố"},
    {"id": "lex.en.200k.057769", "hw": "achromatic lens", "pos": "phrase", "ipa": "", "vi": "thấu kính tiêu sắc khử sắc sai"},
    {"id": "lex.en.200k.057770", "hw": "achromatic vision", "pos": "phrase", "ipa": "", "vi": "thị giác đen trắng không màu"},
    {"id": "lex.en.200k.057771", "hw": "agnus dei", "pos": "phrase", "ipa": "", "vi": "Chiên Thiên Chúa trong phụng vụ"},
    {"id": "lex.en.200k.057772", "hw": "airedale terrier", "pos": "phrase", "ipa": "", "vi": "chó sục cảnh lớn giống Airedale"},
    {"id": "lex.en.200k.057773", "hw": "algonquian language", "pos": "phrase", "ipa": "", "vi": "nhóm ngữ hệ bản địa Algonquian"},
    {"id": "lex.en.200k.057774", "hw": "amaryllis belladonna", "pos": "phrase", "ipa": "", "vi": "hoa huệ chuông Amaryllis belladonna"},
    {"id": "lex.en.200k.057775", "hw": "basilar artery", "pos": "phrase", "ipa": "", "vi": "động mạch thân nền nuôi não"},
    {"id": "lex.en.200k.057776", "hw": "basilar membrane", "pos": "phrase", "ipa": "", "vi": "màng đáy nền thụ cảm ốc tai"},
    {"id": "lex.en.200k.057777", "hw": "benoit mandelbrot", "pos": "phrase", "ipa": "", "vi": "nhà toán học Benoit Mandelbrot"},
    {"id": "lex.en.200k.057778", "hw": "bermudian rig", "pos": "phrase", "ipa": "", "vi": "kiểu cánh buồm tam giác Bermuda"},
    {"id": "lex.en.200k.057779", "hw": "candy striper", "pos": "phrase", "ipa": "", "vi": "tình nguyện viên trẻ bệnh viện"},
    {"id": "lex.en.200k.057780", "hw": "catechetical instruction", "pos": "phrase", "ipa": "", "vi": "lời dạy giáo lý theo lối vấn đáp"},
    {"id": "lex.en.200k.057781", "hw": "coaling station", "pos": "phrase", "ipa": "", "vi": "trạm tiếp than đá cho tàu thuyền"},
    {"id": "lex.en.200k.057782", "hw": "cottonseed cake", "pos": "phrase", "ipa": "", "vi": "khô bã ép bã dầu hạt bông vải"},
    {"id": "lex.en.200k.057783", "hw": "cottonseed oil", "pos": "phrase", "ipa": "", "vi": "dầu hạt bông vải ép dinh dưỡng"},
    {"id": "lex.en.200k.057784", "hw": "dorothea lynde dix", "pos": "phrase", "ipa": "", "vi": "nhà cải cách Dorothea Lynde Dix"},
    {"id": "lex.en.200k.057785", "hw": "emanuel swedenborg", "pos": "phrase", "ipa": "", "vi": "nhà thần học triết gia Swedenborg"},
    {"id": "lex.en.200k.057786", "hw": "english ryegrass", "pos": "phrase", "ipa": "", "vi": "cỏ lúa mạch đen trường cửu Anh"},
    {"id": "lex.en.200k.057787", "hw": "erik satie", "pos": "phrase", "ipa": "", "vi": "nhà soạn nhạc Pháp Erik Satie"},
    {"id": "lex.en.200k.057788", "hw": "erythrocyte sedimentation rate", "pos": "phrase", "ipa": "", "vi": "tốc độ lắng máu lắng hồng cầu ESR"},
    {"id": "lex.en.200k.057789", "hw": "genus archaeopteryx", "pos": "phrase", "ipa": "", "vi": "chi chim thủy tổ tiền sử hóa thạch"},
    {"id": "lex.en.200k.057790", "hw": "genus sedum", "pos": "phrase", "ipa": "", "vi": "chi hoa đá thuốc bỏng mọng nước"},
    {"id": "lex.en.200k.057791", "hw": "giant ryegrass", "pos": "phrase", "ipa": "", "vi": "cỏ lúa mạch khổng lồ thân cao"},
    {"id": "lex.en.200k.057792", "hw": "irish wolfhound", "pos": "phrase", "ipa": "", "vi": "chó săn chó sói khổng lồ Ireland"},
    {"id": "lex.en.200k.057793", "hw": "italian ryegrass", "pos": "phrase", "ipa": "", "vi": "loài cỏ lúa mạch một năm của Ý"},
    {"id": "lex.en.200k.057794", "hw": "jean monnet", "pos": "phrase", "ipa": "", "vi": "chính khách kiến tạo EU Jean Monnet"},
    {"id": "lex.en.200k.057795", "hw": "john edward masefield", "pos": "phrase", "ipa": "", "vi": "nhà thơ Anh John Edward Masefield"},
    {"id": "lex.en.200k.057796", "hw": "john masefield", "pos": "phrase", "ipa": "", "vi": "nhà thơ Anh John Masefield"},
    {"id": "lex.en.200k.057797", "hw": "laser trabecular surgery", "pos": "phrase", "ipa": "", "vi": "phẫu thuật laser vùng bè mắt"},
    {"id": "lex.en.200k.057798", "hw": "lightning hurler", "pos": "phrase", "ipa": "", "vi": "thần phóng sét; người ném sấm sét"},
    {"id": "lex.en.200k.057799", "hw": "linolenic acid", "pos": "phrase", "ipa": "", "vi": "axit béo omega-3 linolenic"},
    {"id": "lex.en.200k.0577800" if False else "lex.en.200k.057800", "hw": "lithia water", "pos": "phrase", "ipa": "", "vi": "nước khoáng tự nhiên chứa liti"},
    {"id": "lex.en.200k.057801", "hw": "longleaf pine", "pos": "phrase", "ipa": "", "vi": "loài cây thông lá dài phương nam"}
]

# Validation
with open('scratch/b32_r06_raw_p3.json') as f:
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
final_p3 = []
for r, raw_r in zip(records, raw):
    item = dict(raw_r)
    item['pos'] = r['pos']
    item['ipa'] = r['ipa']
    item['vi'] = r['vi']
    item['status'] = 'reviewed'
    final_p3.append(item)

with open('scratch/b32_r06_p3.json', 'w') as f:
    json.dump(final_p3, f, ensure_ascii=False, indent=2)
print("Part 3 validated and written successfully.")
