import json, re

with open('scratch/b32_r02_raw_p2.json') as f:
    raw_items = json.load(f)

# Human QA reviewed definitions for Part 2 (records 600 to 699, IDs 055602 to 055701)
reviewed_data = {
    "lex.en.200k.055602": {"pos": "noun", "ipa": "/ˈpɑːmpənoʊz/", "vi": "cá chim biển; cá pompano"},
    "lex.en.200k.055603": {"pos": "noun", "ipa": "/ˌpoʊpʊˈriːz/", "vi": "hoa khô thơm; mớ hỗn hợp"},
    "lex.en.200k.055604": {"pos": "noun", "ipa": "/proʊˈbɑːsɪdiːz/", "vi": "vòi voi; vòi côn trùng; mũi dài"},
    "lex.en.200k.055605": {"pos": "noun", "ipa": "/proʊˈbɑːsɪsɪz/", "vi": "vòi voi; vòi côn trùng; mũi dài"},
    "lex.en.200k.055606": {"pos": "noun", "ipa": "/proʊˈklɪvətiz/", "vi": "khuynh hướng; thiên hướng"},
    "lex.en.200k.055607": {"pos": "noun", "ipa": "/ˈpuːljəz/", "vi": "vùng Puglia của Ý"},
    "lex.en.200k.055608": {"pos": "noun", "ipa": "/ˈpɜːrsərz/", "vi": "viên quản lý tàu; tiếp viên trưởng"},
    "lex.en.200k.055609": {"pos": "noun", "ipa": "/ˈreɪndʒˌfaɪndərz/", "vi": "máy đo cự ly; máy đo khoảng cách"},
    "lex.en.200k.055610": {"pos": "noun", "ipa": "/ˈriːdʒənəlɪzəmz/", "vi": "chủ nghĩa địa phương; từ địa phương"},
    "lex.en.200k.055611": {"pos": "noun", "ipa": "/ˈrɛŋkwɪsts/", "vi": "chánh án William Rehnquist"},
    "lex.en.200k.055612": {"pos": "noun", "ipa": "/ˌriːpəˈzɛʃənz/", "vi": "sự tịch thu tài sản thế chấp"},
    "lex.en.200k.055613": {"pos": "noun", "ipa": "/ˌruːməˈtɑːlədʒiz/", "vi": "khoa thấp khớp học"},
    "lex.en.200k.055614": {"pos": "noun", "ipa": "/ˌsækərəˈmaɪsiːsɪz/", "vi": "chi nấm men bia"},
    "lex.en.200k.055615": {"pos": "noun", "ipa": "/ˈsælˌtaɪərz/", "vi": "chữ thập chéo chữ X"},
    "lex.en.200k.055616": {"pos": "noun", "ipa": "/ˌɛsˌsiːˈdiːz/", "vi": "bằng tiến sĩ khoa học"},
    "lex.en.200k.055617": {"pos": "noun", "ipa": "/ˈʃnɪtsəlz/", "vi": "món thịt bao bột rán schnitzel"},
    "lex.en.200k.055618": {"pos": "noun", "ipa": "/ˈskrætʃərz/", "vi": "dụng cụ gãi; vé cào trúng thưởng"},
    "lex.en.200k.055619": {"pos": "noun", "ipa": "/ˈsiːˌʃɛlz/", "vi": "vỏ sò; vỏ ốc biển"},
    "lex.en.200k.055620": {"pos": "noun", "ipa": "/ˈsɑːrdʒənts/", "vi": "hội viên luật sư cao cấp; trung sĩ"},
    "lex.en.200k.055621": {"pos": "noun", "ipa": "/ˈʃɔːrtkeɪks/", "vi": "bánh xốp kem dâu shortcake"},
    "lex.en.200k.055622": {"pos": "verb", "ipa": "/ˈʃrɪvəlɪŋ/", "vi": "làm teo lại; héo hon; khô quắt"},
    "lex.en.200k.055623": {"pos": "noun", "ipa": "/sɪˈbeɪliəsɪz/", "vi": "nhà soạn nhạc Jean Sibelius"},
    "lex.en.200k.055624": {"pos": "noun", "ipa": "/sɪbz/", "vi": "anh chị em ruột"},
    "lex.en.200k.055625": {"pos": "noun", "ipa": "/ˌstɛrələˈzeɪʃənz/", "vi": "sự triệt sản; sự tiệt trùng"},
    "lex.en.200k.055626": {"pos": "noun", "ipa": "/staɪlz/", "vi": "bậc thang qua rào; đố cửa đứng"},
    "lex.en.200k.055627": {"pos": "noun", "ipa": "/ˈstrætədʒəmz/", "vi": "mưu kế; mưu chước; kế sách"},
    "lex.en.200k.055628": {"pos": "verb", "ipa": "/ˈʃʊɡərˌkoʊtɪd/", "vi": "bọc đường; nói giảm nhẹ bề ngoài"},
    "lex.en.200k.055629": {"pos": "verb", "ipa": "/ˈʃʊɡərˌkoʊtɪŋ/", "vi": "bọc đường; nói giảm nhẹ để dễ nghe"},
    "lex.en.200k.055630": {"pos": "verb", "ipa": "/ˈʃʊɡərˌkoʊts/", "vi": "bọc đường; nói khéo giảm khó chịu"},
    "lex.en.200k.055631": {"pos": "noun", "ipa": "/ˈtɑːləz/", "vi": "đồng tala Samoa; nhịp tala Ấn Độ"},
    "lex.en.200k.055632": {"pos": "noun", "ipa": "/ˈtuːnɪkəz/", "vi": "lớp màng bọc; áo màng giải phẫu"},
    "lex.en.200k.055633": {"pos": "noun", "ipa": "/ˈtɜːrnstaɪlz/", "vi": "cổng xoay kiểm soát ra vào"},
    "lex.en.200k.055634": {"pos": "noun", "ipa": "/ˈtwɪŋkiz/", "vi": "bánh xốp kem Twinkie"},
    "lex.en.200k.055635": {"pos": "noun", "ipa": "/ˈʌmbrəz/", "vi": "vùng bóng tối hoàn toàn; vùng tối"},
    "lex.en.200k.055636": {"pos": "noun", "ipa": "/ˈveɪɡaɪ/", "vi": "các dây thần kinh phế vị"},
    "lex.en.200k.055637": {"pos": "noun", "ipa": "/vælˈdɑːstəz/", "vi": "thành phố Valdosta"},
    "lex.en.200k.055638": {"pos": "noun", "ipa": "/ˈwɔːsɔːz/", "vi": "thành phố Wausau"},
    "lex.en.200k.055639": {"pos": "noun", "ipa": "/ˈweɪvlɪts/", "vi": "gợn sóng nhỏ; sóng con toán học"},
    "lex.en.200k.055640": {"pos": "noun", "ipa": "/ˈwɛbˌmæstərz/", "vi": "người quản trị trang web"},
    "lex.en.200k.055641": {"pos": "noun", "ipa": "/viːˈzɛlz/", "vi": "nhà văn Elie Wiesel"},
    "lex.en.200k.055642": {"pos": "noun", "ipa": "/ˈvɪnthʊks/", "vi": "thủ đô Windhoek của Namibia"},
    "lex.en.200k.055643": {"pos": "adj", "ipa": "/ˈwɪnsərmər/", "vi": "hấp dẫn hơn; duyên dáng hơn"},
    "lex.en.200k.055644": {"pos": "adj", "ipa": "/ˈwɪnsərmɪst/", "vi": "hấp dẫn nhất; duyên dáng nhất"},
    "lex.en.200k.055645": {"pos": "noun", "ipa": "/vɪtˈvɑːtərzˌrændz/", "vi": "vùng khai khoáng Witwatersrand"},
    "lex.en.200k.055646": {"pos": "noun", "ipa": "/ˈwʊdhaʊsɪz/", "vi": "nhà văn P. G. Wodehouse"},
    "lex.en.200k.055647": {"pos": "noun", "ipa": "/jɪzˈrɑːɛlz/", "vi": "người mang tên Yisrael; Israel"},
    "lex.en.200k.055648": {"pos": "noun", "ipa": "/ˈziːɡfɛldz/", "vi": "nhà sản xuất Florenz Ziegfeld"},
    "lex.en.200k.055649": {"pos": "phrase", "ipa": "", "vi": "nhà sử học nghệ thuật Aby Warburg"},
    "lex.en.200k.055650": {"pos": "phrase", "ipa": "", "vi": "tĩnh mạch đầu phụ"},
    "lex.en.200k.055651": {"pos": "phrase", "ipa": "", "vi": "Agrippina Cả; Agrippina Trưởng"},
    "lex.en.200k.055652": {"pos": "phrase", "ipa": "", "vi": "Agrippina Trẻ; Agrippina Con"},
    "lex.en.200k.055653": {"pos": "phrase", "ipa": "", "vi": "chỉ huy Ahmad Shah Massoud"},
    "lex.en.200k.055654": {"pos": "phrase", "ipa": "", "vi": "nhà vật lý Andrei Sakharov"},
    "lex.en.200k.055655": {"pos": "phrase", "ipa": "", "vi": "cầu treo Angostura ở Venezuela"},
    "lex.en.200k.055656": {"pos": "phrase", "ipa": "", "vi": "thuốc chống co giật"},
    "lex.en.200k.055657": {"pos": "phrase", "ipa": "", "vi": "giáo hội phái Arminius"},
    "lex.en.200k.055658": {"pos": "phrase", "ipa": "", "vi": "cây cúc hoàng anh lá rộng"},
    "lex.en.200k.055659": {"pos": "phrase", "ipa": "", "vi": "quả cây carob; quả minh đậu"},
    "lex.en.200k.055660": {"pos": "phrase", "ipa": "", "vi": "cây carob; cây minh đậu"},
    "lex.en.200k.055661": {"pos": "phrase", "ipa": "/ˌʃeɪz ˈlɔːŋ/", "vi": "ghế dài tựa thư giãn; ghế trường kỷ"},
    "lex.en.200k.055662": {"pos": "phrase", "ipa": "", "vi": "bán đảo Chukchi"},
    "lex.en.200k.055663": {"pos": "phrase", "ipa": "", "vi": "giày bốt ngắn chukka"},
    "lex.en.200k.055664": {"pos": "phrase", "ipa": "", "vi": "cây bưởi; quả bưởi"},
    "lex.en.200k.055665": {"pos": "phrase", "ipa": "/ˌkʌm iːl ˈfoʊ/", "vi": "đúng mực; hợp lẽ; lịch sự"},
    "lex.en.200k.055666": {"pos": "phrase", "ipa": "", "vi": "rượu vang Côtes de Provence"},
    "lex.en.200k.055667": {"pos": "phrase", "ipa": "", "vi": "ống tia âm cực Crookes"},
    "lex.en.200k.055668": {"pos": "phrase", "ipa": "", "vi": "bệnh leishmania ngoài da"},
    "lex.en.200k.055669": {"pos": "phrase", "ipa": "", "vi": "phương pháp sắc; quá trình sắc"},
    "lex.en.200k.055670": {"pos": "phrase", "ipa": "", "vi": "lồi củ cơ delta xương cánh tay"},
    "lex.en.200k.055671": {"pos": "phrase", "ipa": "", "vi": "xương ngón chân ngựa; xương pastern"},
    "lex.en.200k.055672": {"pos": "phrase", "ipa": "", "vi": "bụi cây fetterbush hoa trắng"},
    "lex.en.200k.055673": {"pos": "phrase", "ipa": "", "vi": "dương xỉ màng mỏng"},
    "lex.en.200k.055674": {"pos": "phrase", "ipa": "", "vi": "thống chế Archibald Wavell"},
    "lex.en.200k.055675": {"pos": "phrase", "ipa": "", "vi": "nhà văn François Rabelais"},
    "lex.en.200k.055676": {"pos": "phrase", "ipa": "", "vi": "kháng thể gamma globulin"},
    "lex.en.200k.055677": {"pos": "phrase", "ipa": "", "vi": "chi cây hoa giấy"},
    "lex.en.200k.055678": {"pos": "phrase", "ipa": "", "vi": "chi mèo nhỏ felis"},
    "lex.en.200k.055679": {"pos": "phrase", "ipa": "", "vi": "chi cây mộc tê reseda"},
    "lex.en.200k.055680": {"pos": "phrase", "ipa": "", "vi": "nguyên soái Georgy Zhukov"},
    "lex.en.200k.055681": {"pos": "phrase", "ipa": "", "vi": "cơ mông lớn"},
    "lex.en.200k.055682": {"pos": "phrase", "ipa": "", "vi": "kinh thánh Granth Sahib đạo Sikh"},
    "lex.en.200k.055683": {"pos": "phrase", "ipa": "", "vi": "phân tích theo khối lượng"},
    "lex.en.200k.055684": {"pos": "phrase", "ipa": "", "vi": "thành cổ Hippo Regius ở Algérie"},
    "lex.en.200k.055685": {"pos": "phrase", "ipa": "", "vi": "gamma globulin ở người"},
    "lex.en.200k.055686": {"pos": "phrase", "ipa": "", "vi": "nhà chế tạo máy bay Igor Sikorsky"},
    "lex.en.200k.055687": {"pos": "phrase", "ipa": "", "vi": "nhà văn Ilya Ehrenburg"},
    "lex.en.200k.055688": {"pos": "phrase", "ipa": "", "vi": "kháng thể huyết thanh miễn dịch"},
    "lex.en.200k.055689": {"pos": "phrase", "ipa": "", "vi": "đại văn hào Nga Ivan Turgenev"},
    "lex.en.200k.055690": {"pos": "phrase", "ipa": "", "vi": "nhà văn Anh Lytton Strachey"},
    "lex.en.200k.055691": {"pos": "phrase", "ipa": "", "vi": "hội chứng kém hấp thu đường ruột"},
    "lex.en.200k.055692": {"pos": "phrase", "ipa": "", "vi": "đồng rupee Mauritius"},
    "lex.en.200k.055693": {"pos": "phrase", "ipa": "", "vi": "eo biển Menai ở xứ Wales"},
    "lex.en.200k.055694": {"pos": "phrase", "ipa": "", "vi": "nữ thần trí tuệ Pallas Athena"},
    "lex.en.200k.055695": {"pos": "phrase", "ipa": "", "vi": "nhà thơ Pháp Paul Verlaine"},
    "lex.en.200k.055696": {"pos": "phrase", "ipa": "", "vi": "danh ca opera Plácido Domingo"},
    "lex.en.200k.055697": {"pos": "phrase", "ipa": "", "vi": "thùng chìm khí nén thi công móng"},
    "lex.en.200k.055698": {"pos": "phrase", "ipa": "", "vi": "đâm va hỏng xe; làm tai nạn"},
    "lex.en.200k.055699": {"pos": "phrase", "ipa": "", "vi": "tướng quân Publius Cornelius Scipio"},
    "lex.en.200k.055700": {"pos": "phrase", "ipa": "", "vi": "sợi Purkinje dẫn truyền xung tim"},
    "lex.en.200k.055701": {"pos": "phrase", "ipa": "", "vi": "góc tái nhập; góc chĩa vào trong"}
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

with open('scratch/b32_r02_p2.json', 'w', encoding='utf-8') as f:
    json.dump(output_items, f, ensure_ascii=False, indent=2)

print(f"Successfully authored and validated Part 2: {len(output_items)} items saved to scratch/b32_r02_p2.json")
