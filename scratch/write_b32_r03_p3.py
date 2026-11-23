import json

with open('scratch/b32_r03_raw_p3.json') as f:
    raw_items = json.load(f)

reviewed_data = {
    "lex.en.200k.056202": {"pos": "noun", "ipa": "/θjuːˈsɪdɪdiːzɪz/", "vi": "sử gia Thucydides Hy Lạp"},
    "lex.en.200k.056203": {"pos": "noun", "ipa": "/ˈtɑːkvɪlz/", "vi": "nhà tư tưởng Alexis de Tocqueville"},
    "lex.en.200k.056204": {"pos": "noun", "ipa": "/ˈtɔːrtəsʃɛlz/", "vi": "mai đồi mồi; họa tiết đồi mồi"},
    "lex.en.200k.056205": {"pos": "noun", "ipa": "/ˈtuːkænz/", "vi": "loài chim tu-căng mỏ sừng lớn"},
    "lex.en.200k.056206": {"pos": "noun", "ipa": "/ˈʌmbriəz/", "vi": "vùng Umbria ở miền trung nước Ý"},
    "lex.en.200k.056207": {"pos": "verb", "ipa": "/ˌʌndərpərˈfɔːrmd/", "vi": "đã hoạt động kém kỳ vọng"},
    "lex.en.200k.056208": {"pos": "verb", "ipa": "/ˌʌndərpərˈfɔːrmɪŋ/", "vi": "hoạt động kém hiệu quả; tụt lùi"},
    "lex.en.200k.056209": {"pos": "verb", "ipa": "/ˌʌndərpərˈfɔːrmz/", "vi": "hoạt động dưới mức kỳ vọng"},
    "lex.en.200k.056210": {"pos": "noun", "ipa": "/ˈviːziz/", "vi": "thủ lĩnh nô lệ Denmark Vesey"},
    "lex.en.200k.056211": {"pos": "noun", "ipa": "/ˈweɪlərz/", "vi": "tàu săn cá voi; thủy thủ săn voi"},
    "lex.en.200k.056212": {"pos": "noun", "ipa": "/ˈwaɪthɔːrsɪz/", "vi": "thành phố Whitehorse ở Canada"},
    "lex.en.200k.056213": {"pos": "noun", "ipa": "/ˌdʌbəljuːˌɛmˈoʊz/", "vi": "Tổ chức Khí tượng Thế giới WMO"},
    "lex.en.200k.056214": {"pos": "noun", "ipa": "/ˌzɔːroʊˈæstriənz/", "vi": "tín đồ đạo Hỏa giáo Zoroaster"},
    "lex.en.200k.056215": {"pos": "phrase", "ipa": "", "vi": "nhựa tổng hợp acrylic acrylate"},
    "lex.en.200k.056216": {"pos": "phrase", "ipa": "", "vi": "nhà địa chất học Alfred Wegener"},
    "lex.en.200k.056217": {"pos": "phrase", "ipa": "", "vi": "nhà hóa học Antoine Lavoisier"},
    "lex.en.200k.056218": {"pos": "phrase", "ipa": "", "vi": "sông Apalachicola ở bang Florida"},
    "lex.en.200k.056219": {"pos": "phrase", "ipa": "", "vi": "cây tía tô đỏ; cây tía tô cảnh"},
    "lex.en.200k.056220": {"pos": "phrase", "ipa": "", "vi": "cá vược pike xanh Bắc Mỹ"},
    "lex.en.200k.056221": {"pos": "phrase", "ipa": "", "vi": "cao su tổng hợp Buna đàn hồi"},
    "lex.en.200k.056222": {"pos": "phrase", "ipa": "", "vi": "loài cá chó sọc vằn pickerel"},
    "lex.en.200k.056223": {"pos": "phrase", "ipa": "", "vi": "loài sâu bọ đuôi kìm châu Âu"},
    "lex.en.200k.056224": {"pos": "phrase", "ipa": "", "vi": "đĩa quang CD ghi một lần CD-R"},
    "lex.en.200k.056225": {"pos": "phrase", "ipa": "", "vi": "thể chai kết nối hai bán cầu não"},
    "lex.en.200k.056226": {"pos": "phrase", "ipa": "", "vi": "Công đồng tôn giáo Vienne"},
    "lex.en.200k.056227": {"pos": "phrase", "ipa": "", "vi": "chim sơn ca đồng cỏ miền đông"},
    "lex.en.200k.056228": {"pos": "phrase", "ipa": "", "vi": "phi công Eddie Rickenbacker"},
    "lex.en.200k.056229": {"pos": "phrase", "ipa": "", "vi": "chi cây cảnh Ô rô Acanthus"},
    "lex.en.200k.056230": {"pos": "phrase", "ipa": "", "vi": "chi cây hoa lỗ bình Lobelia"},
    "lex.en.200k.056231": {"pos": "phrase", "ipa": "", "vi": "chi chim anca lùn Plautus"},
    "lex.en.200k.056232": {"pos": "phrase", "ipa": "", "vi": "chi cây cọ sợi Raphia"},
    "lex.en.200k.056233": {"pos": "phrase", "ipa": "", "vi": "người dân bang New Hampshire"},
    "lex.en.200k.056234": {"pos": "phrase", "ipa": "", "vi": "vịnh Sidra ngoài khơi Libya"},
    "lex.en.200k.056235": {"pos": "phrase", "ipa": "", "vi": "bản mã thép nối thanh giàn"},
    "lex.en.200k.056236": {"pos": "phrase", "ipa": "", "vi": "họa tiết kẻ răng sói caro dệt"},
    "lex.en.200k.056237": {"pos": "phrase", "ipa": "", "vi": "axit flohiđric ăn mòn thủy tinh"},
    "lex.en.200k.056238": {"pos": "phrase", "ipa": "", "vi": "vị cha già Thổ Nhĩ Kỳ Atatürk"},
    "lex.en.200k.056239": {"pos": "phrase", "ipa": "", "vi": "nhà toán học vĩ đại Leonhard Euler"},
    "lex.en.200k.056240": {"pos": "phrase", "ipa": "", "vi": "xương gò má mặt"},
    "lex.en.200k.056241": {"pos": "phrase", "ipa": "", "vi": "thủy tinh thể nhân tạo đa tiêu cự"},
    "lex.en.200k.056242": {"pos": "phrase", "ipa": "", "vi": "thành phố Naha thuộc Okinawa"},
    "lex.en.200k.056243": {"pos": "phrase", "ipa": "", "vi": "con sông Neosho ở Bắc Mỹ"},
    "lex.en.200k.056244": {"pos": "phrase", "ipa": "", "vi": "bệnh bàng quang do thần kinh"},
    "lex.en.200k.056245": {"pos": "phrase", "ipa": "", "vi": "quá trình sinh đẻ; đỡ đẻ"},
    "lex.en.200k.056246": {"pos": "phrase", "ipa": "", "vi": "cây lục bình củ; rau mác nước"},
    "lex.en.200k.056247": {"pos": "phrase", "ipa": "", "vi": "hội chứng tiền kinh nguyệt PMS"},
    "lex.en.200k.056248": {"pos": "phrase", "ipa": "", "vi": "cụm từ đại từ trong ngữ pháp"},
    "lex.en.200k.056249": {"pos": "phrase", "ipa": "", "vi": "thảm len dệt xù rya Bắc Âu"},
    "lex.en.200k.056250": {"pos": "phrase", "ipa": "", "vi": "cuộc khởi nghĩa lính Sepoy Ấn Độ"},
    "lex.en.200k.056251": {"pos": "phrase", "ipa": "", "vi": "cây thông sierra lodgepole"},
    "lex.en.200k.056252": {"pos": "phrase", "ipa": "", "vi": "khớp cầu xoay chuyển tự do"},
    "lex.en.200k.056253": {"pos": "phrase", "ipa": "", "vi": "cây cỏ dính bám mùa xuân"},
    "lex.en.200k.056254": {"pos": "phrase", "ipa": "", "vi": "loài sư tử biển phương bắc Steller"},
    "lex.en.200k.056255": {"pos": "phrase", "ipa": "", "vi": "cây linh sam cận núi cao"},
    "lex.en.200k.056256": {"pos": "phrase", "ipa": "", "vi": "xương cổ chân; nhóm xương bàn chân"},
    "lex.en.200k.056257": {"pos": "phrase", "ipa": "", "vi": "mưa tuôn xối xả; tràn ngập"},
    "lex.en.200k.056258": {"pos": "phrase", "ipa": "", "vi": "vi khuẩn trực khuẩn lao Koch"},
    "lex.en.200k.056259": {"pos": "phrase", "ipa": "", "vi": "tổng thống nhà văn Václav Havel"},
    "lex.en.200k.056260": {"pos": "phrase", "ipa": "", "vi": "loài cá đá đỏ son sẫm màu"},
    "lex.en.200k.056261": {"pos": "phrase", "ipa": "", "vi": "lá tạng bao màng ngoài tim"},
    "lex.en.200k.056262": {"pos": "phrase", "ipa": "", "vi": "chim sơn ca đồng cỏ miền tây Bắc Mỹ"},
    "lex.en.200k.056263": {"pos": "phrase", "ipa": "", "vi": "nhà văn đoạt giải William Faulkner"},
    "lex.en.200k.056264": {"pos": "phrase", "ipa": "", "vi": "nhà văn Mỹ William Saroyan"},
    "lex.en.200k.056265": {"pos": "phrase", "ipa": "", "vi": "cây cỏ dính hoa vàng rực"},
    "lex.en.200k.056266": {"pos": "noun", "ipa": "/ˈædʒɪnkʊərts/", "vi": "trận chiến lịch sử Agincourt"},
    "lex.en.200k.056267": {"pos": "noun", "ipa": "/əˈkeɪdiənz/", "vi": "người dân vùng Akkad cổ đại"},
    "lex.en.200k.056268": {"pos": "noun", "ipa": "/ˈælbərzɪz/", "vi": "họa sĩ trường phái Josef Albers"},
    "lex.en.200k.056269": {"pos": "noun", "ipa": "/ˈæntɪkwɛriz/", "vi": "người sưu tầm cổ vật; nhà khảo cổ"},
    "lex.en.200k.056270": {"pos": "noun", "ipa": "/əˈriːələz/", "vi": "quầng vú; vùng quầng sắc tố da"},
    "lex.en.200k.056271": {"pos": "noun", "ipa": "/ˈɑːrmrɛsts/", "vi": "tay vịn ghế tựa; chỗ để tay"},
    "lex.en.200k.056272": {"pos": "noun", "ipa": "/ɑːrˈtwɑːz/", "vi": "tỉnh cổ Artois miền bắc nước Pháp"},
    "lex.en.200k.056273": {"pos": "noun", "ipa": "/ˈbæɡdædz/", "vi": "thủ đô Baghdad của Iraq"},
    "lex.en.200k.056274": {"pos": "noun", "ipa": "/ˈbɑːlz/", "vi": "thành phố Basel ở Thụy Sĩ"},
    "lex.en.200k.056275": {"pos": "noun", "ipa": "/bɪˈtreɪərz/", "vi": "kẻ phản bội; quân bội phản xảo trá"},
    "lex.en.200k.056276": {"pos": "noun", "ipa": "/ˌbiːˌdʒeɪˈɛsɪz/", "vi": "Cục Thống kê Tư pháp Mỹ BJS"},
    "lex.en.200k.056277": {"pos": "verb", "ipa": "/ˈblɪŋkərɪŋ/", "vi": "bịt mắt ngựa; làm che mắt thiển cận"},
    "lex.en.200k.056278": {"pos": "noun", "ipa": "/ˈblɪŋkərz/", "vi": "miếng che mắt ngựa; đèn xi-nhan"},
    "lex.en.200k.056279": {"pos": "noun", "ipa": "/ˈbuːɡənvɪlz/", "vi": "nhà thám hiểm Louis de Bougainville"},
    "lex.en.200k.056280": {"pos": "noun", "ipa": "/ˈbrædstriːts/", "vi": "nhà thơ nữ Anne Bradstreet"},
    "lex.en.200k.056281": {"pos": "noun", "ipa": "/ˈbraɪərz/", "vi": "bụi cây gai rậm; tẩu gỗ thạch nam"},
    "lex.en.200k.056282": {"pos": "noun", "ipa": "/bruːˈnɛts/", "vi": "người đàn ông có tóc màu đen nâu"},
    "lex.en.200k.056283": {"pos": "noun", "ipa": "/ˈbɜːroʊz/", "vi": "con lừa thồ nhỏ ở Tây Nam Mỹ"},
    "lex.en.200k.056284": {"pos": "noun", "ipa": "/ˈkrɪsməstaɪmz/", "vi": "dịp lễ Giáng sinh; mùa Noel"},
    "lex.en.200k.056285": {"pos": "noun", "ipa": "/kliːˈʃiz/", "vi": "thị trấn Clichy ngoại ô Paris"},
    "lex.en.200k.056286": {"pos": "noun", "ipa": "/ˈklɪntʃərz/", "vi": "lập luận dứt khoát; lốp xe gài sườn"},
    "lex.en.200k.056287": {"pos": "noun", "ipa": "/ˈkoʊhoʊz/", "vi": "loài cá hồi bạc coho Bắc Thái Bình"},
    "lex.en.200k.056288": {"pos": "noun", "ipa": "/ˈkɑːŋkiː/", "vi": "hốc xoăn mũi; loa tai giải phẫu"},
    "lex.en.200k.056289": {"pos": "noun", "ipa": "/kənˈstrʌktɪvɪzəmz/", "vi": "chủ nghĩa kiến tạo trong nghệ thuật"},
    "lex.en.200k.056290": {"pos": "noun", "ipa": "/ˈkɔːrnəlz/", "vi": "cây thù du cornel; quả anh đào gai"},
    "lex.en.200k.056291": {"pos": "adj", "ipa": "/ˈkriːkiər/", "vi": "kẽo kẹt hơn; ọp ẹp già nua hơn"},
    "lex.en.200k.056292": {"pos": "adj", "ipa": "/ˈkriːkiɪst/", "vi": "kẽo kẹt nhất; ọp ẹp già nua nhất"},
    "lex.en.200k.056293": {"pos": "noun", "ipa": "/ˌsiːˌviːˈeɪz/", "vi": "cơn tai biến mạch máu não CVA"},
    "lex.en.200k.056294": {"pos": "noun", "ipa": "/ˌsaɪtoʊtɑːkˈsɪsətiz/", "vi": "độ độc tế bào; tính gây độc tế bào"},
    "lex.en.200k.056295": {"pos": "noun", "ipa": "/ˈdiːkənəsɪz/", "vi": "nữ chấp sự trong giáo hội Kitô"},
    "lex.en.200k.056296": {"pos": "noun", "ipa": "/ˈdɪəriz/", "vi": "người thương yêu quý; cục cưng"},
    "lex.en.200k.056297": {"pos": "noun", "ipa": "/ˌdaɪəˈkliːʃənz/", "vi": "Hoàng đế La Mã Diocletian"},
    "lex.en.200k.056298": {"pos": "noun", "ipa": "/drəˈvɪdiənz/", "vi": "người ngữ hệ Dravida ở Nam Ấn"},
    "lex.en.200k.056299": {"pos": "noun", "ipa": "/ˈdrʌmbiːts/", "vi": "tiếng đập trống rộn ràng vang dội"},
    "lex.en.200k.056300": {"pos": "noun", "ipa": "/ɛldz/", "vi": "tuổi xế chiều già nua; thời xưa cũ"},
    "lex.en.200k.056301": {"pos": "noun", "ipa": "/ɪmˈpleɪsmənts/", "vi": "bệ súng đại bác; vị trí đặt pháo"}
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

with open('scratch/b32_r03_p3.json', 'w', encoding='utf-8') as f:
    json.dump(output_items, f, ensure_ascii=False, indent=2)

print(f"Successfully authored and validated Part 3: {len(output_items)} items saved to scratch/b32_r03_p3.json")
