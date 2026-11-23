import json

items = [
    ("072203", "sebes", "noun", "/ˌɛs iː biː ˈiːz/", "hướng đông-nam lệch đông (SEbE)"),
    ("072204", "shavians", "noun", "/ˈʃeɪviənz/", "người hâm mộ văn hào G. B. Shaw"),
    ("072205", "speedskaters", "noun", "/ˈspiːdˌskeɪtərz/", "vận động viên trượt băng tốc độ"),
    ("072206", "stoneflies", "noun", "/ˈstoʊnˌflaɪz/", "bọ cánh úp sống gần suối đá"),
    ("072207", "storaxes", "noun", "/ˈstɔːræksɪz/", "nhựa thơm cây bồ đề (storax)"),
    ("072208", "supercargoes", "noun", "/ˌsuːpərˈkɑːrɡoʊz/", "người giám sát hàng hóa trên tàu"),
    ("072209", "swagmans", "noun", "/ˈswæɡmənz/", "người làm thuê lang thang (Úc cũ)"),
    ("072210", "tablespoonfuls", "noun", "/ˈteɪbəlˌspuːnfʊlz/", "lượng đầy một thìa canh"),
    ("072211", "technophobes", "noun", "/ˈtɛknəˌfoʊbz/", "người sợ hãi né tránh công nghệ"),
    ("072212", "termers", "noun", "/ˈtɜːrmərz/", "người giữ chức vụ theo nhiệm kỳ"),
    ("072213", "tessins", "noun", "/ˈtɛsɪnz/", "bang Ticino ở miền nam Thụy Sĩ"),
    ("072214", "theorizations", "noun", "/ˌθiːəraɪˈzeɪʃənz/", "sự khái quát hóa thành lý thuyết"),
    ("072215", "throughways", "noun", "/ˈθruːˌweɪz/", "đường cao tốc thu phí nối liền"),
    ("072216", "thumbscrews", "noun", "/ˈθʌmˌskruːz/", "ốc vặn tay cái; kẹp tra tấn xưa"),
    ("072217", "tungas", "noun", "/ˈtʌŋɡəz/", "bọ chét cát chui da chi Tunga"),
    ("072218", "uniates", "noun", "/ˈjuːniˌeɪts/", "tín đồ Công giáo nghi lễ Đông"),
    ("072219", "veratrums", "noun", "/vɪˈreɪtrəmz/", "cây lê lô độc thuộc chi Veratrum"),
    ("072220", "waldenseses", "noun", "/wɔːlˈdɛnsiːzɪz/", "giáo phái Tin Lành Waldensian"),
    ("072221", "whoresons", "noun", "/ˈhɔːrsənz/", "từ chửi thô tục cổ (văn học cổ)"),
    ("072222", "wimbles", "noun", "/ˈwɪmbəlz/", "mũi khoan gỗ lớn cầm tay (khoan)"),
    ("072223", "wiseacres", "noun", "/ˈwaɪzˌeɪkərz/", "kẻ hợm hĩnh làm bộ hiểu biết"),
    ("072224", "yogacaras", "noun", "/ˌjoʊɡəˈtʃɑːrəz/", "Duy thức tông trong Phật giáo"),
    ("072225", "advancers", "noun", "/ədˈvænsərz/", "người thăng tiến; vật thúc đẩy"),
    ("072226", "affixations", "noun", "/ˌæfɪkˈseɪʃənz/", "sự gắn thêm phụ tố; sự đóng dấu"),
    ("072227", "agnates", "noun", "/ˈæɡneɪts/", "họ hàng bên nội (cùng dòng cha)"),
    ("072228", "alabamians", "noun", "/ˌæləˈbæmiənz/", "người dân bang Alabama của Mỹ"),
    ("072229", "alcas", "noun", "/ˈælkəz/", "chi Chim an ca Bắc Cực (Alca)"),
    ("072230", "aldoses", "noun", "/ˈældoʊsɪz/", "đường đơn chứa nhóm andehit"),
    ("072231", "alendronates", "noun", "/əˈlɛndrəˌneɪts/", "thuốc trị loãng xương alendronate"),
    ("072232", "andrenas", "noun", "/ænˈdriːnəz/", "chi Ong thợ đào đất (Andrena)"),
    ("072233", "ankylosauruses", "noun", "/æŋˌkaɪləˈsɔːrəsɪz/", "khủng long bọc giáp Ankylosaurus"),
    ("072234", "annelidas", "noun", "/əˈnɛlɪdəz/", "ngành Giun đốt (giun đất, đỉa)"),
    ("072235", "appropriators", "noun", "/əˈproʊpriˌeɪtərz/", "người chiếm dụng; nghị sĩ phân bổ"),
    ("072236", "ariosos", "noun", "/ˌɑːriˈoʊsoʊz/", "khúc nhạc thanh nhạc arioso"),
    ("072237", "artocarpi", "noun", "/ˌɑːrtəˈkɑːrpaɪ/", "chi Cây mít và xa kê (Artocarpus)"),
    ("072238", "asklepioses", "noun", "/æˈskliːpiˌɒsɪz/", "thần y học Hy Lạp Asclepius"),
    ("072239", "backbends", "noun", "/ˈbækˌbɛndz/", "động tác uốn dẻo cong lưng ra sau"),
    ("072240", "bailors", "noun", "/ˈbeɪlərz/", "người ký gửi giao giữ tài sản"),
    ("072241", "benisons", "noun", "/ˈbɛnɪzənz/", "lời chúc phúc ban phước lành"),
    ("072242", "benzylpenicillins", "noun", "/ˌbɛnzɪlpɛnɪˈsɪlɪnz/", "kháng sinh penicillin G (tiêm)"),
    ("072243", "bhagavadgitas", "noun", "/ˌbʌɡəvədˈɡiːtəz/", "kinh Bhagavad Gita Ấn Độ giáo"),
    ("072244", "bilharzias", "noun", "/bɪlˈhɑːrziəz/", "bệnh sán máng nhiệt đới"),
    ("072245", "blastulae", "noun", "/ˈblæstjʊˌliː/", "phôi nang (giai đoạn phôi sớm)"),
    ("072246", "blastulas", "noun", "/ˈblæstjʊləz/", "phôi nang (giai đoạn phôi sớm)"),
    ("072247", "boorishnesses", "noun", "/ˈbʊərɪʃnəsɪz/", "tính thô lỗ cục cằn thiếu lịch sự"),
    ("072248", "cairenes", "noun", "/kaɪˈriːnz/", "người dân thành phố Cairo Ai Cập"),
    ("072249", "carassiuses", "noun", "/kəˈræsiəsɪz/", "chi Cá diếc và cá vàng (Carassius)"),
    ("072250", "cardizems", "noun", "/ˈkɑːrdɪˌzɛmz/", "thuốc tim mạch hạ áp Cardizem"),
    ("072251", "catchwords", "noun", "/ˈkætʃˌwɜːrdz/", "khẩu hiệu cửa miệng; từ dẫn trang"),
    ("072252", "censed", "verb", "/sɛnst/", "đã xông trầm hương nghi lễ"),
    ("072253", "censes", "verb", "/ˈsɛnsɪz/", "xông trầm hương trong nghi lễ"),
    ("072254", "censing", "verb", "/ˈsɛnsɪŋ/", "đang xông trầm hương nghi lễ"),
    ("072255", "chadics", "noun", "/ˈtʃædɪks/", "nhóm ngôn ngữ Chadic Tây Phi"),
    ("072256", "coccidias", "noun", "/kɒkˈsɪdiəz/", "phân lớp Trùng cầu ký sinh"),
    ("072257", "confucianists", "noun", "/kənˈfjuːʃənɪsts/", "người theo Nho giáo (Khổng giáo)"),
    ("072258", "cucurbitaceaes", "noun", "/kjuːˌkɜːrbɪˈteɪʃiˌiːz/", "họ Bầu bí (bí, dưa, mướp)"),
    ("072259", "curiosas", "noun", "/ˌkjʊəriˈoʊzəz/", "sách cổ quý hiếm hoặc gợi cảm"),
    ("072260", "decimalisations", "noun", "/ˌdɛsɪməlaɪˈzeɪʃənz/", "sự chuyển sang hệ thập phân (Anh)"),
    ("072261", "deepfreezes", "noun", "/ˌdiːpˈfriːzɪz/", "tủ cấp đông nhiệt độ rất sâu"),
    ("072262", "dentifrices", "noun", "/ˈdɛntɪfrɪsɪz/", "kem hoặc bột vệ sinh đánh răng"),
    ("072263", "diplegias", "noun", "/daɪˈpliːdʒəz/", "chứng liệt đối xứng hai bên cơ thể"),
    ("072264", "dotterels", "noun", "/ˈdɒtərəlz/", "chim choi choi vùng núi cao"),
    ("072265", "duennas", "noun", "/djuːˈɛnəz/", "nữ gia sư kèm cặp thiếu nữ (TBN)"),
    ("072266", "echinuses", "noun", "/ɪˈkaɪnəsɪz/", "đường gờ tròn đầu cột Hy Lạp; nhím"),
    ("072267", "elsasses", "noun", "/ˈɛlzɑːsɪz/", "vùng Alsace phía đông Pháp (Đức)"),
    ("072268", "elymi", "noun", "/ˈɛlɪˌmaɪ/", "chi Cỏ lúa mì hoang Elymus"),
    ("072269", "embracements", "noun", "/ɪmˈbreɪsmənts/", "cái ôm siết chặt; sự đón nhận"),
    ("072270", "epicondylitises", "noun", "/ˌɛpɪkɒndɪˈlaɪtɪsɪz/", "viêm lồi cầu khuỷu tay (tay vợt)"),
    ("072271", "erwinias", "noun", "/ɜːrˈwɪniəz/", "vi khuẩn gây thối nhũn Erwinia"),
    ("072272", "fauteuils", "noun", "/foʊˈtɜːɪz/", "ghế bành có tay vịn bọc nệm"),
    ("072273", "fireboats", "noun", "/ˈfaɪərˌboʊts/", "tàu cứu hỏa chuyên dụng trên sông"),
    ("072274", "forgivers", "noun", "/fərˈɡɪvərz/", "người bao dung sẵn lòng tha thứ"),
    ("072275", "fulbes", "noun", "/ˈfʊlbeɪz/", "dân tộc và tiếng Fulani (Tây Phi)"),
    ("072276", "geebungs", "noun", "/ˈdʒiːbʌŋz/", "cây bụi quả geebung của Úc"),
    ("072277", "gossipers", "noun", "/ˈɡɒsɪpərz/", "người hay ngồi lê đôi mách"),
    ("072278", "guncottons", "noun", "/ˈɡʌnˌkɒtənz/", "thuốc súng bông (nitroxenluloza)"),
    ("072279", "hareems", "noun", "/həˈriːmz/", "hậu cung cung phi Hồi giáo (cổ)"),
    ("072280", "heimdals", "noun", "/ˈheɪmdɑːlz/", "thần canh gác cầu vồng Heimdall"),
    ("072281", "horehounds", "noun", "/ˈhɔːrˌhaʊndz/", "cây thảo dược trị ho horehound"),
    ("072282", "iduns", "noun", "/ˈiːdʊnz/", "nữ thần tuổi trẻ Idunn Bắc Âu"),
    ("072283", "imides", "noun", "/ˈɪmaɪdz/", "hợp chất hữu cơ chứa nhóm imid"),
    ("072284", "kabbalas", "noun", "/kəˈbɑːləz/", "triết lý mật giáo Do Thái Kabbalah"),
    ("072285", "labdanums", "noun", "/ˈlæbdənəmz/", "nhựa thơm thực vật labdanum"),
    ("072286", "lexicologies", "noun", "/ˌlɛksɪˈkɒlədʒiz/", "ngành từ vựng học ngôn ngữ"),
    ("072287", "magnetisations", "noun", "/ˌmæɡnɪtaɪˈzeɪʃənz/", "sự từ hóa nhiễm từ vật liệu (Anh)"),
    ("072288", "malingerers", "noun", "/məˈlɪŋɡərərz/", "kẻ giả vờ ốm đau để trốn việc"),
    ("072289", "massines", "noun", "/mæˈsiːnz/", "biên đạo múa Nga Léonide Massine"),
    ("072290", "miscounted", "verb", "/ˌmɪsˈkaʊntɪd/", "đã đếm nhầm; đã kiểm phiếu sai"),
    ("072291", "miscounting", "verb", "/ˌmɪsˈkaʊntɪŋ/", "đang đếm nhầm số lượng"),
    ("072292", "miscounts", "noun", "/ˌmɪsˈkaʊnts/", "sự đếm nhầm; sai sót kiểm đếm"),
    ("072293", "monacans", "noun", "/ˈmɒnəkənz/", "bộ tộc bản địa Monacan ở Virginia"),
    ("072294", "moneymans", "noun", "/ˈmʌnɪmənz/", "ông trùm cấp vốn; chuyên gia tiền"),
    ("072295", "musers", "noun", "/ˈmjuːzərz/", "người trầm tư suy nghĩ mông lung"),
    ("072296", "nanuses", "noun", "/ˈneɪnəsɪz/", "người lùn cổ (Latinh); cây lùn"),
    ("072297", "nebbishes", "noun", "/ˈnɛbɪʃɪz/", "kẻ nhút nhát khờ khạo yếu đuối"),
    ("072298", "neuroethicses", "noun", "/ˌnjʊəroʊˈɛθɪksɪz/", "đạo đức học thần kinh"),
    ("072299", "nosebands", "noun", "/ˈnoʊzˌbændz/", "dây đai vòng qua sống mũi ngựa"),
    ("072300", "orographies", "noun", "/ɔːˈrɒɡrəfiz/", "sơn địa học (nghiên cứu núi non)"),
    ("072301", "otoscopes", "noun", "/ˈoʊtəˌskoʊps/", "đèn soi kiểm tra màng nhĩ ống tai"),
    ("072302", "oujdas", "noun", "/ˈuːdʒdəz/", "thành phố Oujda ở đông bắc Morocco"),
]

with open("scratch/b35_r05_raw_p3.json") as f:
    raw = json.load(f)

assert len(items) == 100
assert len(raw) == 100
allowed_pos = {"noun", "verb", "adj", "adv", "num", "intj", "prep", "pron", "conj", "det", "phrase"}
out = []
for r, (rid, hw, pos, ipa, vi) in zip(raw, items):
    assert r["id"].endswith("." + rid), f"ID mismatch: {r['id']} != {rid}"
    assert r["hw"] == hw, f"HW mismatch: {r['hw']} != {hw}"
    assert pos in allowed_pos, f"Bad POS: {pos}"
    assert len(vi) <= 35, f"VI too long ({len(vi)}): {hw} -> {vi}"
    assert ipa.startswith("/") and ipa.endswith("/") and ipa.count("/") == 2, f"Bad IPA: {hw} -> {ipa}"
    assert not ipa[1:-1].startswith(" ") and not ipa[1:-1].endswith(" "), f"Space in IPA: {hw} -> {ipa}"
    out.append({**r, "pos": pos, "ipa": ipa, "vi": vi, "status": "reviewed"})

with open("scratch/b35_r05_p3.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r05_p3.json OK")
