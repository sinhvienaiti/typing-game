import json

with open('scratch/b32_r03_raw_p5.json') as f:
    raw_items = json.load(f)

reviewed_data = {
    "lex.en.200k.056402": {"pos": "phrase", "ipa": "", "vi": "cây hương thảo Apalachicola"},
    "lex.en.200k.056403": {"pos": "phrase", "ipa": "", "vi": "bánh men xốp baba ngâm rượu rum"},
    "lex.en.200k.056404": {"pos": "phrase", "ipa": "", "vi": "trực khuẩn cỏ khô bacillus"},
    "lex.en.200k.056405": {"pos": "phrase", "ipa": "", "vi": "loài cá chó sọc vằn pickerel"},
    "lex.en.200k.056406": {"pos": "phrase", "ipa": "", "vi": "hoa diên vĩ cánh trơn không râu"},
    "lex.en.200k.056407": {"pos": "phrase", "ipa": "", "vi": "nấm thịt bò bít tết vân đỏ"},
    "lex.en.200k.056408": {"pos": "phrase", "ipa": "", "vi": "cà chua thịt quả lớn beefsteak"},
    "lex.en.200k.056409": {"pos": "phrase", "ipa": "", "vi": "pháo phòng không tự động Bofors"},
    "lex.en.200k.056410": {"pos": "phrase", "ipa": "", "vi": "sốt vang đỏ kiểu Bourguignon"},
    "lex.en.200k.056411": {"pos": "phrase", "ipa": "", "vi": "bài ca ngợi khen của Simeon"},
    "lex.en.200k.056412": {"pos": "phrase", "ipa": "", "vi": "dầu xoa dịu vết bỏng Carron"},
    "lex.en.200k.056413": {"pos": "phrase", "ipa": "", "vi": "người mua phải tự chịu rủi ro"},
    "lex.en.200k.056414": {"pos": "phrase", "ipa": "", "vi": "kề vai sát cánh; san sát nhau"},
    "lex.en.200k.056415": {"pos": "phrase", "ipa": "", "vi": "cây cúc hoa ngô Stokes xanh"},
    "lex.en.200k.056416": {"pos": "phrase", "ipa": "", "vi": "loài chim dẽ mỏ cong bụng nâu"},
    "lex.en.200k.056417": {"pos": "phrase", "ipa": "", "vi": "nhà sản xuất phim Darryl Zanuck"},
    "lex.en.200k.056418": {"pos": "phrase", "ipa": "", "vi": "nhà sản xuất phim Darryl Zanuck"},
    "lex.en.200k.056419": {"pos": "phrase", "ipa": "", "vi": "cà phê đã tách chất caffein"},
    "lex.en.200k.056420": {"pos": "phrase", "ipa": "", "vi": "nhà nữ tiên tri đền Delphi Hy Lạp"},
    "lex.en.200k.056421": {"pos": "phrase", "ipa": "", "vi": "băng từ ghi âm kỹ thuật số DAT"},
    "lex.en.200k.056422": {"pos": "phrase", "ipa": "", "vi": "nhà văn nữ Mỹ Edna Ferber"},
    "lex.en.200k.056423": {"pos": "phrase", "ipa": "", "vi": "nhà soạn nhạc Na Uy Edvard Grieg"},
    "lex.en.200k.056424": {"pos": "phrase", "ipa": "", "vi": "nhà văn nhân đạo Elie Wiesel"},
    "lex.en.200k.056425": {"pos": "phrase", "ipa": "", "vi": "nhân tiện; luật bắt tốt qua đường"},
    "lex.en.200k.056426": {"pos": "phrase", "ipa": "", "vi": "khối u xơ cơ trơn lành tính"},
    "lex.en.200k.056427": {"pos": "phrase", "ipa": "", "vi": "Hoàng đế La Mã Theodosius Cả"},
    "lex.en.200k.056428": {"pos": "phrase", "ipa": "", "vi": "lỗ gian não thất Monro ở não"},
    "lex.en.200k.056429": {"pos": "phrase", "ipa": "", "vi": "buồm đỉnh tam giác trên càng gaff"},
    "lex.en.200k.056430": {"pos": "phrase", "ipa": "", "vi": "chi xương rồng thân cột Cereus"},
    "lex.en.200k.056431": {"pos": "phrase", "ipa": "", "vi": "danh họa điểm họa Georges Seurat"},
    "lex.en.200k.056432": {"pos": "phrase", "ipa": "", "vi": "cây phong lữ thảo mềm nhỏ hoa tím"},
    "lex.en.200k.056433": {"pos": "phrase", "ipa": "", "vi": "nhà cách mạng Ý Giuseppe Mazzini"},
    "lex.en.200k.056434": {"pos": "phrase", "ipa": "", "vi": "nhà vật lý học Gustav Kirchhoff"},
    "lex.en.200k.056435": {"pos": "phrase", "ipa": "", "vi": "Hoàng đế Ethiopia Haile Selassie"},
    "lex.en.200k.056436": {"pos": "phrase", "ipa": "", "vi": "đuôi biến cách biến tố ngữ pháp"},
    "lex.en.200k.056437": {"pos": "phrase", "ipa": "", "vi": "nhà văn Anh Izaak Walton"},
    "lex.en.200k.056438": {"pos": "phrase", "ipa": "", "vi": "triết gia Karl Theodor Jaspers"},
    "lex.en.200k.056439": {"pos": "phrase", "ipa": "", "vi": "người dân bang Pennsylvania"},
    "lex.en.200k.056440": {"pos": "phrase", "ipa": "", "vi": "cây kinh giới ngọt marjoram"},
    "lex.en.200k.056441": {"pos": "phrase", "ipa": "", "vi": "thuyết dân số học Thomas Malthus"},
    "lex.en.200k.056442": {"pos": "phrase", "ipa": "", "vi": "rượu mùi quả anh đào Maraschino"},
    "lex.en.200k.056443": {"pos": "phrase", "ipa": "", "vi": "chuyên gia kinh tế học vi mô"},
    "lex.en.200k.056444": {"pos": "phrase", "ipa": "", "vi": "ngộ độc băng phiến naphtalen"},
    "lex.en.200k.056445": {"pos": "phrase", "ipa": "", "vi": "đồng tiền rial của vương quốc Oman"},
    "lex.en.200k.056446": {"pos": "phrase", "ipa": "", "vi": "cây thảo dược cohosh xanh"},
    "lex.en.200k.056447": {"pos": "phrase", "ipa": "", "vi": "tài khoản tiền gửi tiết kiệm có sổ"},
    "lex.en.200k.056448": {"pos": "phrase", "ipa": "", "vi": "tĩnh mạch xuyên nối tĩnh mạch"},
    "lex.en.200k.056449": {"pos": "phrase", "ipa": "", "vi": "nhà thơ nữ da màu Phillis Wheatley"},
    "lex.en.200k.056450": {"pos": "phrase", "ipa": "", "vi": "rung giật nhãn cầu sinh lý tự nhiên"},
    "lex.en.200k.056451": {"pos": "phrase", "ipa": "", "vi": "loài ếch đồng đốm vuông pickerel"},
    "lex.en.200k.056452": {"pos": "phrase", "ipa": "", "vi": "bệnh dịch hạch thể phổi nguy kịch"},
    "lex.en.200k.056453": {"pos": "phrase", "ipa": "", "vi": "bột làm bánh cream of tartar"},
    "lex.en.200k.056454": {"pos": "phrase", "ipa": "", "vi": "muối kép Rochelle tartrat"},
    "lex.en.200k.056455": {"pos": "phrase", "ipa": "", "vi": "cây mận bụi hoa anh đào Nhật Bản"},
    "lex.en.200k.056456": {"pos": "phrase", "ipa": "", "vi": "phát triển tâm lý vận động ở trẻ"},
    "lex.en.200k.056457": {"pos": "phrase", "ipa": "", "vi": "khối đa diện đều hình học phẳng"},
    "lex.en.200k.056458": {"pos": "phrase", "ipa": "", "vi": "chính khách triết gia Lord Haldane"},
    "lex.en.200k.056459": {"pos": "phrase", "ipa": "", "vi": "loài gà gô ruffed Bắc Mỹ"},
    "lex.en.200k.056460": {"pos": "phrase", "ipa": "", "vi": "vùng biển rong biển Sargasso"},
    "lex.en.200k.056461": {"pos": "phrase", "ipa": "", "vi": "vòm cuốn phân đoạn hình cung tròn"},
    "lex.en.200k.056462": {"pos": "phrase", "ipa": "", "vi": "rượu mùi gin ngâm quả mận gai"},
    "lex.en.200k.056463": {"pos": "phrase", "ipa": "", "vi": "hoa phong quỳ cỏ hải đường trắng"},
    "lex.en.200k.056464": {"pos": "phrase", "ipa": "", "vi": "thuốc chống trầm cảm ba vòng TCA"},
    "lex.en.200k.056465": {"pos": "phrase", "ipa": "", "vi": "thuốc chống trầm cảm ba vòng TCA"},
    "lex.en.200k.056466": {"pos": "phrase", "ipa": "", "vi": "cây đậu vảy chùm hoa tím biếc"},
    "lex.en.200k.056467": {"pos": "phrase", "ipa": "", "vi": "tĩnh mạch ngón tay giải phẫu"},
    "lex.en.200k.056468": {"pos": "phrase", "ipa": "", "vi": "vật liệu sợi cellulose lưu hóa"},
    "lex.en.200k.056469": {"pos": "phrase", "ipa": "", "vi": "sóc linh dương đuôi trắng sa mạc"},
    "lex.en.200k.056470": {"pos": "phrase", "ipa": "", "vi": "đại văn hào W. M. Thackeray"},
    "lex.en.200k.056471": {"pos": "noun", "ipa": "/ˌædrɛˈsiːz/", "vi": "người nhận thư tín; người tiếp nhận"},
    "lex.en.200k.056472": {"pos": "noun", "ipa": "/ɪˈniːɪdz/", "vi": "sử thi thiên anh hùng ca Aeneid"},
    "lex.en.200k.056473": {"pos": "noun", "ipa": "/ˈæpsɪz/", "vi": "hốc bán nguyệt gian thờ nhà thờ"},
    "lex.en.200k.056474": {"pos": "noun", "ipa": "/ˈeɪsɪnz/", "vi": "mã số định danh sản phẩm ASIN"},
    "lex.en.200k.056475": {"pos": "noun", "ipa": "/ˈbeɪkəlaɪts/", "vi": "nhựa nhiệt rắn nhân tạo Bakelite"},
    "lex.en.200k.056476": {"pos": "noun", "ipa": "/bænˈzaɪz/", "vi": "tiếng hô vạn tuế; xung phong liều"},
    "lex.en.200k.056477": {"pos": "noun", "ipa": "/bæθˈʃiːbəz/", "vi": "bà hoàng Bathsheba trong Kinh Thánh"},
    "lex.en.200k.056478": {"pos": "noun", "ipa": "/ˈboʊmz/", "vi": "nhà thần bí Đức Jakob Böhme"},
    "lex.en.200k.056479": {"pos": "noun", "ipa": "/ˈbraʊnʃwaɪɡz/", "vi": "thành phố Braunschweig ở Đức"},
    "lex.en.200k.056480": {"pos": "adj", "ipa": "/ˈbrɔːniər/", "vi": "vạm vỡ khỏe mạnh hơn; cơ bắp hơn"},
    "lex.en.200k.056481": {"pos": "adj", "ipa": "/ˈbrɔːniɪst/", "vi": "vạm vỡ khỏe nhất; cơ bắp cuồn cuộn"},
    "lex.en.200k.056482": {"pos": "noun", "ipa": "/ˈbrɔɪərz/", "vi": "kiến trúc sư Marcel Breuer"},
    "lex.en.200k.056483": {"pos": "noun", "ipa": "/ˈbʊlfrɔːɡz/", "vi": "loài ếch bò châu Mỹ; ếch ễnh ương"},
    "lex.en.200k.056484": {"pos": "noun", "ipa": "/kəˈsiːnoʊz/", "vi": "trận Monte Cassino; trò chơi bài"},
    "lex.en.200k.056485": {"pos": "noun", "ipa": "/ˈkoʊlfiːldz/", "vi": "vùng mỏ than khoáng sản"},
    "lex.en.200k.056486": {"pos": "noun", "ipa": "/ˈkɑːkəlz/", "vi": "con sò huyết; sò biển ăn được"},
    "lex.en.200k.056487": {"pos": "noun", "ipa": "/kʌmˈʌpənsɪz/", "vi": "sự trừng phạt thích đáng; quả báo"},
    "lex.en.200k.056488": {"pos": "noun", "ipa": "/ˌkɑːnvərˈseɪʃənəlɪsts/", "vi": "người có tài trò chuyện khéo léo"},
    "lex.en.200k.056489": {"pos": "noun", "ipa": "/ˈkɔːrmərənts/", "vi": "loài chim cốc bắt cá biển"},
    "lex.en.200k.056490": {"pos": "noun", "ipa": "/ˈkræftərz/", "vi": "người làm đồ thủ công mỹ nghệ"},
    "lex.en.200k.056491": {"pos": "noun", "ipa": "/ˈkɜːriərz/", "vi": "thợ thuộc da và nhuộm bóng da"},
    "lex.en.200k.056492": {"pos": "noun", "ipa": "/diːˈmɛrɪts/", "vi": "điểm trừ kỷ luật; lỗi lầm tì vết"},
    "lex.en.200k.056493": {"pos": "noun", "ipa": "/daɪˈmɔːrfɪzəmz/", "vi": "hiện tượng lưỡng hình sinh học"},
    "lex.en.200k.056494": {"pos": "noun", "ipa": "/ˈeɪbroʊz/", "vi": "con sông Ebro ở Tây Ban Nha"},
    "lex.en.200k.056495": {"pos": "noun", "ipa": "/ɪnˈdɔːrsərz/", "vi": "người bảo chứng; người ký hậu séc"},
    "lex.en.200k.056496": {"pos": "noun", "ipa": "/ˈɛərzætsɪz/", "vi": "hàng thay thế nhân tạo rẻ tiền"},
    "lex.en.200k.056497": {"pos": "noun", "ipa": "/ˈflɔːrioʊz/", "vi": "giải đua xe cổ Targa Florio ở Ý"},
    "lex.en.200k.056498": {"pos": "noun", "ipa": "/ˈfʊtfɔːlz/", "vi": "tiếng bước chân đi lại lộp cộp"},
    "lex.en.200k.056499": {"pos": "noun", "ipa": "/ˈfʌŋkʃənɛriz/", "vi": "viên chức quan lại thừa hành"},
    "lex.en.200k.056500": {"pos": "noun", "ipa": "/ˈdʒɛlətiːnz/", "vi": "chất làm đông thạch gelatine"},
    "lex.en.200k.056501": {"pos": "noun", "ipa": "/ˈɡræməz/", "vi": "loài cỏ đồng cỏ khô grama"}
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

with open('scratch/b32_r03_p5.json', 'w', encoding='utf-8') as f:
    json.dump(output_items, f, ensure_ascii=False, indent=2)

print(f"Successfully authored and validated Part 5: {len(output_items)} items saved to scratch/b32_r03_p5.json")
