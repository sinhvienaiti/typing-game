import json

with open('scratch/b32_r03_raw_p2.json') as f:
    raw_items = json.load(f)

reviewed_data = {
    "lex.en.200k.056102": {"pos": "verb", "ipa": "/əˈbɔːt/", "vi": "đã đền tội; đã chuộc lỗi"},
    "lex.en.200k.056103": {"pos": "verb", "ipa": "/əˈbaɪɪŋ/", "vi": "chuộc lỗi; chịu phạt đền tội"},
    "lex.en.200k.056104": {"pos": "noun", "ipa": "/iːˈoʊliənz/", "vi": "người bộ tộc Aeolis thời Hy Lạp"},
    "lex.en.200k.056105": {"pos": "noun", "ipa": "/ˌæntiˈhɪstəmiːnz/", "vi": "thuốc kháng sinh histamine dị ứng"},
    "lex.en.200k.056106": {"pos": "noun", "ipa": "/ˌæpəˈloʊdʒiəz/", "vi": "bài tự biện; văn biện bạch"},
    "lex.en.200k.056107": {"pos": "verb", "ipa": "/ˈɑːrbɪtreɪtɪd/", "vi": "đã phân xử; đã làm trọng tài"},
    "lex.en.200k.056108": {"pos": "verb", "ipa": "/ˈɑːrbɪtreɪts/", "vi": "phân xử; làm trọng tài xét xử"},
    "lex.en.200k.056109": {"pos": "verb", "ipa": "/ˈɑːrbɪtreɪtɪŋ/", "vi": "đang phân xử; xét xử trọng tài"},
    "lex.en.200k.056110": {"pos": "noun", "ipa": "/ɑːrˈtɪfɪsərz/", "vi": "thợ thủ công khéo tay; nhà sáng chế"},
    "lex.en.200k.056111": {"pos": "noun", "ipa": "/ˈbæŋkhɛdz/", "vi": "nữ minh tinh Tallulah Bankhead"},
    "lex.en.200k.056112": {"pos": "noun", "ipa": "/ˈbiːnbæɡz/", "vi": "ghế lười hạt xốp; túi đậu ném"},
    "lex.en.200k.056113": {"pos": "noun", "ipa": "/ˈbɛkliz/", "vi": "thành phố Beckley ở West Virginia"},
    "lex.en.200k.056114": {"pos": "noun", "ipa": "/ˈbɛdsprɛdz/", "vi": "khăn trải giường; ga phủ giường"},
    "lex.en.200k.056115": {"pos": "noun", "ipa": "/ˈbaʊdɪtʃɪz/", "vi": "nhà hàng hải Nathaniel Bowditch"},
    "lex.en.200k.056116": {"pos": "noun", "ipa": "/ˈbrʊknərz/", "vi": "nhà soạn nhạc Anton Bruckner"},
    "lex.en.200k.056117": {"pos": "noun", "ipa": "/ˌkæbriəˈleɪz/", "vi": "xe mui trần; cỗ xe ngựa mui gấp"},
    "lex.en.200k.056118": {"pos": "noun", "ipa": "/ˌsɛntrəlaɪˈzeɪʃənz/", "vi": "sự tập trung hóa quyền lực"},
    "lex.en.200k.056119": {"pos": "noun", "ipa": "/ˈklɔːrɑːksɪz/", "vi": "thuốc tẩy Clorox; nước javen"},
    "lex.en.200k.056120": {"pos": "noun", "ipa": "/ˈkɑːkərəlz/", "vi": "gà trống tơ; gà trống choai"},
    "lex.en.200k.056121": {"pos": "adj", "ipa": "/ˈkʌmliər/", "vi": "duyên dáng hơn; dễ coi ưa nhìn hơn"},
    "lex.en.200k.056122": {"pos": "adj", "ipa": "/ˈkʌmliɪst/", "vi": "duyên dáng nhất; ưa nhìn nhất"},
    "lex.en.200k.056123": {"pos": "noun", "ipa": "/ˈkɑːməroʊzɪz/", "vi": "quần đảo Comoros ở Ấn Độ Dương"},
    "lex.en.200k.056124": {"pos": "noun", "ipa": "/ˈkuːliz/", "vi": "người phu khuân vác cu-li thời xưa"},
    "lex.en.200k.056125": {"pos": "noun", "ipa": "/ˈkɔːrpərətɪsts/", "vi": "người theo chủ nghĩa tập đoàn"},
    "lex.en.200k.056126": {"pos": "noun", "ipa": "/ˈkjuːvieɪz/", "vi": "nhà tự nhiên học Georges Cuvier"},
    "lex.en.200k.056127": {"pos": "noun", "ipa": "/ˈsaɪklətrɑːnz/", "vi": "máy gia tốc hạt cyclotron"},
    "lex.en.200k.056128": {"pos": "noun", "ipa": "/ˌdɛspəˈrɑːdoʊz/", "vi": "kẻ liều mạng; tên cướp táo tợn"},
    "lex.en.200k.056129": {"pos": "noun", "ipa": "/ˈdrʌmstɪks/", "vi": "dùi đánh trống; đùi gà rán"},
    "lex.en.200k.056130": {"pos": "noun", "ipa": "/ˈaɪzənstaɪnz/", "vi": "đạo diễn phim Sergei Eisenstein"},
    "lex.en.200k.056131": {"pos": "noun", "ipa": "/ˈɛksmɔːrz/", "vi": "giống ngựa Exmoor; vùng Exmoor"},
    "lex.en.200k.056132": {"pos": "noun", "ipa": "/ˈfleɪvərɪŋz/", "vi": "chất tạo hương liệu; gia vị thơm"},
    "lex.en.200k.056133": {"pos": "noun", "ipa": "/ˈfuːdstʌfs/", "vi": "lương thực thực phẩm thiết yếu"},
    "lex.en.200k.056134": {"pos": "noun", "ipa": "/ˈfruːtkeɪks/", "vi": "bánh nướng trái cây; kẻ dở hơi"},
    "lex.en.200k.056135": {"pos": "noun", "ipa": "/ˌɛfˌɛsˈeɪtʃɪz/", "vi": "hoóc-môn kích thích nang trứng FSH"},
    "lex.en.200k.056136": {"pos": "noun", "ipa": "/fjuˈrɔːriz/", "vi": "sự giận dữ kịch liệt; cơn xôn xao"},
    "lex.en.200k.056137": {"pos": "noun", "ipa": "/ɡɑːts/", "vi": "bậc thang bến sông ghat ở Ấn Độ"},
    "lex.en.200k.056138": {"pos": "noun", "ipa": "/ˈnɑːstəsɪzəmz/", "vi": "thuyết ngộ đạo trí năng tôn giáo"},
    "lex.en.200k.056139": {"pos": "noun", "ipa": "/ˈɡrɑːzniz/", "vi": "thành phố Grozny của Chechnya"},
    "lex.en.200k.056140": {"pos": "noun", "ipa": "/ˈhɛdrɛsts/", "vi": "gối tựa đầu ghế xe hơi"},
    "lex.en.200k.056141": {"pos": "noun", "ipa": "/ɪnˈdʌktərz/", "vi": "cuộn cảm ứng từ điện tử"},
    "lex.en.200k.056142": {"pos": "noun", "ipa": "/ˈɪŋərz/", "vi": "người dân tộc thiểu số Inger"},
    "lex.en.200k.056143": {"pos": "noun", "ipa": "/aɪˈoʊniəz/", "vi": "vùng cổ Ionia ở Hy Lạp cổ đại"},
    "lex.en.200k.056144": {"pos": "noun", "ipa": "/ˌaɪˌoʊˈpiːz/", "vi": "chỉ số nhãn áp của mắt"},
    "lex.en.200k.056145": {"pos": "noun", "ipa": "/dʒəˈlɑːləbædz/", "vi": "thành phố Jalalabad ở Afghanistan"},
    "lex.en.200k.056146": {"pos": "noun", "ipa": "/ˈkaɪliz/", "vi": "boomerang ném của thổ dân Úc"},
    "lex.en.200k.056147": {"pos": "noun", "ipa": "/kʊrsks/", "vi": "thành phố Kursk ở miền tây Nga"},
    "lex.en.200k.056148": {"pos": "noun", "ipa": "/ˈlɛzbɑːsɪz/", "vi": "hòn đảo Lesbos của Hy Lạp"},
    "lex.en.200k.056149": {"pos": "noun", "ipa": "/ˈlɪpskəmz/", "vi": "trường đại học Lipscomb"},
    "lex.en.200k.056150": {"pos": "noun", "ipa": "/ˈluːaʊz/", "vi": "bữa tiệc luau truyền thống Hawaii"},
    "lex.en.200k.056151": {"pos": "noun", "ipa": "/ˈmæŋɡoʊldz/", "vi": "củ dền thức ăn gia súc mangold"},
    "lex.en.200k.056152": {"pos": "noun", "ipa": "/ˌmæriˈænəsɪz/", "vi": "quần đảo Mariana ở Thái Bình Dương"},
    "lex.en.200k.056153": {"pos": "noun", "ipa": "/ˈmɑːrvəlz/", "vi": "nhà thơ Andrew Marvell"},
    "lex.en.200k.056154": {"pos": "noun", "ipa": "/ˈmɛŋkənz/", "vi": "nhà văn nhà báo H. L. Mencken"},
    "lex.en.200k.056155": {"pos": "noun", "ipa": "/ˈmɛθəliːnz/", "vi": "gốc hóa học metylen CH2"},
    "lex.en.200k.056156": {"pos": "noun", "ipa": "/ˌmɪnəˈrɛts/", "vi": "ngọn tháp giáo đường Hồi giáo"},
    "lex.en.200k.056157": {"pos": "noun", "ipa": "/ˈmɪntərz/", "vi": "thợ đúc tiền xu; người đúc tiền"},
    "lex.en.200k.056158": {"pos": "noun", "ipa": "/ˌmɪnjuˈɛts/", "vi": "điệu nhảy menuet cung đình cổ"},
    "lex.en.200k.056159": {"pos": "noun", "ipa": "/ˌmɪsədˈvɛntʃərz/", "vi": "chuyện rủi ro; tai bay vạ gió"},
    "lex.en.200k.056160": {"pos": "noun", "ipa": "/ˈmɪtʃəmz/", "vi": "diễn viên điện ảnh Robert Mitchum"},
    "lex.en.200k.056161": {"pos": "noun", "ipa": "/ˌmɑːnəˈlɪŋɡwəlz/", "vi": "người chỉ biết một ngôn ngữ"},
    "lex.en.200k.056162": {"pos": "noun", "ipa": "/məˈræsɪz/", "vi": "bãi lầy ngập nước; mớ bòng bong"},
    "lex.en.200k.056163": {"pos": "noun", "ipa": "/ˌmoʊzæmˈbiːkənz/", "vi": "người dân nước Mozambique"},
    "lex.en.200k.056164": {"pos": "noun", "ipa": "/ˈnænoʊˌsɛkəndz/", "vi": "khoảng một phần tỉ giây nano"},
    "lex.en.200k.056165": {"pos": "noun", "ipa": "/ˌnʊroʊsaɪˈkɑːlədʒiz/", "vi": "khoa tâm lý học thần kinh"},
    "lex.en.200k.056166": {"pos": "noun", "ipa": "/ˌɑːpəˈrɛtəz/", "vi": "vở kịch nhạc kịch hài operetta"},
    "lex.en.200k.056167": {"pos": "verb", "ipa": "/ˌoʊvərˈpeɪɪŋ/", "vi": "trả tiền thừa; trả giá quá đắt"},
    "lex.en.200k.056168": {"pos": "verb", "ipa": "/ˌoʊvərˈpeɪz/", "vi": "trả giá quá cao; chi trả quá đắt"},
    "lex.en.200k.056169": {"pos": "noun", "ipa": "/ˌpiːdəˈfɪliəz/", "vi": "hội chứng ấu dâm; bệnh ấu dâm"},
    "lex.en.200k.056170": {"pos": "noun", "ipa": "/ˈpæŋɡəlɪnz/", "vi": "con tê tê có vảy cứng bọc thân"},
    "lex.en.200k.056171": {"pos": "noun", "ipa": "/ˈpærəmʊərz/", "vi": "nhân tình lén lút; người tình"},
    "lex.en.200k.056172": {"pos": "noun", "ipa": "/ˈfiːbəsɪz/", "vi": "thần mặt trời Phoebus Apollo"},
    "lex.en.200k.056173": {"pos": "noun", "ipa": "/piˌænoʊˈfɔːrteɪz/", "vi": "đàn đại dương cầm pianoforte"},
    "lex.en.200k.056174": {"pos": "noun", "ipa": "/ˈpleɪnərz/", "vi": "máy bào gỗ; thợ bào gỗ mặt bàn"},
    "lex.en.200k.056175": {"pos": "noun", "ipa": "/ˈprɛsmən/", "vi": "thợ vận hành máy in; ký giả báo"},
    "lex.en.200k.056176": {"pos": "noun", "ipa": "/tʃjɑːŋz/", "vi": "người dân tộc Khương ở Tứ Xuyên"},
    "lex.en.200k.056177": {"pos": "noun", "ipa": "/kwaɪnz/", "vi": "triết gia W. V. Quine; mã quine"},
    "lex.en.200k.056178": {"pos": "verb", "ipa": "/ˈræʃənəlaɪzd/", "vi": "đã hợp lý hóa; tìm cách biện minh"},
    "lex.en.200k.056179": {"pos": "verb", "ipa": "/ˈræʃənəlaɪzɪz/", "vi": "hợp lý hóa; tìm cớ ngụy biện"},
    "lex.en.200k.056180": {"pos": "verb", "ipa": "/ˈræʃənəlaɪzɪŋ/", "vi": "hợp lý hóa tổ chức; ngụy biện"},
    "lex.en.200k.056181": {"pos": "noun", "ipa": "/ˈreɪzərbæks/", "vi": "lợn rừng lưng nhọn razorback"},
    "lex.en.200k.056182": {"pos": "noun", "ipa": "/roʊˈzeɪʃiəz/", "vi": "bệnh đỏ mặt da rosacea"},
    "lex.en.200k.056183": {"pos": "noun", "ipa": "/ˈrʌfiənz/", "vi": "kẻ côn đồ hung ác; quân bất lương"},
    "lex.en.200k.056184": {"pos": "noun", "ipa": "/ˈrʌnjənz/", "vi": "nhà văn Mỹ Damon Runyon"},
    "lex.en.200k.056185": {"pos": "noun", "ipa": "/ʃvaɪtsɪz/", "vi": "nước Thụy Sĩ nói tiếng Đức"},
    "lex.en.200k.056186": {"pos": "noun", "ipa": "/ˈskɔːrpiaɪ/", "vi": "sao thuộc chòm sao Thiên Hạt"},
    "lex.en.200k.056187": {"pos": "noun", "ipa": "/ˈsiːkoʊsts/", "vi": "bờ biển; vùng duyên hải ven biển"},
    "lex.en.200k.056188": {"pos": "noun", "ipa": "/ˈsiːɡræsɪz/", "vi": "loài cỏ biển đáy đại dương"},
    "lex.en.200k.056189": {"pos": "noun", "ipa": "/ˈsɛsɪz/", "vi": "cần sa khô; tiếng lóng cần sa"},
    "lex.en.200k.056190": {"pos": "noun", "ipa": "/ʃəˈlɑːts/", "vi": "củ hành tím; củ hẹ tây nấu ăn"},
    "lex.en.200k.056191": {"pos": "noun", "ipa": "/ʃɪˈbæŋz/", "vi": "toàn bộ sự việc; chuỗi ký tự #!"},
    "lex.en.200k.056192": {"pos": "noun", "ipa": "/ˈskaɪbɑːksɪz/", "vi": "khu phòng VIP khán đài sân vận động"},
    "lex.en.200k.056193": {"pos": "noun", "ipa": "/ˈslɪŋərz/", "vi": "người bắn ná đá; người ném đạn"},
    "lex.en.200k.056194": {"pos": "noun", "ipa": "/ˈspiːkərfoʊnz/", "vi": "chức năng loa ngoài đàm thoại"},
    "lex.en.200k.056195": {"pos": "noun", "ipa": "/ˈstɪlwɛlz/", "vi": "tướng quân Joseph Stilwell"},
    "lex.en.200k.056196": {"pos": "noun", "ipa": "/ˈsuːləz/", "vi": "chi chim điên biển họ Sulidae"},
    "lex.en.200k.056197": {"pos": "noun", "ipa": "/ˈtæŋkərdz/", "vi": "vại lớn uống bia bằng thiếc"},
    "lex.en.200k.056198": {"pos": "noun", "ipa": "/ˈtɑːrpɑːnz/", "vi": "loài cá cháo lớn biển khơi"},
    "lex.en.200k.056199": {"pos": "noun", "ipa": "/ˌtiːˌsiːˈiːz/", "vi": "dung môi trichloroethylene TCE"},
    "lex.en.200k.056200": {"pos": "noun", "ipa": "/təˈrɛriəmz/", "vi": "bể cây cảnh tiểu cảnh kính kín"},
    "lex.en.200k.056201": {"pos": "noun", "ipa": "/ˈθɛspiənz/", "vi": "diễn viên kịch nghệ sân khấu"}
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

with open('scratch/b32_r03_p2.json', 'w', encoding='utf-8') as f:
    json.dump(output_items, f, ensure_ascii=False, indent=2)

print(f"Successfully authored and validated Part 2: {len(output_items)} items saved to scratch/b32_r03_p2.json")
