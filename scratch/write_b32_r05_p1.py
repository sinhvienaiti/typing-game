import json

with open('scratch/b32_r05_raw_p1.json') as f:
    raw_items = json.load(f)

reviewed_data = {
    "lex.en.200k.057002": {"pos": "noun", "ipa": "/ˈnɑːstrəmz/", "vi": "thuốc thần rởm; thuốc lang băm"},
    "lex.en.200k.057003": {"pos": "noun", "ipa": "/ɑːkˈteɪvoʊz/", "vi": "sách khổ tám in ấn giấy"},
    "lex.en.200k.057004": {"pos": "noun", "ipa": "/ˈɑːnlʊkərz/", "vi": "người xem đứng ngoài bàng quan"},
    "lex.en.200k.057005": {"pos": "noun", "ipa": "/ˌɔːriˈɛntəlɪsts/", "vi": "nhà nghiên cứu phương Đông học"},
    "lex.en.200k.057006": {"pos": "noun", "ipa": "/pəˈlætənəts/", "vi": "lãnh địa bá tước công quốc cổ"},
    "lex.en.200k.057007": {"pos": "noun", "ipa": "/ˈpɔːlɪŋz/", "vi": "nhà hóa học Linus Pauling"},
    "lex.en.200k.057008": {"pos": "noun", "ipa": "/ˈpɛdəmənts/", "vi": "trán tường hình tam giác cổ điển"},
    "lex.en.200k.057009": {"pos": "noun", "ipa": "/ˈpɜːrɡələz/", "vi": "giàn hoa leo che nắng sân vườn"},
    "lex.en.200k.057010": {"pos": "noun", "ipa": "/ˌpɛrɪpəˈtɛtɪks/", "vi": "người đi chu du; triết gia lãng du"},
    "lex.en.200k.057011": {"pos": "noun", "ipa": "/ˈpɑːthɛdz/", "vi": "kẻ nghiện hút cần sa triền miên"},
    "lex.en.200k.057012": {"pos": "noun", "ipa": "/prəˈkɔːfiɛfs/", "vi": "nhà soạn nhạc Sergei Prokofiev"},
    "lex.en.200k.057013": {"pos": "noun", "ipa": "/ˌprɑːstəˈɡlændɪnz/", "vi": "chất trung gian lipid prostaglandin"},
    "lex.en.200k.057014": {"pos": "noun", "ipa": "/pʊˈrɑːnəz/", "vi": "kinh văn cổ sử thi Purana Ấn Độ"},
    "lex.en.200k.057015": {"pos": "noun", "ipa": "/ˈrɛfərənts/", "vi": "vật sở chỉ; đối tượng quy chiếu"},
    "lex.en.200k.057016": {"pos": "verb", "ipa": "/riːˈplæntɪd/", "vi": "đã trồng lại; đã cấy ghép lại"},
    "lex.en.200k.057017": {"pos": "verb", "ipa": "/riːˈplæntɪŋ/", "vi": "trồng lại cây xanh; cấy ghép lại"},
    "lex.en.200k.057018": {"pos": "verb", "ipa": "/riːˈplænts/", "vi": "trồng lại cây con; cấy lại"},
    "lex.en.200k.057019": {"pos": "noun", "ipa": "/ˈraɪmiː/", "vi": "khe hẹp giải phẫu; rãnh nứt hẹp"},
    "lex.en.200k.057020": {"pos": "noun", "ipa": "/ˈraɪməz/", "vi": "khe nứt giải phẫu; rãnh nứt hẹp"},
    "lex.en.200k.057021": {"pos": "noun", "ipa": "/ˈsændbɑːrz/", "vi": "doi cát bồi ngầm; bãi cát ngầm"},
    "lex.en.200k.057022": {"pos": "noun", "ipa": "/ʃtɪks/", "vi": "món ngón nghề sở trường; trò diễn"},
    "lex.en.200k.057023": {"pos": "noun", "ipa": "/skaʊsɪz/", "vi": "món hầm scouse; giọng Liverpool"},
    "lex.en.200k.057024": {"pos": "noun", "ipa": "/skriːz/", "vi": "sườn dốc tích tụ đá vụn scree"},
    "lex.en.200k.057025": {"pos": "adj", "ipa": "/ˈskruːiər/", "vi": "kỳ cục quặc hơn; điên rồ hơn"},
    "lex.en.200k.057026": {"pos": "adj", "ipa": "/ˈskruːiɪst/", "vi": "kỳ quặc nhất; điên rồ ngớ ngẩn nhất"},
    "lex.en.200k.057027": {"pos": "adj", "ipa": "/ˈskrʌbiər/", "vi": "cằn cỗi hơn; rậm bụi cây thấp hơn"},
    "lex.en.200k.057028": {"pos": "adj", "ipa": "/ˈskrʌbiɪst/", "vi": "cằn cỗi nhất; xơ xác lùn tịt nhất"},
    "lex.en.200k.057029": {"pos": "noun", "ipa": "/ˈsɪsɪfəsɪz/", "vi": "người làm việc dã tràng Sisyphus"},
    "lex.en.200k.057030": {"pos": "noun", "ipa": "/ˈspɛktrəɡræfs/", "vi": "máy quang phổ ghi quang phổ ký"},
    "lex.en.200k.057031": {"pos": "adj", "ipa": "/ˈspɪndliər/", "vi": "khẳng khiu hơn; mảnh khảnh hơn"},
    "lex.en.200k.057032": {"pos": "adj", "ipa": "/ˈspɪndliɪst/", "vi": "khẳng khiu nhất; dài ngoẵng nhất"},
    "lex.en.200k.057033": {"pos": "noun", "ipa": "/spɪˈnɛlz/", "vi": "đá quý khoáng vật spinel đỏ hồng"},
    "lex.en.200k.057034": {"pos": "noun", "ipa": "/sʌbˈdʒɛnərə/", "vi": "các phân chi sinh học dưới chi"},
    "lex.en.200k.057035": {"pos": "noun", "ipa": "/sʌbˈdʒiːnəsɪz/", "vi": "các phân chi sinh học phân loại"},
    "lex.en.200k.057036": {"pos": "noun", "ipa": "/ˈsuːpərfæmɪliz/", "vi": "liên họ phân loại học sinh học"},
    "lex.en.200k.057037": {"pos": "noun", "ipa": "/tɑːˈhiːniz/", "vi": "sốt bơ vừng mè tahini Trung Đông"},
    "lex.en.200k.057038": {"pos": "noun", "ipa": "/ˈteɪlbæks/", "vi": "hàng dài xe ùn tắc; cầu thủ đuôi"},
    "lex.en.200k.057039": {"pos": "noun", "ipa": "/ˈteɪlwɪndz/", "vi": "ngọn gió xuôi thổi từ sau lưng"},
    "lex.en.200k.057040": {"pos": "noun", "ipa": "/ˈtɛlfərz/", "vi": "cabin xe cáp treo đơn ray trên cao"},
    "lex.en.200k.057041": {"pos": "noun", "ipa": "/ˈtɛmptrəsɪz/", "vi": "người phụ nữ quyến rũ mê hoặc"},
    "lex.en.200k.057042": {"pos": "noun", "ipa": "/ˈtjuːksbəriz/", "vi": "trận chiến lịch sử Tewkesbury"},
    "lex.en.200k.057043": {"pos": "noun", "ipa": "/tɔːrˈmɛntərz/", "vi": "kẻ hành hạ đày đọa; màn cánh gà"},
    "lex.en.200k.057044": {"pos": "noun", "ipa": "/ˈtɔːrtʃərərz/", "vi": "kẻ tra tấn tàn bạo dã man"},
    "lex.en.200k.057045": {"pos": "noun", "ipa": "/ˈtoʊpæθs/", "vi": "đường mòn kéo thuyền ven bờ kênh"},
    "lex.en.200k.057046": {"pos": "noun", "ipa": "/ˈtɔɪnbiz/", "vi": "nhà sử học Arnold J. Toynbee"},
    "lex.en.200k.057047": {"pos": "noun", "ipa": "/trəˈvɜːrsəlz/", "vi": "sự băng qua; quá trình duyệt cây"},
    "lex.en.200k.057048": {"pos": "noun", "ipa": "/tuːˈvɑːluːz/", "vi": "quốc đảo Tuvalu ở Thái Bình Dương"},
    "lex.en.200k.057049": {"pos": "noun", "ipa": "/ʊlz/", "vi": "thần cung tiễn và trượt tuyết Ull"},
    "lex.en.200k.057050": {"pos": "noun", "ipa": "/ˌjuːˌjuːˈpiːz/", "vi": "nguyên tố ununpentium moscovi"},
    "lex.en.200k.057051": {"pos": "noun", "ipa": "/ˈwɑːʃbɔːrdz/", "vi": "ván giặt quần áo; cơ bụng sáu múi"},
    "lex.en.200k.057052": {"pos": "noun", "ipa": "/ˈveɪɡənərz/", "vi": "nhà địa vật lý Alfred Wegener"},
    "lex.en.200k.057053": {"pos": "noun", "ipa": "/ˈwɜːrkwɛərz/", "vi": "đồ bảo hộ lao động cho công nhân"},
    "lex.en.200k.057054": {"pos": "noun", "ipa": "/ˈwaɪvərnz/", "vi": "loài rồng hai chân wyvern có cánh"},
    "lex.en.200k.057055": {"pos": "noun", "ipa": "/ˈɪɡdrəsɪlz/", "vi": "cây thế giới thần thoại Yggdrasil"},
    "lex.en.200k.057056": {"pos": "noun", "ipa": "/ˌzærəˈθuːstrəz/", "vi": "nhà tiên tri Zarathustra Ba Tư"},
    "lex.en.200k.057057": {"pos": "phrase", "ipa": "", "vi": "nhà điêu khắc Alberto Giacometti"},
    "lex.en.200k.057058": {"pos": "phrase", "ipa": "", "vi": "cây vỏ hắc mai đen châu Âu"},
    "lex.en.200k.057059": {"pos": "phrase", "ipa": "", "vi": "nhà soạn nhạc Aleksandr Borodin"},
    "lex.en.200k.057060": {"pos": "phrase", "ipa": "", "vi": "phết tế bào đường tiêu hóa"},
    "lex.en.200k.057061": {"pos": "phrase", "ipa": "", "vi": "rượu cồn pentanol amyl alcohol"},
    "lex.en.200k.057062": {"pos": "phrase", "ipa": "", "vi": "họa sĩ thời Phục hưng Mantegna"},
    "lex.en.200k.057063": {"pos": "phrase", "ipa": "", "vi": "quả mướp khía; cây mướp khía"},
    "lex.en.200k.057064": {"pos": "phrase", "ipa": "", "vi": "nhà hoạt động nữ quyền Friedan"},
    "lex.en.200k.057065": {"pos": "phrase", "ipa": "", "vi": "nhà văn nữ quyền Betty Friedan"},
    "lex.en.200k.057066": {"pos": "phrase", "ipa": "", "vi": "sách tiên tri Ha-ba-cúc Cựu Ước"},
    "lex.en.200k.057067": {"pos": "phrase", "ipa": "", "vi": "đại kiện tướng cờ vua Boris Spassky"},
    "lex.en.200k.057068": {"pos": "phrase", "ipa": "", "vi": "dụng cụ vẽ hỗ trợ camera lucida"},
    "lex.en.200k.057069": {"pos": "phrase", "ipa": "", "vi": "nguyên cớ gây ra chiến tranh"},
    "lex.en.200k.057070": {"pos": "phrase", "ipa": "", "vi": "nhà điêu khắc pop art Oldenburg"},
    "lex.en.200k.057071": {"pos": "phrase", "ipa": "", "vi": "tật lác mắt vào trong; mắt lác chụm"},
    "lex.en.200k.057072": {"pos": "phrase", "ipa": "", "vi": "khối đa diện lồi trong hình học"},
    "lex.en.200k.057073": {"pos": "phrase", "ipa": "", "vi": "băng chuyền tải hàng tự động"},
    "lex.en.200k.057074": {"pos": "phrase", "ipa": "", "vi": "loài hươu hoang dã châu Âu"},
    "lex.en.200k.057075": {"pos": "phrase", "ipa": "", "vi": "rùa mai hoa văn kim cương đầm lầy"},
    "lex.en.200k.057076": {"pos": "phrase", "ipa": "", "vi": "nhà thơ nữ Edna St. Vincent Millay"},
    "lex.en.200k.057077": {"pos": "phrase", "ipa": "", "vi": "cha mẹ có con cái dọn ra ở riêng"},
    "lex.en.200k.057078": {"pos": "phrase", "ipa": "", "vi": "Thánh Giêrônimô dịch Kinh Thánh"},
    "lex.en.200k.057079": {"pos": "phrase", "ipa": "", "vi": "lượng từ tồn tại ký hiệu ∃"},
    "lex.en.200k.057080": {"pos": "phrase", "ipa": "", "vi": "rau bắp cải rau diếp quăn Bỉ"},
    "lex.en.200k.057081": {"pos": "phrase", "ipa": "", "vi": "súng trường bán tự động M1 Garand"},
    "lex.en.200k.057082": {"pos": "phrase", "ipa": "", "vi": "chi cây bụi kim ngân Viburnum"},
    "lex.en.200k.057083": {"pos": "phrase", "ipa": "", "vi": "cây bách lùn Gowen ở California"},
    "lex.en.200k.057084": {"pos": "phrase", "ipa": "", "vi": "họa sĩ hiện thực Gustave Courbet"},
    "lex.en.200k.057085": {"pos": "phrase", "ipa": "", "vi": "xe ngựa hai bánh hansom kiểu cổ"},
    "lex.en.200k.057086": {"pos": "phrase", "ipa": "", "vi": "cột trụ bắt bản lề cánh cổng"},
    "lex.en.200k.057087": {"pos": "phrase", "ipa": "", "vi": "phản ứng đáp ứng hệ miễn dịch"},
    "lex.en.200k.057088": {"pos": "phrase", "ipa": "", "vi": "lâm vào cảnh túng quẫn nghèo khó"},
    "lex.en.200k.057089": {"pos": "phrase", "ipa": "", "vi": "loài kiến quân đội ăn thịt hung dữ"},
    "lex.en.200k.057090": {"pos": "phrase", "ipa": "", "vi": "văn bản tòa án chuẩn thuận di chúc"},
    "lex.en.200k.057091": {"pos": "phrase", "ipa": "", "vi": "ống sinh hàn ngưng tụ Liebig"},
    "lex.en.200k.057092": {"pos": "phrase", "ipa": "", "vi": "biển Liguria ở miền bắc nước Ý"},
    "lex.en.200k.057093": {"pos": "phrase", "ipa": "", "vi": "chứng mất điều hòa vận động đi lại"},
    "lex.en.200k.057094": {"pos": "phrase", "ipa": "", "vi": "cây cỏ rau diếp cọng Malheur"},
    "lex.en.200k.057095": {"pos": "phrase", "ipa": "", "vi": "triết gia Do Thái Martin Buber"},
    "lex.en.200k.057096": {"pos": "phrase", "ipa": "", "vi": "vương triều Meroving của Frank"},
    "lex.en.200k.057097": {"pos": "phrase", "ipa": "", "vi": "vua Mithridates VI Đại đế xứ Pontus"},
    "lex.en.200k.057098": {"pos": "phrase", "ipa": "", "vi": "vua Mithridates VI xứ Pontus"},
    "lex.en.200k.057099": {"pos": "phrase", "ipa": "", "vi": "tuyến nước bọt mang tai lớn"},
    "lex.en.200k.057100": {"pos": "phrase", "ipa": "", "vi": "cây bụi hoa chuông manzanita Parry"},
    "lex.en.200k.057101": {"pos": "phrase", "ipa": "", "vi": "nhà vật lý đoạt giải Philipp Lenard"}
}

