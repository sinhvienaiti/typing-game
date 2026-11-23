import json

with open('scratch/b32_r04_raw_p1.json') as f:
    raw_items = json.load(f)

reviewed_data = {
    "lex.en.200k.056502": {"pos": "noun", "ipa": "/ˌdʒiːˌɛsˈɑːrz/", "vi": "phản xạ dẫn truyền điện da GSR"},
    "lex.en.200k.056503": {"pos": "noun", "ipa": "/ˈɡʌnpleɪz/", "vi": "cuộc đấu súng dữ dội; đọ súng"},
    "lex.en.200k.056504": {"pos": "noun", "ipa": "/ɡʊərz/", "vi": "ngữ tộc Gur; đường thốt nốt gur"},
    "lex.en.200k.056505": {"pos": "noun", "ipa": "/ˈheɪmənz/", "vi": "quan tể tướng Haman gian ác"},
    "lex.en.200k.056506": {"pos": "noun", "ipa": "/ˈhɑːnʃuːz/", "vi": "đảo chính Honshu của Nhật Bản"},
    "lex.en.200k.056507": {"pos": "noun", "ipa": "/hoʊˈzænəz/", "vi": "tiếng hô vang chúc tụng Hosanna"},
    "lex.en.200k.056508": {"pos": "noun", "ipa": "/ˌhaɪməˈnɑːptərəz/", "vi": "bộ côn trùng cánh màng"},
    "lex.en.200k.056509": {"pos": "noun", "ipa": "/ˌhaɪpərˈθɜːrmiəz/", "vi": "chứng sốt tăng thân nhiệt quá cao"},
    "lex.en.200k.056510": {"pos": "verb", "ipa": "/ɪmˈpɛrəld/", "vi": "đã đẩy vào thế nguy hiểm"},
    "lex.en.200k.056511": {"pos": "verb", "ipa": "/ɪmˈpɛrəlɪŋ/", "vi": "gây nguy hại; đe dọa an nguy"},
    "lex.en.200k.056512": {"pos": "noun", "ipa": "/dʒjaʊz/", "vi": "hào tiền tệ Trung Quốc jiao"},
    "lex.en.200k.056513": {"pos": "noun", "ipa": "/ˈkɛnənz/", "vi": "nhà ngoại giao George F. Kennan"},
    "lex.en.200k.056514": {"pos": "noun", "ipa": "/ˈlædiz/", "vi": "chàng trai trẻ; cậu bé xứ Scotland"},
    "lex.en.200k.056515": {"pos": "noun", "ipa": "/ˈlæmppoʊsts/", "vi": "cột đèn chiếu sáng đường phố"},
    "lex.en.200k.056516": {"pos": "noun", "ipa": "/ˈlɪtəɡeɪtərz/", "vi": "luật sư tranh tụng tại tòa án"},
    "lex.en.200k.056517": {"pos": "noun", "ipa": "/ˈmæpərz/", "vi": "người vẽ bản đồ; công cụ ánh xạ"},
    "lex.en.200k.056518": {"pos": "noun", "ipa": "/mɑːrˈsɑːləz/", "vi": "rượu vang ngọt Marsala nước Ý"},
    "lex.en.200k.056519": {"pos": "noun", "ipa": "/ˈmɑːrʃlændz/", "vi": "vùng đầm lầy trũng ẩm ướt"},
    "lex.en.200k.056520": {"pos": "noun", "ipa": "/moʊˈhɑːviz/", "vi": "bộ tộc thổ dân Mohave; sa mạc"},
    "lex.en.200k.056521": {"pos": "noun", "ipa": "/məˈlʌskəz/", "vi": "ngành động vật thân mềm nhuyễn thể"},
    "lex.en.200k.056522": {"pos": "noun", "ipa": "/mʌsˈkoʊɡiːz/", "vi": "bộ tộc thổ dân da đỏ Muskogee"},
    "lex.en.200k.056523": {"pos": "noun", "ipa": "/ˌmjuːtəˈdʒɛnəsɪz/", "vi": "quá trình sinh đột biến gen"},
    "lex.en.200k.056524": {"pos": "noun", "ipa": "/ˈnɔːrðərnərz/", "vi": "người phương bắc; dân miền bắc"},
    "lex.en.200k.056525": {"pos": "noun", "ipa": "/ˌnɪmfəˈmeɪniæks/", "vi": "người mắc chứng cuồng dục nữ"},
    "lex.en.200k.056526": {"pos": "noun", "ipa": "/ˈɑːsəlɑːts/", "vi": "loài mèo gấm mèo rừng ocelot"},
    "lex.en.200k.056527": {"pos": "noun", "ipa": "/ˈɑːksɪz/", "vi": "chủ báo Adolph Ochs của New York"},
    "lex.en.200k.056528": {"pos": "noun", "ipa": "/ˈwɑːʃɪtɔːz/", "vi": "dãy núi và dòng sông Ouachita"},
    "lex.en.200k.056529": {"pos": "noun", "ipa": "/ˌpeɪlioʊˈlɪθɪks/", "vi": "thời kỳ đồ đá cũ nguyên thủy"},
    "lex.en.200k.056530": {"pos": "noun", "ipa": "/ˈpɑːrsiz/", "vi": "người Parsi theo Hỏa giáo ở Ấn"},
    "lex.en.200k.056531": {"pos": "noun", "ipa": "/ˈpɑːrtəzənz/", "vi": "du kích chiến sĩ; người trung kiên"},
    "lex.en.200k.056532": {"pos": "noun", "ipa": "/pəˈtɑːnz/", "vi": "người dân tộc Pashtun Pathan"},
    "lex.en.200k.056533": {"pos": "noun", "ipa": "/piːnz/", "vi": "đầu búa đập tán đinh; gáy búa"},
    "lex.en.200k.056534": {"pos": "noun", "ipa": "/ˈpɪnhɛdz/", "vi": "đầu đinh ghim; kẻ ngốc nghếch"},
    "lex.en.200k.056535": {"pos": "noun", "ipa": "/pwɑːtˈjeɪz/", "vi": "trận chiến lịch sử Poitiers ở Pháp"},
    "lex.en.200k.056536": {"pos": "noun", "ipa": "/ˈpɑːləneɪtərz/", "vi": "loài thụ phấn; vật truyền phấn"},
    "lex.en.200k.056537": {"pos": "noun", "ipa": "/ˈpriːfæbz/", "vi": "nhà lắp ghép tiền chế đúc sẵn"},
    "lex.en.200k.056538": {"pos": "noun", "ipa": "/prɪˈtɛnʃənz/", "vi": "yêu sách; thói tự phụ khoe mẽ"},
    "lex.en.200k.056539": {"pos": "adj", "ipa": "/ˈprɪsiər/", "vi": "kiểu cách hơn; khó tính điệu đà hơn"},
    "lex.en.200k.056540": {"pos": "adj", "ipa": "/ˈprɪsiɪst/", "vi": "kiểu cách nhất; quá đỗi khó tính"},
    "lex.en.200k.056541": {"pos": "noun", "ipa": "/ˈproʊlɑːɡz/", "vi": "ngôn ngữ lập trình logic Prolog"},
    "lex.en.200k.056542": {"pos": "verb", "ipa": "/ˈpʌŋktʃueɪtɪd/", "vi": "đã chấm câu; điểm xuyết xen kẽ"},
    "lex.en.200k.056543": {"pos": "verb", "ipa": "/ˈpʌŋktʃueɪts/", "vi": "chấm câu ngắt đoạn; điểm xuyết"},
    "lex.en.200k.056544": {"pos": "verb", "ipa": "/ˈpʌŋktʃueɪtɪŋ/", "vi": "đang chấm câu; xen ngang điểm xuyết"},
    "lex.en.200k.056545": {"pos": "noun", "ipa": "/ˈpɪntʃənz/", "vi": "tiểu thuyết gia Thomas Pynchon"},
    "lex.en.200k.056546": {"pos": "verb", "ipa": "/riːˈlɜːrnd/", "vi": "đã học lại; đã tiếp thu lại"},
    "lex.en.200k.056547": {"pos": "verb", "ipa": "/riːˈlɜːrnɪŋ/", "vi": "học lại kiến thức; rèn luyện lại"},
    "lex.en.200k.056548": {"pos": "verb", "ipa": "/riːˈlɜːrnz/", "vi": "học lại; tiếp thu bồi dưỡng lại"},
    "lex.en.200k.056549": {"pos": "noun", "ipa": "/ˈrɪlkiz/", "vi": "nhà thơ trữ tình Rainer Maria Rilke"},
    "lex.en.200k.056550": {"pos": "noun", "ipa": "/ˈseɪlɪksɪz/", "vi": "chi cây liễu rủ lá bóng Salix"},
    "lex.en.200k.056551": {"pos": "adj", "ipa": "/ˈskæntiər/", "vi": "ít ỏi hơn; chật hẹp thiếu thốn hơn"},
    "lex.en.200k.056552": {"pos": "adj", "ipa": "/ˈskæntiɪst/", "vi": "ít ỏi nhất; thiếu thốn nhất"},
    "lex.en.200k.056553": {"pos": "noun", "ipa": "/ˈʃiːðɪŋz/", "vi": "lớp ván ốp tường; lớp bọc bảo vệ"},
    "lex.en.200k.056554": {"pos": "noun", "ipa": "/ʃʌnˈjɑːŋz/", "vi": "thành phố Thẩm Dương ở Trung Quốc"},
    "lex.en.200k.056555": {"pos": "noun", "ipa": "/ʃuːts/", "vi": "nhà văn Nevil Shute người Anh"},
    "lex.en.200k.056556": {"pos": "noun", "ipa": "/ˈsɪlvərbæks/", "vi": "khỉ đột lưng bạc đầu đàn trưởng"},
    "lex.en.200k.056557": {"pos": "noun", "ipa": "/skeɪnz/", "vi": "cuộn len sợi; đàn ngỗng trời bay"},
    "lex.en.200k.056558": {"pos": "noun", "ipa": "/ˈsmɔːliz/", "vi": "nhà hóa học Richard Smalley"},
    "lex.en.200k.056559": {"pos": "noun", "ipa": "/splɪfs/", "vi": "điếu thuốc lá cuốn cỏ cần sa"},
    "lex.en.200k.056560": {"pos": "verb", "ipa": "/ˈstiːmroʊlərd/", "vi": "đã đàn áp thô bạo; đè bẹp đối thủ"},
    "lex.en.200k.056561": {"pos": "verb", "ipa": "/ˈstiːmroʊlərɪŋ/", "vi": "dùng sức mạnh áp đảo; đàn áp"},
    "lex.en.200k.056562": {"pos": "noun", "ipa": "/ˈstiːmroʊlərz/", "vi": "xe lu hơi nước; thế lực áp đảo"},
    "lex.en.200k.056563": {"pos": "noun", "ipa": "/ˈstiːliːz/", "vi": "tấm bia đá khắc chữ cổ; bia mộ"},
    "lex.en.200k.056564": {"pos": "noun", "ipa": "/təˈbuːz/", "vi": "điều cấm kỵ; hủ tục kiêng cữ"},
    "lex.en.200k.056565": {"pos": "noun", "ipa": "/ˈtæklərz/", "vi": "cầu thủ tranh bóng; người cản phá"},
    "lex.en.200k.056566": {"pos": "noun", "ipa": "/ˈtiːhaʊsɪz/", "vi": "quán trà đạo; phòng uống trà"},
    "lex.en.200k.056567": {"pos": "noun", "ipa": "/ˈtɛlɪkɑːnfərənsɪz/", "vi": "cuộc họp hội nghị truyền hình từ xa"},
    "lex.en.200k.056568": {"pos": "noun", "ipa": "/ˈθrɛʃərz/", "vi": "máy tuốt đập lúa; cá mập đuôi dài"},
    "lex.en.200k.056569": {"pos": "noun", "ipa": "/ˈtwiːləriːzɪz/", "vi": "khu vườn hoàng gia Tuileries Paris"},
    "lex.en.200k.056570": {"pos": "noun", "ipa": "/ˌvɪtəlˈaɪɡoʊz/", "vi": "chứng bệnh bạch biến mất sắc tố da"},
    "lex.en.200k.056571": {"pos": "noun", "ipa": "/ˈwɔːrdərz/", "vi": "cai ngục; giám thị trại giam"},
    "lex.en.200k.056572": {"pos": "adj", "ipa": "/ˈwiːpiər/", "vi": "mau nước mắt hơn; sướt mướt hơn"},
    "lex.en.200k.056573": {"pos": "adj", "ipa": "/ˈwiːpiɪst/", "vi": "mau nước mắt nhất; sướt mướt nhất"},
    "lex.en.200k.056574": {"pos": "noun", "ipa": "/ˈvaɪtsmənz/", "vi": "tổng thống Chaim Weizmann Israel"},
    "lex.en.200k.056575": {"pos": "verb", "ipa": "/ˈjoʊdəld/", "vi": "đã hát luyến giọng yodel Thụy Sĩ"},
    "lex.en.200k.056576": {"pos": "noun", "ipa": "/əˈbɑːlɪʃmənts/", "vi": "sự hủy bỏ; sự thủ tiêu bãi bỏ"},
    "lex.en.200k.056577": {"pos": "noun", "ipa": "/əˈkeɪdiənz/", "vi": "người định cư Acadia gốc Pháp"},
    "lex.en.200k.056578": {"pos": "noun", "ipa": "/əˈkwaɪərərz/", "vi": "công ty thâu tóm; bên mua lại"},
    "lex.en.200k.056579": {"pos": "noun", "ipa": "/æmˈniːziæks/", "vi": "người bị mất trí nhớ; người quên"},
    "lex.en.200k.056580": {"pos": "noun", "ipa": "/ˈɑːrθrəpɑːdz/", "vi": "động vật chân khớp chân đốt"},
    "lex.en.200k.056581": {"pos": "noun", "ipa": "/ˈbækbɛntʃɪz/", "vi": "hàng ghế sau của nghị sĩ hạ viện"},
    "lex.en.200k.056582": {"pos": "noun", "ipa": "/bɔːdz/", "vi": "đơn vị tốc độ truyền tin baud"},
    "lex.en.200k.056583": {"pos": "noun", "ipa": "/bɪˈhɑːriz/", "vi": "người dân bang Bihar ở Ấn Độ"},
    "lex.en.200k.056584": {"pos": "noun", "ipa": "/ˈbɪləbɑːŋz/", "vi": "nhánh sông cụt; hồ nước cạn ở Úc"},
    "lex.en.200k.056585": {"pos": "noun", "ipa": "/ˌbaɪoʊstəˈtɪstɪksɪz/", "vi": "ngành thống kê y sinh học"},
    "lex.en.200k.056586": {"pos": "noun", "ipa": "/ˈbræzəvɪlz/", "vi": "thủ đô Brazzaville của Congo"},
    "lex.en.200k.056587": {"pos": "noun", "ipa": "/ˈkæbəlz/", "vi": "nhà văn giả tưởng James Cabell"},
    "lex.en.200k.056588": {"pos": "noun", "ipa": "/kæˈstiːjəz/", "vi": "vương quốc cổ Castilla Tây Ban Nha"},
    "lex.en.200k.056589": {"pos": "noun", "ipa": "/ˌkæθətərəˈzeɪʃənz/", "vi": "thủ thuật đặt ống thông y tế"},
    "lex.en.200k.056590": {"pos": "noun", "ipa": "/ˈtʃiːkboʊnz/", "vi": "xương gò má nhô cao trên mặt"},
    "lex.en.200k.056591": {"pos": "noun", "ipa": "/sɪˈstɜːrʃənz/", "vi": "tu sĩ dòng Xitô nghiêm nhặt"},
    "lex.en.200k.056592": {"pos": "noun", "ipa": "/ˈkʌlərɪsts/", "vi": "chuyên gia phối màu; thợ nhuộm tóc"},
    "lex.en.200k.056593": {"pos": "noun", "ipa": "/kənˈsɪstəriz/", "vi": "mật nghị hồng y; tòa án giáo hội"},
    "lex.en.200k.056594": {"pos": "noun", "ipa": "/ˈkoʊpləndz/", "vi": "nhà soạn nhạc Mỹ Aaron Copland"},
    "lex.en.200k.056595": {"pos": "noun", "ipa": "/kraʊsɪz/", "vi": "nhà biên kịch Russel Crouse"},
    "lex.en.200k.056596": {"pos": "noun", "ipa": "/ˈdɑːməz/", "vi": "loài linh dương dama; hươu hoang"},
    "lex.en.200k.056597": {"pos": "noun", "ipa": "/dɪˈsiːdənts/", "vi": "người đã qua đời; người quá cố"},
    "lex.en.200k.056598": {"pos": "noun", "ipa": "/ˌdɛksəˈmɛθəsoʊnz/", "vi": "thuốc chống viêm dexamethasone"},
    "lex.en.200k.056599": {"pos": "noun", "ipa": "/ɛnˈtɛbiz/", "vi": "thành phố sân bay Entebbe ở Uganda"},
    "lex.en.200k.056600": {"pos": "noun", "ipa": "/ɪˌskeɪˈpiːz/", "vi": "tù nhân đào tẩu; người trốn thoát"},
    "lex.en.200k.056601": {"pos": "noun", "ipa": "/jʊˈrɪdɪsiz/", "vi": "nàng Eurydice thần thoại Hy Lạp"}
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

with open('scratch/b32_r04_p1.json', 'w', encoding='utf-8') as f:
    json.dump(output_items, f, ensure_ascii=False, indent=2)

print(f"Successfully authored and validated Part 1: {len(output_items)} items saved to scratch/b32_r04_p1.json")
