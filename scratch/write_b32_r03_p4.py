import json

with open('scratch/b32_r03_raw_p4.json') as f:
    raw_items = json.load(f)

reviewed_data = {
    "lex.en.200k.056302": {"pos": "noun", "ipa": "/ˌɛntʃɪˈlɑːdəz/", "vi": "món bánh cuộn nướng enchilada"},
    "lex.en.200k.056303": {"pos": "noun", "ipa": "/ˌiːkwɪˈlætərəlz/", "vi": "hình tam giác đều; hình đều"},
    "lex.en.200k.056304": {"pos": "noun", "ipa": "/ˌɛksjuːˈmeɪʃənz/", "vi": "sự khai quật tử thi mồ mả"},
    "lex.en.200k.056305": {"pos": "noun", "ipa": "/ˈfiːdlərz/", "vi": "nhạc trưởng Arthur Fiedler"},
    "lex.en.200k.056306": {"pos": "noun", "ipa": "/floʊˈbɛərz/", "vi": "nhà văn Pháp Gustave Flaubert"},
    "lex.en.200k.056307": {"pos": "noun", "ipa": "/ˈflaɪkætʃərz/", "vi": "loài chim đớp ruồi bắt mồi"},
    "lex.en.200k.056308": {"pos": "noun", "ipa": "/ˈfrʌntɪspiːsɪz/", "vi": "trang tranh đầu sách; mặt chính"},
    "lex.en.200k.056309": {"pos": "noun", "ipa": "/ˌdʒiːniˈælədʒɪsts/", "vi": "nhà nghiên cứu gia phả dòng họ"},
    "lex.en.200k.056310": {"pos": "noun", "ipa": "/ˈɡrændædiz/", "vi": "ông nội; ông ngoại; cụ tổ"},
    "lex.en.200k.056311": {"pos": "adj", "ipa": "/ˈɡrʌndʒiər/", "vi": "nhếch nhác hơn; bẩn thỉu luộm thuộm"},
    "lex.en.200k.056312": {"pos": "adj", "ipa": "/ˈɡrʌndʒiɪst/", "vi": "nhếch nhác nhất; luộm thuộm nhất"},
    "lex.en.200k.056313": {"pos": "noun", "ipa": "/ˈɡʌnsmɪθs/", "vi": "thợ chế tạo và sửa chữa súng"},
    "lex.en.200k.056314": {"pos": "noun", "ipa": "/ˈhɛərbbrʌʃɪz/", "vi": "bàn chải tóc; bàn chải chải đầu"},
    "lex.en.200k.056315": {"pos": "noun", "ipa": "/ˈhændreɪlz/", "vi": "tay vịn lan can cầu thang"},
    "lex.en.200k.056316": {"pos": "noun", "ipa": "/ˌhɪspænˈjoʊləz/", "vi": "đảo Hispaniola ở vùng Caribe"},
    "lex.en.200k.056317": {"pos": "noun", "ipa": "/ˌɪntəˈrɑːɡətɪvz/", "vi": "từ nghi vấn; đại từ nghi vấn"},
    "lex.en.200k.056318": {"pos": "noun", "ipa": "/kəˈzuːz/", "vi": "kèn kèn môi kazoo đồ chơi"},
    "lex.en.200k.056319": {"pos": "noun", "ipa": "/ˈkɛtʃɪz/", "vi": "thuyền buồm ketch hai cột buồm"},
    "lex.en.200k.056320": {"pos": "noun", "ipa": "/ˈnɑːkərz/", "vi": "tay gõ cửa; kẻ hay chê bai"},
    "lex.en.200k.056321": {"pos": "noun", "ipa": "/ˌɛlˌdʒiːˈbiːz/", "vi": "bom lượn thông minh dẫn bằng laser"},
    "lex.en.200k.056322": {"pos": "noun", "ipa": "/ˈlaɪnətaɪps/", "vi": "máy đúc chữ in xếp dòng Linotype"},
    "lex.en.200k.056323": {"pos": "noun", "ipa": "/ˌɛlˌpiːˈɛnz/", "vi": "y tá thực hành có chứng chỉ LPN"},
    "lex.en.200k.056324": {"pos": "noun", "ipa": "/ˈlʌtjənzɪz/", "vi": "kiến trúc sư Edwin Lutyens"},
    "lex.en.200k.056325": {"pos": "noun", "ipa": "/mæˈsɜːrz/", "vi": "nam nhân viên xoa bóp bấm huyệt"},
    "lex.en.200k.056326": {"pos": "noun", "ipa": "/ˈmɪdræʃɪz/", "vi": "bình giải kinh Midrash Do Thái"},
    "lex.en.200k.056327": {"pos": "noun", "ipa": "/mɪdrɑːˈʃiːm/", "vi": "các sách chú giải Midrash Do Thái"},
    "lex.en.200k.056328": {"pos": "noun", "ipa": "/ˈmɑːnædz/", "vi": "đơn vị đơn tử; phần tử đơn nhất"},
    "lex.en.200k.056329": {"pos": "noun", "ipa": "/ˈmuːləz/", "vi": "tiền nong; đống tiền mặt lóng"},
    "lex.en.200k.056330": {"pos": "noun", "ipa": "/ˈnuːzpeɪpərmən/", "vi": "các nhà báo; phóng viên tòa soạn"},
    "lex.en.200k.056331": {"pos": "noun", "ipa": "/iːˈsɑːfəɡəsɪz/", "vi": "ống thực quản đường tiêu hóa"},
    "lex.en.200k.056332": {"pos": "noun", "ipa": "/ˈɑːmɪkrɑːnz/", "vi": "chữ cái Hy Lạp omicron; biến thể"},
    "lex.en.200k.056333": {"pos": "noun", "ipa": "/ˈɔːrbɪsənz/", "vi": "danh ca rock Roy Orbison"},
    "lex.en.200k.056334": {"pos": "noun", "ipa": "/ˈɔːrioʊlz/", "vi": "loài chim hoàng anh vàng óng"},
    "lex.en.200k.056335": {"pos": "verb", "ipa": "/ˈfæntəsaɪzd/", "vi": "đã mơ tưởng viển vông; ảo tưởng"},
    "lex.en.200k.056336": {"pos": "noun", "ipa": "/ˈpleɪpɛnz/", "vi": "cũi quây cho trẻ em tập chơi"},
    "lex.en.200k.056337": {"pos": "noun", "ipa": "/ˈpɑːləksɪz/", "vi": "ngôi sao Pollux trong chòm Song Tử"},
    "lex.en.200k.056338": {"pos": "noun", "ipa": "/ˈpuːləz/", "vi": "đồng tiền pula của Botswana"},
    "lex.en.200k.056339": {"pos": "noun", "ipa": "/ˈpʊtʃɪz/", "vi": "cuộc đảo chính quân sự chớp nhoáng"},
    "lex.en.200k.056340": {"pos": "noun", "ipa": "/ˌkwɑːdrəˈpliːdʒɪks/", "vi": "người bị liệt tứ chi bại liệt"},
    "lex.en.200k.056341": {"pos": "noun", "ipa": "/kwɪnˈtɛsnsɪz/", "vi": "tinh hoa cốt lõi; ví dụ tinh túy"},
    "lex.en.200k.056342": {"pos": "verb", "ipa": "/riːˈdɛkəreɪtɪd/", "vi": "đã trang hoàng lại; sơn sửa lại"},
    "lex.en.200k.056343": {"pos": "verb", "ipa": "/riːˈdɛkəreɪts/", "vi": "trang hoàng lại; đổi mới nội thất"},
    "lex.en.200k.056344": {"pos": "verb", "ipa": "/riːˈdɛkəreɪtɪŋ/", "vi": "trang trí lại; sửa sang nội thất"},
    "lex.en.200k.056345": {"pos": "verb", "ipa": "/ˌriːdɪˈplɔɪd/", "vi": "đã tái bố trí; điều chuyển vị trí"},
    "lex.en.200k.056346": {"pos": "verb", "ipa": "/ˌriːdɪˈplɔɪɪŋ/", "vi": "tái bố trí nhân lực; điều động"},
    "lex.en.200k.056347": {"pos": "verb", "ipa": "/ˌriːdɪˈplɔɪz/", "vi": "tái bố trí; điều chuyển nguồn lực"},
    "lex.en.200k.056348": {"pos": "noun", "ipa": "/ˈrɛtroʊvaɪrəsɪz/", "vi": "chủng vi-rút sao chép ngược RNA"},
    "lex.en.200k.056349": {"pos": "noun", "ipa": "/ˈrɪŋlɪŋz/", "vi": "gánh xiếc anh em nhà Ringling"},
    "lex.en.200k.056350": {"pos": "noun", "ipa": "/ruːˈpiːəz/", "vi": "đồng tiền rupiah của Indonesia"},
    "lex.en.200k.056351": {"pos": "noun", "ipa": "/ˈsɔːtuːθs/", "vi": "răng cưa nhọn; dạng sóng răng cưa"},
    "lex.en.200k.056352": {"pos": "verb", "ipa": "/skræmd/", "vi": "đã chuồn biến mất; đã tẩu thoát"},
    "lex.en.200k.056353": {"pos": "verb", "ipa": "/ˈskræmɪŋ/", "vi": "chuồn đi mau lẹ; tẩu thoát lẹ"},
    "lex.en.200k.056354": {"pos": "verb", "ipa": "/skræmz/", "vi": "chuồn biến; cút đi thật nhanh"},
    "lex.en.200k.056355": {"pos": "noun", "ipa": "/ˈseɪɑːnsɪz/", "vi": "buổi cầu hồn đồng cốt gọi hồn"},
    "lex.en.200k.056356": {"pos": "noun", "ipa": "/ˈsiːskeɪps/", "vi": "tranh vẽ phong cảnh biển khơi"},
    "lex.en.200k.056357": {"pos": "noun", "ipa": "/səˈbæstəpɑːlz/", "vi": "thành phố cảng Sevastopol"},
    "lex.en.200k.056358": {"pos": "noun", "ipa": "/sɪˈdjuːsərz/", "vi": "kẻ dụ dỗ quyến rũ; kẻ cám dỗ"},
    "lex.en.200k.056359": {"pos": "noun", "ipa": "/ˈʃeɪməsɪz/", "vi": "thám tử tư theo dõi lén"},
    "lex.en.200k.056360": {"pos": "noun", "ipa": "/ˈʃuːleɪsɪz/", "vi": "dây buộc giày da thể thao"},
    "lex.en.200k.056361": {"pos": "verb", "ipa": "/ˈslætɪŋ/", "vi": "đóng then nan gỗ; vỗ phần phật"},
    "lex.en.200k.056362": {"pos": "noun", "ipa": "/ˈsnætʃərz/", "vi": "tên giật đồ; kẻ bắt cóc giật dây"},
    "lex.en.200k.056363": {"pos": "noun", "ipa": "/ˈsɔːftiz/", "vi": "người đa cảm yếu lòng; kẻ mềm lòng"},
    "lex.en.200k.056364": {"pos": "noun", "ipa": "/suːks/", "vi": "khu chợ truyền thống Ả Rập souk"},
    "lex.en.200k.056365": {"pos": "noun", "ipa": "/ˈstækərz/", "vi": "máy bốc dỡ xếp chồng; xe nâng hàng"},
    "lex.en.200k.056366": {"pos": "noun", "ipa": "/ˈstɪltənz/", "vi": "phô mai xanh béo ngậy Stilton"},
    "lex.en.200k.056367": {"pos": "noun", "ipa": "/ˈstɑːpərdz/", "vi": "nhà viết kịch Tom Stoppard"},
    "lex.en.200k.056368": {"pos": "noun", "ipa": "/ˈstɔːrkiːpərz/", "vi": "chủ tiệm bán lẻ; người thủ kho"},
    "lex.en.200k.056369": {"pos": "noun", "ipa": "/ˈstriːtlaɪts/", "vi": "đèn chiếu sáng đường phố ban đêm"},
    "lex.en.200k.056370": {"pos": "noun", "ipa": "/ˈstrɪksɪz/", "vi": "chi chim cú vọ không tai Strix"},
    "lex.en.200k.056371": {"pos": "noun", "ipa": "/səbˈmærɪnərz/", "vi": "thủy thủ đoàn tàu ngầm quân sự"},
    "lex.en.200k.056372": {"pos": "noun", "ipa": "/ˈsʌnfɪʃɪz/", "vi": "loài cá mặt trăng khổng lồ biển"},
    "lex.en.200k.056373": {"pos": "noun", "ipa": "/ˈsuːpərhaɪweɪz/", "vi": "đại lộ cao tốc nhiều làn xe"},
    "lex.en.200k.056374": {"pos": "noun", "ipa": "/ˈtiːtaɪmz/", "vi": "giờ tiệc trà chiều thư thả"},
    "lex.en.200k.056375": {"pos": "noun", "ipa": "/taɪˌkɑːndəˈroʊɡəz/", "vi": "pháo đài lịch sử Ticonderoga"},
    "lex.en.200k.056376": {"pos": "noun", "ipa": "/ˈtɑːnsəlz/", "vi": "hạch vòm họng a-mi-đan"},
    "lex.en.200k.056377": {"pos": "noun", "ipa": "/ˈtʌtʃlaɪnz/", "vi": "đường biên dọc sân bóng đá"},
    "lex.en.200k.056378": {"pos": "noun", "ipa": "/ˈtrænsɛpts/", "vi": "gian cánh ngang giáo đường thánh"},
    "lex.en.200k.056379": {"pos": "noun", "ipa": "/ˈtrɛsɪz/", "vi": "lọn tóc bồng bềnh; món tóc dài"},
    "lex.en.200k.056380": {"pos": "noun", "ipa": "/ˈtrɪlbiz/", "vi": "chiếc mũ phớt vành hẹp trilby"},
    "lex.en.200k.056381": {"pos": "verb", "ipa": "/ˌʌndərˈvæljuːd/", "vi": "đã đánh giá thấp; coi nhẹ giá trị"},
    "lex.en.200k.056382": {"pos": "verb", "ipa": "/ˌʌndərˈvæljuːz/", "vi": "đánh giá thấp hơn giá trị thực"},
    "lex.en.200k.056383": {"pos": "verb", "ipa": "/ˌʌndərˈvæljuːɪŋ/", "vi": "coi thường giá trị; đánh giá thấp"},
    "lex.en.200k.056384": {"pos": "verb", "ipa": "/ˌʌpˈsteɪdʒd/", "vi": "đã lấn át chiếm trọn sân khấu"},
    "lex.en.200k.056385": {"pos": "verb", "ipa": "/ˌʌpˈsteɪdʒɪz/", "vi": "lấn át làm lu mờ; chiếm nổi bật"},
    "lex.en.200k.056386": {"pos": "verb", "ipa": "/ˌʌpˈsteɪdʒɪŋ/", "vi": "lấn át làm lu mờ vai diễn khác"},
    "lex.en.200k.056387": {"pos": "noun", "ipa": "/ˈvaɪəleɪtərz/", "vi": "người vi phạm luật lệ giao thông"},
    "lex.en.200k.056388": {"pos": "noun", "ipa": "/weɪfs/", "vi": "đứa trẻ bơ vơ không nơi nương tựa"},
    "lex.en.200k.056389": {"pos": "noun", "ipa": "/ˈwɔːrpæθs/", "vi": "con đường chinh chiến xuất quân"},
    "lex.en.200k.056390": {"pos": "noun", "ipa": "/ˈwɔːtərkɔːrsɪz/", "vi": "dòng chảy tự nhiên; lòng kênh rạch"},
    "lex.en.200k.056391": {"pos": "noun", "ipa": "/ˈwʊlwərθs/", "vi": "chuỗi cửa hàng bách hóa Woolworth"},
    "lex.en.200k.056392": {"pos": "noun", "ipa": "/ˈjɛloʊnaɪfs/", "vi": "thành phố Yellowknife ở Canada"},
    "lex.en.200k.056393": {"pos": "noun", "ipa": "/ˈzaɪɡoʊts/", "vi": "tế bào hợp tử sau thụ tinh"},
    "lex.en.200k.056394": {"pos": "phrase", "ipa": "", "vi": "nhà thơ học giả A. E. Housman"},
    "lex.en.200k.056395": {"pos": "phrase", "ipa": "", "vi": "đường ống tiêu hóa của cơ thể"},
    "lex.en.200k.056396": {"pos": "phrase", "ipa": "", "vi": "cây dược liệu thục quỳ trắng"},
    "lex.en.200k.056397": {"pos": "phrase", "ipa": "", "vi": "cây râm bụt thủy lạp Amur"},
    "lex.en.200k.056398": {"pos": "phrase", "ipa": "", "vi": "giáo phái Kháng cách Tái báp-têm"},
    "lex.en.200k.056399": {"pos": "phrase", "ipa": "", "vi": "kiến trúc sư Andrea Palladio"},
    "lex.en.200k.056400": {"pos": "phrase", "ipa": "", "vi": "tộc trưởng thời tiền Đại hồng thủy"},
    "lex.en.200k.056401": {"pos": "phrase", "ipa": "", "vi": "đại văn hào Nga Anton Chekhov"}
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

with open('scratch/b32_r03_p4.json', 'w', encoding='utf-8') as f:
    json.dump(output_items, f, ensure_ascii=False, indent=2)

print(f"Successfully authored and validated Part 4: {len(output_items)} items saved to scratch/b32_r03_p4.json")
