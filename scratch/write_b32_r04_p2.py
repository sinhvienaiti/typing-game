import json

with open('scratch/b32_r04_raw_p2.json') as f:
    raw_items = json.load(f)

reviewed_data = {
    "lex.en.200k.056602": {"pos": "noun", "ipa": "/ˈfʊtstuːlz/", "vi": "chiếc ghế đôn kê chân nhỏ"},
    "lex.en.200k.056603": {"pos": "noun", "ipa": "/ˈfroʊbɪʃərz/", "vi": "nhà hàng hải Martin Frobisher"},
    "lex.en.200k.056604": {"pos": "noun", "ipa": "/ˌɡluːkoʊˈkɔːrtɪkɔɪdz/", "vi": "hoóc-môn steroid chống viêm"},
    "lex.en.200k.056605": {"pos": "noun", "ipa": "/ɡluːˈkoʊsəmiːnz/", "vi": "hợp chất bổ khớp glucosamine"},
    "lex.en.200k.056606": {"pos": "noun", "ipa": "/ˈɡruːpθɪŋks/", "vi": "tư duy bầy đàn; tư duy tập thể"},
    "lex.en.200k.056607": {"pos": "noun", "ipa": "/ˈhaɪweɪmən/", "vi": "những tên cướp đường cưỡi ngựa"},
    "lex.en.200k.056608": {"pos": "noun", "ipa": "/ˈhɪmnəlz/", "vi": "sách thánh ca trong nhà thờ"},
    "lex.en.200k.056609": {"pos": "noun", "ipa": "/ˌɪɡnəˈreɪməsɪz/", "vi": "kẻ dốt đặc cán mai; kẻ ngu dốt"},
    "lex.en.200k.056610": {"pos": "noun", "ipa": "/ɪˈmeɪɡoʊz/", "vi": "giai đoạn trưởng thành côn trùng"},
    "lex.en.200k.056611": {"pos": "noun", "ipa": "/ˌɪndʌkˈtiːz/", "vi": "người được vinh danh; tân binh"},
    "lex.en.200k.056612": {"pos": "noun", "ipa": "/ˈɪntrɪkəsiz/", "vi": "chi tiết phức tạp; sự rắc rối"},
    "lex.en.200k.056613": {"pos": "noun", "ipa": "/ˈdʒækhæmərz/", "vi": "máy khoan phá bê tông chạy khí"},
    "lex.en.200k.056614": {"pos": "noun", "ipa": "/ˈdʒeɪnɪzəmz/", "vi": "đạo Kì-na giáo; Kỳ-na giáo Ấn Độ"},
    "lex.en.200k.056615": {"pos": "noun", "ipa": "/ˈkɑːlsəz/", "vi": "cộng đồng chiến binh thánh Khalsa"},
    "lex.en.200k.056616": {"pos": "noun", "ipa": "/ˈkɔːriːz/", "vi": "tượng phụ nữ Hy Lạp Kore; nữ thần"},
    "lex.en.200k.056617": {"pos": "verb", "ipa": "/læmˈpuːnd/", "vi": "đã chế giễu; đã đả kích châm biếm"},
    "lex.en.200k.056618": {"pos": "verb", "ipa": "/læmˈpuːnɪŋ/", "vi": "đả kích châm biếm; chế giễu cay độc"},
    "lex.en.200k.056619": {"pos": "noun", "ipa": "/læmˈpuːnz/", "vi": "bài văn châm biếm; tác phẩm giễu"},
    "lex.en.200k.056620": {"pos": "noun", "ipa": "/ˈlɔːtənz/", "vi": "diễn viên kỳ cựu Charles Laughton"},
    "lex.en.200k.056621": {"pos": "noun", "ipa": "/lɛks/", "vi": "bãi ve vãn giao phối; đồng lek"},
    "lex.en.200k.056622": {"pos": "noun", "ipa": "/ˈlɛmɪŋz/", "vi": "loài chuột lemming; kẻ a dua"},
    "lex.en.200k.056623": {"pos": "noun", "ipa": "/ˈlɪntʃpɪnz/", "vi": "chốt hãm trục xe; nhân tố cốt lõi"},
    "lex.en.200k.056624": {"pos": "noun", "ipa": "/məˈkɔːz/", "vi": "loài vẹt đuôi dài rực rỡ macaw"},
    "lex.en.200k.056625": {"pos": "noun", "ipa": "/ˈmæɡlɛvz/", "vi": "tàu hỏa đệm từ trường tốc độ cao"},
    "lex.en.200k.056626": {"pos": "noun", "ipa": "/ˌmælɪˈnɔːfskiz/", "vi": "nhà nhân học Bronisław Malinowski"},
    "lex.en.200k.056627": {"pos": "noun", "ipa": "/ˈmælənz/", "vi": "bệnh nhân Mary Mallon truyền bệnh"},
    "lex.en.200k.056628": {"pos": "noun", "ipa": "/ˈmæləriz/", "vi": "nhà văn Sir Thomas Malory"},
    "lex.en.200k.056629": {"pos": "noun", "ipa": "/ˈmɛɡətʌnz/", "vi": "đơn vị triệu tấn thuốc nổ TNT"},
    "lex.en.200k.056630": {"pos": "noun", "ipa": "/meɪˈtiːdz/", "vi": "người bản địa lai da đỏ Métis"},
    "lex.en.200k.056631": {"pos": "noun", "ipa": "/mɪˈdæzoʊlæmz/", "vi": "thuốc an thần tiền mê midazolam"},
    "lex.en.200k.056632": {"pos": "noun", "ipa": "/ˌmɑːləˈkaɪz/", "vi": "hòn đảo Molokai ở Hawaii"},
    "lex.en.200k.056633": {"pos": "noun", "ipa": "/ˈmɑːŋɡəlɔɪdz/", "vi": "người chủng Á da vàng; người Down"},
    "lex.en.200k.056634": {"pos": "noun", "ipa": "/ˌmɑːnoʊəˈmiːnz/", "vi": "chất dẫn truyền thần kinh monoamin"},
    "lex.en.200k.056635": {"pos": "noun", "ipa": "/mɑːnˈtɛzɪz/", "vi": "nữ vũ công trứ danh Lola Montez"},
    "lex.en.200k.056636": {"pos": "noun", "ipa": "/ˈmoʊtaɪlz/", "vi": "dạng di động; trí nhớ vận động"},
    "lex.en.200k.056637": {"pos": "noun", "ipa": "/ˈneɪhəmz/", "vi": "sách tiên tri Na-hum Kinh Thánh"},
    "lex.en.200k.056638": {"pos": "noun", "ipa": "/ˌnʊroʊˈtɑːksɪnz/", "vi": "chất độc thần kinh nguy hiểm"},
    "lex.en.200k.056639": {"pos": "adj", "ipa": "/ˈɔːrnəriər/", "vi": "cáu bẳn hơn; gàn dở khó tính hơn"},
    "lex.en.200k.056640": {"pos": "adj", "ipa": "/ˈɔːrnəriɪst/", "vi": "cáu bẳn nhất; gàn dở nhất"},
    "lex.en.200k.056641": {"pos": "noun", "ipa": "/ˈoʊənzbərəʊz/", "vi": "thành phố Owensboro ở Kentucky"},
    "lex.en.200k.056642": {"pos": "noun", "ipa": "/ˌpærəˈθaɪrɔɪdz/", "vi": "các tuyến cận giáp trong cơ thể"},
    "lex.en.200k.056643": {"pos": "noun", "ipa": "/ˌpiːˌoʊˈbiːz/", "vi": "hộp thư bưu điện POB"},
    "lex.en.200k.056644": {"pos": "verb", "ipa": "/ˈpɑːmpədɔːrd/", "vi": "đã chải hất ngược kiểu pompadour"},
    "lex.en.200k.056645": {"pos": "noun", "ipa": "/ˈpɑːmpədɔːrz/", "vi": "kiểu tóc uốn phồng bồng pompadour"},
    "lex.en.200k.056646": {"pos": "noun", "ipa": "/ˈpɑːntəsɪz/", "vi": "vương quốc cổ Pontus bên Biển Đen"},
    "lex.en.200k.056647": {"pos": "noun", "ipa": "/ˌpriːɪˈklæmpsiəz/", "vi": "chứng tiền sản giật ở thai phụ"},
    "lex.en.200k.056648": {"pos": "noun", "ipa": "/ˈpraɪəmz/", "vi": "vua thành Troy Priam trong sử thi"},
    "lex.en.200k.056649": {"pos": "verb", "ipa": "/ˈpʌməld/", "vi": "đã đấm túi bụi; đã đánh liên tiếp"},
    "lex.en.200k.056650": {"pos": "noun", "ipa": "/ˌkeɪsəˈdiːjəz/", "vi": "bánh kẹp phô mai nướng quesadilla"},
    "lex.en.200k.056651": {"pos": "noun", "ipa": "/ˈrɪdʒlaɪnz/", "vi": "đường gờ sống núi; dải đỉnh núi"},
    "lex.en.200k.056652": {"pos": "noun", "ipa": "/ˈrɪɡərz/", "vi": "thợ lắp giàn khoan; thợ buộc cáp"},
    "lex.en.200k.056653": {"pos": "noun", "ipa": "/sæmˈsɑːrəz/", "vi": "vòng luân hồi sinh tử bất tận"},
    "lex.en.200k.056654": {"pos": "noun", "ipa": "/sɑːrˈtɔːriəsɪz/", "vi": "dải cơ may ở đùi giải phẫu"},
    "lex.en.200k.056655": {"pos": "noun", "ipa": "/sætˈsuːməz/", "vi": "giống cam quýt ngọt satsuma Nhật"},
    "lex.en.200k.056656": {"pos": "noun", "ipa": "/ˈʃɑːplɪftərz/", "vi": "kẻ trộm vặt ở cửa hàng siêu thị"},
    "lex.en.200k.056657": {"pos": "noun", "ipa": "/ˈsɪndiz/", "vi": "người dân tộc Sindh ở Pakistan"},
    "lex.en.200k.056658": {"pos": "noun", "ipa": "/ˈsɪnjuːz/", "vi": "đường gân cơ bắp; nguồn sức mạnh"},
    "lex.en.200k.056659": {"pos": "adj", "ipa": "/ˈsʌlkiər/", "vi": "hờn dỗi hơn; mặt ủ rũ khó đăm đăm"},
    "lex.en.200k.056660": {"pos": "noun", "ipa": "/ˈsʌlkiz/", "vi": "xe ngựa kéo hai bánh đua sulky"},
    "lex.en.200k.056661": {"pos": "adj", "ipa": "/ˈsʌlkiɪst/", "vi": "hay hờn dỗi nhất; ủ rũ nhất"},
    "lex.en.200k.056662": {"pos": "noun", "ipa": "/ˈtɔːriːnz/", "vi": "axit amin taurine bổ não tim"},
    "lex.en.200k.056663": {"pos": "noun", "ipa": "/ˌtɛnəˈsiːənz/", "vi": "người dân bang Tennessee nước Mỹ"},
    "lex.en.200k.056664": {"pos": "noun", "ipa": "/juːˈkreɪniənz/", "vi": "người dân đất nước Ukraina"},
    "lex.en.200k.056665": {"pos": "adj", "ipa": "/ʌnˈwɛəriər/", "vi": "mất cảnh giác hơn; lơ là hơn"},
    "lex.en.200k.056666": {"pos": "adj", "ipa": "/ʌnˈwɛəriɪst/", "vi": "mất cảnh giác nhất; sơ hở nhất"},
    "lex.en.200k.056667": {"pos": "noun", "ipa": "/vəˈlɑːsɪræptərz/", "vi": "khủng long săn mồi velociraptor"},
    "lex.en.200k.056668": {"pos": "noun", "ipa": "/ˈweɪstərz/", "vi": "kẻ hoang phí; kẻ lãng phí thời giờ"},
    "lex.en.200k.056669": {"pos": "noun", "ipa": "/zæˈkɑːts/", "vi": "khoản thuế từ thiện zakat Hồi giáo"},
    "lex.en.200k.056670": {"pos": "phrase", "ipa": "", "vi": "nhóm vũ trang tổ chức Abu Nidal"},
    "lex.en.200k.056671": {"pos": "phrase", "ipa": "", "vi": "bột nhào làm mì sợi nui pasta"},
    "lex.en.200k.056672": {"pos": "phrase", "ipa": "", "vi": "đường ống dẫn tiêu hóa thức ăn"},
    "lex.en.200k.056673": {"pos": "phrase", "ipa": "", "vi": "cây đoạn hoa bồ đề châu Mỹ"},
    "lex.en.200k.056674": {"pos": "phrase", "ipa": "", "vi": "nhà thơ Mỹ Archibald MacLeish"},
    "lex.en.200k.056675": {"pos": "phrase", "ipa": "", "vi": "nhạc trưởng lừng danh Toscanini"},
    "lex.en.200k.056676": {"pos": "phrase", "ipa": "", "vi": "tổ chức Hội dòng Cam Orangemen"},
    "lex.en.200k.056677": {"pos": "phrase", "ipa": "", "vi": "cầu phao bằng thuyền nổi quân sự"},
    "lex.en.200k.056678": {"pos": "phrase", "ipa": "", "vi": "người dân bang Kentucky nước Mỹ"},
    "lex.en.200k.056679": {"pos": "phrase", "ipa": "", "vi": "nhiệt lượng kế bom kín áp suất"},
    "lex.en.200k.056680": {"pos": "phrase", "ipa": "", "vi": "các loài cá rình mồi tầng đáy"},
    "lex.en.200k.056681": {"pos": "phrase", "ipa": "", "vi": "cây mù tạt đen gia vị hạt"},
    "lex.en.200k.056682": {"pos": "phrase", "ipa": "", "vi": "chất trợ tim cardiac glycoside"},
    "lex.en.200k.056683": {"pos": "phrase", "ipa": "", "vi": "nhà văn nữ Mỹ Carson McCullers"},
    "lex.en.200k.056684": {"pos": "phrase", "ipa": "", "vi": "nhà văn Mỹ Carson Smith McCullers"},
    "lex.en.200k.056685": {"pos": "phrase", "ipa": "", "vi": "nhà quật hài cốt; gian để hài cốt"},
    "lex.en.200k.056686": {"pos": "phrase", "ipa": "", "vi": "bánh quy dừa nướng giòn ngọt"},
    "lex.en.200k.056687": {"pos": "phrase", "ipa": "", "vi": "phản ứng hóa học thu nhiệt lượng"},
    "lex.en.200k.056688": {"pos": "phrase", "ipa": "", "vi": "Giáo hoàng Sixtus IV Rovere"},
    "lex.en.200k.056689": {"pos": "phrase", "ipa": "", "vi": "nhà soạn nhạc Anh Frederick Delius"},
    "lex.en.200k.056690": {"pos": "phrase", "ipa": "", "vi": "cây long đởm xanh có tua riềm"},
    "lex.en.200k.056691": {"pos": "phrase", "ipa": "", "vi": "con sông Garonne miền tây nam Pháp"},
    "lex.en.200k.056692": {"pos": "phrase", "ipa": "", "vi": "danh họa Georges-Pierre Seurat"},
    "lex.en.200k.056693": {"pos": "phrase", "ipa": "", "vi": "nhóm cơ mông vùng xương chậu"},
    "lex.en.200k.056694": {"pos": "phrase", "ipa": "", "vi": "đế chế triều đại Hohenzollern"},
    "lex.en.200k.056695": {"pos": "phrase", "ipa": "", "vi": "loài vịt mào mỏ nhọn châu Mỹ"},
    "lex.en.200k.056696": {"pos": "phrase", "ipa": "", "vi": "loài địa y sợi tóc ngựa nâu đen"},
    "lex.en.200k.056697": {"pos": "phrase", "ipa": "", "vi": "nhà khoa học Nobel Howard Florey"},
    "lex.en.200k.056698": {"pos": "phrase", "ipa": "", "vi": "nhà sinh lý học Hudson Hoagland"},
    "lex.en.200k.056699": {"pos": "phrase", "ipa": "", "vi": "axit hydrazoic; hydro azua HN3"},
    "lex.en.200k.056700": {"pos": "phrase", "ipa": "", "vi": "nhà báo điều tra Lincoln Steffens"},
    "lex.en.200k.056701": {"pos": "phrase", "ipa": "", "vi": "đơn vị tiền tệ của Kazakhstan"}
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

with open('scratch/b32_r04_p2.json', 'w', encoding='utf-8') as f:
    json.dump(output_items, f, ensure_ascii=False, indent=2)

print(f"Successfully authored and validated Part 2: {len(output_items)} items saved to scratch/b32_r04_p2.json")