output_items = []
errors = []

for item in raw_items:
    item_id = item['id']
    if item_id not in reviewed_data:
        errors.append(f"Missing reviewed data for {item_id}")
        continue
    
    rev = reviewed_data[item_id]
    vi = rev['vi']
    pos = rev['pos']
    ipa = rev['ipa']
    
    # Validation
    if len(vi) > 35:
        errors.append(f"Length violation (>35) for {item_id} ({item['hw']}): '{vi}' ({len(vi)} chars)")
    if pos not in ['noun', 'verb', 'adj', 'adv', 'num', 'intj', 'prep', 'pron', 'conj', 'det', 'phrase']:
        errors.append(f"Invalid POS '{pos}' for {item_id}")
    if ipa != "":
        if not (ipa.startswith('/') and ipa.endswith('/') and ipa.count('/') == 2):
            errors.append(f"Invalid IPA format '{ipa}' for {item_id}")
    elif ' ' not in item['hw']:
        errors.append(f"Single word missing IPA for {item_id} ({item['hw']})")
        
    new_item = {
        "id": item["id"],
        "hw": item["hw"],
        "pos": pos,
        "ipa": ipa,
        "vi": vi,
        "cefr": item.get("cefr", "C2"),
        "tier": item.get("tier", 5),
        "status": "reviewed",
        "notes": item.get("notes", "")
    }
    output_items.append(new_item)

if errors:
    print(f"Validation FAILED with {len(errors)} errors:")
    for e in errors:
        print(" - " + e)
    exit(1)

with open('scratch/b32_r05_p1.json', 'w', encoding='utf-8') as f:
    json.dump(output_items, f, ensure_ascii=False, indent=2)

print(f"Successfully authored and validated Part 1: {len(output_items)} items saved to scratch/b32_r05_p1.json")
