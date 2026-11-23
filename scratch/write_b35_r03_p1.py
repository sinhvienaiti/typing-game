import json

items = [
    ("071003", "boswellias", "noun", "/bɒzˈwɛliəz/", "cây nhũ hương thuộc chi Boswellia"),
    ("071004", "boused", "verb", "/baʊzd/", "đã kéo tời lên bằng ròng rọc (hải)"),
    ("071005", "bouses", "verb", "/ˈbaʊzɪz/", "kéo tời nâng bằng ròng rọc (hải)"),
    ("071006", "bousing", "verb", "/ˈbaʊzɪŋ/", "đang kéo nâng bằng ròng rọc"),
    ("071007", "bowlfuls", "noun", "/ˈboʊlˌfʊlz/", "lượng đầy một bát tô"),
    ("071008", "breadboxes", "noun", "/ˈbrɛdˌbɒksɪz/", "hộp đậy bảo quản bánh mì"),
    ("071009", "burbots", "noun", "/ˈbɜːrbəts/", "cá tuyết sông nước ngọt burbot"),
    ("071010", "cadetships", "noun", "/kəˈdɛtʃɪps/", "suất học viên trường sĩ quan"),
    ("071011", "camponotuses", "noun", "/ˌkæmpəˈnoʊtəsɪz/", "kiến thợ mộc thuộc chi Camponotus"),
    ("071012", "cebuses", "noun", "/ˈsiːbəsɪz/", "khỉ mũ thầy tu Nam Mỹ chi Cebus"),
    ("071013", "cephalopodas", "noun", "/ˌsɛfəˈlɒpədəz/", "lớp Chân đầu (bạch tuộc, mực)"),
    ("071014", "cheilitides", "noun", "/kaɪˈlaɪtɪˌdiːz/", "bệnh viêm sưng nứt môi"),
    ("071015", "chevres", "noun", "/ˈʃɛvrəz/", "phô mai sữa dê mềm Pháp chèvre"),
    ("071016", "chlamydes", "noun", "/ˈklæmɪdiːz/", "áo choàng ngắn Hy Lạp cổ; bao hoa"),
    ("071017", "chlamyses", "noun", "/ˈklæmɪsɪz/", "áo choàng ngắn Hy Lạp cổ chlamys"),
    ("071018", "chokepoints", "noun", "/ˈtʃoʊkˌpɔɪnts/", "điểm nghẽn cổ chai; nút thắt"),
    ("071019", "cimexes", "noun", "/ˈsaɪmɛksɪz/", "chi Rệp giường hút máu Cimex"),
    ("071020", "cimices", "noun", "/ˈsɪmɪsiːz/", "chi Rệp giường hút máu Cimex"),
    ("071021", "conspectuses", "noun", "/kənˈspɛktəsɪz/", "bản tóm tắt tổng quan đại cương"),
    ("071022", "coregonuses", "noun", "/ˌkɔːrɪˈɡoʊnəsɪz/", "chi Cá hồi trắng nước ngọt"),
    ("071023", "couths", "noun", "/kuːθs/", "sự lịch thiệp nhã nhặn (hiếm)"),
    ("071024", "cryptorchidisms", "noun", "/krɪpˈtɔːrkɪˌdɪzəmz/", "tật tinh hoàn ẩn chưa xuống bìu"),
    ("071025", "cyclopropanes", "noun", "/ˌsaɪkloʊˈproʊpeɪnz/", "hợp chất vòng xyclopropan (C3H6)"),
    ("071026", "cynaras", "noun", "/sɪˈnɛərəz/", "chi Actisô và cây cardoon Cynara"),
    ("071027", "delibeses", "noun", "/dəˈliːbz/", "nhà soạn nhạc Pháp Léo Delibes"),
    ("071028", "dowsers", "noun", "/ˈdaʊzərz/", "người dò mạch nước ngầm bằng que"),
    ("071029", "dukases", "noun", "/duːˈkɑːz/", "nhà soạn nhạc Pháp Paul Dukas"),
    ("071030", "ecchymoses", "noun", "/ˌɛkɪˈmoʊsiːz/", "vết bầm xuất huyết dưới da"),
    ("071031", "electrodepositions", "noun", "/ɪˌlɛktroʊdɛpəˈzɪʃənz/", "quá trình kết tủa mạ điện phân"),
    ("071032", "enculturations", "noun", "/ɪnˌkʌltʃəˈreɪʃənz/", "quá trình tiếp biến nhập văn hóa"),
    ("071033", "enneads", "noun", "/ˈɛniˌædz/", "nhóm chín người hoặc chín sự vật"),
    ("071034", "extraverts", "noun", "/ˈɛkstrəˌvɜːrts/", "người có tính cách hướng ngoại"),
    ("071035", "footpads", "noun", "/ˈfʊtˌpædz/", "cướp đường đi bộ; miếng đệm chân"),
    ("071036", "fugos", "noun", "/ˈfuːɡoʊz/", "bom khinh khí cầu Fu-Go Nhật Bản"),
    ("071037", "fumigants", "noun", "/ˈfjuːmɪɡənts/", "hóa chất xông khói diệt côn trùng"),
    ("071038", "funafutis", "noun", "/ˌfuːnɑːˈfuːtiz/", "thủ đô Funafuti của Tuvalu"),
    ("071039", "furfurals", "noun", "/ˈfɜːrfəˌrælz/", "dung môi hữu cơ furfural"),
    ("071040", "gastroscopies", "noun", "/ɡæˈstrɒskəpiz/", "thủ thuật nội soi dạ dày"),
    ("071041", "grievers", "noun", "/ˈɡriːvərz/", "người đau buồn thương tiếc"),
    ("071042", "groundbreakers", "noun", "/ˈɡraʊndˌbreɪkərz/", "người mở đường tiên phong sáng tạo"),
    ("071043", "hauliers", "noun", "/ˈhɔːliərz/", "nhà thầu vận tải chở hàng nặng"),
    ("071044", "hawkmoths", "noun", "/ˈhɔːkˌmɒθs/", "bướm đêm nhân sư bay lượn nhanh"),
    ("071045", "heliographed", "verb", "/ˈhiːliəˌɡræft/", "đã truyền tin bằng gương phản nắng"),
    ("071046", "heliographing", "verb", "/ˈhiːliəˌɡræfɪŋ/", "đang truyền tin bằng gương nắng"),
    ("071047", "hobbyhorses", "noun", "/ˈhɒbiˌhɔːrsɪz/", "ngựa gỗ trẻ em; chủ đề say mê"),
    ("071048", "ingatherings", "noun", "/ˈɪnˌɡæðərɪŋz/", "sự quy tụ thu hoạch mùa màng"),
    ("071049", "institutionalises", "verb", "/ˌɪnstɪˈtjuːʃənəˌlaɪzɪz/", "thể chế hóa; đưa vào trại (Anh)"),
    ("071050", "institutionalising", "verb", "/ˌɪnstɪˈtjuːʃənəˌlaɪzɪŋ/", "đang thể chế hóa; đưa vào viện"),
    ("071051", "interpellations", "noun", "/ɪnˌtɜːrpəˈleɪʃənz/", "chất vấn nghị trường; sự gán định"),
    ("071052", "involucra", "noun", "/ˌɪnvəˈluːkrə/", "tổng bao lá bắc cụm hoa; vỏ bọc"),
    ("071053", "involucres", "noun", "/ˈɪnvəˌluːkərz/", "tổng bao lá bắc quanh cụm hoa"),
    ("071054", "joliots", "noun", "/ʒoʊˈljoʊz/", "nhà vật lý Pháp Frédéric Joliot"),
    ("071055", "jowlier", "adj", "/ˈdʒaʊliər/", "má phính xệ hàm dưới hơn"),
    ("071056", "jowliest", "adj", "/ˈdʒaʊliɪst/", "má phính xệ hàm dưới nhất"),
    ("071057", "kalians", "noun", "/ˈkɑːliənz/", "điếu hút thuốc nước kiểu Ba Tư"),
    ("071058", "labetalols", "noun", "/ləˈbɛtəˌlɒlz/", "thuốc hạ huyết áp labetalol"),
    ("071059", "landlubbers", "noun", "/ˈlændˌlʌbərz/", "người sống trên cạn lạ lẫm đi biển"),
    ("071060", "lansoprazoles", "noun", "/lænˈsɒprəˌzoʊlz/", "thuốc giảm tiết axit lansoprazole"),
    ("071061", "layettes", "noun", "/leɪˈɛts/", "bộ đồ dùng cho trẻ sơ sinh"),
    ("071062", "leatherjackets", "noun", "/ˈlɛðərˌdʒækɪts/", "cá bò da; sâu bọ ăn rễ; áo da"),
    ("071063", "locaters", "noun", "/ˈloʊkeɪtərz/", "người hoặc thiết bị định vị vị trí"),
    ("071064", "lutras", "noun", "/ˈluːtrəz/", "chi Rái cá sông Á-Âu (Lutra)"),
    ("071065", "malaprops", "noun", "/ˈmæləˌprɒps/", "lỗi dùng nhầm từ giống âm hài hước"),
    ("071066", "micturitions", "noun", "/ˌmɪktʃəˈrɪʃənz/", "sự đi tiểu (thuật ngữ sinh lý)"),
    ("071067", "mirasols", "noun", "/ˈmɪrəˌsɒlz/", "hoa hướng dương cây bụi mirasol"),
    ("071068", "musths", "noun", "/mʌsts/", "cơn động dục hung hăng ở voi đực"),
    ("071069", "myricas", "noun", "/mɪˈraɪkəz/", "chi Cây thanh mai (dâu đất sáp)"),
    ("071070", "neuropteras", "noun", "/njʊˈrɒptərəz/", "bộ Cánh gân (chuồn chuồn cỏ)"),
    ("071071", "nothofaguses", "noun", "/ˌnɒθoʊˈfeɪɡəsɪz/", "cây dẻ gai phương Nam (Nothofagus)"),
    ("071072", "noumena", "noun", "/ˈnuːmɪnə/", "vật tự thân bản thể (triết Kant)"),
    ("071073", "noumenons", "noun", "/ˈnuːmɪnɒnz/", "vật tự thân bản thể (triết Kant)"),
    ("071074", "nurturances", "noun", "/ˈnɜːrtʃərənsɪz/", "sự chăm sóc nuôi dưỡng âu yếm"),
    ("071075", "oscans", "noun", "/ˈɒskənz/", "người và tiếng Oscan cổ ở Ý"),
    ("071076", "ouzels", "noun", "/ˈuːzəlz/", "chim hoét đen; chim lặn suối (cổ)"),
    ("071077", "paleoanthropologies", "noun", "/ˌpeɪlioʊænθrəˈpɒlədʒiz/", "ngành cổ nhân loại học"),
    ("071078", "peignoirs", "noun", "/ˈpeɪnwɑːrz/", "áo choàng ngủ mỏng của phụ nữ"),
    ("071079", "peterburgs", "noun", "/ˈpiːtərbɜːrɡz/", "thành phố Saint Petersburg (tên cũ)"),
    ("071080", "phycologies", "noun", "/faɪˈkɒlədʒiz/", "tảo học (ngành nghiên cứu rong tảo)"),
    ("071081", "pillagers", "noun", "/ˈpɪlɪdʒərz/", "kẻ cướp bóc cướp phá làng mạc"),
    ("071082", "pimentas", "noun", "/pɪˈmɛntəz/", "cây tiêu Jamaica (chi Pimenta)"),
    ("071083", "podocarpuses", "noun", "/ˌpɒdəˈkɑːrpəsɪz/", "cây thông tre thuộc chi Podocarpus"),
    ("071084", "pressburgs", "noun", "/ˈprɛsbɜːrɡz/", "thành phố Bratislava (tên Đức cổ)"),
    ("071085", "prizefights", "noun", "/ˈpraɪzˌfaɪts/", "trận đấu quyền Anh chuyên nghiệp"),
    ("071086", "prorations", "noun", "/proʊˈreɪʃənz/", "sự phân bổ tính toán theo tỷ lệ"),
    ("071087", "quaaludes", "noun", "/ˈkweɪluːdz/", "thuốc ngủ an thần Quaalude (Mỹ)"),
    ("071088", "quipus", "noun", "/ˈkiːpuːz/", "dây thắt nút ghi chép quipu Inca"),
    ("071089", "riatas", "noun", "/riˈɑːtəz/", "dây thòng lọng bện da bắt gia súc"),
    ("071090", "saxifrages", "noun", "/ˈsæksɪfrɪdʒɪz/", "cây tai hùm phá thạch (vườn đá)"),
    ("071091", "schutzstaffeln", "noun", "/ˈʃʊtsˌʃtɑːfəln/", "lực lượng vũ trang phát xít SS"),
    ("071092", "schutzstaffels", "noun", "/ˈʃʊtsˌʃtɑːfəlz/", "lực lượng vũ trang phát xít SS"),
    ("071093", "sergers", "noun", "/ˈsɜːrdʒərz/", "máy may vắt sổ mép vải (Mỹ)"),
    ("071094", "skivvied", "verb", "/ˈskɪvid/", "đã làm việc vặt tạp dịch (Anh)"),
    ("071095", "splitsvilles", "noun", "/ˈsplɪtsˌvɪlz/", "tình cảnh chia tay ly hôn (lóng)"),
    ("071096", "sploshed", "verb", "/splɒʃt/", "đã té nước văng tung tóe (khẩu ngữ)"),
    ("071097", "sploshes", "verb", "/ˈsplɒʃɪz/", "té nước văng tung tóe (khẩu ngữ)"),
    ("071098", "sploshing", "verb", "/ˈsplɒʃɪŋ/", "đang té nước văng tung tóe"),
    ("071099", "stickups", "noun", "/ˈstɪkˌʌps/", "vụ cướp chĩa súng đe dọa (lóng Mỹ)"),
    ("071100", "strugglers", "noun", "/ˈstrʌɡlərz/", "người vùng vẫy vật lộn khó khăn"),
    ("071101", "surds", "noun", "/sɜːrdz/", "căn vô tỷ (toán); âm vô thanh"),
    ("071102", "sybarites", "noun", "/ˈsɪbəˌraɪts/", "người đam mê hưởng lạc xa hoa"),
]

with open("scratch/b35_r03_raw_p1.json") as f:
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

with open("scratch/b35_r03_p1.json", "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print("Saved scratch/b35_r03_p1.json OK")
