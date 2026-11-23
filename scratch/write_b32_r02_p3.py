import json

with open('scratch/b32_r02_raw_p3.json') as f:
    raw_items = json.load(f)

reviewed_data = {
    "lex.en.200k.055702": {"pos": "phrase", "ipa": "", "vi": "hệ thống kích hoạt lưới ở não"},
    "lex.en.200k.055703": {"pos": "phrase", "ipa": "", "vi": "nhà cổ nhân học Richard Leakey"},
    "lex.en.200k.055704": {"pos": "phrase", "ipa": "", "vi": "nhà sử học kinh tế R. H. Tawney"},
    "lex.en.200k.055705": {"pos": "phrase", "ipa": "", "vi": "sốt phô mai Roquefort"},
    "lex.en.200k.055706": {"pos": "phrase", "ipa": "", "vi": "thoát vị đĩa đệm cột sống"},
    "lex.en.200k.055707": {"pos": "phrase", "ipa": "", "vi": "sự hối lỗi; sự ăn năn đau buồn"},
    "lex.en.200k.055708": {"pos": "phrase", "ipa": "", "vi": "globulin huyết thanh"},
    "lex.en.200k.055709": {"pos": "phrase", "ipa": "", "vi": "người Sierra Leone"},
    "lex.en.200k.055710": {"pos": "phrase", "ipa": "", "vi": "nhà hóa học William Crookes"},
    "lex.en.200k.055711": {"pos": "phrase", "ipa": "", "vi": "cá bống tượng; cá bống ngủ"},
    "lex.en.200k.055712": {"pos": "phrase", "ipa": "", "vi": "bõm bõm; sánh nước; văng tóe nước"},
    "lex.en.200k.055713": {"pos": "phrase", "ipa": "", "vi": "chải chuốt; làm cho bảnh bao"},
    "lex.en.200k.055714": {"pos": "phrase", "ipa": "", "vi": "cây mao địa hoàng hoa vàng"},
    "lex.en.200k.055715": {"pos": "phrase", "ipa": "", "vi": "khu vực phát bóng gôn"},
    "lex.en.200k.055716": {"pos": "phrase", "ipa": "", "vi": "vị tướng Tadeusz Kościuszko"},
    "lex.en.200k.055717": {"pos": "phrase", "ipa": "", "vi": "hoa cát tường; hoa lan tường"},
    "lex.en.200k.055718": {"pos": "phrase", "ipa": "", "vi": "xương màng nhĩ"},
    "lex.en.200k.055719": {"pos": "phrase", "ipa": "", "vi": "màu tía hoàng gia Tyrian"},
    "lex.en.200k.055720": {"pos": "phrase", "ipa": "", "vi": "ren đăng ten Valenciennes"},
    "lex.en.200k.055721": {"pos": "phrase", "ipa": "", "vi": "cây lá dưa hấu; hồ tiêu dưa hấu"},
    "lex.en.200k.055722": {"pos": "phrase", "ipa": "", "vi": "nhà viết kịch William Congreve"},
    "lex.en.200k.055723": {"pos": "phrase", "ipa": "", "vi": "nhà hóa học William Crookes"},
    "lex.en.200k.055724": {"pos": "noun", "ipa": "/ˈɛskɪləsɪz/", "vi": "nhà bi kịch Aeschylus"},
    "lex.en.200k.055725": {"pos": "noun", "ipa": "/ˈæmərænθs/", "vi": "cây rau dền; sắc đỏ hoa dền"},
    "lex.en.200k.055726": {"pos": "noun", "ipa": "/ˈɑːmʊndsənz/", "vi": "nhà thám hiểm Roald Amundsen"},
    "lex.en.200k.055727": {"pos": "noun", "ipa": "/ˌærɪˈstɑːfəniːzɪz/", "vi": "nhà hài kịch Aristophanes"},
    "lex.en.200k.055728": {"pos": "noun", "ipa": "/ˈeɪviːzɪz/", "vi": "lớp chim; các loài chim"},
    "lex.en.200k.055729": {"pos": "noun", "ipa": "/buːtəˈniːzɪz/", "vi": "người Bhutan"},
    "lex.en.200k.055730": {"pos": "noun", "ipa": "/bəˈnoʊboʊz/", "vi": "loài vượn bonobo; tinh tinh lùn"},
    "lex.en.200k.055731": {"pos": "noun", "ipa": "/bɜːrks/", "vi": "người mang họ Burk"},
    "lex.en.200k.055732": {"pos": "noun", "ipa": "/kænˈtuːnmənts/", "vi": "doanh trại quân đội; khu đóng quân"},
    "lex.en.200k.055733": {"pos": "noun", "ipa": "/ˈkeɪsˌwɜːrkərz/", "vi": "nhân viên xã hội phụ trách hồ sơ"},
    "lex.en.200k.055734": {"pos": "noun", "ipa": "/ˌkæsioʊˈpiːəz/", "vi": "chòm sao Thiên Hậu"},
    "lex.en.200k.055735": {"pos": "noun", "ipa": "/ˈtʃiːvərz/", "vi": "nhà văn John Cheever"},
    "lex.en.200k.055736": {"pos": "noun", "ipa": "/tʃɛlˈjɑːbɪnsks/", "vi": "thành phố Chelyabinsk của Nga"},
    "lex.en.200k.055737": {"pos": "noun", "ipa": "/ʃɪˈkeɪnz/", "vi": "khúc cua chữ S zic-zắc; mưu lừa dối"},
    "lex.en.200k.055738": {"pos": "noun", "ipa": "/ˌkɑːnvəˈlɛsənsɪz/", "vi": "thời kỳ dưỡng bệnh hồi phục"},
    "lex.en.200k.055739": {"pos": "noun", "ipa": "/ˈkræŋkkeɪsɪz/", "vi": "hộp các-te; hộp trục khuỷu động cơ"},
    "lex.en.200k.055740": {"pos": "noun", "ipa": "/krɔːz/", "vi": "diều chim; dạ dày động vật"},
    "lex.en.200k.055741": {"pos": "verb", "ipa": "/dɪˈfreɪd/", "vi": "đã thanh toán; đã chi trả chi phí"},
    "lex.en.200k.055742": {"pos": "verb", "ipa": "/dɪˈfreɪɪŋ/", "vi": "thanh toán viện trợ; chi trả"},
    "lex.en.200k.055743": {"pos": "verb", "ipa": "/dɪˈfreɪz/", "vi": "thanh toán; chịu chi phí"},
    "lex.en.200k.055744": {"pos": "noun", "ipa": "/dɪˈlɪvərərz/", "vi": "người cứu rỗi; người giao hàng"},
    "lex.en.200k.055745": {"pos": "noun", "ipa": "/dɪˈsɛndənts/", "vi": "hậu duệ; con cháu đời sau"},
    "lex.en.200k.055746": {"pos": "noun", "ipa": "/ˈdɜːrdʒɪz/", "vi": "khúc bi ca; bài hát đám tang"},
    "lex.en.200k.055747": {"pos": "verb", "ipa": "/dɪsˈmɛmbərd/", "vi": "đã phân thây; chặt đứt chân tay"},
    "lex.en.200k.055748": {"pos": "verb", "ipa": "/dɪsˈmɛmbərɪŋ/", "vi": "phân thây xé xác; chia cắt đất"},
    "lex.en.200k.055749": {"pos": "verb", "ipa": "/dɪsˈmɛmbərz/", "vi": "phân thây; chia nhỏ cắt đoạn"},
    "lex.en.200k.055750": {"pos": "noun", "ipa": "/ˈdoʊzərz/", "vi": "máy ủi đất; người ngủ gật"},
    "lex.en.200k.055751": {"pos": "noun", "ipa": "/ˈaɪɡənˌvæljuːz/", "vi": "giá trị riêng toán học"},
    "lex.en.200k.055752": {"pos": "noun", "ipa": "/ˈɛnθælpiz/", "vi": "nhiệt hàm entanpi hóa học"},
    "lex.en.200k.055753": {"pos": "noun", "ipa": "/ˈfɑːrmstɛdz/", "vi": "khu nhà trang trại gia đình"},
    "lex.en.200k.055754": {"pos": "noun", "ipa": "/ˌfɛmənəˈzeɪʃənz/", "vi": "quá trình nữ tính hóa"},
    "lex.en.200k.055755": {"pos": "noun", "ipa": "/ˈfɔːrfɪŋɡərz/", "vi": "ngón tay trỏ"},
    "lex.en.200k.055756": {"pos": "noun", "ipa": "/ˈfreɪkəsɪz/", "vi": "những cuộc ẩu đả ầm ĩ"},
    "lex.en.200k.055757": {"pos": "noun", "ipa": "/ˈɡɔːltənz/", "vi": "nhà khoa học Francis Galton"},
    "lex.en.200k.055758": {"pos": "adj", "ipa": "/ˈɡæsiər/", "vi": "đầy hơi hơn; nhiều khí gas hơn"},
    "lex.en.200k.055759": {"pos": "adj", "ipa": "/ˈɡæsiɪst/", "vi": "đầy hơi nhất; nhiều khí gas nhất"},
    "lex.en.200k.055760": {"pos": "noun", "ipa": "/ˈɡɪzərdz/", "vi": "mề chim; mề gà vịt"},
    "lex.en.200k.055761": {"pos": "noun", "ipa": "/ɡəˈdaɪvəz/", "vi": "phu nhân Lady Godiva"},
    "lex.en.200k.055762": {"pos": "noun", "ipa": "/ˈɡoʊməz/", "vi": "thành phố Goma ở Congo"},
    "lex.en.200k.055763": {"pos": "noun", "ipa": "/ˈɡraɪndstoʊnz/", "vi": "đá mài dụng cụ dao kéo"},
    "lex.en.200k.055764": {"pos": "noun", "ipa": "/ˈhɑːdʒpɑːdʒɪz/", "vi": "mớ hỗn độn thập cẩm tạp nham"},
    "lex.en.200k.055765": {"pos": "noun", "ipa": "/ˌɑːnəˈrɪfɪks/", "vi": "kính ngữ; tước hiệu tôn kính"},
    "lex.en.200k.055766": {"pos": "noun", "ipa": "/ˈhɑːpskɑːtʃɪz/", "vi": "trò chơi nhảy lò cò"},
    "lex.en.200k.055767": {"pos": "verb", "ipa": "/ɪnˈstɪlz/", "vi": "thấm nhuần; truyền thụ từ từ"},
    "lex.en.200k.055768": {"pos": "verb", "ipa": "/ɜːrkt/", "vi": "đã làm phiền lòng; đã làm bực bội"},
    "lex.en.200k.055769": {"pos": "verb", "ipa": "/ˈɜːrkɪŋ/", "vi": "làm phát cáu; chọc tức; làm bực"},
    "lex.en.200k.055770": {"pos": "verb", "ipa": "/ɜːrks/", "vi": "làm bực mình; làm chướng mắt"},
    "lex.en.200k.055771": {"pos": "noun", "ipa": "/ˌdʒɛfərˈsoʊniənz/", "vi": "người theo chủ nghĩa Jefferson"},
    "lex.en.200k.055772": {"pos": "noun", "ipa": "/kraʊts/", "vi": "tiếng lóng miệt thị người Đức"},
    "lex.en.200k.055773": {"pos": "noun", "ipa": "/kuːˈmɑːsiz/", "vi": "thành phố Kumasi của Ghana"},
    "lex.en.200k.055774": {"pos": "noun", "ipa": "/ˌlæktoʊbəˈsɪlaɪ/", "vi": "vi khuẩn axit lactic lactobacillus"},
    "lex.en.200k.055775": {"pos": "noun", "ipa": "/lɪzˈboʊəz/", "vi": "thành phố Lisboa ở Bồ Đào Nha"},
    "lex.en.200k.055776": {"pos": "noun", "ipa": "/meɪnˈteɪnərz/", "vi": "người bảo trì; người duy trì dự án"},
    "lex.en.200k.055777": {"pos": "noun", "ipa": "/ˈmɛndəlsənz/", "vi": "nhà soạn nhạc Felix Mendelssohn"},
    "lex.en.200k.055778": {"pos": "noun", "ipa": "/mərˈkeɪtərz/", "vi": "nhà vẽ bản đồ Gerardus Mercator"},
    "lex.en.200k.055779": {"pos": "noun", "ipa": "/ˈmɪlɪnərz/", "vi": "thợ làm và bán mũ nữ"},
    "lex.en.200k.055780": {"pos": "noun", "ipa": "/ˈmɪniskɜːrts/", "vi": "váy ngắn ngang đùi; váy mini"},
    "lex.en.200k.055781": {"pos": "noun", "ipa": "/ˈmɪtfərdz/", "vi": "gia đình quý tộc chị em Mitford"},
    "lex.en.200k.055782": {"pos": "noun", "ipa": "/nɪˈfrɑːlədʒiz/", "vi": "chuyên khoa thận học"},
    "lex.en.200k.055783": {"pos": "noun", "ipa": "/ˈnɛsiz/", "vi": "quái vật hồ Loch Ness"},
    "lex.en.200k.055784": {"pos": "adj", "ipa": "/ˈnɪpiər/", "vi": "lạnh buốt hơn; nhanh nhẹn hơn"},
    "lex.en.200k.055785": {"pos": "adj", "ipa": "/ˈnɪpiɪst/", "vi": "lạnh buốt nhất; nhanh nhẹn nhất"},
    "lex.en.200k.055786": {"pos": "noun", "ipa": "/ˌoʊkiːˈtʃoʊbiz/", "vi": "hồ nước ngọt Okeechobee ở Florida"},
    "lex.en.200k.055787": {"pos": "noun", "ipa": "/ˈuːlɑːŋz/", "vi": "trà ô long thượng hạng"},
    "lex.en.200k.055788": {"pos": "noun", "ipa": "/ˌɔːriˈɛntəlɪzəmz/", "vi": "chủ nghĩa đông phương học"},
    "lex.en.200k.055789": {"pos": "noun", "ipa": "/pəˈtʃɪŋkoʊz/", "vi": "máy trò chơi bắn bi pachinko"},
    "lex.en.200k.055790": {"pos": "noun", "ipa": "/ˈpælətəlz/", "vi": "phụ âm vòm cứng ngạc mềm"},
    "lex.en.200k.055791": {"pos": "noun", "ipa": "/ˌpɛnsəlˈveɪniənz/", "vi": "người dân bang Pennsylvania"},
    "lex.en.200k.055792": {"pos": "noun", "ipa": "/pɛˈroʊnz/", "vi": "nhà chính trị Perón của Argentina"},
    "lex.en.200k.055793": {"pos": "noun", "ipa": "/ˈpɜːrsənɪdʒɪz/", "vi": "nhân vật quan trọng; bậc danh nhân"},
    "lex.en.200k.055794": {"pos": "noun", "ipa": "/ˈpɛtərz/", "vi": "người vuốt ve thú cưng"},
    "lex.en.200k.055795": {"pos": "noun", "ipa": "/ˈpɑːliɡlɑːts/", "vi": "người thông thạo nhiều thứ tiếng"},
    "lex.en.200k.055796": {"pos": "adj", "ipa": "/ˈpriːtʃiər/", "vi": "thích thuyết giáo luân lý hơn"},
    "lex.en.200k.055797": {"pos": "adj", "ipa": "/ˈpriːtʃiɪst/", "vi": "thích thuyết giáo luân lý nhất"},
    "lex.en.200k.055798": {"pos": "noun", "ipa": "/prɪˈzɜːrvərz/", "vi": "người bảo tồn; phao cứu sinh"},
    "lex.en.200k.055799": {"pos": "verb", "ipa": "/ˈpʌblɪsaɪzɪz/", "vi": "quảng bá; công khai rộng rãi"},
    "lex.en.200k.055800": {"pos": "verb", "ipa": "/ˈpʌblɪsaɪzɪŋ/", "vi": "quảng bá; đưa tin rầm rộ"},
    "lex.en.200k.055801": {"pos": "noun", "ipa": "/ˌræʃnələˈzeɪʃənz/", "vi": "sự hợp lý hóa; sự ngụy biện"}
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

with open('scratch/b32_r02_p3.json', 'w', encoding='utf-8') as f:
    json.dump(output_items, f, ensure_ascii=False, indent=2)

print(f"Successfully authored and validated Part 3: {len(output_items)} items saved to scratch/b32_r02_p3.json")
