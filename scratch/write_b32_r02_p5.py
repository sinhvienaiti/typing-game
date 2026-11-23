import json

with open('scratch/b32_r02_raw_p5.json') as f:
    raw_items = json.load(f)

reviewed_data = {
    "lex.en.200k.055902": {"pos": "phrase", "ipa": "", "vi": "cây hoa arbutus bò lan"},
    "lex.en.200k.055903": {"pos": "phrase", "ipa": "", "vi": "hòm nhĩ; khoang tai giữa"},
    "lex.en.200k.055904": {"pos": "phrase", "ipa": "", "vi": "màng nhĩ tai"},
    "lex.en.200k.055905": {"pos": "phrase", "ipa": "", "vi": "tĩnh mạch màng nhĩ"},
    "lex.en.200k.055906": {"pos": "phrase", "ipa": "", "vi": "xe téc chở nước; xe bồn nước"},
    "lex.en.200k.055907": {"pos": "phrase", "ipa": "", "vi": "cá đù trắng"},
    "lex.en.200k.055908": {"pos": "phrase", "ipa": "", "vi": "danh họa Willem de Kooning"},
    "lex.en.200k.055909": {"pos": "noun", "ipa": "/ˌænəˈsɑːtrəpiz/", "vi": "tính dị hướng vật lý"},
    "lex.en.200k.055910": {"pos": "noun", "ipa": "/ˈɛərəmz/", "vi": "loài cây chân vịt; cây họ môn"},
    "lex.en.200k.055911": {"pos": "noun", "ipa": "/ˈɑːsʊrəz/", "vi": "chư thần A-tu-la; ác thần Asura"},
    "lex.en.200k.055912": {"pos": "noun", "ipa": "/æˈswɑːnz/", "vi": "thành phố Aswan ở Ai Cập"},
    "lex.en.200k.055913": {"pos": "noun", "ipa": "/ˈbɛlsənz/", "vi": "trại tập trung Bergen-Belsen"},
    "lex.en.200k.055914": {"pos": "noun", "ipa": "/ˈbɑːtlnoʊzɪz/", "vi": "loài cá heo mũi chai"},
    "lex.en.200k.055915": {"pos": "adj", "ipa": "/ˈbræsiər/", "vi": "chát tai hơn; trơ trẽn bỗ bã hơn"},
    "lex.en.200k.055916": {"pos": "adj", "ipa": "/ˈbræsiɪst/", "vi": "chát tai nhất; trơ trẽn bỗ bã nhất"},
    "lex.en.200k.055917": {"pos": "noun", "ipa": "/ˈkæpjuːʃɪnz/", "vi": "tu sĩ dòng Capuchin; khỉ mũ"},
    "lex.en.200k.055918": {"pos": "noun", "ipa": "/kɑːrˈtɑːɡrəfərz/", "vi": "nhà họa đồ; người vẽ bản đồ"},
    "lex.en.200k.055919": {"pos": "noun", "ipa": "/xɑːˈbɑːdz/", "vi": "phong trào Do Thái giáo Chabad"},
    "lex.en.200k.055920": {"pos": "noun", "ipa": "/ˈʃoʊvənɪsts/", "vi": "kẻ theo chủ nghĩa sô-vanh"},
    "lex.en.200k.055921": {"pos": "noun", "ipa": "/ˈkʌləndərz/", "vi": "rổ chắt nước; rá vo gạo có lỗ"},
    "lex.en.200k.055922": {"pos": "noun", "ipa": "/krəˈvæsɪz/", "vi": "khe nứt sông băng; vực băng sâu"},
    "lex.en.200k.055923": {"pos": "noun", "ipa": "/ˈkruːnərz/", "vi": "ca sĩ hát nhạc trữ tình êm dịu"},
    "lex.en.200k.055924": {"pos": "noun", "ipa": "/ˈkrɔːstɔːks/", "vi": "sự xuyên âm; màn tấu hài đối đáp"},
    "lex.en.200k.055925": {"pos": "noun", "ipa": "/doʊlts/", "vi": "kẻ ngu đần; kẻ đại ngốc"},
    "lex.en.200k.055926": {"pos": "noun", "ipa": "/dwiːbz/", "vi": "kẻ mọt sách lập dị; gã ngờ nghệch"},
    "lex.en.200k.055927": {"pos": "noun", "ipa": "/ˈɛdɪŋtənz/", "vi": "nhà vật lý Arthur Eddington"},
    "lex.en.200k.055928": {"pos": "noun", "ipa": "/ˌiːˌdiːˌtiːˈeɪz/", "vi": "chất tạo phức hóa học EDTA"},
    "lex.en.200k.055929": {"pos": "noun", "ipa": "/fiːz/", "vi": "cô gái trẻ; thiếu nữ người Pháp"},
    "lex.en.200k.055930": {"pos": "noun", "ipa": "/ˈfaɪərbɑːksɪz/", "vi": "buồng đốt nhiên liệu lò hơi"},
    "lex.en.200k.055931": {"pos": "noun", "ipa": "/ˈfɪstfaɪts/", "vi": "cuộc ẩu đả đánh lộn tay đôi"},
    "lex.en.200k.055932": {"pos": "noun", "ipa": "/ˈflætˌaɪərnz/", "vi": "bàn là ủi phẳng cổ điển"},
    "lex.en.200k.055933": {"pos": "adj", "ipa": "/ˈflaɪtiər/", "vi": "nông nổi hơn; bốc đồng thất thường"},
    "lex.en.200k.055934": {"pos": "adj", "ipa": "/ˈflaɪtiɪst/", "vi": "nông nổi nhất; bốc đồng nhất"},
    "lex.en.200k.055935": {"pos": "noun", "ipa": "/ˈflɪntstoʊnz/", "vi": "đá lửa; hòn sỏi lửa bật tia"},
    "lex.en.200k.055936": {"pos": "noun", "ipa": "/ˈflɔːrɪnz/", "vi": "đồng tiền vàng florin cổ"},
    "lex.en.200k.055937": {"pos": "noun", "ipa": "/ˌfrækʃəˈneɪʃənz/", "vi": "phương pháp chưng cất phân đoạn"},
    "lex.en.200k.055938": {"pos": "noun", "ipa": "/ˈɡɪlmərz/", "vi": "thành phố Gilmer ở bang Texas"},
    "lex.en.200k.055939": {"pos": "noun", "ipa": "/ɡlaɪˈkɑːləsiːz/", "vi": "quá trình đường phân năng lượng"},
    "lex.en.200k.055940": {"pos": "noun", "ipa": "/ɡuˈɑːʃɪz/", "vi": "tranh vẽ màu nước bột đục gouache"},
    "lex.en.200k.055941": {"pos": "noun", "ipa": "/ˈɡrɪfənz/", "vi": "quái thú đầu ưng mình sư tử"},
    "lex.en.200k.055942": {"pos": "noun", "ipa": "/ˌɡwaɪəˈkiːlz/", "vi": "thành phố cảng Guayaquil"},
    "lex.en.200k.055943": {"pos": "noun", "ipa": "/ˈhɑːrdtɑːps/", "vi": "xe ô tô mui cứng kim loại"},
    "lex.en.200k.055944": {"pos": "noun", "ipa": "/ˌhaɪəˈwɑːθəz/", "vi": "thủ lĩnh bộ tộc Hiawatha"},
    "lex.en.200k.055945": {"pos": "noun", "ipa": "/ˌhɪndʊˈstɑːniz/", "vi": "người Hindustan; tiếng Hin-đu"},
    "lex.en.200k.055946": {"pos": "noun", "ipa": "/ˈhɪpədroʊmz/", "vi": "trường đua ngựa đấu giác đấu cổ"},
    "lex.en.200k.055947": {"pos": "noun", "ipa": "/hɑːθs/", "vi": "hành tinh băng giá Hoth"},
    "lex.en.200k.055948": {"pos": "noun", "ipa": "/ˈhɜːrdlərz/", "vi": "vận động viên vượt rào"},
    "lex.en.200k.055949": {"pos": "noun", "ipa": "/haɪˈdreɪndʒəz/", "vi": "hoa cẩm tú cầu đổi màu"},
    "lex.en.200k.055950": {"pos": "noun", "ipa": "/aɪˈæmbɪks/", "vi": "thể thơ nhịp iamb hai âm tiết"},
    "lex.en.200k.055951": {"pos": "noun", "ipa": "/ˌɪntərˈlɑːkjətərz/", "vi": "người đối thoại; người đàm thoại"},
    "lex.en.200k.055952": {"pos": "noun", "ipa": "/dʒɑːts/", "vi": "người dân tộc Jat ở Nam Á"},
    "lex.en.200k.055953": {"pos": "noun", "ipa": "/ˈdʒɑːbərz/", "vi": "thương nhân bán buôn trung gian"},
    "lex.en.200k.055954": {"pos": "noun", "ipa": "/kɪˌniːsiˈɑːlədʒiz/", "vi": "môn khoa học vận động cơ thể"},
    "lex.en.200k.055955": {"pos": "noun", "ipa": "/ˈkaɪpərz/", "vi": "nhà thiên văn học Gerard Kuiper"},
    "lex.en.200k.055956": {"pos": "noun", "ipa": "/ˈleɪmiiː/", "vi": "nữ quỷ hút máu Lamia Hy Lạp"},
    "lex.en.200k.055957": {"pos": "noun", "ipa": "/ˈleɪmiəz/", "vi": "nữ quỷ nửa người nửa rắn Lamia"},
    "lex.en.200k.055958": {"pos": "noun", "ipa": "/ˈluːblɪnz/", "vi": "thành phố Lublin ở Ba Lan"},
    "lex.en.200k.055959": {"pos": "noun", "ipa": "/ˈmɔːltɪdz/", "vi": "sữa lắc mạch nha thơm béo"},
    "lex.en.200k.055960": {"pos": "noun", "ipa": "/ˈmɑːrʃənɪsɪz/", "vi": "các nữ hầu tước quý tộc"},
    "lex.en.200k.055961": {"pos": "noun", "ipa": "/ˌmɛnəˈleɪəsɪz/", "vi": "vua Sparta Menelaus sử thi"},
    "lex.en.200k.055962": {"pos": "noun", "ipa": "/ˈmɪdrɪfs/", "vi": "vùng cơ hoành eo bụng; áo lửng"},
    "lex.en.200k.055963": {"pos": "noun", "ipa": "/ˈmɪndənz/", "vi": "thị trấn Minden ở Đức"},
    "lex.en.200k.055964": {"pos": "noun", "ipa": "/ˈmɪsɪvz/", "vi": "thư tín dài; công văn trịnh trọng"},
    "lex.en.200k.055965": {"pos": "noun", "ipa": "/mʌŋz/", "vi": "hạt đậu xanh; cây đậu xanh"},
    "lex.en.200k.055966": {"pos": "noun", "ipa": "/ˈmjuːɑːnz/", "vi": "hạt muon cơ bản trong vật lý"},
    "lex.en.200k.055967": {"pos": "noun", "ipa": "/ˈmaɪlɑːrz/", "vi": "màng nhựa polyester mỏng Mylar"},
    "lex.en.200k.055968": {"pos": "noun", "ipa": "/ˈmaɪəsɪnz/", "vi": "protein co cơ myosin sinh học"},
    "lex.en.200k.055969": {"pos": "noun", "ipa": "/ˌnʊroʊblæˈstoʊməz/", "vi": "khối u nguyên bào thần kinh"},
    "lex.en.200k.055970": {"pos": "noun", "ipa": "/ˌnɑːnkənˈfɔːrmɪsts/", "vi": "người không theo quy ước xã hội"},
    "lex.en.200k.055971": {"pos": "noun", "ipa": "/ˌoʊbəˈdaɪəz/", "vi": "sách tiên tri Ô-ba-đia Cựu Ước"},
    "lex.en.200k.055972": {"pos": "noun", "ipa": "/ˈpɑːrkərzbɜːrɡz/", "vi": "thành phố Parkersburg của Mỹ"},
    "lex.en.200k.055973": {"pos": "noun", "ipa": "/pɑːrˈnæsəsɪz/", "vi": "ngọn núi Parnassus thần thoại"},
    "lex.en.200k.055974": {"pos": "noun", "ipa": "/ˌpiːˌeɪˌwaɪˈiːz/", "vi": "chế độ nộp thuế thu nhập tự động"},
    "lex.en.200k.055975": {"pos": "noun", "ipa": "/ˈpɛntətuːks/", "vi": "năm sách luật Ngũ Thư Kinh Thánh"},
    "lex.en.200k.055976": {"pos": "noun", "ipa": "/ˈpɛpɪnz/", "vi": "vua Pepin của vương quốc Frank"},
    "lex.en.200k.055977": {"pos": "noun", "ipa": "/piːəˈʒeɪz/", "vi": "nhà tâm lý học Jean Piaget"},
    "lex.en.200k.055978": {"pos": "noun", "ipa": "/ˈpɪnstraɪps/", "vi": "họa tiết kẻ sọc tăm; vest sọc nhỏ"},
    "lex.en.200k.055979": {"pos": "noun", "ipa": "/ˌnuːmoʊˈθɔːræksɪz/", "vi": "bệnh lý tràn khí màng phổi"},
    "lex.en.200k.055980": {"pos": "noun", "ipa": "/prəˈsɛʃənəlz/", "vi": "bài thánh ca diễu hành rước lễ"},
    "lex.en.200k.055981": {"pos": "noun", "ipa": "/ˈprɑːflɪɡɪts/", "vi": "kẻ trác táng hoang toàng phung phí"},
    "lex.en.200k.055982": {"pos": "noun", "ipa": "/proʊˈlæktɪnz/", "vi": "hoóc-môn tiết sữa prolactin"},
    "lex.en.200k.055983": {"pos": "noun", "ipa": "/ˌproʊtioʊˈmɪksɪz/", "vi": "ngành nghiên cứu protein cơ thể"},
    "lex.en.200k.055984": {"pos": "noun", "ipa": "/ˈprɑːksɪməz/", "vi": "sao Cận Tinh Proxima Centauri"},
    "lex.en.200k.055985": {"pos": "noun", "ipa": "/ˈkwɑːdrəsɛpsɪz/", "vi": "khối cơ tứ đầu đùi chân"},
    "lex.en.200k.055986": {"pos": "noun", "ipa": "/ˌkwɑːdrəˈlætərəlz/", "vi": "hình tứ giác bốn cạnh hình học"},
    "lex.en.200k.055987": {"pos": "noun", "ipa": "/ˈkwɔːrtaɪlz/", "vi": "điểm tứ phân vị trong thống kê"},
    "lex.en.200k.055988": {"pos": "noun", "ipa": "/ˈræɡtæɡz/", "vi": "đám dân hỗn tạp nhếch nhác"},
    "lex.en.200k.055989": {"pos": "noun", "ipa": "/ˈræzəlz/", "vi": "sự ồn ào náo nhiệt phô trương"},
    "lex.en.200k.055990": {"pos": "noun", "ipa": "/riːˈsteɪtmənts/", "vi": "lời trình bày lại; sự phát biểu lại"},
    "lex.en.200k.055991": {"pos": "noun", "ipa": "/ˌsaɪəˈnɑːrəz/", "vi": "lời chào tạm biệt; từ biệt"},
    "lex.en.200k.055992": {"pos": "noun", "ipa": "/ˈskrɪptˌraɪtərz/", "vi": "nhà biên kịch phim kịch bản"},
    "lex.en.200k.055993": {"pos": "adj", "ipa": "/ˈskʌmiər/", "vi": "bẩn thỉu hơn; đê tiện đê hèn hơn"},
    "lex.en.200k.055994": {"pos": "adj", "ipa": "/ˈskʌmiɪst/", "vi": "bẩn thỉu nhất; đê tiện đê hèn nhất"},
    "lex.en.200k.055995": {"pos": "noun", "ipa": "/sɪˈɡoʊviəz/", "vi": "nghệ sĩ guitar Andrés Segovia"},
    "lex.en.200k.055996": {"pos": "noun", "ipa": "/ˈsmɪdʒɪz/", "vi": "chút xíu; mẩu tí teo; chút ít"},
    "lex.en.200k.055997": {"pos": "adj", "ipa": "/ˈspɪfiər/", "vi": "diện hơn; bảnh bao lịch sự hơn"},
    "lex.en.200k.055998": {"pos": "adj", "ipa": "/ˈspɪfiɪst/", "vi": "diện nhất; bảnh bao lịch sự nhất"},
    "lex.en.200k.055999": {"pos": "noun", "ipa": "/ˈsteɪtruːmz/", "vi": "phòng khánh tiết; cabin tàu cao cấp"},
    "lex.en.200k.056000": {"pos": "noun", "ipa": "/stɑːˈvɑːŋərz/", "vi": "thành phố cảng Stavanger ở Na Uy"},
    "lex.en.200k.056001": {"pos": "noun", "ipa": "/stɪlts/", "vi": "cặp cà kheo; cọc chống nhà sàn"}
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

with open('scratch/b32_r02_p5.json', 'w', encoding='utf-8') as f:
    json.dump(output_items, f, ensure_ascii=False, indent=2)

print(f"Successfully authored and validated Part 5: {len(output_items)} items saved to scratch/b32_r02_p5.json")
