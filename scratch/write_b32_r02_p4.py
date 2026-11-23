import json

with open('scratch/b32_r02_raw_p4.json') as f:
    raw_items = json.load(f)

reviewed_data = {
    "lex.en.200k.055802": {"pos": "noun", "ipa": "/rɪˈtrɛntʃmənts/", "vi": "sự cắt giảm chi tiêu; hào lũy thủ"},
    "lex.en.200k.055803": {"pos": "noun", "ipa": "/ˈreɪnɑːrdz/", "vi": "con cáo già ranh mãnh Reynard"},
    "lex.en.200k.055804": {"pos": "noun", "ipa": "/rɪsks/", "vi": "vi xử lý tập lệnh rút gọn RISC"},
    "lex.en.200k.055805": {"pos": "noun", "ipa": "/ˈrɑːθkoʊz/", "vi": "danh họa Mark Rothko"},
    "lex.en.200k.055806": {"pos": "noun", "ipa": "/ˈroʊboʊts/", "vi": "thuyền chèo bằng tay"},
    "lex.en.200k.055807": {"pos": "noun", "ipa": "/ˈrʌndəlz/", "vi": "nấc thang; then ngang thang"},
    "lex.en.200k.055808": {"pos": "noun", "ipa": "/ˈsiːbɜːrdz/", "vi": "loài chim biển; loài hải âu"},
    "lex.en.200k.055809": {"pos": "noun", "ipa": "/ˈsaɪdəlz/", "vi": "cốc vại uống bia cỡ lớn"},
    "lex.en.200k.055810": {"pos": "noun", "ipa": "/ˈʃoʊpiːsɪz/", "vi": "tác phẩm tiêu biểu; vật trưng bày"},
    "lex.en.200k.055811": {"pos": "noun", "ipa": "/ˈʃoʊˌstɑːpərz/", "vi": "tiết mục đỉnh cao; điểm nghẽn lớn"},
    "lex.en.200k.055812": {"pos": "noun", "ipa": "/ˈsaɪdwɔːlz/", "vi": "thành lốp xe; vách tường bên hông"},
    "lex.en.200k.055813": {"pos": "verb", "ipa": "/ˈslɪŋkɪŋ/", "vi": "lén lút lẻn đi; trườn lách né tránh"},
    "lex.en.200k.055814": {"pos": "verb", "ipa": "/slɪŋks/", "vi": "lén lút lẻn đi; trườn nhẹ"},
    "lex.en.200k.055815": {"pos": "verb", "ipa": "/slʌŋk/", "vi": "đã lén lút lẻn đi; lủi đi"},
    "lex.en.200k.055816": {"pos": "noun", "ipa": "/sniːdz/", "vi": "tay gôn huyền thoại Sam Snead"},
    "lex.en.200k.055817": {"pos": "noun", "ipa": "/ˈsɑːntæɡz/", "vi": "nhà phê bình văn hóa Susan Sontag"},
    "lex.en.200k.055818": {"pos": "noun", "ipa": "/ˈteɪləsɪz/", "vi": "xương sên cổ chân; sườn dốc đá vụn"},
    "lex.en.200k.055819": {"pos": "noun", "ipa": "/tæmˈpiːkoʊz/", "vi": "thành phố cảng Tampico của Mexico"},
    "lex.en.200k.055820": {"pos": "noun", "ipa": "/ˈtiːləmɪərz/", "vi": "đoạn mút telomere nhiễm sắc thể"},
    "lex.en.200k.055821": {"pos": "noun", "ipa": "/ˈtɛsərækts/", "vi": "khối lập phương 4 chiều tesseract"},
    "lex.en.200k.055822": {"pos": "noun", "ipa": "/θoʊθs/", "vi": "thần trí tuệ Thoth Ai Cập"},
    "lex.en.200k.055823": {"pos": "noun", "ipa": "/ˈθɜːrbərz/", "vi": "nhà văn biếm họa James Thurber"},
    "lex.en.200k.055824": {"pos": "noun", "ipa": "/ˈtiːəmɑːts/", "vi": "nữ thần biển Tiamat xứ Babylon"},
    "lex.en.200k.055825": {"pos": "adj", "ipa": "/ˈtɪniər/", "vi": "chói tiếng kim loại hơn; mỏng hơn"},
    "lex.en.200k.055826": {"pos": "adj", "ipa": "/ˈtɪniɪst/", "vi": "chói tiếng kim loại nhất; mỏng nhất"},
    "lex.en.200k.055827": {"pos": "noun", "ipa": "/ˈtiːtiz/", "vi": "cây titi; khỉ đuôi sóc titi"},
    "lex.en.200k.055828": {"pos": "noun", "ipa": "/taɪˈtreɪʃənz/", "vi": "phép chuẩn độ dung dịch hóa học"},
    "lex.en.200k.055829": {"pos": "noun", "ipa": "/ˈtaʊnzɪz/", "vi": "nhà vật lý Charles Townes"},
    "lex.en.200k.055830": {"pos": "noun", "ipa": "/ˈtɜːrboʊprɑːps/", "vi": "động cơ phản lực cánh quạt tuabin"},
    "lex.en.200k.055831": {"pos": "noun", "ipa": "/ˈwækoʊz/", "vi": "kẻ lập dị; người gàn dở quái đản"},
    "lex.en.200k.055832": {"pos": "noun", "ipa": "/ˈwɑːʃklɔːθs/", "vi": "khăn mặt; khăn tắm nhỏ"},
    "lex.en.200k.055833": {"pos": "adj", "ipa": "/ˈwɛbiər/", "vi": "nhiều màng hơn; chằng chịt hơn"},
    "lex.en.200k.055834": {"pos": "adj", "ipa": "/ˈwɛbiɪst/", "vi": "nhiều màng nhất; chằng chịt nhất"},
    "lex.en.200k.055835": {"pos": "noun", "ipa": "/ˈwɛlsprɪŋz/", "vi": "nguồn suối; cội nguồn dồi dào"},
    "lex.en.200k.055836": {"pos": "phrase", "ipa": "", "vi": "phản kháng âm thanh"},
    "lex.en.200k.055837": {"pos": "phrase", "ipa": "", "vi": "rượu anlyl; cồn anlyl"},
    "lex.en.200k.055838": {"pos": "phrase", "ipa": "", "vi": "nhóm định chức anlyl"},
    "lex.en.200k.055839": {"pos": "phrase", "ipa": "", "vi": "gốc tự do anlyl"},
    "lex.en.200k.055840": {"pos": "phrase", "ipa": "", "vi": "tiêu xương ổ răng"},
    "lex.en.200k.055841": {"pos": "phrase", "ipa": "", "vi": "loài vạc rạ châu Mỹ"},
    "lex.en.200k.055842": {"pos": "phrase", "ipa": "", "vi": "đạo diễn phim Andrei Tarkovsky"},
    "lex.en.200k.055843": {"pos": "phrase", "ipa": "", "vi": "vỏ cây thảo dược angostura"},
    "lex.en.200k.055844": {"pos": "phrase", "ipa": "", "vi": "vượn người hình nhân"},
    "lex.en.200k.055845": {"pos": "phrase", "ipa": "", "vi": "nhà hóa học Antoine Lavoisier"},
    "lex.en.200k.055846": {"pos": "phrase", "ipa": "", "vi": "tín đồ phái Báp-tít Arminius"},
    "lex.en.200k.055847": {"pos": "phrase", "ipa": "", "vi": "cá đù Đại Tây Dương"},
    "lex.en.200k.055848": {"pos": "phrase", "ipa": "", "vi": "cá voi tấm sừng hàm"},
    "lex.en.200k.055849": {"pos": "phrase", "ipa": "", "vi": "xe ô tô gia đình station wagon"},
    "lex.en.200k.055850": {"pos": "phrase", "ipa": "", "vi": "nhà giáo dục Booker T. Washington"},
    "lex.en.200k.055851": {"pos": "phrase", "ipa": "", "vi": "cầu treo Bosphorus ở Istanbul"},
    "lex.en.200k.055852": {"pos": "phrase", "ipa": "", "vi": "chính khách La Mã Cassius Longinus"},
    "lex.en.200k.055853": {"pos": "phrase", "ipa": "", "vi": "nhà soạn nhạc Claude Debussy"},
    "lex.en.200k.055854": {"pos": "phrase", "ipa": "", "vi": "nhà soạn nhạc Claudio Monteverdi"},
    "lex.en.200k.055855": {"pos": "phrase", "ipa": "", "vi": "loài trăn siết mồi Boa"},
    "lex.en.200k.055856": {"pos": "phrase", "ipa": "", "vi": "nhà thần học Cornelis Jansen"},
    "lex.en.200k.055857": {"pos": "phrase", "ipa": "", "vi": "nhân vật Cyrano de Bergerac"},
    "lex.en.200k.055858": {"pos": "phrase", "ipa": "", "vi": "tật lác ngoài; lé kim phân kỳ"},
    "lex.en.200k.055859": {"pos": "phrase", "ipa": "", "vi": "loét hành tá tràng"},
    "lex.en.200k.055860": {"pos": "phrase", "ipa": "", "vi": "nhà thiết kế Elsa Schiaparelli"},
    "lex.en.200k.055861": {"pos": "phrase", "ipa": "", "vi": "loài chim vạc rạ Á Âu"},
    "lex.en.200k.055862": {"pos": "phrase", "ipa": "", "vi": "hạt cỏ cà ri lợi sữa"},
    "lex.en.200k.055863": {"pos": "phrase", "ipa": "", "vi": "họa sĩ thời Phục hưng Lippi"},
    "lex.en.200k.055864": {"pos": "phrase", "ipa": "", "vi": "thuốc kháng axit dạ dày"},
    "lex.en.200k.055865": {"pos": "phrase", "ipa": "", "vi": "Đức Phật Thích Ca Mâu Ni"},
    "lex.en.200k.055866": {"pos": "phrase", "ipa": "", "vi": "chi cây dâu dại arbutus"},
    "lex.en.200k.055867": {"pos": "phrase", "ipa": "", "vi": "chi cá tuyết nước ngọt lota"},
    "lex.en.200k.055868": {"pos": "phrase", "ipa": "", "vi": "nhà văn Anh Lytton Strachey"},
    "lex.en.200k.055869": {"pos": "phrase", "ipa": "", "vi": "axit amin glutamic"},
    "lex.en.200k.055870": {"pos": "phrase", "ipa": "", "vi": "kiệt sức vì nắng nóng; say nắng"},
    "lex.en.200k.055871": {"pos": "phrase", "ipa": "", "vi": "thị sai nhật tâm thiên văn"},
    "lex.en.200k.055872": {"pos": "phrase", "ipa": "", "vi": "đại văn hào Honoré de Balzac"},
    "lex.en.200k.055873": {"pos": "phrase", "ipa": "", "vi": "đại văn hào Honoré de Balzac"},
    "lex.en.200k.055874": {"pos": "phrase", "ipa": "", "vi": "vi-rút u nhú ở người; HPV"},
    "lex.en.200k.055875": {"pos": "phrase", "ipa": "", "vi": "kháng thể gamma globulin"},
    "lex.en.200k.055876": {"pos": "phrase", "ipa": "", "vi": "nhà văn nữ Joan Didion"},
    "lex.en.200k.055877": {"pos": "phrase", "ipa": "", "vi": "nhà thần học linh mục John Keble"},
    "lex.en.200k.055878": {"pos": "phrase", "ipa": "", "vi": "cây katsura Nhật Bản"},
    "lex.en.200k.055879": {"pos": "phrase", "ipa": "", "vi": "sự tiết nước mắt; nước mắt"},
    "lex.en.200k.055880": {"pos": "phrase", "ipa": "", "vi": "loài vạc lùn châu Mỹ"},
    "lex.en.200k.055881": {"pos": "phrase", "ipa": "", "vi": "nhà soạn nhạc Manuel de Falla"},
    "lex.en.200k.055882": {"pos": "phrase", "ipa": "", "vi": "đám rối thần kinh mạc treo"},
    "lex.en.200k.055883": {"pos": "phrase", "ipa": "", "vi": "đồng thau Muntz chống rỉ mạn tàu"},
    "lex.en.200k.055884": {"pos": "phrase", "ipa": "", "vi": "sa mạc ven biển Namib"},
    "lex.en.200k.055885": {"pos": "phrase", "ipa": "", "vi": "suy nhược hệ thần kinh"},
    "lex.en.200k.055886": {"pos": "phrase", "ipa": "", "vi": "người không theo tôn giáo nào"},
    "lex.en.200k.055887": {"pos": "phrase", "ipa": "", "vi": "cây bách vàng Nootka"},
    "lex.en.200k.055888": {"pos": "phrase", "ipa": "", "vi": "cây vân sam đỏ Bắc Mỹ"},
    "lex.en.200k.055889": {"pos": "phrase", "ipa": "", "vi": "cây mận đen Canada"},
    "lex.en.200k.055880": {"pos": "phrase", "ipa": "", "vi": "loài vạc lùn châu Mỹ"},
    "lex.en.200k.055890": {"pos": "phrase", "ipa": "", "vi": "phát triển tâm lý tính dục"},
    "lex.en.200k.055891": {"pos": "phrase", "ipa": "", "vi": "lực lượng vũ trang al-Qassam"},
    "lex.en.200k.055892": {"pos": "phrase", "ipa": "", "vi": "kính thiên văn khúc xạ thấu kính"},
    "lex.en.200k.055893": {"pos": "phrase", "ipa": "", "vi": "khối bát diện đều 8 mặt"},
    "lex.en.200k.055894": {"pos": "phrase", "ipa": "", "vi": "viêm cột sống dính khớp"},
    "lex.en.200k.055895": {"pos": "phrase", "ipa": "", "vi": "cây muồng trâu trị lác"},
    "lex.en.200k.055896": {"pos": "phrase", "ipa": "", "vi": "cá nục thuôn; cá nục sọc dưa"},
    "lex.en.200k.055897": {"pos": "phrase", "ipa": "", "vi": "cây xô thơm dược liệu"},
    "lex.en.200k.055898": {"pos": "phrase", "ipa": "", "vi": "cây muồng hòe; muồng lá hẹp"},
    "lex.en.200k.055899": {"pos": "phrase", "ipa": "", "vi": "xe ô tô du lịch năm cửa"},
    "lex.en.200k.055900": {"pos": "phrase", "ipa": "", "vi": "sông Tagus ở bán đảo Iberia"},
    "lex.en.200k.055901": {"pos": "phrase", "ipa": "", "vi": "Cộng hòa Togo ở Tây Phi"}
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

with open('scratch/b32_r02_p4.json', 'w', encoding='utf-8') as f:
    json.dump(output_items, f, ensure_ascii=False, indent=2)

print(f"Successfully authored and validated Part 4: {len(output_items)} items saved to scratch/b32_r02_p4.json")
