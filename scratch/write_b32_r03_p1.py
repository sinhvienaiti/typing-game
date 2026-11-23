import json

with open('scratch/b32_r03_raw_p1.json') as f:
    raw_items = json.load(f)

reviewed_data = {
    "lex.en.200k.056002": {"pos": "noun", "ipa": "/ˈsʌlfaɪdz/", "vi": "hợp chất muối sunfua"},
    "lex.en.200k.056003": {"pos": "noun", "ipa": "/ˈtæskˌmæstərz/", "vi": "người đốc thúc; đốc công hà khắc"},
    "lex.en.200k.056004": {"pos": "noun", "ipa": "/tɪbz/", "vi": "ngày không bao giờ đến; tib"},
    "lex.en.200k.056005": {"pos": "verb", "ipa": "/ˈtaɪpˌkæstɪŋ/", "vi": "đóng khung vào một vai diễn"},
    "lex.en.200k.056006": {"pos": "verb", "ipa": "/ˈtaɪpˌkæsts/", "vi": "đóng khung vào một kiểu vai"},
    "lex.en.200k.056007": {"pos": "noun", "ipa": "/ˈjuːnəˌsaɪkəlz/", "vi": "xe đạp một bánh biểu diễn"},
    "lex.en.200k.056008": {"pos": "noun", "ipa": "/vælˈwɑːz/", "vi": "vương triều Valois nước Pháp"},
    "lex.en.200k.056009": {"pos": "noun", "ipa": "/vəˈzɑːriz/", "vi": "danh họa Giorgio Vasari"},
    "lex.en.200k.056010": {"pos": "noun", "ipa": "/vjɛnˈtjɑːnz/", "vi": "thủ đô Viêng Chăn của Lào"},
    "lex.en.200k.056011": {"pos": "noun", "ipa": "/ˈweɪˌfɛərərz/", "vi": "người bộ hành; khách lữ hành"},
    "lex.en.200k.056012": {"pos": "adj", "ipa": "/ˈwiːdiər/", "vi": "nhiều cỏ dại hơn; còi cọc hơn"},
    "lex.en.200k.056013": {"pos": "adj", "ipa": "/ˈwiːdiɪst/", "vi": "nhiều cỏ dại nhất; gầy gò nhất"},
    "lex.en.200k.056014": {"pos": "noun", "ipa": "/ˈwaɪlərz/", "vi": "đạo diễn điện ảnh William Wyler"},
    "lex.en.200k.056015": {"pos": "noun", "ipa": "/ˈzaɪləfoʊnz/", "vi": "đàn mộc cầm gõ thanh gỗ"},
    "lex.en.200k.056016": {"pos": "phrase", "ipa": "", "vi": "họ thực vật Ô rô Acanthaceae"},
    "lex.en.200k.056017": {"pos": "phrase", "ipa": "", "vi": "nhà văn Ý Alessandro Manzoni"},
    "lex.en.200k.056018": {"pos": "phrase", "ipa": "", "vi": "nhựa tổng hợp anlyl nhiệt rắn"},
    "lex.en.200k.056019": {"pos": "phrase", "ipa": "", "vi": "biên đạo múa Alvin Ailey"},
    "lex.en.200k.056020": {"pos": "phrase", "ipa": "", "vi": "danh họa Anthony van Dyck"},
    "lex.en.200k.056021": {"pos": "phrase", "ipa": "", "vi": "thuốc giải tỏa lo âu an thần"},
    "lex.en.200k.056022": {"pos": "phrase", "ipa": "", "vi": "loài cầy vằn cọ Bắc Bộ"},
    "lex.en.200k.056023": {"pos": "phrase", "ipa": "", "vi": "cư dân bang Massachusetts"},
    "lex.en.200k.056024": {"pos": "phrase", "ipa": "", "vi": "học giả Anh Benjamin Jowett"},
    "lex.en.200k.056025": {"pos": "phrase", "ipa": "", "vi": "vết thương để giải ngũ về quê"},
    "lex.en.200k.056026": {"pos": "phrase", "ipa": "", "vi": "cây hoàng cầm râu hoa xanh"},
    "lex.en.200k.056027": {"pos": "phrase", "ipa": "", "vi": "kiến trúc sư Buckminster Fuller"},
    "lex.en.200k.056028": {"pos": "phrase", "ipa": "", "vi": "quả mọng hắc mai dại"},
    "lex.en.200k.056029": {"pos": "phrase", "ipa": "", "vi": "họ thực vật hắc mai Rhamnaceae"},
    "lex.en.200k.056030": {"pos": "phrase", "ipa": "", "vi": "cây hắc mai dại California"},
    "lex.en.200k.056031": {"pos": "phrase", "ipa": "", "vi": "cây chè xanh thực vật"},
    "lex.en.200k.056032": {"pos": "phrase", "ipa": "", "vi": "cây hắc mai dại Carolina"},
    "lex.en.200k.056033": {"pos": "phrase", "ipa": "", "vi": "Hoàng hậu Catherine de' Medici"},
    "lex.en.200k.056034": {"pos": "phrase", "ipa": "", "vi": "nhà sáng lập Charles Harrod"},
    "lex.en.200k.056035": {"pos": "phrase", "ipa": "", "vi": "nữ thích khách Charlotte Corday"},
    "lex.en.200k.056036": {"pos": "phrase", "ipa": "", "vi": "dây viền sợi nhung chenille"},
    "lex.en.200k.056037": {"pos": "phrase", "ipa": "", "vi": "Công đồng tôn giáo Chalcedon"},
    "lex.en.200k.056038": {"pos": "phrase", "ipa": "", "vi": "bảng cắm cọc đếm điểm cribbage"},
    "lex.en.200k.056039": {"pos": "phrase", "ipa": "", "vi": "bộ dồn kênh truyền dữ liệu"},
    "lex.en.200k.056040": {"pos": "phrase", "ipa": "", "vi": "nhà vật lý Louis de Broglie"},
    "lex.en.200k.056041": {"pos": "phrase", "ipa": "", "vi": "lúa mì cứng durum làm mì ống"},
    "lex.en.200k.056042": {"pos": "phrase", "ipa": "", "vi": "phi công át chủ Eddie Rickenbacker"},
    "lex.en.200k.056043": {"pos": "phrase", "ipa": "", "vi": "nhà xã hội học Émile Durkheim"},
    "lex.en.200k.056044": {"pos": "phrase", "ipa": "", "vi": "thời gian lịch thiên văn ET"},
    "lex.en.200k.056045": {"pos": "phrase", "ipa": "", "vi": "cây hắc mai giả giả rhamnus"},
    "lex.en.200k.056046": {"pos": "phrase", "ipa": "", "vi": "đại văn hào Chateaubriand"},
    "lex.en.200k.056047": {"pos": "phrase", "ipa": "", "vi": "thang âm ngũ cung khuyết nốt"},
    "lex.en.200k.056048": {"pos": "phrase", "ipa": "", "vi": "người dân bang New Jersey"},
    "lex.en.200k.056049": {"pos": "phrase", "ipa": "", "vi": "chi muỗi vằn truyền bệnh Culex"},
    "lex.en.200k.056050": {"pos": "phrase", "ipa": "", "vi": "chi cây hoa anh thảo Cyclamen"},
    "lex.en.200k.056051": {"pos": "phrase", "ipa": "", "vi": "chi cây nhựa ruồi Ilex"},
    "lex.en.200k.056052": {"pos": "phrase", "ipa": "", "vi": "chi động vật họ cáo Vulpes"},
    "lex.en.200k.056053": {"pos": "phrase", "ipa": "", "vi": "Giáo hoàng Biển Đức XV Chiesa"},
    "lex.en.200k.056054": {"pos": "phrase", "ipa": "", "vi": "cây hoa lỗ bình xanh lớn"},
    "lex.en.200k.056055": {"pos": "phrase", "ipa": "", "vi": "tiếng Khách Gia; tiếng Hẹ"},
    "lex.en.200k.056056": {"pos": "phrase", "ipa": "", "vi": "động vật có móng guốc"},
    "lex.en.200k.056057": {"pos": "phrase", "ipa": "", "vi": "bán đảo Đông Dương"},
    "lex.en.200k.056058": {"pos": "phrase", "ipa": "", "vi": "kỹ thuật in khắc lõm bề mặt"},
    "lex.en.200k.056059": {"pos": "phrase", "ipa": "", "vi": "cô thiếu nữ mới lớn; thiếu nữ"},
    "lex.en.200k.056060": {"pos": "phrase", "ipa": "", "vi": "nhà văn Mỹ John P. Marquand"},
    "lex.en.200k.056061": {"pos": "phrase", "ipa": "", "vi": "nhà văn Mỹ John Philip Marquand"},
    "lex.en.200k.056062": {"pos": "phrase", "ipa": "", "vi": "tổng thống Zambia Kenneth Kaunda"},
    "lex.en.200k.056063": {"pos": "phrase", "ipa": "", "vi": "tổng thống Kenneth Kaunda"},
    "lex.en.200k.056064": {"pos": "phrase", "ipa": "", "vi": "hỗn hợp cấu trúc phiến mỏng"},
    "lex.en.200k.056065": {"pos": "phrase", "ipa": "", "vi": "họ cây hoa lỗ bình chuông"},
    "lex.en.200k.056066": {"pos": "phrase", "ipa": "", "vi": "cây thông vỏ xoắn lodgepole"},
    "lex.en.200k.056067": {"pos": "phrase", "ipa": "", "vi": "chứng suy sinh dục ở nam giới"},
    "lex.en.200k.056068": {"pos": "phrase", "ipa": "", "vi": "triết gia Hầu tước Condorcet"},
    "lex.en.200k.056069": {"pos": "phrase", "ipa": "", "vi": "loài cá chuồn hai cánh bay"},
    "lex.en.200k.056070": {"pos": "phrase", "ipa": "", "vi": "cây xuân đào; cây đào trơn láng"},
    "lex.en.200k.056071": {"pos": "phrase", "ipa": "", "vi": "chứng trào ngược dạ dày thực quản"},
    "lex.en.200k.056072": {"pos": "phrase", "ipa": "", "vi": "thác nước Paulo Afonso ở Brazil"},
    "lex.en.200k.056073": {"pos": "phrase", "ipa": "", "vi": "thác nước Paulo Afonso ở Brazil"},
    "lex.en.200k.056074": {"pos": "phrase", "ipa": "", "vi": "nghệ nhân kim hoàn Fabergé"},
    "lex.en.200k.056075": {"pos": "phrase", "ipa": "", "vi": "cây hoa kế có mào lông tơ"},
    "lex.en.200k.056076": {"pos": "phrase", "ipa": "", "vi": "bệnh viêm khớp vảy nến"},
    "lex.en.200k.056077": {"pos": "phrase", "ipa": "", "vi": "cây cọ sợi raffia châu Phi"},
    "lex.en.200k.056078": {"pos": "phrase", "ipa": "", "vi": "nhà sáng chế Buckminster Fuller"},
    "lex.en.200k.056079": {"pos": "phrase", "ipa": "", "vi": "con sông Acheron thần thoại"},
    "lex.en.200k.056080": {"pos": "phrase", "ipa": "", "vi": "nấm cựa gà ký sinh trên lúa mạch"},
    "lex.en.200k.056081": {"pos": "phrase", "ipa": "", "vi": "tế bào thần kinh đệm Schwann"},
    "lex.en.200k.056082": {"pos": "phrase", "ipa": "", "vi": "danh họa Sir Anthony van Dyck"},
    "lex.en.200k.056083": {"pos": "phrase", "ipa": "", "vi": "cây cao lương ngũ cốc"},
    "lex.en.200k.056084": {"pos": "phrase", "ipa": "", "vi": "cây hắc mai dại miền nam Mỹ"},
    "lex.en.200k.056085": {"pos": "phrase", "ipa": "", "vi": "hoa hồi; quả đại hồi thơm cay"},
    "lex.en.200k.056086": {"pos": "phrase", "ipa": "", "vi": "món dồi ruột bò nhồi kishke"},
    "lex.en.200k.056087": {"pos": "phrase", "ipa": "", "vi": "động mạch dưới xương đòn"},
    "lex.en.200k.056088": {"pos": "phrase", "ipa": "", "vi": "tĩnh mạch dưới xương đòn"},
    "lex.en.200k.056089": {"pos": "phrase", "ipa": "", "vi": "tuyến nước bọt dưới lưỡi"},
    "lex.en.200k.056090": {"pos": "phrase", "ipa": "", "vi": "cây cúc dại lá cúc ngải"},
    "lex.en.200k.056091": {"pos": "phrase", "ipa": "", "vi": "chòm râu quai nón nhọn Van Dyck"},
    "lex.en.200k.056092": {"pos": "phrase", "ipa": "", "vi": "màu nâu ấm Van Dyck"},
    "lex.en.200k.056093": {"pos": "phrase", "ipa": "", "vi": "lãnh tụ Vladimir Ilyich Lenin"},
    "lex.en.200k.056094": {"pos": "phrase", "ipa": "", "vi": "ruồi trâu ký sinh da trâu bò"},
    "lex.en.200k.056095": {"pos": "phrase", "ipa": "", "vi": "cây hoa lỗ bình thủy sinh"},
    "lex.en.200k.056096": {"pos": "phrase", "ipa": "", "vi": "máy bay chở khách thân rộng"},
    "lex.en.200k.056097": {"pos": "phrase", "ipa": "", "vi": "đồng tiền dinar của Nam Tư"},
    "lex.en.200k.056098": {"pos": "phrase", "ipa": "", "vi": "cung tiếp gò má giải phẫu"},
    "lex.en.200k.056099": {"pos": "phrase", "ipa": "", "vi": "xương gò má mặt"},
    "lex.en.200k.056100": {"pos": "phrase", "ipa": "", "vi": "mỏm tiếp xương gò má"},
    "lex.en.200k.056101": {"pos": "verb", "ipa": "/əˈbaɪd/", "vi": "đã chuộc tội; đã đền tội"}
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

with open('scratch/b32_r03_p1.json', 'w', encoding='utf-8') as f:
    json.dump(output_items, f, ensure_ascii=False, indent=2)

print(f"Successfully authored and validated Part 1: {len(output_items)} items saved to scratch/b32_r03_p1.json")
