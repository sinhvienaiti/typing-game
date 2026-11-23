import json

with open('scratch/b32_r04_raw_p3.json') as f:
    raw_items = json.load(f)

reviewed_data = {
    "lex.en.200k.056702": {"pos": "phrase", "ipa": "", "vi": "loài rùa da biển khổng lồ"},
    "lex.en.200k.056703": {"pos": "phrase", "ipa": "", "vi": "nhà nhân văn Leon Battista Alberti"},
    "lex.en.200k.056704": {"pos": "phrase", "ipa": "", "vi": "nhà báo điều tra Lincoln Steffens"},
    "lex.en.200k.056705": {"pos": "phrase", "ipa": "", "vi": "khỉ sóc sư tử lông vàng"},
    "lex.en.200k.056706": {"pos": "phrase", "ipa": "", "vi": "lượng từ logic trong toán học"},
    "lex.en.200k.056707": {"pos": "phrase", "ipa": "", "vi": "loài cá nục thuôn đuôi đỏ"},
    "lex.en.200k.056708": {"pos": "phrase", "ipa": "", "vi": "hạ sĩ quan chỉ huy quân đội"},
    "lex.en.200k.056709": {"pos": "phrase", "ipa": "", "vi": "loài cóc bà đỡ cõng trứng"},
    "lex.en.200k.056710": {"pos": "phrase", "ipa": "", "vi": "bộ côn trùng cánh nửa Hemiptera"},
    "lex.en.200k.056711": {"pos": "phrase", "ipa": "", "vi": "nhà toán học Oswald Veblen"},
    "lex.en.200k.056712": {"pos": "phrase", "ipa": "", "vi": "axit oxalic tẩy rỉ sét"},
    "lex.en.200k.056713": {"pos": "phrase", "ipa": "", "vi": "thủ phủ Pago Pago của Samoa Mỹ"},
    "lex.en.200k.056714": {"pos": "phrase", "ipa": "", "vi": "cơ ngực lớn trên lồng ngực"},
    "lex.en.200k.056715": {"pos": "phrase", "ipa": "", "vi": "cơ ngực bé dưới cơ ngực lớn"},
    "lex.en.200k.056716": {"pos": "phrase", "ipa": "", "vi": "hạch a-mi-đan vòm họng VA"},
    "lex.en.200k.056717": {"pos": "phrase", "ipa": "", "vi": "ngành động vật thân mềm nhuyễn thể"},
    "lex.en.200k.056718": {"pos": "phrase", "ipa": "", "vi": "cây rễ bướm trị viêm màng phổi"},
    "lex.en.200k.056719": {"pos": "phrase", "ipa": "", "vi": "thịt bò bít tết xương chữ T dày"},
    "lex.en.200k.056720": {"pos": "phrase", "ipa": "", "vi": "cây mận dại Mexico"},
    "lex.en.200k.056721": {"pos": "phrase", "ipa": "", "vi": "hình đa giác lõm có góc lõm"},
    "lex.en.200k.056722": {"pos": "phrase", "ipa": "", "vi": "vật liệu bán dẫn điện tử"},
    "lex.en.200k.056723": {"pos": "phrase", "ipa": "", "vi": "trực khuẩn lỵ Shiga vi trùng"},
    "lex.en.200k.056724": {"pos": "phrase", "ipa": "", "vi": "sân chơi ném bóng gỗ skittles"},
    "lex.en.200k.056725": {"pos": "phrase", "ipa": "", "vi": "quả bóng gỗ chơi trò skittles"},
    "lex.en.200k.056726": {"pos": "phrase", "ipa": "", "vi": "con ky gỗ trong trò ném skittles"},
    "lex.en.200k.056727": {"pos": "phrase", "ipa": "", "vi": "hóa chất diệt cỏ natri clorat"},
    "lex.en.200k.056728": {"pos": "phrase", "ipa": "", "vi": "tuyến sụn mi mắt Meibomius"},
    "lex.en.200k.056729": {"pos": "phrase", "ipa": "", "vi": "hỗn hợp độc tố và kháng độc tố"},
    "lex.en.200k.056730": {"pos": "phrase", "ipa": "", "vi": "van ba lá ở tim phải"},
    "lex.en.200k.056731": {"pos": "phrase", "ipa": "", "vi": "bệnh tiêu chảy sprue nhiệt đới"},
    "lex.en.200k.056732": {"pos": "phrase", "ipa": "", "vi": "loài khỉ sóc marmoset Nam Mỹ"},
    "lex.en.200k.056733": {"pos": "phrase", "ipa": "", "vi": "lượng từ phổ dụng với mọi ∀"},
    "lex.en.200k.056734": {"pos": "phrase", "ipa": "", "vi": "cây đoạn trắng miền nam Mỹ"},
    "lex.en.200k.056735": {"pos": "phrase", "ipa": "", "vi": "sông Áp Lục biên giới Trung-Triều"},
    "lex.en.200k.056736": {"pos": "phrase", "ipa": "", "vi": "hiện tượng ánh sáng hoàng đạo"},
    "lex.en.200k.056737": {"pos": "noun", "ipa": "/ˌæbɪˈsɪniənz/", "vi": "người Abyssinia; mèo lông vằn cát"},
    "lex.en.200k.056738": {"pos": "noun", "ipa": "/ælˈbɛərtiz/", "vi": "nhà kiến trúc Leon Battista Alberti"},
    "lex.en.200k.056739": {"pos": "noun", "ipa": "/ˌærəˈbɛsks/", "vi": "họa tiết Ả Rập; tư thế múa ba-lê"},
    "lex.en.200k.056740": {"pos": "noun", "ipa": "/ˈætɑːrz/", "vi": "tinh dầu hoa hồng thơm ngát"},
    "lex.en.200k.056741": {"pos": "noun", "ipa": "/bænˈdænəz/", "vi": "khăn rằn đội đầu quàng cổ bandana"},
    "lex.en.200k.056742": {"pos": "adj", "ipa": "/ˈbɑːrmiɪst/", "vi": "gàn dở nhất; khùng điên nhất"},
    "lex.en.200k.056743": {"pos": "noun", "ipa": "/ˌboʊʒəˈleɪz/", "vi": "rượu vang đỏ Beaujolais nước Pháp"},
    "lex.en.200k.056744": {"pos": "noun", "ipa": "/ˈbɛərɪŋz/", "vi": "bác sĩ đoạt giải Emil von Behring"},
    "lex.en.200k.056745": {"pos": "noun", "ipa": "/bɛərˈniːniz/", "vi": "nhà điêu khắc Gian Lorenzo Bernini"},
    "lex.en.200k.056746": {"pos": "noun", "ipa": "/ˈbɜːrdhaʊsɪz/", "vi": "ngôi nhà tổ chim nhân tạo"},
    "lex.en.200k.056747": {"pos": "noun", "ipa": "/ˈbaɪroʊz/", "vi": "bút bi mực nước; cây bút bi"},
    "lex.en.200k.056748": {"pos": "noun", "ipa": "/brəˈtɑːnjəz/", "vi": "vùng bán đảo Bretagne nước Pháp"},
    "lex.en.200k.056749": {"pos": "noun", "ipa": "/ˈbrɔːdʃiːts/", "vi": "báo khổ lớn; tờ tin tức khổ rộng"},
    "lex.en.200k.056750": {"pos": "noun", "ipa": "/kæpˈseɪɪsɪnz/", "vi": "hoạt chất cay capsaicin trong ớt"},
    "lex.en.200k.056751": {"pos": "noun", "ipa": "/ˌkɑːrbəˈnɑːrəz/", "vi": "món mì Ý sốt kem trứng carbonara"},
    "lex.en.200k.056752": {"pos": "noun", "ipa": "/ˌkɑːrθəˈdʒɪniənz/", "vi": "người dân thành Carthage cổ đại"},
    "lex.en.200k.056753": {"pos": "noun", "ipa": "/ˈkeɪsbʊks/", "vi": "sách tập hợp án lệ luật pháp"},
    "lex.en.200k.056754": {"pos": "noun", "ipa": "/ˈkæspeɪsɪz/", "vi": "enzym caspase gây chết rụng tế bào"},
    "lex.en.200k.056755": {"pos": "noun", "ipa": "/ˈsɛntrə/", "vi": "các thân đốt sống cột sống"},
    "lex.en.200k.056756": {"pos": "noun", "ipa": "/ˈsɛntrəmz/", "vi": "các thân đốt sống cột sống"},
    "lex.en.200k.056757": {"pos": "noun", "ipa": "/kælˈdiːənz/", "vi": "người Chaldea; nhà chiêm tinh cổ"},
    "lex.en.200k.056758": {"pos": "noun", "ipa": "/ˌtʃɪəriˈoʊz/", "vi": "lời chào tạm biệt; ngũ cốc Cheerios"},
    "lex.en.200k.056759": {"pos": "noun", "ipa": "/sɪˈtriːnz/", "vi": "đá thạch anh vàng phong thủy"},
    "lex.en.200k.056760": {"pos": "noun", "ipa": "/ˈklæmʃɛlz/", "vi": "vỏ sò vỏ ngao; gầu ngoạm cơ khí"},
    "lex.en.200k.056761": {"pos": "noun", "ipa": "/ˈkɑːlɪts/", "vi": "ống kẹp collet mũi khoan; vòng gá"},
    "lex.en.200k.056762": {"pos": "noun", "ipa": "/ˈkuːtərz/", "vi": "loài rùa nước ngọt đồng cỏ cooter"},
    "lex.en.200k.056763": {"pos": "noun", "ipa": "/ˈkræpiz/", "vi": "loài cá vược nước ngọt crappie"},
    "lex.en.200k.056764": {"pos": "noun", "ipa": "/kuːmz/", "vi": "thung lũng lòng chảo băng hà cwm"},
    "lex.en.200k.056765": {"pos": "noun", "ipa": "/dælˈmeɪʃiəz/", "vi": "vùng duyên hải Dalmatia ở Croatia"},
    "lex.en.200k.056766": {"pos": "verb", "ipa": "/dɪˈfeɪst/", "vi": "đã bôi bẩn làm hoen ố bề mặt"},
    "lex.en.200k.056767": {"pos": "verb", "ipa": "/dɪˈfeɪsɪz/", "vi": "bôi bẩn; làm hư hỏng mặt ngoài"},
    "lex.en.200k.056768": {"pos": "verb", "ipa": "/dɪˈfeɪsɪŋ/", "vi": "hành vi bôi bẩn; làm biến dạng"},
    "lex.en.200k.056769": {"pos": "noun", "ipa": "/ˈdɪɡnətɛriz/", "vi": "các vị chức sắc; quan khách cấp cao"},
    "lex.en.200k.056770": {"pos": "noun", "ipa": "/ˈdɔːɡfɪʃɪz/", "vi": "loài cá nhám góc; cá nhám chó nhỏ"},
    "lex.en.200k.056771": {"pos": "noun", "ipa": "/ˈdɔːrkɪŋz/", "vi": "giống gà thịt năm ngón Dorking Anh"},
    "lex.en.200k.056772": {"pos": "noun", "ipa": "/ˈdʌblɪts/", "vi": "áo chẽn đôi thời Phục hưng; từ đôi"},
    "lex.en.200k.056773": {"pos": "adj", "ipa": "/ˈdʌmpiər/", "vi": "lùn mập hơn; thô kệch mập mạp hơn"},
    "lex.en.200k.056774": {"pos": "adj", "ipa": "/ˈdʌmpiɪst/", "vi": "lùn mập nhất; thô kệch nhất"},
    "lex.en.200k.056775": {"pos": "noun", "ipa": "/ˈiːɡrɪts/", "vi": "loài chim cò trắng lông tơ muốt"},
    "lex.en.200k.056776": {"pos": "noun", "ipa": "/ˈɛkwəsɪz/", "vi": "chi ngựa lừa vằn móng guốc Equus"},
    "lex.en.200k.056777": {"pos": "noun", "ipa": "/ɜːrnz/", "vi": "đại bàng đuôi trắng săn cá"},
    "lex.en.200k.056778": {"pos": "noun", "ipa": "/ˈfɔːlsətiz/", "vi": "điều sai sự thật; tính dối trá"},
    "lex.en.200k.056779": {"pos": "noun", "ipa": "/ˈfeɪvərɪtɪzəmz/", "vi": "thói thiên vị bất công bè phái"},
    "lex.en.200k.056780": {"pos": "noun", "ipa": "/ɡæts/", "vi": "Hiệp định chung Thuế quan GATT"},
    "lex.en.200k.056781": {"pos": "noun", "ipa": "/ˈnoʊsiːz/", "vi": "linh tri; sự thấu hiểu tâm linh"},
    "lex.en.200k.056782": {"pos": "noun", "ipa": "/ɡrɪmˈwɑːrz/", "vi": "sách ma thuật phù thủy cổ xưa"},
    "lex.en.200k.056783": {"pos": "noun", "ipa": "/ˈhɑːrpoʊz/", "vi": "danh hài câm Harpo Marx"},
    "lex.en.200k.056784": {"pos": "noun", "ipa": "/ˈhɛdstɑːks/", "vi": "đầu máy tiện; đầu cần đàn guitar"},
    "lex.en.200k.056785": {"pos": "noun", "ipa": "/ˈhɜːrmiː/", "vi": "tượng bán thân đá trụ thần Hermes"},
    "lex.en.200k.056786": {"pos": "noun", "ipa": "/hɜːrmz/", "vi": "tượng đá trụ có đầu thần Hy Lạp"},
    "lex.en.200k.056787": {"pos": "verb", "ipa": "/ɪmˈbaɪbd/", "vi": "đã uống cạn; đã tiếp thu thấm nhuần"},
    "lex.en.200k.056788": {"pos": "verb", "ipa": "/ɪmˈbaɪbz/", "vi": "uống cạn; tiếp thu đón nhận"},
    "lex.en.200k.056789": {"pos": "noun", "ipa": "/ˌɪnˈtɜːrnɪsts/", "vi": "bác sĩ chuyên khoa nội khoa"},
    "lex.en.200k.056790": {"pos": "noun", "ipa": "/ɪnˈtrænsətɪvz/", "vi": "các nội động từ trong ngữ pháp"},
    "lex.en.200k.056791": {"pos": "noun", "ipa": "/ˈɪʃərwʊdz/", "vi": "nhà văn Christopher Isherwood"},
    "lex.en.200k.056792": {"pos": "noun", "ipa": "/ˌkælɪˈmæntænz/", "vi": "vùng đất Kalimantan ở đảo Borneo"},
    "lex.en.200k.056793": {"pos": "noun", "ipa": "/ˈkɑːrpɔːfs/", "vi": "vua cờ Anatoly Karpov nước Nga"},
    "lex.en.200k.056794": {"pos": "noun", "ipa": "/kætˈsiːnəz/", "vi": "thành phố Katsina ở Nigeria"},
    "lex.en.200k.056795": {"pos": "noun", "ipa": "/ˈkoʊmiz/", "vi": "người dân tộc Komi ở miền bắc Nga"},
    "lex.en.200k.056796": {"pos": "noun", "ipa": "/ˈlɪntəlz/", "vi": "thanh lanh-tô giằng ngang cửa"},
    "lex.en.200k.056797": {"pos": "noun", "ipa": "/ˈloʊnərz/", "vi": "xe cho mượn tạm; đồ cho mượn"},
    "lex.en.200k.056798": {"pos": "noun", "ipa": "/ˈlʌfkɪnz/", "vi": "thành phố Lufkin ở bang Texas"},
    "lex.en.200k.056799": {"pos": "noun", "ipa": "/ˈmæmɪts/", "vi": "nhà biên kịch David Mamet"},
    "lex.en.200k.056800": {"pos": "noun", "ipa": "/məˈrɑːks/", "vi": "nước Ma-rốc ở vùng Bắc Phi"},
    "lex.en.200k.056801": {"pos": "noun", "ipa": "/məkˈluːənz/", "vi": "nhà lý luận truyền thông McLuhan"}
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

with open('scratch/b32_r04_p3.json', 'w', encoding='utf-8') as f:
    json.dump(output_items, f, ensure_ascii=False, indent=2)

print(f"Successfully authored and validated Part 3: {len(output_items)} items saved to scratch/b32_r04_p3.json")
