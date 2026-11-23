import json

items = [
    ("066303", "red phalarope", "phrase", "/rɛd ˈfæləˌroʊp/", "chim phalarope ngực hung"),
    ("066304", "relocatable program", "phrase", "/ˌriːloʊˈkeɪtəbəl ˈproʊɡræm/", "chương trình máy tính tái định vị"),
    ("066305", "res judicata", "phrase", "/ˌreɪz ˌdʒuːdɪˈkɑːtə/", "bản án đã có hiệu lực chung thẩm"),
    ("066306", "rubus ursinus", "phrase", "/ˈruːbəs ɜːrˈsaɪnəs/", "cây mâm xôi đen Thái Bình Dương"),
    ("066307", "socotra begonia", "phrase", "/səˈkoʊtrə bɪˈɡoʊniə/", "cây thu hải đường đảo Socotra"),
    ("066308", "tenpenny nail", "phrase", "/ˈtɛnpɛni neɪl/", "đinh sắt đóng gỗ dài ba inch"),
    ("066309", "tinea capitis", "phrase", "/ˈtɪniə ˈkæpɪtɪs/", "bệnh nấm hắc lào trên da đầu"),
    ("066310", "uncompahgre peak", "phrase", "/ˌʌnkəmˈpɑːɡreɪ piːk/", "đỉnh núi Uncompahgre Colorado"),
    ("066311", "undescended testis", "phrase", "/ˌʌndɪˈsɛndɪd ˈtɛstɪs/", "tật tinh hoàn ẩn bẩm sinh"),
    ("066312", "vanadium pentoxide", "phrase", "/vəˈneɪdiəm pɛnˈtɒksaɪd/", "hợp chất vanadi pentoxit xúc tác"),
    ("066313", "viola rostrata", "phrase", "/vaɪˈoʊlə rɒˈstreɪtə/", "cây hoa tím cựa dài Bắc Mỹ"),
    ("066314", "wild medlar", "phrase", "/waɪld ˈmɛdlər/", "cây sơn tra dại; cây nhót tây dại"),
    ("066315", "wild medlar tree", "phrase", "/waɪld ˈmɛdlər triː/", "cây gỗ sơn tra dại; nhót tây dại"),
    ("066316", "woolly mullein", "phrase", "/ˈwʊli ˈmʌlɪn/", "cây nhung thảo phủ lông len mịn"),
    ("066317", "acclimatized", "verb", "/əˈklaɪməˌtaɪzd/", "đã thích nghi khí hậu môi trường"),
    ("066318", "aconites", "noun", "/ˈækəˌnaɪts/", "cây ô đầu phụ tử có độc tính"),
    ("066319", "aments", "noun", "/ˈeɪmənts/", "cụm hoa đuôi sóc không cánh"),
    ("066320", "aneuploidies", "noun", "/ˈænjʊˌplɔɪdiz/", "thể lệch bội số lượng nhiễm sắc thể"),
    ("066321", "antiprotons", "noun", "/ˌæntiˈproʊtɒnz/", "hạt phản proton mang điện âm"),
    ("066322", "aurochses", "noun", "/ˈɔːrɒksɪz/", "bò rừng châu Âu cổ đại đã tuyệt"),
    ("066323", "backgrounders", "noun", "/ˈbækˌɡraʊndərz/", "buổi họp báo cung cấp thông tin nền"),
    ("066324", "bareboats", "noun", "/ˈbɛərˌboʊts/", "tàu thủy cho thuê nguyên vỏ trần"),
    ("066325", "bingers", "noun", "/ˈbɪndʒərz/", "người ăn chơi buông thả quá độ"),
    ("066326", "bucketfuls", "noun", "/ˈbʌkɪtˌfʊlz/", "lượng chất chứa đầy một xô"),
    ("066327", "buras", "noun", "/ˈbʊrəz/", "ngôn ngữ Bura ở đông bắc Nigeria"),
    ("066328", "buttonwoods", "noun", "/ˈbʌtənˌwʊdz/", "cây tiêu huyền Mỹ; cây đước nút"),
    ("066329", "cancans", "noun", "/ˈkænˌkænz/", "điệu múa đá chân cao cancan Pháp"),
    ("066330", "childproofed", "verb", "/ˈtʃaɪldˌpruːft/", "đã thiết kế khóa an toàn trẻ em"),
    ("066331", "childproofing", "verb", "/ˈtʃaɪldˌpruːfɪŋ/", "đang lắp đặt an toàn cho trẻ em"),
    ("066332", "childproofs", "verb", "/ˈtʃaɪldˌpruːfs/", "làm cho an toàn với trẻ nhỏ"),
    ("066333", "cicerones", "noun", "/ˌtʃɪtʃəˈroʊniz/", "hướng dẫn viên bảo tàng am hiểu"),
    ("066334", "cimetidines", "noun", "/sɪˈmɛtɪˌdiːnz/", "thuốc giảm axit dạ dày cimetidin"),
    ("066335", "citrullines", "noun", "/ˈsɪtrəˌliːnz/", "axit amin citrullin trong dưa hấu"),
    ("066336", "clomiphenes", "noun", "/ˈklɒmɪˌfiːnz/", "thuốc kích rụng trứng clomiphen"),
    ("066337", "codgers", "noun", "/ˈkɒdʒərz/", "ông lão lập dị hay gàn dở (lóng)"),
    ("066338", "codpieces", "noun", "/ˈkɒdˌpiːsɪz/", "miếng vải che hạ bộ thời Phục Hưng"),
    ("066339", "collied", "verb", "/ˈkɒlid/", "đã bôi đen bằng than mồ hóng (cổ)"),
    ("066340", "colliest", "verb", "/ˈkɒliɪst/", "bôi đen bằng than mồ hóng (cổ ngữ)"),
    ("066341", "collying", "verb", "/ˈkɒliɪŋ/", "đang bôi đen bằng bồ hóng (cổ ngữ)"),
    ("066342", "countersuits", "noun", "/ˈkaʊntərˌsuːts/", "đơn kiện ngược lại nguyên đơn"),
    ("066343", "cyclooxygenases", "noun", "/ˌsaɪkloʊˈɒksɪdʒəneɪsɪz/", "enzym tổng hợp prostaglandin"),
    ("066344", "cydonias", "noun", "/sɪˈdoʊniəz/", "cây mộc qua thuộc chi Cydonia"),
    ("066345", "daguerres", "noun", "/dəˈɡɛərz/", "nhà phát minh nhiếp ảnh Daguerre"),
    ("066346", "dehiscences", "noun", "/dɪˈhɪsənsɪz/", "sự nứt tách vỏ quả hoặc vết mổ"),
    ("066347", "destabilisations", "noun", "/diːˌsteɪbəlaɪˈzeɪʃənz/", "hành động gây bất ổn định"),
    ("066348", "devanagaris", "noun", "/ˌdeɪvəˈnɑːɡəriz/", "hệ chữ viết Devanagari của Ấn Độ"),
    ("066349", "diopters", "noun", "/daɪˈɒptərz/", "đơn vị đo độ tụ thấu kính điốp"),
    ("066350", "disembowelled", "verb", "/ˌdɪsɪmˈbaʊəld/", "đã mổ moi bỏ nội tạng"),
    ("066351", "disembowelling", "verb", "/ˌdɪsɪmˈbaʊəlɪŋ/", "đang mổ moi bỏ hết nội tạng"),
    ("066352", "distentions", "noun", "/dɪˈstɛnʃənz/", "sự căng trướng phồng rộp nội tạng"),
    ("066353", "dowlands", "noun", "/ˈdaʊləndz/", "nhà soạn nhạc Anh John Dowland"),
    ("066354", "dunkerques", "noun", "/dʌnˈkɜːrks/", "thành phố cảng Dunkirk của Pháp"),
    ("066355", "dunlins", "noun", "/ˈdʌnlɪnz/", "chim choắt bụng đen vùng ven biển"),
    ("066356", "endodonticses", "noun", "/ˌɛndəˈdɒntɪksɪz/", "chuyên khoa nội nha điều trị tủy"),
    ("066357", "etonians", "noun", "/iːˈtoʊniənz/", "học sinh hoặc cựu sinh viên Eton"),
    ("066358", "exordiums", "noun", "/ɛɡˈzɔːrdiəmz/", "phần mở đầu bài diễn văn hùng biện"),
    ("066359", "expectorants", "noun", "/ɪkˈspɛktərənts/", "thuốc long đờm giảm ho thông họng"),
    ("066360", "fenestras", "noun", "/fəˈnɛstrəz/", "lỗ cửa sổ nhỏ trên xương hoặc lá"),
    ("066361", "filariases", "noun", "/ˌfɪləˈraɪəsiːz/", "bệnh nhiễm giun chỉ bạch huyết"),
    ("066362", "finalisations", "noun", "/ˌfaɪnəlaɪˈzeɪʃənz/", "sự hoàn tất hoàn chỉnh lần cuối"),
    ("066363", "flossier", "adj", "/ˈflɒsiər/", "mịn như tơ hơn; hào nhoáng hơn"),
    ("066364", "flossiest", "adj", "/ˈflɒsiɪst/", "mịn như tơ nhất; hào nhoáng nhất"),
    ("066365", "forelocks", "noun", "/ˈfɔːrˌlɒks/", "tóc mái trước trán; bờm trán ngựa"),
    ("066366", "forints", "noun", "/ˈfɒrɪnts/", "đơn vị tiền tệ forint của Hungary"),
    ("066367", "fragonards", "noun", "/ˌfræɡəˈnɑːrdz/", "họa sĩ Rococo Pháp Fragonard"),
    ("066368", "gamboled", "verb", "/ˈɡæmbəld/", "đã nhảy nhót vui đùa tung tăng"),
    ("066369", "gamboling", "verb", "/ˈɡæmbəlɪŋ/", "đang nhảy nhót vui đùa tung tăng"),
    ("066370", "gambolled", "verb", "/ˈɡæmbəld/", "đã nhảy nhót vui đùa tung tăng"),
    ("066371", "gambolling", "verb", "/ˈɡæmbəlɪŋ/", "đang nhảy nhót vui đùa tung tăng"),
    ("066372", "gambols", "noun", "/ˈɡæmbəlz/", "cú nhảy nhót tung tăng vui đùa"),
    ("066373", "glomerulonephritides", "noun", "/ɡloʊˌmɛrjəloʊnəˈfraɪtɪdiːz/", "bệnh viêm tiểu cầu thận"),
    ("066374", "glottides", "noun", "/ˈɡlɒtɪdiːz/", "thanh môn giữa hai dây thanh âm"),
    ("066375", "glottises", "noun", "/ˈɡlɒtɪsɪz/", "thanh môn nằm trong thanh quản"),
    ("066376", "goudies", "noun", "/ˈɡaʊdiz/", "nhà thiết kế kiểu chữ Mỹ Goudy"),
    ("066377", "gurnards", "noun", "/ˈɡɜːrnərdz/", "cá chào mào biển có vây như cánh"),
    ("066378", "hejazes", "noun", "/hiːˈdʒɑːzɪz/", "vùng lịch sử Hejaz Ả Rập Xê Út"),
    ("066379", "hereros", "noun", "/həˈrɛəroʊz/", "người dân tộc Herero ở Namibia"),
    ("066380", "heterozygosities", "noun", "/ˌhɛtəroʊzaɪˈɡɒsɪtiz/", "tính trạng dị hợp tử di truyền"),
    ("066381", "hindbrains", "noun", "/ˈhaɪndˌbreɪnz/", "phần não sau gồm hành cầu tiểu não"),
    ("066382", "hortensias", "noun", "/hɔːrˈtɛnsiəz/", "hoa cẩm tú cầu màu lam hồng"),
    ("066383", "hypnoses", "noun", "/hɪpˈnoʊsiːz/", "trạng thái thôi miên; thần Hypnos"),
    ("066384", "izanamis", "noun", "/ˌiːzəˈnɑːmiz/", "nữ thần sáng thế Nhật Izanami"),
    ("066385", "jatrophas", "noun", "/dʒəˈtroʊfəz/", "cây cọc rào dầu diesel sinh học"),
    ("066386", "kroneckers", "noun", "/ˈkroʊnɛkərz/", "nhà toán học Đức Leopold Kronecker"),
    ("066387", "lambasted", "verb", "/læmˈbæstɪd/", "đã chỉ trích gay gắt; đã đánh đòn"),
    ("066388", "lambasting", "verb", "/læmˈbæstɪŋ/", "đang chỉ trích gay gắt; đánh đòn"),
    ("066389", "lambasts", "verb", "/læmˈbæsts/", "chỉ trích gay gắt; đánh đập mạnh"),
    ("066390", "langurs", "noun", "/lʌŋˈɡʊərz/", "loài voọc đuôi dài châu Á"),
    ("066391", "logotypes", "noun", "/ˈlɒɡəˌtaɪps/", "biểu trưng chữ cái thương hiệu"),
    ("066392", "lovages", "noun", "/ˈlʌvɪdʒɪz/", "cây cần núi gia vị giống cần tây"),
    ("066393", "medicagos", "noun", "/ˌmɛdɪˈkeɪɡoʊz/", "cây linh lăng thuộc chi Medicago"),
    ("066394", "middlebrows", "noun", "/ˈmɪdəlˌbraʊz/", "người chuộng văn hóa tầm trung"),
    ("066395", "minivers", "noun", "/ˈmɪnɪvərz/", "lông thú trắng viền áo lễ quý tộc"),
    ("066396", "missourians", "noun", "/mɪˈzʊriənz/", "người dân bang Missouri của Mỹ"),
    ("066397", "motorcoaches", "noun", "/ˈmoʊtərˌkoʊtʃɪz/", "xe buýt khách đường dài cỡ lớn"),
    ("066398", "moviegoers", "noun", "/ˈmuːviˌɡoʊərz/", "khán giả hay đi xem phim rạp"),
    ("066399", "nauruans", "noun", "/nɑːˈuːruːənz/", "người dân đảo quốc Nauru"),
    ("066400", "ncdcs", "noun", "/ˌɛn siː diː ˈsiːz/", "Trung tâm Dữ liệu Khí hậu Mỹ"),
    ("066401", "nembutals", "noun", "/ˈnɛmbjʊˌtɔːlz/", "thuốc ngủ an thần Nembutal"),
    ("066402", "nephrectomies", "noun", "/nəˈfrɛktəmiz/", "ca phẫu thuật cắt bỏ một bên thận"),
]

with open("scratch/b34_r03_raw_p4.json") as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100
allowed_pos = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det", "phrase"}

out = []
for r, (rid, hw, pos, ipa, vi) in zip(raw, items):
    assert r["id"].endswith("." + rid), f"ID mismatch: {r['id']} != {rid}"
    assert r["hw"] == hw, f"HW mismatch: {r['hw']} != {hw}"
    assert pos in allowed_pos, f"Bad POS {pos} for {hw}"
    assert len(vi) <= 35, f"VI too long ({len(vi)}): {hw} -> {vi}"
    assert ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2, f"Bad IPA: {hw} -> {ipa}"
    inner = ipa[1:-1]
    assert inner and not inner.startswith(" ") and not inner.endswith(" "), f"Empty/space IPA: {hw} -> {ipa}"
    rec = dict(r)
    rec["pos"] = pos
    rec["ipa"] = ipa
    rec["vi"] = vi
    rec["status"] = "reviewed"
    out.append(rec)

with open("scratch/b34_r03_p4.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b34_r03_p4.json OK")
